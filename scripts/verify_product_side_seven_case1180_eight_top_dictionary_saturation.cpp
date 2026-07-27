#include "product_side_seven_cache_engine.hpp"
#include <set>

namespace {
constexpr int GLOBAL_CASE=1180;
constexpr int TOP_ORDER_COUNT=8;
constexpr uint64_t EXPECTED_DIGEST=3733902510478128199ULL;
const std::array<size_t,TOP_ORDER_COUNT> EXPECTED_DICTIONARY={{66,84,107,120,122,124,142,152}};

uint64_t mix64(uint64_t h,uint64_t v){h^=v;return h*1099511628211ULL;}

std::vector<int> state_edges(State const&s){
    std::vector<int> edges;
    for(int row=0;row<SIDE;++row){uint16_t mask=s[row];while(mask){int col=__builtin_ctz(unsigned(mask));mask&=uint16_t(mask-1);edges.push_back(SIDE*row+col);}}
    assert(edges.size()==28);return edges;
}

Point point_for_edge(int edge,Assignment const&top,std::array<int8_t,N>const&bottom){
    int row=edge/SIDE,col=edge%SIDE;
    return {row<N?row:N+bottom[row%N],N*(col/N)+top[col]};
}

std::array<uint8_t,3> first_bad_triple(State const&s,Assignment const&top,std::array<int8_t,N>const&bottom){
    auto edges=state_edges(s);
    for(size_t i=0;i<edges.size();++i)for(size_t j=i+1;j<edges.size();++j)for(size_t k=j+1;k<edges.size();++k){
        auto a=point_for_edge(edges[i],top,bottom),b=point_for_edge(edges[j],top,bottom),c=point_for_edge(edges[k],top,bottom);
        if(det(a,b,c)==0)return {uint8_t(edges[i]),uint8_t(edges[j]),uint8_t(edges[k])};
    }
    assert(false&&"surviving selector");return {};
}

void locate_case(std::vector<State>const&layer,Signature&signature,std::vector<State>&group){
    std::map<Signature,std::vector<State>>groups;
    for(auto const&state:layer){Signature sig{};for(int row=0;row<N;++row)sig[row]=state[row];groups[sig].push_back(state);}
    int index=0;
    for(auto const&[sig,g]:groups){if(g.size()!=4)continue;if(index==GLOBAL_CASE){signature=sig;group=g;std::sort(group.begin(),group.end());return;}++index;}
    assert(false&&"missing case");
}
}

int main(){
    auto layer=generate_layer();Signature signature{};std::vector<State>group;locate_case(layer,signature,group);
    TopEnumerator top;top.sig=signature;top.run(0);assert(top.solutions.size()>=TOP_ORDER_COUNT);
    std::set<std::array<uint8_t,3>>dictionary;uint64_t digest=1469598103934665603ULL;size_t obligations=0;
    for(int top_index=0;top_index<TOP_ORDER_COUNT;++top_index){
        auto const&assignment=top.solutions[top_index];digest=mix64(digest,top_index);for(auto value:assignment)digest=mix64(digest,uint8_t(value));
        std::array<int8_t,N>bottom{};for(int i=0;i<N;++i)bottom[i]=int8_t(i);
        do{
            for(int candidate=0;candidate<4;++candidate){auto triple=first_bad_triple(group[candidate],assignment,bottom);dictionary.insert(triple);for(auto edge:triple)digest=mix64(digest,edge);++obligations;}
        }while(std::next_permutation(bottom.begin(),bottom.end()));
        assert(dictionary.size()==EXPECTED_DICTIONARY[top_index]);
        std::cout<<"top_orders="<<(top_index+1)<<" dictionary="<<dictionary.size()<<" obligations="<<obligations<<" PASS\n";
    }
    assert(obligations==161280&&dictionary.size()==152&&digest==EXPECTED_DIGEST);
    constexpr size_t header_bytes=48,top_bytes=TOP_ORDER_COUNT*SIDE,record_bytes=TOP_ORDER_COUNT*5040*4;
    size_t compressed_bytes=header_bytes+top_bytes+dictionary.size()*3+record_bytes;
    assert(compressed_bytes==161896);
    std::cout<<"dictionary=152 obligations=161280 compressed_bytes=161896 raw_bytes=484288 digest="<<digest<<" PASS\n";
}

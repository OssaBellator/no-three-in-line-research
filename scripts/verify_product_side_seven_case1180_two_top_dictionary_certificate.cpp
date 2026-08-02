#include "product_side_seven_cache_engine.hpp"
#include <cstring>

namespace {
constexpr int GLOBAL_CASE=1180;
constexpr int ORIENTATION=0;
constexpr int TOP_ORDER_COUNT=2;
constexpr uint64_t EXPECTED_DIGEST=10705560690873782484ULL;

struct Header {
    char magic[8];
    uint32_t version;
    uint32_t global_case;
    uint32_t orientation;
    uint32_t top_order_count;
    uint32_t candidate_count;
    uint32_t permutation_count;
    uint32_t triple_count;
    uint64_t digest;
};

uint64_t mix64(uint64_t h,uint64_t v){h^=v;return h*1099511628211ULL;}

std::vector<int> state_edges(State const&s){
    std::vector<int> edges;
    for(int row=0;row<SIDE;++row){uint16_t mask=s[row];while(mask){int col=__builtin_ctz(unsigned(mask));mask&=uint16_t(mask-1);edges.push_back(SIDE*row+col);}}
    assert(edges.size()==28);return edges;
}

Point point_for_edge(int edge,Assignment const&top,std::array<int8_t,N>const&bottom){
    int row=edge/SIDE,col=edge%SIDE;
    int y=N*(col/N)+top[col];
    int x=row<N?row:N+bottom[row%N];
    return {x,y};
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

struct Proof {
    std::array<Assignment,TOP_ORDER_COUNT> top{};
    std::vector<std::array<uint8_t,3>> dictionary;
    std::vector<uint8_t> records;
    uint64_t digest=0;
};

Proof build(){
    auto layer=generate_layer();Signature signature{};std::vector<State>group;locate_case(layer,signature,group);
    TopEnumerator enumerator;enumerator.sig=signature;enumerator.run(0);assert(enumerator.solutions.size()>=TOP_ORDER_COUNT);
    Proof proof;std::map<std::array<uint8_t,3>,uint8_t>ids;uint64_t digest=1469598103934665603ULL;
    for(int ti=0;ti<TOP_ORDER_COUNT;++ti){
        proof.top[ti]=enumerator.solutions[ti];digest=mix64(digest,ti);for(auto v:proof.top[ti])digest=mix64(digest,uint8_t(v));
        std::array<int8_t,N>perm{};for(int i=0;i<N;++i)perm[i]=int8_t(i);uint32_t pi=0;
        do{
            digest=mix64(digest,pi++);for(auto v:perm)digest=mix64(digest,uint8_t(v));
            for(int candidate=0;candidate<4;++candidate){
                auto triple=first_bad_triple(group[candidate],proof.top[ti],perm);auto it=ids.find(triple);uint8_t id;
                if(it==ids.end()){id=uint8_t(proof.dictionary.size());assert(proof.dictionary.size()<255);proof.dictionary.push_back(triple);ids.emplace(triple,id);}else id=it->second;
                proof.records.push_back(id);digest=mix64(digest,candidate);for(auto e:triple)digest=mix64(digest,e);
            }
        }while(std::next_permutation(perm.begin(),perm.end()));
        assert(pi==5040);
    }
    assert(proof.dictionary.size()==84);assert(proof.records.size()==40320);assert(digest==EXPECTED_DIGEST);proof.digest=digest;return proof;
}

void write(std::string const&path,Proof const&proof){
    Header h{};std::memcpy(h.magic,"NTLDICT",7);h.version=1;h.global_case=GLOBAL_CASE;h.orientation=ORIENTATION;h.top_order_count=TOP_ORDER_COUNT;h.candidate_count=4;h.permutation_count=5040;h.triple_count=proof.dictionary.size();h.digest=proof.digest;
    std::ofstream out(path,std::ios::binary);assert(out);out.write((char*)&h,sizeof h);out.write((char*)proof.top.data(),sizeof(proof.top));out.write((char*)proof.dictionary.data(),proof.dictionary.size()*3);out.write((char*)proof.records.data(),proof.records.size());
    std::cout<<"generated top_orders="<<TOP_ORDER_COUNT<<" dictionary="<<proof.dictionary.size()<<" records="<<proof.records.size()<<" bytes="<<(sizeof h+sizeof(proof.top)+proof.dictionary.size()*3+proof.records.size())<<" digest="<<proof.digest<<"\n";
}

Proof read(std::string const&path){
    std::ifstream in(path,std::ios::binary);assert(in);Header h{};in.read((char*)&h,sizeof h);assert(std::memcmp(h.magic,"NTLDICT",7)==0&&h.version==1&&h.global_case==GLOBAL_CASE&&h.orientation==ORIENTATION&&h.top_order_count==TOP_ORDER_COUNT&&h.candidate_count==4&&h.permutation_count==5040&&h.triple_count==84&&h.digest==EXPECTED_DIGEST);
    Proof proof;proof.digest=h.digest;in.read((char*)proof.top.data(),sizeof(proof.top));proof.dictionary.resize(h.triple_count);in.read((char*)proof.dictionary.data(),proof.dictionary.size()*3);proof.records.resize(size_t(h.top_order_count)*h.permutation_count*h.candidate_count);in.read((char*)proof.records.data(),proof.records.size());char extra;assert(!in.read(&extra,1));return proof;
}

void check(Proof const&proof){
    auto layer=generate_layer();Signature signature{};std::vector<State>group;locate_case(layer,signature,group);
    TopEnumerator enumerator;enumerator.sig=signature;enumerator.run(0);assert(enumerator.solutions.size()>=TOP_ORDER_COUNT);
    uint64_t digest=1469598103934665603ULL;size_t cursor=0;
    for(int ti=0;ti<TOP_ORDER_COUNT;++ti){
        assert(proof.top[ti]==enumerator.solutions[ti]);digest=mix64(digest,ti);for(auto v:proof.top[ti])digest=mix64(digest,uint8_t(v));
        std::array<int8_t,N>perm{};for(int i=0;i<N;++i)perm[i]=int8_t(i);uint32_t pi=0;
        do{
            digest=mix64(digest,pi++);for(auto v:perm)digest=mix64(digest,uint8_t(v));
            for(int candidate=0;candidate<4;++candidate){
                uint8_t id=proof.records.at(cursor++);assert(id<proof.dictionary.size());auto triple=proof.dictionary[id];auto edges=state_edges(group[candidate]);for(auto e:triple)assert(std::binary_search(edges.begin(),edges.end(),int(e)));
                auto a=point_for_edge(triple[0],proof.top[ti],perm),b=point_for_edge(triple[1],proof.top[ti],perm),c=point_for_edge(triple[2],proof.top[ti],perm);assert(det(a,b,c)==0);
                digest=mix64(digest,candidate);for(auto e:triple)digest=mix64(digest,e);
            }
        }while(std::next_permutation(perm.begin(),perm.end()));
        assert(pi==5040);
    }
    assert(cursor==proof.records.size()&&proof.dictionary.size()==84&&digest==proof.digest&&digest==EXPECTED_DIGEST);
    std::cout<<"top_orders=2 permutations=10080 obligations=40320 dictionary=84 digest="<<digest<<" PASS\n";
}
}

int main(int argc,char**argv){assert(argc==3);std::string command=argv[1],path=argv[2];if(command=="generate"){auto proof=build();write(path,proof);check(proof);return 0;}assert(command=="check");auto proof=read(path);check(proof);return 0;}

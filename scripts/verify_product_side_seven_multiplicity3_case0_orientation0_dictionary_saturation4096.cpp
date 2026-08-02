#include "product_side_seven_cache_engine.hpp"
#include <set>

std::vector<int> m3_certificate4096_edges(State const& state) {
    std::vector<int> edges;
    for(int row=0;row<SIDE;++row) {
        uint16_t mask=state[row];
        while(mask) {
            int column=__builtin_ctz(unsigned(mask));
            mask&=uint16_t(mask-1);
            edges.push_back(SIDE*row+column);
        }
    }
    return edges;
}

Point m3_certificate4096_point(int edge,Assignment const& top,std::array<int8_t,N> const& bottom) {
    int row=edge/SIDE;
    int column=edge%SIDE;
    return {row<N ? row : N+bottom[row%N],N*(column/N)+top[column]};
}

std::array<uint8_t,3> m3_certificate4096_first_bad(State const& state,Assignment const& top,std::array<int8_t,N> const& bottom) {
    auto edges=m3_certificate4096_edges(state);
    for(size_t i=0;i<edges.size();++i)
        for(size_t j=i+1;j<edges.size();++j)
            for(size_t k=j+1;k<edges.size();++k)
                if(det(m3_certificate4096_point(edges[i],top,bottom),m3_certificate4096_point(edges[j],top,bottom),m3_certificate4096_point(edges[k],top,bottom))==0)
                    return {static_cast<uint8_t>(edges[i]),static_cast<uint8_t>(edges[j]),static_cast<uint8_t>(edges[k])};
    assert(false);
    return {};
}

uint64_t m3_saturation4096_mix(uint64_t hash,uint64_t value) {return (hash^value)*1099511628211ULL;}

int main() {
    auto layer=generate_layer();
    std::map<Signature,std::vector<State>> groups;
    for(auto const& state:layer) {Signature signature{};for(int row=0;row<N;++row) signature[row]=state[row];groups[signature].push_back(state);}

    Signature signature{};
    std::vector<State> group;
    int case_index=0;
    for(auto const& [candidate_signature,candidate_group]:groups) {
        if(candidate_group.size()!=3) continue;
        if(case_index==0) {signature=candidate_signature;group=candidate_group;std::sort(group.begin(),group.end());break;}
        ++case_index;
    }
    assert(case_index==0&&group.size()==3);

    TopEnumerator top;top.sig=signature;top.run(0);assert(top.solutions.size()>=4096);
    std::set<std::array<uint8_t,3>> dictionary;
    uint64_t digest=1469598103934665603ULL;
    size_t obligations=0;
    for(int top_index=0;top_index<4096;++top_index) {
        auto const& top_assignment=top.solutions[top_index];
        digest=m3_saturation4096_mix(digest,top_index);
        for(auto value:top_assignment) digest=m3_saturation4096_mix(digest,static_cast<uint8_t>(value));
        std::array<int8_t,N> bottom{};for(int value=0;value<N;++value) bottom[value]=static_cast<int8_t>(value);
        do {
            for(int selector=0;selector<3;++selector) {
                auto triple=m3_certificate4096_first_bad(group[selector],top_assignment,bottom);
                dictionary.insert(triple);
                for(auto edge:triple) digest=m3_saturation4096_mix(digest,edge);
                ++obligations;
            }
        } while(std::next_permutation(bottom.begin(),bottom.end()));
        if(top_index==127) assert(dictionary.size()==521);
        if(top_index==255) assert(dictionary.size()==601);
        if(top_index==383) assert(dictionary.size()==722);
        if(top_index==511) assert(dictionary.size()==781);
        if(top_index==767) assert(dictionary.size()==950);
        if(top_index==1023) assert(dictionary.size()==1028);
        if(top_index==1279) assert(dictionary.size()==1074);
        if(top_index==1535) assert(dictionary.size()==1148);
        if(top_index==1791) assert(dictionary.size()==1171);
        if(top_index==2047) assert(dictionary.size()==1202);
        if(top_index==2559) assert(dictionary.size()==1211);
        if(top_index==3071) assert(dictionary.size()==1223);
        if(top_index==3583) assert(dictionary.size()==1233);
        if(top_index==4095) assert(dictionary.size()==1258);
        std::cout<<"top_orders="<<(top_index+1)<<" dictionary="<<dictionary.size()<<" obligations="<<obligations<<" digest="<<digest<<"\n";
    }

    size_t projected_bytes=48+4096*14+dictionary.size()*3+obligations;
    size_t raw_bytes=48+4096*14+3*obligations;
    assert(dictionary.size()==1258);
    assert(obligations==61931520);
    assert(projected_bytes==61992686);
    assert(raw_bytes==185851952);
    assert(digest==13925271990529032304ULL);
    std::cout<<"FINAL dictionary="<<dictionary.size()<<" obligations="<<obligations<<" projected_bytes="<<projected_bytes<<" raw_bytes="<<raw_bytes<<" digest="<<digest<<" PASS\n";
    return 0;
}

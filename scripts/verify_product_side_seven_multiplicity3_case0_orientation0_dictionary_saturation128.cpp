#include "product_side_seven_cache_engine.hpp"
#include <set>

std::vector<int> m3_certificate128_edges(State const& state) {
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

Point m3_certificate128_point(int edge,Assignment const& top,std::array<int8_t,N> const& bottom) {
    int row=edge/SIDE;
    int column=edge%SIDE;
    return {row<N ? row : N+bottom[row%N],N*(column/N)+top[column]};
}

std::array<uint8_t,3> m3_certificate128_first_bad_triple(State const& state,Assignment const& top,std::array<int8_t,N> const& bottom) {
    auto edges=m3_certificate128_edges(state);
    for(size_t i=0;i<edges.size();++i)
        for(size_t j=i+1;j<edges.size();++j)
            for(size_t k=j+1;k<edges.size();++k)
                if(det(m3_certificate128_point(edges[i],top,bottom),m3_certificate128_point(edges[j],top,bottom),m3_certificate128_point(edges[k],top,bottom))==0)
                    return {static_cast<uint8_t>(edges[i]),static_cast<uint8_t>(edges[j]),static_cast<uint8_t>(edges[k])};
    assert(false);
    return {};
}

uint64_t m3_saturation128_mix(uint64_t hash,uint64_t value) {return (hash^value)*1099511628211ULL;}

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

    TopEnumerator top;top.sig=signature;top.run(0);assert(top.solutions.size()>=128);
    const std::array<size_t,128> expected_dictionary_sizes = {{
        59,65,76,80,91,104,124,125,
        130,134,135,137,165,170,178,189,
        190,201,204,206,207,212,212,214,
        217,224,225,226,233,234,238,241,
        241,241,244,247,247,256,256,258,
        263,263,263,266,266,266,267,267,
        267,267,267,267,267,267,267,267,
        267,267,268,268,273,280,282,283,
        284,287,290,292,292,293,294,294,
        363,371,378,383,387,389,392,393,
        395,395,396,397,400,401,403,403,
        403,403,404,404,405,405,405,405,
        440,453,456,461,465,466,488,491,
        497,497,498,499,500,500,500,500,
        500,500,504,512,514,514,515,515,
        516,516,518,518,518,519,519,521
    }};

    std::set<std::array<uint8_t,3>> dictionary;
    uint64_t digest=1469598103934665603ULL;
    size_t obligations=0;
    for(int top_index=0;top_index<128;++top_index) {
        auto const& top_assignment=top.solutions[top_index];
        digest=m3_saturation128_mix(digest,top_index);
        for(auto value:top_assignment) digest=m3_saturation128_mix(digest,static_cast<uint8_t>(value));
        std::array<int8_t,N> bottom{};for(int value=0;value<N;++value) bottom[value]=static_cast<int8_t>(value);
        do {
            for(int selector=0;selector<3;++selector) {
                auto triple=m3_certificate128_first_bad_triple(group[selector],top_assignment,bottom);
                dictionary.insert(triple);
                for(auto edge:triple) digest=m3_saturation128_mix(digest,edge);
                ++obligations;
            }
        } while(std::next_permutation(bottom.begin(),bottom.end()));
        assert(dictionary.size()==expected_dictionary_sizes[top_index]);
        assert(obligations==static_cast<size_t>(top_index+1)*15120);
        std::cout<<"top_orders="<<(top_index+1)<<" dictionary="<<dictionary.size()<<" obligations="<<obligations<<" digest="<<digest<<"\n";
    }

    size_t projected_bytes=48+128*14+dictionary.size()*3+obligations;
    assert(dictionary.size()==521);
    assert(obligations==1935360);
    assert(projected_bytes==1938763);
    assert(digest==13354808297163209304ULL);
    std::cout<<"FINAL dictionary="<<dictionary.size()<<" obligations="<<obligations<<" bytes="<<projected_bytes<<" digest="<<digest<<" PASS\n";
    return 0;
}

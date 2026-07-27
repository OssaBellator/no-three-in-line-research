#include "product_side_seven_cache_engine.hpp"
#include <set>

std::vector<int> certificate_edges(State const& state) {
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

Point certificate_point(
    int edge,
    Assignment const& top,
    std::array<int8_t,N> const& bottom
) {
    int row=edge/SIDE;
    int column=edge%SIDE;
    return {
        row<N ? row : N+bottom[row%N],
        N*(column/N)+top[column]
    };
}

std::array<uint8_t,3> first_bad_triple(
    State const& state,
    Assignment const& top,
    std::array<int8_t,N> const& bottom
) {
    auto edges=certificate_edges(state);
    for(size_t i=0;i<edges.size();++i)
        for(size_t j=i+1;j<edges.size();++j)
            for(size_t k=j+1;k<edges.size();++k)
                if(det(
                    certificate_point(edges[i],top,bottom),
                    certificate_point(edges[j],top,bottom),
                    certificate_point(edges[k],top,bottom)
                )==0)
                    return {
                        static_cast<uint8_t>(edges[i]),
                        static_cast<uint8_t>(edges[j]),
                        static_cast<uint8_t>(edges[k])
                    };
    assert(false);
    return {};
}

uint64_t saturation_mix(uint64_t hash,uint64_t value) {
    hash^=value;
    return hash*1099511628211ULL;
}

int main() {
    auto layer=generate_layer();
    std::map<Signature,std::vector<State>> groups;
    for(auto const& state:layer) {
        Signature signature{};
        for(int row=0;row<N;++row) signature[row]=state[row];
        groups[signature].push_back(state);
    }

    Signature signature{};
    std::vector<State> group;
    int case_index=0;
    for(auto const& [candidate_signature,candidate_group]:groups) {
        if(candidate_group.size()!=4) continue;
        if(case_index==1180) {
            signature=candidate_signature;
            group=candidate_group;
            std::sort(group.begin(),group.end());
            break;
        }
        ++case_index;
    }
    assert(case_index==1180);
    assert(group.size()==4);

    TopEnumerator top;
    top.sig=signature;
    top.run(0);
    assert(top.solutions.size()>=32);

    const std::array<size_t,32> expected_dictionary_sizes = {{
        66,84,107,120,122,124,142,152,
        234,253,277,281,303,320,324,331,
        336,341,344,346,352,356,357,357,
        358,358,361,361,361,363,363,363
    }};

    std::set<std::array<uint8_t,3>> dictionary;
    uint64_t digest=1469598103934665603ULL;
    size_t obligations=0;

    for(int top_index=0;top_index<32;++top_index) {
        auto const& top_assignment=top.solutions[top_index];
        digest=saturation_mix(digest,top_index);
        for(auto value:top_assignment)
            digest=saturation_mix(digest,static_cast<uint8_t>(value));

        std::array<int8_t,N> bottom{};
        for(int value=0;value<N;++value) bottom[value]=static_cast<int8_t>(value);
        do {
            for(int selector=0;selector<4;++selector) {
                auto triple=first_bad_triple(group[selector],top_assignment,bottom);
                dictionary.insert(triple);
                for(auto edge:triple) digest=saturation_mix(digest,edge);
                ++obligations;
            }
        } while(std::next_permutation(bottom.begin(),bottom.end()));

        assert(dictionary.size()==expected_dictionary_sizes[top_index]);
        assert(obligations==static_cast<size_t>(top_index+1)*20160);
        std::cout<<"top_orders="<<(top_index+1)
                 <<" dictionary="<<dictionary.size()
                 <<" obligations="<<obligations
                 <<" digest="<<digest<<"\n";
    }

    size_t projected_bytes=48+32*14+dictionary.size()*3+obligations;
    assert(dictionary.size()==363);
    assert(obligations==645120);
    assert(projected_bytes==646705);
    assert(digest==6386682151196533169ULL);
    std::cout<<"FINAL dictionary="<<dictionary.size()
             <<" obligations="<<obligations
             <<" bytes="<<projected_bytes
             <<" digest="<<digest<<" PASS\n";
    return 0;
}

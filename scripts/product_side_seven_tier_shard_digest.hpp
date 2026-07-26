#pragma once
#include "product_side_seven_cache_engine.hpp"

struct TierShardDigestExpectations {
    int multiplicity;
    int signature_count;
    int first_case;
    int case_count;
    std::array<uint64_t,2> top_orders;
    std::array<uint64_t,2> top_nodes;
    std::array<uint64_t,4> bottom_nodes;
    uint64_t transcript_digest;
};

inline uint64_t tier_shard_digest_mix(uint64_t hash,uint64_t value) {
    hash ^= value;
    return hash * 1099511628211ULL;
}

inline int verify_tier_shard_digest(
    int argc,
    char** argv,
    TierShardDigestExpectations const& expected
) {
    int requested_case=argc>1?std::stoi(argv[1]):-1;
    int requested_orientation=argc>2?std::stoi(argv[2]):-1;
    assert(requested_case<expected.signature_count);
    assert(requested_orientation<4);
    if(requested_case>=0) {
        assert(requested_case>=expected.first_case);
        assert(requested_case<expected.first_case+expected.case_count);
    }

    auto layer=generate_layer();
    std::map<Signature,std::vector<State>> groups;
    std::map<int,int> histogram;
    for(auto const& state:layer) {
        Signature signature{};
        for(int row=0;row<N;++row) signature[row]=state[row];
        groups[signature].push_back(state);
    }
    for(auto const& [signature,group]:groups)
        ++histogram[static_cast<int>(group.size())];
    assert(histogram[expected.multiplicity]==expected.signature_count);

    uint64_t digest=1469598103934665603ULL;
    std::array<uint64_t,2> aggregate_top_orders{};
    std::array<uint64_t,2> aggregate_top_nodes{};
    std::array<uint64_t,4> aggregate_bottom_nodes{};
    int case_index=0;
    int checked=0;

    for(auto const& [signature,unsorted_group]:groups) {
        if(static_cast<int>(unsorted_group.size())!=expected.multiplicity) continue;
        bool in_shard=case_index>=expected.first_case
            && case_index<expected.first_case+expected.case_count;
        bool selected=in_shard && (requested_case<0||requested_case==case_index);
        if(selected) {
            auto group=unsorted_group;
            std::sort(group.begin(),group.end());
            TopEnumerator top[2];
            for(int mode=0;mode<2;++mode) {
                top[mode].sig=signature;
                top[mode].run(mode);
            }
            BottomGroupSolver solver;
            solver.initialize(group);
            std::array<uint64_t,4> bottom_nodes{};
            for(int orientation=0;orientation<4;++orientation) {
                if(requested_orientation>=0&&requested_orientation!=orientation) continue;
                auto const& solutions=top[orientation%2].solutions;
                for(auto const& assignment:solutions) {
                    assert(!solver.solve_top(assignment,orientation));
                    bottom_nodes[orientation]+=solver.nodes;
                }
            }
            if(requested_orientation<0) {
                digest=tier_shard_digest_mix(digest,case_index);
                for(auto value:signature) digest=tier_shard_digest_mix(digest,value);
                for(int mode=0;mode<2;++mode) {
                    digest=tier_shard_digest_mix(digest,top[mode].solutions.size());
                    aggregate_top_orders[mode]+=top[mode].solutions.size();
                }
                for(int mode=0;mode<2;++mode) {
                    digest=tier_shard_digest_mix(digest,top[mode].nodes);
                    aggregate_top_nodes[mode]+=top[mode].nodes;
                }
                for(int orientation=0;orientation<4;++orientation) {
                    digest=tier_shard_digest_mix(digest,bottom_nodes[orientation]);
                    aggregate_bottom_nodes[orientation]+=bottom_nodes[orientation];
                }
            }
            std::cout<<"case="<<case_index<<" signature=";
            print_sig(signature);
            std::cout<<" top_orders="<<top[0].solutions.size()<<","<<top[1].solutions.size()
                     <<" top_nodes="<<top[0].nodes<<","<<top[1].nodes
                     <<" bottom_nodes="<<bottom_nodes[0]<<","<<bottom_nodes[1]<<","<<bottom_nodes[2]<<","<<bottom_nodes[3]
                     <<" PASS\n";
            ++checked;
        }
        ++case_index;
    }
    assert(case_index==expected.signature_count);
    if(requested_case<0) assert(checked==expected.case_count);
    if(requested_case<0&&requested_orientation<0) {
        assert(aggregate_top_orders==expected.top_orders);
        assert(aggregate_top_nodes==expected.top_nodes);
        assert(aggregate_bottom_nodes==expected.bottom_nodes);
        assert(digest==expected.transcript_digest);
        uint64_t total=0;
        for(auto value:aggregate_bottom_nodes) total+=value;
        std::cout<<"transcript_digest="<<digest
                 <<" aggregate_bottom_nodes="<<total<<" PASS\n";
    }
    return 0;
}

#include "product_side_seven_cache_engine.hpp"

static uint64_t mix(uint64_t h,uint64_t value) {
    h ^= value;
    return h * 1099511628211ULL;
}

int main(int argc,char** argv) {
    int requested_case=argc>1?std::stoi(argv[1]):-1;
    int requested_orientation=argc>2?std::stoi(argv[2]):-1;
    assert(requested_case<277);
    assert(requested_orientation<4);

    auto layer=generate_layer();
    std::map<Signature,std::vector<State>> groups;
    std::map<int,int> histogram;
    for(auto const& state:layer) {
        Signature signature{};
        for(int row=0;row<N;++row) signature[row]=state[row];
        groups[signature].push_back(state);
    }
    for(auto const& [signature,group]:groups) ++histogram[static_cast<int>(group.size())];
    assert(histogram[8]==277);

    uint64_t digest=1469598103934665603ULL;
    std::array<uint64_t,2> aggregate_top_orders{};
    std::array<uint64_t,2> aggregate_top_nodes{};
    std::array<uint64_t,4> aggregate_bottom_nodes{};
    int case_index=0;

    for(auto const& [signature,unsorted_group]:groups) {
        if(unsorted_group.size()!=8) continue;
        const bool selected=requested_case<0||requested_case==case_index;
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
                digest=mix(digest,case_index);
                for(auto value:signature) digest=mix(digest,value);
                for(int mode=0;mode<2;++mode) {
                    digest=mix(digest,top[mode].solutions.size());
                    aggregate_top_orders[mode]+=top[mode].solutions.size();
                }
                for(int mode=0;mode<2;++mode) {
                    digest=mix(digest,top[mode].nodes);
                    aggregate_top_nodes[mode]+=top[mode].nodes;
                }
                for(int orientation=0;orientation<4;++orientation) {
                    digest=mix(digest,bottom_nodes[orientation]);
                    aggregate_bottom_nodes[orientation]+=bottom_nodes[orientation];
                }
            }
            std::cout<<"case="<<case_index<<" signature=";
            print_sig(signature);
            std::cout<<" top_orders="<<top[0].solutions.size()<<","<<top[1].solutions.size()
                     <<" top_nodes="<<top[0].nodes<<","<<top[1].nodes
                     <<" bottom_nodes="<<bottom_nodes[0]<<","<<bottom_nodes[1]<<","<<bottom_nodes[2]<<","<<bottom_nodes[3]
                     <<" PASS\n";
        }
        ++case_index;
    }
    assert(case_index==277);
    if(requested_case<0&&requested_orientation<0) {
        assert((aggregate_top_orders==std::array<uint64_t,2>{{11957408ULL,10852546ULL}}));
        assert((aggregate_top_nodes==std::array<uint64_t,2>{{80982232ULL,75065004ULL}}));
        assert((aggregate_bottom_nodes==std::array<uint64_t,4>{{22373701ULL,20809483ULL,22353455ULL,19251567ULL}}));
        assert(digest==5710772046139185874ULL);
        std::cout<<"transcript_digest="<<digest<<" aggregate_bottom_nodes=84788206 PASS\n";
    }
}

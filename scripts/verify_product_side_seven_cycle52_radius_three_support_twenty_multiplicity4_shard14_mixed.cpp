#include "product_side_seven_cache_engine.hpp"

namespace {
constexpr int FIRST_CASE=1380;
constexpr int CASE_COUNT=100;
constexpr int WITNESS_CASE=1392;
constexpr int WITNESS_ORIENTATION=1;
constexpr int WITNESS_TOP_INDEX=6928;
constexpr int WITNESS_CANDIDATE=0;
constexpr uint64_t EXPECTED_DIGEST=6967282382830852367ULL;
const std::array<uint64_t,2> EXPECTED_TOP_ORDERS={{4690759ULL,3076808ULL}};
const std::array<uint64_t,2> EXPECTED_TOP_NODES={{41015945ULL,28518404ULL}};
const std::array<uint64_t,4> EXPECTED_BOTTOM_NODES={{8433604ULL,5303866ULL,8122042ULL,4943386ULL}};
const std::array<uint64_t,4> WITNESS_REJECTED_SUBSET_NODES={{13204ULL,37288ULL,14478ULL,25145ULL}};
const Signature WITNESS_SIGNATURE={{257,514,1028,2056,17,96,4160}};
const Assignment WITNESS_TOP={{2,3,5,6,1,4,0,4,3,1,0,5,2,6}};
const std::array<int8_t,N> WITNESS_BOTTOM={{6,5,4,3,2,0,1}};
const State WITNESS_STATE={{257,514,1028,2056,17,96,4160,130,260,520,1040,2176,8224,12288}};

uint64_t mix(uint64_t h,uint64_t value){h^=value;return h*1099511628211ULL;}
void print_signature(Signature const&s){std::cout<<"(";for(int i=0;i<N;++i){if(i)std::cout<<",";std::cout<<s[i];}std::cout<<")";}

bool is_permutation7(std::array<int8_t,N>const&a){uint8_t seen=0;for(auto v:a){if(v<0||v>=N||(seen&(1u<<v)))return false;seen|=uint8_t(1u<<v);}return seen==127;}
bool top_blocks_are_permutations(Assignment const&a){for(int block=0;block<2;++block){uint8_t seen=0;for(int c=block*N;c<(block+1)*N;++c){int v=a[c];if(v<0||v>=N||(seen&(1u<<v)))return false;seen|=uint8_t(1u<<v);}if(seen!=127)return false;}return true;}

Point witness_point(int edge){
    int row=edge/SIDE,col=edge%SIDE;
    int y=2*WITNESS_TOP[col]+col/N;
    int x=row<N?row:N+WITNESS_BOTTOM[row%N];
    return {x,y};
}

void verify_witness(){
    assert(top_blocks_are_permutations(WITNESS_TOP));assert(is_permutation7(WITNESS_BOTTOM));
    std::vector<Point>points;
    for(int row=0;row<SIDE;++row){uint16_t mask=WITNESS_STATE[row];assert(__builtin_popcount(unsigned(mask))==2);while(mask){int col=__builtin_ctz(unsigned(mask));mask&=uint16_t(mask-1);points.push_back(witness_point(SIDE*row+col));}}
    assert(points.size()==28);
    for(size_t i=0;i<points.size();++i)for(size_t j=i+1;j<points.size();++j){assert(points[i].x!=points[j].x||points[i].y!=points[j].y);for(size_t k=j+1;k<points.size();++k)assert(det(points[i],points[j],points[k])!=0);}
}
}

int main(int argc,char**argv){
    int requested_case=argc>1?std::stoi(argv[1]):-1;
    if(requested_case>=0)assert(requested_case>=FIRST_CASE&&requested_case<FIRST_CASE+CASE_COUNT);
    auto layer=generate_layer();std::map<Signature,std::vector<State>>groups;std::map<int,int>histogram;
    for(auto const&state:layer){Signature signature{};for(int row=0;row<N;++row)signature[row]=state[row];groups[signature].push_back(state);}
    for(auto const&[signature,group]:groups)++histogram[int(group.size())];assert(histogram[4]==2392);
    uint64_t digest=1469598103934665603ULL;std::array<uint64_t,2>aggregate_top_orders{};std::array<uint64_t,2>aggregate_top_nodes{};std::array<uint64_t,4>aggregate_bottom_nodes{};
    int case_index=0,checked=0,rejected=0,witnessed=0;
    for(auto const&[signature,unsorted_group]:groups){
        if(unsorted_group.size()!=4)continue;
        if(case_index>=FIRST_CASE&&case_index<FIRST_CASE+CASE_COUNT&&(requested_case<0||requested_case==case_index)){
            auto group=unsorted_group;std::sort(group.begin(),group.end());TopEnumerator top[2];for(int mode=0;mode<2;++mode){top[mode].sig=signature;top[mode].run(mode);aggregate_top_orders[mode]+=top[mode].solutions.size();aggregate_top_nodes[mode]+=top[mode].nodes;}
            digest=mix(digest,case_index);for(auto value:signature)digest=mix(digest,value);for(int mode=0;mode<2;++mode)digest=mix(digest,top[mode].solutions.size());for(int mode=0;mode<2;++mode)digest=mix(digest,top[mode].nodes);
            std::array<uint64_t,4>bottom_nodes{};
            if(case_index!=WITNESS_CASE){
                digest=mix(digest,0);BottomGroupSolver solver;solver.initialize(group);
                for(int orientation=0;orientation<4;++orientation){for(auto const&assignment:top[orientation%2].solutions){assert(!solver.solve_top(assignment,orientation));bottom_nodes[orientation]+=solver.nodes;}digest=mix(digest,bottom_nodes[orientation]);aggregate_bottom_nodes[orientation]+=bottom_nodes[orientation];}
                rejected+=4;
            }else{
                assert(signature==WITNESS_SIGNATURE&&group[WITNESS_CANDIDATE]==WITNESS_STATE);assert(top[1].solutions.size()>WITNESS_TOP_INDEX&&top[1].solutions[WITNESS_TOP_INDEX]==WITNESS_TOP);verify_witness();
                std::vector<State>rejected_group={group[1],group[2],group[3]};BottomGroupSolver solver;solver.initialize(rejected_group);
                for(int orientation=0;orientation<4;++orientation){for(auto const&assignment:top[orientation%2].solutions){assert(!solver.solve_top(assignment,orientation));bottom_nodes[orientation]+=solver.nodes;}assert(bottom_nodes[orientation]==WITNESS_REJECTED_SUBSET_NODES[orientation]);aggregate_bottom_nodes[orientation]+=bottom_nodes[orientation];}
                digest=mix(digest,1);for(auto value:bottom_nodes)digest=mix(digest,value);for(auto value:std::array<uint64_t,5>{{3,1,WITNESS_ORIENTATION,WITNESS_CANDIDATE,WITNESS_TOP_INDEX}})digest=mix(digest,value);for(auto value:WITNESS_TOP)digest=mix(digest,uint8_t(value));for(auto value:WITNESS_BOTTOM)digest=mix(digest,uint8_t(value));for(auto value:WITNESS_STATE)digest=mix(digest,value);
                rejected+=3;++witnessed;
            }
            std::cout<<"case="<<case_index<<" signature=";print_signature(signature);std::cout<<" top_orders="<<top[0].solutions.size()<<","<<top[1].solutions.size()<<" top_nodes="<<top[0].nodes<<","<<top[1].nodes<<" bottom_nodes="<<bottom_nodes[0]<<","<<bottom_nodes[1]<<","<<bottom_nodes[2]<<","<<bottom_nodes[3]<<" status="<<(case_index==WITNESS_CASE?"MIXED_WITNESS":"INFEASIBLE")<<" PASS\n";++checked;
        }
        ++case_index;
    }
    assert(case_index==2392);
    uint64_t total=0;for(auto value:aggregate_bottom_nodes)total+=value;
    if(requested_case<0){
        assert(checked==CASE_COUNT&&rejected==399&&witnessed==1);assert(aggregate_top_orders==EXPECTED_TOP_ORDERS);assert(aggregate_top_nodes==EXPECTED_TOP_NODES);assert(aggregate_bottom_nodes==EXPECTED_BOTTOM_NODES);assert(digest==EXPECTED_DIGEST);
        std::cout<<"transcript_digest="<<digest<<" rejected=399 witnessed=1 aggregate_bottom_nodes="<<total<<" PASS\n";
    }else{
        assert(checked==1);std::cout<<"selected_case="<<requested_case<<" rejected="<<rejected<<" witnessed="<<witnessed<<" aggregate_bottom_nodes="<<total<<" PASS\n";
    }
}

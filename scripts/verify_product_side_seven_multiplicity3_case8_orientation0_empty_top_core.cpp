#include "product_side_seven_cache_engine.hpp"

namespace {
constexpr int GLOBAL_CASE=8;
const Assignment FULL_TOP={{0,1,6,3,2,5,4,2,0,4,3,5,1,6}};
const std::array<uint64_t,14> EXPECTED_ORDERS={{1,1,1,1,4,6,14,14,32,144,262,744,4644,34516}};
const std::array<uint64_t,14> EXPECTED_TOP_NODES={{2,3,4,7,22,69,147,148,504,1586,3656,11024,62978,123339}};
const std::array<uint64_t,14> EXPECTED_BOTTOM_NODES={{2,2,2,2,6,11,22,22,43,241,424,1147,7881,52388}};

struct AssumptionTopEnumerator {
    Signature signature{};
    Assignment assignment{};
    std::array<uint8_t,2> used{};
    std::vector<Assignment> solutions;
    uint64_t nodes=0;
    bool clean_partial() const {
        std::array<Point,14> points{}; int count=0;
        for(int row=0;row<N;++row){uint16_t mask=signature[row];while(mask){int column=__builtin_ctz(unsigned(mask));mask&=uint16_t(mask-1);if(assignment[column]>=0)points[count++]={row,N*(column/N)+assignment[column]};}}
        for(int i=0;i<count;++i)for(int j=i+1;j<count;++j)for(int k=j+1;k<count;++k)if(det(points[i],points[j],points[k])==0)return false;
        return true;
    }
    void dfs(int depth){
        ++nodes; if(depth==SIDE){solutions.push_back(assignment);return;}
        int best=-1,best_size=8,domain_size=0; std::array<int8_t,N> best_domain{};
        for(int variable=0;variable<SIDE;++variable) if(assignment[variable]<0){
            int block=variable/N,size=0; std::array<int8_t,N> domain{};
            for(int value=0;value<N;++value) if(!((used[block]>>value)&1u)){assignment[variable]=int8_t(value);if(clean_partial())domain[size++]=int8_t(value);assignment[variable]=-1;}
            if(size==0)return; if(size<best_size){best_size=size;best=variable;domain_size=size;best_domain=domain;}
        }
        int block=best/N;
        for(int i=0;i<domain_size;++i){int value=best_domain[i];assignment[best]=int8_t(value);used[block]|=uint8_t(1u<<value);dfs(depth+1);used[block]&=uint8_t(~(1u<<value));assignment[best]=-1;}
    }
    void run(Signature const&sig,uint16_t keep_mask){
        signature=sig;assignment.fill(-1);used.fill(0);solutions.clear();nodes=0;int depth=0;
        for(int column=0;column<SIDE;++column) if((keep_mask>>column)&1u){int value=FULL_TOP[column],block=column/N;assert(!((used[block]>>value)&1u));assignment[column]=int8_t(value);used[block]|=uint8_t(1u<<value);++depth;}
        assert(clean_partial());dfs(depth);
    }
};

void locate_case(std::vector<State>const&layer,Signature&signature,std::vector<State>&group){
    std::map<Signature,std::vector<State>> groups;
    for(auto const&state:layer){Signature sig{};for(int row=0;row<N;++row)sig[row]=state[row];groups[sig].push_back(state);}
    int index=0;
    for(auto const&[sig,g]:groups){if(g.size()!=3)continue;if(index==GLOBAL_CASE){signature=sig;group=g;std::sort(group.begin(),group.end());return;}++index;}
    assert(false&&"missing case");
}
}

int main(){
    auto layer=generate_layer(); Signature signature{}; std::vector<State> group; locate_case(layer,signature,group);
    TopEnumerator ordinary; ordinary.sig=signature; ordinary.run(0); assert(!ordinary.solutions.empty()&&ordinary.solutions.front()==FULL_TOP);
    uint16_t keep_mask=(1u<<SIDE)-1u;
    for(int removed=0;removed<SIDE;++removed){
        keep_mask&=uint16_t(~(1u<<removed)); AssumptionTopEnumerator top; top.run(signature,keep_mask); BottomGroupSolver solver; solver.initialize(group); uint64_t bottom_nodes=0;
        for(auto const&assignment:top.solutions){assert(!solver.solve_top(assignment,0));bottom_nodes+=solver.nodes;}
        assert(top.solutions.size()==EXPECTED_ORDERS[removed]);assert(top.nodes==EXPECTED_TOP_NODES[removed]);assert(bottom_nodes==EXPECTED_BOTTOM_NODES[removed]);
        std::cout<<"removed_through="<<removed<<" retained="<<__builtin_popcount(unsigned(keep_mask))<<" top_orders="<<top.solutions.size()<<" top_nodes="<<top.nodes<<" bottom_nodes="<<bottom_nodes<<" PASS\n";
    }
    assert(keep_mask==0);
    std::cout<<"empty_top_assumption_core top_orders=34516 top_nodes=123339 bottom_nodes=52388 PASS\n";
}

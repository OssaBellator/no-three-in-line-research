// Generic exact radius-three support-range coordinate search.
// Reuse the selector, alternating-cycle, and dangerous-point CSP implementation
// from the radius-two range search, renaming only its command-line entry point.
#define main radius_two_range_search_entry
#include "search_product_side_seven_radius_two_support.cpp"
#undef main

int main(int argc,char**argv){
 assert(argc==5);
 std::string requested=argv[1];
 int support=std::stoi(argv[2]);
 int first=std::stoi(argv[3]);
 int last=std::stoi(argv[4]);
 for(auto&data:C)if(requested==data.name){
  Selector root=centre(data);
  E enumerator;
  enumerator.s=root;
  enumerator.h=host(data);
  enumerator.run();
  assert((int)enumerator.ns.size()==data.n1);
  auto radius_one=enumerator.ns;
  std::unordered_set<Selector,Hash> radius_two;
  for(auto const&parent:radius_one){
   enumerator.s=parent;
   enumerator.run();
   for(auto const&child:enumerator.ns){
    if(child!=root&&!radius_one.count(child))radius_two.insert(child);
   }
  }
  std::set<Selector> layer;
  for(auto const&parent:radius_two){
   enumerator.s=parent;
   enumerator.run();
   for(auto const&child:enumerator.ns){
    if(child==root||radius_one.count(child)||radius_two.count(child))continue;
    int difference=0;
    for(int row=0;row<14;++row){
     difference+=__builtin_popcount(child[row]^root[row]);
    }
    if(difference==support)layer.insert(child);
   }
  }
  std::cerr<<data.name<<" radius3 support="<<support
           <<" layer="<<layer.size()<<"\n";
  std::uint64_t nodes=0;
  int index=0;
  int tested=0;
  for(auto const&selector:layer){
   ++index;
   if(index<first||index>last)continue;
   ++tested;
   for(int orientation=0;orientation<4;++orientation){
    CSP solver;
    bool feasible=solver.solve(selector,orientation);
    nodes+=solver.nodes;
    if(feasible){
     std::cout<<"FOUND "<<data.name<<" radius3 index="<<index
              <<" orientation="<<orientation<<" nodes="<<nodes
              <<" selector=";
     for(auto row:selector)std::cout<<row<<",";
     std::cout<<"\n";
     return 2;
    }
   }
  }
  std::cout<<data.name<<" radius3 range="<<first<<"-"<<last
           <<" done="<<tested<<" nodes="<<nodes<<" NO\n";
  return 0;
 }
 assert(false&&"unknown side-seven class");
}

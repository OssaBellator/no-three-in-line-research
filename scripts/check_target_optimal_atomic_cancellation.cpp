#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;

struct Point { int x,y; };
long long cross(Point a, Point b, Point c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);} 
array<Point,4> orbit_block(int m,int s,int t,int e){int n=2*m; auto J=[n](int x){return n-1-x;}; Point q0{s,e?J(t):t}; Point q1{J(s),e?t:J(t)}; return {q0,q1,Point{J(q0.y),q0.x},Point{J(q1.y),q1.x}};}
int pair_atomic(int m,int sa,int ta,int ea,int sb,int tb,int eb){auto a=orbit_block(m,sa,ta,ea), b=orbit_block(m,sb,tb,eb); array<Point,8> p{}; array<int,8> o{}; for(int i=0;i<4;++i){p[i]=a[i];p[i+4]=b[i];o[i]=0;o[i+4]=1;} int z=0; for(int i=0;i<8;++i)for(int j=i+1;j<8;++j)for(int k=j+1;k<8;++k){if(o[i]==o[j]&&o[j]==o[k])continue; z+=cross(p[i],p[j],p[k])==0;} return z;}
int triple_atomic(int m,int sa,int ta,int ea,int sb,int tb,int eb,int sc,int tc,int ec){auto a=orbit_block(m,sa,ta,ea),b=orbit_block(m,sb,tb,eb),c=orbit_block(m,sc,tc,ec);int z=0;for(auto x:a)for(auto y:b)for(auto w:c)z+=cross(x,y,w)==0;return z;}

struct Geometry {
 int m; size_t six; vector<int8_t> rel; vector<uint8_t> pc,tc;
 explicit Geometry(int M):m(M),six((size_t)m*m*m*m*m*m),rel((size_t)m*m*m*m,0),pc((size_t)m*m*m*m*4,0),tc(six*8,0){
  for(int a=0;a<m;++a)for(int ta=0;ta<m;++ta){if(ta==a)continue;for(int b=a+1;b<m;++b)for(int tb=0;tb<m;++tb){if(tb==b||tb==ta)continue;auto id=i4(a,ta,b,tb);for(int ea=0;ea<2;++ea)for(int eb=0;eb<2;++eb)pc[id*4+ea*2+eb]=(uint8_t)pair_atomic(m,a,ta,ea,b,tb,eb);bool be=pc[id*4]>0, bu=pc[id*4+1]>0;rel[id]=be&&bu?3:be?2:bu?1:0;}}
  for(int a=0;a<m;++a)for(int ta=0;ta<m;++ta){if(ta==a)continue;for(int b=a+1;b<m;++b)for(int tb=0;tb<m;++tb){if(tb==b||tb==ta)continue;for(int c=b+1;c<m;++c)for(int tc0=0;tc0<m;++tc0){if(tc0==c||tc0==ta||tc0==tb)continue;auto id=i6(a,ta,b,tb,c,tc0);for(int mask=0;mask<8;++mask)tc[id*8+mask]=(uint8_t)triple_atomic(m,a,ta,mask&1,b,tb,(mask>>1)&1,c,tc0,(mask>>2)&1);}}}
 }
 size_t i4(int a,int ta,int b,int tb)const{return ((size_t(a)*m+ta)*m+b)*m+tb;}
 size_t i6(int a,int ta,int b,int tb,int c,int tc0)const{return (((((size_t(a)*m+ta)*m+b)*m+tb)*m+c)*m+tc0);}
 int relation(int a,int ta,int b,int tb)const{return rel[i4(a,ta,b,tb)];}
 int pairc(int a,int ta,int ea,int b,int tb,int eb)const{return pc[i4(a,ta,b,tb)*4+ea*2+eb];}
 int triplec(int a,int ta,int ea,int b,int tb,int eb,int c,int tc0,int ec)const{return tc[i6(a,ta,b,tb,c,tc0)*8+ea+2*eb+4*ec];}
};

struct Constraint{int a,b,x;};
struct Info{bool safe=false;int lambda=-1;};
uint64_t encode(const vector<int>&r){uint64_t x=0;for(int t:r)x=(x<<4)|t;return x;}
vector<int> switched(const vector<int>&r,array<int,3>s){array<int,3> cyc{};int f=0,cur=*min_element(s.begin(),s.end());for(int k=0;k<(int)r.size();++k){if(cur==s[0]||cur==s[1]||cur==s[2])cyc[f++]=cur;cur=r[cur];}vector<int>o=r;o[cyc[0]]=r[cyc[1]];o[cyc[1]]=r[cyc[2]];o[cyc[2]]=r[cyc[0]];return o;}

struct CaseResult{
 long long positive_optimal_states=0;
 long long one_step_obstructions=0;
 long long resolved_distance2=0;
 long long resolved_distance3=0;
 long long unresolved_before_parity_clean=0;
 map<int,long long> unresolved_by_lambda;
 map<int,long long> resolved_barrier_distribution;
 map<int,long long> unresolved_best_excess_distribution;
 int max_minimum_barrier=0;
};

CaseResult run_case(int m){
 Geometry g(m); int O=1<<m;
 vector<vector<int>> cycles; vector<int>tail(m-1);iota(tail.begin(),tail.end(),1);do{vector<int>ord(m);ord[0]=0;for(int i=1;i<m;++i)ord[i]=tail[i-1];vector<int>r(m);for(int i=0;i<m;++i)r[ord[i]]=ord[(i+1)%m];cycles.push_back(move(r));}while(next_permutation(tail.begin(),tail.end()));
 unordered_map<uint64_t,int> idx;idx.reserve(cycles.size()*2);for(int i=0;i<(int)cycles.size();++i)idx[encode(cycles[i])]=i;
 vector<Info> info(cycles.size()); vector<uint8_t> optimal((size_t)cycles.size()*O,0);
 for(int ci=0;ci<(int)cycles.size();++ci){vector<Constraint> es;bool safe=true;for(int a=0;a<m&&safe;++a)for(int b=a+1;b<m;++b){int v=g.relation(a,cycles[ci][a],b,cycles[ci][b]);if(v==3){safe=false;break;}if(v)es.push_back({a,b,v==1?0:1});}if(!safe)continue;info[ci].safe=true;int best=es.size();for(int e=0;e<O;++e){int bad=0;for(auto q:es)bad+=((((e>>q.a)&1)^((e>>q.b)&1))!=q.x);if(bad<best){best=bad;for(int x=0;x<O;++x)optimal[(size_t)ci*O+x]=0;}if(bad==best)optimal[(size_t)ci*O+e]=1;}info[ci].lambda=best;}
 vector<array<int,3>> triples;for(int a=0;a<m;++a)for(int b=a+1;b<m;++b)for(int c=b+1;c<m;++c)triples.push_back({a,b,c});
 vector<vector<int>> lower(cycles.size());for(int s=0;s<(int)cycles.size();++s){if(!info[s].safe||info[s].lambda==0)continue;for(auto T:triples){int t=idx.at(encode(switched(cycles[s],T)));if(info[t].safe&&info[t].lambda<info[s].lambda)lower[s].push_back(t);}}
 vector<int16_t> zcache((size_t)cycles.size()*O,-1);
 auto z=[&](int ci,int e){int16_t &v=zcache[(size_t)ci*O+e];if(v>=0)return (int)v;int total=0;for(int a=0;a<m;++a)for(int b=a+1;b<m;++b)total+=g.pairc(a,cycles[ci][a],(e>>a)&1,b,cycles[ci][b],(e>>b)&1);for(int a=0;a<m;++a)for(int b=a+1;b<m;++b)for(int c=b+1;c<m;++c)total+=g.triplec(a,cycles[ci][a],(e>>a)&1,b,cycles[ci][b],(e>>b)&1,c,cycles[ci][c],(e>>c)&1);v=(int16_t)total;return total;};
 CaseResult R;
 for(int s=0;s<(int)cycles.size();++s){if(!info[s].safe||info[s].lambda==0)continue;for(int e=0;e<O;++e){if(!optimal[(size_t)s*O+e])continue;++R.positive_optimal_states;int sourceZ=z(s,e);vector<int> first;for(int t:lower[s])if(optimal[(size_t)t*O+e])first.push_back(t);bool one=false;for(int t:first)if(z(t,e)<sourceZ){one=true;break;}if(one)continue;++R.one_step_obstructions;
   int bestDist=99,bestBarrier=numeric_limits<int>::max(),bestReach=numeric_limits<int>::max();
   struct Node{int c,d,maxz;}; vector<Node> stack;for(int t:first)stack.push_back({t,1,max(sourceZ,z(t,e))});
   while(!stack.empty()){auto cur=stack.back();stack.pop_back();int zc=z(cur.c,e);bestReach=min(bestReach,zc);if(zc<sourceZ){if(cur.d<bestDist||(cur.d==bestDist&&cur.maxz-sourceZ<bestBarrier)){bestDist=cur.d;bestBarrier=cur.maxz-sourceZ;}continue;}for(int t:lower[cur.c])if(optimal[(size_t)t*O+e])stack.push_back({t,cur.d+1,max(cur.maxz,z(t,e))});}
   if(bestDist==2)++R.resolved_distance2;else if(bestDist==3)++R.resolved_distance3;else{++R.unresolved_before_parity_clean;R.unresolved_by_lambda[info[s].lambda]++;R.unresolved_best_excess_distribution[bestReach-sourceZ]++;}
   if(bestDist<99){R.resolved_barrier_distribution[bestBarrier]++;R.max_minimum_barrier=max(R.max_minimum_barrier,bestBarrier);} 
 }}
 return R;
}

bool equal_map(const map<int,long long>&a,const map<int,long long>&b){return a==b;}
struct Expected { long long positive, one, d2, d3, unresolved; int maxbar; map<int,long long> by_lambda, barriers, excess; };
const array<Expected,5> expected={{
 {48,14,0,0,14,0,{{1,14}},{},{{0,12},{4,2}}},
 {272,0,0,0,0,0,{},{},{}},
 {2752,170,0,0,170,0,{{1,170}},{},{{0,128},{4,40},{8,2}}},
 {93980,4308,122,0,4186,16,{{1,4170},{2,16}},{{0,60},{4,30},{8,24},{12,4},{16,4}},{{0,3102},{4,888},{8,178},{12,16},{16,2}}},
 {977312,26164,270,0,25894,28,{{1,25862},{2,32}},{{0,124},{4,76},{8,40},{12,14},{16,6},{20,4},{24,4},{28,2}},{{0,19240},{4,5554},{8,944},{12,140},{16,14},{20,2}}}
}};
void print_map(const map<int,long long>&x){cout<<"{";bool first=true;for(auto [k,v]:x){if(!first)cout<<",";first=false;cout<<"\""<<k<<"\":"<<v;}cout<<"}";}
int main(){
 cout<<"{\n  \"cases\": [\n";
 for(int m=5;m<=9;++m){
  auto r=run_case(m);const auto&e=expected[m-5];
  bool ok=r.positive_optimal_states==e.positive&&r.one_step_obstructions==e.one&&r.resolved_distance2==e.d2&&r.resolved_distance3==e.d3&&r.unresolved_before_parity_clean==e.unresolved&&r.max_minimum_barrier==e.maxbar&&equal_map(r.unresolved_by_lambda,e.by_lambda)&&equal_map(r.resolved_barrier_distribution,e.barriers)&&equal_map(r.unresolved_best_excess_distribution,e.excess);
  if(!ok){cerr<<"cancellation ledger mismatch at m="<<m<<"\n";return 3;}
  cout<<"    {\"m\":"<<m
      <<",\"positive_optimal_states\":"<<r.positive_optimal_states
      <<",\"one_step_total_atomic_obstructions\":"<<r.one_step_obstructions
      <<",\"resolved_at_distance_two\":"<<r.resolved_distance2
      <<",\"resolved_at_distance_three\":"<<r.resolved_distance3
      <<",\"unresolved_before_parity_clean\":"<<r.unresolved_before_parity_clean
      <<",\"maximum_minimum_temporary_atomic_excess\":"<<r.max_minimum_barrier
      <<",\"unresolved_by_source_frustration\":";print_map(r.unresolved_by_lambda);
  cout<<",\"resolved_minimum_barrier_distribution\":";print_map(r.resolved_barrier_distribution);
  cout<<",\"unresolved_best_reachable_excess_distribution\":";print_map(r.unresolved_best_excess_distribution);
  cout<<"}"<<(m<9?",":"")<<"\n";
 }
 cout<<"  ],\n  \"target_optimal_fixed_sign_paths_only\": true,\n  \"third_step_only_cancellation_states\": 0,\n  \"asymptotic_cancellation_theorem_proved\": false\n}\n";
}

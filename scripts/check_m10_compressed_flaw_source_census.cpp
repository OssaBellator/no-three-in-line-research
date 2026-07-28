#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <tuple>
#include <unordered_map>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;
constexpr int M=10,Q=1<<M;
using Rho=array<uint8_t,M>;
struct Point{int x,y;};
struct RH{size_t operator()(Rho const&r)const noexcept{size_t h=0;for(auto x:r)h=h*17+x+1;return h;}};
long long cross(Point a,Point b,Point c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
array<Point,4> block(int s,int t,int e){auto J=[](int x){return 2*M-1-x;};Point q0{s,e?J(t):t},q1{J(s),e?t:J(t)};return {q0,q1,Point{J(q0.y),q0.x},Point{J(q1.y),q1.x}};}
bool pair_bad(int a,int ta,int ea,int b,int tb,int eb){auto A=block(a,ta,ea),B=block(b,tb,eb);array<Point,8>p{};for(int i=0;i<4;i++){p[i]=A[i];p[i+4]=B[i];}for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)if(cross(p[i],p[j],p[k])==0)return true;return false;}
bool triple_bad(int a,int ta,int ea,int b,int tb,int eb,int c,int tc,int ec){auto A=block(a,ta,ea),B=block(b,tb,eb),C=block(c,tc,ec);for(auto x:A)for(auto y:B)for(auto z:C)if(cross(x,y,z)==0)return true;return false;}
vector<Rho> cycles(){vector<Rho>out;array<int,M-1>tail{};iota(tail.begin(),tail.end(),1);do{array<int,M>ord{};ord[0]=0;for(int i=1;i<M;i++)ord[i]=tail[i-1];Rho r{};for(int i=0;i<M;i++)r[ord[i]]=ord[(i+1)%M];out.push_back(r);}while(next_permutation(tail.begin(),tail.end()));return out;}
struct Info{bool clean=false;uint8_t components=0;array<int8_t,M>comp{},colour{};};
struct Candidate{uint16_t s;uint8_t ta,tb,tc,mask;};
struct Best{long long supply=0;int sources=0;Candidate c{};};
bool better(Best const&a,Best const&b){
  if(a.supply!=b.supply) return a.supply>b.supply;
  return tie(a.c.s,a.c.ta,a.c.tb,a.c.tc,a.c.mask)<
         tie(b.c.s,b.c.ta,b.c.tb,b.c.tc,b.c.mask);
}
int main(){
  vector<array<int,3>> triples;for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)for(int c=b+1;c<M;c++)triples.push_back({a,b,c});int K=triples.size();
  static int8_t rel[M][M][M][M];
  for(int a=0;a<M;a++)for(int ta=0;ta<M;ta++)if(a!=ta)for(int b=a+1;b<M;b++)for(int tb=0;tb<M;tb++)if(b!=tb&&ta!=tb){bool eq=pair_bad(a,ta,0,b,tb,0),un=pair_bad(a,ta,0,b,tb,1);rel[a][ta][b][tb]=eq&&un?3:eq?2:un?1:0;}
  auto rhos=cycles();int C=rhos.size();vector<Info>info(C);long long cleanStates=0;int cleanCycles=0;
  for(int ci=0;ci<C;ci++){
    int8_t adj[M][M];for(int i=0;i<M;i++)for(int j=0;j<M;j++)adj[i][j]=-1;bool impossible=false;
    for(int a=0;a<M&&!impossible;a++)for(int b=a+1;b<M;b++){int v=rel[a][rhos[ci][a]][b][rhos[ci][b]];if(v==3){impossible=true;break;}if(v){int p=v==1?0:1;adj[a][b]=adj[b][a]=p;}}
    if(impossible) continue;
    Info in;
    in.comp.fill(-1);
    in.colour.fill(-1);
    bool ok=true;
    int cc=0;
    for(int root=0;root<M;root++)if(in.comp[root]<0){array<int,M>q{};int h=0,z=0;q[z++]=root;in.comp[root]=cc;in.colour[root]=0;while(h<z){int u=q[h++];for(int v=0;v<M;v++)if(adj[u][v]>=0){int want=in.colour[u]^adj[u][v];if(in.comp[v]<0){in.comp[v]=cc;in.colour[v]=want;q[z++]=v;}else if(in.colour[v]!=want)ok=false;}}cc++;}
    if(ok){in.clean=true;in.components=cc;info[ci]=in;cleanCycles++;cleanStates+=1LL<<cc;}
  }
  auto key=[](int s,int ta,int tb,int tc){return ((s*M+ta)*M+tb)*M+tc;};
  vector<vector<int>> lists(K*M*M*M);
  for(int ci=0;ci<C;ci++)for(int s=0;s<K;s++){auto S=triples[s];lists[key(s,rhos[ci][S[0]],rhos[ci][S[1]],rhos[ci][S[2]])].push_back(ci);}
  int maxRaw=0;long long nonemptyArcKeys=0;for(auto const&v:lists)if(!v.empty()){nonemptyArcKeys++;maxRaw=max(maxRaw,(int)v.size());}
  vector<Candidate> cand;cand.reserve(100000);
  for(int s=0;s<K;s++){auto S=triples[s];for(int ta=0;ta<M;ta++)for(int tb=0;tb<M;tb++)for(int tc=0;tc<M;tc++){if(lists[key(s,ta,tb,tc)].empty())continue;for(int mask=0;mask<4;mask++)if(triple_bad(S[0],ta,mask&1,S[1],tb,(mask>>1)&1,S[2],tc,0))cand.push_back({(uint16_t)s,(uint8_t)ta,(uint8_t)tb,(uint8_t)tc,(uint8_t)mask});}}
  int threads=1;
#ifdef _OPENMP
  threads=omp_get_max_threads();
#endif
  struct Acc{long long flaws=0,incidences=0,supply=0;int maxSources=0;array<long long,721>hist{};Best best;};
  vector<Acc> acc(threads);
#pragma omp parallel for schedule(dynamic,32)
  for(int ix=0;ix<(int)cand.size();ix++){
    int tid=0;
#ifdef _OPENMP
    tid=omp_get_thread_num();
#endif
    auto c=cand[ix];auto S=triples[c.s];auto const&raw=lists[key(c.s,c.ta,c.tb,c.tc)];int ns=0;long long supply=0;
    for(int ci:raw){if(!info[ci].clean)continue;array<int8_t,M>root;root.fill(-1);bool ok=true;int distinct=0;for(int k=0;k<3;k++){int owner=S[k],co=info[ci].comp[owner],value=((c.mask>>k)&1)^info[ci].colour[owner];if(root[co]<0){root[co]=value;distinct++;}else if(root[co]!=value)ok=false;}if(ok){ns++;supply+=1LL<<(info[ci].components-distinct);}}
    if(!ns) continue;
    auto &a=acc[tid];
    a.flaws+=2;
    a.incidences+=2LL*ns;
    a.supply+=2*supply;
    a.maxSources=max(a.maxSources,ns);
    a.hist[ns]+=2;
    Best candidateBest{supply,ns,c};
    if(better(candidateBest,a.best)) a.best=candidateBest;
  }
  Acc total;for(auto const&a:acc){total.flaws+=a.flaws;total.incidences+=a.incidences;total.supply+=a.supply;total.maxSources=max(total.maxSources,a.maxSources);for(int i=0;i<=720;i++)total.hist[i]+=a.hist[i];if(better(a.best,total.best)) total.best=a.best;}
  int minSources=0;
  for(int i=1;i<=720;i++) if(total.hist[i]){minSources=i;break;}
  auto quantile=[&](long long numerator,long long denominator){
    long long threshold=(total.flaws*numerator+denominator-1)/denominator;
    long long cumulative=0;
    for(int i=1;i<=720;i++){
      cumulative+=total.hist[i];
      if(cumulative>=threshold) return i;
    }
    return 720;
  };
  bool ok=C==362880&&cleanCycles==297886&&cleanStates==115586396&&
    nonemptyArcKeys==60480&&maxRaw==720&&cand.size()==24762&&
    total.flaws==47512&&minSources==106&&total.maxSources==720&&
    total.incidences==27939188&&total.supply==1485249312&&
    total.best.supply==65256&&total.best.sources==720&&total.hist[720]==412&&
    quantile(1,4)==545&&quantile(1,2)==612&&quantile(3,4)==658&&
    quantile(9,10)==687&&quantile(99,100)==718;
  if(!ok){cerr<<"m10 compressed source regression mismatch\n";return 2;}
  auto B=total.best.c;auto S=triples[B.s];
  cout<<"{\n  \"m\":10,\n  \"hamilton_cycles\":"<<C<<",\n  \"parity_satisfiable_cycles\":"<<cleanCycles<<",\n  \"clean_signed_states\":"<<cleanStates<<",\n  \"nonempty_three_arc_keys\":"<<nonemptyArcKeys<<",\n  \"maximum_raw_source_cycles_per_arc_assignment\":"<<maxRaw<<",\n  \"complement_reduced_geometric_candidates\":"<<cand.size()<<",\n  \"atomic_signed_assignment_flaws_with_clean_sources\":"<<total.flaws<<",\n  \"compatible_source_cycles_range\":["<<minSources<<","<<total.maxSources<<"],\n  \"compatible_source_cycle_quantiles\":{\"25_percent\":"<<quantile(1,4)<<",\"median\":"<<quantile(1,2)<<",\"75_percent\":"<<quantile(3,4)<<",\"90_percent\":"<<quantile(9,10)<<",\"99_percent\":"<<quantile(99,100)<<"},\n  \"flaws_with_all_720_source_cycles\":"<<total.hist[720]<<",\n  \"total_flaw_source_cycle_incidences\":"<<total.incidences<<",\n  \"total_flaw_source_signed_weight\":"<<total.supply<<",\n  \"maximum_single_flaw_source_signed_weight\":"<<total.best.supply<<",\n  \"maximum_weight_flaw_source_cycles\":"<<total.best.sources<<",\n  \"maximum_weight_flaw_source_owners\":["<<S[0]<<","<<S[1]<<","<<S[2]<<"],\n  \"maximum_weight_flaw_targets\":["<<int(B.ta)<<","<<int(B.tb)<<","<<int(B.tc)<<"],\n  \"maximum_weight_flaw_orientations\":["<<int(B.mask&1)<<","<<int((B.mask>>1)&1)<<",0],\n  \"three_arc_factorial_compression_verified\":true,\n  \"full_weighted_hall_mincuts_completed\":false\n}\n";
}

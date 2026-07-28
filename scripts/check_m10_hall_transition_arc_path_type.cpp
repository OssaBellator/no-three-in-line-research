#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <climits>
#include <tuple>
#include <unordered_map>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
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
struct FlowEdge{int to,rev;long long cap;};
struct Dinic{
  vector<vector<FlowEdge>> g;vector<int> level,it;
  explicit Dinic(int n):g(n),level(n),it(n){}
  void add(int u,int v,long long c){FlowEdge a{v,(int)g[v].size(),c},b{u,(int)g[u].size(),0};g[u].push_back(a);g[v].push_back(b);}
  bool bfs(int s,int t){fill(level.begin(),level.end(),-1);queue<int>q;level[s]=0;q.push(s);while(!q.empty()){int u=q.front();q.pop();for(auto const&e:g[u])if(e.cap>0&&level[e.to]<0){level[e.to]=level[u]+1;q.push(e.to);}}return level[t]>=0;}
  long long dfs(int u,int t,long long f){if(u==t)return f;for(int &i=it[u];i<(int)g[u].size();i++){auto &e=g[u][i];if(e.cap>0&&level[e.to]==level[u]+1){long long z=dfs(e.to,t,min(f,e.cap));if(z){e.cap-=z;g[e.to][e.rev].cap+=z;return z;}}}return 0;}
  long long flow(int s,int t){long long ans=0;while(bfs(s,t)){fill(it.begin(),it.end(),0);while(long long z=dfs(s,t,LLONG_MAX/4))ans+=z;}return ans;}
  vector<char> side(int s)const{vector<char>seen(g.size());queue<int>q;seen[s]=1;q.push(s);while(!q.empty()){int u=q.front();q.pop();for(auto const&e:g[u])if(e.cap>0&&!seen[e.to]){seen[e.to]=1;q.push(e.to);}}return seen;}
};
struct Ratio{long long p=0,q=1;int subset=0;long long supply=0,capacity=1;int cuts=1;};
Ratio optimum_ratio(vector<int>const&w,vector<vector<int>>const&nbr,vector<int>const&tids,vector<int>const&caps,vector<int>&pos){
 int nx=w.size(),ny=tids.size();for(int j=0;j<ny;j++)pos[tids[j]]=j;
 long long as=accumulate(w.begin(),w.end(),0LL),ac=accumulate(caps.begin(),caps.end(),0LL),d=gcd(as,ac),p=as/d,q=ac/d;int last=nx;long long ls=as,lc=ac;int cuts=1;
 for(;;){cuts++;int S=nx+ny,T=S+1;Dinic F(T+1);long long inf=LLONG_MAX/8,total=0;for(int i=0;i<nx;i++){long long c=q*w[i];F.add(S,i,c);total+=c;for(int y:nbr[i])F.add(i,nx+pos[y],inf);}for(int j=0;j<ny;j++)F.add(nx+j,T,p*caps[j]);long long gain=total-F.flow(S,T);if(!gain){for(int y:tids)pos[y]=-1;return {p,q,last,ls,lc,cuts};}auto side=F.side(S);vector<char>used(ny);long long ss=0,cc=0;int sub=0;for(int i=0;i<nx;i++)if(side[i]){ss+=w[i];sub++;for(int y:nbr[i])used[pos[y]]=1;}for(int j=0;j<ny;j++)if(used[j])cc+=caps[j];d=gcd(ss,cc);p=ss/d;q=cc/d;last=sub;ls=ss;lc=cc;}
}

struct Best{long long supply=0;int sources=0;Candidate c{};};
bool better(Best const&a,Best const&b){
  if(a.supply!=b.supply) return a.supply>b.supply;
  return tie(a.c.s,a.c.ta,a.c.tb,a.c.tc,a.c.mask)<
         tie(b.c.s,b.c.ta,b.c.tb,b.c.tc,b.c.mask);
}
int arc_path_components(Candidate const&c, vector<array<int,3>> const&triples){
  array<int,M> parent{}; iota(parent.begin(),parent.end(),0);
  auto find=[&](auto&& self,int x)->int{return parent[x]==x?x:parent[x]=self(self,parent[x]);};
  auto join=[&](int a,int b){a=find(find,a);b=find(find,b);if(a!=b)parent[b]=a;};
  auto S=triples[c.s]; array<int,3> T{c.ta,c.tb,c.tc};
  for(int k=0;k<3;k++) join(S[k],T[k]);
  array<int,3> roots{}; for(int k=0;k<3;k++) roots[k]=find(find,S[k]);
  sort(roots.begin(),roots.end());
  return int(unique(roots.begin(),roots.end())-roots.begin());
}
const char* arc_path_type(int components){
  return components==1?"three_edge_path":components==2?"two_edge_path_plus_arc":"three_disjoint_arcs";
}
int main(int argc,char**argv){
  int band_lo=650,band_hi=720;if(argc>1)band_lo=atoi(argv[1]);if(argc>2)band_hi=atoi(argv[2]);
  vector<array<int,3>> triples;for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)for(int c=b+1;c<M;c++)triples.push_back({a,b,c});int K=triples.size();
  static int8_t rel[M][M][M][M];
  for(int a=0;a<M;a++)for(int ta=0;ta<M;ta++)if(a!=ta)for(int b=a+1;b<M;b++)for(int tb=0;tb<M;tb++)if(b!=tb&&ta!=tb){bool eq=pair_bad(a,ta,0,b,tb,0),un=pair_bad(a,ta,0,b,tb,1);rel[a][ta][b][tb]=eq&&un?3:eq?2:un?1:0;}
  auto rhos=cycles();int C=rhos.size();unordered_map<Rho,int,RH>id;id.reserve(C*2);for(int i=0;i<C;i++)id[rhos[i]]=i;vector<Info>info(C);long long cleanStates=0;int cleanCycles=0;
  for(int ci=0;ci<C;ci++){
    int8_t adj[M][M];for(int i=0;i<M;i++)for(int j=0;j<M;j++)adj[i][j]=-1;bool impossible=false;
    for(int a=0;a<M&&!impossible;a++)for(int b=a+1;b<M;b++){int v=rel[a][rhos[ci][a]][b][rhos[ci][b]];if(v==3){impossible=true;break;}if(v){int p=v==1?0:1;adj[a][b]=adj[b][a]=p;}}
    if(impossible) continue;
    Info in;in.comp.fill(-1);in.colour.fill(-1);bool ok=true;int cc=0;
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
    auto &a=acc[tid];a.flaws+=2;a.incidences+=2LL*ns;a.supply+=2*supply;a.maxSources=max(a.maxSources,ns);a.hist[ns]+=2;Best candidateBest{supply,ns,c};if(better(candidateBest,a.best))a.best=candidateBest;
  }
  Acc total;for(auto const&a:acc){total.flaws+=a.flaws;total.incidences+=a.incidences;total.supply+=a.supply;total.maxSources=max(total.maxSources,a.maxSources);for(int i=0;i<=720;i++)total.hist[i]+=a.hist[i];if(better(a.best,total.best))total.best=a.best;}
  int minSources=0;for(int i=1;i<=720;i++)if(total.hist[i]){minSources=i;break;}
  auto quantile=[&](long long numerator,long long denominator){long long threshold=(total.flaws*numerator+denominator-1)/denominator,cumulative=0;for(int i=1;i<=720;i++){cumulative+=total.hist[i];if(cumulative>=threshold)return i;}return 720;};

  struct TrancheAcc{long long flaws=0,proper=0;long long wp=0,wq=1,gp=0,gq=1,pp=1,pq=1;int maxCuts=0,wSources=0,wSubset=0;long long wSupply=0,wCapacity=1;Candidate worst{};};
  struct TypeAcc{long long flaws=0,violations=0;long long np=0,nq=1;int sourceCount=0;Candidate worst{};};
  auto fracgt=[](long long a,long long b,long long c,long long d){return boost::multiprecision::int128_t(a)*d>boost::multiprecision::int128_t(c)*b;};
  vector<char> meet(K*K,0);for(int s=0;s<K;s++)for(int t=0;t<K;t++)for(int a:triples[s])for(int b:triples[t])if(a==b)meet[s*K+t]=1;
  vector<array<TrancheAcc,721>> tracc(threads);vector<array<TypeAcc,3>> tyacc(threads);vector<vector<int>> positions(threads,vector<int>(C,-1));
#pragma omp parallel for schedule(dynamic,1)
  for(int ix=0;ix<(int)cand.size();ix++){
    int tid=0;
#ifdef _OPENMP
    tid=omp_get_thread_num();
#endif
    auto c=cand[ix];auto S=triples[c.s];auto const&raw=lists[key(c.s,c.ta,c.tb,c.tc)];vector<int>sources,weights;sources.reserve(720);weights.reserve(720);
    for(int ci:raw){if(!info[ci].clean)continue;array<int8_t,M>root;root.fill(-1);bool okc=true;int distinct=0;for(int k=0;k<3;k++){int owner=S[k],co=info[ci].comp[owner],value=((c.mask>>k)&1)^info[ci].colour[owner];if(root[co]<0){root[co]=value;distinct++;}else if(root[co]!=value)okc=false;}if(okc){sources.push_back(ci);weights.push_back(1<<(info[ci].components-distinct));}}
    if((int)sources.size()<band_lo||(int)sources.size()>band_hi)continue;
    vector<vector<int>>nbr(sources.size());vector<int>all;all.reserve(61200);
    for(int i=0;i<(int)sources.size();i++){auto &v=nbr[i];v.reserve(85);for(int t=0;t<K;t++)if(meet[c.s*K+t]){Rho rr=rhos[sources[i]];auto T=triples[t];array<int,3>cyc{};int f=0,cur=min({T[0],T[1],T[2]});for(int z=0;z<M;z++){if(cur==T[0]||cur==T[1]||cur==T[2])cyc[f++]=cur;cur=rr[cur];}Rho o=rr;o[cyc[0]]=rr[cyc[1]];o[cyc[1]]=rr[cyc[2]];o[cyc[2]]=rr[cyc[0]];int y=id[o];if(info[y].clean)v.push_back(y);}sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());all.insert(all.end(),v.begin(),v.end());}
    sort(all.begin(),all.end());all.erase(unique(all.begin(),all.end()),all.end());vector<int>caps;caps.reserve(all.size());for(int y:all)caps.push_back(1<<info[y].components);Ratio r=optimum_ratio(weights,nbr,all,caps,positions[tid]);
    long long gs=accumulate(weights.begin(),weights.end(),0LL),gc=accumulate(caps.begin(),caps.end(),0LL),d=gcd(gs,gc),gp=gs/d,gq=gc/d;
    auto &a=tracc[tid][sources.size()];a.flaws+=2;a.maxCuts=max(a.maxCuts,r.cuts);if(fracgt(r.p,r.q,a.wp,a.wq)){a.wp=r.p;a.wq=r.q;a.worst=c;a.wSources=sources.size();a.wSubset=r.subset;a.wSupply=r.supply;a.wCapacity=r.capacity;}if(fracgt(gp,gq,a.gp,a.gq)){a.gp=gp;a.gq=gq;}if(fracgt(r.p,r.q,gp,gq)){a.proper+=2;long long pp=r.p*gq,pq=r.q*gp;d=gcd(pp,pq);pp/=d;pq/=d;if(fracgt(pp,pq,a.pp,a.pq)){a.pp=pp;a.pq=pq;}}
    int typeIndex=arc_path_components(c,triples)-1;auto &ta=tyacc[tid][typeIndex];ta.flaws+=2;long long normP=(long long)sources.size()*r.p,normQ=r.q;if(normP>normQ)ta.violations+=2;if(fracgt(normP,normQ,ta.np,ta.nq)){ta.np=normP;ta.nq=normQ;ta.sourceCount=sources.size();ta.worst=c;}
  }
  array<TrancheAcc,721> per{};TrancheAcc tranche;
  for(int sc=band_lo;sc<=band_hi;sc++)for(int tid=0;tid<threads;tid++){auto const&a=tracc[tid][sc];auto &z=per[sc];z.flaws+=a.flaws;z.proper+=a.proper;z.maxCuts=max(z.maxCuts,a.maxCuts);if(fracgt(a.wp,a.wq,z.wp,z.wq)){z.wp=a.wp;z.wq=a.wq;z.worst=a.worst;z.wSources=a.wSources;z.wSubset=a.wSubset;z.wSupply=a.wSupply;z.wCapacity=a.wCapacity;}if(fracgt(a.gp,a.gq,z.gp,z.gq)){z.gp=a.gp;z.gq=a.gq;}if(fracgt(a.pp,a.pq,z.pp,z.pq)){z.pp=a.pp;z.pq=a.pq;}}
  for(int sc=band_lo;sc<=band_hi;sc++){auto const&a=per[sc];tranche.flaws+=a.flaws;tranche.proper+=a.proper;tranche.maxCuts=max(tranche.maxCuts,a.maxCuts);if(fracgt(a.wp,a.wq,tranche.wp,tranche.wq)){tranche.wp=a.wp;tranche.wq=a.wq;tranche.worst=a.worst;tranche.wSources=a.wSources;tranche.wSubset=a.wSubset;tranche.wSupply=a.wSupply;tranche.wCapacity=a.wCapacity;}if(fracgt(a.gp,a.gq,tranche.gp,tranche.gq)){tranche.gp=a.gp;tranche.gq=a.gq;}if(fracgt(a.pp,a.pq,tranche.pp,tranche.pq)){tranche.pp=a.pp;tranche.pq=a.pq;}}
  array<TypeAcc,3> typeTotal{};for(int tid=0;tid<threads;tid++)for(int t=0;t<3;t++){auto const&a=tyacc[tid][t];auto &z=typeTotal[t];z.flaws+=a.flaws;z.violations+=a.violations;if(fracgt(a.np,a.nq,z.np,z.nq)){z.np=a.np;z.nq=a.nq;z.sourceCount=a.sourceCount;z.worst=a.worst;}}
  array<long long,3> countMaxByType{},violatingCountMaxByType{};int nonemptyCountRows=0,firstViolation=0,lastNonviolation=0;
  for(int sc=band_lo;sc<=band_hi;sc++)if(per[sc].flaws){nonemptyCountRows++;int ti=arc_path_components(per[sc].worst,triples)-1;countMaxByType[ti]++;if((long long)sc*per[sc].wp>per[sc].wq){violatingCountMaxByType[ti]++;if(!firstViolation)firstViolation=sc;}else lastNonviolation=sc;}
  bool ok=C==362880&&cleanCycles==297886&&cleanStates==115586396&&nonemptyArcKeys==60480&&maxRaw==720&&cand.size()==24762&&total.flaws==47512&&minSources==106&&total.maxSources==720&&total.incidences==27939188&&total.supply==1485249312&&total.best.supply==65256&&total.best.sources==720&&total.hist[720]==412&&quantile(1,4)==545&&quantile(1,2)==612&&quantile(3,4)==658&&quantile(9,10)==687&&quantile(99,100)==718;
  if(band_lo==209&&band_hi==287){ok=ok&&tranche.flaws==284&&tranche.proper==284&&nonemptyCountRows==43&&firstViolation==209&&lastNonviolation==287&&typeTotal[0].flaws==40&&typeTotal[0].violations==8&&typeTotal[0].np==14076&&typeTotal[0].nq==11845&&typeTotal[0].sourceCount==276&&typeTotal[1].flaws==124&&typeTotal[1].violations==20&&typeTotal[1].np==51152&&typeTotal[1].nq==38383&&typeTotal[1].sourceCount==278&&typeTotal[2].flaws==120&&typeTotal[2].violations==40&&typeTotal[2].np==1984&&typeTotal[2].nq==1563&&typeTotal[2].sourceCount==248&&countMaxByType[0]==4&&countMaxByType[1]==17&&countMaxByType[2]==22&&violatingCountMaxByType[0]==1&&violatingCountMaxByType[1]==2&&violatingCountMaxByType[2]==10;}
  if(!ok){cerr<<"m10 Hall transition arc-type regression mismatch\n";return 2;}
  cout<<"{\n  \"m\":10,\n  \"source_cycle_band\":["<<band_lo<<","<<band_hi<<"],\n"<<"  \"source_band_signed_flaws\":"<<tranche.flaws<<",\n"<<"  \"source_band_proper_bottlenecks\":"<<tranche.proper<<",\n"<<"  \"source_band_worst_charge\":\""<<tranche.wp<<"/"<<tranche.wq<<"\",\n"<<"  \"support_profile\":[";
  bool firstRow=true;for(int sc=band_lo;sc<=band_hi;sc++)if(per[sc].flaws){auto const&a=per[sc];if(!firstRow)cout<<",";firstRow=false;cout<<"{\"source_cycles\":"<<sc<<",\"signed_flaws\":"<<a.flaws<<",\"proper_bottlenecks\":"<<a.proper<<",\"worst_charge\":\""<<a.wp<<"/"<<a.wq<<"\",\"max_support_normalized_charge\":\""<<sc*a.wp<<"/"<<a.wq<<"\",\"worst_subset_size\":"<<a.wSubset<<",\"worst_supply\":"<<a.wSupply<<",\"worst_capacity\":"<<a.wCapacity<<",\"maximizer_source_owners\":["<<triples[a.worst.s][0]<<","<<triples[a.worst.s][1]<<","<<triples[a.worst.s][2]<<"],\"maximizer_targets\":["<<int(a.worst.ta)<<","<<int(a.worst.tb)<<","<<int(a.worst.tc)<<"],\"maximizer_orientations\":["<<(a.worst.mask&1)<<","<<((a.worst.mask>>1)&1)<<",0],\"prescribed_arc_path_components\":"<<arc_path_components(a.worst,triples)<<",\"prescribed_arc_path_type\":\""<<arc_path_type(arc_path_components(a.worst,triples))<<"\"}";}
  cout<<"],\n  \"arc_path_type_profile\":[";for(int t=0;t<3;t++){auto const&a=typeTotal[t];if(t)cout<<",";cout<<"{\"path_components\":"<<(t+1)<<",\"path_type\":\""<<arc_path_type(t+1)<<"\",\"signed_flaws\":"<<a.flaws<<",\"constant_one_violations\":"<<a.violations<<",\"maximum_support_normalized_charge\":\""<<a.np<<"/"<<a.nq<<"\",\"maximizing_source_count\":"<<a.sourceCount<<",\"maximizer_source_owners\":["<<triples[a.worst.s][0]<<","<<triples[a.worst.s][1]<<","<<triples[a.worst.s][2]<<"],\"maximizer_targets\":["<<int(a.worst.ta)<<","<<int(a.worst.tb)<<","<<int(a.worst.tc)<<"]}";}
  cout<<"],\n  \"count_maximum_path_type_profile\":[";for(int t=0;t<3;t++){if(t)cout<<",";cout<<"{\"path_components\":"<<(t+1)<<",\"path_type\":\""<<arc_path_type(t+1)<<"\",\"nonempty_source_counts_with_this_maximizer_type\":"<<countMaxByType[t]<<",\"violating_count_maxima_with_this_type\":"<<violatingCountMaxByType[t]<<"}";}
  cout<<"],\n  \"transition_nonempty_source_counts\":"<<nonemptyCountRows<<",\n  \"first_count_maximum_violation\":"<<firstViolation<<",\n  \"last_count_maximum_nonviolation\":"<<lastNonviolation<<",\n  \"all_exact_regressions_verified\":true\n}\n";
}

#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;
constexpr int MAXM=10, MAXW=16;
using Rho=array<uint8_t,MAXM>;
struct Point{int x,y;};
long long cross(Point a,Point b,Point c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
array<Point,4> block(int m,int s,int t,int e){int n=2*m;auto J=[n](int x){return n-1-x;};Point q0{s,e?J(t):t},q1{J(s),e?t:J(t)};return {q0,q1,Point{J(q0.y),q0.x},Point{J(q1.y),q1.x}};}
bool pair_bad(int m,int sa,int ta,int ea,int sb,int tb,int eb){auto A=block(m,sa,ta,ea),B=block(m,sb,tb,eb);array<Point,8>p{};for(int i=0;i<4;i++){p[i]=A[i];p[i+4]=B[i];}for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)if(cross(p[i],p[j],p[k])==0)return true;return false;}
bool triple_bad(int m,int a,int ta,int ea,int b,int tb,int eb,int c,int tc,int ec){auto A=block(m,a,ta,ea),B=block(m,b,tb,eb),C=block(m,c,tc,ec);for(auto x:A)for(auto y:B)for(auto z:C)if(cross(x,y,z)==0)return true;return false;}
uint64_t encode(Rho const&r,int m){uint64_t x=0;for(int i=0;i<m;i++)x=(x<<4)|r[i];return x;}
Rho switched(Rho const&r,int m,array<int,3>T){array<int,3>cyc{};int f=0,cur=min({T[0],T[1],T[2]});for(int k=0;k<m;k++){if(cur==T[0]||cur==T[1]||cur==T[2])cyc[f++]=cur;cur=r[cur];}Rho o=r;o[cyc[0]]=r[cyc[1]];o[cyc[1]]=r[cyc[2]];o[cyc[2]]=r[cyc[0]];return o;}
struct Result{int m=0;long long cycles=0,cleanCycles=0,cleanStates=0,validStates=0,unreached=0;vector<long long>dist;int maxDistance=-1,maxWidth=0;map<pair<int,int>,long long> pairCycles,pairStates;map<int,long long>widthCycles,widthStates,completeShellCycles,completeShellStates;long long gapCycles=0;};
Result run_case(int m){
 const int ROOTS=1<<m, WORDS=(ROOTS+63)/64;
 vector<array<int,3>> triples;for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)triples.push_back({a,b,c});int K=triples.size();
 vector<int8_t> rel((size_t)m*m*m*m);auto i4=[m](int a,int ta,int b,int tb){return ((size_t(a)*m+ta)*m+b)*m+tb;};
 for(int a=0;a<m;a++)for(int ta=0;ta<m;ta++)if(ta!=a)for(int b=a+1;b<m;b++)for(int tb=0;tb<m;tb++)if(tb!=b&&tb!=ta){bool eq=pair_bad(m,a,ta,0,b,tb,0),un=pair_bad(m,a,ta,0,b,tb,1);rel[i4(a,ta,b,tb)]=eq&&un?3:eq?2:un?1:0;}
 vector<uint8_t> badpat((size_t)K*m*m*m);auto ib=[m](int ti,int ta,int tb,int tc){return ((size_t(ti)*m+ta)*m+tb)*m+tc;};
 #pragma omp parallel for schedule(static)
 for(int ti=0;ti<K;ti++){auto T=triples[ti];for(int ta=0;ta<m;ta++)for(int tb=0;tb<m;tb++)for(int tc=0;tc<m;tc++){if(ta==tb||ta==tc||tb==tc||ta==T[0]||tb==T[1]||tc==T[2])continue;uint8_t bm=0;for(int p=0;p<8;p++)if(triple_bad(m,T[0],ta,p&1,T[1],tb,(p>>1)&1,T[2],tc,(p>>2)&1))bm|=1u<<p;badpat[ib(ti,ta,tb,tc)]=bm;}}
 vector<Rho> cycles;vector<int>tail(m-1);iota(tail.begin(),tail.end(),1);do{array<int,MAXM>ord{};Rho r{};ord[0]=0;for(int i=1;i<m;i++)ord[i]=tail[i-1];for(int i=0;i<m;i++)r[ord[i]]=ord[(i+1)%m];cycles.push_back(r);}while(next_permutation(tail.begin(),tail.end()));int C=cycles.size();
 unordered_map<uint64_t,int> index;index.reserve(C*2);for(int i=0;i<C;i++)index[encode(cycles[i],m)]=i;
 vector<uint64_t> sat((size_t)C*WORDS);vector<int> cleanIndex(C,-1),cleanCycle;cleanCycle.reserve(C);long long cleanStates=0;
 for(int ci=0;ci<C;ci++){
  struct E{uint8_t a,b,p;};vector<E>edges;bool impossible=false;
  for(int a=0;a<m&&!impossible;a++)for(int b=a+1;b<m;b++){int v=rel[i4(a,cycles[ci][a],b,cycles[ci][b])];if(v==3){impossible=true;break;}if(v)edges.push_back({(uint8_t)a,(uint8_t)b,(uint8_t)(v==1?0:1)});}
  if(impossible) continue;
  long long count=0;
  for(int mask=0;mask<ROOTS;mask++){bool ok=true;for(auto e:edges)if(((((mask>>e.a)^(mask>>e.b))&1)!=e.p)){ok=false;break;}if(ok){sat[(size_t)ci*WORDS+(mask>>6)]|=1ULL<<(mask&63);count++;}}
  if(count){cleanIndex[ci]=cleanCycle.size();cleanCycle.push_back(ci);cleanStates+=count;}
 }
 int NC=cleanCycle.size();
 vector<uint64_t> pattern((size_t)K*8*WORDS);for(int ti=0;ti<K;ti++){auto T=triples[ti];for(int mask=0;mask<ROOTS;mask++){int p=((mask>>T[0])&1)|(((mask>>T[1])&1)<<1)|(((mask>>T[2])&1)<<2);pattern[((size_t)ti*8+p)*WORDS+(mask>>6)]|=1ULL<<(mask&63);}}
 vector<uint64_t> ownerbits((size_t)NC*m*WORDS);
 auto obase=[m,WORDS](int x,int o){return ((size_t)x*m+o)*WORDS;};
 #pragma omp parallel for schedule(dynamic,32)
 for(int x=0;x<NC;x++){
  int ci=cleanCycle[x];
  for(int ti=0;ti<K;ti++){auto T=triples[ti];uint8_t bm=badpat[ib(ti,cycles[ci][T[0]],cycles[ci][T[1]],cycles[ci][T[2]])];if(!bm)continue;for(int w=0;w<WORDS;w++){uint64_t bs=0;for(int p=0;p<8;p++)if((bm>>p)&1)bs|=pattern[((size_t)ti*8+p)*WORDS+w];bs&=sat[(size_t)ci*WORDS+w];ownerbits[obase(x,T[0])+w]|=bs;ownerbits[obase(x,T[1])+w]|=bs;ownerbits[obase(x,T[2])+w]|=bs;}}
 }
 vector<int> neighbour((size_t)NC*K,-1);
 #pragma omp parallel for schedule(static)
 for(int x=0;x<NC;x++){int ci=cleanCycle[x];for(int ti=0;ti<K;ti++){int cj=index[encode(switched(cycles[ci],m,triples[ti]),m)];neighbour[(size_t)x*K+ti]=cleanIndex[cj];}}
 vector<uint64_t> reached((size_t)NC*WORDS);vector<int8_t>cmin(NC,-1),cmax(NC,-1);vector<uint32_t>layers(NC);queue<int>q;vector<long long>dist(32);long long valid=0;
 for(int x=0;x<NC;x++){int ci=cleanCycle[x];long long cnt=0;for(int w=0;w<WORDS;w++){uint64_t any=0;for(int o=0;o<m;o++)any|=ownerbits[obase(x,o)+w];uint64_t v=sat[(size_t)ci*WORDS+w]&~any;reached[(size_t)x*WORDS+w]=v;cnt+=__builtin_popcountll(v);}if(cnt){valid+=cnt;dist[0]+=cnt;cmin[x]=cmax[x]=0;layers[x]|=1u;q.push(x);}}
 while(!q.empty()){int eta=q.front();q.pop();int nd=cmin[eta]+1;for(int ti=0;ti<K;ti++){int rho=neighbour[(size_t)eta*K+ti];if(rho<0)continue;auto T=triples[ti];bool anynew=false;long long added=0;int ci=cleanCycle[rho];for(int w=0;w<WORDS;w++){uint64_t elig=(ownerbits[obase(rho,T[0])+w]|ownerbits[obase(rho,T[1])+w]|ownerbits[obase(rho,T[2])+w])&sat[(size_t)ci*WORDS+w];uint64_t&seen=reached[(size_t)rho*WORDS+w];uint64_t fresh=elig&~seen;if(fresh){seen|=fresh;anynew=true;added+=__builtin_popcountll(fresh);}}if(added){dist[nd]+=added;cmax[rho]=max<int>(cmax[rho],nd);layers[rho]|=1u<<nd;}if(anynew&&cmin[rho]<0){cmin[rho]=nd;q.push(rho);}}}
 Result R;R.m=m;R.cycles=C;R.cleanCycles=NC;R.cleanStates=cleanStates;R.validStates=valid;R.dist=dist;long long total=accumulate(dist.begin(),dist.end(),0LL);R.unreached=cleanStates-total;for(int d=0;d<(int)dist.size();d++)if(dist[d])R.maxDistance=d;
 for(int x=0;x<NC;x++){long long states=0;int ci=cleanCycle[x];for(int w=0;w<WORDS;w++)states+=__builtin_popcountll(sat[(size_t)ci*WORDS+w]);int a=cmin[x],b=cmax[x],wid=b-a;R.maxWidth=max(R.maxWidth,wid);R.pairCycles[{a,b}]++;R.pairStates[{a,b}]+=states;R.widthCycles[wid]++;R.widthStates[wid]+=states;if(wid==0){R.completeShellCycles[a]++;R.completeShellStates[a]+=states;}uint32_t need=0;for(int d=a;d<=b;d++)need|=1u<<d;if((layers[x]&need)!=need)R.gapCycles++;}
 return R;
}
int main(int argc,char**argv){
 int m=argc>1?atoi(argv[1]):10;Result r=run_case(m);
 if(r.unreached){cerr<<"unreached\n";return 2;}
 auto pc=[&](int a,int b){auto it=r.pairCycles.find({a,b});return it==r.pairCycles.end()?0LL:it->second;};
 auto ps=[&](int a,int b){auto it=r.pairStates.find({a,b});return it==r.pairStates.end()?0LL:it->second;};
 bool ok=false;
 if(m==8) ok=r.cycles==5040&&r.cleanCycles==3542&&r.cleanStates==404080&&r.validStates==28&&r.maxDistance==3&&r.maxWidth==2&&r.gapCycles==10&&
   r.dist[0]==28&&r.dist[1]==66844&&r.dist[2]==303576&&r.dist[3]==33632&&
   pc(0,2)==10&&pc(1,1)==446&&pc(1,2)==2&&pc(2,2)==2644&&pc(2,3)==4&&pc(3,3)==436&&
   ps(0,2)==2048&&ps(1,1)==66592&&ps(1,2)==256&&ps(2,2)==301176&&ps(2,3)==384&&ps(3,3)==33624;
 if(m==9) ok=r.cycles==40320&&r.cleanCycles==31688&&r.cleanStates==6727728&&r.validStates==8&&r.maxDistance==4&&r.maxWidth==2&&r.gapCycles==4&&
   r.dist[0]==8&&r.dist[1]==59008&&r.dist[2]==1317376&&r.dist[3]==4873296&&r.dist[4]==478040&&
   pc(0,2)==4&&pc(1,1)==282&&pc(2,2)==6080&&pc(2,3)==8&&pc(3,3)==23016&&pc(4,4)==2298&&
   ps(0,2)==640&&ps(1,1)==59008&&ps(2,2)==1315288&&ps(2,3)==1472&&ps(3,3)==4873280&&ps(4,4)==478040;
 if(m==10) ok=r.cycles==362880&&r.cleanCycles==297886&&r.cleanStates==115586396&&r.validStates==12&&r.maxDistance==5&&r.maxWidth==2&&r.gapCycles==4&&
   r.dist[0]==12&&r.dist[1]==205376&&r.dist[2]==5534564&&r.dist[3]==52044980&&r.dist[4]==57266392&&r.dist[5]==535072&&
   pc(0,2)==4&&pc(1,1)==458&&pc(2,2)==14590&&pc(2,3)==26&&pc(3,3)==137640&&pc(3,4)==12&&pc(4,4)==143896&&pc(5,5)==1260&&
   ps(0,2)==3072&&ps(1,1)==205376&&ps(2,2)==5512128&&ps(2,3)==19456&&ps(3,3)==52039168&&ps(3,4)==5760&&ps(4,4)==57266364&&ps(5,5)==535072;
 if(!ok){cerr<<"fibre-width regression mismatch at m="<<m<<"\n";return 3;}
 long long mixedNonvalid=0;int nonvalidMaxWidth=0;for(auto const&kv:r.pairCycles)if(kv.first.first>0){nonvalidMaxWidth=max(nonvalidMaxWidth,kv.first.second-kv.first.first);if(kv.first.second>kv.first.first)mixedNonvalid+=kv.second;}
 cout<<"{\n  \"m\":"<<r.m<<",\n  \"hamilton_cycles\":"<<r.cycles<<",\n  \"clean_cycles\":"<<r.cleanCycles<<",\n  \"clean_states\":"<<r.cleanStates<<",\n  \"valid_states\":"<<r.validStates<<",\n  \"maximum_distance\":"<<r.maxDistance<<",\n  \"maximum_fibre_width\":"<<r.maxWidth<<",\n  \"nonvalid_maximum_fibre_width\":"<<nonvalidMaxWidth<<",\n  \"mixed_nonvalid_cycles\":"<<mixedNonvalid<<",\n  \"cycles_with_distance_gaps\":"<<r.gapCycles<<",\n  \"distance_distribution\":{";bool f=true;for(int d=0;d<=r.maxDistance;d++)if(r.dist[d]){if(!f)cout<<",";f=false;cout<<"\""<<d<<"\":"<<r.dist[d];}cout<<"},\n  \"cycle_min_max_distribution\":{";f=true;for(auto const&kv:r.pairCycles){if(!f)cout<<",";f=false;cout<<"\""<<kv.first.first<<","<<kv.first.second<<"\":"<<kv.second;}cout<<"},\n  \"state_min_max_distribution\":{";f=true;for(auto const&kv:r.pairStates){if(!f)cout<<",";f=false;cout<<"\""<<kv.first.first<<","<<kv.first.second<<"\":"<<kv.second;}cout<<"},\n  \"fibre_width_cycle_distribution\":{";f=true;for(auto const&kv:r.widthCycles){if(!f)cout<<",";f=false;cout<<"\""<<kv.first<<"\":"<<kv.second;}cout<<"},\n  \"complete_fibre_shell_cycle_distribution\":{";f=true;for(auto const&kv:r.completeShellCycles){if(!f)cout<<",";f=false;cout<<"\""<<kv.first<<"\":"<<kv.second;}cout<<"},\n  \"complete_fibre_shell_state_distribution\":{";f=true;for(auto const&kv:r.completeShellStates){if(!f)cout<<",";f=false;cout<<"\""<<kv.first<<"\":"<<kv.second;}cout<<"},\n  \"all_distance_gaps_confined_to_valid_cycles\":"<<(r.gapCycles==pc(0,2)?"true":"false")<<"\n}\n"; }

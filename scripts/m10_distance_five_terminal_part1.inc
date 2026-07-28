#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;
constexpr int M=10,W=16;
using Rho=array<uint8_t,M>;
struct P{int x,y;};
long long cross(P a,P b,P c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
array<P,4> block(int s,int t,int e){auto J=[](int x){return 19-x;};P q0{s,e?J(t):t},q1{J(s),e?t:J(t)};return {q0,q1,P{J(q0.y),q0.x},P{J(q1.y),q1.x}};}
bool pair_bad(int sa,int ta,int ea,int sb,int tb,int eb){auto A=block(sa,ta,ea),B=block(sb,tb,eb);array<P,8>p{};for(int i=0;i<4;i++){p[i]=A[i];p[i+4]=B[i];}for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)if(cross(p[i],p[j],p[k])==0)return true;return false;}
int triple_count(int a,int ta,int ea,int b,int tb,int eb,int c,int tc,int ec){auto A=block(a,ta,ea),B=block(b,tb,eb),C=block(c,tc,ec);int q=0;for(auto x:A)for(auto y:B)for(auto z:C)q+=cross(x,y,z)==0;return q;}
uint64_t encode(const Rho&r){uint64_t x=0;for(int i=0;i<M;i++)x=(x<<4)|r[i];return x;}
Rho switched(const Rho&r,array<int,3>T){array<int,3>cyc{};int f=0,cur=min({T[0],T[1],T[2]});for(int k=0;k<M;k++){if(cur==T[0]||cur==T[1]||cur==T[2])cyc[f++]=cur;cur=r[cur];}Rho o=r;o[cyc[0]]=r[cyc[1]];o[cyc[1]]=r[cyc[2]];o[cyc[2]]=r[cyc[0]];return o;}
struct Info{uint8_t cc=0,edges=0,rank=0;array<int8_t,M>comp{},colour{};};
struct Witness{array<int,M> rho{};int orientation=0,clean_index=-1,root=0;array<uint16_t,2> supports{};};
struct Local{
 long long states=0,pairs=0; map<int,long long> sup,atom,cover,cc,rank;
 int minSup=999,maxSup=0,minAtom=99999,maxAtom=0; vector<Witness>witnesses;
};
void merge(Local&a,const Local&b){a.states+=b.states;a.pairs+=b.pairs;for(auto [k,v]:b.sup)a.sup[k]+=v;for(auto [k,v]:b.atom)a.atom[k]+=v;for(auto [k,v]:b.cover)a.cover[k]+=v;for(auto [k,v]:b.cc)a.cc[k]+=v;for(auto [k,v]:b.rank)a.rank[k]+=v;a.minSup=min(a.minSup,b.minSup);a.maxSup=max(a.maxSup,b.maxSup);a.minAtom=min(a.minAtom,b.minAtom);a.maxAtom=max(a.maxAtom,b.maxAtom);a.witnesses.insert(a.witnesses.end(),b.witnesses.begin(),b.witnesses.end());}
void printmap(const map<int,long long>&a){cout<<"{";bool f=true;for(auto [k,v]:a){if(!f)cout<<",";f=false;cout<<"\""<<k<<"\":"<<v;}cout<<"}";}
int main(){
 const int ROOTS=1<<M; vector<array<int,3>> triples; for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)for(int c=b+1;c<M;c++)triples.push_back({a,b,c}); int K=triples.size();
 vector<int8_t> rel((size_t)M*M*M*M); auto i4=[](int a,int ta,int b,int tb){return ((size_t(a)*M+ta)*M+b)*M+tb;};
 for(int a=0;a<M;a++)for(int ta=0;ta<M;ta++)if(ta!=a)for(int b=a+1;b<M;b++)for(int tb=0;tb<M;tb++)if(tb!=b&&tb!=ta){bool eq=pair_bad(a,ta,0,b,tb,0),un=pair_bad(a,ta,0,b,tb,1);rel[i4(a,ta,b,tb)]=eq&&un?3:eq?2:un?1:0;}
 auto ib=[](int ti,int ta,int tb,int tc){return ((size_t(ti)*M+ta)*M+tb)*M+tc;};
 vector<uint8_t> badpat((size_t)K*M*M*M),badcount((size_t)K*M*M*M*8);
 #pragma omp parallel for schedule(static)
 for(int ti=0;ti<K;ti++){auto T=triples[ti];for(int ta=0;ta<M;ta++)for(int tb=0;tb<M;tb++)for(int tc=0;tc<M;tc++){if(ta==tb||ta==tc||tb==tc||ta==T[0]||tb==T[1]||tc==T[2])continue;uint8_t bm=0;for(int p=0;p<8;p++){int q=triple_count(T[0],ta,p&1,T[1],tb,(p>>1)&1,T[2],tc,(p>>2)&1);badcount[ib(ti,ta,tb,tc)*8+p]=q;if(q)bm|=1u<<p;}badpat[ib(ti,ta,tb,tc)]=bm;}}
 vector<Rho> cycles;array<int,M-1> tail{};iota(tail.begin(),tail.end(),1);do{array<int,M>ord{};Rho r{};ord[0]=0;for(int i=1;i<M;i++)ord[i]=tail[i-1];for(int i=0;i<M;i++)r[ord[i]]=ord[(i+1)%M];cycles.push_back(r);}while(next_permutation(tail.begin(),tail.end()));int C=cycles.size();
 unordered_map<uint64_t,int> index;index.reserve(C*2);for(int i=0;i<C;i++)index[encode(cycles[i])]=i;
 vector<int> cleanIndex(C,-1),cleanCycle; vector<Info> info; long long cleanStates=0;
 for(int ci=0;ci<C;ci++){int8_t adj[M][M];for(auto &row:adj)for(auto &v:row)v=-1;bool imp=false;int edges=0;for(int a=0;a<M&&!imp;a++)for(int b=a+1;b<M;b++){int v=rel[i4(a,cycles[ci][a],b,cycles[ci][b])];if(v==3){imp=true;break;}if(v){adj[a][b]=adj[b][a]=v==1?0:1;edges++;}}if(imp)continue;Info in;in.comp.fill(-1);in.colour.fill(-1);bool ok=true;int cc=0;for(int root=0;root<M;root++)if(in.comp[root]<0){array<int,M>q{};int h=0,t=0;q[t++]=root;in.comp[root]=cc;in.colour[root]=0;while(h<t){int u=q[h++];for(int v=0;v<M;v++)if(adj[u][v]>=0){int want=in.colour[u]^adj[u][v];if(in.comp[v]<0){in.comp[v]=cc;in.colour[v]=want;q[t++]=v;}else if(in.colour[v]!=want)ok=false;}}cc++;}if(!ok)continue;in.cc=cc;in.edges=edges;in.rank=edges-M+cc;cleanIndex[ci]=info.size();info.push_back(in);cleanCycle.push_back(ci);cleanStates+=1LL<<cc;}
 int NC=info.size(); cerr<<"clean cycles "<<NC<<" states "<<cleanStates<<"\n";
 vector<array<array<uint64_t,W>,M>> varbits(M+1);vector<array<uint64_t,W>> fullmask(M+1);for(int c=1;c<=M;c++){int roots=1<<c,words=(roots+63)/64;for(int w=0;w<words;w++){int left=roots-64*w;fullmask[c][w]=left>=64?~0ULL:(left<=0?0ULL:((1ULL<<left)-1));}for(int j=0;j<c;j++)for(int r=0;r<roots;r++)if((r>>j)&1)varbits[c][j][r>>6]|=1ULL<<(r&63);}
 vector<uint64_t> ownerbits((size_t)NC*M*W),reached((size_t)NC*W);array<vector<uint64_t>,6> layer;for(auto &v:layer)v.assign((size_t)NC*W,0);vector<long long> validPer(NC);
 auto obase=[](int x,int o){return ((size_t)x*M+o)*W;};
 #pragma omp parallel for schedule(dynamic,32)
 for(int x=0;x<NC;x++){int ci=cleanCycle[x],cc=info[x].cc;auto &in=info[x];for(int ti=0;ti<K;ti++){auto T=triples[ti];uint8_t bm=badpat[ib(ti,cycles[ci][T[0]],cycles[ci][T[1]],cycles[ci][T[2]])];if(!bm)continue;for(int w=0;w<W;w++){uint64_t bs=0;for(int p=0;p<8;p++)if((bm>>p)&1){uint64_t term=fullmask[cc][w];for(int k=0;k<3;k++){int o=T[k],cp=in.comp[o],rb=((p>>k)&1)^in.colour[o];uint64_t vb=varbits[cc][cp][w];term&=rb?vb:(~vb&fullmask[cc][w]);}bs|=term;}for(int k=0;k<3;k++)ownerbits[obase(x,T[k])+w]|=bs;}}long long val=0;for(int w=0;w<W;w++){uint64_t any=0;for(int o=0;o<M;o++)any|=ownerbits[obase(x,o)+w];uint64_t v=(~any)&fullmask[cc][w];reached[(size_t)x*W+w]=v;layer[0][(size_t)x*W+w]=v;val+=__builtin_popcountll(v);}validPer[x]=val;}
 long long valid=accumulate(validPer.begin(),validPer.end(),0LL);vector<int> nei((size_t)NC*K,-1);
 #pragma omp parallel for schedule(static)
 for(int x=0;x<NC;x++){int ci=cleanCycle[x];for(int ti=0;ti<K;ti++){int cj=index.at(encode(switched(cycles[ci],triples[ti])));nei[(size_t)x*K+ti]=cleanIndex[cj];}}
 vector<int8_t> cmin(NC,-1);queue<int>q;vector<long long> dist(16);dist[0]=valid;for(int x=0;x<NC;x++)if(validPer[x]){cmin[x]=0;q.push(x);}while(!q.empty()){int eta=q.front();q.pop();int nd=cmin[eta]+1;for(int ti=0;ti<K;ti++){int rho=nei[(size_t)eta*K+ti];if(rho<0)continue;auto T=triples[ti];bool anynew=false;long long add=0;for(int w=0;w<W;w++){uint64_t eligible=ownerbits[obase(rho,T[0])+w]|ownerbits[obase(rho,T[1])+w]|ownerbits[obase(rho,T[2])+w];uint64_t &seen=reached[(size_t)rho*W+w];uint64_t fresh=eligible&~seen;if(fresh){seen|=fresh;anynew=true;add+=__builtin_popcountll(fresh);if(nd<=5)layer[nd][(size_t)rho*W+w]|=fresh;}}if(add)dist[nd]+=add;if(anynew&&cmin[rho]<0){cmin[rho]=nd;q.push(rho);}}}
 cerr<<"d5 "<<dist[5]<<"\n"; if(dist[5]!=535072){cerr<<"distance mismatch\n";return 2;}
 vector<pair<int,int>> masks;for(int s=1;s<ROOTS;s++)masks.push_back({__builtin_popcount((unsigned)s),s});sort(masks.begin(),masks.end());
 int nt=1;
#ifdef _OPENMP
 nt=omp_get_max_threads();
#endif
 vector<Local> locals(nt);vector<int> percycle(NC);
 #pragma omp parallel for schedule(dynamic,32)
 for(int x=0;x<NC;x++){
 int tid=0;
#ifdef _OPENMP
 tid=omp_get_thread_num();
#endif
 Local &L=locals[tid];int ci=cleanCycle[x],cc=info[x].cc,roots=1<<cc;int here=0;for(int r=0;r<roots;r++){if(!((layer[5][(size_t)x*W+(r>>6)]>>(r&63))&1))continue;here++;L.states++;int e=0;for(int o=0;o<M;o++)e|=((((r>>info[x].comp[o])&1)^info[x].colour[o])<<o);int sup=0,atom=0;array<uint16_t,120> sm{};int ns=0;for(int ti=0;ti<K;ti++){auto T=triples[ti];int p=((e>>T[0])&1)|(((e>>T[1])&1)<<1)|(((e>>T[2])&1)<<2);int cnt=badcount[ib(ti,cycles[ci][T[0]],cycles[ci][T[1]],cycles[ci][T[2]])*8+p];if(cnt){sup++;atom+=cnt;sm[ns++]=(1<<T[0])|(1<<T[1])|(1<<T[2]);}}int cv=0;for(auto [k,mask]:masks){bool ok=true;for(int j=0;j<ns;j++)if(!(sm[j]&mask)){ok=false;break;}if(ok){cv=k;break;}}L.sup[sup]++;L.atom[atom]++;L.cover[cv]++;L.cc[cc]++;L.rank[info[x].rank]++;L.minSup=min(L.minSup,sup);L.maxSup=max(L.maxSup,sup);L.minAtom=min(L.minAtom,atom);L.maxAtom=max(L.maxAtom,atom);if(sup==2&&atom==8&&e<(e^1023)){Witness z;for(int o=0;o<M;o++)z.rho[o]=cycles[ci][o];z.orientation=e;z.clean_index=x;z.root=r;z.supports[0]=sm[0];z.supports[1]=sm[1];L.witnesses.push_back(z);}int rc=r^(roots-1);if(r<rc&&((layer[5][(size_t)x*W+(rc>>6)]>>(rc&63))&1))L.pairs++;}percycle[x]=here;}
 Local total;for(auto &l:locals)merge(total,l);int cycCount=0,minPer=1e9,maxPer=0,fullFibres=0;map<int,long long> perDist,cycleCC;for(int x=0;x<NC;x++){int z=percycle[x];if(z){cycCount++;minPer=min(minPer,z);maxPer=max(maxPer,z);perDist[z]++;cycleCC[info[x].cc]++;if(z==(1<<info[x].cc))fullFibres++;}}sort(total.witnesses.begin(),total.witnesses.end(),[](const Witness&a,const Witness&b){return tie(a.rho,a.orientation)<tie(b.rho,b.orientation);});

 // Exact joint shortest-path Pareto recursion, evaluated only in the backward

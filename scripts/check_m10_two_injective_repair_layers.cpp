#include <algorithm>
#include <array>
#include <bitset>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;
constexpr int M=10,N=20,Q=1<<M;
using Rho=array<uint8_t,M>;
struct RH{size_t operator()(Rho const&r)const noexcept{size_t h=0;for(auto x:r)h=h*17+x+1;return h;}};
struct Point{int x,y;}; struct Edge{uint8_t a,b,p;};
array<Point,4> orbit(int s,int t,int e){auto J=[](int x){return N-1-x;};Point q0{s,e?J(t):t},q1{J(s),e?t:J(t)};return {q0,q1,Point{J(q0.y),q0.x},Point{J(q1.y),q1.x}};}
bool col(Point a,Point b,Point c){return 1LL*(b.x-a.x)*(c.y-a.y)==1LL*(b.y-a.y)*(c.x-a.x);}
bool bad(int sa,int ta,int ea,int sb,int tb,int eb){auto A=orbit(sa,ta,ea),B=orbit(sb,tb,eb);array<Point,8>p{};for(int i=0;i<4;i++){p[i]=A[i];p[i+4]=B[i];}for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)if(col(p[i],p[j],p[k]))return true;return false;}
vector<Rho> cycles(){vector<Rho>out;array<int,M-1>tail{};iota(tail.begin(),tail.end(),1);do{array<int,M>ord{};ord[0]=0;for(int i=1;i<M;i++)ord[i]=tail[i-1];Rho r{};for(int i=0;i<M;i++)r[ord[i]]=ord[(i+1)%M];out.push_back(r);}while(next_permutation(tail.begin(),tail.end()));return out;}
Rho switched(Rho const&r,uint16_t mask){int st=0;while(!(mask&(1<<st)))st++;array<int,3>s{};int c=0,cur=st;for(int z=0;z<M;z++){if(mask&(1<<cur))s[c++]=cur;cur=r[cur];}Rho o=r;o[s[0]]=r[s[1]];o[s[1]]=r[s[2]];o[s[2]]=r[s[0]];return o;}
struct HK{
 int nL,nR;vector<vector<int>> const& a;vector<int> ml,mr,dist;
 HK(vector<vector<int>> const&a,int nR):nL(a.size()),nR(nR),a(a),ml(nL,-1),mr(nR,-1),dist(nL){}
 bool bfs(){vector<int>q(nL);int h=0,z=0;bool found=false;for(int u=0;u<nL;u++){if(ml[u]<0){dist[u]=0;q[z++]=u;}else dist[u]=-1;}while(h<z){int u=q[h++];for(int v:a[u]){int w=mr[v];if(w<0)found=true;else if(dist[w]<0){dist[w]=dist[u]+1;q[z++]=w;}}}return found;}
 bool dfs(int u){for(int v:a[u]){int w=mr[v];if(w<0||(dist[w]==dist[u]+1&&dfs(w))){ml[u]=v;mr[v]=u;return true;}}dist[u]=-1;return false;}
 int run(){int m=0;while(bfs())for(int u=0;u<nL;u++)if(ml[u]<0&&dfs(u))m++;return m;}
};
int main(){
 static uint8_t rel[M][M][M][M];
 for(int a=0;a<M;a++)for(int ta=0;ta<M;ta++)if(a!=ta)for(int b=a+1;b<M;b++)for(int tb=0;tb<M;tb++)if(b!=tb&&ta!=tb){bool eq=bad(a,ta,0,b,tb,0),un=bad(a,ta,0,b,tb,1);rel[a][ta][b][tb]=eq&&un?3:eq?2:un?1:0;}
 vector<uint16_t> triples;for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)for(int c=b+1;c<M;c++)triples.push_back((1<<a)|(1<<b)|(1<<c));
 auto rhos=cycles();int C=rhos.size();unordered_map<Rho,int,RH>id;id.reserve(C*2);for(int i=0;i<C;i++)id[rhos[i]]=i;
 vector<int8_t> lambda(C,-1);vector<bitset<Q>> sat(C);vector<vector<int>> sourcesByMask(Q);long long optimalStates=0,cleanStates=0;vector<Edge> edges;edges.reserve(32);
 for(int ri=0;ri<C;ri++){
   edges.clear();bool impossible=false;
   for(int a=0;a<M&&!impossible;a++)for(int b=a+1;b<M;b++){int v=rel[a][rhos[ri][a]][b][rhos[ri][b]];if(v==3){impossible=true;break;}if(v)edges.push_back({(uint8_t)a,(uint8_t)b,(uint8_t)(v==1?0:1)});}
   if(impossible)continue;
   array<uint8_t,Q> vio{};int best=100;
   for(int mask=0;mask<Q;mask++){int z=0;for(auto e:edges)z+=(((((mask>>e.a)^(mask>>e.b))&1)!=e.p));vio[mask]=z;best=min(best,z);}
   lambda[ri]=best;
   if(best==0){for(int mask=0;mask<Q;mask++)if(vio[mask]==0){sat[ri].set(mask);cleanStates++;}}
   else for(int mask=0;mask<Q;mask++)if(vio[mask]==best){sourcesByMask[mask].push_back(ri);optimalStates++;}
 }
 cerr<<"geometry states="<<optimalStates<<" clean="<<cleanStates<<"\n";
 vector<uint64_t> offset(C+1);vector<uint32_t> cleanTarget;vector<uint16_t> cleanTriple;cleanTarget.reserve(30000000);cleanTriple.reserve(30000000);
 for(int ri=0;ri<C;ri++){
   offset[ri]=cleanTarget.size();
   for(uint16_t t:triples){int y=id[switched(rhos[ri],t)];if(lambda[y]==0){cleanTarget.push_back(y);cleanTriple.push_back(t);}}
 }
 offset[C]=cleanTarget.size();cerr<<"cycle-level clean labels="<<cleanTarget.size()<<"\n";
 auto makeRef=[](int mask,int ri,int copy)->uint64_t{return (uint64_t(mask)<<32)|(uint64_t(uint32_t(ri))<<1)|uint64_t(copy);};
 auto refMask=[](uint64_t ref)->int{return int(ref>>32);};
 auto refCycle=[](uint64_t ref)->int{return int((uint32_t(ref))>>1);};
 using Pair=pair<uint64_t,uint64_t>;
 vector<Pair> basePairs;basePairs.reserve(2*optimalStates);vector<uint64_t> deficitCopies;long long matchedTotal=0,edgesTotal=0;int failedMasks=0;long long degree1Sources=0;
 #pragma omp parallel
 {
   vector<Pair> locPairs;vector<uint64_t> locDef;long long locMatched=0,locEdges=0,locDeg1=0;int locFailed=0;
   #pragma omp for schedule(dynamic,1)
   for(int mask=0;mask<Q;mask++){
     vector<int> src;vector<vector<int>> raw;vector<int> targets;src.reserve(sourcesByMask[mask].size());raw.reserve(sourcesByMask[mask].size()*2);
     for(int ri:sourcesByMask[mask]){
       vector<int>a;for(uint64_t p=offset[ri];p<offset[ri+1];p++){int y=cleanTarget[p];if(sat[y].test(mask)){a.push_back(y);targets.push_back(y);}}
       sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());if(a.size()==1)locDeg1++;
       src.push_back(ri);raw.push_back(a);raw.push_back(move(a));locEdges+=2LL*raw[raw.size()-1].size();
     }
     sort(targets.begin(),targets.end());targets.erase(unique(targets.begin(),targets.end()),targets.end());vector<vector<int>>adj(raw.size());
     for(int i=0;i<(int)raw.size();i++){adj[i].reserve(raw[i].size());for(int y:raw[i])adj[i].push_back(lower_bound(targets.begin(),targets.end(),y)-targets.begin());}
     HK hk(adj,targets.size());int got=hk.run();locMatched+=got;if(got!=(int)adj.size())locFailed++;
     for(int u=0;u<(int)adj.size();u++){int ri=src[u/2],copy=u&1;if(hk.ml[u]>=0){uint64_t targetKey=(uint64_t(targets[hk.ml[u]])<<M)|mask;locPairs.push_back({targetKey,makeRef(mask,ri,copy)});}else locDef.push_back(makeRef(mask,ri,copy));}
   }
   #pragma omp critical
   {basePairs.insert(basePairs.end(),locPairs.begin(),locPairs.end());deficitCopies.insert(deficitCopies.end(),locDef.begin(),locDef.end());matchedTotal+=locMatched;edgesTotal+=locEdges;failedMasks+=locFailed;degree1Sources+=locDeg1;}
 }
 sort(basePairs.begin(),basePairs.end(),[](Pair const&a,Pair const&b){return a.first<b.first;});sort(deficitCopies.begin(),deficitCopies.end());
 cerr<<"base twofold matched="<<matchedTotal<<" deficits="<<deficitCopies.size()<<" failed masks="<<failedMasks<<" deg1="<<degree1Sources<<"\n";
 auto localAdjFor=[&](int ri,int mask,vector<uint64_t>&cand){cand.clear();for(uint64_t p=offset[ri];p<offset[ri+1];p++){int y=cleanTarget[p];uint16_t t=cleanTriple[p];int base=mask&~t;for(int sub=t;;sub=(sub-1)&t){int e=base|sub;if(sat[y].test(e))cand.push_back((uint64_t(y)<<M)|e);if(sub==0)break;}}sort(cand.begin(),cand.end());cand.erase(unique(cand.begin(),cand.end()),cand.end());};
 auto fixedAdjFor=[&](uint64_t sourceRef,vector<uint64_t>&out){int mask=refMask(sourceRef),ri=refCycle(sourceRef);out.clear();for(uint64_t p=offset[ri];p<offset[ri+1];p++){int y=cleanTarget[p];if(sat[y].test(mask))out.push_back((uint64_t(y)<<M)|mask);}sort(out.begin(),out.end());out.erase(unique(out.begin(),out.end()),out.end());};
 const uint64_t NONE=~0ULL;unordered_map<uint64_t,uint64_t> changed;changed.reserve(deficitCopies.size()*16+1024);
 auto baseOcc=[&](uint64_t key)->uint64_t{auto it=lower_bound(basePairs.begin(),basePairs.end(),key,[](Pair const&a,uint64_t k){return a.first<k;});return it!=basePairs.end()&&it->first==key?it->second:NONE;};
 auto occupant=[&](uint64_t key)->uint64_t{auto it=changed.find(key);return it==changed.end()?baseOcc(key):it->second;};
 long long directFree=0,maxPathSources=0,bfsSourceVisits=0,bfsTargetVisits=0;vector<uint64_t> temp;
 for(size_t di=0;di<deficitCopies.size();di++){
   uint64_t start=deficitCopies[di];vector<uint64_t>q;size_t qh=0;q.push_back(start);
   unordered_map<uint64_t,uint64_t> parentTargetOfSource,parentSourceOfTarget;unordered_set<uint64_t> seenSource,seenTarget;seenSource.insert(start);uint64_t freeTarget=NONE;
   while(qh<q.size()&&freeTarget==NONE){uint64_t sref=q[qh++];bfsSourceVisits++;if(sref==start)localAdjFor(refCycle(sref),refMask(sref),temp);else fixedAdjFor(sref,temp);for(uint64_t t:temp){if(!seenTarget.insert(t).second)continue;bfsTargetVisits++;parentSourceOfTarget[t]=sref;uint64_t occ=occupant(t);if(occ==NONE){freeTarget=t;break;}if(seenSource.insert(occ).second){parentTargetOfSource[occ]=t;q.push_back(occ);}}}
   if(freeTarget==NONE){cerr<<"twofold global augmenting failure at deficit "<<di<<" / "<<deficitCopies.size()<<"\n";return 14;}
   int pathSources=0;uint64_t t=freeTarget;while(true){uint64_t sref=parentSourceOfTarget[t];pathSources++;changed[t]=sref;auto it=parentTargetOfSource.find(sref);if(it==parentTargetOfSource.end())break;uint64_t old=it->second;changed[old]=NONE;t=old;}
   if(pathSources==1) directFree++;
   maxPathSources=max<long long>(maxPathSources,pathSources);
 }
 long long occupiedCount=0;for(auto const&p:basePairs){auto it=changed.find(p.first);if(it==changed.end()||it->second!=NONE)occupiedCount++;}for(auto const&kv:changed)if(kv.second!=NONE&&baseOcc(kv.first)==NONE)occupiedCount++;
 bool ok=optimalStates==12786720&&cleanStates==115586396&&
   cleanTarget.size()==35746320&&matchedTotal==25572988&&edgesTotal==846320044&&
   deficitCopies.size()==452&&degree1Sources==304&&failedMasks==226&&
   directFree==232&&maxPathSources==2&&bfsSourceVisits==755&&bfsTargetVisits==7032&&
   occupiedCount==25573440;
 if(!ok){cerr<<"two-layer matching regression mismatch\n";return 15;}
 cout<<"{\n  \"m\":10,\n  \"sources\":"<<optimalStates<<",\n  \"required_target_assignments\":"<<2*optimalStates<<",\n  \"fixed_sign_twofold_edges\":"<<edgesTotal<<",\n  \"fixed_sign_twofold_matched\":"<<matchedTotal<<",\n  \"fixed_sign_twofold_deficits\":"<<deficitCopies.size()<<",\n  \"fixed_sign_degree_one_sources\":"<<degree1Sources<<",\n  \"fixed_sign_masks_with_deficit\":"<<failedMasks<<",\n  \"deficits_assigned_without_rerouting\":"<<directFree<<",\n  \"maximum_augmenting_path_source_count\":"<<maxPathSources<<",\n  \"augmenting_bfs_source_visits\":"<<bfsSourceVisits<<",\n  \"augmenting_bfs_target_visits\":"<<bfsTargetVisits<<",\n  \"occupied_distinct_targets\":"<<occupiedCount<<",\n  \"two_injective_layers_constructed\":"<<(occupiedCount==2*optimalStates?"true":"false")<<",\n  \"averaged_maximum_reverse_indegree\":\"1/2\"\n}\n";
 return occupiedCount==2*optimalStates?0:15;
}

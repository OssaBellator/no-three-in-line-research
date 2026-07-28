#include <algorithm>
#include <array>
#include <bitset>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
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
 vector<uint64_t> offset(C+1);vector<uint32_t> cleanTarget;vector<uint16_t> cleanTriple;cleanTarget.reserve(30000000);cleanTriple.reserve(30000000);
 for(int ri=0;ri<C;ri++){
   offset[ri]=cleanTarget.size();
   for(uint16_t t:triples){int y=id[switched(rhos[ri],t)];if(lambda[y]==0){cleanTarget.push_back(y);cleanTriple.push_back(t);}}
 }
 offset[C]=cleanTarget.size();
 long long states=0;int globalMin=100000,globalMax=0;vector<long long>hist(1025,0);vector<pair<int,int>>minExamples;
 #pragma omp parallel
 {
   int localMin=100000,localMax=0;long long localStates=0;vector<long long>localHist(1025,0);vector<pair<int,int>>localExamples;
   #pragma omp for schedule(dynamic,1)
   for(int mask=0;mask<Q;mask++)for(int ri:sourcesByMask[mask]){
     vector<uint64_t>cand;
     for(uint64_t p=offset[ri];p<offset[ri+1];p++){int y=cleanTarget[p];uint16_t t=cleanTriple[p];int base=mask&~t;for(int sub=t;;sub=(sub-1)&t){int e=base|sub;if(sat[y].test(e))cand.push_back((uint64_t(y)<<M)|e);if(sub==0)break;}}
     sort(cand.begin(),cand.end());cand.erase(unique(cand.begin(),cand.end()),cand.end());int d=cand.size();
     localStates++;localMin=min(localMin,d);localMax=max(localMax,d);if(d<(int)localHist.size())localHist[d]++;
     if(d<=3)localExamples.push_back({ri,mask});
   }
   #pragma omp critical
   {states+=localStates;globalMin=min(globalMin,localMin);globalMax=max(globalMax,localMax);for(size_t i=0;i<hist.size();i++)hist[i]+=localHist[i];minExamples.insert(minExamples.end(),localExamples.begin(),localExamples.end());}
 }
 bool ok=optimalStates==12786720&&cleanStates==115586396&&states==12786720&&globalMin==2&&globalMax==420&&hist[2]==8&&hist[4]==24&&hist[6]==28&&hist[8]==36&&minExamples.size()==8;
 if(!ok){cerr<<"local target-degree regression mismatch\n";return 2;}
 cout<<"{\n  \"m\":10,\n  \"sources\":"<<states<<",\n  \"minimum_distinct_local_targets\":"<<globalMin<<",\n  \"maximum_distinct_local_targets\":"<<globalMax<<",\n  \"small_degree_distribution\":{";bool first=true;for(int d=0;d<=10;d++)if(hist[d]){if(!first)cout<<",";first=false;cout<<"\""<<d<<"\":"<<hist[d];}cout<<"},\n  \"degree_two_sources\":[";sort(minExamples.begin(),minExamples.end());for(size_t i=0;i<minExamples.size();i++){auto [ri,mask]=minExamples[i];cout<<"{\"mask\":"<<mask<<",\"rho\":[";for(int j=0;j<M;j++){if(j)cout<<",";cout<<int(rhos[ri][j]);}cout<<"]}"<<(i+1==minExamples.size()?"":",");}cout<<"],\n  \"three_layers_degree_obstruction\":true\n}\n";
 return 0;
}

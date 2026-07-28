#include <algorithm>
#include <array>
#include <bitset>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
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
 auto rhos=cycles();unordered_map<Rho,int,RH>id;id.reserve(rhos.size()*2);for(int i=0;i<(int)rhos.size();i++)id[rhos[i]]=i;
 int C=rhos.size();vector<int8_t>lambda(C,-1);vector<uint8_t>pairsafe(C),clean(C);vector<bitset<Q>>sat(C);vector<Edge>edges;edges.reserve(32);
 for(int ri=0;ri<C;ri++){edges.clear();bool impossible=false;for(int a=0;a<M;a++)for(int b=a+1;b<M;b++){int v=rel[a][rhos[ri][a]][b][rhos[ri][b]];if(v==3)impossible=true;else if(v)edges.push_back({(uint8_t)a,(uint8_t)b,(uint8_t)(v==1?0:1)});}if(impossible)continue;pairsafe[ri]=1;int best=100;for(int mask=0;mask<Q;mask++){int vio=0;for(auto e:edges)vio+=(((((mask>>e.a)^(mask>>e.b))&1)!=e.p));best=min(best,vio);}lambda[ri]=best;if(best==0){clean[ri]=1;for(int mask=0;mask<Q;mask++){bool ok=true;for(auto e:edges)if(((((mask>>e.a)^(mask>>e.b))&1)!=e.p)){ok=false;break;}if(ok)sat[ri].set(mask);}}}
 long long optimalStates=0, coveringLocal=0, coveringFixed=0;
 long long noCoveringLocal=0,noCoveringFixed=0;
 int minCoveringLocal=1000,minCoveringFixed=1000,maxMinCoverHam=0;
 array<long long,4> coverHamHist{};
 array<long long,8> lambdaHist{}, noCoverLambdaHist{};
 long long vertexCoverLe3=0, noTripleCover=0;
 int maxViolEdges=0;
 for(int ri=0;ri<C;ri++)if(pairsafe[ri]&&lambda[ri]>0){
   edges.clear();
   for(int a=0;a<M;a++)for(int b=a+1;b<M;b++){int v=rel[a][rhos[ri][a]][b][rhos[ri][b]];if(v&&v!=3)edges.push_back({(uint8_t)a,(uint8_t)b,(uint8_t)(v==1?0:1)});}
   vector<pair<uint16_t,int>> toClean;
   for(uint16_t t:triples){int y=id[switched(rhos[ri],t)];if(clean[y])toClean.push_back({t,y});}
   for(int mask=0;mask<Q;mask++){
     vector<Edge> viol;
     for(auto e:edges)if(((((mask>>e.a)^(mask>>e.b))&1)!=e.p))viol.push_back(e);
     if((int)viol.size()!=lambda[ri])continue;
     optimalStates++; lambdaHist[lambda[ri]]++; maxViolEdges=max(maxViolEdges,(int)viol.size());
     bool coverExists=false;
     for(uint16_t t:triples){
       bool cov=true;for(auto e:viol) if(!(t&((1<<e.a)|(1<<e.b)))) {cov=false;break;}
       if(cov){coverExists=true;break;}
     }
     if(coverExists) vertexCoverLe3++; else noTripleCover++;
     int fixed=0, local=0,bestHam=99;
     for(auto [t,y]:toClean){
       bool cov=true;for(auto e:viol)if(!(t&((1<<e.a)|(1<<e.b)))){cov=false;break;}
       if(!cov)continue;
       if(sat[y].test(mask))fixed++;
       int base=mask&~t,bh=99;bool ok=false;
       for(int sub=t;;sub=(sub-1)&t){int cand=base|sub;if(sat[y].test(cand)){ok=true;bh=min(bh,__builtin_popcount((unsigned)(cand^mask)));}if(sub==0)break;}
       if(ok){local++;bestHam=min(bestHam,bh);}
     }
     coveringFixed+=fixed;coveringLocal+=local;
     if(!fixed)noCoveringFixed++;else minCoveringFixed=min(minCoveringFixed,fixed);
     if(!local){noCoveringLocal++;noCoverLambdaHist[lambda[ri]]++;}
     else{minCoveringLocal=min(minCoveringLocal,local);maxMinCoverHam=max(maxMinCoverHam,bestHam);coverHamHist[bestHam]++;}
   }
 }
 bool ok =
   optimalStates==12786720 &&
   maxViolEdges==3 &&
   vertexCoverLe3==12786720 &&
   noTripleCover==0 &&
   coveringFixed==423160022 &&
   noCoveringFixed==74 &&
   minCoveringFixed==1 &&
   coveringLocal==652008272 &&
   noCoveringLocal==0 &&
   minCoveringLocal==1 &&
   maxMinCoverHam==2 &&
   coverHamHist==array<long long,4>{12786646,70,4,0} &&
   lambdaHist[1]==12393720 &&
   lambdaHist[2]==387456 &&
   lambdaHist[3]==5544 &&
   lambdaHist[4]==0;
 if(!ok){cerr<<"covering local-repair ledger mismatch\n";return 1;}
 cout<<"{\n"
 <<"  \"m\": 10,\n"
 <<"  \"optimal_positive_signed_states\": "<<optimalStates<<",\n"
 <<"  \"maximum_violated_edges_in_optimum\": "<<maxViolEdges<<",\n"
 <<"  \"states_with_some_three_owner_vertex_cover\": "<<vertexCoverLe3<<",\n"
 <<"  \"states_without_any_three_owner_vertex_cover\": "<<noTripleCover<<",\n"
 <<"  \"covering_fixed_sign_clean_rotations\": "<<coveringFixed<<",\n"
 <<"  \"states_without_covering_fixed_sign_clean_rotation\": "<<noCoveringFixed<<",\n"
 <<"  \"minimum_covering_fixed_sign_choices_when_nonempty\": "<<minCoveringFixed<<",\n"
 <<"  \"covering_local_clean_rotations\": "<<coveringLocal<<",\n"
 <<"  \"states_without_covering_local_clean_rotation\": "<<noCoveringLocal<<",\n"
 <<"  \"minimum_covering_local_choices_when_nonempty\": "<<minCoveringLocal<<",\n"
 <<"  \"maximum_minimum_covering_local_hamming_change\": "<<maxMinCoverHam<<",\n"
 <<"  \"covering_local_minimum_hamming_distribution\": {\"0\": "<<coverHamHist[0]<<", \"1\": "<<coverHamHist[1]<<", \"2\": "<<coverHamHist[2]<<", \"3\": "<<coverHamHist[3]<<"},\n"
 <<"  \"optimal_state_frustration_distribution\": {\"1\": "<<lambdaHist[1]<<", \"2\": "<<lambdaHist[2]<<", \"3\": "<<lambdaHist[3]<<", \"4\": "<<lambdaHist[4]<<"},\n"
 <<"  \"uncovered_local_failure_by_frustration\": {\"1\": "<<noCoverLambdaHist[1]<<", \"2\": "<<noCoverLambdaHist[2]<<", \"3\": "<<noCoverLambdaHist[3]<<", \"4\": "<<noCoverLambdaHist[4]<<"},\n"
 <<"  \"violation_cover_necessity_verified\": true,\n" <<"  \"complete_covering_local_repair_verified\": true,\n" <<"  \"asymptotic_covering_rotation_theorem_proved\": false\n"
 <<"}\n";
}

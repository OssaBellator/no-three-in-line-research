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
 long long optimalStates=0,edgeChecks=0,sameDesc=0,targetInc=0,localDesc=0,localTargetInc=0;
 int minSame=1000,minTarget=1000,minLocal=1000,minLocalTarget=1000,maxMinHamming=0,maxTargetMinHamming=0;
 long long noSame=0,noTarget=0,noLocal=0,noLocalTarget=0;array<long long,4>localHist{},exceptionHist{};
 for(int ri=0;ri<C;ri++)if(pairsafe[ri]&&lambda[ri]>0){edges.clear();for(int a=0;a<M;a++)for(int b=a+1;b<M;b++){int v=rel[a][rhos[ri][a]][b][rhos[ri][b]];if(v&&v!=3)edges.push_back({(uint8_t)a,(uint8_t)b,(uint8_t)(v==1?0:1)});}vector<pair<uint16_t,int>>toClean;for(uint16_t t:triples){int y=id[switched(rhos[ri],t)];if(clean[y])toClean.push_back({t,y});}
  for(int mask=0;mask<Q;mask++){int vio=0;vector<Edge>viol;for(auto e:edges)if(((((mask>>e.a)^(mask>>e.b))&1)!=e.p)){vio++;viol.push_back(e);}if(vio!=lambda[ri])continue;optimalStates++;int same=0,local=0,bestHam=99;
   for(auto [t,y]:toClean){if(sat[y].test(mask))same++;int base=mask&~t,bh=99;bool ok=false;for(int sub=t;;sub=(sub-1)&t){int cand=base|sub;if(sat[y].test(cand)){ok=true;bh=min(bh,__builtin_popcount((unsigned)(cand^mask)));}if(sub==0)break;}if(ok){local++;bestHam=min(bestHam,bh);}}
   sameDesc+=same;minSame=min(minSame,same);if(!same)noSame++;localDesc+=local;minLocal=min(minLocal,local);if(!local)noLocal++;else{maxMinHamming=max(maxMinHamming,bestHam);localHist[bestHam]++;if(!same)exceptionHist[bestHam]++;}
   for(auto e:viol){edgeChecks++;int hit=0,lhit=0,bestTH=99;uint16_t owners=(1<<e.a)|(1<<e.b);for(auto [t,y]:toClean)if(t&owners){if(sat[y].test(mask))hit++;int base=mask&~t,bh=99;bool ok=false;for(int sub=t;;sub=(sub-1)&t){int cand=base|sub;if(sat[y].test(cand)){ok=true;bh=min(bh,__builtin_popcount((unsigned)(cand^mask)));}if(sub==0)break;}if(ok){lhit++;bestTH=min(bestTH,bh);}}targetInc+=hit;minTarget=min(minTarget,hit);if(!hit)noTarget++;localTargetInc+=lhit;minLocalTarget=min(minLocalTarget,lhit);if(!lhit)noLocalTarget++;else maxTargetMinHamming=max(maxTargetMinHamming,bestTH);}
  }
 }
 bool ok=optimalStates==12786720&&sameDesc==423160022&&minSame==0&&edgeChecks==13185264&&targetInc==429279344&&minTarget==0&&noSame==74&&noTarget==218&&localDesc==652008272&&minLocal==1&&maxMinHamming==2&&noLocal==0&&localTargetInc==661435264&&minLocalTarget==1&&maxTargetMinHamming==2&&noLocalTarget==0&&localHist==array<long long,4>{12786646,70,4,0}&&exceptionHist==array<long long,4>{0,70,4,0};
 if(!ok){cerr<<"verification mismatch\n";return 1;}
 cout<<"{\n  \"m\": 10,\n  \"optimal_positive_signed_states\": "<<optimalStates<<",\n  \"fixed_orientation_direct_clean_rotations\": "<<sameDesc<<",\n  \"minimum_fixed_orientation_clean_rotations_per_optimal_state\": "<<minSame<<",\n  \"optimal_violated_edge_checks\": "<<edgeChecks<<",\n  \"fixed_orientation_targeted_clean_incidences\": "<<targetInc<<",\n  \"minimum_fixed_orientation_targeted_clean_rotations_per_edge\": "<<minTarget<<",\n  \"optimal_states_without_fixed_orientation_clean_rotation\": "<<noSame<<",\n  \"violated_edges_without_fixed_orientation_targeted_clean_rotation\": "<<noTarget<<",\n  \"local_three_owner_clean_rotations\": "<<localDesc<<",\n  \"minimum_local_rotations_per_optimal_state\": "<<minLocal<<",\n  \"maximum_minimum_local_hamming_change\": "<<maxMinHamming<<",\n  \"optimal_states_without_local_three_owner_repair\": "<<noLocal<<",\n  \"local_targeted_clean_incidences\": "<<localTargetInc<<",\n  \"minimum_local_targeted_rotations_per_edge\": "<<minLocalTarget<<",\n  \"maximum_targeted_minimum_hamming_change\": "<<maxTargetMinHamming<<",\n  \"violated_edges_without_local_targeted_repair\": "<<noLocalTarget<<",\n  \"minimum_hamming_distribution_over_optimal_states\": {\"0\": "<<localHist[0]<<", \"1\": "<<localHist[1]<<", \"2\": "<<localHist[2]<<", \"3\": "<<localHist[3]<<"},\n  \"fixed_sign_exception_hamming_distribution\": {\"1\": "<<exceptionHist[1]<<", \"2\": "<<exceptionHist[2]<<", \"3\": "<<exceptionHist[3]<<"},\n  \"asymptotic_theorem_proved\": false\n}\n";
}

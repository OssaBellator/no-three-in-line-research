#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;
struct Point{int x,y;};
long long cross(Point a,Point b,Point c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
array<Point,4> orbit(int m,int s,int t,int e){int n=2*m;auto r=[n](int x){return n-1-x;};Point q0{s,e?r(t):t},q1{r(s),e?t:r(t)};return {q0,q1,Point{r(q0.y),q0.x},Point{r(q1.y),q1.x}};}
bool pair_bad(int m,int sa,int ta,int ea,int sb,int tb,int eb){auto a=orbit(m,sa,ta,ea),b=orbit(m,sb,tb,eb);array<Point,8>p{};for(int i=0;i<4;i++){p[i]=a[i];p[i+4]=b[i];}for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)if(cross(p[i],p[j],p[k])==0)return true;return false;}
bool triple_bad(int m,int a,int ta,int ea,int b,int tb,int eb,int c,int tc,int ec){auto A=orbit(m,a,ta,ea),B=orbit(m,b,tb,eb),C=orbit(m,c,tc,ec);for(auto x:A)for(auto y:B)for(auto z:C)if(cross(x,y,z)==0)return true;return false;}
struct Relations{int m;vector<int8_t>d;explicit Relations(int M):m(M),d(m*m*m*m,0){for(int a=0;a<m;a++)for(int ta=0;ta<m;ta++){if(ta==a)continue;for(int b=a+1;b<m;b++)for(int tb=0;tb<m;tb++){if(tb==b||tb==ta)continue;bool eq=pair_bad(m,a,ta,0,b,tb,0),un=pair_bad(m,a,ta,0,b,tb,1);d[index(a,ta,b,tb)]=eq&&un?3:eq?2:un?1:0;}}}int index(int a,int ta,int b,int tb)const{return ((a*m+ta)*m+b)*m+tb;}int get(int a,int ta,int b,int tb)const{return d[index(a,ta,b,tb)];}};
uint64_t encode(const vector<int>&r){uint64_t x=0;for(int t:r)x=(x<<4)|t;return x;}
vector<int> switched(const vector<int>&r,array<int,3>s){array<int,3>cyclic{};int found=0,current=min({s[0],s[1],s[2]});for(int k=0;k<(int)r.size();k++){if(current==s[0]||current==s[1]||current==s[2])cyclic[found++]=current;current=r[current];}auto out=r;out[cyclic[0]]=r[cyclic[1]];out[cyclic[1]]=r[cyclic[2]];out[cyclic[2]]=r[cyclic[0]];return out;}
struct Flaw{array<int,3>source,target,orientation;bool operator<(const Flaw&o)const{return tie(source,target,orientation)<tie(o.source,o.target,o.orientation);}};
struct Expected{long long clean,flaws,worstNum,worstDen,proper;int worstSources,worstSubset;long double maxRatio;};
const array<Expected,4> expected={{
 {80,52,2,48,0,1,1,1.0L},
 {376,368,4,148,0,1,1,1.0L},
 {3576,1692,16,860,884,2,2,1.44962L},
 {36736,5100,96,7448,4864,6,6,1.69555L}
}};
int main(){
 cout<<"{\n  \"cases\": [\n";
 for(int m=4;m<=7;m++){
  Relations relation(m);vector<vector<int>>cycles;vector<int>tail(m-1);iota(tail.begin(),tail.end(),1);do{vector<int>order(m),rho(m);order[0]=0;for(int i=1;i<m;i++)order[i]=tail[i-1];for(int i=0;i<m;i++)rho[order[i]]=order[(i+1)%m];cycles.push_back(move(rho));}while(next_permutation(tail.begin(),tail.end()));
  unordered_map<uint64_t,int>index;index.reserve(cycles.size()*2);for(int i=0;i<(int)cycles.size();i++)index[encode(cycles[i])]=i;vector<array<int,3>>triples;for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)triples.push_back({a,b,c});
  vector<vector<int>>clean(cycles.size());long long totalClean=0;for(int ci=0;ci<(int)cycles.size();ci++){vector<vector<pair<int,int>>>adj(m);bool impossible=false;for(int a=0;a<m;a++)for(int b=a+1;b<m;b++){int v=relation.get(a,cycles[ci][a],b,cycles[ci][b]);if(v==3)impossible=true;else if(v){int parity=v==1?0:1;adj[a].push_back({b,parity});adj[b].push_back({a,parity});}}if(impossible)continue;vector<int>colour(m,-1);bool satisfiable=true;for(int root=0;root<m;root++)if(colour[root]<0){vector<int>queue={root};colour[root]=0;for(size_t h=0;h<queue.size();h++){int u=queue[h];for(auto [v,p]:adj[u]){int wanted=colour[u]^p;if(colour[v]<0){colour[v]=wanted;queue.push_back(v);}else if(colour[v]!=wanted)satisfiable=false;}}}if(!satisfiable)continue;for(int orientation=0;orientation<(1<<m);orientation++){bool ok=true;for(int a=0;a<m;a++)for(auto [b,p]:adj[a])if(a<b&&((((orientation>>a)&1)^((orientation>>b)&1))!=p))ok=false;if(ok)clean[ci].push_back(orientation);}totalClean+=clean[ci].size();}
  set<Flaw>flaws;for(int ci=0;ci<(int)cycles.size();ci++)for(int orientation:clean[ci])for(auto S:triples)if(triple_bad(m,S[0],cycles[ci][S[0]],(orientation>>S[0])&1,S[1],cycles[ci][S[1]],(orientation>>S[1])&1,S[2],cycles[ci][S[2]],(orientation>>S[2])&1)){Flaw A;A.source=S;for(int k=0;k<3;k++){A.target[k]=cycles[ci][S[k]];A.orientation[k]=(orientation>>S[k])&1;}flaws.insert(A);}
  long long worstNum=0,worstDen=1,worstGlobalNum=0,worstGlobalDen=1,proper=0;int worstSources=0,worstSubset=0;long double maxRatio=1;
  for(const Flaw&A:flaws){vector<int>X,weight;for(int ci=0;ci<(int)cycles.size();ci++){bool contains=true;for(int k=0;k<3;k++)if(cycles[ci][A.source[k]]!=A.target[k])contains=false;if(!contains||clean[ci].empty())continue;int count=0;for(int orientation:clean[ci]){bool same=true;for(int k=0;k<3;k++)if(((orientation>>A.source[k])&1)!=A.orientation[k])same=false;if(same)count++;}if(count){X.push_back(ci);weight.push_back(count);}}if(X.empty()||X.size()>20)return 1;
   vector<vector<int>>neighbour(X.size());for(int i=0;i<(int)X.size();i++){set<int>targets;for(auto T:triples){bool hit=false;for(int x:T)for(int y:A.source)if(x==y)hit=true;if(!hit)continue;int eta=index.at(encode(switched(cycles[X[i]],T)));if(!clean[eta].empty())targets.insert(eta);}neighbour[i]=vector<int>(targets.begin(),targets.end());}
   long long localNum=0,localDen=1;int localSubset=0;for(int mask=1;mask<(1<<(int)X.size());mask++){long long supply=0;set<int>targets;for(int i=0;i<(int)X.size();i++)if((mask>>i)&1){supply+=weight[i];targets.insert(neighbour[i].begin(),neighbour[i].end());}long long capacity=0;for(int eta:targets)capacity+=clean[eta].size();if(!capacity)return 2;if(supply*localDen>localNum*capacity){localNum=supply;localDen=capacity;localSubset=__builtin_popcount((unsigned)mask);}}
   long long allSupply=accumulate(weight.begin(),weight.end(),0LL);set<int>allTargets;for(auto&v:neighbour)allTargets.insert(v.begin(),v.end());long long allCapacity=0;for(int eta:allTargets)allCapacity+=clean[eta].size();if(allSupply*worstGlobalDen>worstGlobalNum*allCapacity){worstGlobalNum=allSupply;worstGlobalDen=allCapacity;}if(localNum*allCapacity>allSupply*localDen){proper++;maxRatio=max(maxRatio,(long double)localNum*allCapacity/(localDen*allSupply));}if(localNum*worstDen>worstNum*localDen){worstNum=localNum;worstDen=localDen;worstSources=X.size();worstSubset=localSubset;}}
  const Expected&e=expected[m-4];bool verified=totalClean==e.clean&&(long long)flaws.size()==e.flaws&&worstNum==e.worstNum&&worstDen==e.worstDen&&worstSources==e.worstSources&&worstSubset==e.worstSubset&&worstGlobalNum==e.worstNum&&worstGlobalDen==e.worstDen&&proper==e.proper&&abs((double)(maxRatio-e.maxRatio))<0.00001;if(!verified){cerr<<"verification mismatch at m="<<m<<"\n";return 3;}
  cout<<"    {\"m\": "<<m<<", \"clean_signed_states\": "<<totalClean<<", \"atomic_signed_assignment_flaws\": "<<flaws.size()<<", \"maximum_source_cycles_per_worst_flaw\": "<<worstSources<<", \"worst_hall_subset_size\": "<<worstSubset<<", \"optimal_charge_numerator\": "<<worstNum<<", \"optimal_charge_denominator\": "<<worstDen<<", \"optimal_charge_max\": "<<(double)worstNum/worstDen<<", \"m_cubed_scaled_charge\": "<<(double)worstNum*m*m*m/worstDen<<", \"global_subset_charge_numerator\": "<<worstGlobalNum<<", \"global_subset_charge_denominator\": "<<worstGlobalDen<<", \"proper_hall_bottleneck_flaws\": "<<proper<<", \"maximum_local_to_global_ratio\": "<<(double)maxRatio<<"}"<<(m<7?",":"")<<"\n";
 }
 cout<<"  ],\n  \"all_hall_subsets_enumerated\": true,\n  \"asymptotic_expansion_proved\": false\n}\n";
}

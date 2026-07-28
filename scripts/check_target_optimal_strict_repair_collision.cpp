#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <sstream>
#include <unordered_map>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::uint128_t;

constexpr int MAXM=10;
using Rho=array<uint8_t,MAXM>;
struct Point{int x,y;};
struct PairEdge{uint8_t a,b,p;};
struct RhoHash{size_t operator()(Rho const&r)const noexcept{size_t h=0;for(uint8_t x:r)h=h*17+x+1;return h;}};

long long cross(Point a,Point b,Point c){
  return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);
}
array<Point,4> block(int m,int s,int t,int e){
  int n=2*m;auto J=[n](int x){return n-1-x;};
  Point q0{s,e?J(t):t},q1{J(s),e?t:J(t)};
  return {q0,q1,Point{J(q0.y),q0.x},Point{J(q1.y),q1.x}};
}
bool pair_bad(int m,int sa,int ta,int ea,int sb,int tb,int eb){
  auto A=block(m,sa,ta,ea),B=block(m,sb,tb,eb);array<Point,8>p{};
  for(int i=0;i<4;i++){p[i]=A[i];p[i+4]=B[i];}
  for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)
    if(cross(p[i],p[j],p[k])==0)return true;
  return false;
}
vector<Rho> cycles(int m){
  vector<Rho>out;vector<int>tail(m-1);iota(tail.begin(),tail.end(),1);
  do{
    array<int,MAXM>ord{};ord[0]=0;for(int i=1;i<m;i++)ord[i]=tail[i-1];
    Rho r{};for(int i=0;i<m;i++)r[ord[i]]=ord[(i+1)%m];out.push_back(r);
  }while(next_permutation(tail.begin(),tail.end()));
  return out;
}
Rho switched(Rho const&r,int m,array<int,3>T){
  array<int,3>s{};int f=0,cur=min({T[0],T[1],T[2]});
  for(int z=0;z<m;z++){if(cur==T[0]||cur==T[1]||cur==T[2])s[f++]=cur;cur=r[cur];}
  Rho o=r;o[s[0]]=r[s[1]];o[s[1]]=r[s[2]];o[s[2]]=r[s[0]];return o;
}
uint128_t gcd128(uint128_t a,uint128_t b){while(b!=0){uint128_t r=a%b;a=b;b=r;}return a;}
uint128_t lcm128(uint128_t a,uint128_t b){return a/gcd128(a,b)*b;}
string text128(uint128_t x){ostringstream out;out<<x;return out.str();}

struct Dinic{
  struct Edge{int to,rev;long long cap;};
  int n;vector<vector<Edge>>g;vector<int>level,it;
  explicit Dinic(int n):n(n),g(n),level(n),it(n){}
  void add(int u,int v,long long c){Edge a{v,(int)g[v].size(),c},b{u,(int)g[u].size(),0};g[u].push_back(a);g[v].push_back(b);}
  bool bfs(int s,int t){
    fill(level.begin(),level.end(),-1);queue<int>q;level[s]=0;q.push(s);
    while(!q.empty()){int u=q.front();q.pop();for(auto const&e:g[u])if(e.cap&&level[e.to]<0){level[e.to]=level[u]+1;q.push(e.to);}}
    return level[t]>=0;
  }
  long long dfs(int u,int t,long long f){
    if(u==t)return f;
    for(int&i=it[u];i<(int)g[u].size();i++){
      Edge&e=g[u][i];if(e.cap&&level[e.to]==level[u]+1){long long z=dfs(e.to,t,min(f,e.cap));if(z){e.cap-=z;g[e.to][e.rev].cap+=z;return z;}}
    }
    return 0;
  }
  long long flow(int s,int t){long long ans=0,z;while(bfs(s,t)){fill(it.begin(),it.end(),0);while((z=dfs(s,t,(1LL<<60))))ans+=z;}return ans;}
  vector<char> reachable(int s){vector<char>seen(n);queue<int>q;seen[s]=1;q.push(s);while(!q.empty()){int u=q.front();q.pop();for(auto const&e:g[u])if(e.cap&&!seen[e.to]){seen[e.to]=1;q.push(e.to);}}return seen;}
};
long long gcd64(long long a,long long b){while(b){long long r=a%b;a=b;b=r;}return a;}
struct Ratio{long long p=0,q=1,u=0,v=0;int mask=0,iterations=0;};
bool ratio_less(Ratio const&a,Ratio const&b){return a.p*b.q<b.p*a.q;}
Ratio hall_ratio(vector<vector<int>> const&adj,int targetCount,int mask){
  int sourceCount=adj.size();Ratio result;result.mask=mask;if(sourceCount==0)return result;
  long long p=0,q=1;
  for(int iteration=0;iteration<64;iteration++){
    int source=0,sourceOffset=1,targetOffset=1+sourceCount,sink=1+sourceCount+targetCount;
    Dinic network(sink+1);long long inf=q*sourceCount+max(1LL,p)*targetCount+1;
    for(int i=0;i<sourceCount;i++){
      network.add(source,sourceOffset+i,q);
      for(int t:adj[i])network.add(sourceOffset+i,targetOffset+t,inf);
    }
    for(int t=0;t<targetCount;t++)network.add(targetOffset+t,sink,p);
    long long cut=network.flow(source,sink);long long closure=q*sourceCount-cut;result.iterations=iteration+1;
    if(closure<=0){result.p=p;result.q=q;return result;}
    auto side=network.reachable(source);long long U=0,V=0;
    for(int i=0;i<sourceCount;i++)U+=side[sourceOffset+i];
    for(int t=0;t<targetCount;t++)V+=side[targetOffset+t];
    if(V==0){cerr<<"zero-neighbour closure\n";exit(4);}
    long long g=gcd64(U,V),np=U/g,nq=V/g;
    if(np==p&&nq==q){cerr<<"stalled Dinkelbach iteration\n";exit(5);}
    p=np;q=nq;result.u=U;result.v=V;
  }
  cerr<<"too many Dinkelbach iterations\n";exit(6);
}

struct Geometry{
  int m,Q,K,C;
  vector<array<int,3>> triples;
  vector<Rho> rhos;
  vector<int8_t> lambda;
  vector<uint8_t> violations;
  vector<int> neighbour;
};
Geometry build_geometry(int m){
  Geometry G;G.m=m;G.Q=1<<m;
  for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)G.triples.push_back({a,b,c});
  G.K=G.triples.size();G.rhos=cycles(m);G.C=G.rhos.size();
  unordered_map<Rho,int,RhoHash>id;id.reserve(G.C*2);for(int i=0;i<G.C;i++)id[G.rhos[i]]=i;
  vector<int8_t>rel((size_t)m*m*m*m,0);
  auto index4=[m](int a,int ta,int b,int tb){return ((size_t(a)*m+ta)*m+b)*m+tb;};
  for(int a=0;a<m;a++)for(int ta=0;ta<m;ta++)if(a!=ta)
    for(int b=a+1;b<m;b++)for(int tb=0;tb<m;tb++)if(b!=tb&&ta!=tb){
      bool equalBad=pair_bad(m,a,ta,0,b,tb,0),unequalBad=pair_bad(m,a,ta,0,b,tb,1);
      rel[index4(a,ta,b,tb)]=equalBad&&unequalBad?3:equalBad?2:unequalBad?1:0;
    }
  G.lambda.assign(G.C,-1);G.violations.assign((size_t)G.C*G.Q,255);vector<PairEdge>edges;
  for(int cycle=0;cycle<G.C;cycle++){
    edges.clear();bool impossible=false;
    for(int a=0;a<m&&!impossible;a++)for(int b=a+1;b<m;b++){
      int value=rel[index4(a,G.rhos[cycle][a],b,G.rhos[cycle][b])];
      if(value==3){impossible=true;break;}
      if(value)edges.push_back({(uint8_t)a,(uint8_t)b,(uint8_t)(value==1?0:1)});
    }
    if(impossible)continue;
    int best=127;
    for(int mask=0;mask<G.Q;mask++){
      int count=0;for(auto edge:edges)count+=((((mask>>edge.a)^(mask>>edge.b))&1)!=edge.p);
      G.violations[(size_t)cycle*G.Q+mask]=count;best=min(best,count);
    }
    G.lambda[cycle]=best;
  }
  G.neighbour.resize((size_t)G.C*G.K);
  for(int cycle=0;cycle<G.C;cycle++)for(int triple=0;triple<G.K;triple++)
    G.neighbour[(size_t)cycle*G.K+triple]=id[switched(G.rhos[cycle],m,G.triples[triple])];
  return G;
}
bool admissible(Geometry const&G,int cycle,int mask,int triple){
  int target=G.neighbour[(size_t)cycle*G.K+triple];
  return G.lambda[target]>=0&&G.lambda[target]<G.lambda[cycle]&&
         G.violations[(size_t)target*G.Q+mask]==G.lambda[target];
}

struct UniformAudit{
  long long states=0,transitions=0,positiveColumns=0,columnsAboveOne=0;
  int minForward=999,maxForward=0,maxReverse=0,targetLambda=-1;
  uint128_t numerator=0,denominator=1;
};
UniformAudit uniform_audit(Geometry const&G,vector<uint8_t>&degree){
  degree.assign((size_t)G.C*G.Q,0);UniformAudit A;
  for(int cycle=0;cycle<G.C;cycle++)if(G.lambda[cycle]>0){
    for(int mask=0;mask<G.Q;mask++)if(G.violations[(size_t)cycle*G.Q+mask]==G.lambda[cycle]){
      int count=0;for(int triple=0;triple<G.K;triple++)count+=admissible(G,cycle,mask,triple);
      if(count==0){cerr<<"zero forward degree\n";exit(7);}
      degree[(size_t)cycle*G.Q+mask]=count;A.states++;A.transitions+=count;
      A.minForward=min(A.minForward,count);A.maxForward=max(A.maxForward,count);
    }
  }
  uint128_t common=1;for(int d=1;d<=G.K;d++)common=lcm128(common,uint128_t(d));
  vector<uint128_t>load((size_t)G.C*G.Q,0);vector<uint8_t>reverse((size_t)G.C*G.Q,0);
  for(int cycle=0;cycle<G.C;cycle++)if(G.lambda[cycle]>0){
    for(int mask=0;mask<G.Q;mask++){
      int count=degree[(size_t)cycle*G.Q+mask];if(!count)continue;uint128_t add=common/count;
      for(int triple=0;triple<G.K;triple++)if(admissible(G,cycle,mask,triple)){
        int target=G.neighbour[(size_t)cycle*G.K+triple];size_t key=(size_t)target*G.Q+mask;
        load[key]+=add;reverse[key]++;
      }
    }
  }
  uint128_t best=0;size_t bestKey=0;
  for(size_t key=0;key<load.size();key++)if(load[key]!=0){
    A.positiveColumns++;if(load[key]>common)A.columnsAboveOne++;A.maxReverse=max(A.maxReverse,(int)reverse[key]);
    if(load[key]>best){best=load[key];bestKey=key;}
  }
  uint128_t g=gcd128(best,common);A.numerator=best/g;A.denominator=common/g;A.targetLambda=G.lambda[bestKey/G.Q];
  return A;
}
struct OptimalAudit{
  long long states=0,transitions=0;int masksWithSources=0,masksAboveOne=0,masksEqualOne=0;
  Ratio worst;
};
OptimalAudit optimal_audit(Geometry const&G){
  OptimalAudit A;Ratio global;
  for(int mask=0;mask<G.Q;mask++){
    vector<int>sources;
    for(int cycle=0;cycle<G.C;cycle++)if(G.lambda[cycle]>0&&G.violations[(size_t)cycle*G.Q+mask]==G.lambda[cycle])sources.push_back(cycle);
    if(sources.empty())continue;
    A.masksWithSources++;
    A.states+=sources.size();
    vector<vector<int>>raw(sources.size());vector<int>targets;targets.reserve(sources.size()*4);
    for(size_t source=0;source<sources.size();source++){
      int cycle=sources[source];
      for(int triple=0;triple<G.K;triple++)if(admissible(G,cycle,mask,triple)){
        int target=G.neighbour[(size_t)cycle*G.K+triple];raw[source].push_back(target);targets.push_back(target);A.transitions++;
      }
    }
    sort(targets.begin(),targets.end());targets.erase(unique(targets.begin(),targets.end()),targets.end());
    unordered_map<int,int>targetIndex;targetIndex.reserve(targets.size()*2);for(int i=0;i<(int)targets.size();i++)targetIndex[targets[i]]=i;
    vector<vector<int>>adj(raw.size());
    for(size_t source=0;source<raw.size();source++){adj[source].reserve(raw[source].size());for(int target:raw[source])adj[source].push_back(targetIndex[target]);}
    Ratio ratio=hall_ratio(adj,targets.size(),mask);
    if(ratio.p>ratio.q)A.masksAboveOne++;else if(ratio.p==ratio.q)A.masksEqualOne++;
    if(ratio_less(global,ratio))global=ratio;
  }
  A.worst=global;return A;
}
struct CompleteAudit{int m;UniformAudit uniform;OptimalAudit optimal;};

int main(){
  vector<CompleteAudit> audits;
  for(int m=5;m<=9;m++){
    Geometry geometry=build_geometry(m);vector<uint8_t>degree;
    UniformAudit uniform=uniform_audit(geometry,degree);degree.clear();degree.shrink_to_fit();
    OptimalAudit optimal=optimal_audit(geometry);audits.push_back({m,uniform,optimal});
    cerr<<"m="<<m<<" uniform="<<text128(uniform.numerator)<<"/"<<text128(uniform.denominator)
        <<" optimal="<<optimal.worst.p<<"/"<<optimal.worst.q<<"\n";
  }
  const long long expectedStates[10]={0,0,0,0,0,48,272,2752,93980,977312};
  const long long expectedTransitions[10]={0,0,0,0,0,244,2596,37020,1642058,24730616};
  const int expectedMinForward[10]={0,0,0,0,0,3,5,6,5,4};
  const char* expectedUniform[10]={"","","","","","1/3","127/252","5069/5544","22357817/17907120","6619279336199/4658179125600"};
  const char* expectedOptimal[10]={"","","","","","1/3","4/19","1/5","489/1726","1/4"};
  for(auto const&A:audits){
    string uniform=text128(A.uniform.numerator)+"/"+text128(A.uniform.denominator);
    string optimal=to_string(A.optimal.worst.p)+"/"+to_string(A.optimal.worst.q);
    if(A.uniform.states!=expectedStates[A.m]||A.uniform.transitions!=expectedTransitions[A.m]||
       A.uniform.minForward!=expectedMinForward[A.m]||uniform!=expectedUniform[A.m]||
       A.optimal.states!=expectedStates[A.m]||A.optimal.transitions!=expectedTransitions[A.m]||
       optimal!=expectedOptimal[A.m]){
      cerr<<"strict-repair collision regression mismatch at m="<<A.m<<"\n";return 8;
    }
  }
  cout<<"{\n  \"strict_policy_graph\": \"target-optimal fixed-sign strict-frustration descents\",\n  \"sizes\": [\n";
  for(size_t i=0;i<audits.size();i++){
    auto const&A=audits[i];
    cout<<"    {\"m\":"<<A.m
        <<",\"optimal_positive_states\":"<<A.uniform.states
        <<",\"labelled_transitions\":"<<A.uniform.transitions
        <<",\"minimum_forward_degree\":"<<A.uniform.minForward
        <<",\"maximum_forward_degree\":"<<A.uniform.maxForward
        <<",\"uniform_maximum_reverse_multiplicity\":"<<A.uniform.maxReverse
        <<",\"uniform_maximum_weighted_reverse_indegree\":\""<<text128(A.uniform.numerator)<<"/"<<text128(A.uniform.denominator)<<"\""
        <<",\"uniform_positive_target_columns\":"<<A.uniform.positiveColumns
        <<",\"uniform_columns_above_one\":"<<A.uniform.columnsAboveOne
        <<",\"uniform_maximizer_target_frustration\":"<<A.uniform.targetLambda
        <<",\"orientation_masks_with_sources\":"<<A.optimal.masksWithSources
        <<",\"optimally_weighted_masks_above_one\":"<<A.optimal.masksAboveOne
        <<",\"optimally_weighted_masks_equal_one\":"<<A.optimal.masksEqualOne
        <<",\"optimal_maximum_weighted_reverse_indegree\":\""<<A.optimal.worst.p<<"/"<<A.optimal.worst.q<<"\""
        <<",\"worst_orientation_mask\":"<<A.optimal.worst.mask
        <<",\"worst_hall_sources\":"<<A.optimal.worst.u
        <<",\"worst_hall_targets\":"<<A.optimal.worst.v
        <<",\"worst_dinkelbach_iterations\":"<<A.optimal.worst.iterations<<"}"
        <<(i+1==audits.size()?"\n":",\n");
  }
  cout<<"  ],\n"
      <<"  \"uniform_load_accumulation_exact\": true,\n"
      <<"  \"orientation_masks_solved_independently\": true,\n"
      <<"  \"optimal_policy_via_exact_maximum_closure_mincut\": true,\n"
      <<"  \"largest_optimal_reverse_indegree_through_m9\": \"489/1726\",\n"
      <<"  \"three_step_absorbing_column_bound_through_m9\": \"1986421179/5141885176\"\n"
      <<"}\n";
}

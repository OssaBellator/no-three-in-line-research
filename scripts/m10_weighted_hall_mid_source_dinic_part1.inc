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
int main(int argc,char**argv){

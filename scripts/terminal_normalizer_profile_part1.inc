#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;

constexpr int MAXM=10, MAXW=16;
using Rho=array<uint8_t,MAXM>;
struct Point{int x,y;};

long long cross(Point a,Point b,Point c){
  return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);
}
array<Point,4> block(int m,int s,int t,int e){
  int n=2*m; auto J=[n](int x){return n-1-x;};
  Point q0{s,e?J(t):t},q1{J(s),e?t:J(t)};
  return {q0,q1,Point{J(q0.y),q0.x},Point{J(q1.y),q1.x}};
}
bool pair_bad(int m,int sa,int ta,int ea,int sb,int tb,int eb){
  auto A=block(m,sa,ta,ea),B=block(m,sb,tb,eb);
  array<Point,8> p{};
  for(int i=0;i<4;i++){p[i]=A[i];p[i+4]=B[i];}
  for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)
    if(cross(p[i],p[j],p[k])==0)return true;
  return false;
}
bool triple_bad(int m,int a,int ta,int ea,int b,int tb,int eb,int c,int tc,int ec){
  auto A=block(m,a,ta,ea),B=block(m,b,tb,eb),C=block(m,c,tc,ec);
  for(auto x:A)for(auto y:B)for(auto z:C)if(cross(x,y,z)==0)return true;
  return false;
}
uint64_t encode(const Rho&r,int m){
  uint64_t x=0;for(int i=0;i<m;i++)x=(x<<4)|r[i];return x;
}
Rho switched(const Rho&r,int m,array<int,3>T){
  array<int,3> cyc{};int f=0,cur=min({T[0],T[1],T[2]});
  for(int k=0;k<m;k++){
    if(cur==T[0]||cur==T[1]||cur==T[2])cyc[f++]=cur;
    cur=r[cur];
  }
  Rho o=r;o[cyc[0]]=r[cyc[1]];o[cyc[1]]=r[cyc[2]];o[cyc[2]]=r[cyc[0]];
  return o;
}
struct CleanInfo{
  uint8_t components=0;
  array<int8_t,MAXM> comp{};
  array<int8_t,MAXM> colour{};
};
struct ProfileResult{
  int m=0;
  long long cycles=0,clean_cycles=0,clean_states=0,valid_states=0,unreached=0;
  vector<long long> distance;
  int max_distance=-1;
  long long terminal_cycles=0,terminal_states=0,closing_cycle_labels=0,incoming_signed_labels=0;
  int targets_with_incoming=0,min_normalizer=0,max_normalizer=0,max_target_labels=0;
  array<int,20> max_c_at_dyadic{};
  long long sqrt_num=0,sqrt_den=1;
  int sqrt_c=0,sqrt_t=1,sqrt_target_components=0,sqrt_ties=0;
  long long bound_square_num=0,bound_square_den=1;
};

ProfileResult run_case(int m){
  const int ROOTS=1<<m;
  const int WORDS=(ROOTS+63)/64;

  vector<array<int,3>> triples;
  for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)
    triples.push_back({a,b,c});
  int K=triples.size();

  vector<int8_t> rel((size_t)m*m*m*m,0);
  auto i4=[m](int a,int ta,int b,int tb){
    return ((size_t(a)*m+ta)*m+b)*m+tb;
  };
  for(int a=0;a<m;a++)for(int ta=0;ta<m;ta++)if(ta!=a)
    for(int b=a+1;b<m;b++)for(int tb=0;tb<m;tb++)
      if(tb!=b&&tb!=ta){
        bool eq=pair_bad(m,a,ta,0,b,tb,0);
        bool un=pair_bad(m,a,ta,0,b,tb,1);
        rel[i4(a,ta,b,tb)]=eq&&un?3:eq?2:un?1:0;
      }

  vector<uint8_t> badpat((size_t)K*m*m*m,0);
  auto ib=[m](int ti,int ta,int tb,int tc){
    return ((size_t(ti)*m+ta)*m+tb)*m+tc;
  };
  #pragma omp parallel for schedule(static)
  for(int ti=0;ti<K;ti++){
    auto T=triples[ti];
    for(int ta=0;ta<m;ta++)for(int tb=0;tb<m;tb++)for(int tc=0;tc<m;tc++){
      if(ta==tb||ta==tc||tb==tc||ta==T[0]||tb==T[1]||tc==T[2])continue;
      uint8_t mask=0;
      for(int p=0;p<8;p++)
        if(triple_bad(m,T[0],ta,p&1,T[1],tb,(p>>1)&1,T[2],tc,(p>>2)&1))
          mask|=uint8_t(1u<<p);
      badpat[ib(ti,ta,tb,tc)]=mask;
    }
  }

  vector<Rho> cycles;
  vector<int> tail(m-1);iota(tail.begin(),tail.end(),1);
  do{
    array<int,MAXM> ord{};Rho r{};ord[0]=0;
    for(int i=1;i<m;i++)ord[i]=tail[i-1];
    for(int i=0;i<m;i++)r[ord[i]]=ord[(i+1)%m];
    cycles.push_back(r);
  }while(next_permutation(tail.begin(),tail.end()));
  int C=cycles.size();

  unordered_map<uint64_t,int> index;
  index.reserve(C*2);
  for(int i=0;i<C;i++)index[encode(cycles[i],m)]=i;

  vector<int> clean_index(C,-1);
  vector<CleanInfo> infos;
  vector<int> clean_cycle;
  long long clean_states=0;
  for(int ci=0;ci<C;ci++){
    int8_t adj[MAXM][MAXM];
    for(int i=0;i<m;i++)for(int j=0;j<m;j++)adj[i][j]=-1;
    bool impossible=false;
    for(int a=0;a<m;a++)for(int b=a+1;b<m;b++){
      int v=rel[i4(a,cycles[ci][a],b,cycles[ci][b])];
      if(v==3){impossible=true;break;}
      if(v){
        int p=v==1?0:1;adj[a][b]=adj[b][a]=p;
      }

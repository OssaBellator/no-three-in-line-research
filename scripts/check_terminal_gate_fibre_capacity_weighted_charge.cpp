#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <map>
#include <cmath>
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;
using boost::multiprecision::uint256_t;

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
struct Result{
  int m=0;
  long long cycles=0,clean_cycles=0,clean_states=0,valid_states=0,unreached=0;
  vector<long long> distance;
  int max_distance=-1;
  long long terminal_cycles=0,terminal_states=0,lower_gate_nonempty=0,closing_gate_notfull=0;
  int min_active=999,max_active=0,min_root=999,max_root=0;
  long long total_active=0,total_minroot=0;
  uint256_t reverse_num=0, reverse_den=1;
  long double reverse_decimal=0;
  long double second_decimal=0;
  long long max_raw_incoming_labels=0;
  int reverse_target_components=0;
  long long reverse_target_cycles_tied=0;
  long long overloaded_target_cycles=0,overloaded_signed_columns=0;
};
Result run_case(int m){
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
    }
    if(impossible)continue;
    CleanInfo inf;inf.comp.fill(-1);inf.colour.fill(-1);
    bool ok=true;int cc=0;
    for(int root=0;root<m;root++)if(inf.comp[root]<0){
      array<int,MAXM> qq{};int head=0,tailq=0;qq[tailq++]=root;
      inf.comp[root]=cc;inf.colour[root]=0;
      while(head<tailq){
        int u=qq[head++];
        for(int v=0;v<m;v++)if(adj[u][v]>=0){
          int want=inf.colour[u]^adj[u][v];
          if(inf.comp[v]<0){inf.comp[v]=cc;inf.colour[v]=want;qq[tailq++]=v;}
          else if(inf.colour[v]!=want)ok=false;
        }
      }
      cc++;
    }
    if(!ok)continue;
    inf.components=cc;
    clean_index[ci]=infos.size();
    infos.push_back(inf);clean_cycle.push_back(ci);
    clean_states+=1LL<<cc;
  }
  int NC=infos.size();

  vector<array<array<uint64_t,MAXW>,MAXM>> varbits(MAXM+1);
  vector<array<uint64_t,MAXW>> fullmask(MAXM+1);
  for(int c=1;c<=m;c++){
    int roots=1<<c, words=(roots+63)/64;
    for(int w=0;w<words;w++){
      int left=roots-64*w;
      fullmask[c][w]=left>=64?~0ULL:(left<=0?0ULL:((1ULL<<left)-1));
    }
    for(int j=0;j<c;j++)for(int r=0;r<roots;r++)
      if((r>>j)&1)varbits[c][j][r>>6]|=1ULL<<(r&63);
  }

  vector<uint64_t> ownerbits((size_t)NC*m*WORDS,0);
  vector<uint64_t> reached((size_t)NC*WORDS,0);
  vector<long long> valid_per(NC,0);

  auto obase=[m,WORDS](int x,int owner){return ((size_t)x*m+owner)*WORDS;};
  #pragma omp parallel for schedule(dynamic,32)
  for(int x=0;x<NC;x++){
    int ci=clean_cycle[x], cc=infos[x].components;
    auto &inf=infos[x];
    for(int ti=0;ti<K;ti++){
      auto T=triples[ti];
      uint8_t bm=badpat[ib(ti,cycles[ci][T[0]],cycles[ci][T[1]],cycles[ci][T[2]])];
      if(!bm)continue;
      for(int w=0;w<WORDS;w++){
        uint64_t bs=0;
        for(int p=0;p<8;p++)if((bm>>p)&1){
          uint64_t term=fullmask[cc][w];
          for(int k=0;k<3;k++){
            int owner=T[k], comp=inf.comp[owner];
            int rootbit=((p>>k)&1)^inf.colour[owner];
            uint64_t vb=varbits[cc][comp][w];
            term &= rootbit?vb:(~vb&fullmask[cc][w]);
          }
          bs|=term;
        }
        ownerbits[obase(x,T[0])+w]|=bs;
        ownerbits[obase(x,T[1])+w]|=bs;
        ownerbits[obase(x,T[2])+w]|=bs;
      }
    }
    long long valid=0;
    for(int w=0;w<WORDS;w++){
      uint64_t any=0;
      for(int owner=0;owner<m;owner++)any|=ownerbits[obase(x,owner)+w];
      uint64_t v=(~any)&fullmask[cc][w];
      reached[(size_t)x*WORDS+w]=v;
      valid+=__builtin_popcountll(v);
    }
    valid_per[x]=valid;
  }
  long long valid_states=accumulate(valid_per.begin(),valid_per.end(),0LL);

  vector<int> neighbour((size_t)NC*K,-1);
  #pragma omp parallel for schedule(static)
  for(int x=0;x<NC;x++){
    int ci=clean_cycle[x];
    for(int ti=0;ti<K;ti++){
      auto it=index.find(encode(switched(cycles[ci],m,triples[ti]),m));
      int cj=it->second;
      neighbour[(size_t)x*K+ti]=clean_index[cj];
    }
  }

  vector<int8_t> cmin(NC,-1);
  queue<int> q;
  vector<long long> dist(32,0);
  dist[0]=valid_states;
  for(int x=0;x<NC;x++)if(valid_per[x]){cmin[x]=0;q.push(x);}
  while(!q.empty()){
    int eta=q.front();q.pop();
    int nd=cmin[eta]+1;
    for(int ti=0;ti<K;ti++){
      int rho=neighbour[(size_t)eta*K+ti];
      if(rho<0)continue;
      auto T=triples[ti];
      bool anynew=false;long long added=0;
      for(int w=0;w<WORDS;w++){
        uint64_t eligible=ownerbits[obase(rho,T[0])+w]|
                          ownerbits[obase(rho,T[1])+w]|
                          ownerbits[obase(rho,T[2])+w];
        uint64_t &seen=reached[(size_t)rho*WORDS+w];
        uint64_t fresh=eligible&~seen;
        if(fresh){seen|=fresh;anynew=true;added+=__builtin_popcountll(fresh);}
      }
      if(added)dist[nd]+=added;
      if(anynew&&cmin[rho]<0){cmin[rho]=nd;q.push(rho);}
    }
  }
  long long reached_total=accumulate(dist.begin(),dist.end(),0LL);
  int maxd=-1;for(int d=0;d<(int)dist.size();d++)if(dist[d])maxd=d;
  Result R;R.m=m;R.cycles=C;R.clean_cycles=NC;R.clean_states=clean_states;
  R.valid_states=valid_states;R.unreached=clean_states-reached_total;
  R.distance=dist;R.max_distance=maxd;
  int h=maxd;
  vector<long double> reverse_lower(NC,0.0L), reverse_upper(NC,0.0L);
  vector<long long> raw_incoming(NC,0);
  struct Gate{array<uint64_t,MAXW> elig{};int target=-1;};
  for(int x=0;x<NC;x++)if(cmin[x]==h){
    int cc=infos[x].components;array<uint64_t,MAXW> lower{},closing{};
    vector<Gate> gates;int active=0;
    for(int ti=0;ti<K;ti++){
      int y=neighbour[(size_t)x*K+ti];if(y<0)continue;auto T=triples[ti];
      array<uint64_t,MAXW> elig{};bool nonempty=false;
      for(int w=0;w<WORDS;w++){
        elig[w]=ownerbits[obase(x,T[0])+w]|ownerbits[obase(x,T[1])+w]|ownerbits[obase(x,T[2])+w];
        nonempty|=elig[w]!=0;if(cmin[y]<=h-2)lower[w]|=elig[w];if(cmin[y]<=h-1)closing[w]|=elig[w];
      }
      if(nonempty&&cmin[y]==h-1){gates.push_back({elig,y});active++;}
    }
    bool lowerEmpty=true,closingFull=true;for(int w=0;w<WORDS;w++){lowerEmpty&=lower[w]==0;closingFull&=closing[w]==fullmask[cc][w];}
    R.terminal_cycles++;R.terminal_states+=1LL<<cc;R.lower_gate_nonempty+=!lowerEmpty;R.closing_gate_notfull+=!closingFull;
    R.min_active=min(R.min_active,active);R.max_active=max(R.max_active,active);R.total_active+=active;
    int minmult=K,maxmult=0;
    for(int root=0;root<(1<<cc);root++){
      int mult=0; long long capacity_sum=0;
      for(auto const&g:gates) if((g.elig[root>>6]>>(root&63))&1ULL){
        mult++;
        capacity_sum += 1LL<<infos[g.target].components;
      }
      minmult=min(minmult,mult);maxmult=max(maxmult,mult);
      if(mult==0) continue;
      for(auto const&g:gates) if((g.elig[root>>6]>>(root&63))&1ULL){
        long double term=1.0L/(long double)capacity_sum;
        long double term_lo=nextafterl(term,-numeric_limits<long double>::infinity());
        long double term_hi=nextafterl(term, numeric_limits<long double>::infinity());
        reverse_lower[g.target]=nextafterl(reverse_lower[g.target]+term_lo,
          -numeric_limits<long double>::infinity());
        reverse_upper[g.target]=nextafterl(reverse_upper[g.target]+term_hi,
           numeric_limits<long double>::infinity());
        raw_incoming[g.target]++;
      }
    }
    R.min_root=min(R.min_root,minmult);R.max_root=max(R.max_root,maxmult);R.total_minroot+=minmult;
  }
  int floatingBest=-1, floatingSecond=-1;
  long double bestLower=0;
  for(int y=0;y<NC;y++){
    R.max_raw_incoming_labels=max(R.max_raw_incoming_labels,raw_incoming[y]);
    if(reverse_lower[y]>1.0L){R.overloaded_target_cycles++;R.overloaded_signed_columns+=1LL<<infos[y].components;}
    if(floatingBest<0||reverse_lower[y]>reverse_lower[floatingBest]){
      floatingSecond=floatingBest;floatingBest=y;
    }else if(floatingSecond<0||reverse_lower[y]>reverse_lower[floatingSecond]) floatingSecond=y;
    bestLower=max(bestLower,reverse_lower[y]);
  }
  R.reverse_decimal=reverse_lower[floatingBest];
  R.second_decimal=floatingSecond>=0?reverse_lower[floatingSecond]:0;

  // Outward-rounded intervals enclose every exact positive sum.  A target is
  // retained precisely when its upper endpoint can still meet the largest
  // lower endpoint; all retained targets are recomputed as exact rationals.
  vector<int> candidates;
  for(int y=0;y<NC;y++) if(reverse_upper[y]>=bestLower)candidates.push_back(y);
  vector<int> candidate_position(NC,-1);
  for(int i=0;i<(int)candidates.size();i++)candidate_position[candidates[i]]=i;
  vector<map<long long,long long>> denominator_counts(candidates.size());
  for(int x=0;x<NC;x++)if(cmin[x]==h){
    int cc=infos[x].components;
    vector<Gate> gates;
    for(int ti=0;ti<K;ti++){
      int y=neighbour[(size_t)x*K+ti];if(y<0||cmin[y]!=h-1)continue;auto T=triples[ti];
      array<uint64_t,MAXW> elig{};bool nonempty=false;
      for(int w=0;w<WORDS;w++){
        elig[w]=ownerbits[obase(x,T[0])+w]|ownerbits[obase(x,T[1])+w]|ownerbits[obase(x,T[2])+w];
        nonempty|=elig[w]!=0;
      }
      if(nonempty)gates.push_back({elig,y});
    }
    for(int root=0;root<(1<<cc);root++){
      long long capacity_sum=0;
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL)
        capacity_sum+=1LL<<infos[g.target].components;
      if(!capacity_sum)continue;
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL){
        int pos=candidate_position[g.target];
        if(pos>=0)denominator_counts[pos][capacity_sum]++;
      }
    }
  }
  using boost::multiprecision::cpp_int;
  auto gcd_big=[](cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;};
  auto exact_sum=[&](map<long long,long long> const& counts){
    cpp_int num=0,den=1;
    for(auto [d,c]:counts){
      cpp_int g=gcd_big(den,cpp_int(d));
      cpp_int newden=den/g*d;
      num=num*(newden/den)+cpp_int(c)*(newden/d);
      den=newden;
      cpp_int z=gcd_big(num,den);num/=z;den/=z;
    }
    return pair<cpp_int,cpp_int>{num,den};
  };
  cpp_int bestNum=0,bestDen=1;int bestIndex=-1;long long ties=0;
  for(int i=0;i<(int)candidates.size();i++){
    auto [num,den]=exact_sum(denominator_counts[i]);
    cpp_int left=num*bestDen,right=bestNum*den;
    if(bestIndex<0||left>right){bestNum=num;bestDen=den;bestIndex=candidates[i];ties=1;}
    else if(left==right)ties++;
  }
  R.reverse_num=uint256_t(bestNum);R.reverse_den=uint256_t(bestDen);
  R.reverse_target_components=infos[bestIndex].components;
  R.reverse_target_cycles_tied=ties;
  return R;
}

int main(int argc,char**argv){
  int first=8,last=10;if(argc>1)first=last=atoi(argv[1]);
  const int expectedH[11]={0,0,0,0,0,0,0,0,3,4,5};
  const long long expectedCycles[11]={0,0,0,0,0,0,0,0,436,2298,1260};
  const long long expectedStates[11]={0,0,0,0,0,0,0,0,33624,478040,535072};
  const char* expectedNum[11]={"0","0","0","0","0","0","0","0",
    "1468416446839930521721999",
    "406616023430754819367780545483294984597292560691",
    "5252950050653541320261353842660696885393101"};
  const char* expectedDen[11]={"1","1","1","1","1","1","1","1",
    "3789940340738886748063650",
    "708943793924084504981546740829982708967717363200",
    "33843848222070502440710524758866309866934400"};
  const long long expectedRaw[11]={0,0,0,0,0,0,0,0,1744,8574,8960};
  const int expectedComp[11]={0,0,0,0,0,0,0,0,8,8,9};
  cout<<setprecision(17)<<"{\n  \"cases\": [\n";
  for(int m=first;m<=last;m++){
    Result r=run_case(m);
    bool ok=!r.unreached&&!r.lower_gate_nonempty&&!r.closing_gate_notfull&&
      r.max_distance==expectedH[m]&&r.terminal_cycles==expectedCycles[m]&&
      r.terminal_states==expectedStates[m]&&
      r.reverse_num==uint256_t(expectedNum[m])&&r.reverse_den==uint256_t(expectedDen[m])&&
      r.max_raw_incoming_labels==expectedRaw[m]&&
      r.reverse_target_components==expectedComp[m]&&r.reverse_target_cycles_tied==2&&
      r.overloaded_target_cycles==0&&r.overloaded_signed_columns==0;
    if(!ok){cerr<<"capacity-weighted terminal ledger mismatch at m="<<m<<"\n";return 2;}
    cout<<"    {\"m\":"<<m
        <<",\"maximum_distance\":"<<r.max_distance
        <<",\"terminal_cycles\":"<<r.terminal_cycles
        <<",\"terminal_states\":"<<r.terminal_states
        <<",\"capacity_weighted_maximum_regenerated_reverse_load\":\""<<r.reverse_num<<"/"<<r.reverse_den<<"\""
        <<",\"capacity_weighted_maximum_decimal\":"<<(double)r.reverse_decimal
        <<",\"maximum_raw_incoming_terminal_labels\":"<<r.max_raw_incoming_labels
        <<",\"maximizing_target_components\":"<<r.reverse_target_components
        <<",\"maximizing_target_cycles_tied\":"<<r.reverse_target_cycles_tied
        <<",\"overloaded_target_cycles\":"<<r.overloaded_target_cycles
        <<",\"overloaded_signed_columns\":"<<r.overloaded_signed_columns<<"}"<<(m<last?",":"")<<"\n";
  }
  cout<<"  ],\n"
      <<"  \"target_cycle_weight_proportional_to_fibre_size\": true,\n"
      <<"  \"capacity_weighted_terminal_policy_contracts\": true,\n"
      <<"  \"uniform_bound_through_m10\": \"3/5\",\n"
      <<"  \"all_exact_regressions_verified\": true\n"
      <<"}\n";
}

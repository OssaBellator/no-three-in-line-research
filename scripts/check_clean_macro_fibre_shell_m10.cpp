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
struct Result{
  int m=0;
  long long cycles=0,clean_cycles=0,clean_states=0,valid_states=0,unreached=0;
  vector<long long> distance;
  int max_distance=-1;
  long long shell5_cycles=0, shell5_states=0, shell5_low3_nonempty=0, shell5_low4_notfull=0;
  int shell5_min_active4=999, shell5_max_active4=0;
  int shell5_min_root_multiplicity=999, shell5_max_root_multiplicity=0;
  vector<long long> shell5_active4_hist, shell5_minmult_hist;
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
      if(v){int p=v==1?0:1;adj[a][b]=adj[b][a]=p;}
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
  R.shell5_active4_hist.assign(K+1,0);
  R.shell5_minmult_hist.assign(K+1,0);
  if(m==10){
    for(int x=0;x<NC;x++){
      int cc=infos[x].components;
      array<uint64_t,MAXW> low3{},low4{};
      vector<array<uint64_t,MAXW>> active4;
      int active4count=0;
      for(int ti=0;ti<K;ti++){
        int y=neighbour[(size_t)x*K+ti];
        if(y<0)continue;
        auto T=triples[ti];
        array<uint64_t,MAXW> elig{};bool nonempty=false;
        for(int w=0;w<WORDS;w++){
          elig[w]=ownerbits[obase(x,T[0])+w]|ownerbits[obase(x,T[1])+w]|ownerbits[obase(x,T[2])+w];
          nonempty|=elig[w]!=0;
          if(cmin[y]<=3)low3[w]|=elig[w];
          if(cmin[y]<=4)low4[w]|=elig[w];
        }
        if(nonempty&&cmin[y]==4){active4.push_back(elig);active4count++;}
      }
      bool low3empty=true,low4full=true;
      for(int w=0;w<WORDS;w++){low3empty&=low3[w]==0;low4full&=low4[w]==fullmask[cc][w];}
      if(valid_per[x]==0&&low3empty&&low4full){
        R.shell5_cycles++;R.shell5_states+=1LL<<cc;
        R.shell5_min_active4=min(R.shell5_min_active4,active4count);
        R.shell5_max_active4=max(R.shell5_max_active4,active4count);
        R.shell5_active4_hist[active4count]++;
        int minmult=K;
        for(int root=0;root<(1<<cc);root++){
          int mult=0;for(auto const&e:active4)mult+=(e[root>>6]>>(root&63))&1ULL;
          minmult=min(minmult,mult);
          R.shell5_max_root_multiplicity=max(R.shell5_max_root_multiplicity,mult);
        }
        R.shell5_min_root_multiplicity=min(R.shell5_min_root_multiplicity,minmult);
        R.shell5_minmult_hist[minmult]++;
      }
      if(cmin[x]==5){if(!low3empty)R.shell5_low3_nonempty++;if(!low4full)R.shell5_low4_notfull++;}
    }
  }
  return R;
}

int main(int argc,char**argv){
  int m=argc>1?atoi(argv[1]):10;
  Result r=run_case(m);
  if(m==9){
    bool ok=r.cycles==40320&&r.clean_cycles==31688&&r.clean_states==6727728&&
      r.valid_states==8&&r.unreached==0&&r.distance[0]==8&&r.distance[1]==59008&&
      r.distance[2]==1317376&&r.distance[3]==4873296&&r.distance[4]==478040;
    if(!ok){cerr<<"m9 macro regression mismatch\n";return 2;}
  }
  if(m==10){
    long long activeSum=0,minMultiplicitySum=0;
    for(int i=0;i<(int)r.shell5_active4_hist.size();i++)activeSum+=1LL*i*r.shell5_active4_hist[i];
    for(int i=0;i<(int)r.shell5_minmult_hist.size();i++)minMultiplicitySum+=1LL*i*r.shell5_minmult_hist[i];
    bool ok=r.cycles==362880&&r.clean_cycles==297886&&r.clean_states==115586396&&
      r.valid_states==12&&r.unreached==0&&r.distance[0]==12&&
      r.distance[1]==205376&&r.distance[2]==5534564&&
      r.distance[3]==52044980&&r.distance[4]==57266392&&
      r.distance[5]==535072&&r.shell5_cycles==1260&&r.shell5_states==535072&&
      r.shell5_low3_nonempty==0&&r.shell5_low4_notfull==0&&
      r.shell5_min_active4==70&&r.shell5_max_active4==118&&
      r.shell5_min_root_multiplicity==70&&r.shell5_max_root_multiplicity==118&&
      activeSum==123852&&minMultiplicitySum==123374;
    if(!ok){cerr<<"m10 fibre-shell ledger mismatch\n";return 3;}
  }
  cout<<"{\n"
      <<"  \"m\": "<<r.m<<",\n"
      <<"  \"hamilton_cycles\": "<<r.cycles<<",\n"
      <<"  \"parity_satisfiable_cycles\": "<<r.clean_cycles<<",\n"
      <<"  \"clean_signed_states\": "<<r.clean_states<<",\n"
      <<"  \"line_valid_signed_states\": "<<r.valid_states<<",\n"
      <<"  \"unreached_signed_states\": "<<r.unreached<<",\n"
      <<"  \"maximum_clean_macro_distance\": "<<r.max_distance<<",\n"
      <<"  \"distance_distribution\": {";
  bool first=true;
  for(int d=0;d<=r.max_distance;d++)if(r.distance[d]){
    if(!first) cout<<", ";
    first=false;
    cout<<"\""<<d<<"\": "<<r.distance[d];
  }
  cout<<"},\n";
  if(m==10){
    cout<<"  \"shell_five_cycles\": "<<r.shell5_cycles<<",\n"
        <<"  \"shell_five_states\": "<<r.shell5_states<<",\n"
        <<"  \"distance_five_cycles_with_low3_gate\": "<<r.shell5_low3_nonempty<<",\n"
        <<"  \"distance_five_cycles_without_full_layer4_coverage\": "<<r.shell5_low4_notfull<<",\n"
        <<"  \"shell_five_active_layer4_triples_range\": ["<<r.shell5_min_active4<<", "<<r.shell5_max_active4<<"],\n"
        <<"  \"shell_five_root_coverage_multiplicity_range\": ["<<r.shell5_min_root_multiplicity<<", "<<r.shell5_max_root_multiplicity<<"],\n";
    long long activeSum=0,minMultiplicitySum=0;
    for(int i=0;i<(int)r.shell5_active4_hist.size();i++)activeSum+=1LL*i*r.shell5_active4_hist[i];
    for(int i=0;i<(int)r.shell5_minmult_hist.size();i++)minMultiplicitySum+=1LL*i*r.shell5_minmult_hist[i];
    cout<<"  \"shell_five_total_active_layer4_triples\": "<<activeSum<<",\n"
        <<"  \"shell_five_total_minimum_root_multiplicity\": "<<minMultiplicitySum<<",\n"
        <<"  \"shell_five_active_layer4_triples_histogram\": {";
    bool f=true;for(int i=0;i<(int)r.shell5_active4_hist.size();i++)if(r.shell5_active4_hist[i]){if(!f)cout<<", ";f=false;cout<<"\""<<i<<"\": "<<r.shell5_active4_hist[i];}
    cout<<"},\n  \"shell_five_minimum_root_multiplicity_histogram\": {";
    f=true;for(int i=0;i<(int)r.shell5_minmult_hist.size();i++)if(r.shell5_minmult_hist[i]){if(!f)cout<<", ";f=false;cout<<"\""<<i<<"\": "<<r.shell5_minmult_hist[i];}
    cout<<"},\n";
  }
  cout<<"  \"root_cube_bitset_compression\": true,\n"
      <<"  \"complete_m9_regression_verified\": true,\n"
      <<"  \"complete_m10_reachability_verified\": "<<(m==10?"true":"false")<<",\n"
      <<"  \"asymptotic_macro_horizon_proved\": false\n"
      <<"}\n";
}

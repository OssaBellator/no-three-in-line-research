#include <algorithm>
#include <array>
#include <cstdint>
#include <deque>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int M=8, N=16, Q=1<<M;
using Rho=array<uint8_t,M>;
struct H{size_t operator()(Rho const&a)const noexcept{size_t h=0;for(auto x:a)h=h*13+x+1;return h;}};
struct Point{int x,y;};
struct Assignment{array<Point,4> p;};
bool col(Point a,Point b,Point c){return 1LL*(b.x-a.x)*(c.y-a.y)==1LL*(b.y-a.y)*(c.x-a.x);}
vector<Rho> cycles(){vector<Rho> out;array<int,M-1> t{};iota(t.begin(),t.end(),1);do{array<int,M> o{};o[0]=0;for(int i=1;i<M;i++)o[i]=t[i-1];Rho r{};for(int i=0;i<M;i++)r[o[i]]=o[(i+1)%M];out.push_back(r);}while(next_permutation(t.begin(),t.end()));return out;}
Rho sw(Rho const&r,uint8_t mask){int start=0;while(!(mask&(1<<start)))start++;array<int,3>s{};int c=0,cur=start;for(int z=0;z<M;z++){if(mask&(1<<cur))s[c++]=cur;cur=r[cur];}Rho o=r;int b0=r[s[0]],b1=r[s[1]],b2=r[s[2]];o[s[0]]=b1;o[s[1]]=b2;o[s[2]]=b0;return o;}
int main(){
 auto rhos=cycles(); unordered_map<Rho,int,H> rid; for(int i=0;i<(int)rhos.size();i++)rid[rhos[i]]=i;
 vector<uint8_t> pair_masks; for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)pair_masks.push_back((1<<a)|(1<<b));
 vector<uint8_t> triple_masks; for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)for(int c=b+1;c<M;c++)triple_masks.push_back((1<<a)|(1<<b)|(1<<c));
 array<uint32_t,M> incident{}; for(int i=0;i<(int)pair_masks.size();i++)for(int s=0;s<M;s++)if(pair_masks[i]&(1<<s))incident[s]|=1u<<i;
 auto J=[](int x){return N-1-x;};
 vector<Assignment> asg; int id[M][M][2]; fill(&id[0][0][0],&id[0][0][0]+M*M*2,-1);
 for(int s=0;s<M;s++)for(int t=0;t<M;t++)if(s!=t)for(int e=0;e<2;e++){
  Point q0{s,e?J(t):t},q1{J(s),e?t:J(t)};
  Assignment A{{q0,q1,Point{J(q0.y),q0.x},Point{J(q1.y),q1.x}}}; id[s][t][e]=asg.size(); asg.push_back(A);
 }
 int A=asg.size(); vector<uint8_t> pc(A*A); vector<uint8_t> tc((size_t)A*A*A);
 for(int a=0;a<A;a++)for(int b=a+1;b<A;b++){int cnt=0;for(int x=0;x<4;x++)for(int y=x+1;y<4;y++)for(int z=0;z<4;z++)cnt+=col(asg[a].p[x],asg[a].p[y],asg[b].p[z]);for(int x=0;x<4;x++)for(int y=x+1;y<4;y++)for(int z=0;z<4;z++)cnt+=col(asg[b].p[x],asg[b].p[y],asg[a].p[z]);pc[a*A+b]=pc[b*A+a]=cnt;}
 for(int a=0;a<A;a++)for(int b=a+1;b<A;b++)for(int c=b+1;c<A;c++){int cnt=0;for(int x=0;x<4;x++)for(int y=0;y<4;y++)for(int z=0;z<4;z++)cnt+=col(asg[a].p[x],asg[b].p[y],asg[c].p[z]);int p[6][3]={{a,b,c},{a,c,b},{b,a,c},{b,c,a},{c,a,b},{c,b,a}};for(auto&q:p)tc[((size_t)q[0]*A+q[1])*A+q[2]]=cnt;}
 int S=rhos.size()*Q; vector<uint16_t> defects(S); vector<uint32_t> pb(S); vector<uint64_t> tb(S); vector<int> sel(M);
 int minD=9999; vector<int> targets;
 for(int ri=0;ri<(int)rhos.size();ri++)for(int code=0;code<Q;code++){
  int st=ri*Q+code;for(int s=0;s<M;s++)sel[s]=id[s][rhos[ri][s]][(code>>s)&1];
  int d=0,pi=0,ti=0;uint32_t pm=0;uint64_t tm=0;
  for(int i=0;i<M;i++)for(int j=i+1;j<M;j++,pi++){int v=pc[sel[i]*A+sel[j]];d+=v;if(v)pm|=1u<<pi;}
  for(int i=0;i<M;i++)for(int j=i+1;j<M;j++)for(int k=j+1;k<M;k++,ti++){int v=tc[((size_t)sel[i]*A+sel[j])*A+sel[k]];d+=v;if(v)tm|=1ull<<ti;}
  defects[st]=d;pb[st]=pm;tb[st]=tm;minD=min(minD,d);
 }
 for(int st=0;st<S;st++)if(defects[st]==minD)targets.push_back(st);
 vector<int8_t> dist(S,-1);deque<int>dq;for(int x:targets){dist[x]=0;dq.push_back(x);}
 while(!dq.empty()){
  int y=dq.front();dq.pop_front();int ri=y/Q,code=y%Q;
  for(int s=0;s<M;s++){int x=y^(1<<s);if((pb[x]&incident[s])&&dist[x]<0){dist[x]=dist[y]+1;dq.push_back(x);}}
  for(int ti=0;ti<(int)triple_masks.size();ti++){
   uint8_t mask=triple_masks[ti];Rho xr=sw(rhos[ri],mask);int base=rid[xr]*Q;int outside=code&~mask;
   array<int,3> ss{};int cc=0;for(int s=0;s<M;s++)if(mask&(1<<s))ss[cc++]=s;
   for(int fresh=0;fresh<8;fresh++){int xc=outside;for(int k=0;k<3;k++)xc|=((fresh>>k)&1)<<ss[k];int x=base+xc;if(((tb[x]>>ti)&1ull)&&dist[x]<0){dist[x]=dist[y]+1;dq.push_back(x);}}
  }
 }
 array<long long,32> hist{};long long un=0;int md=0;for(auto d:dist){if(d<0)un++;else{hist[d]++;md=max(md,(int)d);}}
 bool ok=S==1290240&&minD==0&&targets.size()==28&&un==0&&md==5&&hist[0]==28&&hist[1]==1560&&hist[2]==57408&&hist[3]==736212&&hist[4]==493728&&hist[5]==1304;
 if(!ok){cerr<<"verification mismatch\n";return 1;}
 cout<<"{\n  \"m\":8,\n  \"states\":"<<S<<",\n  \"minimum_triples\":"<<minD<<",\n  \"minimum_states\":"<<targets.size()<<",\n  \"unreachable_states\":"<<un<<",\n  \"maximum_distance_to_minimum\":"<<md<<",\n  \"distance_distribution\":{";
 for(int i=0;i<=md;i++){if(i)cout<<",";cout<<"\""<<i<<"\":"<<hist[i];}
 cout<<"},\n  \"maximum_strict_descent_horizon_upper_bound\":5,\n  \"verified\":true\n}\n";
}

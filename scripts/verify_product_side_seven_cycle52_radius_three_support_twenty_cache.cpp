#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
constexpr int PAIRS[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
using S=std::array<uint16_t,14>; using A=std::array<int8_t,14>;
struct Hash{size_t operator()(S const&s)const noexcept{uint64_t h=1469598103934665603ULL;for(auto x:s){h^=x;h*=1099511628211ULL;}return h;}};
const std::array<int,7> hp={1,2,3,4,0,6,5},pp={4,5,6,1,3,2,0}; const std::array<int,14>opts={2,2,2,2,2,2,2,2,2,2,2,5,0,2};
S centre(){S s{};for(int sr=0;sr<14;sr++){int o=sr/7,u=sr%7,z=o?pp[u]:u;int ad[4]={z,hp[z],7+z,7+hp[z]};int r=7*o+z;for(int k=0;k<2;k++)s[r]|=1u<<ad[PAIRS[opts[sr]][k]];}return s;}
std::array<uint16_t,14> host(){std::array<uint16_t,14>x{};for(int o=0;o<2;o++)for(int z=0;z<7;z++)x[7*o+z]=(1u<<z)|(1u<<hp[z])|(1u<<(7+z))|(1u<<(7+hp[z]));return x;}
struct E{S s;std::array<uint16_t,14>h{},at{};std::unordered_set<S,Hash>ns;std::vector<int>rs,cs;int st;void dfs(int r,uint16_t ur,uint16_t uc){uint16_t u=h[r]&~s[r];while(u){int c=__builtin_ctz(u);u&=u-1;if(uc>>c&1)continue;uint16_t q=at[c];while(q){int rr=__builtin_ctz(q);q&=q-1;if(rr==st){if(rs.size()<2)continue;S f=s;for(size_t i=0;i<cs.size();i++){int oc=cs[i];f[rs[i]]^=1u<<oc;f[rs[i+1]]^=1u<<oc;}f[rs.back()]^=1u<<c;f[st]^=1u<<c;ns.insert(f);}else if(!(ur>>rr&1)&&rr>=st){rs.push_back(rr);cs.push_back(c);dfs(rr,ur|(1u<<rr),uc|(1u<<c));cs.pop_back();rs.pop_back();}}}}void run(){at.fill(0);ns.clear();for(int c=0;c<14;c++)for(int r=0;r<14;r++)if(s[r]>>c&1)at[c]|=1u<<r;for(st=0;st<14;st++){rs={st};cs.clear();dfs(st,1u<<st,0);}}};
int supp(const S&a,const S&b){int d=0;for(int r=0;r<14;r++)d+=__builtin_popcount(a[r]^b[r]);return d;}
struct P{int x,y;};inline int det(P a,P b,P c){return(b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);}
struct TopEnum{
 std::array<uint16_t,7>sig{3,768,12,3072,144,8224,4160};std::array<int8_t,14>asg{};std::array<uint8_t,2>used{};std::vector<A>sol;int mode=0;uint64_t nodes=0;
 bool clean_partial()const{std::array<P,14>p{};int n=0;for(int r=0;r<7;r++){uint16_t m=sig[r];while(m){int c=__builtin_ctz(m);m&=m-1;if(asg[c]>=0){int y=mode==0?7*(c/7)+asg[c]:2*asg[c]+c/7;p[n++]={r,y};}}}for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++)if(det(p[i],p[j],p[k])==0)return false;return true;}
 void dfs(int d){nodes++;if(d==14){sol.push_back(asg);return;}int bv=-1,best=8;std::array<int8_t,7>dom{};int dc=0;for(int v=0;v<14;v++)if(asg[v]<0){int g=v/7,c=0;std::array<int8_t,7>x{};for(int z=0;z<7;z++)if(!(used[g]>>z&1)){asg[v]=z;if(clean_partial())x[c++]=z;asg[v]=-1;}if(!c)return;if(c<best){best=c;bv=v;dc=c;dom=x;}}int g=bv/7;for(int i=0;i<dc;i++){int z=dom[i];asg[bv]=z;used[g]|=1u<<z;dfs(d+1);used[g]&=~(1u<<z);asg[bv]=-1;}}
 void run(int m){mode=m;asg.fill(-1);used.fill(0);sol.clear();nodes=0;dfs(0);}
};
struct BottomGroup{
 std::vector<S>cand;std::array<uint16_t,14>ho;A a{};std::array<int8_t,7>r{};uint8_t used=0;int ori=0;uint64_t nodes=0;std::array<uint64_t,196>emask{};uint64_t all=0;
 int point(int edge)const{int row=edge/14,c=edge%14,z=row%7;int rp=row<7?z:r[z];int x=ori<2?(row<7?rp:7+rp):2*rp+(row<7?0:1);int y=ori%2==0?7*(c/7)+a[c]:2*a[c]+c/7;return 14*x+y;}
 uint64_t transition(int z,uint64_t active)const{std::vector<int>prior,nw;for(int rr=0;rr<7;rr++){uint16_t m=cand[0][rr];while(m){int c=__builtin_ctz(m);m&=m-1;prior.push_back(14*rr+c);}}for(int rr=7;rr<14;rr++){uint16_t m=ho[rr];while(m){int c=__builtin_ctz(m);m&=m-1;int e=14*rr+c;if(r[rr%7]<0)continue;(rr%7==z?nw:prior).push_back(e);}}for(int e:nw){int pe=point(e);for(int i=0;i<(int)prior.size();i++)for(int j=i+1;j<(int)prior.size();j++){int f=prior[i],g=prior[j],pf=point(f),pg=point(g);if(det({pe/14,pe%14},{pf/14,pf%14},{pg/14,pg%14})==0)active&=~(emask[e]&emask[f]&emask[g]);}prior.push_back(e);if(!active)break;}return active;}
 bool dfs(int d,uint64_t active){nodes++;if(d==7)return active!=0;int bz=-1,best=8;std::array<int8_t,7>dom{};int dc=0;for(int z=0;z<7;z++)if(r[z]<0){std::array<int8_t,7>x{};int c=0;for(int v=0;v<7;v++)if(!(used>>v&1)){r[z]=v;auto ch=transition(z,active);r[z]=-1;if(ch)x[c++]=v;}if(!c)return false;if(c<best){best=c;bz=z;dc=c;dom=x;}}for(int i=0;i<dc;i++){int v=dom[i];r[bz]=v;used|=1u<<v;auto ch=transition(bz,active);if(dfs(d+1,ch))return true;used&=~(1u<<v);r[bz]=-1;}return false;}
 bool solve(const std::vector<S>&cs,const A&aa,int o){cand=cs;a=aa;ori=o;ho=host();r.fill(-1);used=0;nodes=0;all=cand.size()==64?~0ULL:((1ULL<<cand.size())-1);emask.fill(0);for(int i=0;i<(int)cand.size();i++)for(int rr=0;rr<14;rr++){uint16_t m=cand[i][rr];while(m){int c=__builtin_ctz(m);m&=m-1;emask[14*rr+c]|=1ULL<<i;}}return dfs(0,all);}
};
int main(int argc,char**argv){
 S c=centre();E e;e.s=c;e.h=host();e.run();auto r1=e.ns;assert(r1.size()==364);std::unordered_set<S,Hash>r2;for(auto const&p:r1){e.s=p;e.run();for(auto const&v:e.ns)if(v!=c&&!r1.count(v))r2.insert(v);}assert(r2.size()==26550);std::unordered_set<S,Hash>r3;for(auto const&p:r2){e.s=p;e.run();for(auto const&v:e.ns)if(v!=c&&!r1.count(v)&&!r2.count(v)&&supp(c,v)==20)r3.insert(v);}assert(r3.size()==71860);std::array<uint16_t,7>sig{3,768,12,3072,144,8224,4160};std::vector<S>group;for(auto const&s:r3){bool ok=true;for(int i=0;i<7;i++)ok&=s[i]==sig[i];if(ok)group.push_back(s);}std::sort(group.begin(),group.end());assert(group.size()==46);
 if(argc==2&&std::string(argv[1])=="interleaved"){
  TopEnum t;t.run(1);assert(t.sol.size()==1584);assert(t.nodes==39556);const uint64_t expected[2]={6842,9539};for(int k=0;k<2;k++){int ori=1+2*k;uint64_t total=0;for(auto const&a:t.sol){BottomGroup b;assert(!b.solve(group,a,ori));total+=b.nodes;}assert(total==expected[k]);std::cout<<"orientation="<<ori<<" top_orders="<<t.sol.size()<<" bottom_nodes="<<total<<" PASS\n";}return 0;
 }
 assert(argc==4&&std::string(argv[1])=="concatenated");int ori=std::stoi(argv[2]),shard=std::stoi(argv[3]);assert((ori==0||ori==2)&&shard>=0&&shard<16);TopEnum t;t.run(0);assert(t.sol.size()==65296);assert(t.nodes==576716);const uint64_t expected0[16]={15379,16924,16151,17392,18612,17058,19270,17197,20011,19395,17881,18030,19376,18309,18658,21568};const uint64_t expected2[16]={16400,15371,17044,16062,18929,17101,18064,20345,17543,20796,19178,18612,18694,18210,21444,20020};int first=shard*4081,last=first+4081;uint64_t total=0;for(int i=first;i<last;i++){BottomGroup b;assert(!b.solve(group,t.sol[i],ori));total+=b.nodes;}assert(total==(ori==0?expected0[shard]:expected2[shard]));std::cout<<"orientation="<<ori<<" shard="<<shard<<" top_orders="<<last-first<<" bottom_nodes="<<total<<" PASS\n";
}

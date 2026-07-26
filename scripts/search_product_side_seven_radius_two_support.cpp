// Generic exact radius-two support-range search for side-seven selectors.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>

constexpr int PAIRS[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
using Selector=std::array<uint16_t,14>;
struct Hash{size_t operator()(Selector const&s)const noexcept{uint64_t h=1469598103934665603ULL;for(auto x:s){h^=x;h*=1099511628211ULL;}return h;}};
struct Case{std::string name;std::array<int,7>h,p;std::array<int,14>opts;int n1;};
const std::array<Case,4> C={{
{"cycle7",{1,2,3,4,5,6,0},{5,4,0,6,2,1,3},{0,3,0,3,5,2,2,2,2,3,0,5,5,2},1092},
{"cycle52",{1,2,3,4,0,6,5},{4,5,6,1,3,2,0},{2,2,2,2,2,2,2,2,2,2,2,5,0,2},364},
{"cycle43",{1,2,3,0,5,6,4},{3,5,4,2,1,0,6},{5,5,2,0,0,5,2,0,0,5,5,0,3,3},180},
{"cycle322",{1,2,0,4,3,6,5},{4,6,5,3,1,2,0},{5,0,3,1,0,5,0,5,5,0,4,3,5,0},112}
}};
Selector centre(const Case&d){Selector s{};for(int sr=0;sr<14;sr++){int o=sr/7,u=sr%7,z=o?d.p[u]:u;int a[4]={z,d.h[z],7+z,7+d.h[z]};int r=7*o+z;for(int k=0;k<2;k++)s[r]|=1u<<a[PAIRS[d.opts[sr]][k]];}return s;}
std::array<uint16_t,14> host(const Case&d){std::array<uint16_t,14>x{};for(int o=0;o<2;o++)for(int z=0;z<7;z++)x[7*o+z]=(1u<<z)|(1u<<d.h[z])|(1u<<(7+z))|(1u<<(7+d.h[z]));return x;}
struct E{Selector s;std::array<uint16_t,14>h{},at{};std::unordered_set<Selector,Hash> ns;std::vector<int>rs,cs;int st;
void dfs(int r,uint16_t ur,uint16_t uc){uint16_t u=h[r]&~s[r];while(u){int c=__builtin_ctz(u);u&=u-1;if(uc>>c&1)continue;uint16_t q=at[c];while(q){int rr=__builtin_ctz(q);q&=q-1;if(rr==st){if(rs.size()<2)continue;Selector f=s;for(size_t i=0;i<cs.size();i++){int oc=cs[i];f[rs[i]]^=1u<<oc;f[rs[i+1]]^=1u<<oc;}f[rs.back()]^=1u<<c;f[st]^=1u<<c;ns.insert(f);}else if(!(ur>>rr&1)&&rr>=st){rs.push_back(rr);cs.push_back(c);dfs(rr,ur|(1u<<rr),uc|(1u<<c));cs.pop_back();rs.pop_back();}}}}
void run(){at.fill(0);ns.clear();for(int c=0;c<14;c++)for(int r=0;r<14;r++)if(s[r]>>c&1)at[c]|=1u<<r;for(st=0;st<14;st++){rs={st};cs.clear();dfs(st,1u<<st,0);}}
};
struct Point{int x,y;};
inline int det(const Point&a,const Point&b,const Point&c){return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);}
struct Spec{bool top;uint8_t label,col;};
struct CSP{
 struct Mask{uint64_t w[4]{};inline void add(const Mask&o){for(int i=0;i<4;i++)w[i]|=o.w[i];}inline bool has(int id)const{return(w[id>>6]>>(id&63))&1ULL;}};
 static std::array<std::array<Mask,196>,196> lines;static bool ready;
 std::array<Spec,28>spec{};std::array<int8_t,21>asg{};std::array<uint8_t,3>used{};std::array<std::array<uint8_t,2>,21>touch{};std::array<uint8_t,21>tc{};std::array<uint8_t,28>complete{},list{},pid{};int count=0,ori=0;uint64_t nodes=0;
 static void init(){if(ready)return;for(int a=0;a<196;a++){Point pa{a/14,a%14};for(int b=0;b<196;b++){if(a==b)continue;Point pb{b/14,b%14};for(int c=0;c<196;c++){Point pc{c/14,c%14};if(det(pa,pb,pc)==0)lines[a][b].w[c>>6]|=1ULL<<(c&63);}}}ready=true;}
 int group(int v)const{return v<7?0:v<14?1:2;}bool done(int i)const{auto&p=spec[i];return asg[p.col]>=0&&(p.top||asg[14+p.label]>=0);}int id(int i)const{auto&p=spec[i];int r=p.top?p.label:asg[14+p.label];int x=ori<2?(p.top?r:7+r):2*r+(p.top?0:1);int oc=p.col/7,cp=asg[p.col];int y=ori%2==0?7*oc+cp:2*cp+oc;return14*x+y;}
 int newly(int v,std::array<uint8_t,2>&o){int n=0;for(int k=0;k<tc[v];k++){int i=touch[v][k];if(!complete[i]&&done(i))o[n++]=i;}return n;}
 bool valid(const Mask&d,const std::array<uint8_t,2>&n,int nc,std::array<uint8_t,2>&ids)const{if(!nc)return true;ids[0]=id(n[0]);if(d.has(ids[0]))return false;if(nc==2){ids[1]=id(n[1]);if(d.has(ids[1]))return false;for(int i=0;i<count;i++)if(lines[ids[0]][pid[list[i]]].has(ids[1]))return false;}return true;}
 bool allowed(int v,int z,const Mask&d){int g=group(v);if(used[g]>>z&1)return false;asg[v]=z;std::array<uint8_t,2>n{},ids{};int nc=newly(v,n);bool ok=valid(d,n,nc,ids);asg[v]=-1;return ok;}
 bool search(int depth,const Mask&d){++nodes;if(depth==21)return true;int bv=-1,best=8,dc=0;std::array<int8_t,7>dom{};for(int v=0;v<21;v++)if(asg[v]<0){std::array<int8_t,7>x{};int c=0;for(int z=0;z<7;z++)if(allowed(v,z,d))x[c++]=z;if(!c)return false;if(c<best){best=c;bv=v;dc=c;dom=x;if(c==1)break;}}int g=group(bv);for(int q=0;q<dc;q++){int z=dom[q];asg[bv]=z;used[g]|=1u<<z;std::array<uint8_t,2>n{},ids{};int nc=newly(bv,n);assert(valid(d,n,nc,ids));Mask child=d;for(int k=0;k<nc;k++){int i=n[k],x=ids[k];for(int j=0;j<count;j++)child.add(lines[x][pid[list[j]]]);for(int j=0;j<k;j++)child.add(lines[x][ids[j]]);complete[i]=1;pid[i]=x;list[count++]=i;}if(search(depth+1,child))return true;for(int k=nc-1;k>=0;k--){--count;complete[n[k]]=0;}used[g]&=~(1u<<z);asg[bv]=-1;}return false;}
 bool solve(const Selector&s,int o){init();ori=o;asg.fill(-1);used.fill(0);complete.fill(0);tc.fill(0);count=0;nodes=0;int n=0;for(int r=0;r<14;r++){uint16_t m=s[r];while(m){int c=__builtin_ctz(m);m&=m-1;spec[n]={r<7,(uint8_t)(r%7),(uint8_t)c};touch[c][tc[c]++]=n;if(r>=7)touch[14+r%7][tc[14+r%7]++]=n;n++;}}assert(n==28);Mask empty{};return search(0,empty);}
};
std::array<std::array<CSP::Mask,196>,196>CSP::lines{};bool CSP::ready=false;
int main(int argc,char**argv){assert(argc==5);std::string req=argv[1];int support=std::stoi(argv[2]),lo=std::stoi(argv[3]),hi=std::stoi(argv[4]);for(auto&d:C)if(req==d.name){Selector c=centre(d);E e;e.s=c;e.h=host(d);e.run();assert((int)e.ns.size()==d.n1);auto r1=e.ns;std::set<Selector>layer;for(auto const&p:r1){e.s=p;e.run();for(auto const&v:e.ns){if(v==c||r1.count(v))continue;int diff=0;for(int r=0;r<14;r++)diff+=__builtin_popcount(v[r]^c[r]);if(diff==support)layer.insert(v);}}std::cerr<<d.name<<" support="<<support<<" layer="<<layer.size()<<"\n";uint64_t total=0;int index=0,tested=0;for(auto const&s:layer){++index;if(index<lo||index>hi)continue;++tested;for(int o=0;o<4;o++){CSP solver;bool ok=solver.solve(s,o);total+=solver.nodes;if(ok){std::cout<<"FOUND "<<d.name<<" index="<<index<<" orientation="<<o<<" nodes="<<total<<" selector=";for(auto x:s)std::cout<<x<<",";std::cout<<"\n";return2;}}}std::cout<<d.name<<" range="<<lo<<"-"<<hi<<" done="<<tested<<" nodes="<<total<<" NO\n";return0;}assert(false);}

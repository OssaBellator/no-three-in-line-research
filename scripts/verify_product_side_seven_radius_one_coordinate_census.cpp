// Exact radius-one selector-coordinate census for PX515--PX518.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

constexpr int PAIRS[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
struct Point{int x,y;};
inline int det(const Point&a,const Point&b,const Point&c){return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);}
using Selector=std::array<uint16_t,14>;
struct CaseData{std::string name;std::array<int,7>h,p;std::array<int,14>opts;int expected;std::vector<uint64_t> shard_nodes;};
const std::array<CaseData,4> CASES={{
{"cycle7",{1,2,3,4,5,6,0},{5,4,0,6,2,1,3},{0,3,0,3,5,2,2,2,2,3,0,5,5,2},1092,
 {35038440ULL,43056369ULL,52194270ULL,53689245ULL,56565762ULL,56142863ULL,80332273ULL,81151641ULL,72506987ULL,70629491ULL,61920921ULL,86223848ULL}},
{"cycle52",{1,2,3,4,0,6,5},{4,5,6,1,3,2,0},{2,2,2,2,2,2,2,2,2,2,2,5,0,2},364,
 {22028716ULL,26803106ULL,32454263ULL,22515188ULL,34349868ULL,32685591ULL,30715924ULL,35978982ULL}},
{"cycle43",{1,2,3,0,5,6,4},{3,5,4,2,1,0,6},{5,5,2,0,0,5,2,0,0,5,5,0,3,3},180,
 {28948065ULL,33000425ULL,39819541ULL,53866507ULL}},
{"cycle322",{1,2,0,4,3,6,5},{4,6,5,3,1,2,0},{5,0,3,1,0,5,0,5,5,0,4,3,5,0},112,{59379166ULL}}
}};
Selector centre(const CaseData&d){Selector s{};for(int sr=0;sr<14;++sr){int o=sr/7,u=sr%7,z=o?d.p[u]:u;int a[4]={z,d.h[z],7+z,7+d.h[z]};int r=7*o+z;for(int k=0;k<2;k++)s[r]|=1u<<a[PAIRS[d.opts[sr]][k]];}return s;}
std::array<uint16_t,14> host(const CaseData&d){std::array<uint16_t,14>h{};for(int o=0;o<2;o++)for(int z=0;z<7;z++){int r=7*o+z;h[r]=(1u<<z)|(1u<<d.h[z])|(1u<<(7+z))|(1u<<(7+d.h[z]));}return h;}
struct Enum{Selector s;std::array<uint16_t,14>h{},at{};std::set<Selector>ns;std::vector<int>rs,cs;int st;
 void dfs(int r,uint16_t ur,uint16_t uc){uint16_t u=h[r]&~s[r];while(u){int c=__builtin_ctz(u);u&=u-1;if(uc>>c&1)continue;uint16_t q=at[c];while(q){int rr=__builtin_ctz(q);q&=q-1;if(rr==st){if(rs.size()<2)continue;Selector f=s;for(size_t i=0;i<cs.size();i++){int oc=cs[i];f[rs[i]]^=1u<<oc;f[rs[i+1]]^=1u<<oc;}f[rs.back()]^=1u<<c;f[st]^=1u<<c;ns.insert(f);}else if(!(ur>>rr&1)&&rr>=st){rs.push_back(rr);cs.push_back(c);dfs(rr,ur|(1u<<rr),uc|(1u<<c));cs.pop_back();rs.pop_back();}}}}
 void run(){for(int c=0;c<14;c++)for(int r=0;r<14;r++)if(s[r]>>c&1)at[c]|=1u<<r;for(st=0;st<14;st++){rs={st};cs.clear();dfs(st,1u<<st,0);}}
};
struct Spec{bool top;uint8_t label,col;};
struct CSP{
 struct Mask{uint64_t w[4]{};void add(const Mask&o){for(int i=0;i<4;i++)w[i]|=o.w[i];}bool has(int id)const{return (w[id>>6]>>(id&63))&1ULL;}};
 static std::array<std::array<Mask,196>,196> lines;static bool ready;
 std::array<Spec,28>spec{};std::array<int8_t,21>asg{};std::array<uint8_t,3>used{};
 std::array<std::array<uint8_t,2>,21>touch{};std::array<uint8_t,21>tc{};
 std::array<uint8_t,28>complete{},list{},pid{};int count=0,ori=0;uint64_t nodes=0;
 static void init(){if(ready)return;for(int a=0;a<196;a++){Point x{a/14,a%14};for(int b=0;b<196;b++){if(a==b)continue;Point y{b/14,b%14};for(int c=0;c<196;c++){Point z{c/14,c%14};if(det(x,y,z)==0)lines[a][b].w[c>>6]|=1ULL<<(c&63);}}}ready=true;}
 int group(int v)const{return v<7?0:v<14?1:2;}
 bool done(int i)const{auto&p=spec[i];return asg[p.col]>=0&&(p.top||asg[14+p.label]>=0);}
 int id(int i)const{auto&p=spec[i];int rp=p.top?p.label:asg[14+p.label];int x=ori<2?(p.top?rp:7+rp):2*rp+(p.top?0:1);int j=p.col/7,cp=asg[p.col];int y=ori%2==0?7*j+cp:2*cp+j;return 14*x+y;}
 int fresh(int v,std::array<uint8_t,2>&out){int n=0;for(int k=0;k<tc[v];k++){int i=touch[v][k];if(!complete[i]&&done(i))out[n++]=i;}return n;}
 bool candidate(const Mask&danger,const std::array<uint8_t,2>&nw,int n,std::array<uint8_t,2>&ids)const{if(!n)return true;ids[0]=id(nw[0]);if(danger.has(ids[0]))return false;if(n==2){ids[1]=id(nw[1]);if(danger.has(ids[1]))return false;for(int i=0;i<count;i++)if(lines[ids[0]][pid[list[i]]].has(ids[1]))return false;}return true;}
 bool allowed(int v,int val,const Mask&danger){int g=group(v);if(used[g]>>val&1)return false;asg[v]=val;std::array<uint8_t,2>nw{},ids{};int n=fresh(v,nw);bool ok=candidate(danger,nw,n,ids);asg[v]=-1;return ok;}
 bool search(int depth,const Mask&danger){++nodes;if(depth==21)return true;int bv=-1,bc=8;std::array<int8_t,7>dom{};int dn=0;for(int v=0;v<21;v++)if(asg[v]<0){std::array<int8_t,7>d{};int c=0;for(int x=0;x<7;x++)if(allowed(v,x,danger))d[c++]=x;if(!c)return false;if(c<bc){bc=c;bv=v;dn=c;dom=d;if(c==1)break;}}int g=group(bv);for(int q=0;q<dn;q++){int val=dom[q];asg[bv]=val;used[g]|=1u<<val;std::array<uint8_t,2>nw{},ids{};int n=fresh(bv,nw);assert(candidate(danger,nw,n,ids));Mask child=danger;for(int k=0;k<n;k++){int pi=nw[k],x=ids[k];for(int i=0;i<count;i++)child.add(lines[x][pid[list[i]]]);for(int j=0;j<k;j++)child.add(lines[x][ids[j]]);complete[pi]=1;pid[pi]=x;list[count++]=pi;}if(search(depth+1,child))return true;for(int k=n-1;k>=0;k--){--count;complete[nw[k]]=0;}used[g]&=~(1u<<val);asg[bv]=-1;}return false;}
 bool solve(const Selector&s,int o){init();ori=o;asg.fill(-1);used.fill(0);complete.fill(0);tc.fill(0);count=0;nodes=0;int n=0;for(int r=0;r<14;r++){uint16_t m=s[r];while(m){int c=__builtin_ctz(m);m&=m-1;spec[n]={r<7,(uint8_t)(r%7),(uint8_t)c};touch[c][tc[c]++]=n;if(r>=7)touch[14+r%7][tc[14+r%7]++]=n;n++;}}assert(n==28);Mask empty{};return search(0,empty);}
};
std::array<std::array<CSP::Mask,196>,196>CSP::lines{};bool CSP::ready=false;
int main(int argc,char**argv){assert(argc==3);std::string req=argv[1];int shard=std::stoi(argv[2]);for(const auto&d:CASES)if(req==d.name){assert(shard>=0&&shard<(int)d.shard_nodes.size());Enum e;e.s=centre(d);e.h=host(d);e.run();assert((int)e.ns.size()==d.expected);int sc=d.shard_nodes.size(),ss=(d.expected+sc-1)/sc,first=shard*ss+1,last=std::min(d.expected,first+ss-1);uint64_t nodes=0;int index=0,tested=0;for(const auto&s:e.ns){++index;if(index<first||index>last)continue;++tested;for(int o=0;o<4;o++){CSP solver;assert(!solver.solve(s,o));nodes+=solver.nodes;}}assert(tested==std::max(0,last-first+1));assert(nodes==d.shard_nodes[shard]);std::cout<<d.name<<" shard "<<shard<<"/"<<sc<<" selectors="<<tested<<" nodes="<<nodes<<" PASS\n";return 0;}assert(false);}

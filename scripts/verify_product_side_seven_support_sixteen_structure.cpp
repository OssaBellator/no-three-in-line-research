// Exact structural census for the side-seven radius-two support-sixteen layer.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

constexpr int PAIRS[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
using Selector=std::array<std::uint16_t,14>;
struct Hash{std::size_t operator()(Selector const&s)const noexcept{std::uint64_t h=1469598103934665603ULL;for(auto x:s){h^=x;h*=1099511628211ULL;}return h;}};
struct CaseData{std::string name;std::array<int,7>h,p;std::array<int,14>opts;int radius_one,support16,with_four;std::map<int,int>d4;std::map<std::string,int>shapes;};
const std::array<CaseData,4> CASES={{
{"cycle7",{1,2,3,4,5,6,0},{5,4,0,6,2,1,3},{0,3,0,3,5,2,2,2,2,3,0,5,5,2},1092,18878,176,
 {{0,6008},{1,8276},{2,3497},{3,876},{4,188},{5,28},{6,5}},{{"4+12",3264},{"4+4+4+4",3648},{"4+4+8",8559},{"4+6+6",792},{"6+10",472},{"8+8",1548},{"16",595}}},
{"cycle52",{1,2,3,4,0,6,5},{4,5,6,1,3,2,0},{2,2,2,2,2,2,2,2,2,2,2,5,0,2},364,5315,2176,
 {{0,2336},{1,1600},{2,912},{3,336},{4,117},{5,8},{6,5},{8,1}},{{"4+12",2592},{"4+4+4+4",128},{"4+4+8",792},{"4+6+6",32},{"6+10",64},{"8+8",685},{"16",1022}}},
{"cycle43",{1,2,3,0,5,6,4},{3,5,4,2,1,0,6},{5,5,2,0,0,5,2,0,0,5,5,0,3,3},180,2013,664,
 {{0,1072},{1,192},{2,342},{3,216},{4,131},{5,52},{6,8}},{{"4+12",780},{"4+4+4+4",4},{"4+4+8",76},{"4+6+6",4},{"6+10",504},{"8+8",95},{"16",550}}},
{"cycle322",{1,2,0,4,3,6,5},{4,6,5,3,1,2,0},{5,0,3,1,0,5,0,5,5,0,4,3,5,0},112,478,0,
 {{0,408},{4,46},{5,20},{6,2},{8,2}},{{"6+10",192},{"8+8",216},{"16",70}}}
}};
Selector centre(const CaseData&d){Selector s{};for(int sr=0;sr<14;sr++){int o=sr/7,u=sr%7,z=o?d.p[u]:u;int a[4]={z,d.h[z],7+z,7+d.h[z]};int r=7*o+z;for(int k=0;k<2;k++)s[r]|=1u<<a[PAIRS[d.opts[sr]][k]];}return s;}
std::array<std::uint16_t,14> host(const CaseData&d){std::array<std::uint16_t,14>x{};for(int o=0;o<2;o++)for(int z=0;z<7;z++)x[7*o+z]=(1u<<z)|(1u<<d.h[z])|(1u<<(7+z))|(1u<<(7+d.h[z]));return x;}
struct Enumerator{Selector s;std::array<std::uint16_t,14>h{},at{};std::unordered_set<Selector,Hash>ns;std::vector<int>rs,cs;int st;
 void dfs(int r,std::uint16_t ur,std::uint16_t uc){auto u=h[r]&~s[r];while(u){int c=__builtin_ctz(u);u&=u-1;if(uc>>c&1)continue;auto q=at[c];while(q){int rr=__builtin_ctz(q);q&=q-1;if(rr==st){if(rs.size()<2)continue;Selector f=s;for(std::size_t i=0;i<cs.size();i++){int old=cs[i];f[rs[i]]^=1u<<old;f[rs[i+1]]^=1u<<old;}f[rs.back()]^=1u<<c;f[st]^=1u<<c;ns.insert(f);}else if(!(ur>>rr&1)&&rr>=st){rs.push_back(rr);cs.push_back(c);dfs(rr,ur|(1u<<rr),uc|(1u<<c));cs.pop_back();rs.pop_back();}}}}
 void run(){at.fill(0);ns.clear();for(int c=0;c<14;c++)for(int r=0;r<14;r++)if(s[r]>>c&1)at[c]|=1u<<r;for(st=0;st<14;st++){rs={st};cs.clear();dfs(st,1u<<st,0);}}
};
int support(const Selector&a,const Selector&b){int z=0;for(int r=0;r<14;r++)z+=__builtin_popcount(a[r]^b[r]);return z;}
std::pair<int,std::string> shape(const Selector&a,const Selector&b){std::array<std::uint16_t,14>d{},rows_at{};int d4=0;for(int r=0;r<14;r++){d[r]=a[r]^b[r];if(__builtin_popcount(d[r])==4)d4++;for(int c=0;c<14;c++)if(d[r]>>c&1)rows_at[c]|=1u<<r;}for(int c=0;c<14;c++)if(__builtin_popcount(rows_at[c])==4)d4++;
 std::uint16_t seen_r=0,seen_c=0;std::vector<int>sizes;for(int start=0;start<14;start++)if(d[start]&&!(seen_r>>start&1)){std::vector<std::pair<int,int>>q={{0,start}};seen_r|=1u<<start;int edges=0;for(std::size_t i=0;i<q.size();i++){auto [side,v]=q[i];if(!side){auto m=d[v];edges+=__builtin_popcount(m);while(m){int c=__builtin_ctz(m);m&=m-1;if(!(seen_c>>c&1)){seen_c|=1u<<c;q.push_back({1,c});}}}else{auto m=rows_at[v];while(m){int r=__builtin_ctz(m);m&=m-1;if(!(seen_r>>r&1)){seen_r|=1u<<r;q.push_back({0,r});}}}}sizes.push_back(edges);}std::sort(sizes.begin(),sizes.end());std::string key;for(std::size_t i=0;i<sizes.size();i++){if(i)key+="+";key+=std::to_string(sizes[i]);}return {d4,key};}
void verify(const CaseData&d){Selector c=centre(d);auto h=host(d);Enumerator e;e.s=c;e.h=h;e.run();assert((int)e.ns.size()==d.radius_one);auto n1=e.ns;std::unordered_map<Selector,int,Hash>parents;std::unordered_map<Selector,bool,Hash>short_path;for(auto const&p:n1){int first=support(c,p);e.s=p;e.h=h;e.run();for(auto const&v:e.ns){if(v==c||n1.count(v)||support(c,v)!=16)continue;parents[v]++;if(first==4||support(p,v)==4)short_path[v]=true;}}assert((int)parents.size()==d.support16);std::map<int,int>d4;std::map<std::string,int>shapes;int with_four=0;for(auto const&kv:parents){auto [degree,key]=shape(c,kv.first);d4[degree]++;shapes[key]++;if(short_path[kv.first])with_four++;assert(kv.second>=2);}assert(d4==d.d4);assert(shapes==d.shapes);assert(with_four==d.with_four);std::cout<<d.name<<": support16="<<parents.size()<<" short4="<<with_four<<" PASS\n";}
int main(int argc,char**argv){assert(argc==2);std::string req=argv[1];for(auto const&d:CASES)if(req==d.name){verify(d);return 0;}assert(false);}

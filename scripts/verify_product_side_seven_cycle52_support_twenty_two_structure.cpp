// Exact structural census for PX568--PX570.
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
const std::array<int,7> H={1,2,3,4,0,6,5};
const std::array<int,7> P={4,5,6,1,3,2,0};
const std::array<int,14> OPTIONS={2,2,2,2,2,2,2,2,2,2,2,5,0,2};

Selector centre(){Selector s{};for(int sr=0;sr<14;sr++){int o=sr/7,u=sr%7,z=o?P[u]:u;int a[4]={z,H[z],7+z,7+H[z]};int r=7*o+z;for(int k=0;k<2;k++)s[r]|=1u<<a[PAIRS[OPTIONS[sr]][k]];}return s;}
std::array<std::uint16_t,14> host(){std::array<std::uint16_t,14>x{};for(int o=0;o<2;o++)for(int z=0;z<7;z++)x[7*o+z]=(1u<<z)|(1u<<H[z])|(1u<<(7+z))|(1u<<(7+H[z]));return x;}
struct Enumerator{Selector s;std::array<std::uint16_t,14>h{},at{};std::unordered_set<Selector,Hash>ns;std::vector<int>rs,cs;int st;
 void dfs(int r,std::uint16_t ur,std::uint16_t uc){auto u=h[r]&~s[r];while(u){int c=__builtin_ctz(u);u&=u-1;if(uc>>c&1)continue;auto q=at[c];while(q){int rr=__builtin_ctz(q);q&=q-1;if(rr==st){if(rs.size()<2)continue;Selector f=s;for(std::size_t i=0;i<cs.size();i++){int old=cs[i];f[rs[i]]^=1u<<old;f[rs[i+1]]^=1u<<old;}f[rs.back()]^=1u<<c;f[st]^=1u<<c;ns.insert(f);}else if(!(ur>>rr&1)&&rr>=st){rs.push_back(rr);cs.push_back(c);dfs(rr,ur|(1u<<rr),uc|(1u<<c));cs.pop_back();rs.pop_back();}}}}
 void run(){at.fill(0);ns.clear();for(int c=0;c<14;c++)for(int r=0;r<14;r++)if(s[r]>>c&1)at[c]|=1u<<r;for(st=0;st<14;st++){rs={st};cs.clear();dfs(st,1u<<st,0);}}
};
int support(const Selector&a,const Selector&b){int z=0;for(int r=0;r<14;r++)z+=__builtin_popcount(a[r]^b[r]);return z;}
std::pair<int,std::string> shape(const Selector&a,const Selector&b){std::array<std::uint16_t,14>d{},rows_at{};int degree4=0;for(int r=0;r<14;r++){d[r]=a[r]^b[r];if(__builtin_popcount(d[r])==4)degree4++;for(int c=0;c<14;c++)if(d[r]>>c&1)rows_at[c]|=1u<<r;}for(int c=0;c<14;c++)if(__builtin_popcount(rows_at[c])==4)degree4++;
 std::uint16_t seen_r=0,seen_c=0;std::vector<int>sizes;for(int start=0;start<14;start++)if(d[start]&&!(seen_r>>start&1)){std::vector<std::pair<int,int>>q={{0,start}};seen_r|=1u<<start;int edges=0;for(std::size_t i=0;i<q.size();i++){auto [side,v]=q[i];if(!side){auto m=d[v];edges+=__builtin_popcount(m);while(m){int c=__builtin_ctz(m);m&=m-1;if(!(seen_c>>c&1)){seen_c|=1u<<c;q.push_back({1,c});}}}else{auto m=rows_at[v];while(m){int r=__builtin_ctz(m);m&=m-1;if(!(seen_r>>r&1)){seen_r|=1u<<r;q.push_back({0,r});}}}}sizes.push_back(edges);}std::sort(sizes.begin(),sizes.end());std::string key;for(std::size_t i=0;i<sizes.size();i++){if(i)key+="+";key+=std::to_string(sizes[i]);}return {degree4,key};}
int main(){Selector c=centre();auto ho=host();Enumerator e;e.s=c;e.h=ho;e.run();assert(e.ns.size()==364);auto n1=e.ns;std::unordered_map<Selector,int,Hash>parents;std::unordered_map<Selector,bool,Hash>with4;for(auto const&p:n1){int first=support(c,p);e.s=p;e.run();for(auto const&v:e.ns){if(v==c||n1.count(v)||support(c,v)!=22)continue;parents[v]++;if(first==4||support(p,v)==4)with4[v]=true;}}
 assert(parents.size()==3544);std::map<int,int>d4,mult;std::map<std::string,int>shapes;long long incidences=0;int short_count=0;for(auto const&kv:parents){auto [degree,key]=shape(c,kv.first);d4[degree]++;shapes[key]++;mult[kv.second]++;incidences+=kv.second;if(with4[kv.first])short_count++;}
 assert((shapes==std::map<std::string,int>{{"22",1800},{"4+18",1280},{"4+4+14",64},{"6+16",8},{"8+14",392}}));
 assert((d4==std::map<int,int>{{0,1280},{2,512},{3,800},{4,688},{5,248},{6,8},{7,8}}));
 assert((mult==std::map<int,int>{{2,1312},{4,672},{6,64},{7,256},{8,576},{10,192},{11,64},{12,128},{13,64},{14,128},{21,64},{24,16},{32,8}}));
 assert(incidences==20864);assert(short_count==1088);std::cout<<"cycle52 support22 structure: PASS\n";
}

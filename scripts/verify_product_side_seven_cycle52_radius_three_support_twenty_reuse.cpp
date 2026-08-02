#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

constexpr int PAIRS[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
using Selector=std::array<std::uint16_t,14>;
using Half=std::array<std::uint16_t,7>;
struct Hash{std::size_t operator()(Selector const&s)const noexcept{std::uint64_t h=1469598103934665603ULL;for(auto x:s){h^=x;h*=1099511628211ULL;}return h;}};
struct HalfHash{std::size_t operator()(Half const&s)const noexcept{std::uint64_t h=1469598103934665603ULL;for(auto x:s){h^=x;h*=1099511628211ULL;}return h;}};
const std::array<int,7> H={1,2,3,4,0,6,5};
const std::array<int,7> P={4,5,6,1,3,2,0};
const std::array<int,14> OPTIONS={2,2,2,2,2,2,2,2,2,2,2,5,0,2};

Selector centre(){Selector s{};for(int scalar=0;scalar<14;scalar++){int outer=scalar/7,u=scalar%7,z=outer?P[u]:u;int a[4]={z,H[z],7+z,7+H[z]};int row=7*outer+z;for(int k=0;k<2;k++)s[row]|=1u<<a[PAIRS[OPTIONS[scalar]][k]];}return s;}
std::array<std::uint16_t,14> host(){std::array<std::uint16_t,14>x{};for(int outer=0;outer<2;outer++)for(int z=0;z<7;z++)x[7*outer+z]=(1u<<z)|(1u<<H[z])|(1u<<(7+z))|(1u<<(7+H[z]));return x;}
struct Enumerator{Selector s;std::array<std::uint16_t,14>h{},at{};std::unordered_set<Selector,Hash> neighbours;std::vector<int>rows,cols;int start;
 void dfs(int row,std::uint16_t used_rows,std::uint16_t used_cols){std::uint16_t u=h[row]&~s[row];while(u){int col=__builtin_ctz(u);u&=u-1;if(used_cols>>col&1)continue;std::uint16_t q=at[col];while(q){int next=__builtin_ctz(q);q&=q-1;if(next==start){if(rows.size()<2)continue;Selector f=s;for(std::size_t i=0;i<cols.size();i++){int old=cols[i];f[rows[i]]^=1u<<old;f[rows[i+1]]^=1u<<old;}f[rows.back()]^=1u<<col;f[start]^=1u<<col;neighbours.insert(f);}else if(!(used_rows>>next&1)&&next>=start){rows.push_back(next);cols.push_back(col);dfs(next,used_rows|(1u<<next),used_cols|(1u<<col));cols.pop_back();rows.pop_back();}}}}
 void run(){at.fill(0);neighbours.clear();for(int c=0;c<14;c++)for(int r=0;r<14;r++)if(s[r]>>c&1)at[c]|=1u<<r;for(start=0;start<14;start++){rows={start};cols.clear();dfs(start,1u<<start,0);}}
};
int support(Selector const&a,Selector const&b){int d=0;for(int r=0;r<14;r++)d+=__builtin_popcount(a[r]^b[r]);return d;}

int main(){
 Selector c=centre();auto full_host=host();Enumerator e;e.s=c;e.h=full_host;e.run();auto radius_one=e.neighbours;assert(radius_one.size()==364);
 std::unordered_set<Selector,Hash> radius_two;for(auto const&p:radius_one){e.s=p;e.run();for(auto const&v:e.neighbours)if(v!=c&&!radius_one.count(v))radius_two.insert(v);}assert(radius_two.size()==26550);
 std::vector<Selector> parents(radius_two.begin(),radius_two.end());std::sort(parents.begin(),parents.end());
 std::unordered_map<Selector,int,Hash> child_id;child_id.reserve(80000);std::vector<std::vector<int>> children(parents.size());
 for(std::size_t i=0;i<parents.size();i++){e.s=parents[i];e.run();for(auto const&v:e.neighbours){if(v==c||radius_one.count(v)||radius_two.count(v)||support(c,v)!=20)continue;auto [it,inserted]=child_id.emplace(v,child_id.size());children[i].push_back(it->second);}std::sort(children[i].begin(),children[i].end());children[i].erase(std::unique(children[i].begin(),children[i].end()),children[i].end());}
 assert(child_id.size()==71860);std::vector<int> parent_count(child_id.size());std::uint64_t incidences=0;int zero_parents=0,max_degree=0;for(auto const&v:children){if(v.empty())zero_parents++;max_degree=std::max(max_degree,(int)v.size());incidences+=v.size();for(int id:v)parent_count[id]++;}assert(incidences==1669828);assert(*std::min_element(parent_count.begin(),parent_count.end())==5);assert(*std::max_element(parent_count.begin(),parent_count.end())==241);assert(zero_parents==4237);assert(max_degree==594);
 std::unordered_map<Half,int,HalfHash> top,bottom;Half target{3,768,12,3072,144,8224,4160};int target_count=0;for(auto const&kv:child_id){Half a{},b{};std::copy_n(kv.first.begin(),7,a.begin());std::copy_n(kv.first.begin()+7,7,b.begin());top[a]++;bottom[b]++;if(a==target)target_count++;}assert(top.size()==38553&&bottom.size()==38553);int intersection=0,max_top=0,max_bottom=0;for(auto const&kv:top){if(bottom.count(kv.first))intersection++;max_top=std::max(max_top,kv.second);}for(auto const&kv:bottom)max_bottom=std::max(max_bottom,kv.second);assert(intersection==29632);assert(max_top==46&&max_bottom==46);assert(target_count==46);
 using Item=std::pair<int,int>;std::priority_queue<Item> queue;std::vector<char> covered(child_id.size()),chosen(parents.size());for(int i=0;i<(int)parents.size();i++)queue.push({(int)children[i].size(),i});int uncovered=child_id.size(),cover_size=0,first_hundred=0;while(uncovered){auto [score,p]=queue.top();queue.pop();if(chosen[p])continue;int actual=0;for(int id:children[p])if(!covered[id])actual++;if(actual!=score){queue.push({actual,p});continue;}assert(actual>0);chosen[p]=1;cover_size++;if(cover_size<=100)first_hundred+=actual;for(int id:children[p])if(!covered[id]){covered[id]=1;uncovered--;}}
 assert(cover_size==699);assert(first_hundred==43726);
 std::cout<<"PX592--PX594 support-twenty reuse census: PASS\n";
}

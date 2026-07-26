// Exact radius-three selector census for the completed side-seven `(5,2)` class.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_set>
#include <vector>

constexpr int PAIRS[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
using Selector=std::array<std::uint16_t,14>;
struct Hash{std::size_t operator()(Selector const&s)const noexcept{std::uint64_t h=1469598103934665603ULL;for(auto x:s){h^=x;h*=1099511628211ULL;}return h;}};
const std::array<int,7> H={1,2,3,4,0,6,5};
const std::array<int,7> P={4,5,6,1,3,2,0};
const std::array<int,14> OPTIONS={2,2,2,2,2,2,2,2,2,2,2,5,0,2};

Selector centre(){Selector s{};for(int row=0;row<14;++row){int outer=row/7,u=row%7,z=outer?P[u]:u;int adjacency[4]={z,H[z],7+z,7+H[z]};int abstract_row=7*outer+z;for(int k=0;k<2;++k)s[abstract_row]|=1u<<adjacency[PAIRS[OPTIONS[row]][k]];}return s;}
std::array<std::uint16_t,14> host(){std::array<std::uint16_t,14>x{};for(int outer=0;outer<2;++outer)for(int z=0;z<7;++z)x[7*outer+z]=(1u<<z)|(1u<<H[z])|(1u<<(7+z))|(1u<<(7+H[z]));return x;}

struct Enumerator{
 Selector selector{};std::array<std::uint16_t,14> host_rows{},rows_at_column{};std::unordered_set<Selector,Hash> neighbours;std::vector<int> rows,columns;int start=0;
 void dfs(int row,std::uint16_t used_rows,std::uint16_t used_columns){std::uint16_t available=host_rows[row]&~selector[row];while(available){int column=__builtin_ctz(available);available&=available-1;if(used_columns>>column&1u)continue;std::uint16_t next=rows_at_column[column];while(next){int next_row=__builtin_ctz(next);next&=next-1;if(next_row==start){if(rows.size()<2)continue;Selector flipped=selector;for(std::size_t i=0;i<columns.size();++i){int old=columns[i];flipped[rows[i]]^=1u<<old;flipped[rows[i+1]]^=1u<<old;}flipped[rows.back()]^=1u<<column;flipped[start]^=1u<<column;neighbours.insert(flipped);}else if(!(used_rows>>next_row&1u)&&next_row>=start){rows.push_back(next_row);columns.push_back(column);dfs(next_row,used_rows|(1u<<next_row),used_columns|(1u<<column));columns.pop_back();rows.pop_back();}}}}
 void run(){rows_at_column.fill(0);neighbours.clear();for(int c=0;c<14;++c)for(int r=0;r<14;++r)if(selector[r]>>c&1u)rows_at_column[c]|=1u<<r;for(start=0;start<14;++start){rows={start};columns.clear();dfs(start,1u<<start,0);}}
};

int main(){
 const Selector root=centre();Enumerator e;e.selector=root;e.host_rows=host();e.run();const auto radius_one=e.neighbours;assert(radius_one.size()==364);
 std::unordered_set<Selector,Hash> radius_two;for(const auto&parent:radius_one){e.selector=parent;e.run();for(const auto&child:e.neighbours)if(child!=root&&!radius_one.count(child))radius_two.insert(child);}assert(radius_two.size()==26550);
 std::unordered_set<Selector,Hash> radius_three;std::uint64_t directed=0;for(const auto&parent:radius_two){e.selector=parent;e.run();directed+=e.neighbours.size();for(const auto&child:e.neighbours)if(child!=root&&!radius_one.count(child)&&!radius_two.count(child))radius_three.insert(child);}
 assert(directed==15767760ULL);assert(radius_three.size()==468452);
 std::map<int,std::size_t> histogram;for(const auto&s:radius_three){int difference=0;for(int r=0;r<14;++r)difference+=__builtin_popcount(s[r]^root[r]);++histogram[difference];}
 const std::map<int,std::size_t> expected={{12,3600},{14,2048},{16,19352},{18,18336},{20,71860},{22,55432},{24,121872},{26,63024},{28,68880},{30,23488},{32,14336},{34,3072},{36,2032},{38,576},{40,424},{42,64},{44,48},{48,8}};
 assert(histogram==expected);std::cout<<"cycle52 radius3="<<radius_three.size()<<" directed="<<directed<<" support12="<<histogram.at(12)<<" PASS\n";
}

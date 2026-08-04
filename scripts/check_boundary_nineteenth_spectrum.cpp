#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
struct Pt { int x,y; bool operator<(Pt const&o) const {return tie(x,y)<tie(o.x,o.y);} bool operator==(Pt const&o) const{return x==o.x&&y==o.y;} };
long long cross(Pt a,Pt b,Pt c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
struct Node{string name;vector<Pt> pts;};
struct Solver{
 int n; vector<array<int,3>> edges; vector<char> sel; int best;
 bool hit(array<int,3> const&e){return sel[e[0]]||sel[e[1]]||sel[e[2]];}
 int packing_lb(vector<int> const&unhit){vector<char> used(n);int c=0;for(int ix:unhit){auto e=edges[ix];if(!used[e[0]]&&!used[e[1]]&&!used[e[2]]){used[e[0]]=used[e[1]]=used[e[2]]=1;c++;}}return c;}
 void dfs(int count){if(count>=best)return;vector<int> unhit;vector<int> freq(n);for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){unhit.push_back(i);for(int v:edges[i])freq[v]++;}if(unhit.empty()){best=count;return;}if(count+packing_lb(unhit)>=best)return;int chosen=unhit[0],score=-1;for(int ix:unhit){int s=0;for(int v:edges[ix])s+=freq[v];if(s>score){score=s;chosen=ix;}}auto br=edges[chosen];sort(br.begin(),br.end(),[&](int a,int b){return freq[a]>freq[b];});for(int v:br){sel[v]=1;dfs(count+1);sel[v]=0;}}
 int minimum(int ub){sel.assign(n,0);best=ub;dfs(0);return best;}
 void enum_exact(int target,set<vector<int>>&out,int count=0){if(count>target)return;vector<int> unhit;vector<int> freq(n);for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){unhit.push_back(i);for(int v:edges[i])freq[v]++;}if(unhit.empty()){if(count==target){vector<int>s;for(int i=0;i<n;i++)if(sel[i])s.push_back(i);out.insert(s);}return;}if(count+packing_lb(unhit)>target)return;int chosen=unhit[0],score=-1;for(int ix:unhit){int s=0;for(int v:edges[ix])s+=freq[v];if(s>score){score=s;chosen=ix;}}auto br=edges[chosen];sort(br.begin(),br.end(),[&](int a,int b){return freq[a]>freq[b];});for(int v:br){sel[v]=1;enum_exact(target,out,count+1);sel[v]=0;}}
};
int main(){
 vector<Pt> T={{0,196},{0,252},{1,61},{1,113},{2,98},{2,213},{3,3},{3,100},{4,33},{4,77},{5,1},{5,35},{6,2},{6,33},{7,32},{7,35},{8,34},{8,105},{9,60},{9,349},{10,58},{10,61},{11,59},{11,60},{12,2},{12,105},{13,46},{13,77},{14,47},{14,258},{15,46},{15,49},{16,75},{16,76},{17,74},{17,99},{18,76},{18,316},{19,0},{19,346},{20,106},{20,107},{21,0},{21,108},{22,107},{22,315},{23,58},{23,195},{24,82},{24,110},{25,80},{25,81},{26,47},{26,48},{27,80},{27,81},{28,3},{28,108},{29,111},{29,112},{30,49},{30,113},{31,112},{31,257},{32,98},{32,258},{33,99},{33,101},{34,32},{34,101},{35,82},{35,100},{36,163},{36,164},{37,162},{37,165},{38,163},{38,164},{39,162},{39,312},{40,34},{40,315},{41,194},{41,195},{42,196},{42,378},{43,79},{43,194},{44,260},{44,377},{45,257},{45,259},{46,1},{46,259},{47,48},{47,260},{48,165},{48,313},{49,314},{49,316},{50,193},{50,314},{51,75},{51,313},{52,79},{52,379},{53,376},{53,378},{54,253},{54,376},{55,377},{55,379},{56,346},{56,348},{57,347},{57,349},{58,74},{58,216},{59,59},{59,348},{60,309},{60,312},{61,310},{61,311},{62,106},{62,309},{63,310},{63,311},{64,110},{64,255},{65,252},{65,254},{66,193},{66,254},{67,253},{67,255},{68,213},{68,215},{69,214},{69,215},{70,214},{70,216},{71,111},{71,347}}; sort(T.begin(),T.end());
 for(int i=0;i<(int)T.size();i++)for(int j=i+1;j<(int)T.size();j++)for(int k=j+1;k<(int)T.size();k++)if(cross(T[i],T[j],T[k])==0){cerr<<"BAD_STATE\n";return 2;}
 vector<Node> nodes={
 {"P0",{{0,0},{0,2},{1,1},{1,3},{2,1},{2,3},{3,0},{3,2}}},{"P1",{{0,0},{0,3},{1,1},{1,2},{2,0},{2,3},{3,1},{3,2}}},{"P2",{{0,1},{0,3},{1,0},{1,2},{2,0},{2,2},{3,1},{3,3}}},{"P3",{{0,1},{0,2},{1,0},{1,3},{2,1},{2,2},{3,0},{3,3}}},
 {"Q0",{{0,3},{0,5},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,1},{6,3}}},{"Q1",{{0,1},{0,5},{1,0},{1,3},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,3},{5,6},{6,1},{6,5}}},{"Q2",{{0,1},{0,3},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,3},{6,5}}},{"Q3",{{0,1},{0,5},{1,3},{1,6},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,0},{5,3},{6,1},{6,5}}}
 };
 map<int,int> hist;int small=0;long long totalsets=0;
 for(auto const&node:nodes)for(int off=-64;off<=64;off++){
  vector<Pt> block;for(auto p:node.pts)block.push_back({72+p.x,213+off+p.y});
  vector<Pt> all=T;all.insert(all.end(),block.begin(),block.end());sort(all.begin(),all.end());all.erase(unique(all.begin(),all.end()),all.end());
  auto locate=[&](Pt p){return int(lower_bound(all.begin(),all.end(),p)-all.begin());};set<array<int,3>>es;
  for(int i=0;i<(int)T.size();i++)for(int j=i+1;j<(int)T.size();j++)for(auto c:block)if(cross(T[i],T[j],c)==0){array<int,3>e={locate(T[i]),locate(T[j]),locate(c)};sort(e.begin(),e.end());es.insert(e);}
  for(int i=0;i<(int)block.size();i++)for(int j=i+1;j<(int)block.size();j++)for(auto c:T)if(cross(block[i],block[j],c)==0){array<int,3>e={locate(block[i]),locate(block[j]),locate(c)};sort(e.begin(),e.end());es.insert(e);}
  Solver s;s.n=all.size();s.edges.assign(es.begin(),es.end());int m=s.minimum(node.pts.size()+1);hist[m]++;
  if(m<=6){s.sel.assign(s.n,0);set<vector<int>>sets;s.enum_exact(m,sets);small++;totalsets+=sets.size();cout<<node.name<<" "<<off<<" min "<<m<<" triples "<<es.size()<<" cores "<<sets.size()<<"\n";}
 }
 cerr<<"state="<<T.size()<<"\n";cerr<<"hist";for(auto [k,v]:hist)cerr<<" "<<k<<":"<<v;cerr<<" small="<<small<<" sets="<<totalsets<<"\n";
}

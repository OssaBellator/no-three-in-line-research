
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
struct Node{string k;int v;vector<Pt> pts;};
struct Solver{
 int n; vector<array<int,3>> edges; vector<char> sel; int best;
 bool hit(array<int,3> const&e){return sel[e[0]]||sel[e[1]]||sel[e[2]];}
 int packing_lb(vector<int> const&unhit){vector<char> used(n);int c=0;for(int ix:unhit){auto e=edges[ix];if(!used[e[0]]&&!used[e[1]]&&!used[e[2]]){used[e[0]]=used[e[1]]=used[e[2]]=1;c++;}}return c;}
 void dfs(int count){
   if(count>=best)return;
   vector<int> unhit;vector<int> freq(n);
   for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){unhit.push_back(i);for(int v:edges[i])freq[v]++;}
   if(unhit.empty()){best=count;return;}
   if(count+packing_lb(unhit)>=best)return;
   int chosen=unhit[0],score=-1;
   for(int ix:unhit){int s=0;for(int v:edges[ix])s+=freq[v];if(s>score){score=s;chosen=ix;}}
   auto br=edges[chosen]; sort(br.begin(),br.end(),[&](int a,int b){return freq[a]>freq[b];});
   for(int v:br){sel[v]=1;dfs(count+1);sel[v]=0;}
 }
 int minimum(int ub){sel.assign(n,0);best=ub;dfs(0);return best;}
 void enum_exact(int target,set<vector<int>>&out,int count=0){
   if(count>target)return;
   vector<int> unhit;vector<int> freq(n);
   for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){unhit.push_back(i);for(int v:edges[i])freq[v]++;}
   if(unhit.empty()){if(count==target){vector<int>s;for(int i=0;i<n;i++)if(sel[i])s.push_back(i);out.insert(s);}return;}
   if(count+packing_lb(unhit)>target)return;
   int chosen=unhit[0],score=-1;for(int ix:unhit){int s=0;for(int v:edges[ix])s+=freq[v];if(s>score){score=s;chosen=ix;}}
   auto br=edges[chosen];sort(br.begin(),br.end(),[&](int a,int b){return freq[a]>freq[b];});
   for(int v:br){sel[v]=1;enum_exact(target,out,count+1);sel[v]=0;}
 }
};
int main(){
 vector<Pt> T={{0,110},{0,196},{1,61},{1,113},{2,98},{2,257},{3,3},{3,100},{4,33},{4,77},{5,1},{5,35},{6,2},{6,33},{7,32},{7,35},{8,34},{8,105},{9,59},{9,60},{10,58},{10,61},{11,59},{11,60},{12,2},{12,105},{13,46},{13,77},{14,47},{14,258},{15,46},{15,49},{16,75},{16,76},{17,74},{17,99},{18,75},{18,76},{19,0},{19,74},{20,106},{20,107},{21,0},{21,108},{22,106},{22,107},{23,58},{23,195},{24,82},{24,110},{25,80},{25,81},{26,47},{26,48},{27,80},{27,81},{28,3},{28,108},{29,111},{29,112},{30,49},{30,113},{31,111},{31,112},{32,79},{32,98},{33,99},{33,101},{34,32},{34,101},{35,82},{35,100},{36,163},{36,164},{37,162},{37,165},{38,163},{38,164},{39,162},{39,165},{40,34},{40,193},{41,194},{41,195},{42,193},{42,196},{43,79},{43,194},{44,258},{44,260},{45,257},{45,259},{46,1},{46,259},{47,48},{47,260}};
 sort(T.begin(),T.end());
 vector<Node> nodes={
 {"P",0,{{0,0},{0,2},{1,1},{1,3},{2,1},{2,3},{3,0},{3,2}}},
 {"P",1,{{0,0},{0,3},{1,1},{1,2},{2,0},{2,3},{3,1},{3,2}}},
 {"P",2,{{0,1},{0,3},{1,0},{1,2},{2,0},{2,2},{3,1},{3,3}}},
 {"P",3,{{0,1},{0,2},{1,0},{1,3},{2,1},{2,2},{3,0},{3,3}}},
 {"Q",0,{{0,3},{0,5},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,1},{6,3}}},
 {"Q",1,{{0,1},{0,5},{1,0},{1,3},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,3},{5,6},{6,1},{6,5}}},
 {"Q",2,{{0,1},{0,3},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,3},{6,5}}},
 {"Q",3,{{0,1},{0,5},{1,3},{1,6},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,0},{5,3},{6,1},{6,5}}}
 };
 map<int,int> hist; int small=0; long long totalsets=0;
 for(auto const&node:nodes){
  for(int off=-64;off<=64;off++){
   vector<Pt> block;for(auto p:node.pts)block.push_back({48+p.x,257+off+p.y});
   vector<Pt> all=T;all.insert(all.end(),block.begin(),block.end());sort(all.begin(),all.end());all.erase(unique(all.begin(),all.end()),all.end());
   auto locate=[&](Pt p){return int(lower_bound(all.begin(),all.end(),p)-all.begin());};
   set<array<int,3>> eset;
   for(int i=0;i<(int)T.size();i++)for(int j=i+1;j<(int)T.size();j++)for(auto c:block)if(cross(T[i],T[j],c)==0){array<int,3>e={locate(T[i]),locate(T[j]),locate(c)};sort(e.begin(),e.end());eset.insert(e);}
   for(int i=0;i<(int)block.size();i++)for(int j=i+1;j<(int)block.size();j++)for(auto c:T)if(cross(block[i],block[j],c)==0){array<int,3>e={locate(block[i]),locate(block[j]),locate(c)};sort(e.begin(),e.end());eset.insert(e);}
   Solver s;s.n=all.size();s.edges.assign(eset.begin(),eset.end());int ub=block.size()+1;int m=s.minimum(ub);hist[m]++;
   if(m<=6){s.sel.assign(s.n,0);set<vector<int>>sets;s.enum_exact(m,sets);small++;totalsets+=sets.size();cout<<node.k<<node.v<<" "<<off<<" min "<<m<<" triples "<<eset.size()<<" sets "<<sets.size()<<"\n";}
  }
 }
 cerr<<"hist";for(auto [k,v]:hist)cerr<<" "<<k<<":"<<v;cerr<<" small="<<small<<" sets="<<totalsets<<"\n";
}

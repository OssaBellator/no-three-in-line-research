#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
spectrum = (HERE / "check_boundary_nineteenth_spectrum.cpp").read_text()
match = re.search(r"vector<Pt> T=\{(.*?)\};\s*sort", spectrum, re.S)
assert match
points = re.findall(r"\{(-?\d+),(-?\d+)\}", match.group(1))
assert len(points) == 144
state = ",".join(f"{{{x},{y}}}" for x, y in points)

kernel = r'''#include <algorithm>
#include <array>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
struct Pt { int x,y; bool operator<(Pt const&o) const {return tie(x,y)<tie(o.x,o.y);} bool operator==(Pt const&o) const{return x==o.x&&y==o.y;} };
long long cross(Pt a,Pt b,Pt c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
pair<int,int> ndir(Pt a,Pt b){int dx=b.x-a.x,dy=b.y-a.y,g=gcd(abs(dx),abs(dy));dx/=g;dy/=g;if(dx<0||(dx==0&&dy<0)){dx=-dx;dy=-dy;}return {dx,dy};}
struct Node{string name;vector<Pt> pts;};
struct Solver{
 int n; vector<array<int,3>> edges; vector<char> sel; int best;
 bool hit(array<int,3> const&e){return sel[e[0]]||sel[e[1]]||sel[e[2]];}
 int packing_lb(vector<int> const&unhit){vector<char> used(n);int c=0;for(int ix:unhit){auto e=edges[ix];if(!used[e[0]]&&!used[e[1]]&&!used[e[2]]){used[e[0]]=used[e[1]]=used[e[2]]=1;c++;}}return c;}
 void dfs(int count){if(count>=best)return;vector<int> unhit;vector<int> freq(n);for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){unhit.push_back(i);for(int v:edges[i])freq[v]++;}if(unhit.empty()){best=count;return;}if(count+packing_lb(unhit)>=best)return;int chosen=unhit[0],score=-1;for(int ix:unhit){int s=0;for(int v:edges[ix])s+=freq[v];if(s>score){score=s;chosen=ix;}}auto br=edges[chosen];sort(br.begin(),br.end(),[&](int a,int b){return freq[a]>freq[b];});for(int v:br){sel[v]=1;dfs(count+1);sel[v]=0;}}
 int minimum(int ub){sel.assign(n,0);best=ub;dfs(0);return best;}
 void enum_exact(int target,set<vector<int>>&out,int count=0){if(count>target)return;vector<int> unhit;vector<int> freq(n);for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){unhit.push_back(i);for(int v:edges[i])freq[v]++;}if(unhit.empty()){if(count==target){vector<int>s;for(int i=0;i<n;i++)if(sel[i])s.push_back(i);out.insert(s);}return;}if(count+packing_lb(unhit)>target)return;int chosen=unhit[0],score=-1;for(int ix:unhit){int s=0;for(int v:edges[ix])s+=freq[v];if(s>score){score=s;chosen=ix;}}auto br=edges[chosen];sort(br.begin(),br.end(),[&](int a,int b){return freq[a]>freq[b];});for(int v:br){sel[v]=1;enum_exact(target,out,count+1);sel[v]=0;}}
};
bool search_deletion(vector<Pt>const&all, vector<Pt>D, unsigned long long&tested){
 sort(D.begin(),D.end());set<Pt>ds(D.begin(),D.end());vector<Pt>base;for(auto p:all)if(!ds.count(p))base.push_back(p);sort(base.begin(),base.end());
 vector<int>xs,ys;for(auto p:D){xs.push_back(p.x);ys.push_back(p.y);}sort(xs.begin(),xs.end());sort(ys.begin(),ys.end());
 vector<Pt>grid;map<Pt,int>index;for(int x:xs)for(int y:ys){Pt p{x,y};if(!index.count(p)){index[p]=grid.size();grid.push_back(p);}}
 int g=grid.size();vector<char>point_ok(g,1);vector<vector<char>>pair_ok(g,vector<char>(g,1));
 for(int i=0;i<g;i++){if(binary_search(base.begin(),base.end(),grid[i])){point_ok[i]=0;continue;}set<pair<int,int>>dirs;for(auto q:base)if(!dirs.insert(ndir(grid[i],q)).second){point_ok[i]=0;break;}}
 for(auto r:base){map<pair<int,int>,vector<int>>groups;for(int i=0;i<g;i++)if(point_ok[i])groups[ndir(r,grid[i])].push_back(i);for(auto &en:groups){auto &v=en.second;for(int i=0;i<(int)v.size();i++)for(int j=i+1;j<(int)v.size();j++)pair_ok[v[i]][v[j]]=pair_ok[v[j]][v[i]]=0;}}
 do{tested++;vector<Pt>A;vector<int>ix;set<Pt>uni;bool ok=true;for(int i=0;i<(int)D.size();i++){Pt p{xs[i],ys[i]};if(!uni.insert(p).second){ok=false;break;}int z=index[p];if(!point_ok[z]){ok=false;break;}A.push_back(p);ix.push_back(z);}if(!ok||uni==ds)continue;for(int i=0;i<(int)A.size()&&ok;i++)for(int j=i+1;j<(int)A.size();j++)if(!pair_ok[ix[i]][ix[j]]){ok=false;break;}for(int i=0;i<(int)A.size()&&ok;i++)for(int j=i+1;j<(int)A.size();j++)for(int k=j+1;k<(int)A.size();k++)if(cross(A[i],A[j],A[k])==0){ok=false;break;}if(ok)return true;}while(next_permutation(ys.begin(),ys.end()));return false;
}
bool search_budget(vector<Pt>const&all,vector<Pt>const&core,int budget,unsigned long long&tested){set<Pt>cs(core.begin(),core.end());vector<Pt>av;for(auto p:all)if(!cs.count(p))av.push_back(p);int extras=budget-(int)core.size();vector<Pt>ch;bool found=false;function<void(int,int)>go=[&](int st,int left){if(found)return;if(left==0){vector<Pt>D=core;D.insert(D.end(),ch.begin(),ch.end());if(search_deletion(all,D,tested))found=true;return;}for(int i=st;i<=(int)av.size()-left&&!found;i++){ch.push_back(av[i]);go(i+1,left-1);ch.pop_back();}};go(0,extras);return found;}
int main(){
 vector<Pt> T={STATE}; sort(T.begin(),T.end());
 vector<Node> nodes={
 {"P0",{{0,0},{0,2},{1,1},{1,3},{2,1},{2,3},{3,0},{3,2}}},{"P1",{{0,0},{0,3},{1,1},{1,2},{2,0},{2,3},{3,1},{3,2}}},{"P2",{{0,1},{0,3},{1,0},{1,2},{2,0},{2,2},{3,1},{3,3}}},{"P3",{{0,1},{0,2},{1,0},{1,3},{2,1},{2,2},{3,0},{3,3}}},
 {"Q0",{{0,3},{0,5},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,1},{6,3}}},{"Q1",{{0,1},{0,5},{1,0},{1,3},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,3},{5,6},{6,1},{6,5}}},{"Q2",{{0,1},{0,3},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,3},{6,5}}},{"Q3",{{0,1},{0,5},{1,3},{1,6},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,0},{5,3},{6,1},{6,5}}}
 };
 int attempts5=0,cores5=0,attempts6=0,cores6=0,repairs=0;unsigned long long tested5=0,tested6from5=0,tested6from6=0;map<int,int> core_hist5,core_hist6;
 for(auto const&node:nodes)for(int off=-64;off<=64;off++){
  vector<Pt> block;for(auto p:node.pts)block.push_back({72+p.x,213+off+p.y});
  vector<Pt> all=T;all.insert(all.end(),block.begin(),block.end());sort(all.begin(),all.end());all.erase(unique(all.begin(),all.end()),all.end());
  auto locate=[&](Pt p){return int(lower_bound(all.begin(),all.end(),p)-all.begin());};set<array<int,3>>es;
  for(int i=0;i<(int)T.size();i++)for(int j=i+1;j<(int)T.size();j++)for(auto c:block)if(cross(T[i],T[j],c)==0){array<int,3>e={locate(T[i]),locate(T[j]),locate(c)};sort(e.begin(),e.end());es.insert(e);}
  for(int i=0;i<(int)block.size();i++)for(int j=i+1;j<(int)block.size();j++)for(auto c:T)if(cross(block[i],block[j],c)==0){array<int,3>e={locate(block[i]),locate(block[j]),locate(c)};sort(e.begin(),e.end());es.insert(e);}
  Solver s;s.n=all.size();s.edges.assign(es.begin(),es.end());int m=s.minimum(node.pts.size()+1);if(m!=5&&m!=6)continue;
  s.sel.assign(s.n,0);set<vector<int>>sets;s.enum_exact(m,sets);if(m==5){attempts5++;cores5+=sets.size();core_hist5[sets.size()]++;}else{attempts6++;cores6+=sets.size();core_hist6[sets.size()]++;}
  for(auto const&ixcore:sets){vector<Pt>core;for(int ix:ixcore)core.push_back(all[ix]);unsigned long long t=0;if(m==5){if(search_budget(all,core,5,t))repairs++;tested5+=t;t=0;if(search_budget(all,core,6,t))repairs++;tested6from5+=t;}else{if(search_budget(all,core,6,t))repairs++;tested6from6+=t;}}
 }
 cout<<"attempts5="<<attempts5<<" cores5="<<cores5<<" attempts6="<<attempts6<<" cores6="<<cores6<<" tested5="<<tested5<<" tested6from5="<<tested6from5<<" tested6from6="<<tested6from6<<" repairs="<<repairs<<" core_hist5";for(auto [k,v]:core_hist5)cout<<" "<<k<<":"<<v;cout<<" core_hist6";for(auto [k,v]:core_hist6)cout<<" "<<k<<":"<<v;cout<<"\n";
}
'''.replace("STATE", state)

with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    source = directory / "kernel.cpp"
    binary = directory / "kernel"
    source.write_text(kernel)
    subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)], check=True)
    result = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

assert result.stdout.splitlines() == [
    "attempts5=13 cores5=68 attempts6=46 cores6=442 tested5=4890 tested6from5=4258350 tested6from6=142200 repairs=0 core_hist5 3:6 5:3 6:1 9:2 11:1 core_hist6 1:6 3:17 5:1 9:13 11:1 15:2 21:2 27:1 33:1 39:1 81:1"
]
assert result.stderr == ""
print({
    "minimum_five_attempts": 13,
    "minimum_five_cores": 68,
    "minimum_six_attempts": 46,
    "minimum_six_cores": 442,
    "minimum_five_core_count_histogram": {3: 6, 5: 3, 6: 1, 9: 2, 11: 1},
    "minimum_six_core_count_histogram": {
        1: 6, 3: 17, 5: 1, 9: 13, 11: 1, 15: 2,
        21: 2, 27: 1, 33: 1, 39: 1, 81: 1,
    },
    "five_point_replacements_rejected": 4890,
    "six_point_replacements_from_minimum_five_cores_rejected": 4258350,
    "six_point_replacements_from_minimum_six_cores_rejected": 142200,
    "repairs": 0,
    "status": "passed",
})

#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from pathlib import Path
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = Path(__file__).resolve().parent

def parse_state(path):
    text = path.read_text()
    match = re.search(r"vector<Pt> T=\{(.*?)\};\s*sort", text, re.S)
    assert match
    return {(int(x), int(y)) for x, y in re.findall(r"\{(-?\d+),(-?\d+)\}", match.group(1))}

def collinear(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

LOW_KERNEL = '#include <algorithm>\n#include <array>\n#include <functional>\n#include <iostream>\n#include <numeric>\n#include <map>\n#include <set>\n#include <string>\n#include <tuple>\n#include <vector>\nusing namespace std;\nstruct Pt { int x,y; bool operator<(Pt const&o) const {return tie(x,y)<tie(o.x,o.y);} bool operator==(Pt const&o) const{return x==o.x&&y==o.y;} };\nlong long cross(Pt a,Pt b,Pt c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}\n\npair<int,int> ndir(Pt a,Pt b){int dx=b.x-a.x,dy=b.y-a.y,g=gcd(abs(dx),abs(dy));dx/=g;dy/=g;if(dx<0||(dx==0&&dy<0)){dx=-dx;dy=-dy;}return {dx,dy};}\nbool search_deletion(vector<Pt>const&all, vector<Pt>D, vector<Pt>&answer, unsigned long long&tested){\n sort(D.begin(),D.end());set<Pt>ds(D.begin(),D.end());vector<Pt>base;for(auto p:all)if(!ds.count(p))base.push_back(p);sort(base.begin(),base.end());\n vector<int>xs,ys;for(auto p:D){xs.push_back(p.x);ys.push_back(p.y);}sort(xs.begin(),xs.end());sort(ys.begin(),ys.end());\n vector<Pt>grid;map<Pt,int>index;for(int x:xs)for(int y:ys){Pt p{x,y};if(!index.count(p)){index[p]=grid.size();grid.push_back(p);}}\n int g=grid.size();vector<char>point_ok(g,1);vector<vector<char>>pair_ok(g,vector<char>(g,1));\n for(int i=0;i<g;i++){if(binary_search(base.begin(),base.end(),grid[i])){point_ok[i]=0;continue;}set<pair<int,int>>dirs;for(auto q:base)if(!dirs.insert(ndir(grid[i],q)).second){point_ok[i]=0;break;}}\n for(auto r:base){map<pair<int,int>,vector<int>>groups;for(int i=0;i<g;i++)if(point_ok[i])groups[ndir(r,grid[i])].push_back(i);for(auto &en:groups){auto &v=en.second;for(int i=0;i<(int)v.size();i++)for(int j=i+1;j<(int)v.size();j++)pair_ok[v[i]][v[j]]=pair_ok[v[j]][v[i]]=0;}}\n do{tested++;vector<Pt>A;vector<int>ix;set<Pt>uni;bool ok=true;for(int i=0;i<(int)D.size();i++){Pt p{xs[i],ys[i]};if(!uni.insert(p).second){ok=false;break;}int z=index[p];if(!point_ok[z]){ok=false;break;}A.push_back(p);ix.push_back(z);}if(!ok||uni==ds)continue;for(int i=0;i<(int)A.size()&&ok;i++)for(int j=i+1;j<(int)A.size();j++)if(!pair_ok[ix[i]][ix[j]]){ok=false;break;}for(int i=0;i<(int)A.size()&&ok;i++)for(int j=i+1;j<(int)A.size();j++)for(int k=j+1;k<(int)A.size();k++)if(cross(A[i],A[j],A[k])==0){ok=false;break;}if(ok){answer=A;sort(answer.begin(),answer.end());return true;}}while(next_permutation(ys.begin(),ys.end()));return false;\n}\nbool search_budget(vector<Pt>const&all,vector<Pt>const&core,int budget,unsigned long long&tested){set<Pt>cs(core.begin(),core.end());vector<Pt>av;for(auto p:all)if(!cs.count(p))av.push_back(p);int extras=budget-(int)core.size();vector<Pt>ch;bool found=false;function<void(int,int)>go=[&](int st,int left){if(found)return;if(left==0){vector<Pt>D=core;D.insert(D.end(),ch.begin(),ch.end());vector<Pt>A;if(search_deletion(all,D,A,tested))found=true;return;}for(int i=st;i<=(int)av.size()-left&&!found;i++){ch.push_back(av[i]);go(i+1,left-1);ch.pop_back();}};go(0,extras);return found;}\nstruct Node{string name;vector<Pt> pts;};\nstruct Solver{\n int n; vector<array<int,3>> edges; vector<char> sel; int best;\n bool hit(array<int,3> const&e){return sel[e[0]]||sel[e[1]]||sel[e[2]];}\n int packing_lb(vector<int> const&unhit){vector<char> used(n);int c=0;for(int ix:unhit){auto e=edges[ix];if(!used[e[0]]&&!used[e[1]]&&!used[e[2]]){used[e[0]]=used[e[1]]=used[e[2]]=1;c++;}}return c;}\n void dfs(int count){if(count>=best)return;vector<int> unhit;vector<int> freq(n);for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){unhit.push_back(i);for(int v:edges[i])freq[v]++;}if(unhit.empty()){best=count;return;}if(count+packing_lb(unhit)>=best)return;int chosen=unhit[0],score=-1;for(int ix:unhit){int s=0;for(int v:edges[ix])s+=freq[v];if(s>score){score=s;chosen=ix;}}auto br=edges[chosen];sort(br.begin(),br.end(),[&](int a,int b){return freq[a]>freq[b];});for(int v:br){sel[v]=1;dfs(count+1);sel[v]=0;}}\n int minimum(int ub){sel.assign(n,0);best=ub;dfs(0);return best;}\n void enum_exact(int target,set<vector<int>>&out,int count=0){if(count>target)return;vector<int> unhit;vector<int> freq(n);for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){unhit.push_back(i);for(int v:edges[i])freq[v]++;}if(unhit.empty()){if(count==target){vector<int>s;for(int i=0;i<n;i++)if(sel[i])s.push_back(i);out.insert(s);}return;}if(count+packing_lb(unhit)>target)return;int chosen=unhit[0],score=-1;for(int ix:unhit){int s=0;for(int v:edges[ix])s+=freq[v];if(s>score){score=s;chosen=ix;}}auto br=edges[chosen];sort(br.begin(),br.end(),[&](int a,int b){return freq[a]>freq[b];});for(int v:br){sel[v]=1;enum_exact(target,out,count+1);sel[v]=0;}}\n};\nint main(){\n vector<Pt> T={STATE}; sort(T.begin(),T.end());\n for(int i=0;i<(int)T.size();i++)for(int j=i+1;j<(int)T.size();j++)for(int k=j+1;k<(int)T.size();k++)if(cross(T[i],T[j],T[k])==0){cerr<<"BAD STATE\\n";return 2;}\n vector<Node> nodes={\n {"P0",{{0,0},{0,2},{1,1},{1,3},{2,1},{2,3},{3,0},{3,2}}},{"P1",{{0,0},{0,3},{1,1},{1,2},{2,0},{2,3},{3,1},{3,2}}},{"P2",{{0,1},{0,3},{1,0},{1,2},{2,0},{2,2},{3,1},{3,3}}},{"P3",{{0,1},{0,2},{1,0},{1,3},{2,1},{2,2},{3,0},{3,3}}},\n {"Q0",{{0,3},{0,5},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,1},{6,3}}},{"Q1",{{0,1},{0,5},{1,0},{1,3},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,3},{5,6},{6,1},{6,5}}},{"Q2",{{0,1},{0,3},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,3},{6,5}}},{"Q3",{{0,1},{0,5},{1,3},{1,6},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,0},{5,3},{6,1},{6,5}}}\n };\n map<int,int> hist;int small=0;long long totalsets=0;int attempts5=0,cores5=0,attempts6=0,cores6=0,repairs=0;unsigned long long tested5=0,tested6from5=0,tested6from6=0;map<int,int>core_hist5,core_hist6;\n for(auto const&node:nodes)for(int off=-64;off<=64;off++){\n  vector<Pt> block;for(auto p:node.pts)block.push_back({72+p.x,213+off+p.y});\n  vector<Pt> all=T;all.insert(all.end(),block.begin(),block.end());sort(all.begin(),all.end());all.erase(unique(all.begin(),all.end()),all.end());\n  auto locate=[&](Pt p){return int(lower_bound(all.begin(),all.end(),p)-all.begin());};set<array<int,3>>es;\n  for(int i=0;i<(int)T.size();i++)for(int j=i+1;j<(int)T.size();j++)for(auto c:block)if(cross(T[i],T[j],c)==0){array<int,3>e={locate(T[i]),locate(T[j]),locate(c)};sort(e.begin(),e.end());es.insert(e);}\n  for(int i=0;i<(int)block.size();i++)for(int j=i+1;j<(int)block.size();j++)for(auto c:T)if(cross(block[i],block[j],c)==0){array<int,3>e={locate(block[i]),locate(block[j]),locate(c)};sort(e.begin(),e.end());es.insert(e);}\n  Solver s;s.n=all.size();s.edges.assign(es.begin(),es.end());int m=s.minimum(node.pts.size()+1);hist[m]++;\n  if(m<=7){s.sel.assign(s.n,0);set<vector<int>>sets;s.enum_exact(m,sets);small++;totalsets+=sets.size();cout<<node.name<<" "<<off<<" min "<<m<<" triples "<<es.size()<<" cores "<<sets.size()<<"\\n";if(m==5||m==6){if(m==5){attempts5++;cores5+=sets.size();core_hist5[sets.size()]++;}else{attempts6++;cores6+=sets.size();core_hist6[sets.size()]++;}for(auto const&ss:sets){vector<Pt>core;for(int ix:ss)core.push_back(all[ix]);unsigned long long t=0;if(m==5){if(search_budget(all,core,5,t))repairs++;tested5+=t;t=0;if(search_budget(all,core,6,t))repairs++;tested6from5+=t;}else{if(search_budget(all,core,6,t))repairs++;tested6from6+=t;}}}}\n }\n cerr<<"state="<<T.size()<<"\\n";cerr<<"hist";for(auto [k,v]:hist)cerr<<" "<<k<<":"<<v;cerr<<" small="<<small<<" sets="<<totalsets<<"\\n";cerr<<"low attempts5="<<attempts5<<" cores5="<<cores5<<" attempts6="<<attempts6<<" cores6="<<cores6<<" tested5="<<tested5<<" tested6from5="<<tested6from5<<" tested6from6="<<tested6from6<<" repairs="<<repairs<<" core_hist5";for(auto [k,v]:core_hist5)cerr<<" "<<k<<":"<<v;cerr<<" core_hist6";for(auto [k,v]:core_hist6)cerr<<" "<<k<<":"<<v;cerr<<"\\n";\n}\n'
CORRECTION_KERNEL = '#include <algorithm>\n#include <functional>\n#include <iostream>\n#include <map>\n#include <numeric>\n#include <set>\n#include <tuple>\n#include <vector>\nusing namespace std;\nstruct Pt{int x,y;bool operator<(Pt const&o)const{return tie(x,y)<tie(o.x,o.y);}bool operator==(Pt const&o)const{return x==o.x&&y==o.y;}};\nlong long cross(Pt a,Pt b,Pt c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}\npair<int,int> ndir(Pt a,Pt b){int dx=b.x-a.x,dy=b.y-a.y,g=gcd(abs(dx),abs(dy));dx/=g;dy/=g;if(dx<0||(dx==0&&dy<0)){dx=-dx;dy=-dy;}return {dx,dy};}\nbool search_deletion(vector<Pt>const&all, vector<Pt>D, vector<Pt>&answer, unsigned long long&tested){\n sort(D.begin(),D.end());set<Pt>ds(D.begin(),D.end());vector<Pt>base;for(auto p:all)if(!ds.count(p))base.push_back(p);sort(base.begin(),base.end());\n vector<int>xs,ys;for(auto p:D){xs.push_back(p.x);ys.push_back(p.y);}sort(xs.begin(),xs.end());sort(ys.begin(),ys.end());\n vector<Pt>grid;map<Pt,int>index;for(int x:xs)for(int y:ys){Pt p{x,y};if(!index.count(p)){index[p]=grid.size();grid.push_back(p);}}\n int g=grid.size();vector<char>point_ok(g,1);vector<vector<char>>pair_ok(g,vector<char>(g,1));\n for(int i=0;i<g;i++){if(binary_search(base.begin(),base.end(),grid[i])){point_ok[i]=0;continue;}set<pair<int,int>>dirs;for(auto q:base)if(!dirs.insert(ndir(grid[i],q)).second){point_ok[i]=0;break;}}\n for(auto r:base){map<pair<int,int>,vector<int>>groups;for(int i=0;i<g;i++)if(point_ok[i])groups[ndir(r,grid[i])].push_back(i);for(auto &en:groups){auto &v=en.second;for(int i=0;i<(int)v.size();i++)for(int j=i+1;j<(int)v.size();j++)pair_ok[v[i]][v[j]]=pair_ok[v[j]][v[i]]=0;}}\n do{tested++;vector<Pt>A;vector<int>ix;set<Pt>uni;bool ok=true;for(int i=0;i<(int)D.size();i++){Pt p{xs[i],ys[i]};if(!uni.insert(p).second){ok=false;break;}int z=index[p];if(!point_ok[z]){ok=false;break;}A.push_back(p);ix.push_back(z);}if(!ok||uni==ds)continue;for(int i=0;i<(int)A.size()&&ok;i++)for(int j=i+1;j<(int)A.size();j++)if(!pair_ok[ix[i]][ix[j]]){ok=false;break;}for(int i=0;i<(int)A.size()&&ok;i++)for(int j=i+1;j<(int)A.size();j++)for(int k=j+1;k<(int)A.size();k++)if(cross(A[i],A[j],A[k])==0){ok=false;break;}if(ok){answer=A;sort(answer.begin(),answer.end());return true;}}while(next_permutation(ys.begin(),ys.end()));return false;\n}\nbool search_budget(vector<Pt>const&all,vector<Pt>const&core,int budget,vector<Pt>&Dout,vector<Pt>&Aout,unsigned long long&tested){set<Pt>cs(core.begin(),core.end());vector<Pt>av;for(auto p:all)if(!cs.count(p))av.push_back(p);int extras=budget-(int)core.size();vector<Pt>ch;bool found=false;function<void(int,int)>go=[&](int st,int left){if(found)return;if(left==0){vector<Pt>D=core;D.insert(D.end(),ch.begin(),ch.end());vector<Pt>A;if(search_deletion(all,D,A,tested)){Dout=D;sort(Dout.begin(),Dout.end());Aout=A;found=true;}return;}for(int i=st;i<=(int)av.size()-left&&!found;i++){ch.push_back(av[i]);go(i+1,left-1);ch.pop_back();}};go(0,extras);return found;}\nint main(int argc,char**argv){\n vector<Pt>T={STATE};sort(T.begin(),T.end());\n vector<pair<string,vector<Pt>>> attempts;\n vector<Pt>P1={{0,0},{0,3},{1,1},{1,2},{2,0},{2,3},{3,1},{3,2}};vector<Pt>all1=T;for(auto p:P1)all1.push_back({72+p.x,180+p.y});sort(all1.begin(),all1.end());attempts.push_back({"P1/-33",all1});\n vector<Pt>P2={{0,1},{0,3},{1,0},{1,2},{2,0},{2,2},{3,1},{3,3}};vector<Pt>all2=T;for(auto p:P2)all2.push_back({72+p.x,149+p.y});sort(all2.begin(),all2.end());attempts.push_back({"P2/-64",all2});\n vector<vector<vector<Pt>>> cores={{{{70,214},{74,180},{74,183},{75,181}}},{{{13,77},{73,151},{75,150},{75,152}},{{33,101},{73,151},{75,150},{75,152}},{{36,163},{73,149},{73,151},{75,152}},{{39,162},{73,149},{73,151},{75,152}},{{73,149},{73,151},{75,150},{75,152}}}};\n int a=atoi(argv[1]),c=atoi(argv[2]);cout<<attempts[a].first<<" core"<<c+1<<"\\n";for(int b=4;b<=6;b++){unsigned long long tested=0;vector<Pt>D,A;bool ok=search_budget(attempts[a].second,cores[a][c],b,D,A,tested);cout<<"budget "<<b<<" "<<(ok?"FOUND":"none")<<" tested "<<tested<<"\\n";if(ok)return 2;}\n}\n'

seventeenth = parse_state(HERE / "check_boundary_eighteenth_spectrum.cpp")
assert len(seventeenth) == 136
p0 = ((0,0),(0,2),(1,1),(1,3),(2,1),(2,3),(3,0),(3,2))
block = {(68+x,213+y) for x,y in p0}
deleted = {(2,257),(31,111),(58,347),(69,216),(71,213),(71,215)}
added = {(2,213),(31,257),(58,216),(69,215),(71,111),(71,347)}
assert Counter(x for x,_ in deleted) == Counter(x for x,_ in added)
assert Counter(y for _,y in deleted) == Counter(y for _,y in added)
state = (seventeenth | block) - deleted | added
assert len(state) == 144
assert all(not collinear(*triple) for triple in combinations(sorted(state),3))
assert collinear((36,163),(42,193),(54,253))
assert (42,378) in state and (42,193) not in state
state_cpp = ",".join(f"{{{x},{y}}}" for x,y in sorted(state))

low_kernel = LOW_KERNEL.replace("STATE", state_cpp)
correction_kernel = CORRECTION_KERNEL.replace("STATE", state_cpp)

with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    low_source = directory / "low.cpp"
    low_binary = directory / "low"
    low_source.write_text(low_kernel)
    subprocess.run(["c++","-O2","-std=c++17",str(low_source),"-o",str(low_binary)],check=True)
    low_run = subprocess.run([str(low_binary)],check=True,capture_output=True,text=True)
    assert low_run.stderr.splitlines() == [
        "state=144",
        "hist 4:2 5:9 6:47 7:175 8:283 9:3 10:16 11:63 12:121 13:176 14:137 small=233 sets=2258",
        "low attempts5=9 cores5=54 attempts6=47 cores6=435 tested5=3810 tested6from5=3318750 tested6from6=143640 repairs=0 core_hist5 3:3 5:2 6:1 9:2 11:1 core_hist6 1:6 3:15 5:1 9:15 11:1 15:3 21:2 27:1 33:1 39:1 47:1",
    ]
    low_lines = low_run.stdout.splitlines()
    assert "P1 -33 min 4 triples 10 cores 1" in low_lines
    assert "P2 -64 min 4 triples 9 cores 5" in low_lines

    correction_source = directory / "corrections.cpp"
    correction_binary = directory / "corrections"
    correction_source.write_text(correction_kernel)
    subprocess.run(["c++","-O2","-std=c++17",str(correction_source),"-o",str(correction_binary)],check=True)
    cases = [(0,0)] + [(1,index) for index in range(5)]
    def run_case(case):
        attempt,core = case
        return subprocess.run([str(correction_binary),str(attempt),str(core)],check=True,capture_output=True,text=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        runs = list(pool.map(run_case, cases))
    for run in runs:
        lines = run.stdout.splitlines()
        assert lines[1:] == [
            "budget 4 none tested 24",
            "budget 5 none tested 17520",
            "budget 6 none tested 7595640",
        ]
        assert run.stderr == ""

print({
    "corrected_state_points": 144,
    "legacy_bad_point": (42,193),
    "canonical_point": (42,378),
    "minimum_transversal_histogram": {4:2,5:9,6:47,7:175,8:283,9:3,10:16,11:63,12:121,13:176,14:137},
    "minimum_four_attempts": {"P1/-33":1,"P2/-64":5},
    "minimum_five": {"attempts":9,"cores":54},
    "minimum_six": {"attempts":47,"cores":435},
    "minimum_four_rejected": {4:144,5:105120,6:45573840},
    "minimum_five_rejected": {5:3810,6:3318750},
    "minimum_six_rejected": {6:143640},
    "total_replacements_rejected": 49145304,
    "repairs_through_budget_six": 0,
    "status": "passed",
})

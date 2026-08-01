#include <algorithm>
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
struct Pt{int x,y;bool operator<(Pt const&o)const{return tie(x,y)<tie(o.x,o.y);}bool operator==(Pt const&o)const{return x==o.x&&y==o.y;}};
long long cross(Pt a,Pt b,Pt c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);} 
pair<int,int> dir(Pt a,Pt b){int dx=b.x-a.x,dy=b.y-a.y;int g=gcd(abs(dx),abs(dy));dx/=g;dy/=g;if(dx<0||(dx==0&&dy<0)){dx=-dx;dy=-dy;}return {dx,dy};}
struct Node{string k;int v;vector<Pt> pts;};
struct Solver{
 int n;vector<array<int,3>>edges;vector<char>sel;int best;
 bool hit(array<int,3>const&e){return sel[e[0]]||sel[e[1]]||sel[e[2]];}
 int lb(vector<int>const&u){vector<char>used(n);int c=0;for(int ix:u){auto e=edges[ix];if(!used[e[0]]&&!used[e[1]]&&!used[e[2]]){for(int v:e)used[v]=1;c++;}}return c;}
 void dfs(int c){if(c>=best)return;vector<int>u;vector<int>f(n);for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){u.push_back(i);for(int v:edges[i])f[v]++;}if(u.empty()){best=c;return;}if(c+lb(u)>=best)return;int ch=u[0],sc=-1;for(int ix:u){int s=0;for(int v:edges[ix])s+=f[v];if(s>sc){sc=s;ch=ix;}}auto br=edges[ch];sort(br.begin(),br.end(),[&](int a,int b){return f[a]>f[b];});for(int v:br){sel[v]=1;dfs(c+1);sel[v]=0;}}
 int minimum(int ub){sel.assign(n,0);best=ub;dfs(0);return best;}
 void enum_exact(int target,set<vector<int>>&out,int c=0){if(c>target)return;vector<int>u;vector<int>f(n);for(int i=0;i<(int)edges.size();i++)if(!hit(edges[i])){u.push_back(i);for(int v:edges[i])f[v]++;}if(u.empty()){if(c==target){vector<int>s;for(int i=0;i<n;i++)if(sel[i])s.push_back(i);out.insert(s);}return;}if(c+lb(u)>target)return;int ch=u[0],sc=-1;for(int ix:u){int s=0;for(int v:edges[ix])s+=f[v];if(s>sc){sc=s;ch=ix;}}auto br=edges[ch];sort(br.begin(),br.end(),[&](int a,int b){return f[a]>f[b];});for(int v:br){sel[v]=1;enum_exact(target,out,c+1);sel[v]=0;}}
};
bool refill_search(const vector<Pt>&original,const vector<Pt>&deleted,vector<Pt>&answer){set<Pt>del(deleted.begin(),deleted.end());vector<Pt>base;for(auto p:original)if(!del.count(p))base.push_back(p);sort(base.begin(),base.end());map<int,int>cc,rc;for(auto p:deleted){cc[p.x]++;rc[p.y]++;}vector<int>cols;for(auto [x,n]:cc)for(int i=0;i<n;i++)cols.push_back(x);sort(cols.begin(),cols.end(),[&](int a,int b){if(cc[a]!=cc[b])return cc[a]>cc[b];return a<b;});map<int,vector<int>>cand;for(auto [x,n]:cc){for(auto [y,m]:rc){Pt p{x,y};if(binary_search(base.begin(),base.end(),p))continue;set<pair<int,int>>ds;bool ok=true;for(auto q:base){auto d=dir(p,q);if(!ds.insert(d).second){ok=false;break;}}if(ok)cand[x].push_back(y);}if((int)cand[x].size()<n)return false;}vector<Pt>chosen;map<int,int>rem=rc;function<bool(int)>dfs=[&](int i){if(i==(int)cols.size()){answer=chosen;sort(answer.begin(),answer.end());return true;}int x=cols[i],prev=-1000000000;if(i&&cols[i-1]==x)prev=chosen.back().y;for(int y:cand[x]){if(y<=prev||rem[y]==0)continue;Pt p{x,y};if(find(chosen.begin(),chosen.end(),p)!=chosen.end())continue;bool bad=false;for(auto s:chosen){for(auto q:base)if(cross(q,s,p)==0){bad=true;break;}if(bad)break;}for(int a=0;a<(int)chosen.size()&&!bad;a++)for(int b=a+1;b<(int)chosen.size();b++)if(cross(chosen[a],chosen[b],p)==0){bad=true;break;}if(bad)continue;rem[y]--;chosen.push_back(p);if(dfs(i+1))return true;chosen.pop_back();rem[y]++;}return false;};return dfs(0);}

int main(){
 vector<Pt>T={{0,79},{0,110},{1,61},{1,113},{2,1},{2,98},{3,3},{3,100},{4,33},{4,77},{5,1},{5,35},{6,33},{6,34},{7,32},{7,35},{8,34},{8,105},{9,59},{9,60},{10,58},{10,61},{11,59},{11,60},{12,2},{12,105},{13,46},{13,77},{14,47},{14,48},{15,46},{15,49},{16,75},{16,76},{17,74},{17,99},{18,75},{18,76},{19,0},{19,74},{20,106},{20,107},{21,0},{21,108},{22,106},{22,107},{23,2},{23,58},{24,82},{24,110},{25,80},{25,81},{26,47},{26,48},{27,80},{27,81},{28,3},{28,108},{29,111},{29,112},{30,49},{30,113},{31,111},{31,112},{32,79},{32,98},{33,99},{33,101},{34,32},{34,101},{35,82},{35,100},{36,163},{36,164},{37,162},{37,165},{38,163},{38,164},{39,162},{39,165}};sort(T.begin(),T.end());
 vector<Node>nodes={{"P",0,{{0,0},{0,2},{1,1},{1,3},{2,1},{2,3},{3,0},{3,2}}},{"P",1,{{0,0},{0,3},{1,1},{1,2},{2,0},{2,3},{3,1},{3,2}}},{"P",2,{{0,1},{0,3},{1,0},{1,2},{2,0},{2,2},{3,1},{3,3}}},{"P",3,{{0,1},{0,2},{1,0},{1,3},{2,1},{2,2},{3,0},{3,3}}}};
 int successes=0;
 for(auto const&node:nodes)for(int off=-64;off<=64;off++){
   vector<Pt>block;for(auto p:node.pts)block.push_back({40+p.x,162+off+p.y});vector<Pt>all=T;all.insert(all.end(),block.begin(),block.end());sort(all.begin(),all.end());all.erase(unique(all.begin(),all.end()),all.end());auto locate=[&](Pt p){return int(lower_bound(all.begin(),all.end(),p)-all.begin());};set<array<int,3>>es;
   for(int i=0;i<(int)T.size();i++)for(int j=i+1;j<(int)T.size();j++)for(auto c:block)if(cross(T[i],T[j],c)==0){array<int,3>e={locate(T[i]),locate(T[j]),locate(c)};sort(e.begin(),e.end());es.insert(e);}for(int i=0;i<(int)block.size();i++)for(int j=i+1;j<(int)block.size();j++)for(auto c:T)if(cross(block[i],block[j],c)==0){array<int,3>e={locate(block[i]),locate(block[j]),locate(c)};sort(e.begin(),e.end());es.insert(e);}Solver s;s.n=all.size();s.edges.assign(es.begin(),es.end());int m=s.minimum(9);if(m!=4)continue;s.sel.assign(s.n,0);set<vector<int>>sets;s.enum_exact(m,sets);cerr<<node.k<<node.v<<" "<<off<<" cores="<<sets.size()<<"\n";
   for(auto const&ixs:sets){vector<Pt>core;set<int>ci(ixs.begin(),ixs.end());for(int ix:ixs)core.push_back(all[ix]);vector<Pt>avail;for(int i=0;i<(int)all.size();i++)if(!ci.count(i))avail.push_back(all[i]);
     for(int budget=4;budget<=7;budget++){
       int e=budget-4;bool found=false;vector<Pt>del,add;
       if(e==0){del=core;found=refill_search(all,del,add);}else if(e==1){for(int a=0;a<(int)avail.size()&&!found;a++){del=core;del.push_back(avail[a]);found=refill_search(all,del,add);}}else if(e==2){for(int a=0;a<(int)avail.size()&&!found;a++)for(int b=a+1;b<(int)avail.size()&&!found;b++){del=core;del.push_back(avail[a]);del.push_back(avail[b]);found=refill_search(all,del,add);}}else if(e==3){for(int a=0;a<(int)avail.size()&&!found;a++)for(int b=a+1;b<(int)avail.size()&&!found;b++)for(int c=b+1;c<(int)avail.size()&&!found;c++){del=core;del.push_back(avail[a]);del.push_back(avail[b]);del.push_back(avail[c]);found=refill_search(all,del,add);}}
       if(found){successes++;sort(del.begin(),del.end());cout<<node.k<<node.v<<" "<<off<<" budget "<<budget<<"\nD";for(auto p:del)cout<<" ("<<p.x<<","<<p.y<<")";cout<<"\nA";for(auto p:add)cout<<" ("<<p.x<<","<<p.y<<")";cout<<"\n";goto next_attempt;}
     }
   }
   next_attempt: ;
 }
 cerr<<"successes="<<successes<<"\n";
}

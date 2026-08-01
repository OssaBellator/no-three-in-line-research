#include <algorithm>
#include <array>
#include <iostream>
#include <functional>
#include <climits>
#include <map>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
struct P{int x,y; bool operator<(P const&o)const{return tie(x,y)<tie(o.x,o.y);} bool operator==(P const&o)const{return x==o.x&&y==o.y;}};
long long cross(P a,P b,P c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);} 
pair<int,int> dir(P a,P b){int dx=b.x-a.x,dy=b.y-a.y;int g=std::gcd(abs(dx),abs(dy));dx/=g;dy/=g;if(dx<0||(dx==0&&dy<0)){dx=-dx;dy=-dy;}return {dx,dy};}

bool refill_search(const vector<P>& original, const vector<P>& deleted, vector<P>& answer){
 set<P> del(deleted.begin(),deleted.end()); vector<P> base; for(auto p:original) if(!del.count(p)) base.push_back(p);
 map<int,int> cc,rc; for(auto p:deleted){cc[p.x]++;rc[p.y]++;}
 vector<int> cols; for(auto [x,n]:cc) for(int i=0;i<n;i++) cols.push_back(x);
 sort(cols.begin(),cols.end(),[&](int a,int b){if(cc[a]!=cc[b])return cc[a]>cc[b];return a<b;});
 map<int,vector<int>> cand;
 for(auto [x,n]:cc){
   for(auto [y,m]:rc){P p{x,y}; if(binary_search(base.begin(),base.end(),p))continue; set<pair<int,int>> ds; bool ok=true; for(auto q:base){auto d=dir(p,q); if(!ds.insert(d).second){ok=false;break;}} if(ok)cand[x].push_back(y);}
   if((int)cand[x].size()<n)return false;
 }
 vector<P> chosen; map<int,int> rem=rc;
 function<bool(int)> dfs=[&](int i){
   if(i==(int)cols.size()){answer=chosen;sort(answer.begin(),answer.end());return true;}
   int x=cols[i]; int prev=INT_MIN; if(i&&cols[i-1]==x) prev=chosen.back().y;
   for(int y:cand[x]){if(y<=prev||rem[y]==0)continue;P p{x,y};if(find(chosen.begin(),chosen.end(),p)!=chosen.end())continue;bool bad=false;
     for(auto s:chosen){for(auto q:base)if(cross(q,s,p)==0){bad=true;break;}if(bad)break;}
     for(int a=0;a<(int)chosen.size()&&!bad;a++)for(int b=a+1;b<(int)chosen.size();b++)if(cross(chosen[a],chosen[b],p)==0){bad=true;break;}
     if(bad)continue; rem[y]--;chosen.push_back(p);if(dfs(i+1))return true;chosen.pop_back();rem[y]++;
   } return false;
 };
 return dfs(0);
}

int main(){
 vector<P> state={
{0,79},{0,110},{1,61},{1,113},{2,1},{2,2},{3,0},{3,3},{4,33},{4,77},{5,1},{5,35},{6,33},{6,34},{7,32},{7,35},{8,34},{8,105},{9,59},{9,60},{10,58},{10,61},{11,59},{11,60},{12,47},{12,105},{13,46},{13,77},{14,47},{14,48},{15,46},{15,49},{16,75},{16,76},{17,74},{17,99},{18,75},{18,76},{19,0},{19,74},{20,106},{20,107},{21,98},{21,108},{22,106},{22,107},{23,2},{23,58},{24,82},{24,110},{25,80},{25,81},{26,48},{26,79},{27,80},{27,81},{28,3},{28,108},{29,111},{29,112},{30,49},{30,113},{31,111},{31,112},{32,98},{32,100},{33,99},{33,101},{34,32},{34,101},{35,82},{35,100}};
 vector<vector<P>> locals={{{0,1},{0,3},{1,0},{1,2},{2,0},{2,2},{3,1},{3,3}},{{0,1},{0,2},{1,0},{1,3},{2,1},{2,2},{3,0},{3,3}}};
 vector<vector<P>> cores={{{36,69},{37,68},{38,66},{38,68},{39,67}},{{36,68},{37,69},{38,67},{38,68},{39,66}}};
 for(int z=0;z<2;z++){
   vector<P> original=state; for(auto p:locals[z]) original.push_back({36+p.x,98-32+p.y}); sort(original.begin(),original.end());
   set<P> core(cores[z].begin(),cores[z].end()); vector<P> avail;for(auto p:original)if(!core.count(p))avail.push_back(p);
   long long checked=0; bool found=false; vector<P> bestdel,bestadd;
   int n=avail.size();
   for(int a=0;a<n&&!found;a++)for(int b=a+1;b<n&&!found;b++)for(int c=b+1;c<n&&!found;c++){
      checked++; vector<P> del=cores[z];del.push_back(avail[a]);del.push_back(avail[b]);del.push_back(avail[c]);vector<P> add;
      if(refill_search(original,del,add)){found=true;bestdel=del;bestadd=add;}
   }
   cout<<"candidate "<<z<<" checked "<<checked<<" found "<<found<<"\n";
   if(found){sort(bestdel.begin(),bestdel.end());for(auto p:bestdel)cout<<"d("<<p.x<<","<<p.y<<") ";cout<<"\n";for(auto p:bestadd)cout<<"a("<<p.x<<","<<p.y<<") ";cout<<"\n";}
 }
}

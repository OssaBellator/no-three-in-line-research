#include <algorithm>
#include <array>
#include <cassert>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
struct Pt{long long x,y;bool operator<(Pt const&o)const{return tie(x,y)<tie(o.x,o.y);}bool operator==(Pt const&o)const{return x==o.x&&y==o.y;}};
long long cross(Pt a,Pt b,Pt c){return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);}
pair<long long,long long> primitive(Pt a,Pt b){long long dx=b.x-a.x,dy=b.y-a.y,g=gcd(llabs(dx),llabs(dy));return {dx/g,dy/g};}
const int N=13;
array<int,N>P={9,4,7,3,0,1,12,8,11,10,2,6,5};
array<int,N>Q={7,12,9,1,4,3,8,0,2,11,5,10,6};
array<int,N>CID={0,1,0,2,1,2,1,1,3,3,3,3,3};
vector<vector<int>>allowed(N);
vector<array<int,N>> minimumCrossMatchings(){
 vector<array<int,N>>out;array<int,N>image{};
 function<void(int,int,int)>dfs=[&](int row,int mask,int crossCount){
   if(crossCount>4)return;
   if(row==N){if(crossCount==4)out.push_back(image);return;}
   for(int target:allowed[row])if(!(mask>>target&1)){
     image[row]=target;
     dfs(row+1,mask|(1<<target),crossCount+(CID[row]!=CID[target]));
   }
 };
 dfs(0,0,0);sort(out.begin(),out.end());return out;
}
vector<array<int,11>> optimalRoutes(array<int,N>const&image,vector<int>const&rows,int&distance){
 map<int,int>index;for(int i=0;i<11;i++)index[rows[i]]=i;map<pair<int,int>,int>memo;
 function<int(int,int)>best=[&](int pos,int mask){if(pos==11)return mask==(1<<11)-1?0:99;auto key=make_pair(pos,mask);auto it=memo.find(key);if(it!=memo.end())return it->second;int row=rows[pos],ans=99;for(int target:allowed[row]){auto jt=index.find(target);if(jt==index.end()||mask>>jt->second&1)continue;ans=min(ans,best(pos+1,mask|(1<<jt->second))+(target!=image[row]));}return memo[key]=ans;};
 distance=best(0,0);vector<array<int,11>>routes;array<int,11>route{};
 function<void(int,int)>gen=[&](int pos,int mask){if(pos==11){routes.push_back(route);return;}int row=rows[pos],goal=best(pos,mask);for(int target:allowed[row]){auto jt=index.find(target);if(jt==index.end()||mask>>jt->second&1)continue;int cost=(target!=image[row])+best(pos+1,mask|(1<<jt->second));if(cost==goal){route[pos]=target;gen(pos+1,mask|(1<<jt->second));}}};
 gen(0,0);return routes;
}
vector<vector<int>> compositions(){vector<vector<int>>out;vector<int>cur;function<void(int)>dfs=[&](int rem){if(rem==0){out.push_back(cur);return;}for(int first=1;first<=rem;first++){cur.push_back(first);dfs(rem-first);cur.pop_back();}};dfs(11);return out;}
bool embed(vector<int>const&rows,array<int,11>const&image,vector<int>const&lengths,long long&maxcoord){
 vector<Pt>source;for(int r:rows){source.push_back({r,P[r]});source.push_back({r,Q[r]});}
 for(int i=0;i<22;i++)for(int j=i+1;j<22;j++)for(int k=j+1;k<22;k++)if(cross(source[i],source[j],source[k])==0)return false;
 set<int>rowset(rows.begin(),rows.end());vector<pair<Pt,Pt>>anchors;
 for(int i=0;i<11;i++){int r=rows[i],target=image[i];if(!rowset.count(target))return false;Pt a{r,P[r]},b{target,Q[target]};if(a.x==b.x||a.y==b.y)return false;anchors.push_back({a,b});}
 set<Pt>used;for(auto [a,b]:anchors){used.insert(a);used.insert(b);}if(used.size()!=22)return false;
 vector<Pt>pts=source;vector<int>labels(22,-1);
 for(int run=0;run<(int)lengths.size();run++){auto [a,b]=anchors[run];for(int i=0;i<22;i++)if(pts[i]==a||pts[i]==b)labels[i]=run;}
 set<long long>occupiedRows,occupiedCols;for(auto p:pts){occupiedRows.insert(p.x);occupiedCols.insert(p.y);}
 for(int run=0;run<(int)lengths.size();run++){
   auto [a,b]=anchors[run];auto [dx,dy]=primitive(a,b);int inserted=0;
   for(long long mag=1;mag<50000&&inserted<lengths[run];mag++)for(long long sign:{1LL,-1LL}){
     Pt c{a.x+sign*mag*dx,a.y+sign*mag*dy};
     if(occupiedRows.count(c.x)||occupiedCols.count(c.y)||find(pts.begin(),pts.end(),c)!=pts.end())continue;
     bool bad=false;
     for(int i=0;i<(int)pts.size()&&!bad;i++)for(int j=i+1;j<(int)pts.size();j++)if(cross(pts[i],pts[j],c)==0){if(labels[i]==run&&labels[j]==run)continue;bad=true;break;}
     if(bad)continue;pts.push_back(c);labels.push_back(run);occupiedRows.insert(c.x);occupiedCols.insert(c.y);inserted++;break;
   }
   if(inserted!=lengths[run])return false;
 }
 for(int i=0;i<(int)pts.size();i++)for(int j=i+1;j<(int)pts.size();j++)for(int k=j+1;k<(int)pts.size();k++)if(cross(pts[i],pts[j],pts[k])==0&&!(labels[i]>=0&&labels[i]==labels[j]&&labels[j]==labels[k]))return false;
 for(auto p:pts)maxcoord=max({maxcoord,llabs(p.x),llabs(p.y)});return true;
}
int main(){
 for(int row=0;row<N;row++)for(int target=0;target<N;target++)if(target!=row&&Q[target]!=P[row])allowed[row].push_back(target);
 auto matchings=minimumCrossMatchings();assert(matchings.size()==104);auto comps=compositions();assert(comps.size()==1024);
 vector<vector<int>>deletions={{1,3,4,5,6,7,8,9,10,11,12},{0,1,2,4,6,7,8,9,10,11,12}};
 map<int,int>distanceHist;map<int,map<long long,int>>coordinateHist;map<int,long long>routeCountHist;long long audits=0;int cases=0;
 for(int mi=0;mi<(int)matchings.size();mi++)for(int deletion=0;deletion<2;deletion++){
   int distance;auto routes=optimalRoutes(matchings[mi],deletions[deletion],distance);distanceHist[distance]++;routeCountHist[routes.size()]++;
   if(distance!=4||routes.empty()){cerr<<"bad matching="<<mi<<" deletion="<<deletion<<" distance="<<distance<<" routes="<<routes.size()<<"\n";return 2;}
   auto route=routes.front();long long maximum=0;int passed=0;
   for(auto const&composition:comps){if(embed(deletions[deletion],route,composition,maximum))passed++;audits++;}
   if(passed!=1024){cerr<<"fail matching="<<mi<<" deletion="<<deletion<<" passed="<<passed<<"\n";return 3;}
   coordinateHist[deletion][maximum]++;cases++;
 }
 cout<<"matchings="<<matchings.size()<<" cases="<<cases<<" compositions="<<comps.size()<<" audits="<<audits<<"\n";
 cout<<"distance_hist";for(auto [d,c]:distanceHist)cout<<" "<<d<<":"<<c;cout<<"\n";
 cout<<"optimal_route_count_hist";for(auto [r,c]:routeCountHist)cout<<" "<<r<<":"<<c;cout<<"\n";
 for(auto &[deletion,h]:coordinateHist){cout<<"deletion="<<deletion<<" maxcoord";for(auto [coordinate,count]:h)cout<<" "<<coordinate<<":"<<count;cout<<"\n";}
}

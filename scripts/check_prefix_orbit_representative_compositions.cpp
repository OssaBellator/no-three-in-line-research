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
struct Case{int representative,deletion;vector<int>rows;array<int,11>route;};
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
     for(int i=0;i<(int)pts.size()&&!bad;i++)for(int j=i+1;j<(int)pts.size();j++)if(cross(pts[i],pts[j],c)==0){
       if(labels[i]==run&&labels[j]==run)continue;bad=true;break;
     }
     if(bad)continue;
     pts.push_back(c);labels.push_back(run);occupiedRows.insert(c.x);occupiedCols.insert(c.y);inserted++;break;
   }
   if(inserted!=lengths[run])return false;
 }
 for(int i=0;i<(int)pts.size();i++)for(int j=i+1;j<(int)pts.size();j++)for(int k=j+1;k<(int)pts.size();k++)
   if(cross(pts[i],pts[j],pts[k])==0&&!(labels[i]>=0&&labels[i]==labels[j]&&labels[j]==labels[k]))return false;
 for(auto p:pts)maxcoord=max({maxcoord,llabs(p.x),llabs(p.y)});
 return true;
}
int main(){
 vector<Case>cases;
 cases.push_back(Case{0,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,10,8,12,9,11}});
 cases.push_back(Case{0,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,10,8,12,9,11}});
 cases.push_back(Case{1,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,10,8,12,11,9}});
 cases.push_back(Case{1,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,10,8,12,11,9}});
 cases.push_back(Case{2,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,10,8,9,12,11}});
 cases.push_back(Case{2,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,10,8,9,12,11}});
 cases.push_back(Case{3,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,10,8,9,11,12}});
 cases.push_back(Case{3,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,10,8,9,11,12}});
 cases.push_back(Case{4,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,8,10,12,9,11}});
 cases.push_back(Case{4,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,8,10,12,9,11}});
 cases.push_back(Case{5,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,8,10,12,11,9}});
 cases.push_back(Case{5,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,8,10,12,11,9}});
 cases.push_back(Case{6,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,8,10,9,12,11}});
 cases.push_back(Case{6,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,8,10,9,12,11}});
 cases.push_back(Case{7,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,8,10,9,11,12}});
 cases.push_back(Case{7,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,8,10,9,11,12}});
 cases.push_back(Case{8,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,12,8,10,9,11}});
 cases.push_back(Case{8,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,12,8,10,9,11}});
 cases.push_back(Case{9,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,12,8,10,11,9}});
 cases.push_back(Case{9,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,12,8,10,11,9}});
 cases.push_back(Case{10,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,12,8,9,10,11}});
 cases.push_back(Case{10,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,12,8,9,10,11}});
 cases.push_back(Case{11,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,12,8,9,11,10}});
 cases.push_back(Case{11,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,12,8,9,11,10}});
 cases.push_back(Case{12,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,9,8,10,12,11}});
 cases.push_back(Case{12,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,9,8,10,12,11}});
 cases.push_back(Case{13,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,9,8,10,11,12}});
 cases.push_back(Case{13,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,9,8,10,11,12}});
 cases.push_back(Case{14,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,9,8,12,10,11}});
 cases.push_back(Case{14,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,9,8,12,10,11}});
 cases.push_back(Case{15,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,9,8,12,11,10}});
 cases.push_back(Case{15,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,9,8,12,11,10}});
 cases.push_back(Case{16,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,9,8,11,10,12}});
 cases.push_back(Case{16,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,9,8,11,10,12}});
 cases.push_back(Case{17,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,9,8,11,12,10}});
 cases.push_back(Case{17,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,9,8,11,12,10}});
 cases.push_back(Case{18,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,9,8,10,11,12}});
 cases.push_back(Case{18,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,9,8,10,11,12}});
 cases.push_back(Case{19,0,{1,3,4,5,6,7,8,9,10,11,12},{3,1,5,6,7,4,9,8,10,12,11}});
 cases.push_back(Case{19,1,{0,1,2,4,6,7,8,9,10,11,12},{1,0,6,2,7,4,9,8,10,12,11}});
 auto comps=compositions();assert(comps.size()==1024);
 map<int,map<long long,int>>hist;long long audits=0;
 for(auto const&ca:cases){long long maximum=0;int passed=0;for(auto const&composition:comps){if(embed(ca.rows,ca.route,composition,maximum))passed++;audits++;}
   cout<<"representative="<<ca.representative<<" deletion="<<ca.deletion<<" passed="<<passed<<" maximum="<<maximum<<"\n";
   if(passed!=1024)return 2;hist[ca.deletion][maximum]++;
 }
 cerr<<"cases="<<cases.size()<<" compositions="<<comps.size()<<" audits="<<audits<<"\n";
 for(auto &[deletion,h]:hist){cerr<<"deletion="<<deletion<<" hist";for(auto [coordinate,count]:h)cerr<<" "<<coordinate<<":"<<count;cerr<<"\n";}
}

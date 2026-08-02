#include <algorithm>
#include <array>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
struct Pt{long long x,y; bool operator<(Pt const&o)const{return tie(x,y)<tie(o.x,o.y);} bool operator==(Pt const&o)const{return x==o.x&&y==o.y;}};
long long cross(Pt a,Pt b,Pt c){return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);}
pair<long long,long long> primitive(Pt a,Pt b){long long dx=b.x-a.x,dy=b.y-a.y,g=gcd(llabs(dx),llabs(dy));return {dx/g,dy/g};}
const int N=14;
array<int,N>P={8,3,4,11,13,6,1,12,7,0,10,5,2,9};
array<int,N>Q={4,11,8,3,7,12,13,0,1,6,2,9,10,5};
array<int,N>PAIR={1,0,3,2,5,4,7,6,9,8,11,10,13,12};
vector<Pt>SOURCE; vector<pair<Pt,Pt>>ANCHORS;
long long compositions_checked=0,maxcoord=0;

vector<Pt> embed(vector<int> const&lengths){
 vector<Pt> pts=SOURCE; vector<int> labels(pts.size(),-1);
 for(int run=0;run<(int)lengths.size();run++){
   auto [a,b]=ANCHORS[run];
   for(int i=0;i<(int)pts.size();i++)if(pts[i]==a||pts[i]==b)labels[i]=run;
 }
 set<long long> rows,cols;for(auto p:pts){rows.insert(p.x);cols.insert(p.y);}
 for(int run=0;run<(int)lengths.size();run++){
   auto [a,b]=ANCHORS[run];auto [dx,dy]=primitive(a,b);int inserted=0;
   for(long long mag=1;mag<50000&&inserted<lengths[run];mag++)for(long long sign:{1LL,-1LL}){
     Pt c{a.x+sign*mag*dx,a.y+sign*mag*dy};
     if(rows.count(c.x)||cols.count(c.y)||find(pts.begin(),pts.end(),c)!=pts.end())continue;
     bool bad=false;
     for(int i=0;i<(int)pts.size()&&!bad;i++)for(int j=i+1;j<(int)pts.size();j++)if(cross(pts[i],pts[j],c)==0){if(labels[i]==run&&labels[j]==run)continue;bad=true;break;}
     if(bad)continue;
     pts.push_back(c);labels.push_back(run);rows.insert(c.x);cols.insert(c.y);inserted++;break;
   }
   assert(inserted==lengths[run]);
 }
 for(int i=0;i<(int)pts.size();i++)for(int j=i+1;j<(int)pts.size();j++)for(int k=j+1;k<(int)pts.size();k++)if(cross(pts[i],pts[j],pts[k])==0)assert(labels[i]>=0&&labels[i]==labels[j]&&labels[j]==labels[k]);
 return pts;
}
void compositions(int rem,vector<int>&cur){
 if(rem==0){auto pts=embed(cur);compositions_checked++;for(auto p:pts)maxcoord=max({maxcoord,llabs(p.x),llabs(p.y)});return;}
 for(int first=1;first<=rem;first++){cur.push_back(first);compositions(rem-first,cur);cur.pop_back();}
}
int main(){
 array<int,N>a=P,b=Q;sort(a.begin(),a.end());sort(b.begin(),b.end());
 for(int i=0;i<N;i++){assert(a[i]==i&&b[i]==i&&P[i]!=Q[i]);SOURCE.push_back({i,P[i]});SOURCE.push_back({i,Q[i]});}
 assert(set<Pt>(SOURCE.begin(),SOURCE.end()).size()==2*N);
 for(int r=0;r<N;r++){int n=0;for(auto p:SOURCE)n+=p.x==r;assert(n==2);}for(int c=0;c<N;c++){int n=0;for(auto p:SOURCE)n+=p.y==c;assert(n==2);}
 for(int i=0;i<2*N;i++)for(int j=i+1;j<2*N;j++)for(int k=j+1;k<2*N;k++)assert(cross(SOURCE[i],SOURCE[j],SOURCE[k])!=0);
 for(int r=0;r<N;r++){Pt x{r,P[r]},y{PAIR[r],Q[PAIR[r]]};assert(x.x!=y.x&&x.y!=y.y);ANCHORS.push_back({x,y});}
 set<Pt>used;for(auto [x,y]:ANCHORS){used.insert(x);used.insert(y);}assert(used.size()==2*N);
 vector<int> inv(N);for(int i=0;i<N;i++)inv[Q[i]]=i;vector<int> seenRows(N),sizes;
 for(int r=0;r<N;r++)if(!seenRows[r]){int cur=r,size=0;do{seenRows[cur]=1;size++;cur=inv[P[cur]];}while(!seenRows[cur]);sizes.push_back(size);}
 sort(sizes.begin(),sizes.end());assert((sizes==vector<int>{2,2,2,2,3,3}));
 vector<int>cur;compositions(N,cur);assert(compositions_checked==8192);
 cout<<"compositions="<<compositions_checked<<" maximum_coordinate="<<maxcoord<<" components=2,2,2,2,3,3 induced12=4 induced11=2 component_anchor=false\n";
 cout<<"P";for(int x:P)cout<<" "<<x;cout<<"\nQ";for(int x:Q)cout<<" "<<x;cout<<"\nPAIR";for(int x:PAIR)cout<<" "<<x;cout<<"\n";
}

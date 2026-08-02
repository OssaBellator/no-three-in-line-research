#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
using Pt=pair<int,int>;
long long cross(Pt a,Pt b,Pt c){return 1LL*(b.first-a.first)*(c.second-a.second)-1LL*(b.second-a.second)*(c.first-a.first);}
pair<int,int> prim(Pt a,Pt b){int dx=b.first-a.first,dy=b.second-a.second,g=gcd(abs(dx),abs(dy));return {dx/g,dy/g};}
void compositions(int total, vector<int>&cur, vector<vector<int>>&out){if(total==0){out.push_back(cur);return;}for(int first=1;first<=total;first++){cur.push_back(first);compositions(total-first,cur,out);cur.pop_back();}}
int main(){
 const int N=14; vector<int>P={8,6,2,3,10,13,5,12,1,0,4,9,11,7};vector<int>Q={7,3,8,0,11,1,2,10,9,13,5,12,4,6};vector<int>pairing(N);for(int r=0;r<N;r++)pairing[r]=(r+5)%N;
 vector<Pt> source;for(int r=0;r<N;r++)source.push_back({r,P[r]});for(int r=0;r<N;r++)source.push_back({r,Q[r]});
 for(int i=0;i<(int)source.size();i++)for(int j=i+1;j<(int)source.size();j++)for(int k=j+1;k<(int)source.size();k++)if(cross(source[i],source[j],source[k])==0){cerr<<"source bad\n";return 1;}
 vector<pair<Pt,Pt>> anchors;for(int r=0;r<N;r++){Pt a={r,P[r]},b={pairing[r],Q[pairing[r]]};if(a.first==b.first||a.second==b.second){cerr<<"anchor bad\n";return 1;}anchors.push_back({a,b});}
 vector<vector<int>> comps;vector<int>cur;compositions(N,cur,comps);long long checked=0;int maxcoord=0;
 for(auto const&lens:comps){
   vector<Pt> pts=source;vector<int>labels(pts.size(),-1);map<Pt,int>pos;for(int i=0;i<(int)pts.size();i++)pos[pts[i]]=i;
   for(int run=0;run<(int)lens.size();run++){labels[pos[anchors[run].first]]=run;labels[pos[anchors[run].second]]=run;}
   set<int> rows,cols;for(auto p:pts){rows.insert(p.first);cols.insert(p.second);}
   for(int run=0;run<(int)lens.size();run++){
     auto [anchor,other]=anchors[run];auto [dx,dy]=prim(anchor,other);int inserted=0;
     for(int mag=1;mag<50000&&inserted<lens[run];mag++)for(int sign: {1,-1}){
       Pt cand={anchor.first+sign*mag*dx,anchor.second+sign*mag*dy};
       if(pos.count(cand)||rows.count(cand.first)||cols.count(cand.second))continue;bool bad=false;
       for(int i=0;i<(int)pts.size()&&!bad;i++)for(int j=i+1;j<(int)pts.size();j++)if(cross(pts[i],pts[j],cand)==0 && !(labels[i]==run&&labels[j]==run)){bad=true;break;}
       if(bad)continue;pos[cand]=pts.size();pts.push_back(cand);labels.push_back(run);rows.insert(cand.first);cols.insert(cand.second);inserted++;if(inserted==lens[run])break;
     }
     if(inserted!=lens[run]){cerr<<"insertion fail\n";return 1;}
   }
   for(int i=0;i<(int)pts.size();i++)for(int j=i+1;j<(int)pts.size();j++)for(int k=j+1;k<(int)pts.size();k++)if(cross(pts[i],pts[j],pts[k])==0 && !(labels[i]>=0&&labels[i]==labels[j]&&labels[j]==labels[k])){cerr<<"mixed fail\n";return 1;}
   for(auto p:pts)maxcoord=max({maxcoord,abs(p.first),abs(p.second)});checked++;
 }
 vector<int> qinv(N);for(int r=0;r<N;r++)qinv[Q[r]]=r;vector<int>sigma(N);for(int r=0;r<N;r++)sigma[r]=qinv[P[r]];vector<int>seen(N);int components=0;vector<int>sizes;for(int r=0;r<N;r++)if(!seen[r]){components++;int current=r,size=0;while(!seen[current]){seen[current]=1;size++;current=sigma[current];}sizes.push_back(size);}sort(sizes.begin(),sizes.end());
 cout<<"OK compositions="<<checked<<" max_coordinate="<<maxcoord<<" components="<<components<<" component_sizes";for(int v:sizes)cout<<" "<<v;cout<<" pairing";for(int v:pairing)cout<<" "<<v;cout<<"\n";
}

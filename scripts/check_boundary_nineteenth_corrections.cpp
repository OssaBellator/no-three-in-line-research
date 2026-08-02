#include <algorithm>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
struct Pt{int x,y;bool operator<(Pt const&o)const{return tie(x,y)<tie(o.x,o.y);}bool operator==(Pt const&o)const{return x==o.x&&y==o.y;}};
long long cross(Pt a,Pt b,Pt c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
pair<int,int> ndir(Pt a,Pt b){int dx=b.x-a.x,dy=b.y-a.y,g=gcd(abs(dx),abs(dy));dx/=g;dy/=g;if(dx<0||(dx==0&&dy<0)){dx=-dx;dy=-dy;}return {dx,dy};}

bool search_deletion(vector<Pt>const&all, vector<Pt>D, vector<Pt>&answer, unsigned long long&tested){
 sort(D.begin(),D.end());set<Pt>ds(D.begin(),D.end());vector<Pt>base;for(auto p:all)if(!ds.count(p))base.push_back(p);sort(base.begin(),base.end());
 vector<int>xs,ys;for(auto p:D){xs.push_back(p.x);ys.push_back(p.y);}sort(xs.begin(),xs.end());sort(ys.begin(),ys.end());
 vector<Pt>grid;map<Pt,int>index;for(int x:xs)for(int y:ys){Pt p{x,y};if(!index.count(p)){index[p]=grid.size();grid.push_back(p);}}
 int g=grid.size();vector<char>point_ok(g,1);vector<vector<char>>pair_ok(g,vector<char>(g,1));
 for(int i=0;i<g;i++){if(binary_search(base.begin(),base.end(),grid[i])){point_ok[i]=0;continue;}set<pair<int,int>>dirs;for(auto q:base)if(!dirs.insert(ndir(grid[i],q)).second){point_ok[i]=0;break;}}
 for(auto r:base){map<pair<int,int>,vector<int>>groups;for(int i=0;i<g;i++)if(point_ok[i])groups[ndir(r,grid[i])].push_back(i);for(auto &en:groups){auto &v=en.second;for(int i=0;i<(int)v.size();i++)for(int j=i+1;j<(int)v.size();j++)pair_ok[v[i]][v[j]]=pair_ok[v[j]][v[i]]=0;}}
 do{tested++;vector<Pt>A;vector<int>ix;set<Pt>uni;bool ok=true;for(int i=0;i<(int)D.size();i++){Pt p{xs[i],ys[i]};if(!uni.insert(p).second){ok=false;break;}int z=index[p];if(!point_ok[z]){ok=false;break;}A.push_back(p);ix.push_back(z);}if(!ok||uni==ds)continue;for(int i=0;i<(int)A.size()&&ok;i++)for(int j=i+1;j<(int)A.size();j++)if(!pair_ok[ix[i]][ix[j]]){ok=false;break;}for(int i=0;i<(int)A.size()&&ok;i++)for(int j=i+1;j<(int)A.size();j++)for(int k=j+1;k<(int)A.size();k++)if(cross(A[i],A[j],A[k])==0){ok=false;break;}if(ok){answer=A;sort(answer.begin(),answer.end());return true;}}while(next_permutation(ys.begin(),ys.end()));return false;
}

bool search_budget(vector<Pt>const&all,vector<Pt>const&core,int budget,vector<Pt>&Dout,vector<Pt>&Aout,unsigned long long&tested){set<Pt>cs(core.begin(),core.end());vector<Pt>av;for(auto p:all)if(!cs.count(p))av.push_back(p);int extras=budget-(int)core.size();vector<Pt>ch;bool found=false;function<void(int,int)>go=[&](int st,int left){if(found)return;if(left==0){vector<Pt>D=core;D.insert(D.end(),ch.begin(),ch.end());vector<Pt>A;if(search_deletion(all,D,A,tested)){Dout=D;sort(Dout.begin(),Dout.end());Aout=A;found=true;}return;}for(int i=st;i<=(int)av.size()-left&&!found;i++){ch.push_back(av[i]);go(i+1,left-1);ch.pop_back();}};go(0,extras);return found;}

int main(){
 vector<Pt> all={{0,196},{0,252},{1,61},{1,113},{2,98},{2,213},{3,3},{3,100},{4,33},{4,77},{5,1},{5,35},{6,2},{6,33},{7,32},{7,35},{8,34},{8,105},{9,60},{9,349},{10,58},{10,61},{11,59},{11,60},{12,2},{12,105},{13,46},{13,77},{14,47},{14,258},{15,46},{15,49},{16,75},{16,76},{17,74},{17,99},{18,76},{18,316},{19,0},{19,346},{20,106},{20,107},{21,0},{21,108},{22,107},{22,315},{23,58},{23,195},{24,82},{24,110},{25,80},{25,81},{26,47},{26,48},{27,80},{27,81},{28,3},{28,108},{29,111},{29,112},{30,49},{30,113},{31,112},{31,257},{32,98},{32,258},{33,99},{33,101},{34,32},{34,101},{35,82},{35,100},{36,163},{36,164},{37,162},{37,165},{38,163},{38,164},{39,162},{39,312},{40,34},{40,315},{41,194},{41,195},{42,193},{42,196},{43,79},{43,194},{44,260},{44,377},{45,257},{45,259},{46,1},{46,259},{47,48},{47,260},{48,165},{48,313},{49,314},{49,316},{50,193},{50,314},{51,75},{51,313},{52,79},{52,379},{53,376},{53,378},{54,253},{54,376},{55,377},{55,379},{56,346},{56,348},{57,347},{57,349},{58,74},{58,216},{59,59},{59,348},{60,309},{60,312},{61,310},{61,311},{62,106},{62,309},{63,310},{63,311},{64,110},{64,255},{65,252},{65,254},{66,193},{66,254},{67,253},{67,255},{68,213},{68,215},{69,214},{69,215},{70,214},{70,216},{71,111},{71,347},{72,150},{72,152},{73,149},{73,151},{74,149},{74,151},{75,150},{75,152}}; sort(all.begin(),all.end());
 vector<vector<Pt>> cores={
  {{13,77},{73,151},{75,150},{75,152}},
  {{33,101},{73,151},{75,150},{75,152}},
  {{36,163},{73,149},{73,151},{75,152}},
  {{39,162},{73,149},{73,151},{75,152}},
  {{73,149},{73,151},{75,150},{75,152}}
 };
 const vector<unsigned long long> expected6={7595280,7595280,7595280,7595280,7595280};
 for(int i=0;i<(int)cores.size();i++){
  cout<<"P2/-64 core"<<i+1; for(auto p:cores[i])cout<<" ("<<p.x<<","<<p.y<<")"; cout<<"\n";
  for(int budget=4;budget<=6;budget++){unsigned long long tested=0;vector<Pt>D,A;bool ok=search_budget(all,cores[i],budget,D,A,tested);if(ok){cerr<<"unexpected repair core="<<i+1<<" budget="<<budget<<"\n";return 1;} if(budget==4&&tested!=24)return 2; if(budget==5&&tested!=17520)return 3; if(budget==6&&tested!=expected6[i])return 4; cout<<"budget "<<budget<<" none tested "<<tested<<"\n";}
 }
 cout<<"summary attempts=1 cores=5 none_through_budget_6=true\n";
}

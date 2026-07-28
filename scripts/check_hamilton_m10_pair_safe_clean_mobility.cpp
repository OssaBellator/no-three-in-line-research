#include <algorithm>
#include <array>
#include <bitset>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int M=10,N=20,Q=1<<M,TR=120;
using Rho=array<uint8_t,M>;
struct RH{size_t operator()(Rho const&r)const noexcept{size_t h=0;for(auto x:r)h=h*17+x+1;return h;}};
struct Point{int x,y;};
struct Edge{uint8_t a,b,p;};
array<Point,4> orbit(int s,int t,int e){auto J=[](int x){return N-1-x;};Point q0{s,e?J(t):t},q1{J(s),e?t:J(t)};return {q0,q1,Point{J(q0.y),q0.x},Point{J(q1.y),q1.x}};}
bool col(Point a,Point b,Point c){return 1LL*(b.x-a.x)*(c.y-a.y)==1LL*(b.y-a.y)*(c.x-a.x);}
bool bad(int sa,int ta,int ea,int sb,int tb,int eb){auto A=orbit(sa,ta,ea),B=orbit(sb,tb,eb);array<Point,8>P{};for(int i=0;i<4;i++)P[i]=A[i],P[i+4]=B[i];for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++){int owners=(i<4)+(j<4)+(k<4);if((owners==1||owners==2)&&col(P[i],P[j],P[k]))return true;}return false;}
vector<Rho> cycles(){vector<Rho>out;array<int,M-1>tail{};iota(tail.begin(),tail.end(),1);do{array<int,M>ord{};ord[0]=0;for(int i=1;i<M;i++)ord[i]=tail[i-1];Rho r{};for(int i=0;i<M;i++)r[ord[i]]=ord[(i+1)%M];out.push_back(r);}while(next_permutation(tail.begin(),tail.end()));return out;}
Rho sw(Rho const&r,uint16_t mask){int st=0;while(!(mask&(1<<st)))++st;array<int,3>s{};int c=0,cur=st;for(int z=0;z<M;z++){if(mask&(1<<cur))s[c++]=cur;cur=r[cur];}Rho o=r;int b0=r[s[0]],b1=r[s[1]],b2=r[s[2]];o[s[0]]=b1;o[s[1]]=b2;o[s[2]]=b0;return o;}
int main(){
 static uint8_t rel[M][M][M][M];
 for(int a=0;a<M;a++)for(int ta=0;ta<M;ta++)if(a!=ta)for(int b=a+1;b<M;b++)for(int tb=0;tb<M;tb++)if(b!=tb&&ta!=tb){bool eq=bad(a,ta,0,b,tb,0),un=bad(a,ta,0,b,tb,1);rel[a][ta][b][tb]=eq&&un?3:eq?2:un?1:0;}
 vector<uint16_t> triples;for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)for(int c=b+1;c<M;c++)triples.push_back((1<<a)|(1<<b)|(1<<c));
 array<bitset<TR>,TR> meeting{};for(int i=0;i<TR;i++)for(int j=0;j<TR;j++)if(triples[i]&triples[j])meeting[i].set(j);
 auto rhos=cycles();unordered_map<Rho,int,RH>id;id.reserve(rhos.size()*2);for(int i=0;i<(int)rhos.size();i++)id[rhos[i]]=i;
 int C=rhos.size();vector<int8_t> lambda(C,-1);vector<uint8_t> clean(C),pairsafe(C);vector<uint8_t> components(C);map<int,int> lambda_hist;map<int,int> impossible_hist;map<int,int> rank_hist;long long total_clean_orient=0;
 vector<Edge> edges;edges.reserve(32);
 for(int ri=0;ri<C;ri++){
  edges.clear();int impossible=0;
  for(int a=0;a<M;a++)for(int b=a+1;b<M;b++){int v=rel[a][rhos[ri][a]][b][rhos[ri][b]];if(v==3)impossible++;else if(v)edges.push_back({(uint8_t)a,(uint8_t)b,(uint8_t)(v==1?0:1)});}
  impossible_hist[impossible]++;
  if(impossible)continue;
  pairsafe[ri]=1;int best=100;
  for(int mask=0;mask<Q;mask++){int vio=0;for(auto e:edges)vio+=((((mask>>e.a)^(mask>>e.b))&1)!=e.p);best=min(best,vio);}
  lambda[ri]=best;lambda_hist[best]++;if(best==0){clean[ri]=1;array<vector<int>,M>adj;for(auto e:edges){adj[e.a].push_back(e.b);adj[e.b].push_back(e.a);}array<uint8_t,M>seen{};int comp=0;for(int s=0;s<M;s++)if(!seen[s]){comp++;deque<int>q;q.push_back(s);seen[s]=1;while(!q.empty()){int x=q.front();q.pop_front();for(int y:adj[x])if(!seen[y])seen[y]=1,q.push_back(y);}}components[ri]=comp;int rank=edges.size()-M+comp;rank_hist[rank]++;total_clean_orient+=1LL<<comp;}
 }
 cerr<<"classified cycles="<<C<<" pair-safe="<<accumulate(pairsafe.begin(),pairsafe.end(),0LL)<<" clean="<<accumulate(clean.begin(),clean.end(),0LL)<<"\n";
 int min_clean_degree=1000,max_clean_degree=0,min_meeting=1000;long long clean_edges=0;vector<bitset<TR>> clean_masks(C);
 for(int ri=0;ri<C;ri++)if(clean[ri]){bitset<TR> cm;for(int ti=0;ti<TR;ti++){int j=id[sw(rhos[ri],triples[ti])];if(clean[j])cm.set(ti);}clean_masks[ri]=cm;int deg=cm.count();min_clean_degree=min(min_clean_degree,deg);max_clean_degree=max(max_clean_degree,deg);clean_edges+=deg;for(int si=0;si<TR;si++)min_meeting=min(min_meeting,(int)(cm&meeting[si]).count());}
 vector<uint8_t> clean_seen(C);int clean_components=0,largest_clean_component=0;
 for(int root=0;root<C;root++)if(clean[root]&&!clean_seen[root]){clean_components++;int size=0;deque<int>qq;qq.push_back(root);clean_seen[root]=1;while(!qq.empty()){int x=qq.front();qq.pop_front();size++;for(int ti=0;ti<TR;ti++)if(clean_masks[x].test(ti)){int y=id[sw(rhos[x],triples[ti])];if(!clean_seen[y])clean_seen[y]=1,qq.push_back(y);}}largest_clean_component=max(largest_clean_component,size);}
 vector<int16_t> dist(C,-1);deque<int>q;for(int i=0;i<C;i++)if(clean[i])dist[i]=0,q.push_back(i);while(!q.empty()){int x=q.front();q.pop_front();for(auto mask:triples){int y=id[sw(rhos[x],mask)];if(pairsafe[y]&&dist[y]<0)dist[y]=dist[x]+1,q.push_back(y);}}
 map<int,int> dist_hist;int un=0,maxdist=0;for(int i=0;i<C;i++)if(pairsafe[i]){if(dist[i]<0)un++;else dist_hist[dist[i]]++,maxdist=max(maxdist,(int)dist[i]);}
 map<int,int> best_target_hist;map<pair<int,int>,int> source_best;int no_descent=0;for(int i=0;i<C;i++)if(pairsafe[i]&&lambda[i]>0){int best=100;for(auto mask:triples){int y=id[sw(rhos[i],mask)];if(pairsafe[y])best=min(best,(int)lambda[y]);}best_target_hist[best]++;source_best[{lambda[i],best}]++;if(best>=lambda[i])no_descent++;}
 long long optimal_violated_edge_checks=0;int minimum_targeted_clean_rotations=1000;int minimum_clean_rotations_from_positive=1000;int untargetable_optimal_edges=0;
 for(int ri=0;ri<C;ri++)if(pairsafe[ri]&&lambda[ri]>0){
  edges.clear();for(int a=0;a<M;a++)for(int b=a+1;b<M;b++){int v=rel[a][rhos[ri][a]][b][rhos[ri][b]];if(v&&v!=3)edges.push_back({(uint8_t)a,(uint8_t)b,(uint8_t)(v==1?0:1)});}
  bitset<TR> to_clean;for(int ti=0;ti<TR;ti++){int y=id[sw(rhos[ri],triples[ti])];if(clean[y])to_clean.set(ti);}minimum_clean_rotations_from_positive=min(minimum_clean_rotations_from_positive,(int)to_clean.count());
  for(int mask=0;mask<Q;mask++){vector<Edge> violated;for(auto e:edges)if(((((mask>>e.a)^(mask>>e.b))&1)!=e.p))violated.push_back(e);if((int)violated.size()!=lambda[ri])continue;for(auto e:violated){optimal_violated_edge_checks++;int count=0;uint16_t owner=(1<<e.a)|(1<<e.b);for(int ti=0;ti<TR;ti++)if(to_clean.test(ti)&&(triples[ti]&owner))count++;minimum_targeted_clean_rotations=min(minimum_targeted_clean_rotations,count);if(!count)untargetable_optimal_edges++;}}
 }
 long long pair_safe_count=accumulate(pairsafe.begin(),pairsafe.end(),0LL);
 long long clean_count=accumulate(clean.begin(),clean.end(),0LL);
 bool ok=C==362880 && pair_safe_count==342720 && clean_count==297886 &&
  total_clean_orient==115586396 && impossible_hist==map<int,int>{{0,342720},{1,20160}} &&
  lambda_hist==map<int,int>{{0,297886},{1,42190},{2,2582},{3,62}} &&
  rank_hist==map<int,int>{{0,296298},{1,1588}} && min_clean_degree==69 &&
  max_clean_degree==120 && min_meeting==40 && clean_components==1 &&
  largest_clean_component==297886 && dist_hist==map<int,int>{{0,297886},{1,44834}} &&
  un==0 && maxdist==1 && source_best==map<pair<int,int>,int>{{{1,0},42190},{{2,0},2582},{{3,0},62}} && no_descent==0 && optimal_violated_edge_checks==13185264 && minimum_targeted_clean_rotations==6 && minimum_clean_rotations_from_positive==11 && untargetable_optimal_edges==0;
 if(!ok){cerr<<"verification mismatch\n";return 1;}
 cout<<"{\n  \"m\":10,\n  \"hamilton_cycles\":"<<C<<",\n  \"pair_safe_cycles\":"<<pair_safe_count<<",\n  \"clean_cycles\":"<<clean_count<<",\n  \"total_clean_orientations\":"<<total_clean_orient<<",\n  \"lambda_distribution\":{";bool f=1;for(auto[k,v]:lambda_hist){if(!f)cout<<",";f=0;cout<<"\""<<k<<"\":"<<v;}cout<<"},\n  \"clean_rank_distribution\":{";f=1;for(auto[k,v]:rank_hist){if(!f)cout<<",";f=0;cout<<"\""<<k<<"\":"<<v;}cout<<"},\n  \"minimum_clean_degree\":"<<min_clean_degree<<",\n  \"maximum_clean_degree\":"<<max_clean_degree<<",\n  \"minimum_clean_rotations_intersecting_any_owner_triple\":"<<min_meeting<<",\n  \"clean_induced_components\":"<<clean_components<<",\n  \"largest_clean_component\":"<<largest_clean_component<<",\n  \"pair_safe_distance_to_clean_distribution\":{";f=1;for(auto[k,v]:dist_hist){if(!f)cout<<",";f=0;cout<<"\""<<k<<"\":"<<v;}cout<<"},\n  \"pair_safe_unreachable_to_clean\":"<<un<<",\n  \"maximum_pair_safe_distance_to_clean\":"<<maxdist<<",\n  \"lambda_source_to_best_target_distribution\":{";f=1;for(auto[k,v]:source_best){if(!f)cout<<",";f=0;cout<<"\""<<k.first<<"->"<<k.second<<"\":"<<v;}cout<<"},\n  \"pair_safe_nonclean_without_immediate_lambda_descent\":"<<no_descent<<",\n  \"optimal_violated_edge_checks\":"<<optimal_violated_edge_checks<<",\n  \"minimum_targeted_clean_rotations_per_optimal_violated_edge\":"<<minimum_targeted_clean_rotations<<",\n  \"minimum_clean_rotations_from_positive_cycle\":"<<minimum_clean_rotations_from_positive<<",\n  \"untargetable_optimal_violated_edges\":"<<untargetable_optimal_edges<<",\n  \"verified\":true,\n  \"asymptotic_seed_theorem_proved\":false\n}\n";
}

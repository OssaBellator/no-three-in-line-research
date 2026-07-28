#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;
struct Point{int x,y;};
long long cross(Point a,Point b,Point c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);} 
array<Point,4> orbit(int m,int s,int t,int e){int n=2*m;auto J=[n](int x){return n-1-x;};Point q0{s,e?J(t):t},q1{J(s),e?t:J(t)};return {q0,q1,Point{J(q0.y),q0.x},Point{J(q1.y),q1.x}};}
bool pair_bad(int m,int sa,int ta,int ea,int sb,int tb,int eb){auto a=orbit(m,sa,ta,ea),b=orbit(m,sb,tb,eb);array<Point,8>p{};for(int i=0;i<4;++i){p[i]=a[i];p[i+4]=b[i];}for(int i=0;i<8;++i)for(int j=i+1;j<8;++j)for(int k=j+1;k<8;++k)if(cross(p[i],p[j],p[k])==0)return true;return false;}
bool triple_bad_raw(int m,int a,int ta,int ea,int b,int tb,int eb,int c,int tc,int ec){auto A=orbit(m,a,ta,ea),B=orbit(m,b,tb,eb),C=orbit(m,c,tc,ec);for(auto x:A)for(auto y:B)for(auto z:C)if(cross(x,y,z)==0)return true;return false;}
struct Geometry{int m;vector<int8_t>rel;vector<uint8_t>tb;size_t six;explicit Geometry(int M):m(M),rel((size_t)m*m*m*m,0),tb((size_t)m*m*m*m*m*m*8,0),six((size_t)m*m*m*m*m*m){for(int a=0;a<m;++a)for(int ta=0;ta<m;++ta){if(ta==a)continue;for(int b=a+1;b<m;++b)for(int tbb=0;tbb<m;++tbb){if(tbb==b||tbb==ta)continue;bool eq=pair_bad(m,a,ta,0,b,tbb,0),un=pair_bad(m,a,ta,0,b,tbb,1);rel[i4(a,ta,b,tbb)]=eq&&un?3:eq?2:un?1:0;}}
for(int a=0;a<m;++a)for(int ta=0;ta<m;++ta){if(ta==a)continue;for(int b=a+1;b<m;++b)for(int tbb=0;tbb<m;++tbb){if(tbb==b||tbb==ta)continue;for(int c=b+1;c<m;++c)for(int tcc=0;tcc<m;++tcc){if(tcc==c||tcc==ta||tcc==tbb)continue;size_t id=i6(a,ta,b,tbb,c,tcc);for(int mask=0;mask<8;++mask)tb[id*8+mask]=triple_bad_raw(m,a,ta,mask&1,b,tbb,(mask>>1)&1,c,tcc,(mask>>2)&1);}}}}
size_t i4(int a,int ta,int b,int tbb)const{return ((size_t(a)*m+ta)*m+b)*m+tbb;}size_t i6(int a,int ta,int b,int tbb,int c,int tcc)const{return (((((size_t(a)*m+ta)*m+b)*m+tbb)*m+c)*m+tcc);}int relation(int a,int ta,int b,int tbb)const{return rel[i4(a,ta,b,tbb)];}bool triple_bad(int a,int ta,int ea,int b,int tbb,int eb,int c,int tcc,int ec)const{return tb[i6(a,ta,b,tbb,c,tcc)*8+ea+2*eb+4*ec];}};
uint64_t encode(const vector<int>&r){uint64_t x=0;for(int t:r)x=(x<<4)|t;return x;}vector<int> switched(const vector<int>&r,array<int,3>s){array<int,3>cyc{};int f=0,cur=min({s[0],s[1],s[2]});for(int k=0;k<(int)r.size();++k){if(cur==s[0]||cur==s[1]||cur==s[2])cyc[f++]=cur;cur=r[cur];}auto o=r;o[cyc[0]]=r[cyc[1]];o[cyc[1]]=r[cyc[2]];o[cyc[2]]=r[cyc[0]];return o;}
struct Flaw{array<int,3>s,t,e;bool operator<(const Flaw&o)const{return tie(s,t,e)<tie(o.s,o.t,o.e);}};
struct Dinic{struct E{int to,rev;long long cap;};int n;vector<vector<E>>g;vector<int>lv,it;Dinic(int N):n(N),g(N),lv(N),it(N){}void add(int s,int t,long long c){E a{t,(int)g[t].size(),c},b{s,(int)g[s].size(),0};g[s].push_back(a);g[t].push_back(b);}bool bfs(int s,int t){fill(lv.begin(),lv.end(),-1);queue<int>q;lv[s]=0;q.push(s);while(!q.empty()){int v=q.front();q.pop();for(auto&e:g[v])if(e.cap&&lv[e.to]<0)lv[e.to]=lv[v]+1,q.push(e.to);}return lv[t]>=0;}long long dfs(int v,int t,long long f){if(v==t)return f;for(int&i=it[v];i<(int)g[v].size();++i){E&e=g[v][i];if(e.cap&&lv[e.to]==lv[v]+1){long long z=dfs(e.to,t,min(f,e.cap));if(z){e.cap-=z;g[e.to][e.rev].cap+=z;return z;}}}return 0;}long long flow(int s,int t){long long ans=0,f;while(bfs(s,t)){fill(it.begin(),it.end(),0);while((f=dfs(s,t,(long long)4e18)))ans+=f;}return ans;}vector<char>reach(int s){vector<char>v(n);queue<int>q;v[s]=1;q.push(s);while(!q.empty()){int x=q.front();q.pop();for(auto&e:g[x])if(e.cap&&!v[e.to])v[e.to]=1,q.push(e.to);}return v;}};
struct RatioResult{long long p=0,q=1;int subset=0,iterations=0;vector<int> selected;};
RatioResult optimum_ratio(const vector<int>&w,const vector<vector<int>>&nbr,const vector<int>&targets,const vector<int>&cap){long long p=0,q=1;int bestSubset=0,iterations=0;vector<int> bestSelected;for(;;){++iterations;int L=w.size(),R=targets.size(),S=L+R,T=S+1;Dinic D(T+1);long long pos=0,neg=0;for(int i=0;i<L;++i){long long c=q*w[i];pos+=c;D.add(S,i,c);}for(int j=0;j<R;++j){long long c=p*cap[j];neg+=c;D.add(L+j,T,c);}long long INF=min((long long)4e18,pos+neg+1);for(int i=0;i<L;++i)for(int j:nbr[i])D.add(i,L+j,INF);long long cut=D.flow(S,T);long long gain=pos-cut;if(gain<=0)break;auto seen=D.reach(S);long long W=0,V=0;int sub=0;vector<char>used(R);for(int i=0;i<L;++i)if(seen[i]){W+=w[i];++sub;for(int j:nbr[i])used[j]=1;}for(int j=0;j<R;++j)if(used[j])V+=cap[j];long long gg=gcd(W,V);p=W/gg;q=V/gg;bestSubset=sub;bestSelected.clear();for(int i=0;i<L;++i)if(seen[i])bestSelected.push_back(i);if(iterations>100){cerr<<"dinkelbach loop\n";exit(9);}}return {p,q,bestSubset,iterations,bestSelected};}

struct CaseResult{long long clean=0,flaws=0,proper=0;long long worstP=0,worstQ=1,worstGlobalP=0,worstGlobalQ=1,worstFlawGlobalP=0,worstFlawGlobalQ=1;int worstSources=0,worstSubset=0,maxIterations=0,maxSourceCycles=0;long double maxPenalty=1;long long maxPenaltyNum=1,maxPenaltyDen=1;Flaw worstFlaw{},penaltyFlaw{};vector<int>worstSelectedWeights;};
CaseResult run(int m){Geometry geom(m);vector<vector<int>>cycles;vector<int>tail(m-1);iota(tail.begin(),tail.end(),1);do{vector<int>ord(m),r(m);ord[0]=0;for(int i=1;i<m;++i)ord[i]=tail[i-1];for(int i=0;i<m;++i)r[ord[i]]=ord[(i+1)%m];cycles.push_back(move(r));}while(next_permutation(tail.begin(),tail.end()));unordered_map<uint64_t,int>idx;idx.reserve(cycles.size()*2);for(int i=0;i<(int)cycles.size();++i)idx[encode(cycles[i])]=i;vector<array<int,3>>triples;for(int a=0;a<m;++a)for(int b=a+1;b<m;++b)for(int c=b+1;c<m;++c)triples.push_back({a,b,c});
 vector<vector<int>>clean(cycles.size());long long totalClean=0;for(int ci=0;ci<(int)cycles.size();++ci){vector<tuple<int,int,int>>edges;bool imp=false;for(int a=0;a<m&&!imp;++a)for(int b=a+1;b<m;++b){int v=geom.relation(a,cycles[ci][a],b,cycles[ci][b]);if(v==3){imp=true;break;}if(v)edges.push_back({a,b,v==1?0:1});}if(imp)continue;for(int e=0;e<(1<<m);++e){bool ok=true;for(auto [a,b,x]:edges)if(((((e>>a)&1)^((e>>b)&1))!=x)){ok=false;break;}if(ok)clean[ci].push_back(e);}totalClean+=clean[ci].size();}
 set<Flaw>flaws;for(int ci=0;ci<(int)cycles.size();++ci)for(int e:clean[ci])for(auto S:triples)if(geom.triple_bad(S[0],cycles[ci][S[0]],(e>>S[0])&1,S[1],cycles[ci][S[1]],(e>>S[1])&1,S[2],cycles[ci][S[2]],(e>>S[2])&1)){Flaw A;A.s=S;for(int k=0;k<3;++k){A.t[k]=cycles[ci][S[k]];A.e[k]=(e>>S[k])&1;}flaws.insert(A);}
 CaseResult out;out.clean=totalClean;out.flaws=flaws.size();
 for(auto&A:flaws){vector<int>X,w;for(int ci=0;ci<(int)cycles.size();++ci){bool contains=true;for(int k=0;k<3;++k)if(cycles[ci][A.s[k]]!=A.t[k])contains=false;if(!contains||clean[ci].empty())continue;int cnt=0;for(int e:clean[ci]){bool same=true;for(int k=0;k<3;++k)if(((e>>A.s[k])&1)!=A.e[k])same=false;cnt+=same;}if(cnt){X.push_back(ci);w.push_back(cnt);}}
  out.maxSourceCycles=max(out.maxSourceCycles,(int)X.size());set<int>allT;vector<set<int>>nset(X.size());for(int i=0;i<(int)X.size();++i)for(auto T:triples){bool hit=false;for(int x:T)for(int y:A.s)hit|=x==y;if(!hit)continue;int eta=idx.at(encode(switched(cycles[X[i]],T)));if(!clean[eta].empty())nset[i].insert(eta),allT.insert(eta);}vector<int>targets(allT.begin(),allT.end()),caps;unordered_map<int,int>pos;for(int j=0;j<(int)targets.size();++j){pos[targets[j]]=j;caps.push_back(clean[targets[j]].size());}vector<vector<int>>nbr(X.size());for(int i=0;i<(int)X.size();++i)for(int t:nset[i])nbr[i].push_back(pos[t]);
  auto rr=optimum_ratio(w,nbr,targets,caps);out.maxIterations=max(out.maxIterations,rr.iterations);long long allW=accumulate(w.begin(),w.end(),0LL),allV=accumulate(caps.begin(),caps.end(),0LL);long long gg=gcd(allW,allV),gp=allW/gg,gq=allV/gg;if(rr.p*gq>gp*rr.q){out.proper++;long long pn=rr.p*gq,pd=rr.q*gp,pg=gcd(pn,pd);pn/=pg;pd/=pg;if((long double)pn/pd>out.maxPenalty){out.maxPenalty=(long double)pn/pd;out.maxPenaltyNum=pn;out.maxPenaltyDen=pd;out.penaltyFlaw=A;}}if(rr.p*out.worstQ>out.worstP*rr.q){out.worstP=rr.p;out.worstQ=rr.q;out.worstSources=X.size();out.worstSubset=rr.subset;out.worstFlawGlobalP=gp;out.worstFlawGlobalQ=gq;out.worstFlaw=A;out.worstSelectedWeights.clear();for(int ii:rr.selected)out.worstSelectedWeights.push_back(w[ii]);}if(gp*out.worstGlobalQ>out.worstGlobalP*gq){out.worstGlobalP=gp;out.worstGlobalQ=gq;}
 }
 return out;}
struct ExpectedCase {
 long long clean,flaws,proper,worstP,worstQ,worstGlobalP,worstGlobalQ,worstFlawGlobalP,worstFlawGlobalQ,maxPenaltyNum,maxPenaltyDen;
 int maxX,worstSources,worstSubset,maxIterations;
 array<int,3> ws,wt,we;
 vector<int> weights;
};
const array<ExpectedCase,5> expected={{
 {80,52,0,1,24,1,24,1,24,1,1,1,1,1,2,{0,1,2},{1,3,0},{0,1,1},{2}},
 {376,368,0,1,37,1,37,1,37,1,1,1,1,1,2,{0,1,2},{3,2,4},{0,0,0},{4}},
 {3576,1692,884,4,215,4,215,4,215,964,665,2,2,2,3,{0,3,4},{1,5,2},{0,0,0},{8,8}},
 {36736,5100,4864,12,931,12,931,12,931,724,427,6,6,6,5,{0,3,5},{5,1,3},{0,1,0},{16,16,16,16,16,16}},
 {404080,12048,11952,1,93,265,26714,8,901,10338,4891,24,15,2,6,{3,5,6},{4,6,7},{0,0,0},{32,32}}
}};
void print_array(const array<int,3>&a){cout<<"["<<a[0]<<","<<a[1]<<","<<a[2]<<"]";}
void print_vector(const vector<int>&a){cout<<"[";for(int i=0;i<(int)a.size();++i){if(i)cout<<",";cout<<a[i];}cout<<"]";}
int main(){
 cout<<"{\n  \"cases\": [\n";
 for(int m=4;m<=8;++m){auto r=run(m);const auto&e=expected[m-4];bool ok=r.clean==e.clean&&r.flaws==e.flaws&&r.proper==e.proper&&r.worstP==e.worstP&&r.worstQ==e.worstQ&&r.worstGlobalP==e.worstGlobalP&&r.worstGlobalQ==e.worstGlobalQ&&r.worstFlawGlobalP==e.worstFlawGlobalP&&r.worstFlawGlobalQ==e.worstFlawGlobalQ&&r.maxPenaltyNum==e.maxPenaltyNum&&r.maxPenaltyDen==e.maxPenaltyDen&&r.maxSourceCycles==e.maxX&&r.worstSources==e.worstSources&&r.worstSubset==e.worstSubset&&r.maxIterations==e.maxIterations&&r.worstFlaw.s==e.ws&&r.worstFlaw.t==e.wt&&r.worstFlaw.e==e.we&&r.worstSelectedWeights==e.weights;if(!ok){cerr<<"min-cut transport ledger mismatch at m="<<m<<"\n";return 3;}
  cout<<"    {\"m\":"<<m<<",\"clean_signed_states\":"<<r.clean<<",\"atomic_signed_assignment_flaws\":"<<r.flaws<<",\"maximum_source_cycles\":"<<r.maxSourceCycles<<",\"optimal_charge_numerator\":"<<r.worstP<<",\"optimal_charge_denominator\":"<<r.worstQ<<",\"m_cubed_scaled_charge\":"<<(double)r.worstP*m*m*m/r.worstQ<<",\"worst_flaw_source_cycles\":"<<r.worstSources<<",\"worst_hall_subset_size\":"<<r.worstSubset<<",\"worst_flaw_global_numerator\":"<<r.worstFlawGlobalP<<",\"worst_flaw_global_denominator\":"<<r.worstFlawGlobalQ<<",\"proper_hall_bottleneck_flaws\":"<<r.proper<<",\"maximum_label_merging_penalty_numerator\":"<<r.maxPenaltyNum<<",\"maximum_label_merging_penalty_denominator\":"<<r.maxPenaltyDen<<",\"maximum_dinkelbach_iterations\":"<<r.maxIterations<<",\"worst_flaw_sources\":";print_array(r.worstFlaw.s);cout<<",\"worst_flaw_targets\":";print_array(r.worstFlaw.t);cout<<",\"worst_flaw_orientations\":";print_array(r.worstFlaw.e);cout<<",\"worst_cut_source_weights\":";print_vector(r.worstSelectedWeights);cout<<"}"<<(m<8?",":"")<<"\n";
 }
 cout<<"  ],\n  \"weighted_maximum_closure_mincut_used\": true,\n  \"dinkelbach_exact_rational_iteration_used\": true,\n  \"m4_through_m7_exhaustive_ledgers_reproduced\": true,\n  \"asymptotic_expansion_proved\": false\n}\n";
}

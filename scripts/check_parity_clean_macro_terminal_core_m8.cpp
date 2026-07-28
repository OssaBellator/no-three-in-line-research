#include <algorithm>
#include <array>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;
struct Point{int x,y;};
long long cross(Point a,Point b,Point c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
array<Point,4> orbit(int m,int s,int t,int e){int n=2*m;auto r=[n](int x){return n-1-x;};Point q0{s,e?r(t):t},q1{r(s),e?t:r(t)};return {q0,q1,Point{r(q0.y),q0.x},Point{r(q1.y),q1.x}};}
bool pair_bad(int m,int sa,int ta,int ea,int sb,int tb,int eb){auto a=orbit(m,sa,ta,ea),b=orbit(m,sb,tb,eb);array<Point,8>p{};for(int i=0;i<4;i++){p[i]=a[i];p[i+4]=b[i];}for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)if(cross(p[i],p[j],p[k])==0)return true;return false;}
int triple_count(int m,int a,int ta,int ea,int b,int tb,int eb,int c,int tc,int ec){auto A=orbit(m,a,ta,ea),B=orbit(m,b,tb,eb),C=orbit(m,c,tc,ec);int z=0;for(auto x:A)for(auto y:B)for(auto w:C)z+=cross(x,y,w)==0;return z;}
struct Relations{int m;vector<int8_t>d;explicit Relations(int M):m(M),d(m*m*m*m,0){for(int a=0;a<m;a++)for(int ta=0;ta<m;ta++){if(ta==a)continue;for(int b=a+1;b<m;b++)for(int tb=0;tb<m;tb++){if(tb==b||tb==ta)continue;bool eq=pair_bad(m,a,ta,0,b,tb,0),un=pair_bad(m,a,ta,0,b,tb,1);d[index(a,ta,b,tb)]=eq&&un?3:eq?2:un?1:0;}}}int index(int a,int ta,int b,int tb)const{return ((a*m+ta)*m+b)*m+tb;}int get(int a,int ta,int b,int tb)const{return d[index(a,ta,b,tb)];}};
uint64_t encode(const vector<int>&r){uint64_t x=0;for(int t:r)x=(x<<4)|t;return x;}
vector<int> switched(const vector<int>&r,array<int,3>s){array<int,3>cyclic{};int found=0,current=min({s[0],s[1],s[2]});for(int k=0;k<(int)r.size();k++){if(current==s[0]||current==s[1]||current==s[2])cyclic[found++]=current;current=r[current];}auto out=r;out[cyclic[0]]=r[cyclic[1]];out[cyclic[1]]=r[cyclic[2]];out[cyclic[2]]=r[cyclic[0]];return out;}
struct State{uint64_t flaws=0;int atomic=0,supports=0;};
int main(){
 const int m=8;Relations relation(m);vector<vector<int>>cycles;vector<int>tail(m-1);iota(tail.begin(),tail.end(),1);do{vector<int>order(m),rho(m);order[0]=0;for(int i=1;i<m;i++)order[i]=tail[i-1];for(int i=0;i<m;i++)rho[order[i]]=order[(i+1)%m];cycles.push_back(move(rho));}while(next_permutation(tail.begin(),tail.end()));
 unordered_map<uint64_t,int>index;index.reserve(cycles.size()*2);for(int i=0;i<(int)cycles.size();i++)index[encode(cycles[i])]=i;vector<array<int,3>>triples;for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)triples.push_back({a,b,c});
 vector<vector<int>>clean(cycles.size());vector<int>stateCycle,stateOrientation;vector<vector<int>>stateId(cycles.size(),vector<int>(1<<m,-1));
 for(int ci=0;ci<(int)cycles.size();ci++){bool impossible=false;vector<array<int,3>>edges;for(int a=0;a<m;a++)for(int b=a+1;b<m;b++){int v=relation.get(a,cycles[ci][a],b,cycles[ci][b]);if(v==3)impossible=true;else if(v)edges.push_back({a,b,v==1?0:1});}if(impossible)continue;for(int orientation=0;orientation<(1<<m);orientation++){bool ok=true;for(auto e:edges)if(((((orientation>>e[0])&1)^((orientation>>e[1])&1))!=e[2])){ok=false;break;}if(ok){int id=stateCycle.size();clean[ci].push_back(orientation);stateId[ci][orientation]=id;stateCycle.push_back(ci);stateOrientation.push_back(orientation);}}}
 vector<State>data(stateCycle.size());vector<int>valid;for(int id=0;id<(int)stateCycle.size();id++){int ci=stateCycle[id],orientation=stateOrientation[id];uint64_t mask=0;int atomic=0;for(int ti=0;ti<(int)triples.size();ti++){auto t=triples[ti];int q=triple_count(m,t[0],cycles[ci][t[0]],(orientation>>t[0])&1,t[1],cycles[ci][t[1]],(orientation>>t[1])&1,t[2],cycles[ci][t[2]],(orientation>>t[2])&1);if(q){mask|=1ULL<<ti;atomic+=q;}}data[id]={mask,atomic,__builtin_popcountll(mask)};if(!mask)valid.push_back(id);}
 vector<uint64_t>meeting(triples.size());for(int ti=0;ti<(int)triples.size();ti++)for(int si=0;si<(int)triples.size();si++){bool hit=false;for(int x:triples[ti])for(int y:triples[si])if(x==y)hit=true;if(hit)meeting[ti]|=1ULL<<si;}
 vector<int>distance(stateCycle.size(),-1),cycleMin(cycles.size(),-1);deque<int>queue;for(int id:valid){distance[id]=0;int ci=stateCycle[id];if(cycleMin[ci]<0){cycleMin[ci]=0;queue.push_back(ci);}}
 while(!queue.empty()){int eta=queue.front();queue.pop_front();int next=cycleMin[eta]+1;for(int ti=0;ti<(int)triples.size();ti++){int rho=index.at(encode(switched(cycles[eta],triples[ti])));bool added=false;for(int orientation:clean[rho]){int id=stateId[rho][orientation];if(distance[id]<0&&(data[id].flaws&meeting[ti])){distance[id]=next;added=true;}}if(added&&cycleMin[rho]<0){cycleMin[rho]=next;queue.push_back(rho);}}}
 map<int,long long>distHist,supportHist,coverHist;long long unreached=0,commonOwner=0;int maxSupport=0,maxAtomic=0;for(int d:distance){if(d<0)unreached++;else distHist[d]++;}
 for(int id=0;id<(int)distance.size();id++)if(distance[id]==3){uint64_t fm=data[id].flaws;supportHist[data[id].supports]++;maxSupport=max(maxSupport,data[id].supports);maxAtomic=max(maxAtomic,data[id].atomic);int intersection=(1<<m)-1;for(int ti=0;ti<(int)triples.size();ti++)if((fm>>ti)&1){int mask=0;for(int x:triples[ti])mask|=1<<x;intersection&=mask;}int tau=0;if(intersection){tau=1;commonOwner++;}else{tau=m;for(int mask=1;mask<(1<<m);mask++){int size=__builtin_popcount((unsigned)mask);if(size>=tau)continue;bool cover=true;for(int ti=0;ti<(int)triples.size();ti++)if((fm>>ti)&1){bool hit=false;for(int x:triples[ti])if((mask>>x)&1)hit=true;if(!hit){cover=false;break;}}if(cover)tau=size;}}coverHist[tau]++;}
 const map<int,long long>expectedDistance={{0,28},{1,66844},{2,303576},{3,33632}};
 const map<int,long long>expectedSupport={{1,36},{2,188},{3,568},{4,1272},{5,3000},{6,3672},{7,4232},{8,4680},{9,4104},{10,3056},{11,2204},{12,1528},{13,1272},{14,1092},{15,736},{16,608},{17,448},{18,240},{19,128},{20,16},{21,48},{22,52},{23,48},{24,36},{25,56},{26,40},{27,16},{35,88},{36,88},{37,72},{38,8}};
 const map<int,long long>expectedCover={{1,528},{2,11908},{3,19508},{4,1688}};
 bool verified=stateCycle.size()==404080&&valid.size()==28&&unreached==0&&distHist==expectedDistance&&maxSupport==38&&maxAtomic==160&&commonOwner==528&&supportHist==expectedSupport&&coverHist==expectedCover;if(!verified){cerr<<"verification mismatch\n";return 1;}
 cout<<"{\n  \"m\": 8,\n  \"clean_signed_states\": "<<stateCycle.size()<<",\n  \"valid_states\": "<<valid.size()<<",\n  \"unreached_states\": "<<unreached<<",\n  \"distance_distribution\": {\"0\": 28, \"1\": 66844, \"2\": 303576, \"3\": 33632},\n  \"distance_three_maximum_supports\": "<<maxSupport<<",\n  \"distance_three_maximum_atomic_triples\": "<<maxAtomic<<",\n  \"distance_three_states_with_common_owner\": "<<commonOwner<<",\n  \"verified\": true,\n  \"asymptotic_theorem_proved\": false\n}\n";
}

#include <algorithm>
#include <array>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
struct P{int x,y;}; inline long long cr(P a,P b,P c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
array<P,4> blk(int m,int s,int t,int e){int n=2*m;auto r=[n](int x){return n-1-x;};P q0{s,e?r(t):t},q1{r(s),e?t:r(t)};return {q0,q1,P{r(q0.y),q0.x},P{r(q1.y),q1.x}};}
bool pairbad(int m,int sa,int ta,int ea,int sb,int tb,int eb){auto a=blk(m,sa,ta,ea),b=blk(m,sb,tb,eb);array<P,8>p{};for(int i=0;i<4;i++){p[i]=a[i];p[i+4]=b[i];}for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)for(int k=j+1;k<8;k++)if(cr(p[i],p[j],p[k])==0)return true;return false;}
int triplecount(int m,int a,int ta,int ea,int b,int tb,int eb,int c,int tc,int ec){auto A=blk(m,a,ta,ea),B=blk(m,b,tb,eb),C=blk(m,c,tc,ec);int q=0;for(auto x:A)for(auto y:B)for(auto z:C)q+=cr(x,y,z)==0;return q;}
struct Rel{int m;vector<int8_t>d;Rel(int M):m(M),d(m*m*m*m,0){for(int a=0;a<m;a++)for(int ta=0;ta<m;ta++){if(ta==a)continue;for(int b=a+1;b<m;b++)for(int tb=0;tb<m;tb++){if(tb==b||tb==ta)continue;bool e=pairbad(m,a,ta,0,b,tb,0),u=pairbad(m,a,ta,0,b,tb,1);d[idx(a,ta,b,tb)]=e&&u?3:e?2:u?1:0;}}}int idx(int a,int ta,int b,int tb)const{return ((a*m+ta)*m+b)*m+tb;}int get(int a,int ta,int b,int tb)const{return d[idx(a,ta,b,tb)];}};
uint64_t enc(const array<uint8_t,9>&r,int m){uint64_t x=0;for(int i=0;i<m;i++)x=(x<<4)|r[i];return x;}
array<uint8_t,9> sw(const array<uint8_t,9>&r,int m,array<int,3>s){array<int,3>c{};int f=0,u=min({s[0],s[1],s[2]});for(int k=0;k<m;k++){if(u==s[0]||u==s[1]||u==s[2])c[f++]=u;u=r[u];}auto o=r;o[c[0]]=r[c[1]];o[c[1]]=r[c[2]];o[c[2]]=r[c[0]];return o;}
int main(){const int m=9;Rel R(m);vector<array<uint8_t,9>>cy;vector<int>tail(m-1);iota(tail.begin(),tail.end(),1);do{array<uint8_t,9>ord{},r{};ord[0]=0;for(int i=1;i<m;i++)ord[i]=tail[i-1];for(int i=0;i<m;i++)r[ord[i]]=ord[(i+1)%m];cy.push_back(r);}while(next_permutation(tail.begin(),tail.end()));unordered_map<uint64_t,int>ix;ix.reserve(cy.size()*2);for(int i=0;i<(int)cy.size();i++)ix[enc(cy[i],m)]=i;vector<array<int,3>>tr;for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)tr.push_back({a,b,c});const int K=tr.size();
 vector<array<int,84>>nei(cy.size());for(int i=0;i<(int)cy.size();i++)for(int t=0;t<K;t++)nei[i][t]=ix.at(enc(sw(cy[i],m,tr[t]),m));
 vector<uint64_t>meetLo(K),meetHi(K);for(int t=0;t<K;t++)for(int s=0;s<K;s++){bool hit=false;for(int x:tr[t])for(int y:tr[s])if(x==y)hit=true;if(hit){if(s<64)meetLo[t]|=1ULL<<s;else meetHi[t]|=1ULL<<(s-64);}}
 vector<int>off(cy.size()+1);vector<uint16_t>oris;oris.reserve(7000000);vector<uint64_t>flo,fhi;vector<uint16_t>atom;flo.reserve(7000000);fhi.reserve(7000000);atom.reserve(7000000);long long valid=0;int satcycles=0;
 for(int ci=0;ci<(int)cy.size();ci++){off[ci]=oris.size();vector<array<int,3>>edges;bool imp=false;for(int a=0;a<m;a++)for(int b=a+1;b<m;b++){int v=R.get(a,cy[ci][a],b,cy[ci][b]);if(v==3)imp=true;else if(v)edges.push_back({a,b,v==1?0:1});}if(imp)continue;array<uint8_t,84>badpat{};array<array<uint8_t,8>,84>ac{};for(int ti=0;ti<K;ti++){auto T=tr[ti];uint8_t mask=0;for(int p=0;p<8;p++){int q=triplecount(m,T[0],cy[ci][T[0]],(p>>0)&1,T[1],cy[ci][T[1]],(p>>1)&1,T[2],cy[ci][T[2]],(p>>2)&1);ac[ti][p]=q;if(q)mask|=1u<<p;}badpat[ti]=mask;}int before=oris.size();for(int o=0;o<(1<<m);o++){bool ok=true;for(auto e:edges)if(((((o>>e[0])&1)^((o>>e[1])&1))!=e[2])){ok=false;break;}if(!ok)continue;uint64_t lo=0,hi=0;int at=0;for(int ti=0;ti<K;ti++){auto T=tr[ti];int p=((o>>T[0])&1)|(((o>>T[1])&1)<<1)|(((o>>T[2])&1)<<2);at+=ac[ti][p];if((badpat[ti]>>p)&1){if(ti<64)lo|=1ULL<<ti;else hi|=1ULL<<(ti-64);}}oris.push_back(o);flo.push_back(lo);fhi.push_back(hi);atom.push_back(at);if(!(lo|hi))valid++;}if((int)oris.size()>before)satcycles++;}
 off[cy.size()]=oris.size();vector<int8_t>dist(oris.size(),-1),cmin(cy.size(),-1);deque<int>q;for(int ci=0;ci<(int)cy.size();ci++)for(int id=off[ci];id<off[ci+1];id++)if(!(flo[id]|fhi[id])){dist[id]=0;if(cmin[ci]<0){cmin[ci]=0;q.push_back(ci);}}
 while(!q.empty()){int eta=q.front();q.pop_front();int nd=cmin[eta]+1;for(int t=0;t<K;t++){int rho=nei[eta][t];bool any=false;for(int id=off[rho];id<off[rho+1];id++)if(dist[id]<0&&((flo[id]&meetLo[t])||(fhi[id]&meetHi[t]))){dist[id]=nd;any=true;}if(any&&cmin[rho]<0){cmin[rho]=nd;q.push_back(rho);}}}
 vector<int>minSup(cy.size(),999),minAtom(cy.size(),9999);for(int ci=0;ci<(int)cy.size();ci++)for(int id=off[ci];id<off[ci+1];id++){int sp=__builtin_popcountll(flo[id])+__builtin_popcountll(fhi[id]);minSup[ci]=min(minSup[ci],sp);minAtom[ci]=min(minAtom[ci],(int)atom[id]);}
 vector<uint16_t> peakA(oris.size(),65535),peakS(oris.size(),65535); vector<int> parentA(oris.size(),-1), parentAT(oris.size(),-1);
 for(int id=0;id<(int)oris.size();id++)if(dist[id]==0){peakA[id]=atom[id];peakS[id]=0;}
 for(int d=1;d<=4;d++){vector<uint16_t> cpa(cy.size(),65535),cps(cy.size(),65535);vector<int> cpaid(cy.size(),-1);for(int ci=0;ci<(int)cy.size();ci++)for(int id=off[ci];id<off[ci+1];id++)if(dist[id]==d-1){if(peakA[id]<cpa[ci]){cpa[ci]=peakA[id];cpaid[ci]=id;}cps[ci]=min(cps[ci],peakS[id]);}
  for(int ci=0;ci<(int)cy.size();ci++)for(int id=off[ci];id<off[ci+1];id++)if(dist[id]==d){int sp=__builtin_popcountll(flo[id])+__builtin_popcountll(fhi[id]);for(int t=0;t<K;t++)if((flo[id]&meetLo[t])||(fhi[id]&meetHi[t])){int eta=nei[ci][t];if(cpa[eta]!=65535){uint16_t ca=max<uint16_t>(atom[id],cpa[eta]);if(ca<peakA[id]){peakA[id]=ca;parentA[id]=cpaid[eta];parentAT[id]=t;}}if(cps[eta]!=65535)peakS[id]=min<uint16_t>(peakS[id],max<uint16_t>(sp,cps[eta]));}}
 }
 vector<int>oriToId(cy.size()*(1<<m),-1);for(int ci=0;ci<(int)cy.size();ci++)for(int id=off[ci];id<off[ci+1];id++)oriToId[ci*(1<<m)+oris[id]]=id;
 vector<int>hardIds;for(int ci=0;ci<(int)cy.size();ci++)for(int id=off[ci];id<off[ci+1];id++){if(dist[id]!=4)continue;int sp=__builtin_popcountll(flo[id])+__builtin_popcountll(fhi[id]);if(sp!=1||atom[id]!=4)continue;bool sd=false,ad=false;for(int t=0;t<K;t++)if((flo[id]&meetLo[t])||(fhi[id]&meetHi[t])){int eta=nei[ci][t];if(minSup[eta]<sp)sd=true;if(minAtom[eta]<(int)atom[id])ad=true;}if(!sd&&!ad)hardIds.push_back(id);}
 struct Witness{array<int,9> rho;int ori,comp;array<int,3> support;array<array<int,3>,4> word;array<int,5> atomic,support_count;};
 vector<Witness>witnesses;set<int>hardCycles;int complementPairs=0;
 for(int id:hardIds){int ci=upper_bound(off.begin(),off.end(),id)-off.begin()-1;hardCycles.insert(ci);if(oris[id]>(oris[id]^511))continue;int comp=oriToId[ci*(1<<m)+(oris[id]^511)];if(comp<0||find(hardIds.begin(),hardIds.end(),comp)==hardIds.end()){cerr<<"missing complement\n";return 2;}complementPairs++;Witness w{};for(int i=0;i<m;i++)w.rho[i]=cy[ci][i];w.ori=oris[id];w.comp=oris[comp];for(int ti=0;ti<K;ti++){bool on=ti<64?((flo[id]>>ti)&1):((fhi[id]>>(ti-64))&1);if(on)w.support=tr[ti];}w.atomic[0]=atom[id];w.support_count[0]=1;int cur=id;for(int d=0;d<4;d++){int ti=parentAT[cur],nid=parentA[cur];if(ti<0||nid<0){cerr<<"missing parent\n";return 3;}w.word[d]=tr[ti];w.atomic[d+1]=atom[nid];w.support_count[d+1]=__builtin_popcountll(flo[nid])+__builtin_popcountll(fhi[nid]);cur=nid;}witnesses.push_back(w);}
 const array<Witness,4> expected={{
  {{{3,6,7,4,2,8,5,1,0}},136,375,{0,1,5},{{{0,1,2},{3,5,8},{0,2,6},{1,2,3}}},{4,8,8,8,0},{1,2,2,2,0}},
  {{{4,3,7,6,1,8,5,0,2}},59,452,{3,4,5},{{{0,2,3},{0,2,5},{1,6,7},{3,4,5}}},{4,8,8,8,0},{1,2,2,2,0}},
  {{{7,4,8,1,0,6,3,2,5}},165,346,{1,6,8},{{{4,6,7},{4,6,8},{0,3,5},{1,4,7}}},{4,8,8,8,0},{1,2,2,2,0}},
  {{{8,7,4,0,3,6,1,2,5}},18,493,{3,6,8},{{{0,6,8},{3,5,6},{3,5,7},{3,4,5}}},{4,4,8,8,0},{1,1,2,2,0}}
 }};
 auto equalW=[](const Witness&a,const Witness&b){return a.rho==b.rho&&a.ori==b.ori&&a.comp==b.comp&&a.support==b.support&&a.word==b.word&&a.atomic==b.atomic&&a.support_count==b.support_count;};
 bool verified=satcycles==31688&&oris.size()==6727728&&valid==8&&hardIds.size()==8&&hardCycles.size()==4&&complementPairs==4&&witnesses.size()==4;
 for(int id:hardIds)verified=verified&&dist[id]==4&&atom[id]==4&&peakA[id]==8&&peakS[id]==2;
 for(int i=0;i<4;i++)verified=verified&&equalW(witnesses[i],expected[i]);
 if(!verified){cerr<<"single-support collateral ledger mismatch\n";return 4;}
 cout<<"{\n  \"m\":9,\n  \"clean_signed_states\":"<<oris.size()<<",\n  \"valid_states\":"<<valid<<",\n  \"one_support_distance_four_states\":"<<hardIds.size()<<",\n  \"hamilton_cycles\":"<<hardCycles.size()<<",\n  \"global_sign_complement_pairs\":"<<complementPairs<<",\n  \"minimum_peak_atomic_count\":8,\n  \"minimum_peak_support_count\":2,\n  \"canonical_words\":[\n";
 for(int i=0;i<4;i++){auto&w=witnesses[i];cout<<"    {\"source_orientation_pair\":["<<w.ori<<","<<w.comp<<"],\"rho\":[";for(int j=0;j<9;j++)cout<<w.rho[j]<<(j<8?",":"");cout<<"],\"source_support\":["<<w.support[0]<<","<<w.support[1]<<","<<w.support[2]<<"],\"rotation_word\":[";for(int d=0;d<4;d++)cout<<"["<<w.word[d][0]<<","<<w.word[d][1]<<","<<w.word[d][2]<<"]"<<(d<3?",":"");cout<<"],\"atomic_sequence\":[";for(int d=0;d<5;d++)cout<<w.atomic[d]<<(d<4?",":"");cout<<"],\"support_sequence\":[";for(int d=0;d<5;d++)cout<<w.support_count[d]<<(d<4?",":"");cout<<"]}"<<(i<3?",":"")<<"\n";}
 cout<<"  ],\n  \"exact_shortest_path_barrier_verified\":true,\n  \"asymptotic_collateral_word_proved\":false\n}\n";
}

#include <bits/stdc++.h>
using namespace std;

static const int N=30, CELLS=900;
struct Move{uint8_t layer,i,j;};
struct LineKey{int a,b,c; bool operator==(LineKey const&o)const{return a==o.a&&b==o.b&&c==o.c;}};
struct KeyHash{size_t operator()(LineKey const&k)const{uint64_t x=(uint32_t)(k.a+64); x=x*1315423911u+(uint32_t)(k.b+64); x=x*2654435761u+(uint32_t)(k.c+4096); return (size_t)x;}};
vector<array<int,CELLS>> dummy;
vector<int> pairLine;
vector<vector<int>> lineCells;
vector<Move> allMoves;

LineKey key_for(int p,int q){
 int x1=p/N+1,y1=p%N+1,x2=q/N+1,y2=q%N+1;
 int a=y2-y1,b=x1-x2,c=a*x1+b*y1;
 int g=std::gcd(abs(a),abs(b)); a/=g;b/=g;c/=g;
 if(a<0 || (a==0&&b<0)){a=-a;b=-b;c=-c;}
 return {a,b,c};
}
void init_geom(){
 unordered_map<LineKey,int,KeyHash> ids; ids.reserve(500000);
 pairLine.assign(CELLS*CELLS,-1);
 for(int p=0;p<CELLS;p++)for(int q=p+1;q<CELLS;q++){
   auto k=key_for(p,q); auto it=ids.find(k); int id;
   if(it==ids.end()){id=ids.size();ids.emplace(k,id);}else id=it->second;
   pairLine[p*CELLS+q]=pairLine[q*CELLS+p]=id;
 }
 lineCells.resize(ids.size());
 for(auto const&kv:ids){auto k=kv.first;int id=kv.second;auto &v=lineCells[id];
   for(int x=1;x<=N;x++){
     if(k.b!=0){int num=k.c-k.a*x;if(num%k.b==0){int y=num/k.b;if(1<=y&&y<=N)v.push_back((x-1)*N+y-1);}}
     else if(k.a*x==k.c){for(int y=1;y<=N;y++)v.push_back((x-1)*N+y-1);break;}
   }
 }
 for(int l=0;l<2;l++)for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)allMoves.push_back({(uint8_t)l,(uint8_t)i,(uint8_t)j});
 cerr<<"lines="<<lineCells.size()<<" moves="<<allMoves.size()<<"\n";
}
inline int C2(int k){return k*(k-1)/2;} inline int C3(int k){return k*(k-1)*(k-2)/6;}
static vector<uint16_t> g_pm;
static vector<uint8_t> g_cnt;
static vector<uint32_t> g_stamp;
static uint32_t g_epoch=0;
struct Eval{
 bool selected[CELLS];
 array<uint16_t,CELLS> F;
 vector<int> touched;
 uint32_t epoch;
 int pot;
 Eval(string const&s){
   if(g_pm.empty()){g_pm.resize(lineCells.size());g_cnt.resize(lineCells.size());g_stamp.resize(lineCells.size());}
   epoch=++g_epoch; if(epoch==0){fill(g_stamp.begin(),g_stamp.end(),0);epoch=++g_epoch;}
   memset(selected,0,sizeof(selected)); int pts[60],z=0;
   for(int r=0;r<N;r++){int a=r*N+(uint8_t)s[r]-1,b=r*N+(uint8_t)s[N+r]-1;selected[a]=selected[b]=1;pts[z++]=a;pts[z++]=b;}
   touched.reserve(1800);
   for(int i=0;i<60;i++)for(int j=i+1;j<60;j++){int id=pairLine[pts[i]*CELLS+pts[j]];if(g_stamp[id]!=epoch){g_stamp[id]=epoch;g_pm[id]=1;touched.push_back(id);}else g_pm[id]++;}
   pot=0;F.fill(0);
   for(int id:touched){int m=g_pm[id],k=(1+(int)llround(sqrt(1+8.0*m)))/2;while(C2(k)<m)k++;while(C2(k)>m)k--;if(C2(k)!=m)abort();g_cnt[id]=k;pot+=C3(k);for(int p:lineCells[id]){int kk=k-(selected[p]?1:0);F[p]+=C2(kk);}}
 }
 inline int activeCount(int id)const{return g_stamp[id]==epoch?g_cnt[id]:-1;}
 inline int countLine(int id)const{int k=activeCount(id);if(k>=0)return k;for(int p:lineCells[id])if(selected[p])return 1;return 0;}
 int nextPot(string const&s,Move m)const{
   int off=m.layer?N:0; int i=m.i,j=m.j; int yi=(uint8_t)s[off+i], yj=(uint8_t)s[off+j];
   int A=i*N+yi-1,B=j*N+yj-1,C=i*N+yj-1,D=j*N+yi-1;
   int idAB=pairLine[A*CELLS+B];int kAB=activeCount(idAB);int gOld=kAB-2;
   auto q=[&](int X,int Y){int id=pairLine[X*CELLS+Y];int k=activeCount(id);return (k<0?1:k)-1;};
   bool iCAB=(pairLine[C*CELLS+A]==pairLine[C*CELLS+B]);
   bool iDAB=(pairLine[D*CELLS+A]==pairLine[D*CELLS+B]);
   int fA=F[A]-gOld, fB=F[B]-gOld;
   int fC=(int)F[C]-q(C,A)-q(C,B)+(iCAB?1:0);
   int fD=(int)F[D]-q(D,A)-q(D,B)+(iDAB?1:0);
   int idCD=pairLine[C*CELLS+D];int kCD=countLine(idCD);
   int gNew=kCD-(idCD==pairLine[C*CELLS+A]?1:0)-(idCD==pairLine[C*CELLS+B]?1:0);
   return pot - fA-fB-gOld + fC+fD+gNew;
 }
};inline bool legal(string const&s,Move m){int o=m.layer?N:0,q=m.layer?0:N;return (uint8_t)s[o+m.j]!=(uint8_t)s[q+m.i]&&(uint8_t)s[o+m.i]!=(uint8_t)s[q+m.j];}
inline string apply(string s,Move m){int o=m.layer?N:0;swap(s[o+m.i],s[o+m.j]);return s;}
int brutePot(string const&s){struct P{int x,y;};P p[60];for(int i=0;i<N;i++){p[2*i]={i+1,(uint8_t)s[i]};p[2*i+1]={i+1,(uint8_t)s[N+i]};}int v=0;for(int i=0;i<60;i++)for(int j=i+1;j<60;j++)for(int k=j+1;k<60;k++)v+=(long long)(p[j].x-p[i].x)*(p[k].y-p[i].y)==(long long)(p[j].y-p[i].y)*(p[k].x-p[i].x);return v;}
string encode(vector<int> const&r,vector<int> const&b){string s;for(int x:r)s.push_back((char)x);for(int x:b)s.push_back((char)x);return s;}
struct Rec{string s;int parent;Move mv;uint8_t p;};
struct SearchResult{bool found;vector<Move> path;vector<int> pots;string end;size_t processed,discovered;};
array<array<int,CELLS>,8>tcell;
void init_sym(){for(int g=0;g<8;g++)for(int p=0;p<CELLS;p++){int x=p/N+1,y=p%N+1,X,Y;switch(g){case 0:X=x;Y=y;break;case 1:X=y;Y=N+1-x;break;case 2:X=N+1-x;Y=N+1-y;break;case 3:X=N+1-y;Y=x;break;case 4:X=N+1-x;Y=y;break;case 5:X=x;Y=N+1-y;break;case 6:X=y;Y=x;break;default:X=N+1-y;Y=N+1-x;}tcell[g][p]=(X-1)*N+Y-1;}}
string canonical(string const&s){string best(60,char(127)),u(60,'\0');for(int g=0;g<8;g++)for(int sw=0;sw<2;sw++){fill(u.begin(),u.end(),'\0');for(int l=0;l<2;l++)for(int x=0;x<N;x++){int p=x*N+(uint8_t)s[l*N+x]-1,q=tcell[g][p],X=q/N,Y=q%N+1,L=l^sw;u[L*N+X]=(char)Y;}if(u<best)best=u;}return best;}
uint16_t encMove(Move m){return(uint16_t)(m.layer*900+m.i*30+m.j);}Move decMove(uint16_t x){Move m;m.layer=x/900;x%=900;m.i=x/30;m.j=x%30;return m;}string moveWord(Move m){return string(m.layer?"b:":"r:")+to_string((int)m.i+1)+","+to_string((int)m.j+1);}
struct DRec{char s[60],key[60];int32_t parent;uint16_t mv;uint8_t p;};static_assert(sizeof(DRec)==128);
const uint64_t MAGIC=0x4143333251554f54ULL;
uint64_t hkey(char const*k){uint64_t h=1469598103934665603ULL;for(int i=0;i<60;i++){h^=(uint8_t)k[i];h*=1099511628211ULL;}h^=h>>33;h*=0xff51afd7ed558ccdULL;h^=h>>33;return h;}
struct Index{vector<uint32_t>tab;vector<DRec>*rec;size_t used=0;Index(vector<DRec>&r):rec(&r){size_t cap=1;while(cap<r.size()*2+1024)cap<<=1;tab.assign(cap,UINT32_MAX);for(uint32_t i=0;i<r.size();i++)insertKnown(i);}void insertKnown(uint32_t i){size_t m=tab.size()-1,j=hkey((*rec)[i].key)&m;while(tab[j]!=UINT32_MAX)j=(j+1)&m;tab[j]=i;used++;}void rehash(){vector<uint32_t>old=move(tab);tab.assign(old.size()*2,UINT32_MAX);used=0;for(uint32_t i=0;i<rec->size();i++)insertKnown(i);}pair<uint32_t,bool> findOrInsert(char const*k,uint32_t newIndex){if((used+1)*10>tab.size()*7)rehash();size_t m=tab.size()-1,j=hkey(k)&m;while(true){uint32_t v=tab[j];if(v==UINT32_MAX){tab[j]=newIndex;used++;return{newIndex,true};}if(memcmp((*rec)[v].key,k,60)==0)return{v,false};j=(j+1)&m;}}};
void savecp(string path,uint64_t pos,vector<DRec>const&rec){string tmp=path+".tmp";ofstream f(tmp,ios::binary);uint64_t n=rec.size();f.write((char*)&MAGIC,8);f.write((char*)&pos,8);f.write((char*)&n,8);f.write((char*)rec.data(),n*sizeof(DRec));f.close();rename(tmp.c_str(),path.c_str());}
bool loadcp(string path,uint64_t&pos,vector<DRec>&rec){ifstream f(path,ios::binary);if(!f)return false;uint64_t magic,n;f.read((char*)&magic,8);f.read((char*)&pos,8);f.read((char*)&n,8);assert(magic==MAGIC);rec.resize(n);f.read((char*)rec.data(),n*sizeof(DRec));return true;}
void writeResult(string path,vector<DRec>const&rec,int end,uint64_t processed){vector<int>ids;for(int x=end;x>=0;x=rec[x].parent)ids.push_back(x);reverse(ids.begin(),ids.end());ofstream f(path);f<<"{\n  \"processed_quotient_states_before_first_lower\": "<<processed<<",\n  \"discovered_quotient_states_before_first_lower\": "<<rec.size()<<",\n  \"moves\": [";for(size_t k=1;k<ids.size();k++){if(k>1)f<<",";f<<"\""<<moveWord(decMove(rec[ids[k]].mv))<<"\"";}f<<"],\n  \"potentials\": [";for(size_t k=0;k<ids.size();k++){if(k)f<<",";f<<(int)rec[ids[k]].p;}f<<"],\n  \"end_red\": [";for(int i=0;i<N;i++){if(i)f<<",";f<<(int)(uint8_t)rec[end].s[i];}f<<"],\n  \"end_blue\": [";for(int i=0;i<N;i++){if(i)f<<",";f<<(int)(uint8_t)rec[end].s[N+i];}f<<"]\n}\n";}
int main(int argc,char**argv){ios::sync_with_stdio(false);init_geom();init_sym();int barrier=argc>1?atoi(argv[1]):9;uint64_t budget=argc>2?stoull(argv[2]):100000;string prefix=argc>3?argv[3]:"/tmp/p31_3";string cp=prefix+"_b"+to_string(barrier)+"_quot.cp",out=prefix+"_b"+to_string(barrier)+"_result.json";vector<int>r={12,15,24,9,27,20,4,28,25,29,6,2,8,13,1,18,7,19,23,11,26,30,10,5,14,3,21,22,17,16};vector<int>b={17,10,21,22,7,15,8,23,28,13,9,4,20,26,30,12,27,24,29,5,14,1,2,11,18,6,3,16,25,19};string start=encode(r,b);assert(brutePot(start)==3);uint64_t pos=0;vector<DRec>rec;rec.reserve(8000000);if(!loadcp(cp,pos,rec)){DRec d{};memcpy(d.s,start.data(),60);string k=canonical(start);memcpy(d.key,k.data(),60);d.parent=-1;d.mv=0;d.p=3;rec.push_back(d);savecp(cp,pos,rec);}Index idx(rec);cerr<<"loaded barrier="<<barrier<<" pos="<<pos<<" n="<<rec.size()<<" table="<<idx.tab.size()<<"\n";uint64_t done=0;while(pos<rec.size()&&done<budget){string s(rec[pos].s,60);Eval ev(s);assert(ev.pot==rec[pos].p);for(Move m:allMoves){if(!legal(s,m))continue;int np=ev.nextPot(s,m);if(np>barrier)continue;string t=apply(s,m),key=canonical(t);auto[it,ins]=idx.findOrInsert(key.data(),rec.size());if(!ins)continue;DRec d{};memcpy(d.s,t.data(),60);memcpy(d.key,key.data(),60);d.parent=pos;d.mv=encMove(m);d.p=np;int ni=rec.size();rec.push_back(d);if(np<3){pos++;savecp(cp,pos,rec);writeResult(out,rec,ni,pos);cout<<"FOUND barrier="<<barrier<<" processed="<<pos<<" discovered="<<rec.size()<<" result="<<out<<"\n";return 0;}}pos++;done++;if(pos%50000==0){savecp(cp,pos,rec);cerr<<"checkpoint pos="<<pos<<" n="<<rec.size()<<"\n";}}savecp(cp,pos,rec);cout<<"PAUSED barrier="<<barrier<<" pos="<<pos<<" discovered="<<rec.size()<<" queue="<<(rec.size()-pos)<<"\n";if(pos==rec.size())cout<<"EXHAUSTED quotient_states="<<rec.size()<<"\n";}

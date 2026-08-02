#include <bits/stdc++.h>
using namespace std;
struct Pt{int x,y;};
struct Edge{uint8_t a[4];};
struct Line {int A,B,C; bool operator==(Line const&o)const{return A==o.A&&B==o.B&&C==o.C;}};
struct LH{size_t operator()(Line const&l)const{return ((uint64_t)(l.A+64)*1315423911u)^((uint64_t)(l.B+64)*2654435761u)^((uint64_t)(l.C+1024)*97531u);}};
Line linekey(Pt p,Pt q){int A=q.y-p.y,B=p.x-q.x,C=-(A*p.x+B*p.y);int g=std::gcd(abs(A),std::gcd(abs(B),abs(C)));if(g){A/=g;B/=g;C/=g;}if(A<0||(A==0&&B<0)){A=-A;B=-B;C=-C;}return {A,B,C};}
long long det(Pt a,Pt b,Pt c){return 1LL*(b.x-a.x)*(c.y-a.y)-1LL*(b.y-a.y)*(c.x-a.x);}
struct Solver{
 int n,E,W,G; string ori; vector<Edge> edges; vector<array<int,4>> rect; vector<vector<uint64_t>> byPart, atPoint, lineEdge, pairBad; unordered_map<Line,int,LH> lineId; vector<Line> lines; vector<int> sel; long long nodes=0; bool abort=false; long long limit=0;
 Solver(int N,string O):n(N),E(N*N*N*N),W((E+63)/64),G(4*N*N),ori(O){build();}
 int pointId(int x,int y){return x*(2*n)+y;}
 array<int,4> corners(int u,int p,int t,int r){int x0=ori[0]=='c'?u:2*u;int x1=ori[0]=='c'?n+p:2*p+1;int y0=ori[1]=='c'?t:2*t;int y1=ori[1]=='c'?n+r:2*r+1;return {pointId(x0,y0),pointId(x0,y1),pointId(x1,y0),pointId(x1,y1)};}
 Pt pt(int id){return {id/(2*n),id%(2*n)};}
 void setbit(vector<uint64_t>&b,int i){b[i>>6]|=1ULL<<(i&63);} bool test(const vector<uint64_t>&b,int i){return b[i>>6]>>(i&63)&1ULL;}
 void build(){
  edges.reserve(E);rect.reserve(E);byPart.assign(4*n,vector<uint64_t>(W));atPoint.assign(G,vector<uint64_t>(W));
  for(int u=0,idx=0;u<n;u++)for(int p=0;p<n;p++)for(int t=0;t<n;t++)for(int r=0;r<n;r++,idx++){
   Edge e{{(uint8_t)u,(uint8_t)p,(uint8_t)t,(uint8_t)r}};edges.push_back(e);auto c=corners(u,p,t,r);rect.push_back(c);
   for(int k=0;k<4;k++)setbit(byPart[k*n+e.a[k]],idx);for(int q:c)setbit(atPoint[q],idx);
  }
  vector<vector<int>> linePts;
  for(int i=0;i<G;i++)for(int j=i+1;j<G;j++){
   Line L=linekey(pt(i),pt(j));auto it=lineId.find(L);int id;
   if(it==lineId.end()){id=lines.size();lineId[L]=id;lines.push_back(L);linePts.push_back({});}else id=it->second;
  }
  linePts.assign(lines.size(),{});
  for(int id=0;id<(int)lines.size();id++){auto L=lines[id];for(int q=0;q<G;q++){auto z=pt(q);if(L.A*z.x+L.B*z.y+L.C==0)linePts[id].push_back(q);}}
  lineEdge.assign(lines.size(),vector<uint64_t>(W));
  for(int id=0;id<(int)lines.size();id++)for(int q:linePts[id])for(int w=0;w<W;w++)lineEdge[id][w]|=atPoint[q][w];
  pairBad.assign(E,vector<uint64_t>(W));
  for(int i=0;i<E;i++)for(auto pr: {pair<int,int>{0,3},{1,2}}){Line L=linekey(pt(rect[i][pr.first]),pt(rect[i][pr.second]));int id=lineId[L];for(int w=0;w<W;w++)pairBad[i][w]|=lineEdge[id][w];}
  for(int i=0;i<E;i++)for(int j=i+1;j<E;j++){
    bool bad=test(pairBad[i],j)||test(pairBad[j],i); if(bad){setbit(pairBad[i],j);setbit(pairBad[j],i);}
  }
  cerr<<"built n="<<n<<" ori="<<ori<<" E="<<E<<" lines="<<lines.size()<<" W="<<W<<"\n";
 }
 void addTrans(vector<uint64_t>&dst,int i,int j){
  for(int a:rect[i])for(int b:rect[j]){Line L=linekey(pt(a),pt(b));int id=lineId[L];auto &m=lineEdge[id];for(int w=0;w<W;w++)dst[w]|=m[w];}
 }
 bool hallCheck(const vector<uint64_t>&legalBase, array<int,4> used){
  vector<int> us;for(int u=0;u<n;u++)if(!(used[0]>>u&1))us.push_back(u);int k=us.size(); if(k<=2)return true;
  for(int part=1;part<4;part++){
    vector<int> poss(k,0);
    for(int ii=0;ii<k;ii++){
      int u=us[ii];
      for(int v=0;v<n;v++)if(!(used[part]>>v&1)){
        bool any=false; auto &mu=byPart[u]; auto &mv=byPart[part*n+v];
        for(int w=0;w<W;w++)if(mu[w]&mv[w]&legalBase[w]){any=true;break;}
        if(any)poss[ii]|=1<<v;
      }
      if(!poss[ii])return false;
    }
    for(int mask=1;mask<(1<<k);mask++){
      int uni=0,cnt=0;for(int ii=0;ii<k;ii++)if(mask>>ii&1){uni|=poss[ii];cnt++;}
      if(__builtin_popcount((unsigned)uni)<cnt)return false;
    }
  }
  return true;
 }
 bool dfs(array<int,4> used, vector<uint64_t> const&forb){
  nodes++; if(limit&&nodes>limit){abort=true;return false;} if((int)sel.size()==n)return true;
  vector<uint64_t> legal(W);for(int w=0;w<W;w++)legal[w]=~forb[w]; if(E&63)legal[W-1]&=(1ULL<<(E&63))-1;
  for(int part=0;part<4;part++)for(int v=0;v<n;v++)if(used[part]>>v&1){auto&m=byPart[part*n+v];for(int w=0;w<W;w++)legal[w]&=~m[w];}
  if(!hallCheck(legal,used))return false;
  int bestPart=-1,bestVal=-1,bestCnt=INT_MAX; vector<int> cand;
  for(int part=0;part<4;part++)for(int v=0;v<n;v++)if(!(used[part]>>v&1)){
    int cnt=0;auto&m=byPart[part*n+v];for(int w=0;w<W;w++)cnt+=__builtin_popcountll(legal[w]&m[w]);
    if(cnt==0)return false; if(cnt<bestCnt){bestCnt=cnt;bestPart=part;bestVal=v;}
  }
  auto &bm=byPart[bestPart*n+bestVal];
  for(int w=0;w<W;w++){uint64_t x=legal[w]&bm[w];while(x){int b=__builtin_ctzll(x);cand.push_back((w<<6)+b);x&=x-1;}}
  sort(cand.begin(),cand.end(),[&](int a,int b){long long da=0,db=0;for(int w=0;w<W;w++){da+=__builtin_popcountll(pairBad[a][w]&legal[w]);db+=__builtin_popcountll(pairBad[b][w]&legal[w]);}return da<db;});
  for(int idx:cand){
    vector<uint64_t> nf=forb;for(int w=0;w<W;w++)nf[w]|=pairBad[idx][w];for(int prev:sel)addTrans(nf,idx,prev);
    auto nu=used;for(int k=0;k<4;k++)nu[k]|=1<<edges[idx].a[k];sel.push_back(idx);if(dfs(nu,nf))return true;sel.pop_back();if(abort)return false;
  }
  return false;
 }
 bool solve(long long lim=0){limit=lim;vector<uint64_t> f(W);array<int,4> u{0,0,0,0};return dfs(u,f);} 
 void printSol(){for(int i:sel){auto e=edges[i];cout<<"("<<(int)e.a[0]<<","<<(int)e.a[1]<<","<<(int)e.a[2]<<","<<(int)e.a[3]<<") ";}cout<<"\n";}
};
int main(int argc,char**argv){
 int n=stoi(argv[1]); string o=argv[2]; auto st=chrono::steady_clock::now(); Solver s(n,o);
 if(argc>=5 && string(argv[3])=="shard"){
   int shard=stoi(argv[4]), shards=stoi(argv[5]); bool ok=false; long long roots=0;
   for(int idx=0; idx<s.E; idx++){
     if(s.edges[idx].a[0]!=0) continue;
     int local=idx;
     if(local%shards!=shard) continue;
     roots++;
     vector<uint64_t> f=s.pairBad[idx]; array<int,4> used{0,0,0,0};
     for(int k=0;k<4;k++) used[k]|=1<<s.edges[idx].a[k];
     s.sel.push_back(idx); if(s.dfs(used,f)){ok=true;break;} s.sel.pop_back();
   }
   double sec=chrono::duration<double>(chrono::steady_clock::now()-st).count();
   cout<<"n="<<n<<" ori="<<o<<" shard="<<shard<<"/"<<shards<<" roots="<<roots<<" ok="<<ok<<" nodes="<<s.nodes<<" sec="<<sec<<"\n"; if(ok)s.printSol(); return 0;
 }
 long long lim=argc>3?stoll(argv[3]):0; bool ok=s.solve(lim); double sec=chrono::duration<double>(chrono::steady_clock::now()-st).count();cout<<"n="<<n<<" ori="<<o<<" ok="<<ok<<" nodes="<<s.nodes<<" abort="<<s.abort<<" sec="<<sec<<"\n";if(ok)s.printSol();
}

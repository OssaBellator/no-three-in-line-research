#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
struct Opt{int s,t,e,oid;vector<pair<int,uint8_t>> lc;};
int main(int argc,char**argv){
 if(argc!=4){cerr<<"usage INPUT_JSON MODE THREADS\n";return 2;}
 ifstream input(argv[1]); if(!input){cerr<<"cannot open input JSON\n";return 2;} string text((istreambuf_iterator<char>(input)),{}); if(text.find("\"p\": 41")==string::npos && text.find("\"p\":41")==string::npos){cerr<<"input is not p=41 near-state\n";return 2;}
 string mode=argv[2]; if(mode!="signed"&&mode!="target"){cerr<<"mode must be signed or target\n";return 2;} bool targetOnly=(mode=="target"); int threads=atoi(argv[3]); if(threads<1)return 2; omp_set_num_threads(threads); const int n=40,m=20,K=13;int r1[m]={19,20,13,14,10,6,11,2,16,1,8,4,15,7,18,12,3,17,5,9};int ee[m]={1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1};vector<int>rho(m),E(ee,ee+m);for(int i=0;i<m;i++)rho[i]=r1[i]-1;
vector<vector<int>> cell_lines(n*n);int L=0;for(int dx=1;dx<n;dx++)for(int dy=-(n-1);dy<n;dy++){if(dy==0||gcd(dx,abs(dy))!=1)continue;for(int x=0;x<n;x++)for(int y=0;y<n;y++){if(0<=x-dx&&x-dx<n&&0<=y-dy&&y-dy<n)continue;vector<int>p;for(int X=x,Y=y;0<=X&&X<n&&0<=Y&&Y<n;X+=dx,Y+=dy)p.push_back(X*n+Y);if(p.size()>=3){for(int c:p)cell_lines[c].push_back(L);L++;}}}if(L!=108190){cerr<<"bad lines\n";return 2;}
auto oid=[&](int i,int j,int e){if(i==j)return i*m+i;if(i<j)return m*m+2*(i*m+j)+e;return m*m+2*(j*m+i)+1-e;};vector<Opt>opts;vector<vector<vector<int>>>by(m,vector<vector<int>>(m));int maxoid=0;
for(int i=0;i<m;i++)for(int j=0;j<m;j++)for(int e=0;e<(i==j?1:2);e++){int I=n-1-i,J=n-1-j;array<int,4>cs=!e?array<int,4>{i*n+j,I*n+J,j*n+I,J*n+i}:array<int,4>{i*n+J,I*n+j,j*n+i,J*n+I};unordered_map<int,int>cnt;for(int c:cs)for(int l:cell_lines[c])cnt[l]++;Opt o{i,j,e,oid(i,j,e),{}};maxoid=max(maxoid,o.oid);o.lc.reserve(cnt.size());for(auto [l,c]:cnt)o.lc.push_back({l,(uint8_t)c});int id=opts.size();opts.push_back(move(o));by[i][j].push_back(id);}
vector<int>base(m),baseocc(L,0);for(int i=0;i<m;i++){int e=rho[i]==i?0:E[i];for(int id:by[i][rho[i]])if(opts[id].e==e)base[i]=id;for(auto[l,c]:opts[base[i]].lc)baseocc[l]+=c;}
vector<array<int,K>> supports;array<int,K>A;for(int i=0;i<K;i++)A[i]=i;while(1){bool hit=false;for(int x:A)if(x==14||x==17||x==19)hit=true;if(hit)supports.push_back(A);int q=K-1;while(q>=0&&A[q]==m-K+q)q--;if(q<0)break;A[q]++;for(int j=q+1;j<K;j++)A[j]=A[j-1]+1;}cerr<<"supports="<<supports.size()<<" opts="<<opts.size()<<"\n";
atomic<bool>found(false);atomic<unsigned long long> done(0),nodes(0),hallfails(0),emptyfails(0);mutex ansmu;array<int,K>ansA{};vector<int>ansOpt;
#pragma omp parallel
{
 vector<int>occ(L),candStore; vector<vector<int>>cand(m);vector<char>in(m),assigned(m),usedoid(maxoid+1); unsigned long long ln=0,lh=0,le=0,ld=0;
#pragma omp for schedule(dynamic,8)
 for(size_t zi=0;zi<supports.size();zi++){
  if(found.load(memory_order_relaxed))continue;ld++;auto S=supports[zi];fill(in.begin(),in.end(),0);uint32_t targetmask=0;for(int s:S){in[s]=1;targetmask|=1u<<rho[s];}
  occ=baseocc;fill(usedoid.begin(),usedoid.end(),0);for(int i=0;i<m;i++)if(!in[i])usedoid[opts[base[i]].oid]=1;for(int s:S)for(auto[l,c]:opts[base[s]].lc)occ[l]-=c;
  bool impossible=false;for(int s:S){cand[s].clear();for(int t=0;t<m;t++)if(targetmask>>t&1u)for(int id:by[s][t]){auto&o=opts[id];if((targetOnly?t==rho[s]:id==base[s])||usedoid[o.oid])continue;bool ok=true;for(auto[l,c]:o.lc)if(occ[l]+c>2){ok=false;break;}if(ok)cand[s].push_back(id);}if(cand[s].empty()){impossible=true;le++;break;}}
  if(impossible)continue;fill(assigned.begin(),assigned.end(),0);uint32_t usedtargets=0;vector<int>chosen;chosen.reserve(K);vector<int>solution;
  function<bool()>dfs=[&](){ln++;if(chosen.size()==K){solution=chosen;return true;}
    vector<vector<int>> sav(m),tav(m); vector<pair<int,uint32_t>>domains; domains.reserve(K-chosen.size()); int bs=-1,bt=-1; size_t bestsz=SIZE_MAX;
    for(int s:S)if(!assigned[s]){uint32_t dm=0;for(int id:cand[s]){auto&o=opts[id];if((usedtargets>>o.t)&1u||usedoid[o.oid])continue;bool ok=true;for(auto[l,c]:o.lc)if(occ[l]+c>2){ok=false;break;}if(ok){sav[s].push_back(id);tav[o.t].push_back(id);dm|=1u<<o.t;}}if(sav[s].empty())return false;domains.push_back({s,dm});if(sav[s].size()<bestsz){bestsz=sav[s].size();bs=s;bt=-1;}}
    for(int t=0;t<m;t++)if((targetmask>>t&1u)&&!((usedtargets>>t)&1u)){if(tav[t].empty())return false;if(tav[t].size()<bestsz){bestsz=tav[t].size();bt=t;bs=-1;}}
    vector<int>tm(m,-1);function<bool(int,vector<char>&)>aug=[&](int q,vector<char>&vis){uint32_t dm=domains[q].second;while(dm){int t=__builtin_ctz(dm);dm&=dm-1;if(vis[t])continue;vis[t]=1;if(tm[t]<0||aug(tm[t],vis)){tm[t]=q;return true;}}return false;};for(int q=0;q<(int)domains.size();q++){vector<char>vis(m);if(!aug(q,vis)){lh++;return false;}}
    vector<int>branch=bs>=0?sav[bs]:tav[bt];sort(branch.begin(),branch.end(),[&](int a,int b){auto&Ao=opts[a];auto&Bo=opts[b];int da=sav[Ao.s].size()+tav[Ao.t].size(),db=sav[Bo.s].size()+tav[Bo.t].size();if(da!=db)return da<db;int sa=0,sb=0;for(auto[l,c]:Ao.lc)sa+=occ[l]*c;for(auto[l,c]:Bo.lc)sb+=occ[l]*c;return sa<sb;});
    for(int id:branch){auto&o=opts[id];if(assigned[o.s]||((usedtargets>>o.t)&1u)||usedoid[o.oid])continue;assigned[o.s]=1;usedtargets|=1u<<o.t;usedoid[o.oid]=1;for(auto[l,c]:o.lc)occ[l]+=c;chosen.push_back(id);if(dfs())return true;chosen.pop_back();for(auto[l,c]:o.lc)occ[l]-=c;usedoid[o.oid]=0;usedtargets&=~(1u<<o.t);assigned[o.s]=0;}return false;};
  if(dfs()){bool expected=false;if(found.compare_exchange_strong(expected,true)){lock_guard<mutex>lk(ansmu);ansA=S;ansOpt=solution;}}
 }
 done.fetch_add(ld);nodes.fetch_add(ln);hallfails.fetch_add(lh);emptyfails.fetch_add(le);
}
cout<<"mode="<<mode<<" supports="<<done.load()<<" nodes="<<nodes.load()<<" hall="<<hallfails.load()<<" empty="<<emptyfails.load()<<" found="<<found.load();if(found){cout<<" A=";for(int s:ansA)cout<<s+1<<',';cout<<" choices=";for(int id:ansOpt){auto&o=opts[id];cout<<o.s+1<<':'<<o.t+1<<':'<<o.e<<',';}}cout<<'\n';
}

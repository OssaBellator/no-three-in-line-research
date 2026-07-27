#include <bits/stdc++.h>
using namespace std;
struct Opt{int s,t,e,oid;vector<pair<int,uint8_t>> lc;};
int main(int argc,char**argv){
 if(argc!=5){cerr<<"usage INPUT_JSON SUPPORT SHARD SHARDS\n";return 2;} ifstream input(argv[1]); if(!input){cerr<<"cannot open input JSON\n";return 2;} string text((istreambuf_iterator<char>(input)),{}); if(text.find("\"p\": 41")==string::npos && text.find("\"p\":41")==string::npos){cerr<<"input is not p=41 near-state\n";return 2;} int K=atoi(argv[2]),shard=atoi(argv[3]),shards=atoi(argv[4]); if(K<1||K>20||shard<0||shards<1||shard>=shards)return 2;
 const int n=40,m=20; int rho1[m]={19,20,13,14,10,6,11,2,16,1,8,4,15,7,18,12,3,17,5,9}; int E0[m]={1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1}; vector<int>rho(m),E(E0,E0+m);for(int i=0;i<m;++i)rho[i]=rho1[i]-1;
 vector<vector<int>> cell_lines(n*n);int L=0;for(int dx=1;dx<n;++dx)for(int dy=-(n-1);dy<n;++dy){if(dy==0||gcd(dx,abs(dy))!=1)continue;for(int x=0;x<n;++x)for(int y=0;y<n;++y){if(0<=x-dx&&x-dx<n&&0<=y-dy&&y-dy<n)continue;vector<int>p;for(int X=x,Y=y;0<=X&&X<n&&0<=Y&&Y<n;X+=dx,Y+=dy)p.push_back(X*n+Y);if(p.size()>=3){for(int c:p)cell_lines[c].push_back(L);++L;}}} if(L!=108190){cerr<<"line count "<<L<<"\n";return 2;}
 auto oid=[&](int i,int j,int e){if(i==j)return i*m+i;if(i<j)return m*m+2*(i*m+j)+e;return m*m+2*(j*m+i)+1-e;};
 vector<Opt> opts; vector<vector<vector<int>>> by(m,vector<vector<int>>(m));
 for(int i=0;i<m;++i)for(int j=0;j<m;++j){int ec=i==j?1:2;for(int e=0;e<ec;++e){int I=n-1-i,J=n-1-j;array<int,4>cs=!e?array<int,4>{i*n+j,I*n+J,j*n+I,J*n+i}:array<int,4>{i*n+J,I*n+j,j*n+i,J*n+I};unordered_map<int,int>cnt;for(int c:cs)for(int l:cell_lines[c])cnt[l]++;Opt o{i,j,e,oid(i,j,e),{}};o.lc.reserve(cnt.size());for(auto [l,c]:cnt)o.lc.push_back({l,(uint8_t)c});int id=opts.size();opts.push_back(move(o));by[i][j].push_back(id);}}
 vector<int> baseopt(m,-1),baseocc(L,0);unordered_set<int> seen;for(int i=0;i<m;++i){int ee=rho[i]==i?0:E[i];for(int id:by[i][rho[i]])if(opts[id].e==ee)baseopt[i]=id;if(baseopt[i]<0)return 2;if(!seen.insert(opts[baseopt[i]].oid).second){cerr<<"base duplicate\n";return 2;}for(auto [l,c]:opts[baseopt[i]].lc)baseocc[l]+=c;}
 vector<int> bad;for(int l=0;l<L;++l)if(baseocc[l]>2)bad.push_back(l);if(bad.size()!=4){cerr<<"base bad lines="<<bad.size()<<"\n";return 2;}
 uint32_t badmask=(1u<<14)|(1u<<17)|(1u<<19); vector<int> A(K);iota(A.begin(),A.end(),0);uint64_t ordinal=0,subsets=0,nodes=0,hallfails=0,emptyfails=0;bool found=false;vector<int>fA,fO;
 auto nextcomb=[&](){int q=K-1;while(q>=0&&A[q]==m-K+q)--q;if(q<0)return false;++A[q];for(int r=q+1;r<K;++r)A[r]=A[r-1]+1;return true;};
 do{uint32_t am=0;for(int x:A)am|=1u<<x;if(!(am&badmask))continue;uint64_t ord=ordinal++;if(ord%shards!=(uint64_t)shard)continue;++subsets;vector<char>in(m,0);uint32_t targetmask=0;for(int x:A){in[x]=1;targetmask|=1u<<rho[x];}
  vector<int>occ=baseocc;unordered_set<int>usedoids;for(int i=0;i<m;++i)if(!in[i])usedoids.insert(opts[baseopt[i]].oid);for(int i:A)for(auto[l,c]:opts[baseopt[i]].lc)occ[l]-=c;
  vector<vector<int>> cand(m);bool impossible=false;for(int s:A){for(int t=0;t<m;++t)if(targetmask>>t&1u)for(int id:by[s][t]){auto&o=opts[id];if(id==baseopt[s]||usedoids.count(o.oid))continue;bool ok=true;for(auto[l,c]:o.lc)if(occ[l]+c>2){ok=false;break;}if(ok)cand[s].push_back(id);}if(cand[s].empty()){impossible=true;++emptyfails;break;}}
  if(impossible)continue;vector<char>assigned(m,0);uint32_t usedtargets=0;vector<int>chosen;
  function<bool()> dfs=[&](){++nodes;if(chosen.size()==A.size()){fA=A;fO=chosen;return true;}int bs=-1;vector<int>bavail;vector<pair<int,uint32_t>>domains;
   for(int s:A)if(!assigned[s]){vector<int>av;uint32_t dm=0;for(int id:cand[s]){auto&o=opts[id];if(usedtargets>>o.t&1u||usedoids.count(o.oid))continue;bool ok=true;for(auto[l,c]:o.lc)if(occ[l]+c>2){ok=false;break;}if(ok){av.push_back(id);dm|=1u<<o.t;}}if(av.empty())return false;domains.push_back({s,dm});if(bs<0||av.size()<bavail.size()){bs=s;bavail=move(av);}}
   vector<int>tm(m,-1);function<bool(int,vector<char>&)>aug=[&](int q,vector<char>&vis){uint32_t dm=domains[q].second;for(int t=0;t<m;++t)if((dm>>t&1u)&&!vis[t]){vis[t]=1;if(tm[t]<0||aug(tm[t],vis)){tm[t]=q;return true;}}return false;};for(int q=0;q<(int)domains.size();++q){vector<char>vis(m,0);if(!aug(q,vis)){++hallfails;return false;}}
   sort(bavail.begin(),bavail.end(),[&](int a,int b){int sa=0,sb=0;for(auto[l,c]:opts[a].lc)sa+=occ[l]*c;for(auto[l,c]:opts[b].lc)sb+=occ[l]*c;return sa<sb;});assigned[bs]=1;for(int id:bavail){auto&o=opts[id];usedtargets|=1u<<o.t;usedoids.insert(o.oid);for(auto[l,c]:o.lc)occ[l]+=c;chosen.push_back(id);if(dfs())return true;chosen.pop_back();for(auto[l,c]:o.lc)occ[l]-=c;usedoids.erase(o.oid);usedtargets&=~(1u<<o.t);}assigned[bs]=0;return false;};
  if(dfs()){found=true;break;}
 }while(nextcomb());
 cout<<"support="<<K<<" shard="<<shard<<" shards="<<shards<<" subsets="<<subsets<<" nodes="<<nodes<<" hall="<<hallfails<<" empty="<<emptyfails<<" found="<<found;if(found){cout<<" A=";for(int x:fA)cout<<x+1<<',';cout<<" choices=";for(int id:fO){auto&o=opts[id];cout<<o.s+1<<':'<<o.t+1<<':'<<o.e<<',';}}cout<<"\n";
}

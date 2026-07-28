    int8_t adj[MAXM][MAXM];
    for(int i=0;i<m;i++)for(int j=0;j<m;j++)adj[i][j]=-1;
    bool impossible=false;
    for(int a=0;a<m;a++)for(int b=a+1;b<m;b++){
      int v=rel[i4(a,cycles[ci][a],b,cycles[ci][b])];
      if(v==3){impossible=true;break;}
      if(v){
        int p=v==1?0:1;adj[a][b]=adj[b][a]=p;
      }
    }
    if(impossible)continue;
    CleanInfo inf;inf.comp.fill(-1);inf.colour.fill(-1);
    bool ok=true;int cc=0;
    for(int root=0;root<m;root++)if(inf.comp[root]<0){
      array<int,MAXM> qq{};int head=0,tailq=0;qq[tailq++]=root;
      inf.comp[root]=cc;inf.colour[root]=0;
      while(head<tailq){
        int u=qq[head++];
        for(int v=0;v<m;v++)if(adj[u][v]>=0){
          int want=inf.colour[u]^adj[u][v];
          if(inf.comp[v]<0){inf.comp[v]=cc;inf.colour[v]=want;qq[tailq++]=v;}
          else if(inf.colour[v]!=want)ok=false;
        }
      }
      cc++;
    }
    if(!ok)continue;
    inf.components=cc;
    clean_index[ci]=infos.size();
    infos.push_back(inf);clean_cycle.push_back(ci);
    clean_states+=1LL<<cc;
  }
  int NC=infos.size();

  vector<array<array<uint64_t,MAXW>,MAXM>> varbits(MAXM+1);
  vector<array<uint64_t,MAXW>> fullmask(MAXM+1);
  for(int c=1;c<=m;c++){
    int roots=1<<c, words=(roots+63)/64;
    for(int w=0;w<words;w++){
      int left=roots-64*w;
      fullmask[c][w]=left>=64?~0ULL:(left<=0?0ULL:((1ULL<<left)-1));
    }
    for(int j=0;j<c;j++)for(int r=0;r<roots;r++)
      if((r>>j)&1)varbits[c][j][r>>6]|=1ULL<<(r&63);
  }

  vector<uint64_t> ownerbits((size_t)NC*m*WORDS,0);
  vector<uint64_t> reached((size_t)NC*WORDS,0);
  vector<long long> valid_per(NC,0);

  auto obase=[m,WORDS](int x,int owner){return ((size_t)x*m+owner)*WORDS;};
  #pragma omp parallel for schedule(dynamic,32)
  for(int x=0;x<NC;x++){
    int ci=clean_cycle[x], cc=infos[x].components;
    auto &inf=infos[x];
    for(int ti=0;ti<K;ti++){
      auto T=triples[ti];
      uint8_t bm=badpat[ib(ti,cycles[ci][T[0]],cycles[ci][T[1]],cycles[ci][T[2]])];
      if(!bm)continue;
      for(int w=0;w<WORDS;w++){
        uint64_t bs=0;
        for(int p=0;p<8;p++)if((bm>>p)&1){
          uint64_t term=fullmask[cc][w];
          for(int k=0;k<3;k++){
            int owner=T[k], comp=inf.comp[owner];
            int rootbit=((p>>k)&1)^inf.colour[owner];
            uint64_t vb=varbits[cc][comp][w];
            term &= rootbit?vb:(~vb&fullmask[cc][w]);
          }
          bs|=term;
        }
        ownerbits[obase(x,T[0])+w]|=bs;
        ownerbits[obase(x,T[1])+w]|=bs;
        ownerbits[obase(x,T[2])+w]|=bs;
      }
    }
    long long valid=0;
    for(int w=0;w<WORDS;w++){
      uint64_t any=0;
      for(int owner=0;owner<m;owner++)any|=ownerbits[obase(x,owner)+w];
      uint64_t v=(~any)&fullmask[cc][w];
      reached[(size_t)x*WORDS+w]=v;
      valid+=__builtin_popcountll(v);
    }
    valid_per[x]=valid;
  }
  long long valid_states=accumulate(valid_per.begin(),valid_per.end(),0LL);

  vector<int> neighbour((size_t)NC*K,-1);
  #pragma omp parallel for schedule(static)
  for(int x=0;x<NC;x++){
    int ci=clean_cycle[x];
    for(int ti=0;ti<K;ti++){
      auto it=index.find(encode(switched(cycles[ci],m,triples[ti]),m));
      int cj=it->second;
      neighbour[(size_t)x*K+ti]=clean_index[cj];
    }
  }

  vector<int8_t> cmin(NC,-1);
  queue<int> q;
  vector<long long> dist(32,0);
  dist[0]=valid_states;
  for(int x=0;x<NC;x++)if(valid_per[x]){cmin[x]=0;q.push(x);}
  while(!q.empty()){
    int eta=q.front();q.pop();
    int nd=cmin[eta]+1;
    for(int ti=0;ti<K;ti++){
      int rho=neighbour[(size_t)eta*K+ti];
      if(rho<0)continue;
      auto T=triples[ti];
      bool anynew=false;long long added=0;
      for(int w=0;w<WORDS;w++){
        uint64_t eligible=ownerbits[obase(rho,T[0])+w]|
                          ownerbits[obase(rho,T[1])+w]|
                          ownerbits[obase(rho,T[2])+w];
        uint64_t &seen=reached[(size_t)rho*WORDS+w];
        uint64_t fresh=eligible&~seen;
        if(fresh){seen|=fresh;anynew=true;added+=__builtin_popcountll(fresh);}
      }
      if(added)dist[nd]+=added;
      if(anynew&&cmin[rho]<0){cmin[rho]=nd;q.push(rho);}
    }
  }
  long long reached_total=accumulate(dist.begin(),dist.end(),0LL);
  int maxd=-1;for(int d=0;d<(int)dist.size();d++)if(dist[d])maxd=d;
  Result R;R.m=m;R.cycles=C;R.clean_cycles=NC;R.clean_states=clean_states;
  R.valid_states=valid_states;R.unreached=clean_states-reached_total;
  R.distance=dist;R.max_distance=maxd;
  int h=maxd;
  vector<long double> reverse_lower(NC,0.0L), reverse_upper(NC,0.0L);
  vector<long long> raw_incoming(NC,0);
  vector<array<long long,5>> normalizer_bin_counts(NC);
  array<long long,5> bin_upper{};
  int bin_count=0;
  if(m==8){bin_upper={2048,4096,8192,0,0};bin_count=3;}
  else if(m==9){bin_upper={4096,8192,16384,32768,0};bin_count=4;}
  else if(m==10){bin_upper={16384,32768,65536,131072,0};bin_count=4;}
  long long observed_min_normalizer=LLONG_MAX,observed_max_normalizer=0;
  struct Gate{array<uint64_t,MAXW> elig{};int target=-1;};
  for(int x=0;x<NC;x++)if(cmin[x]==h){
    int cc=infos[x].components;array<uint64_t,MAXW> lower{},closing{};
    vector<Gate> gates;int active=0;
    for(int ti=0;ti<K;ti++){
      int y=neighbour[(size_t)x*K+ti];if(y<0)continue;auto T=triples[ti];

  int band_lo=650,band_hi=720;if(argc>1)band_lo=atoi(argv[1]);if(argc>2)band_hi=atoi(argv[2]);
  vector<array<int,3>> triples;for(int a=0;a<M;a++)for(int b=a+1;b<M;b++)for(int c=b+1;c<M;c++)triples.push_back({a,b,c});int K=triples.size();
  static int8_t rel[M][M][M][M];
  for(int a=0;a<M;a++)for(int ta=0;ta<M;ta++)if(a!=ta)for(int b=a+1;b<M;b++)for(int tb=0;tb<M;tb++)if(b!=tb&&ta!=tb){bool eq=pair_bad(a,ta,0,b,tb,0),un=pair_bad(a,ta,0,b,tb,1);rel[a][ta][b][tb]=eq&&un?3:eq?2:un?1:0;}
  auto rhos=cycles();int C=rhos.size();unordered_map<Rho,int,RH>id;id.reserve(C*2);for(int i=0;i<C;i++)id[rhos[i]]=i;vector<Info>info(C);long long cleanStates=0;int cleanCycles=0;
  for(int ci=0;ci<C;ci++){
    int8_t adj[M][M];for(int i=0;i<M;i++)for(int j=0;j<M;j++)adj[i][j]=-1;bool impossible=false;
    for(int a=0;a<M&&!impossible;a++)for(int b=a+1;b<M;b++){int v=rel[a][rhos[ci][a]][b][rhos[ci][b]];if(v==3){impossible=true;break;}if(v){int p=v==1?0:1;adj[a][b]=adj[b][a]=p;}}
    if(impossible) continue;
    Info in;
    in.comp.fill(-1);
    in.colour.fill(-1);
    bool ok=true;
    int cc=0;
    for(int root=0;root<M;root++)if(in.comp[root]<0){array<int,M>q{};int h=0,z=0;q[z++]=root;in.comp[root]=cc;in.colour[root]=0;while(h<z){int u=q[h++];for(int v=0;v<M;v++)if(adj[u][v]>=0){int want=in.colour[u]^adj[u][v];if(in.comp[v]<0){in.comp[v]=cc;in.colour[v]=want;q[z++]=v;}else if(in.colour[v]!=want)ok=false;}}cc++;}
    if(ok){in.clean=true;in.components=cc;info[ci]=in;cleanCycles++;cleanStates+=1LL<<cc;}
  }
  auto key=[](int s,int ta,int tb,int tc){return ((s*M+ta)*M+tb)*M+tc;};
  vector<vector<int>> lists(K*M*M*M);
  for(int ci=0;ci<C;ci++)for(int s=0;s<K;s++){auto S=triples[s];lists[key(s,rhos[ci][S[0]],rhos[ci][S[1]],rhos[ci][S[2]])].push_back(ci);}
  int maxRaw=0;long long nonemptyArcKeys=0;for(auto const&v:lists)if(!v.empty()){nonemptyArcKeys++;maxRaw=max(maxRaw,(int)v.size());}
  vector<Candidate> cand;cand.reserve(100000);
  for(int s=0;s<K;s++){auto S=triples[s];for(int ta=0;ta<M;ta++)for(int tb=0;tb<M;tb++)for(int tc=0;tc<M;tc++){if(lists[key(s,ta,tb,tc)].empty())continue;for(int mask=0;mask<4;mask++)if(triple_bad(S[0],ta,mask&1,S[1],tb,(mask>>1)&1,S[2],tc,0))cand.push_back({(uint16_t)s,(uint8_t)ta,(uint8_t)tb,(uint8_t)tc,(uint8_t)mask});}}
  int threads=1;
#ifdef _OPENMP
  threads=omp_get_max_threads();
#endif
  struct Acc{long long flaws=0,incidences=0,supply=0;int maxSources=0;array<long long,721>hist{};Best best;};
  vector<Acc> acc(threads);
#pragma omp parallel for schedule(dynamic,32)
  for(int ix=0;ix<(int)cand.size();ix++){
    int tid=0;
#ifdef _OPENMP
    tid=omp_get_thread_num();
#endif
    auto c=cand[ix];auto S=triples[c.s];auto const&raw=lists[key(c.s,c.ta,c.tb,c.tc)];int ns=0;long long supply=0;
    for(int ci:raw){if(!info[ci].clean)continue;array<int8_t,M>root;root.fill(-1);bool ok=true;int distinct=0;for(int k=0;k<3;k++){int owner=S[k],co=info[ci].comp[owner],value=((c.mask>>k)&1)^info[ci].colour[owner];if(root[co]<0){root[co]=value;distinct++;}else if(root[co]!=value)ok=false;}if(ok){ns++;supply+=1LL<<(info[ci].components-distinct);}}
    if(!ns) continue;
    auto &a=acc[tid];
    a.flaws+=2;
    a.incidences+=2LL*ns;
    a.supply+=2*supply;
    a.maxSources=max(a.maxSources,ns);
    a.hist[ns]+=2;
    Best candidateBest{supply,ns,c};
    if(better(candidateBest,a.best)) a.best=candidateBest;
  }
  Acc total;for(auto const&a:acc){total.flaws+=a.flaws;total.incidences<+=a.incidences;total.supply+=a.supply;total.maxSources=max(total.maxSources,a.maxSources);for(int i=0;i<=720;i++)total.hist[i]+=a.hist[i];if(better(a.best,total.best)) total.best=a.best;}
  int minSources=0;
  for(int i=1;i<=720;i++) if(total.hist[i]){minSources=i;break;}

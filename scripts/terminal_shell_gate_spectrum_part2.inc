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
  for(int x=0;x<NC;x++)if(cmin[x]==h){
    int cc=infos[x].components;array<uint64_t,MAXW> lower{},closing{};
    vector<array<uint64_t,MAXW>> gates;int active=0;
    for(int ti=0;ti<K;ti++){
      int y=neighbour[(size_t)x*K+ti];if(y<0)continue;auto T=triples[ti];
      array<uint64_t,MAXW> elig{};bool nonempty=false;
      for(int w=0;w<WORDS;w++){
        elig[w]=ownerbits[obase(x,T[0])+w]|ownerbits[obase(x,T[1])+w]|ownerbits[obase(x,T[2])+w];
        nonempty|=elig[w]!=0;if(cmin[y]<=h-2)lower[w]|=elig[w];if(cmin[y]<=h-1)closing[w]|=elig[w];
      }
      if(nonempty&&cmin[y]==h-1){gates.push_back(elig);active++;}
    }
    bool lowerEmpty=true,closingFull=true;for(int w=0;w<WORDS;w++){lowerEmpty&=lower[w]==0;closingFull&=closing[w]==fullmask[cc][w];}
    R.terminal_cycles++;R.terminal_states+=1LL<<cc;R.lower_gate_nonempty+=!lowerEmpty;R.closing_gate_notfull+=!closingFull;
    R.min_active=min(R.min_active,active);R.max_active=max(R.max_active,active);R.total_active+=active;
    int minmult=K,maxmult=0;for(int root=0;root<(1<<cc);root++){int mult=0;for(auto const&e:gates)mult+=(e[root>>6]>>(root&63))&1ULL;minmult=min(minmult,mult);maxmult=max(maxmult,mult);}
    R.min_root=min(R.min_root,minmult);R.max_root=max(R.max_root,maxmult);R.total_minroot+=minmult;
  }
  return R;
}

int main(int argc,char**argv){
  int first=8,last=10;if(argc>1)first=last=atoi(argv[1]);
  cout<<"{\n  \"cases\": [\n";
  const int expectedH[11]={0,0,0,0,0,0,0,0,3,4,5};
  const long long expectedCycles[11]={0,0,0,0,0,0,0,0,436,2298,1260};
  const long long expectedStates[11]={0,0,0,0,0,0,0,0,33624,478040,535072};
  const int expectedMin[11]={0,0,0,0,0,0,0,0,13,29,70};
  const int expectedMax[11]={0,0,0,0,0,0,0,0,47,75,118};
  const long long expectedActive[11]={0,0,0,0,0,0,0,0,13674,128592,123852};
  const long long expectedRoot[11]={0,0,0,0,0,0,0,0,13608,128176,123374};
  for(int m=first;m<=last;m++){
    Result r=run_case(m);
    bool ok=!r.unreached&&!r.lower_gate_nonempty&&!r.closing_gate_notfull&&
      r.max_distance==expectedH[m]&&r.terminal_cycles==expectedCycles[m]&&
      r.terminal_states==expectedStates[m]&&r.min_active==expectedMin[m]&&
      r.max_active==expectedMax[m]&&r.min_root==expectedMin[m]&&
      r.max_root==expectedMax[m]&&r.total_active==expectedActive[m]&&
      r.total_minroot==expectedRoot[m];
    if(!ok){cerr<<"terminal gate mismatch at m="<<m<<"\n";return 2;}
    cout<<"    {\"m\":"<<m<<",\"maximum_distance\":"<<r.max_distance<<",\"terminal_cycles\":"<<r.terminal_cycles<<",\"terminal_states\":"<<r.terminal_states
        <<",\"active_closing_gate_triples_range\":["<<r.min_active<<","<<r.max_active<<"]"
        <<",\"minimum_root_gate_multiplicity_range\":["<<r.min_root<<","<<r.max_root<<"]"
        <<",\"total_active_closing_gate_triples\":"<<r.total_active
        <<",\"total_minimum_root_gate_multiplicity\":"<<r.total_minroot<<"}"<<(m<last?",":"")<<"\n";
  }
  cout<<"  ],\n  \"terminal_shell_has_no_two_layer_shortcut\": true,\n  \"closing_predecessor_shell_covers_every_root\": true\n}\n";
}

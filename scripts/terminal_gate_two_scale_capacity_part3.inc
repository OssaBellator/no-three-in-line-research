  vector<long long> raw_incoming(NC,0);
  struct Gate{array<uint64_t,MAXW> elig{};int target=-1;};
  for(int x=0;x<NC;x++)if(cmin[x]==h){
    int cc=infos[x].components;array<uint64_t,MAXW> lower{},closing{};
    vector<Gate> gates;int active=0;
    for(int ti=0;ti<K;ti++){
      int y=neighbour[(size_t)x*K+ti];if(y<0)continue;auto T=triples[ti];
      array<uint64_t,MAXW> elig{};bool nonempty=false;
      for(int w=0;w<WORDS;w++){
        elig[w]=ownerbits[obase(x,T[0])+w]|ownerbits[obase(x,T[1])+w]|ownerbits[obase(x,T[2])+w];
        nonempty|=elig[w]!=0;if(cmin[y]<=h-2)lower[w]|=elig[w];if(cmin[y]<=h-1)closing[w]|=elig[w];
      }
      if(nonempty&&cmin[y]==h-1){gates.push_back({elig,y});active++;}
    }
    bool lowerEmpty=true,closingFull=true;for(int w=0;w<WORDS;w++){lowerEmpty&=lower[w]==0;closingFull&=closing[w]==fullmask[cc][w];}
    R.terminal_cycles++;R.terminal_states+=1LL<<cc;R.lower_gate_nonempty+=!lowerEmpty;R.closing_gate_notfull+=!closingFull;
    R.min_active=min(R.min_active,active);R.max_active=max(R.max_active,active);R.total_active+=active;
    int minmult=K,maxmult=0;
    for(int root=0;root<(1<<cc);root++){
      int mult=0; long long capacity_sum=0;
      for(auto const&g:gates) if((g.elig[root>>6]>>(root&63))&1ULL){
        mult++;
        capacity_sum += 1LL<<infos[g.target].components;
      }
      minmult=min(minmult,mult);maxmult=max(maxmult,mult);
      if(mult==0) continue;
      for(auto const&g:gates) if((g.elig[root>>6]>>(root&63))&1ULL){
        long double term=1.0L/(long double)capacity_sum;
        long double term_lo=nextafterl(term,-numeric_limits<long double>::infinity());
        long double term_hi=nextafterl(term, numeric_limits<long double>::infinity());
        reverse_lower[g.target]=nextafterl(reverse_lower[g.target]+term_lo,
          -numeric_limits<long double>::infinity());
        reverse_upper[g.target]=nextafterl(reverse_upper[g.target]+term_hi,
           numeric_limits<long double>::infinity());
        raw_incoming[g.target]++;
      }
    }
    R.min_root=min(R.min_root,minmult);R.max_root=max(R.max_root,maxmult);R.total_minroot+=minmult;
  }
  int floatingBest=-1, floatingSecond=-1;
  long double bestLower=0;
  for(int y=0;y<NC;y++){
    R.max_raw_incoming_labels=max(R.max_raw_incoming_labels,raw_incoming[y]);
    if(reverse_lower[y]>1.0L){R.overloaded_target_cycles++;R.overloaded_signed_columns+=1LL<<infos[y].components;}
    if(floatingBest<0||reverse_lower[y]>reverse_lower[floatingBest]){
      floatingSecond=floatingBest;floatingBest=y;
    }else if(floatingSecond<0||reverse_lower[y]>reverse_lower[floatingSecond]) floatingSecond=y;
    bestLower=max(bestLower,reverse_lower[y]);
  }
  R.reverse_decimal=reverse_lower[floatingBest];
  R.second_decimal=floatingSecond>=0?reverse_lower[floatingSecond]:0;

  // Outward-rounded intervals enclose every exact positive sum.  A target is
  // retained precisely when its upper endpoint can still meet the largest
  // lower endpoint; all retained targets are recomputed as exact rationals.
  vector<int> candidates;
  for(int y=0;y<NC;y++) if(reverse_upper[y]>=bestLower)candidates.push_back(y);
  vector<int> candidate_position(NC,-1);
  for(int i=0;i<(int)candidates.size();i++)candidate_position[candidates[i]]=i;
  vector<map<long long,long long>> denominator_counts(candidates.size());
  for(int x=0;x<NC;x++)if(cmin[x]==h){
    int cc=infos[x].components;
    vector<Gate> gates;
    for(int ti=0;ti<K;ti++){
      int y=neighbour[(size_t)x*K+ti];if(y<0||cmin[y]!=h-1)continue;auto T=triples[ti];
      array<uint64_t,MAXW> elig{};bool nonempty=false;
      for(int w=0;w<WORDS;w++){
        elig[w]=ownerbits[obase(x,T[0])+w]|ownerbits[obase(x,T[1])+w]|ownerbits[obase(x,T[2])+w];
        nonempty|=elig[w]!=0;
      }
      if(nonempty)gates.push_back({elig,y});
    }
    for(int root=0;root<(1<<cc);root++){
      long long capacity_sum=0;
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL)
        capacity_sum+=1LL<<infos[g.target].components;
      if(!capacity_sum)continue;
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL){
        int pos=candidate_position[g.target];
        if(pos>=0)denominator_counts[pos][capacity_sum]++;
      }
    }
  }
  using boost::multiprecision::cpp_int;
  auto gcd_big=[](cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;};
  auto exact_sum=[&](map<long long,long long> const& counts){
    cpp_int num=0,den=1;
    for(auto [d,c]:counts){
      cpp_int g=gcd_big(den,cpp_int(d));
      cpp_int newden=den/g*d;
      num=num*(newden/den)+cpp_int(c)*(newden/d);
      den=newden;
      cpp_int z=gcd_big(num,den);num/=z;den/=z;
    }
    return pair<cpp_int,cpp_int>{num,den};
  };
  cpp_int bestNum=0,bestDen=1;int bestIndex=-1;long long ties=0;
  for(int i=0;i<(int)candidates.size();i++){
    auto [num,den]=exact_sum(denominator_counts[i]);
    cpp_int left=num*bestDen,right=bestNum*den;
    if(bestIndex<0||left>right){bestNum=num;bestDen=den;bestIndex=candidates[i];ties=1;}
    else if(left==right)ties++;
  }
  R.reverse_num=uint256_t(bestNum);R.reverse_den=uint256_t(bestDen);
  R.reverse_target_components=infos[bestIndex].components;
  R.reverse_target_cycles_tied=ties;

  // A two-scale envelope separates the low-normalizer harmonic tail from the
  // high-normalizer bulk.  For threshold T=2^(m+5), terms with Z<T are kept
  // exactly, while every term with Z>=T is bounded by 1/T.
  const long long threshold=1LL<<(m+5);
  vector<long double> env_lower(NC,0.0L),env_upper(NC,0.0L);
  vector<long long> env_high(NC,0),env_low_count(NC,0);
  for(int x=0;x<NC;x++)if(cmin[x]==h){
    int cc=infos[x].components;
    vector<Gate> gates;
    for(int ti=0;ti<K;ti++){
      int y=neighbour[(size_t)x*K+ti];if(y<0||cmin[y]!=h-1)continue;auto T=triples[ti];
      array<uint64_t,MAXW> elig{};bool nonempty=false;
      for(int w=0;w<WORDS;w++){
        elig[w]=ownerbits[obase(x,T[0])+w]|ownerbits[obase(x,T[1])+w]|ownerbits[obase(x,T[2])+w];
        nonempty|=elig[w]!=0;
      }
      if(nonempty)gates.push_back({elig,y});
    }
    for(int root=0;root<(1<<cc);root++){
      long long capacity_sum=0;
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL)
        capacity_sum+=1LL<<infos[g.target].components;
      if(!capacity_sum)continue;
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL){
        if(capacity_sum<threshold){
          long double term=1.0L/(long double)capacity_sum;
          env_lower[g.target]=nextafterl(env_lower[g.target]+nextafterl(term,-numeric_limits<long double>::infinity()),-numeric_limits<long double>::infinity());
          env_upper[g.target]=nextafterl(env_upper[g.target]+nextafterl(term, numeric_limits<long double>::infinity()), numeric_limits<long double>::infinity());

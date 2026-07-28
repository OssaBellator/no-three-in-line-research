    long long cumulative=0;
    for(int i=1;i<=720;i++){
      cumulative+=total.hist[i];
      if(cumulative>=threshold) return i;
    }
    return 720;
  };

  struct TrancheAcc{long long flaws=0,proper=0;long long wp=0,wq=1,gp=0,gq=1,pp=1,pq=1,sp=0,sq=1,srp=0,srq=1;int maxCuts=0,wSources=0,wSubset=0,sSources=0;long long wSupply=0,wCapacity=1;Candidate worst{},supportWorst{};};
  auto fracgt=[](long long a,long long b,long long c,long long d){return boost::multiprecision::int128_t(a)*d>boost::multiprecision::int128_t(c)*b;};
  vector<char> meet(K*K,0);for(int s=0;s<K;s++)for(int t=0;t<K;t++)for(int a:triples[s])for(int b:triples[t])if(a==b)meet[s*K+t]=1;
  vector<TrancheAcc> tracc(threads);
#pragma omp parallel for schedule(dynamic,1)
  for(int ix=0;ix<(int)cand.size();ix++){
    int tid=0;
#ifdef _OPENMP
    tid=omp_get_thread_num();
#endif
    auto c=cand[ix];auto S=triples[c.s];auto const&raw=lists[key(c.s,c.ta,c.tb,c.tc)];vector<int>sources,weights;sources.reserve(720);weights.reserve(720);
    for(int ci:raw){if(!info[ci].clean)continue;array<int8_t,M>root;root.fill(-1);bool okc=true;int distinct=0;for(int k=0;k<3;k++){int owner=S[k],co=info[ci].comp[owner],value=((c.mask>>k)&1)^info[ci].colour[owner];if(root[co]<0){root[co]=value;distinct++;}else if(root[co]!=value)okc=false;}if(okc){sources.push_back(ci);weights.push_back(1<<(info[ci].components-distinct));}}
    if(sources.empty())continue;
    vector<vector<int>>nbr(sources.size());vector<int>all;all.reserve(61200);
    for(int i=0;i<(int)sources.size();i++){
      auto &v=nbr[i];v.reserve(85);
      for(int t=0;t<K;t++)if(meet[c.s*K+t]){Rho rr=rhos[sources[i]];auto T=triples[t];array<int,3>cyc{};int f=0,cur=min({T[0],T[1],T[2]});for(int z=0;z<M;z++){if(cur==T[0]||cur==T[1]||cur==T[2])cyc[f++]=cur;cur=rr[cur];}Rho o=rr;o[cyc[0]]=rr[cyc[1]];o[cyc[1]]=rr[cyc[2]];o[cyc[2]]=rr[cyc[0]];int y=id[o];if(info[y].clean)v.push_back(y);}
      sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());all.insert(all.end(),v.begin(),v.end());
    }
    sort(all.begin(),all.end());all.erase(unique(all.begin(),all.end()),all.end());vector<int>caps;caps.reserve(all.size());for(int y:all)caps.push_back(1<<info[y].components);vector<int>pos(C,-1);Ratio r=optimum_ratio(weights,nbr,all,caps,pos);
    long long gs=accumulate(weights.begin(),weights.end(),0LL),gc=accumulate(caps.begin(),caps.end(),0LL),d=gcd(gs,gc),gp=gs/d,gq=gc/d;
    auto &a=tracc[tid];a.flaws+=2;a.maxCuts=max(a.maxCuts,r.cuts);if(fracgt(r.p,r.q,a.wp,a.wq)){a.wp=r.p;a.wq=r.q;a.worst=c;a.wSources=sources.size();a.wSubset=r.subset;a.wSupply=r.supply;a.wCapacity=r.capacity;}long long sp=r.p*(long long)sources.size(),sq=r.q;d=gcd(sp,sq);sp/=d;sq/=d;if(fracgt(sp,sq,a.sp,a.sq)){a.sp=sp;a.sq=sq;a.srp=r.p;a.srq=r.q;a.supportWorst=c;a.sSources=sources.size();}if(fracgt(gp,gq,a.gp,a.gq)){a.gp=gp;a.gq=gq;}if(fracgt(r.p,r.q,gp,gq)){a.proper+=2;long long pp=r.p*gq,pq=r.q*gp;d=gcd(pp,pq);pp/=d;pq/=d;if(fracgt(pp,pq,a.pp,a.pq)){a.pp=pp;a.pq=pq;}}
  }
  TrancheAcc tranche;for(auto const&a:tracc){tranche.flaws+=a.flaws;tranche.proper+=a.proper;tranche.maxCuts=max(tranche.maxCuts,a.maxCuts);if(fracgt(a.wp,a.wq,tranche.wp,tranche.wq)){tranche.wp=a.wp;tranche.wq=a.wq;tranche.worst=a.worst;tranche.wSources=a.wSources;tranche.wSubset=a.wSubset;tranche.wSupply=a.wSupply;tranche.wCapacity=a.wCapacity;}if(fracgt(a.sp,a.sq,tranche.sp,tranche.sq)){tranche.sp=a.sp;tranche.sq=a.sq;tranche.srp=a.srp;tranche.srq=a.srq;tranche.supportWorst=a.supportWorst;tranche.sSources=a.sSources;}if(fracgt(a.gp,a.gq,tranche.gp,tranche.gq)){tranche.gp=a.gp;tranche.gq=a.gq;}if(fracgt(a.pp,a.pq,tranche.pp,tranche.pq)){tranche.pp=a.pp;tranche.pq=a.pq;}}
  const long long expectedFlaws[10]={0,0,0,0,52,368,1692,5100,12048,25540};
  const long long expectedProper[10]={0,0,0,0,0,0,884,4864,11952,25520};
  const int expectedMinSources[10]={0,0,0,0,1,1,1,1,2,17};
  const int expectedMaxSources[10]={0,0,0,0,1,1,2,6,24,120};
  const long long expectedWorstP[10]={0,0,0,0,1,1,4,12,1,223};
  const long long expectedWorstQ[10]={1,1,1,1,24,37,215,931,93,29271};
  const long long expectedSupportP[10]={0,0,0,0,1,1,8,72,192,83040};
  const long long expectedSupportQ[10]={1,1,1,1,24,37,215,931,745,96029};
  const int expectedSupportSources[10]={0,0,0,0,1,1,2,6,24,120};
  bool ok=M>=4&&M<=9&&total.flaws==expectedFlaws[M]&&tranche.flaws==expectedFlaws[M]&&
    tranche.proper==expectedProper[M]&&minSources==expectedMinSources[M]&&
    total.maxSources==expectedMaxSources[M]&&tranche.wp==expectedWorstP[M]&&
    tranche.wq==expectedWorstQ[M]&&tranche.sp==expectedSupportP[M]&&
    tranche.sq==expectedSupportQ[M]&&tranche.sSources==expectedSupportSources[M];
  if(!ok){cerr<<"compressed inverse-source regression mismatch at m="<<M<<"\n";return 2;}
  auto B=total.best.c;auto S=triples[B.s];
  auto TW=tranche.worst;auto TS=triples[TW.s];
  auto SW=tranche.supportWorst;auto SS=triples[SW.s];
  cout<<"{\n  \"m\":"<<M<<",\n  \"hamilton_cycles\":"<<C<<",\n  \"parity_satisfiable_cycles\":"<<cleanCycles<<",\n  \"clean_signed_states\":"<<cleanStates<<",\n  \"nonempty_three_arc_keys\":"<<nonemptyArcKeys<<",\n  \"maximum_raw_source_cycles_per_arc_assignment\":"<<maxRaw<<",\n  \"complement_reduced_geometric_candidates\":"<<cand.size()<<",\n  \"atomic_signed_assignment_flaws_with_clean_sources\":"<<total.flaws<<",\n  \"compatible_source_cycles_range\":["<<minSources<<","<<total.maxSources<<"],\n  \"compatible_source_cycle_quantiles\":{\"25_percent\":"<<quantile(1,4)<<",\"median\":"<<quantile(1,2)<<",\"75_percent\":"<<quantile(3,4)<<",\"90_percent\":"<<quantile(9,10)<<",\"99_percent\":"<<quantile(99,100)<<"},\n  \"flaws_with_all_720_source_cycles\":"<<total.hist[720]<<",\n  \"total_flaw_source_cycle_incidences\":"<<total.incidences<<",\n  \"total_flaw_source_signed_weight\":"<<total.supply<<",\n  \"maximum_single_flaw_source_signed_weight\":"<<total.best.supply<<",\n  \"maximum_weight_flaw_source_cycles\":"<<total.best.sources<<",\n  \"maximum_weight_flaw_source_owners\":["<<S[0]<<","<<S[1]<<","<<S[2]<<"],\n  \"maximum_weight_flaw_targets\":["<<int(B.ta)<<","<<int(B.tb)<<","<<int(B.tc)<<"],\n  \"maximum_weight_flaw_orientations\":["<<int(B.mask&1)<<","<<int((B.mask>>1)&1)<<",0],\n  \"full_audit_signed_flaws\":"<<tranche.flaws<<",\n  \"full_audit_proper_bottlenecks\":"<<tranche.proper<<",\n  \"full_audit_worst_charge\":\""<<tranche.wp<<"/"<<tranche.wq<<"\",\n  \"full_audit_max_support_normalized_charge\":\""<<tranche.sp<<"/"<<tranche.sq<<"\",\n  \"full_audit_max_support_normalized_source_count\":"<<tranche.sSources<<",\n  \"full_audit_max_support_normalized_raw_charge\":\""<<tranche.srp<<"/"<<tranche.srq<<"\",\n  \"full_audit_max_support_normalized_source_owners\":["<<SS[0]<<","<<SS[1]<<","<<SS[2]<<"],\n  \"full_audit_max_support_normalized_targets\":["<<int(SW.ta)<<","<<int(SW.tb)<<","<<int(SW.tc)<<"],\n  \"full_audit_max_support_normalized_orientations\":["<<int(SW.mask&1)<<","<<int((SW.mask>>1)&1)<<",0],\n  \"full_audit_worst_global_ratio\":\""<<tranche.gp<<"/"<<tranche.gq<<"\",\n  \"full_audit_max_merging_penalty\":\""<<tranche.pp<<"/"<<tranche.pq<<"\",\n  \"full_audit_max_dinkelbach_cuts\":"<<tranche.maxCuts<<",\n  \"full_audit_worst_flaw_source_owners\":["<<TS[0]<<","<<TS[1]<<","<<TS[2]<<"],\n  \"full_audit_worst_flaw_targets\":["<<int(TW.ta)<<","<<int(TW.tb)<<","<<int(TW.tc)<<"],\n  \"full_audit_worst_flaw_orientations\":["<<int(TW.mask&1)<<","<<int((TW.mask>>1)&1)<<",0],\n  \"full_audit_worst_subset_size\":"<<tranche.wSubset<<",\n  \"full_audit_worst_supply\":"<<tranche.wSupply<<",\n  \"full_audit_worst_capacity\":"<<tranche.wCapacity<<",\n  \"three_arc_factorial_compression_verified\":true,\n  \"full_weighted_hall_mincuts_completed\":true\n}\n";
}

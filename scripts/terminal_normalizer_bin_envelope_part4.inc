      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL)
        capacity_sum+=1LL<<infos[g.target].components;
      if(!capacity_sum)continue;
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL){
        if(capacity_sum<threshold){
          long double term=1.0L/(long double)capacity_sum;
          env_lower[g.target]=nextafterl(env_lower[g.target]+nextafterl(term,-numeric_limits<long double>::infinity()),-numeric_limits<long double>::infinity());
          env_upper[g.target]=nextafterl(env_upper[g.target]+nextafterl(term, numeric_limits<long double>::infinity()), numeric_limits<long double>::infinity());
          env_low_count[g.target]++;
        }else env_high[g.target]++;
      }
    }
  }
  long double env_best_lower=0;
  for(int y=0;y<NC;y++){
    long double bulk=(long double)env_high[y]/threshold;
    env_lower[y]=nextafterl(env_lower[y]+nextafterl(bulk,-numeric_limits<long double>::infinity()),-numeric_limits<long double>::infinity());
    env_upper[y]=nextafterl(env_upper[y]+nextafterl(bulk, numeric_limits<long double>::infinity()), numeric_limits<long double>::infinity());
    env_best_lower=max(env_best_lower,env_lower[y]);
  }
  vector<int> env_candidates;
  for(int y=0;y<NC;y++)if(env_upper[y]>=env_best_lower)env_candidates.push_back(y);
  vector<int> env_pos(NC,-1);
  for(int i=0;i<(int)env_candidates.size();i++)env_pos[env_candidates[i]]=i;
  vector<map<long long,long long>> env_counts(env_candidates.size());
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
      if(!capacity_sum||capacity_sum>=threshold)continue;
      for(auto const&g:gates)if((g.elig[root>>6]>>(root&63))&1ULL){
        int pos=env_pos[g.target];if(pos>=0)env_counts[pos][capacity_sum]++;
      }
    }
  }
  cpp_int envBestNum=0,envBestDen=1;int envBest=-1;long long envTies=0;
  for(int i=0;i<(int)env_candidates.size();i++){
    auto [num,den]=exact_sum(env_counts[i]);
    int y=env_candidates[i];
    cpp_int bulkNum=env_high[y],bulkDen=threshold;
    cpp_int newDen=den/gcd_big(den,bulkDen)*bulkDen;
    num=num*(newDen/den)+bulkNum*(newDen/bulkDen);den=newDen;
    cpp_int z=gcd_big(num,den);num/=z;den/=z;
    cpp_int left=num*envBestDen,right=envBestNum*den;
    if(envBest<0||left>right){envBestNum=num;envBestDen=den;envBest=y;envTies=1;}
    else if(left==right)envTies++;
  }
  R.envelope_num=uint256_t(envBestNum);R.envelope_den=uint256_t(envBestDen);
  R.envelope_decimal=env_lower[envBest];R.envelope_threshold=threshold;
  R.envelope_low_labels=env_low_count[envBest];R.envelope_high_labels=env_high[envBest];
  R.envelope_target_components=infos[envBest].components;
  R.envelope_target_cycles_tied=envTies;
  return R;
}

int main(int argc,char**argv){
  int first=8,last=10;if(argc>1)first=last=atoi(argv[1]);
  const long long expectedMin[11]={0,0,0,0,0,0,0,0,1096,2976,9872};
  const long long expectedMax[11]={0,0,0,0,0,0,0,0,7056,28160,85248};
  const int expectedBins[11]={0,0,0,0,0,0,0,0,3,4,4};
  const long long expectedCounts[11][5]={
    {},{},{},{},{},{},{},{},
    {96,672,1344,0,0},
    {32,616,5376,4864,0},
    {128,1344,6656,6144,0}
  };
  const long long expectedNum[11]={0,0,0,0,0,0,0,0,285067172,18995653877059LL,8507693248751944LL};
  const long long expectedDen[11]={1,1,1,1,1,1,1,1,383360387,17049712431135LL,21711076395041385LL};
  const long long expectedCorrNum[11]={0,0,0,0,0,0,0,0,203200918,148937290752LL,7972033929088LL};
  const long long expectedCorrDen[11]={1,1,1,1,1,1,1,1,383360387,183330241195LL,35188130299905LL};
  const long long expectedCorrCounts[11][5]={
    {},{},{},{},{},{},{},{},
    {16,384,1344,0,0},
    {0,256,5376,1536,0},
    {0,896,4096,3072,0}
  };
  const int expectedCorrComponents[11]={0,0,0,0,0,0,0,0,8,8,9};
  const char* expectedExactNum[11]={"0","0","0","0","0","0","0","0",
    "1468416446839930521721999",
    "406616023430754819367780545483294984597292560691",
    "5252950050653541320261353842660696885393101"};
  const char* expectedExactDen[11]={"1","1","1","1","1","1","1","1",
    "3789940340738886748063650",
    "708943793924084504981546740829982708967717363200",
    "33843848222070502440710524758866309866934400"};
  cout<<setprecision(17)<<"{\n  \"cases\": [\n";
  for(int m=first;m<=last;m++){
    Result r=run_case(m);
    bool ok=r.normalizer_min==expectedMin[m]&&r.normalizer_max==expectedMax[m]&&
      r.normalizer_bin_count==expectedBins[m]&&r.bin_envelope_num==expectedNum[m]&&
      r.bin_envelope_den==expectedDen[m]&&r.correlated_bin_num==uint256_t(expectedCorrNum[m])&&
      r.correlated_bin_den==uint256_t(expectedCorrDen[m])&&
      r.correlated_bin_target_components==expectedCorrComponents[m]&&
      r.correlated_bin_target_cycles_tied==2&&r.reverse_num==uint256_t(expectedExactNum[m])&&
      r.reverse_den==uint256_t(expectedExactDen[m]);
    for(int j=0;j<r.normalizer_bin_count;j++)
      ok=ok&&r.maximum_target_labels_in_bin[j]==expectedCounts[m][j]&&
        r.correlated_bin_counts[j]==expectedCorrCounts[m][j];
    if(!ok){cerr<<"terminal normalizer-bin regression mismatch at m="<<m<<"\n";return 2;}
    cout<<"    {\"m\":"<<m
        <<",\"normalizer_range\":["<<r.normalizer_min<<","<<r.normalizer_max<<"]"
        <<",\"bins\":[";
    for(int j=0;j<r.normalizer_bin_count;j++){
      cout<<"{\"lower\":"<<r.normalizer_bin_lower[j]
          <<",\"upper\":"<<r.normalizer_bin_upper[j]
          <<",\"maximum_target_labels\":"<<r.maximum_target_labels_in_bin[j]<<"}"
          <<(j+1<r.normalizer_bin_count?",":"");
    }
    cout<<"],\"bin_envelope\":\""<<r.bin_envelope_num<<"/"<<r.bin_envelope_den<<"\""
        <<",\"bin_envelope_decimal\":"<<(double)r.bin_envelope_num/r.bin_envelope_den
        <<",\"bin_envelope_contractive\":"<<(r.bin_envelope_num<r.bin_envelope_den?"true":"false")
        <<",\"correlated_bin_envelope\":\""<<r.correlated_bin_num<<"/"<<r.correlated_bin_den<<"\""
        <<",\"correlated_bin_envelope_decimal\":"<<(long double)r.correlated_bin_num.convert_to<long double>()/r.correlated_bin_den.convert_to<long double>()
        <<",\"correlated_bin_counts\":[";
    for(int j=0;j<r.normalizer_bin_count;j++)cout<<r.correlated_bin_counts[j]<<(j+1<r.normalizer_bin_count?",":"");
    cout<<"]"
        <<",\"correlated_bin_target_components\":"<<r.correlated_bin_target_components
        <<",\"correlated_bin_target_cycles_tied\":"<<r.correlated_bin_target_cycles_tied
        <<",\"exact_capacity_weighted_maximum\":\""<<r.reverse_num<<"/"<<r.reverse_den<<"\""
        <<",\"exact_capacity_weighted_maximum_decimal\":"<<(double)r.reverse_decimal
        <<"}"<<(m<last?",":"")<<"\n";
  }
  cout<<"  ],\n"
      <<"  \"bins_are_disjoint_integer_normalizer_intervals\": true,\n"
      <<"  \"bin_bound_uses_maximum_target_population_divided_by_bin_lower_edge\": true,\n"
      <<"  \"m8_bin_certificate_below_three_quarters\": true,\n"
      <<"  \"m9_independent_bin_certificate_contractive\": false,\n"
      <<"  \"all_correlated_bin_envelopes_contractive\": true,\n"
      <<"  \"m8_correlated_bin_certificate_below_eight_fifteenths\": true,\n"
      <<"  \"m9_correlated_bin_certificate_below_thirteen_sixteenths\": true,\n"
      <<"  \"m10_correlated_bin_certificate_below_one_quarter\": true,\n"
      <<"  \"m10_bin_certificate_below_two_fifths\": true,\n"
      <<"  \"asymptotic_bin_population_bound_proved\": false,\n"
      <<"  \"all_exact_regressions_verified\": true\n"
      <<"}\n";
}

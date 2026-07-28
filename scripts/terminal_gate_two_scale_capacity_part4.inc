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
      if(nonempty)gates.push_back({eligy,y});
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
  const int expectedH[11]={0,0,0,0,0,0,0,0,0,3,4,5};
  const long long expectedCycles[11]={0,0,0,0,0,0,0,0,436,2298,1260};
  const long long expectedStates[11]={0,0,0,0,0,0,0,0,33624,478040,535072};
  const char* expectedNum[11]={"0","0","0","0","0","0","0","0",
    "1468416446839930521721999",
    "406616023430754819367780545483294984597292560691",
    "5252950050653541320261353842660696885393101"};
  const char* expectedDen[11]={"1","1","1","1","1","1","1","1",
    "3789940340738886748063650",
    "708943793924084504981546740829982708967717363200",
    "33843848222070502440710524758866309866934400"};
  const long long expectedRaw[11]={0,0,0,0,0,0,0,0,1744,8574,8960};
  const int expectedComp[11]={0,0,0,0,0,0,0,0,8,8,9};
  const char* expectedEnvNum[11]={"0","0","0","0","0","0","0","0",
    "1468416446839930521721999",
    "80380644898328654826210429323",
    "17257"};
  const char* expectedEnvDen[11]={"1","1","1","1","1","1","1","1",
    "3789940340738886748063650",
    "137462767954375595411229359040",
    "63040"};
  const long long expectedThreshold[11]={0,0,0,0,0,0,0,0,8192,16384,32768};
  const long long expectedLow[11]={0,0,0,0,0,0,0,0,1744,4222,256};
  const long long expectedHigh[11]={0,0,0,0,0,0,0,0,0,4352,8704};
  const int expectedEnvComp[11]={0,0,0,0,0,0,0,0,8,9,10};
  cout<<setprecision(17)<<"{\n  \"cases\": [\n";
  for(int m=first;m<=last;m++){
    Result r=run_case(m);
    bool ok=!r.unreached&&!r.lower_gate_nonempty&&!r.closing_gate_notfull&&
      r.max_distance==expectedH[m]&&r.terminal_cycles==expectedCycles[m]&&
      r.terminal_states==expectedStates[m]&&
      r.reverse_num==uint256_t(expectedNum[m])&&r.reverse_den==uint256_t(expectedDen[m])&&
      r.max_raw_incoming_labels==expectedRaw[m]&&
      r.reverse_target_components==expectedComp[m]&&r.reverse_target_cycles_tied==2&&
      r.overloaded_target_cycles==0&&r.overloaded_signed_columns==0&&
      r.envelope_num==uint256_t(expectedEnvNum[m])&&
      r.envelope_den==uint256_t(expectedEnvDen[m])&&
      r.envelope_threshold==expectedThreshold[m]&&
      r.envelope_low_labels==expectedLow[m]&&r.envelope_high_labels==expectedHigh[m]&&
      r.envelope_target_components==expectedEnvComp[m]&&
      r.envelope_target_cycles_tied==2;
    if(!ok){cerr<<"capacity-weighted terminal ledger mismatch at m="<<m<<"\n";return 2;}
    cout<<"    {\"m\":"<<m
        <<",\"maximum_distance\":"<<r.max_distance
        <<",\"terminal_cycles\":"<<r.terminal_cycles
        <<",\"terminal_states\":"<<r.terminal_states
        <<",\"capacity_weighted_maximum_regenerated_reverse_load\":\""<<r.reverse_num<<"/"<<r.reverse_den<<"\""
        <<",\"capacity_weighted_maximum_decimal\":"<<(double)r.reverse_decimal
        <<",\"maximum_raw_incoming_terminal_labels\":"<<r.max_raw_incoming_labels
        <<",\"maximizing_target_components\":"<<r.reverse_target_components
        <<",\"maximizing_target_cycles_tied\":"<<r.reverse_target_cycles_tied
        <<",\"overloaeded_target_cycles\":"<<r.overloaded_target_cycles
        <<",\"overloaeded_signed_columns\":"<<r.overloaded_signed_columns
        <<",\"two_scale_threshold\":"<<r.envelope_threshold
        <<",\"two_scale_envelope\":\""<<r.envelope_num<<"/"<<r.envelope_den<<"\""
        <<",\"two_scale_envelope_decimal\":"<<(double)r.envelope_decimal
        <<",\"two_scale_maximizer_low_labels\":"<<r.envelope_low_labels
        <<",\"two_scale_maximizer_high_labels\":"<<r.envelope_high_labels
        <<",\"two_scale_maximizing_target_components\":"<<r.envelope_target_components
        <<",\"two_scale_maximizing_target_cycles_tied\":"<<r.envelope_target_cycles_tied
        <<"}"<<(m<last?",":"")<<"\n";
  }
  cout<<"  ],\n"
      <<"  \"target_cycle_weight_proportional_to_fibre_size\": true,\n"
      <<"  \"capacity_weighted_terminal_policy_contracts\": true,\n"
      <<"  \"uniform_bound_through_m10\": \"3/5\",\n"
      <<"  \"two_scale_threshold_rule\": \"2^(m+5)\",\n"
      <<"  \"all_exact_regressions_verified\": true\n"
      <<"}\n";
}

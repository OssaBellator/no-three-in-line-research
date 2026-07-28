                  ownerbits[obase(x,T[2])+w];
        nonempty|=e.bits[w]!=0;
      }
      if(nonempty)td.edges.push_back(e);
    }
    for(auto const&e:td.edges){
      int target_fibre=1<<infos[e.target].components;
      for(int r=0;r<roots;r++)if((e.bits[r>>6]>>(r&63))&1ULL)
        td.z[r]+=target_fibre;
    }
    int terminal_index=terminal.size();
    for(int ei=0;ei<(int)td.edges.size();ei++)
      reverse[td.edges[ei].target].push_back({terminal_index,ei});
    for(int z:td.z){
      if(z<=0){cerr<<"terminal state without closing capacity\n";exit(5);}
      minZ=min(minZ,z);maxZ=max(maxZ,z);
    }
    terminal_states+=roots;closing_cycle_labels+=td.edges.size();
    terminal.push_back(move(td));
  }

  long long bestN=0,bestD=1;
  int bestC=0,bestT=1,bestComp=0,bestTies=0,maxTargetLabels=0,targetsIncoming=0;
  array<int,20> dyadic{};
  auto greater_fraction=[](long long a,long long b,long long c,long long d){
    return a*d>c*b;
  };

  for(int y=0;y<NC;y++)if(!reverse[y].empty()){
    vector<int> values;
    for(auto [terminal_index,edge_index]:reverse[y]){
      auto const&td=terminal[terminal_index];
      auto const&e=td.edges[edge_index];
      int roots=1<<td.cc;
      for(int r=0;r<roots;r++)if((e.bits[r>>6]>>(r&63))&1ULL)
        values.push_back(td.z[r]);
    }
    if(values.empty())continue;
    targetsIncoming++;incoming_signed_labels+=values.size();
    maxTargetLabels=max(maxTargetLabels,(int)values.size());
    sort(values.begin(),values.end());
    for(int k=0;k<(int)values.size();){
      int t=values[k],j=k;
      while(j<(int)values.size()&&values[j]==t)j++;
      long long c=j,n=c*c,d=t;
      if(greater_fraction(n,d,bestN,bestD)){
        bestN=n;bestD=d;bestC=c;bestT=t;bestComp=infos[y].components;bestTies=1;
      }else if(n*bestD==bestN*d){
        bestTies++;
      }
      k=j;
    }
    for(int p=0;p<20;p++){
      int threshold=1<<p;
      dyadic[p]=max(dyadic[p],int(upper_bound(values.begin(),values.end(),threshold)-values.begin()));
    }
  }

  long long boundN=4*bestN,boundD=bestD*minZ;
  long long g=gcd(boundN,boundD);boundN/=g;boundD/=g;
  ProfileResult R;R.m=m;R.cycles=C;R.clean_cycles=NC;R.clean_states=clean_states;
  R.valid_states=valid_states;R.unreached=clean_states-reached_total;
  R.distance=dist;R.max_distance=maxd;R.terminal_cycles=terminal.size();
  R.terminal_states=terminal_states;R.closing_cycle_labels=closing_cycle_labels;
  R.incoming_signed_labels=incoming_signed_labels;R.targets_with_incoming=targetsIncoming;
  R.min_normalizer=minZ;R.max_normalizer=maxZ;R.max_target_labels=maxTargetLabels;
  R.max_c_at_dyadic=dyadic;R.sqrt_num=bestN;R.sqrt_den=bestD;
  R.sqrt_c=bestC;R.sqrt_t=bestT;R.sqrt_target_components=bestComp;R.sqrt_ties=bestTies;
  R.bound_square_num=boundN;R.bound_square_den=boundD;
  return R;
}

int main(int argc,char**argv){
  int m=argc>1?atoi(argv[1]):10;
  ProfileResult r=run_case(m);
  bool ok=false;
  if(m==8){
    ok=r.cycles==5040&&r.clean_cycles==3542&&r.clean_states==404080&&r.valid_states==28&&
       r.unreached==0&&r.max_distance==3&&r.terminal_cycles==436&&r.terminal_states==33624&&
       r.closing_cycle_labels==13674&&r.incoming_signed_labels==1136332&&
       r.targets_with_incoming==2614&&r.min_normalizer==1096&&r.max_normalizer==7056&&
       r.max_target_labels==1744&&r.max_c_at_dyadic[11]==96&&r.max_c_at_dyadic[12]==688&&
       r.max_c_at_dyadic[13]==1744&&r.sqrt_c==1744&&r.sqrt_t==6384&&
       r.sqrt_num==3041536&&r.sqrt_den==6384&&r.bound_square_num==95048&&r.bound_square_den==54663;
  }else if(m==9){
    ok=r.cycles==40320&&r.clean_cycles==31688&&r.clean_states==6727728&&r.valid_states==8&&
       r.unreached==0&&r.max_distance==4&&r.terminal_cycles==2298&&r.terminal_states==478040&&
       r.closing_cycle_labels==128592&&r.incoming_signed_labels==28101044&&
       r.targets_with_incoming==22138&&r.min_normalizer==2976&&r.max_normalizer==28160&&
       r.max_target_labels==8574&&r.max_c_at_dyadic[12]==32&&r.max_c_at_dyadic[13]==616&&
       r.max_c_at_dyadic[14]==5632&&r.max_c_at_dyadic[15]==8574&&
       r.sqrt_c==8574&&r.sqrt_t==23584&&r.sqrt_num==73513476&&r.sqrt_den==23584&&
       r.bound_square_num==6126123&&r.bound_square_den==1462208;
  }else if(m==10){
    ok=r.cycles==362880&&r.clean_cycles==297886&&r.clean_states==115586396&&r.valid_states==12&&
       r.unreached==0&&r.max_distance==5&&r.terminal_cycles==1260&&r.terminal_states==535072&&
       r.closing_cycle_labels==123852&&r.incoming_signed_labels==55091040&&
       r.targets_with_incoming==65420&&r.min_normalizer==9872&&r.max_normalizer==85248&&
       r.max_target_labels==8960&&r.max_c_at_dyadic[14]==128&&r.max_c_at_dyadic[15]==1344&&
       r.max_c_at_dyadic[16]==6656&&r.max_c_at_dyadic[17]==8960&&
       r.sqrt_c==8960&&r.sqrt_t==85248&&r.sqrt_num==80281600&&r.sqrt_den==85248&&
       r.bound_square_num==78400&&r.bound_square_den==205461;
  }
  if(!ok){cerr<<"terminal normalizer-profile regression mismatch\n";return 2;}
  cout<<"{\n  \"m\":"<<r.m<<",\n  \"hamilton_cycles\":"<<r.cycles<<",\n"
      <<"  \"parity_satisfiable_cycles\":"<<r.clean_cycles<<",\n  \"clean_signed_states\":"<<r.clean_states<<",\n"
      <<"  \"line_valid_signed_states\":"<<r.valid_states<<",\n  \"maximum_distance\":"<<r.max_distance<<",\n"
      <<"  \"terminal_cycles\":"<<r.terminal_cycles<<",\n  \"terminal_states\":"<<r.terminal_states<<",\n"
      <<"  \"closing_cycle_labels\":"<<r.closing_cycle_labels<<",\n  \"incoming_signed_labels\":"<<r.incoming_signed_labels<<",\n"
      <<"  \"targets_with_incoming\":"<<r.targets_with_incoming<<",\n  \"normalizer_range\":["<<r.min_normalizer<<","<<r.max_normalizer<<"],\n"
      <<"  \"maximum_target_incoming_labels\":"<<r.max_target_labels<<",\n  \"dyadic_cumulative_maxima\":{";
  bool first=true;
  for(int p=0;p<20;p++)if(r.max_c_at_dyadic[p]&&(1<<p)>=r.min_normalizer&&(1<<p)<2*r.max_normalizer){
    if(!first)cout<<",";
    first=false;
    cout<<"\""<<(1<<p)<<"\":"<<r.max_c_at_dyadic[p];
  }
  cout<<"},\n  \"sqrt_profile_extremum\":{\"c\":"<<r.sqrt_c<<",\"t\":"<<r.sqrt_t
      <<",\"c2_over_t\":\""<<r.sqrt_num<<"/"<<r.sqrt_den
      <<"\",\"target_components\":"<<r.sqrt_target_components<<",\"ties\":"<<r.sqrt_ties<<"},\n"
      <<"  \"sqrt_layer_cake_bound_squared\":\""<<r.bound_square_num<<"/"<<r.bound_square_den<<"\",\n"
      <<"  \"sqrt_layer_cake_bound_is_contractive\":"<<(r.bound_square_num<r.bound_square_den?"true":"false")<<"\n}\n";
}

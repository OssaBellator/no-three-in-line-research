 bool ok=dist[0]==12&&
    dist[1]==205376&&
    dist[2]==5534564&&
    dist[3]==52044980&&
    dist[4]==57266392&&
    dist[5]==535072&&
    total.states==535072&&
    total.pairs==267536&&
    cycCount==1260&&
    fullFibres==1260&&
    minPer==16&&
    maxPer==1024&&
    total.minSup==2&&
    total.maxSup==47&&
    total.minAtom==8&&
    total.maxAtom==188&&
    memoCycles==15936&&
    total.witnesses.size()==8&&
    cycleCC==map<int,long long>{{4,6},{5,26},{6,86},{7,202},{8,340},{9,388},{10,212}}&&
    perDist==map<int,long long>{{16,6},{32,26},{64,86},{128,202},{256,340},{512,388},{1024,212}}&&
    total.sup==map<int,long long>{{2,16},{3,208},{4,1240},{5,3896},{6,9756},{7,18548},{8,30396},{9,42128},{10,51428},{11,55820},{12,55940},{13,50676},{14,43620},{15,36880},{16,30696},{17,24304},{18,18920},{19,15000},{20,11276},{21,7644},{22,5224},{23,3604},{24,2788},{25,2444},{26,2408},{27,2436},{28,2464},{29,1660},{30,1048},{31,752},{32,400},{33,192},{34,108},{35,52},{36,40},{37,44},{38,60},{39,164},{40,188},{41,200},{42,200},{43,92},{44,60},{45,36},{46,12},{47,4}}&&
    total.atom==map<int,long long>{{8,16},{12,196},{16,1196},{20,3720},{24,9504},{28,18040},{32,29544},{36,40724},{40,50076},{44,54784},{48,54876},{52,50732},{56,44212},{60,37468},{64,31592},{68,24648},{72,19428},{76,15276},{80,11716},{84,8120},{88,5764},{92,4144},{96,3292},{100,2532},{104,2524},{108,2408},{112,2396},{116,1868},{120,1220},{124,792},{128,616},{132,240},{136,196},{140,60},{144,60},{148,48},{152,44},{156,168},{160,188},{164,184},{168,200},{172,136},{176,40},{180,60},{184,20},{188,4}}&&
    total.cover==map<int,long long>{{1,168},{2,21640},{3,256256},{4,240504},{5,16376},{6,128}}&&
    total.cc==map<int,long long>{{4,96},{5,832},{6,5504},{7,25856},{8,87040},{9,198656},{10,217088}}&&
    total.rank==map<int,long long>{{0,535072}}&&
    minCorePeakS==map<int,long long>{{2,4},{3,12}}&&
    minCorePeakA==map<int,long long>{{8,4},{12,12}}&&
    minCoreJointPeak==map<pair<int,int>,long long>{{{2,8},4},{{3,12},12}}&&
    simultaneousMinima&&
    (total.witnesses[0].orientation==478&&total.witnesses[0].rho==array<int,M>{3,2,8,9,7,1,4,0,6,5}&&total.witnesses[0].supports==array<uint16_t,2>{522,784})&&
    (total.witnesses[1].orientation==293&&total.witnesses[1].rho==array<int,M>{3,4,9,1,5,7,2,8,6,0}&&total.witnesses[1].supports==array<uint16_t,2>{276,296})&&
    (total.witnesses[2].orientation==382&&total.witnesses[2].rho==array<int,M>{3,7,9,1,5,6,8,4,2,0}&&total.witnesses[2].supports==array<uint16_t,2>{22,164})&&
    (total.witnesses[3].orientation==209&&total.witnesses[3].rho==array<int,M>{7,2,6,9,1,3,8,4,5,0}&&total.witnesses[3].supports==array<uint16_t,2>{400,704})&&
    (total.witnesses[4].orientation==42&&total.witnesses[4].rho==array<int,M>{7,5,1,0,6,9,8,4,2,3}&&total.witnesses[4].supports==array<uint16_t,2>{548,224})&&
    (total.witnesses[5].orientation==311&&total.witnesses[5].rho==array<int,M>{9,3,6,0,1,4,8,5,7,2}&&total.witnesses[5].supports==array<uint16_t,2>{194,608})&&
    (total.witnesses[6].orientation==25&&total.witnesses[6].rho==array<int,M>{9,3,8,0,7,4,5,1,6,2}&&total.witnesses[6].supports==array<uint16_t,2>{592,672})&&
    (total.witnesses[7].orientation==402&&total.witnesses[7].rho==array<int,M>{9,4,1,5,7,8,2,0,6,3}&&total.witnesses[7].supports==array<uint16_t,2>{273,50});
 if(!ok){cerr<<"classification ledger mismatch\n";return 3;}
 cout<<"{\n  \"m\":10,\n  \"distance_five_states\":"<<total.states<<",\n  \"distance_five_complement_pairs\":"<<total.pairs<<",\n  \"distance_five_cycles\":"<<cycCount<<",\n  \"complete_fibres_in_distance_five_layer\":"<<fullFibres<<",\n  \"supporting_cycle_component_distribution\":";printmap(cycleCC);cout<<",\n  \"minimum_states_per_supporting_cycle\":"<<minPer<<",\n  \"maximum_states_per_supporting_cycle\":"<<maxPer<<",\n  \"states_per_cycle_distribution\":";printmap(perDist);cout<<",\n  \"flaw_support_distribution\":";printmap(total.sup);cout<<",\n  \"atomic_triple_distribution\":";printmap(total.atom);cout<<",\n  \"owner_cover_distribution\":";printmap(total.cover);cout<<",\n  \"parity_component_distribution\":";printmap(total.cc);cout<<",\n  \"parity_cyclomatic_rank_distribution\":";printmap(total.rank);cout<<",\n  \"minimum_flaw_supports\":"<<total.minSup<<",\n  \"maximum_flaw_supports\":"<<total.maxSup<<",\n  \"minimum_atomic_triples\":"<<total.minAtom<<",\n  \"maximum_atomic_triples\":"<<total.maxAtom<<",\n  \"minimum_core_shortest_peak_support_distribution\":";printmap(minCorePeakS);cout<<",\n  \"minimum_core_shortest_peak_atomic_distribution\":";printmap(minCorePeakA);cout<<",\n  \"minimum_core_shortest_joint_peak_distribution\":{\"2,8\":4,\"3,12\":12},\n  \"minimum_core_joint_minima_simultaneously_attained\":true,\n  \"barrier_recursion_cycles_evaluated\":"<<memoCycles<<",\n  \"minimum_core_complement_pair_representatives\":[";for(size_t i=0;i<total.witnesses.size();i++){auto &z=total.witnesses[i];if(i)cout<<",";cout<<"{\"orientation\":"<<z.orientation<<",\"rho\":[";for(int j=0;j<M;j++){if(j)cout<<",";cout<<z.rho[j];}cout<<"],\"support_masks\":["<<z.supports[0]<<","<<z.supports[1]<<"]}";}cout<<"],\n  \"complete_distance_five_classification_verified\":true,\n  \"shortest_path_collateral_barrier_computed\":true,\n  \"asymptotic_horizon_proved\":false\n}\n";
}

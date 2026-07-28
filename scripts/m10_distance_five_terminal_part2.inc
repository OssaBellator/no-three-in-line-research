 // cone of the eight minimum-core representatives.
 vector<vector<pair<int,int>>> paretoMemo(NC);
 vector<uint8_t> paretoDone(NC,0),paretoBusy(NC,0);
 auto prune=[](vector<pair<int,int>> v){
   sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());
   vector<pair<int,int>> out;
   for(auto p:v){
     bool dominated=false;
     for(auto q:v){
       if(q.first<=p.first&&q.second<=p.second&&(q.first<p.first||q.second<p.second)){
         dominated=true;break;
       }
     }
     if(!dominated)out.push_back(p);
   }
   return out;
 };
 function<const vector<pair<int,int>>& (int)> cyclePareto=
   [&](int x)->const vector<pair<int,int>>&{
     if(paretoDone[x])return paretoMemo[x];
     if(paretoBusy[x]){cerr<<"Pareto recursion dependency\n";exit(7);}
     paretoBusy[x]=1;int d=cmin[x];
     if(d==0){paretoMemo[x]={{0,0}};paretoDone[x]=1;paretoBusy[x]=0;return paretoMemo[x];}
     vector<pair<int,int>> cand;int ci=cleanCycle[x],roots=1<<info[x].cc;
     for(int r=0;r<roots;r++){
       if(!((layer[d][(size_t)x*W+(r>>6)]>>(r&63))&1))continue;
       int e=0;for(int o=0;o<M;o++)e|=((((r>>info[x].comp[o])&1)^info[x].colour[o])<<o);
       int sup=0,atom=0,owners=0;
       for(int ti=0;ti<K;ti++){
         auto T=triples[ti];int p=((e>>T[0])&1)|(((e>>T[1])&1)<<1)|(((e>>T[2])&1)<<2);
         int cnt=badcount[ib(ti,cycles[ci][T[0]],cycles[ci][T[1]],cycles[ci][T[2]])*8+p];
         if(cnt){sup++;atom+=cnt;owners|=(1<<T[0])|(1<<T[1])|(1<<T[2]);}
       }
       for(int ti=0;ti<K;ti++){
         auto T=triples[ti];int tm=(1<<T[0])|(1<<T[1])|(1<<T[2]);
         if(!(tm&owners))continue;
         int y=nei[(size_t)x*K+ti];
         if(y<0||cmin[y]!=d-1)continue;
         for(auto qv:cyclePareto(y))cand.push_back({max(sup,qv.first),max(atom,qv.second)});
       }
     }
     paretoMemo[x]=prune(move(cand));
     if(paretoMemo[x].empty()){cerr<<"missing shortest successor at cycle "<<x<<" d="<<d<<"\n";exit(8);}
     paretoDone[x]=1;paretoBusy[x]=0;return paretoMemo[x];
   };
 map<int,long long> minCorePeakS,minCorePeakA;
 map<pair<int,int>,long long> minCoreJointPeak;
 bool simultaneousMinima=true;
 for(auto &z:total.witnesses){
   int x=z.clean_index,e=z.orientation,ci=cleanCycle[x],owners=0;
   for(int ti=0;ti<K;ti++){
     auto T=triples[ti];int p=((e>>T[0])&1)|(((e>>T[1])&1)<<1)|(((e>>T[2])&1)<<2);
     if(badcount[ib(ti,cycles[ci][T[0]],cycles[ci][T[1]],cycles[ci][T[2]])*8+p])
       owners|=(1<<T[0])|(1<<T[1])|(1<<T[2]);
   }
   vector<pair<int,int>> cand;
   for(int ti=0;ti<K;ti++){
     auto T=triples[ti];int tm=(1<<T[0])|(1<<T[1])|(1<<T[2]);
     if(!(tm&owners))continue;
     int y=nei[(size_t)x*K+ti];
     if(y<0||cmin[y]!=4)continue;
     for(auto qv:cyclePareto(y))cand.push_back({max(2,qv.first),max(8,qv.second)});
   }
   auto pv=prune(move(cand));int bs=999,ba=99999;
   for(auto qv:pv){bs=min(bs,qv.first);ba=min(ba,qv.second);}
   bool joint=false;for(auto qv:pv)if(qv==make_pair(bs,ba))joint=true;
   simultaneousMinima&=joint;minCorePeakS[bs]+=2;minCorePeakA[ba]+=2;
   minCoreJointPeak[{bs,ba}]+=2;
 }
 int memoCycles=0;for(int x=0;x<NC;x++)if(paretoDone[x])memoCycles++;

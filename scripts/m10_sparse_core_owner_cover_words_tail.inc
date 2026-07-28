 // Exact owner-cover Pareto recursion for the sixteen-state minimum core.
 struct Peak3{int s,a,c;};
 auto p3less=[](Peak3 const&x,Peak3 const&y){return tie(x.s,x.a,x.c)<tie(y.s,y.a,y.c);};
 auto equal3=[](Peak3 const&x,Peak3 const&y){return x.s==y.s&&x.a==y.a&&x.c==y.c;};
 auto prune3=[&](vector<Peak3> v){
   sort(v.begin(),v.end(),p3less);v.erase(unique(v.begin(),v.end(),equal3),v.end());vector<Peak3> out;
   for(auto p:v){bool dom=false;for(auto q:v)if(q.s<=p.s&&q.a<=p.a&&q.c<=p.c&&(q.s<p.s||q.a<p.a||q.c<p.c)){dom=true;break;}if(!dom)out.push_back(p);}return out;
 };
 struct Stats{int s=0,a=0,c=0,owners=0;};
 auto stats=[&](int x,int r){
   Stats z;int ci=cleanCycle[x],e=0;for(int o=0;o<M;o++)e|=((((r>>info[x].comp[o])&1)^info[x].colour[o])<<o);array<uint16_t,120> sm{};int ns=0;
   for(int ti=0;ti<K;ti++){auto T=triples[ti];int p=((e>>T[0])&1)|(((e>>T[1])&1)<<1)|(((e>>T[2])&1)<<2);int cnt=badcount[ib(ti,cycles[ci][T[0]],cycles[ci][T[1]],cycles[ci][T[2]])*8+p];if(cnt){z.s++;z.a+=cnt;int mm=(1<<T[0])|(1<<T[1])|(1<<T[2]);sm[ns++]=mm;z.owners|=mm;}}
   if(ns){for(auto [k,mask]:masks){bool hit=true;for(int j=0;j<ns;j++)if(!(sm[j]&mask)){hit=false;break;}if(hit){z.c=k;break;}}}
   return z;
 };
 vector<vector<Peak3>> memo(NC);vector<uint8_t> done(NC),busy(NC);
 function<const vector<Peak3>&(int)> solve=[&](int x)->const vector<Peak3>&{
   if(done[x]) return memo[x];
   if(busy[x]){cerr<<"owner-cover recursion dependency\n";exit(20);}
   busy[x]=1;int d=cmin[x];
   if(d==0){memo[x]={{0,0,0}};done[x]=1;busy[x]=0;return memo[x];}
   vector<Peak3> cand;int roots=1<<info[x].cc;
   for(int r=0;r<roots;r++){if(!((layer[d][(size_t)x*W+(r>>6)]>>(r&63))&1))continue;Stats st=stats(x,r);for(int ti=0;ti<K;ti++){auto T=triples[ti];int tm=(1<<T[0])|(1<<T[1])|(1<<T[2]);if(!(tm&st.owners))continue;int y=nei[(size_t)x*K+ti];if(y<0||cmin[y]!=d-1)continue;for(auto q:solve(y))cand.push_back({max(st.s,q.s),max(st.a,q.a),max(st.c,q.c)});}}
   memo[x]=prune3(move(cand));if(memo[x].empty()){cerr<<"empty owner-cover recursion\n";exit(21);}done[x]=1;busy[x]=0;return memo[x];
 };
 struct PathState{int x,r,e,s,a,c;};struct Word{Peak3 bound;vector<int> masks;vector<PathState> states;};
 auto orientationOf=[&](int x,int r){int e=0;for(int o=0;o<M;o++)e|=((((r>>info[x].comp[o])&1)^info[x].colour[o])<<o);return e;};
 function<bool(int,Peak3,vector<PathState>&,vector<int>&)> buildPath=[&](int x,Peak3 b,vector<PathState>&states,vector<int>&word)->bool{
   int d=cmin[x],roots=1<<info[x].cc;for(int r=0;r<roots;r++){if(!((layer[d][(size_t)x*W+(r>>6)]>>(r&63))&1))continue;Stats st=stats(x,r);if(st.s>b.s||st.a>b.a||st.c>b.c)continue;states.push_back({x,r,orientationOf(x,r),st.s,st.a,st.c});if(d==0)return true;
     for(int ti=0;ti<K;ti++){auto T=triples[ti];int tm=(1<<T[0])|(1<<T[1])|(1<<T[2]);if(!(tm&st.owners))continue;int y=nei[(size_t)x*K+ti];if(y<0||cmin[y]!=d-1)continue;bool feasible=false;for(auto q:solve(y))if(q.s<=b.s&&q.a<=b.a&&q.c<=b.c){feasible=true;break;}if(!feasible)continue;word.push_back(tm);if(buildPath(y,b,states,word))return true;word.pop_back();}states.pop_back();}
   return false;
 };
 vector<vector<Peak3>> profiles;vector<vector<Word>> bank;
 for(auto const&z:total.witnesses){int x=z.clean_index;Stats st=stats(x,z.root);vector<Peak3> cand;for(int ti=0;ti<K;ti++){auto T=triples[ti];int tm=(1<<T[0])|(1<<T[1])|(1<<T[2]);if(!(tm&st.owners))continue;int y=nei[(size_t)x*K+ti];if(y<0||cmin[y]!=4)continue;for(auto q:solve(y))cand.push_back({max(st.s,q.s),max(st.a,q.a),max(st.c,q.c)});}auto pv=prune3(move(cand));profiles.push_back(pv);vector<Word> wb;
   for(auto b:pv){Word w;w.bound=b;w.states.push_back({x,z.root,z.orientation,st.s,st.a,st.c});bool found=false;for(int ti=0;ti<K&&!found;ti++){auto T=triples[ti];int tm=(1<<T[0])|(1<<T[1])|(1<<T[2]);if(!(tm&st.owners))continue;int y=nei[(size_t)x*K+ti];if(y<0||cmin[y]!=4)continue;bool feasible=false;for(auto q:solve(y))if(q.s<=b.s&&q.a<=b.a&&q.c<=b.c){feasible=true;break;}if(!feasible)continue;w.masks.push_back(tm);if(buildPath(y,b,w.states,w.masks))found=true;else w.masks.pop_back();}if(!found){cerr<<"word extraction failure\n";return 22;}wb.push_back(move(w));}bank.push_back(move(wb));
 }
 const vector<int> expectedOrient={478,293,382,209,42,311,25,402};
 const vector<vector<Peak3>> expectedProfiles={{{3,12,2}},{{3,12,2},{4,16,1}},{{3,12,1}},{{2,8,2}},{{3,12,2}},{{3,12,2},{4,16,1}},{{3,12,1}},{{2,8,2}}};
 const vector<vector<vector<int>>> expectedWords={{{13,50,896,88,577}},{{161,42,84,67,800},{259,200,7,577,276}},{{416,81,577,522,324}},{{290,131,784,133,74}},{{82,276,648,69,546}},{{81,552,262,592,273},{88,262,592,321,56}},{{84,296,289,386,529}},{{44,176,11,112,896}}};
 const vector<vector<vector<int>>> expectedTraces={{{478,379,526,235,163,235}},{{293,33,79,24,206,474},{293,289,223,335,10,267}},{{382,230,175,57,40,321}},{{209,58,42,64,790,321}},{{42,398,380,137,51,474}},{{311,510,333,432,772,235},{311,152,137,163,499,235}},{{25,57,57,46,132,474}},{{402,550,582,256,868,474}}};
 bool ok=total.witnesses.size()==8&&profiles.size()==8&&bank.size()==8;for(int i=0;i<8&&ok;i++){ok&=total.witnesses[i].orientation==expectedOrient[i]&&profiles[i].size()==expectedProfiles[i].size()&&bank[i].size()==expectedWords[i].size();for(size_t j=0;j<profiles[i].size()&&ok;j++){ok&=equal3(profiles[i][j],expectedProfiles[i][j])&&bank[i][j].masks==expectedWords[i][j]&&bank[i][j].states.size()==expectedTraces[i][j].size();for(size_t k=0;k<bank[i][j].states.size()&&ok;k++)ok&=bank[i][j].states[k].e==expectedTraces[i][j][k];}}
 if(!ok){cerr<<"sparse owner-cover word-bank regression mismatch\n";return 23;}
 cout<<"{\n  \"m\":10,\n  \"minimum_core_states\":16,\n  \"minimum_core_complement_pairs\":8,\n  \"pareto_profile_distribution\":{\"2,8,2\":4,\"3,12,1\":4,\"3,12,2\":4,\"tradeoff_3,12,2_or_4,16,1\":4},\n  \"states_with_star_local_shortest_path\":8,\n  \"states_requiring_owner_cover_two_on_every_shortest_path\":8,\n  \"states_paying_one_support_and_four_atoms_for_star_locality\":4,\n  \"canonical_words\":[";
 for(size_t i=0;i<bank.size();i++)for(size_t j=0;j<bank[i].size();j++){if(i||j)cout<<",";auto const&w=bank[i][j];cout<<"{\"orientation\":"<<total.witnesses[i].orientation<<",\"peak\":["<<w.bound.s<<","<<w.bound.a<<","<<w.bound.c<<"],\"triple_masks\":[";for(size_t k=0;k<w.masks.size();k++){if(k)cout<<",";cout<<w.masks[k];}cout<<"],\"orientation_trace\":[";for(size_t k=0;k<w.states.size();k++){if(k)cout<<",";cout<<w.states[k].e;}cout<<"]}";}
 cout<<"],\n  \"owner_cover_pareto_classification_verified\":true,\n  \"canonical_shortest_word_bank_verified\":true\n}\n";
}

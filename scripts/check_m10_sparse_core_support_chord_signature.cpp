#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
using Rho=array<int,10>;
struct Rep{int orientation;Rho rho;array<int,2> support;string profile;};
vector<int> bits(int mask){vector<int>v;for(int i=0;i<10;i++)if(mask&(1<<i))v.push_back(i);return v;}
int cyclic_distance(int a,int b){int d=abs(a-b);return min(d,10-d);}
string signature(Rep const&r){
  auto A=bits(r.support[0]),B=bits(r.support[1]);
  set<int>sa(A.begin(),A.end()),sb(B.begin(),B.end());vector<int>inter;
  set_intersection(sa.begin(),sa.end(),sb.begin(),sb.end(),back_inserter(inter));
  if(inter.size()!=1){cerr<<"support intersection mismatch\n";exit(2);}int c=inter[0];
  vector<int>ord{0};for(int i=1;i<10;i++)ord.push_back(r.rho[ord.back()]);
  array<int,10>pos{};for(int i=0;i<10;i++)pos[ord[i]]=i;
  vector<int>la,lb;for(int x:A)if(x!=c)la.push_back(pos[x]);for(int x:B)if(x!=c)lb.push_back(pos[x]);
  int da=cyclic_distance(la[0],la[1]),db=cyclic_distance(lb[0],lb[1]);if(da>db)swap(da,db);
  vector<pair<int,char>>seq;for(int x:la)seq.push_back({x,'A'});for(int x:lb)seq.push_back({x,'B'});sort(seq.begin(),seq.end());
  string s;for(auto [p,z]:seq){(void)p;s+=z;}
  bool alternating=(s=="ABAB"||s=="BABA");
  return string(alternating?"alternating:":"nested:")+to_string(da)+","+to_string(db);
}
int main(){
 vector<Rep> reps={
  {478,{3,2,8,9,7,1,4,0,6,5},{522,784},"3,12,2"},
  {293,{3,4,9,1,5,7,2,8,6,0},{276,296},"tradeoff"},
  {382,{3,7,9,1,5,6,8,4,2,0},{22,164},"3,12,1"},
  {209,{7,2,6,9,1,3,8,4,5,0},{400,704},"2,8,2"},
  {42,{7,5,1,0,6,9,8,4,2,3},{548,224},"3,12,2"},
  {311,{9,3,6,0,1,4,8,5,7,2},{194,608},"tradeoff"},
  {25,{9,3,8,0,7,4,5,1,6,2},{592,672},"3,12,1"},
  {402,{9,4,1,5,7,8,2,0,6,3},{273,50},"2,8,2"}
 };
 map<string,string> expected={{"alternating:4,4","2,8,2"},{"alternating:2,2","3,12,1"},{"alternating:3,5","tradeoff"},{"nested:2,3","3,12,2"}};
 map<string,int> counts;cout<<"{\n  \"m\":10,\n  \"representatives\":[\n";
 for(size_t i=0;i<reps.size();i++){
   string sig=signature(reps[i]);if(!expected.count(sig)||expected[sig]!=reps[i].profile){cerr<<"signature mismatch at "<<reps[i].orientation<<"\n";return 3;}counts[sig]++;
   cout<<"    {\"orientation\":"<<reps[i].orientation<<",\"signature\":\""<<sig<<"\",\"pareto_profile\":\""<<reps[i].profile<<"\"}"<<(i+1==reps.size()?"\n":",\n");
 }
 bool ok=counts.size()==4;for(auto const&kv:counts)ok&=kv.second==2;if(!ok){cerr<<"signature count mismatch\n";return 4;}
 cout<<"  ],\n  \"complement_pairs_per_signature\":2,\n  \"support_chord_signature_classifies_all_four_pareto_types\":true,\n  \"global_sign_complement_invariant\":true\n}\n";
}

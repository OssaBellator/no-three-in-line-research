#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
struct Pt{int x,y;};
inline bool col(Pt a,Pt b,Pt c){return 1LL*(b.x-a.x)*(c.y-a.y)==1LL*(b.y-a.y)*(c.x-a.x);}
int score(const vector<int>&P,const vector<int>&Q){int n=P.size(),s=0;vector<Pt>v;for(int r=0;r<n;r++){v.push_back({r,P[r]});v.push_back({r,Q[r]});}for(int i=0;i<2*n;i++)for(int j=i+1;j<2*n;j++)for(int k=j+1;k<2*n;k++)s+=col(v[i],v[j],v[k]);return s;}
bool valid(const vector<int>&P,const vector<int>&Q){for(int i=0;i<(int)P.size();i++)if(P[i]==Q[i])return false;return true;}
string key(const vector<int>&P,const vector<int>&Q){string s;for(int x:P)s+=char(x+1);for(int x:Q)s+=char(x+1);return s;}
int main(){
 vector<int>P={8,3,0,11,5,2,12,6,13,9,1,10,4,7};
 vector<int>Q={4,11,12,5,7,8,13,0,1,6,2,9,10,3};
 cerr<<"base="<<score(P,Q)<<"\n";
 set<string>seen;vector<pair<vector<int>,vector<int>>>front={{{P},{Q}}},next;seen.insert(key(P,Q));int best=score(P,Q);
 for(int depth=1;depth<=20;depth++){
   next.clear();
   for(auto &st:front)for(int layer=0;layer<2;layer++)for(int a=0;a<14;a++)for(int b=a+1;b<14;b++){
     auto X=st.first,Y=st.second;auto &V=layer?Y:X;swap(V[a],V[b]);if(!valid(X,Y))continue;
     string k=key(X,Y);if(!seen.insert(k).second)continue;int sc=score(X,Y);
     if(sc<best){best=sc;cerr<<"depth="<<depth<<" best="<<best<<" seen="<<seen.size()<<"\n";if(!best){cout<<"P";for(int x:X)cout<<" "<<x;cout<<"\nQ";for(int x:Y)cout<<" "<<x;cout<<"\n";return 0;}}
     if(sc<=4)next.push_back({move(X),move(Y)});
   }
   cerr<<"depth "<<depth<<" frontier="<<next.size()<<" seen="<<seen.size()<<" best="<<best<<"\n";front.swap(next);
 }
 return 1;
}

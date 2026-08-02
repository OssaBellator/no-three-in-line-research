#include <bits/stdc++.h>
using namespace std;
bool col(array<int,2>a,array<int,2>b,array<int,2>c){return 1LL*(b[0]-a[0])*(c[1]-a[1])==1LL*(b[1]-a[1])*(c[0]-a[0]);}
int score(const vector<int>&P,const vector<int>&Q){int n=P.size();vector<array<int,2>>v;for(int i=0;i<n;i++)v.push_back({i,P[i]});for(int i=0;i<n;i++)v.push_back({i,Q[i]});int s=0;for(int i=0;i<2*n;i++)for(int j=i+1;j<2*n;j++)for(int k=j+1;k<2*n;k++)s+=col(v[i],v[j],v[k]);return s;}
vector<int> ins(const vector<int>&A,int a){int n=A.size();vector<int>R=A;R.push_back(A[a]);R[a]=n;return R;}
int main(){vector<int>P13={9,4,7,3,0,1,12,8,11,10,2,6,5},Q13={7,12,9,1,4,3,8,0,2,11,5,10,6};int best=999;vector<int>BP,BQ;long long checked=0;map<int,long long>hist;
for(int a=0;a<13;a++)for(int b=0;b<13;b++){auto P=ins(P13,a),Q=ins(Q13,b);for(int mode=-1;mode<2;mode++){if(mode==-1){bool ok=1;for(int r=0;r<14;r++)if(P[r]==Q[r])ok=0;if(ok){int s=score(P,Q);checked++;hist[s]++;if(s<best){best=s;BP=P;BQ=Q;}}}else for(int i=0;i<14;i++)for(int j=i+1;j<14;j++){auto P2=P,Q2=Q;auto&A=mode?Q2:P2;swap(A[i],A[j]);bool ok=1;for(int r=0;r<14;r++)if(P2[r]==Q2[r])ok=0;if(!ok)continue;int s=score(P2,Q2);checked++;hist[s]++;if(s<best){best=s;BP=P2;BQ=Q2;}}}}
cerr<<"checked="<<checked<<" best="<<best<<"\n";cerr<<"hist";for(auto [k,v]:hist)cerr<<" "<<k<<":"<<v;cerr<<"\n";cout<<"P";for(int x:BP)cout<<" "<<x;cout<<"\nQ";for(int x:BQ)cout<<" "<<x;cout<<"\n";
}

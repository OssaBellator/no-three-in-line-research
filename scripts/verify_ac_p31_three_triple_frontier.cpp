#include <bits/stdc++.h>
using namespace std;struct P{int x,y;};struct M{int l,i,j;};
bool col(P a,P b,P c){return 1LL*(b.x-a.x)*(c.y-a.y)==1LL*(b.y-a.y)*(c.x-a.x);}
string enc(vector<int>r,vector<int>b){string s;for(int x:r)s+=char(x);for(int x:b)s+=char(x);return s;}
bool legal(string const&s,M m){int o=30*m.l,q=30*(1-m.l);return (unsigned char)s[o+m.j]!=(unsigned char)s[q+m.i]&&(unsigned char)s[o+m.i]!=(unsigned char)s[q+m.j];}
string apply(string s,M m){swap(s[30*m.l+m.i],s[30*m.l+m.j]);return s;}
int pot(string const&s){P p[60];for(int i=0;i<30;i++){p[2*i]={i+1,(unsigned char)s[i]};p[2*i+1]={i+1,(unsigned char)s[30+i]};}int v=0;for(int i=0;i<60;i++)for(int j=i+1;j<60;j++)for(int k=j+1;k<60;k++)v+=col(p[i],p[j],p[k]);return v;}
int A(vector<P>const&T,P p){int a[60],n=0;for(auto u:T){int x=u.x-p.x,y=u.y-p.y,g=gcd(abs(x),abs(y));x/=g;y/=g;if(x<0||(x==0&&y<0))x=-x,y=-y;a[n++]=(x+30)*61+y+30;}sort(a,a+n);int z=0;for(int i=0;i<n;){int j=i+1;while(j<n&&a[j]==a[i])j++;int c=j-i;z+=c*(c-1)/2;i=j;}return z;}
int B(vector<P>const&T,P p,P q){int z=0;for(auto u:T)z+=col(p,q,u);return z;}
int npot(string const&s,int cur,M m){int o=30*m.l;P a={m.i+1,(unsigned char)s[o+m.i]},b={m.j+1,(unsigned char)s[o+m.j]},c={m.i+1,b.y},d={m.j+1,a.y};vector<P>T;for(int l=0;l<2;l++)for(int i=0;i<30;i++)if(!(l==m.l&&(i==m.i||i==m.j)))T.push_back({i+1,(unsigned char)s[30*l+i]});return cur+A(T,c)+A(T,d)+B(T,c,d)-A(T,a)-A(T,b)-B(T,a,b);}
vector<M> moves(){vector<M>v;for(int l=0;l<2;l++)for(int i=0;i<30;i++)for(int j=i+1;j<30;j++)v.push_back({l,i,j});return v;}
int main(int argc,char**argv){vector<int>r={14,15,9,18,8,25,29,3,4,13,19,2,23,28,1,12,7,24,6,17,11,26,30,5,22,27,20,16,21,10},b={18,10,24,6,14,15,23,20,25,1,9,4,7,29,30,27,28,19,2,5,3,13,21,11,8,26,12,22,17,16};string st=enc(r,b);assert(pot(st)==3);vector<size_t>want={1,1,9,42,205,3635};auto mv=moves();int lo=argc>1?atoi(argv[1]):3,hi=argc>1?lo:8;for(int barrier=lo;barrier<=hi;barrier++){unordered_set<string>seen;queue<pair<string,int>>q;seen.insert(st);q.push({st,3});bool lower=false;while(!q.empty()){auto [s,p]=q.front();q.pop();for(auto m:mv){if(!legal(s,m))continue;int z=npot(s,p,m);if(z>barrier)continue;string t=apply(s,m);if(!seen.insert(t).second)continue;if(z<3)lower=true;q.push({move(t),z});}}assert(seen.size()==want[barrier-3]&&!lower);cout<<"barrier "<<barrier<<" states "<<seen.size()<<" lower 0\n";}}

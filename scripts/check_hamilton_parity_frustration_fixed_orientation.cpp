#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <numeric>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;

struct Point { int x, y; };
long long cross(Point a, Point b, Point c) {
  return 1LL * (b.x-a.x) * (c.y-a.y) - 1LL * (b.y-a.y) * (c.x-a.x);
}
array<Point,4> orbit_block(int m, int s, int t, int e) {
  int n=2*m; auto r=[n](int x){ return n-1-x; };
  Point q0{s,e?r(t):t}, q1{r(s),e?t:r(t)};
  return {q0,q1,Point{r(q0.y),q0.x},Point{r(q1.y),q1.x}};
}
bool two_owner_bad(int m,int sa,int ta,int ea,int sb,int tb,int eb) {
  auto a=orbit_block(m,sa,ta,ea), b=orbit_block(m,sb,tb,eb);
  array<Point,8> p{}; for(int i=0;i<4;i++){p[i]=a[i];p[i+4]=b[i];}
  for(int i=0;i<8;i++) for(int j=i+1;j<8;j++) for(int k=j+1;k<8;k++)
    if(cross(p[i],p[j],p[k])==0) return true;
  return false;
}
struct Rel {
  int m; vector<int8_t> d;
  explicit Rel(int M):m(M),d(m*m*m*m,0) {
    for(int a=0;a<m;a++) for(int ta=0;ta<m;ta++) { if(ta==a) continue;
      for(int b=a+1;b<m;b++) for(int tb=0;tb<m;tb++) { if(tb==b||tb==ta) continue;
        bool eq=two_owner_bad(m,a,ta,0,b,tb,0), un=two_owner_bad(m,a,ta,0,b,tb,1);
        d[idx(a,ta,b,tb)] = eq&&un ? 3 : eq ? 2 : un ? 1 : 0;
      }
    }
  }
  int idx(int a,int ta,int b,int tb) const { return ((a*m+ta)*m+b)*m+tb; }
  int get(int a,int ta,int b,int tb) const { return d[idx(a,ta,b,tb)]; }
};
struct Edge { int a,b,x; };
struct Info { bool safe=false; int lam=-1; vector<Edge> es; vector<int> opts,cost; };
Info classify(int m,const vector<int>& r,const Rel& R) {
  Info z;
  for(int a=0;a<m;a++) for(int b=a+1;b<m;b++) {
    int v=R.get(a,r[a],b,r[b]); if(v==3) return z;
    if(v) z.es.push_back({a,b,v==1?0:1});
  }
  z.safe=true; z.cost.assign(1<<m,0); z.lam=z.es.size();
  for(int o=0;o<(1<<m);o++) {
    int w=0; for(auto e:z.es) w += ((((o>>e.a)&1)^((o>>e.b)&1))!=e.x);
    z.cost[o]=w;
    if(w<z.lam){z.lam=w;z.opts={o};} else if(w==z.lam) z.opts.push_back(o);
  }
  return z;
}
uint64_t enc(const vector<int>& r){uint64_t x=0;for(int t:r)x=(x<<4)|t;return x;}
vector<int> switched(const vector<int>& r,array<int,3> s) {
  array<int,3> c{}; int f=0,u=*min_element(s.begin(),s.end());
  for(int i=0;i<(int)r.size();i++){if(u==s[0]||u==s[1]||u==s[2])c[f++]=u;u=r[u];}
  auto o=r; o[c[0]]=r[c[1]];o[c[1]]=r[c[2]];o[c[2]]=r[c[0]];return o;
}
struct Case { long long cycles,safe,pos,maxlam,opt,desc,mindesc,checks,targetinc,mintarget; };
const array<Case,5> expected={{
  {24,24,2,1,48,244,3,48,244,3},
  {120,120,8,1,272,2596,5,272,2596,5},
  {720,720,56,1,2752,37020,6,2752,37020,6},
  {5040,4560,1018,2,93980,1674032,5,97224,1724790,5},
  {40320,37440,5752,3,977312,25073346,4,1001344,25538574,4}
}};
int main(){
  cout<<"{\n  \"cases\": [\n";
  for(int m=5;m<=9;m++){
    Rel R(m); vector<vector<int>> cy; vector<int> tail(m-1); iota(tail.begin(),tail.end(),1);
    do { vector<int> ord(m),r(m);ord[0]=0;for(int i=1;i<m;i++)ord[i]=tail[i-1];
      for(int i=0;i<m;i++)r[ord[i]]=ord[(i+1)%m];cy.push_back(move(r));
    } while(next_permutation(tail.begin(),tail.end()));
    unordered_map<uint64_t,int> ix;ix.reserve(cy.size()*2);for(int i=0;i<(int)cy.size();i++)ix[enc(cy[i])]=i;
    vector<Info> info;info.reserve(cy.size());for(auto&r:cy)info.push_back(classify(m,r,R));
    vector<array<int,3>> triples;for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)triples.push_back({a,b,c});
    Case got{(long long)cy.size(),0,0,0,0,0,numeric_limits<int>::max(),0,0,numeric_limits<int>::max()};
    for(int i=0;i<(int)cy.size();i++){
      auto&S=info[i];if(!S.safe)continue;got.safe++;got.maxlam=max(got.maxlam,(long long)S.lam);if(S.lam==0)continue;got.pos++;
      for(int o:S.opts){got.opt++;vector<array<int,3>> good;
        for(auto t:triples){int j=ix.at(enc(switched(cy[i],t)));if(info[j].safe&&info[j].cost[o]<S.lam){good.push_back(t);got.desc++;}}
        if(good.empty())return 1;got.mindesc=min(got.mindesc,(long long)good.size());
        for(auto e:S.es){int p=((o>>e.a)&1)^((o>>e.b)&1);if(p==e.x)continue;got.checks++;int h=0;
          for(auto t:good)if(t[0]==e.a||t[1]==e.a||t[2]==e.a||t[0]==e.b||t[1]==e.b||t[2]==e.b)h++;
          if(!h)return 2;got.targetinc+=h;got.mintarget=min(got.mintarget,(long long)h);
        }
      }
    }
    if(tie(got.cycles,got.safe,got.pos,got.maxlam,got.opt,got.desc,got.mindesc,got.checks,got.targetinc,got.mintarget)!=
       tie(expected[m-5].cycles,expected[m-5].safe,expected[m-5].pos,expected[m-5].maxlam,expected[m-5].opt,expected[m-5].desc,expected[m-5].mindesc,expected[m-5].checks,expected[m-5].targetinc,expected[m-5].mintarget)) return 3;
    cout<<"    {\"m\": "<<m<<", \"hamilton_cycles\": "<<got.cycles<<", \"pair_safe_cycles\": "<<got.safe
        <<", \"positive_frustration_cycles\": "<<got.pos<<", \"maximum_frustration\": "<<got.maxlam
        <<", \"optimal_signed_states\": "<<got.opt<<", \"fixed_orientation_strict_descent_rotations\": "<<got.desc
        <<", \"minimum_fixed_orientation_descents_per_optimal_state\": "<<got.mindesc
        <<", \"optimal_violated_edge_checks\": "<<got.checks
        <<", \"fixed_orientation_targeted_descent_incidences\": "<<got.targetinc
        <<", \"minimum_targeted_descents_per_violated_edge\": "<<got.mintarget<<"}"<<(m<9?",":"")<<"\n";
  }
  cout<<"  ],\n  \"orientation_bits_changed\": 0,\n  \"finite_clean_reachability_proved\": true,\n  \"asymptotic_theorem_proved\": false\n}\n";
}

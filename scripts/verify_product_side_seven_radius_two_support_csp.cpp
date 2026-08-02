// Exact radius-two support-eight through support-sixteen census for PX523--PX561.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>
constexpr int PAIRS[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
using Selector=std::array<uint16_t,14>;
struct Hash{size_t operator()(Selector const&s)const noexcept{uint64_t h=1469598103934665603ULL;for(auto x:s){h^=x;h*=1099511628211ULL;}return h;}};
struct Case {
 std::string name; std::array<int,7> h,p; std::array<int,14> opts; int n1;
 int count8; std::vector<uint64_t> nodes8;
 int count10; std::vector<uint64_t> nodes10;
 int count12; std::vector<uint64_t> nodes12;
 int count14; std::vector<uint64_t> nodes14;
 int count16; std::vector<uint64_t> nodes16;
};
const std::array<Case,4> C={{
{"cycle7",{1,2,3,4,5,6,0},{5,4,0,6,2,1,3},{0,3,0,3,5,2,2,2,2,3,0,5,5,2},1092,
 435,{19127017ULL,33614524ULL,67538237ULL,57041978ULL,64458064ULL,53624461ULL},
 400,{20597821ULL,23018169ULL,40816672ULL,46936004ULL,39311932ULL,61086054ULL},
 3606,{131090413ULL,216370311ULL,404711510ULL,382077982ULL,503551541ULL,293314232ULL,324879897ULL,479206721ULL},
 4424,{197342065ULL,246818321ULL,330593418ULL,357066034ULL,452213057ULL,301577180ULL,507452920ULL,568399610ULL},
 18878,{289087794ULL,318210703ULL,322879082ULL,861741503ULL,758898983ULL,642106496ULL,999493244ULL,509481370ULL,1010276919ULL,1295920468ULL,657018104ULL,474687224ULL,852230809ULL,927236794ULL,769406692ULL,654438254ULL,999771967ULL,1046422487ULL,982987269ULL,1063264358ULL}},
{"cycle52",{1,2,3,4,0,6,5},{4,5,6,1,3,2,0},{2,2,2,2,2,2,2,2,2,2,2,5,0,2},364,
 533,{40030400ULL,57345887ULL,33981701ULL,44048868ULL,101572181ULL,69065925ULL},
 232,{27076183ULL,30286767ULL,58018025ULL,56658274ULL},
 1584,{231405092ULL,251116181ULL,313695839ULL,307223426ULL},
 1768,{240876479ULL,253501850ULL,349043610ULL,382044493ULL},
 5315,{297973260ULL,375305493ULL,305353084ULL,389168515ULL,373483392ULL,357261219ULL,534515368ULL,405841387ULL,488709445ULL,553223034ULL}},
{"cycle43",{1,2,3,0,5,6,4},{3,5,4,2,1,0,6},{5,5,2,0,0,5,2,0,0,5,5,0,3,3},180,
 543,{42585761ULL,66347848ULL,76897952ULL,66169226ULL,103476284ULL,163009711ULL},
 328,{47475742ULL,35822742ULL,54770126ULL,76897799ULL,96188731ULL},
 1004,{153242984ULL,190921908ULL,262696979ULL,308374840ULL},
 2132,{350880977ULL,365965157ULL,475974767ULL,693598023ULL},
 2013,{277360234ULL,289151213ULL,318489994ULL,399523616ULL,533283092ULL}},
{"cycle322",{1,2,0,4,3,6,5},{4,6,5,3,1,2,0},{5,0,3,1,0,5,0,5,5,0,4,3,5,0},112,
 725,{26235664ULL,41988721ULL,22337561ULL,30670276ULL,78907092ULL,68401164ULL,110299561ULL,55229265ULL},
 904,{30876314ULL,41722256ULL,36689106ULL,58922044ULL,73943616ULL,69983797ULL,91619703ULL,79460595ULL,70781994ULL,57790370ULL},
 1202,{124313599ULL,124201892ULL,220161743ULL,239374078ULL},
 988,{155946577ULL,112051316ULL,157387617ULL,214235463ULL},
 478,{81347148ULL,49661110ULL,84567840ULL,95127226ULL}}
}};
Selector centre(const Case&d){Selector s{};for(int sr=0;sr<14;sr++){int o=sr/7,u=sr%7,z=o?d.p[u]:u;int a[4]={z,d.h[z],7+z,7+d.h[z]};int r=7*o+z;for(int k=0;k<2;k++)s[r]|=1u<<a[PAIRS[d.opts[sr]][k]];}return s;}
std::array<uint16_t,14> host(const Case&d){std::array<uint16_t,14>x{};for(int o=0;o<2;o++)for(int z=0;z<7;z++)x[7*o+z]=(1u<<z)|(1u<<d.h[z])|(1u<<(7+z))|(1u<<(7+d.h[z]));return x;}
struct E{Selector s;std::array<uint16_t,14>h{},at{};std::unordered_set<Selector,Hash> ns;std::vector<int>rs,cs;int st;
void dfs(int r,uint16_t ur,uint16_t uc){uint16_t u=h[r]&~s[r];while(u){int c=__builtin_ctz(u);u&=u-1;if(uc>>c&1)continue;uint16_t q=at[c];while(q){int rr=__builtin_ctz(q);q&=q-1;if(rr==st){if(rs.size()<2)continue;Selector f=s;for(size_t i=0;i<cs.size();i++){int oc=cs[i];f[rs[i]]^=1u<<oc;f[rs[i+1]]^=1u<<oc;}f[rs.back()]^=1u<<c;f[st]^=1u<<c;ns.insert(f);}else if(!(ur>>rr&1)&&rr>=st){rs.push_back(rr);cs.push_back(c);dfs(rr,ur|(1u<<rr),uc|(1u<<c));cs.pop_back();rs.pop_back();}}}}
void run(){at.fill(0);ns.clear();for(int c=0;c<14;c++)for(int r=0;r<14;r++)if(s[r]>>c&1)at[c]|=1u<<r;for(st=0;st<14;st++){rs={st};cs.clear();dfs(st,1u<<st,0);}}
};
struct Point{int x,y;};
inline int det(const Point&a,const Point&b,const Point&c){return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);}
struct Spec{bool top;uint8_t label,col;};
struct CSP{
 struct Mask { uint64_t w[4]{}; inline void add(const Mask&o){w[0]|=o.w[0];w[1]|=o.w[1];w[2]|=o.w[2];w[3]|=o.w[3];} inline bool has(int id)const{return (w[id>>6]>>(id&63))&1ULL;} };
 static std::array<std::array<Mask,196>,196> lines; static bool lines_ready;
 std::array<Spec,28> spec{}; std::array<int8_t,21> asg{}; std::array<uint8_t,3> used{};
 std::array<std::array<uint8_t,2>,21> touching{}; std::array<uint8_t,21> touchCount{};
 std::array<uint8_t,28> complete{}; std::array<uint8_t,28> compList{}; std::array<uint8_t,28> pointId{}; int compCount=0; int ori=0; uint64_t nodes=0;
 static void init_lines(){if(lines_ready)return;for(int a=0;a<196;a++){Point pa{a/14,a%14};for(int b=0;b<196;b++){Point pb{b/14,b%14};if(a==b)continue;for(int c=0;c<196;c++){Point pc{c/14,c%14};if(det(pa,pb,pc)==0)lines[a][b].w[c>>6]|=1ULL<<(c&63);}}}lines_ready=true;}
 inline int group(int v) const{return v<7?0:v<14?1:2;}
 inline bool iscomplete(int pi)const{auto&p=spec[pi]; return asg[p.col]>=0 && (p.top || asg[14+p.label]>=0);}
 inline int calc_id(int pi) const {auto&p=spec[pi];int rp=p.top?p.label:asg[14+p.label];int x=ori<2?(p.top?rp:7+rp):2*rp+(p.top?0:1);int oc=p.col/7, cp=asg[p.col];int y=ori%2==0?7*oc+cp:2*cp+oc;return 14*x+y;}
 int newly_for(int v,std::array<uint8_t,2>&out){int n=0;for(int k=0;k<touchCount[v];k++){int pi=touching[v][k];if(!complete[pi]&&iscomplete(pi))out[n++]=pi;}return n;}
 bool candidate_ok(const Mask& danger,const std::array<uint8_t,2>&nw,int nc,std::array<uint8_t,2>&ids) const{if(nc==0)return true;ids[0]=calc_id(nw[0]);if(danger.has(ids[0]))return false;if(nc==2){ids[1]=calc_id(nw[1]);if(danger.has(ids[1]))return false;for(int i=0;i<compCount;i++)if(lines[ids[0]][pointId[compList[i]]].has(ids[1]))return false;}return true;}
 bool allowed(int v,int val,const Mask&danger){int g=group(v);if(used[g]>>val&1)return false;asg[v]=val;std::array<uint8_t,2>nw{},ids{};int nc=newly_for(v,nw);bool ok=candidate_ok(danger,nw,nc,ids);asg[v]=-1;return ok;}
 bool search(int depth,const Mask&danger){++nodes;if(depth==21)return true;int bv=-1,bc=8;std::array<int8_t,7>dom{};int dn=0;for(int v=0;v<21;v++)if(asg[v]<0){std::array<int8_t,7>d{};int c=0;for(int val=0;val<7;val++)if(allowed(v,val,danger))d[c++]=val;if(c==0)return false;if(c<bc){bc=c;bv=v;dn=c;dom=d;if(c==1)break;}}int g=group(bv);for(int ii=0;ii<dn;ii++){int val=dom[ii];asg[bv]=val;used[g]|=1u<<val;std::array<uint8_t,2>nw{},ids{};int nc=newly_for(bv,nw);bool ok=candidate_ok(danger,nw,nc,ids);assert(ok);Mask child=danger;for(int k=0;k<nc;k++){int pi=nw[k],id=ids[k];for(int i=0;i<compCount;i++)child.add(lines[id][pointId[compList[i]]]);for(int q=0;q<k;q++)child.add(lines[id][ids[q]]);complete[pi]=1;pointId[pi]=id;compList[compCount++]=pi;}if(search(depth+1,child))return true;for(int k=nc-1;k>=0;k--){--compCount;complete[nw[k]]=0;}used[g]&=~(1u<<val);asg[bv]=-1;}return false;}
 bool solve(const Selector&s,int o){init_lines();ori=o;asg.fill(-1);used.fill(0);complete.fill(0);touchCount.fill(0);compCount=0;nodes=0;int n=0;for(int r=0;r<14;r++){uint16_t m=s[r];while(m){int c=__builtin_ctz(m);m&=m-1;spec[n]={r<7,(uint8_t)(r%7),(uint8_t)c};touching[c][touchCount[c]++]=n;if(r>=7)touching[14+r%7][touchCount[14+r%7]++]=n;n++;}}assert(n==28);Mask empty{};return search(0,empty);}
};
std::array<std::array<CSP::Mask,196>,196> CSP::lines{}; bool CSP::lines_ready=false;
int main(int argc,char**argv){
 assert(argc==4); std::string req=argv[1]; int support=std::stoi(argv[2]), shard=std::stoi(argv[3]);
 for(auto&d:C) if(req==d.name){
  int expected_count=support==8?d.count8:support==10?d.count10:support==12?d.count12:support==14?d.count14:support==16?d.count16:-1;
  const auto& expected_nodes=support==8?d.nodes8:support==10?d.nodes10:support==12?d.nodes12:support==14?d.nodes14:d.nodes16;
  assert(expected_count>=0 && shard>=0 && shard<(int)expected_nodes.size());
  Selector center=centre(d); auto ho=host(d); E e; e.s=center; e.h=ho; e.run(); assert((int)e.ns.size()==d.n1);
  std::unordered_set<Selector,Hash> n1=e.ns; std::set<Selector> layer;
  for(auto const&parent:n1){e.s=parent;e.run();for(auto const&v:e.ns){if(v==center||n1.count(v))continue;int diff=0;for(int r=0;r<14;r++)diff+=__builtin_popcount(v[r]^center[r]);if(diff==support)layer.insert(v);}}
  assert((int)layer.size()==expected_count);
  int shard_count=expected_nodes.size(); int shard_size=(expected_count+shard_count-1)/shard_count;
  int first=shard*shard_size+1,last=std::min(expected_count,first+shard_size-1);
  uint64_t total=0;int idx=0,done=0;for(auto const&s:layer){++idx;if(idx<first||idx>last)continue;++done;for(int o=0;o<4;o++){CSP solver;bool ok=solver.solve(s,o);assert(!ok);total+=solver.nodes;}}
  assert(done==std::max(0,last-first+1)); assert(total==expected_nodes[shard]);
  std::cout<<d.name<<" support="<<support<<" shard="<<shard<<"/"<<shard_count<<" selectors="<<done<<" nodes="<<total<<" PASS\n";return 0;
 }
 assert(false);
}

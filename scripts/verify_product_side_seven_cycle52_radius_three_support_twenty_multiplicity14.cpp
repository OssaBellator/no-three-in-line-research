#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_set>
#include <vector>

constexpr int N = 7;
constexpr int SIDE = 14;
constexpr int PAIRS[6][2] = {{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
using State = std::array<uint16_t, SIDE>;
using Assignment = std::array<int8_t, SIDE>;
using Signature = std::array<uint16_t, N>;

struct StateHash {
    size_t operator()(State const& s) const noexcept {
        uint64_t h = 1469598103934665603ULL;
        for (auto x : s) { h ^= x; h *= 1099511628211ULL; }
        return static_cast<size_t>(h);
    }
};

const std::array<int,N> hp = {1,2,3,4,0,6,5};
const std::array<int,N> pp = {4,5,6,1,3,2,0};
const std::array<int,SIDE> opts = {2,2,2,2,2,2,2,2,2,2,2,5,0,2};

State centre() {
    State s{};
    for (int sr=0; sr<SIDE; ++sr) {
        int outer=sr/N, u=sr%N, z=outer ? pp[u] : u;
        int adjacent[4] = {z,hp[z],N+z,N+hp[z]};
        int row=N*outer+z;
        for (int k=0;k<2;++k) s[row] |= uint16_t(1u << adjacent[PAIRS[opts[sr]][k]]);
    }
    return s;
}

std::array<uint16_t,SIDE> host_masks() {
    std::array<uint16_t,SIDE> h{};
    for (int outer=0;outer<2;++outer) for (int z=0;z<N;++z)
        h[N*outer+z] = uint16_t((1u<<z)|(1u<<hp[z])|(1u<<(N+z))|(1u<<(N+hp[z])));
    return h;
}

int support_distance(State const& a, State const& b) {
    int d=0;
    for (int r=0;r<SIDE;++r) d += __builtin_popcount(unsigned(a[r]^b[r]));
    return d;
}

struct NeighborEnumerator {
    State s{};
    std::array<uint16_t,SIDE> host{};
    std::array<uint16_t,SIDE> at_column{};
    std::unordered_set<State,StateHash> neighbors;
    std::vector<int> rows, cols;
    int start=0;

    void dfs(int row, uint16_t used_rows, uint16_t used_cols) {
        uint16_t unused = uint16_t(host[row] & ~s[row]);
        while (unused) {
            int col=__builtin_ctz(unsigned(unused));
            unused &= uint16_t(unused-1);
            if ((used_cols>>col)&1u) continue;
            uint16_t q=at_column[col];
            while (q) {
                int next_row=__builtin_ctz(unsigned(q));
                q &= uint16_t(q-1);
                if (next_row==start) {
                    if (rows.size()<2) continue;
                    State f=s;
                    for (size_t i=0;i<cols.size();++i) {
                        int old_col=cols[i];
                        f[rows[i]] ^= uint16_t(1u<<old_col);
                        f[rows[i+1]] ^= uint16_t(1u<<old_col);
                    }
                    f[rows.back()] ^= uint16_t(1u<<col);
                    f[start] ^= uint16_t(1u<<col);
                    neighbors.insert(f);
                } else if (!((used_rows>>next_row)&1u) && next_row>=start) {
                    rows.push_back(next_row); cols.push_back(col);
                    dfs(next_row, uint16_t(used_rows|(1u<<next_row)), uint16_t(used_cols|(1u<<col)));
                    cols.pop_back(); rows.pop_back();
                }
            }
        }
    }

    void run() {
        at_column.fill(0); neighbors.clear();
        for (int c=0;c<SIDE;++c) for (int r=0;r<SIDE;++r)
            if ((s[r]>>c)&1u) at_column[c] |= uint16_t(1u<<r);
        for (start=0;start<SIDE;++start) {
            rows={start}; cols.clear(); dfs(start,uint16_t(1u<<start),0);
        }
    }
};

struct Point { int x,y; };
inline int det(Point a, Point b, Point c) {
    return (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x);
}

struct TopEnumerator {
    Signature sig{};
    Assignment assignment{};
    std::array<uint8_t,2> used{};
    std::vector<Assignment> solutions;
    int mode=0;
    uint64_t nodes=0;

    bool clean_partial() const {
        std::array<Point,14> pts{};
        int count=0;
        for (int row=0;row<N;++row) {
            uint16_t mask=sig[row];
            while (mask) {
                int c=__builtin_ctz(unsigned(mask)); mask &= uint16_t(mask-1);
                if (assignment[c]>=0) {
                    int y = mode==0 ? N*(c/N)+assignment[c] : 2*assignment[c]+c/N;
                    pts[count++]={row,y};
                }
            }
        }
        for (int i=0;i<count;++i) for (int j=i+1;j<count;++j) for (int k=j+1;k<count;++k)
            if (det(pts[i],pts[j],pts[k])==0) return false;
        return true;
    }

    void dfs(int depth) {
        ++nodes;
        if (depth==SIDE) { solutions.push_back(assignment); return; }
        int best_var=-1,best_size=8,domain_size=0;
        std::array<int8_t,N> best_domain{};
        for (int var=0;var<SIDE;++var) if (assignment[var]<0) {
            int group=var/N, sz=0;
            std::array<int8_t,N> domain{};
            for (int value=0;value<N;++value) if (!((used[group]>>value)&1u)) {
                assignment[var]=int8_t(value);
                if (clean_partial()) domain[sz++]=int8_t(value);
                assignment[var]=-1;
            }
            if (sz==0) return;
            if (sz<best_size) { best_size=sz; best_var=var; domain_size=sz; best_domain=domain; }
        }
        int group=best_var/N;
        for (int i=0;i<domain_size;++i) {
            int value=best_domain[i];
            assignment[best_var]=int8_t(value); used[group]|=uint8_t(1u<<value);
            dfs(depth+1);
            used[group]&=uint8_t(~(1u<<value)); assignment[best_var]=-1;
        }
    }

    void run(int selected_mode) {
        mode=selected_mode; assignment.fill(-1); used.fill(0); solutions.clear(); nodes=0; dfs(0);
    }
};

struct BottomGroupSolver {
    std::vector<State> candidates;
    std::array<uint16_t,SIDE> host{};
    Assignment top{};
    std::array<int8_t,N> bottom{};
    uint8_t used=0;
    int orientation=0;
    uint64_t nodes=0;
    std::array<uint64_t,SIDE*SIDE> edge_mask{};
    uint64_t all=0;
    std::array<int,SIDE> column_y{};
    std::array<int,SIDE*SIDE> top_point_code{};
    std::array<std::array<int,N>,SIDE*SIDE> bottom_point_code{};
    std::array<int,14> top_edges{};
    int top_edge_count=0;
    std::array<std::array<int,4>,N> bottom_edges{};

    void initialize(std::vector<State> const& group) {
        candidates=group; host=host_masks();
        all=(1ULL<<candidates.size())-1ULL;
        edge_mask.fill(0);
        for (int i=0;i<(int)candidates.size();++i) for (int rr=0;rr<SIDE;++rr) {
            uint16_t mask=candidates[i][rr];
            while (mask) { int c=__builtin_ctz(unsigned(mask)); mask&=uint16_t(mask-1); edge_mask[SIDE*rr+c]|=1ULL<<i; }
        }
        top_edge_count=0;
        for (int rr=0;rr<N;++rr) {
            uint16_t mask=candidates[0][rr];
            while(mask){int c=__builtin_ctz(unsigned(mask));mask&=uint16_t(mask-1);top_edges[top_edge_count++]=SIDE*rr+c;}
        }
        assert(top_edge_count==14);
        for (int z=0;z<N;++z) {
            int count=0; uint16_t mask=host[N+z];
            while(mask){int c=__builtin_ctz(unsigned(mask));mask&=uint16_t(mask-1);bottom_edges[z][count++]=SIDE*(N+z)+c;}
            assert(count==4);
        }
    }

    void prepare_top(Assignment const& top_assignment,int ori) {
        top=top_assignment; orientation=ori;
        for (int c=0;c<SIDE;++c) column_y[c]=orientation%2==0 ? N*(c/N)+top[c] : 2*top[c]+c/N;
        top_point_code.fill(-1);
        for (int edge:top_edges) {
            int row=edge/SIDE,c=edge%SIDE; int x=orientation<2?row:2*row;
            top_point_code[edge]=SIDE*x+column_y[c];
        }
        for (int z=0;z<N;++z) for (int k=0;k<4;++k) {
            int edge=bottom_edges[z][k],c=edge%SIDE;
            for (int value=0;value<N;++value) {
                int x=orientation<2?N+value:2*value+1;
                bottom_point_code[edge][value]=SIDE*x+column_y[c];
            }
        }
    }

    int point_code(int edge) const {
        int row=edge/SIDE;
        return row<N ? top_point_code[edge] : bottom_point_code[edge][bottom[row%N]];
    }

    uint64_t transition(int newly_assigned_z,uint64_t active) const {
        std::array<int,42> prior{}; int prior_count=0;
        for (int i=0;i<top_edge_count;++i) prior[prior_count++]=top_edges[i];
        for (int z=0;z<N;++z) {
            if (bottom[z]<0 || z==newly_assigned_z) continue;
            for (int k=0;k<4;++k) prior[prior_count++]=bottom_edges[z][k];
        }
        for (int k=0;k<4;++k) {
            int edge=bottom_edges[newly_assigned_z][k],pe=point_code(edge);
            for (int i=0;i<prior_count;++i) for (int j=i+1;j<prior_count;++j) {
                int f=prior[i],g=prior[j],pf=point_code(f),pg=point_code(g);
                if (det({pe/SIDE,pe%SIDE},{pf/SIDE,pf%SIDE},{pg/SIDE,pg%SIDE})==0)
                    active &= ~(edge_mask[edge]&edge_mask[f]&edge_mask[g]);
            }
            prior[prior_count++]=edge;
            if (!active) break;
        }
        return active;
    }

    bool dfs(int depth,uint64_t active) {
        ++nodes;
        if (depth==N) return active!=0;
        int best_z=-1,best_size=8,domain_size=0;
        std::array<int8_t,N> best_domain{};
        std::array<uint64_t,N> best_masks{};
        for (int z=0;z<N;++z) if (bottom[z]<0) {
            int sz=0; std::array<int8_t,N> domain{}; std::array<uint64_t,N> masks{};
            for (int value=0;value<N;++value) if (!((used>>value)&1u)) {
                bottom[z]=int8_t(value); uint64_t child=transition(z,active); bottom[z]=-1;
                if (child) { domain[sz]=int8_t(value); masks[sz]=child; ++sz; }
            }
            if (sz==0) return false;
            if (sz<best_size) { best_size=sz; best_z=z; domain_size=sz; best_domain=domain; best_masks=masks; }
        }
        for (int i=0;i<domain_size;++i) {
            int value=best_domain[i]; bottom[best_z]=int8_t(value); used|=uint8_t(1u<<value);
            if (dfs(depth+1,best_masks[i])) return true;
            used&=uint8_t(~(1u<<value)); bottom[best_z]=-1;
        }
        return false;
    }

    bool solve_top(Assignment const& top_assignment,int ori) {
        prepare_top(top_assignment,ori); bottom.fill(-1); used=0; nodes=0; return dfs(0,all);
    }
};

std::vector<State> generate_layer() {
    State c=centre(); auto h=host_masks(); NeighborEnumerator e; e.s=c; e.host=h; e.run();
    auto r1=e.neighbors; assert(r1.size()==364);
    std::unordered_set<State,StateHash> r2;
    for (auto const& p:r1) { e.s=p; e.run(); for (auto const& v:e.neighbors) if (v!=c&&!r1.count(v)) r2.insert(v); }
    assert(r2.size()==26550);
    std::unordered_set<State,StateHash> r3;
    for (auto const& p:r2) { e.s=p; e.run(); for (auto const& v:e.neighbors)
        if (v!=c&&!r1.count(v)&&!r2.count(v)&&support_distance(c,v)==20) r3.insert(v);
    }
    assert(r3.size()==71860);
    return std::vector<State>(r3.begin(),r3.end());
}

struct CaseData {
    int global_index;
    Signature signature;
    std::array<int,2> top_orders;
    std::array<uint64_t,2> top_nodes;
    std::array<uint64_t,4> bottom_nodes;
};

const std::array<CaseData,40> CASES = {{
    {0, {{3,6,520,2056,144,8224,4160}}, {{25938,43246}}, {{92178,141761}}, {{56647,120705,75434,81474}}},
    {1, {{3,260,1028,24,144,8224,4160}}, {{38280,44956}}, {{123638,141398}}, {{81600,124347,98822,89580}}},
    {2, {{3,260,1028,2056,17,8224,4160}}, {{31436,11758}}, {{102875,41732}}, {{63061,32433,73990,21631}}},
    {3, {{3,260,1028,2056,2176,8224,4160}}, {{54360,97458}}, {{314910,464824}}, {{136964,234369,131597,240546}}},
    {4, {{3,260,1028,3072,144,8224,4160}}, {{62058,33856}}, {{364738,192590}}, {{143694,70520,133211,85249}}},
    {5, {{3,514,1028,1040,2176,8224,4160}}, {{36608,74470}}, {{239845,368481}}, {{92549,171604,91578,187650}}},
    {6, {{3,768,12,24,144,8224,4160}}, {{37792,36784}}, {{116076,115862}}, {{75975,88890,90848,71169}}},
    {7, {{3,768,12,2056,17,8224,4160}}, {{35088,1952}}, {{108565,9004}}, {{82435,5139,87691,4765}}},
    {8, {{3,768,12,2056,2176,8224,4160}}, {{242272,63472}}, {{963030,300702}}, {{596854,144800,552377,167712}}},
    {9, {{3,768,1536,24,144,8224,4160}}, {{137000,110242}}, {{614634,489820}}, {{344998,265387,330383,325903}}},
    {10, {{3,768,1536,2056,17,8224,4160}}, {{47082,27762}}, {{260262,170795}}, {{117839,67671,106105,80443}}},
    {11, {{3,768,1536,2056,2176,8224,4160}}, {{30188,87900}}, {{736288,1156920}}, {{59262,233554,81416,161984}}},
    {12, {{3,768,1536,3072,144,8224,4160}}, {{14456,21088}}, {{482832,491792}}, {{26452,57870,33185,36090}}},
    {13, {{130,260,1028,2056,144,8224,4160}}, {{31625,36322}}, {{190804,210358}}, {{73804,82857,66962,82932}}},
    {14, {{130,514,1028,24,17,8224,4160}}, {{12736,30382}}, {{41768,94826}}, {{25605,80657,32432,54944}}},
    {15, {{130,514,1028,2056,2049,8224,4160}}, {{49461,37950}}, {{256687,182133}}, {{119301,90282,112030,93181}}},
    {16, {{130,514,1028,3072,17,8224,4160}}, {{95076,26794}}, {{456896,132095}}, {{225198,65868,232189,73157}}},
    {17, {{130,768,12,2056,144,8224,4160}}, {{60230,28916}}, {{279121,162770}}, {{152468,68329,134710,73818}}},
    {18, {{130,768,1536,2056,144,8224,4160}}, {{12210,23754}}, {{323120,578006}}, {{24260,58923,31881,39452}}},
    {19, {{257,6,520,24,144,8224,4160}}, {{38592,19140}}, {{124330,64606}}, {{78727,57336,99399,33088}}},
    {20, {{257,6,520,2056,17,8224,4160}}, {{31380,42788}}, {{102076,136274}}, {{65126,135414,78018,69839}}},
    {21, {{257,6,520,2056,2176,8224,4160}}, {{54338,41512}}, {{315491,234872}}, {{134130,87738,119340,99686}}},
    {22, {{257,6,1028,1040,2176,8224,4160}}, {{42834,30624}}, {{286097,197404}}, {{101201,62904,98062,77367}}},
    {23, {{257,260,520,2056,144,8224,4160}}, {{42107,37196}}, {{253093,219356}}, {{97310,85311,100412,93548}}},
    {24, {{257,514,1028,1040,2049,8224,4160}}, {{38766,43067}}, {{205470,205924}}, {{94203,99785,83836,95953}}},
    {25, {{257,514,1536,1040,2176,8224,4160}}, {{26580,20408}}, {{621870,536088}}, {{47106,45523,68100,33706}}},
    {26, {{257,768,1028,1040,2176,8224,4160}}, {{40944,36908}}, {{697618,608342}}, {{85871,102149,114547,69618}}},
    {27, {{384,6,520,2056,144,8224,4160}}, {{58590,36774}}, {{321694,209154}}, {{151473,90586,127075,95938}}},
    {28, {{384,6,1028,24,17,8224,4160}}, {{21104,27304}}, {{67176,86981}}, {{40838,76541,55559,53531}}},
    {29, {{384,6,1028,2056,2049,8224,4160}}, {{80122,30830}}, {{396971,162086}}, {{189291,73256,184577,86366}}},
    {30, {{384,6,1028,3072,17,8224,4160}}, {{188696,140192}}, {{798064,577328}}, {{427684,305089,401107,360645}}},
    {31, {{384,514,12,24,17,8224,4160}}, {{7492,94444}}, {{26866,275124}}, {{14338,226892,16570,148032}}},
    {32, {{384,514,12,2056,2049,8224,4160}}, {{78808,78340}}, {{362221,311152}}, {{187056,175631,167448,178602}}},
    {33, {{384,514,1028,1040,2176,8224,4160}}, {{35440,18056}}, {{560782,294876}}, {{77083,56150,85701,31780}}},
    {34, {{384,514,1536,24,17,8224,4160}}, {{74560,64178}}, {{290555,323317}}, {{210533,153501,196624,172127}}},
    {35, {{384,514,1536,2056,2049,8224,4160}}, {{30164,22616}}, {{507504,451190}}, {{63365,55847,82694,44545}}},
    {36, {{384,514,1536,3072,17,8224,4160}}, {{45864,91216}}, {{633796,1133776}}, {{89713,216615,127360,158125}}},
    {37, {{384,768,1028,24,17,8224,4160}}, {{15222,134621}}, {{78246,535376}}, {{40253,308768,36404,328277}}},
    {38, {{384,768,1028,2056,2049,8224,4160}}, {{26436,47982}}, {{404506,531760}}, {{56054,136754,75077,85296}}},
    {39, {{384,768,1028,3072,17,8224,4160}}, {{27332,29372}}, {{425296,406230}}, {{61508,89104,87996,65634}}}
}};

int main(int argc,char**argv) {
    int requested_case = argc>1 ? std::stoi(argv[1]) : -1;
    int requested_orientation = argc>2 ? std::stoi(argv[2]) : -1;
    assert(requested_case < (int)CASES.size());
    assert(requested_orientation < 4);
    auto layer=generate_layer();
    std::map<Signature,std::vector<State>> groups;
    std::map<int,int> histogram;
    for (auto const& s:layer) { Signature sig{}; for(int i=0;i<N;++i)sig[i]=s[i]; groups[sig].push_back(s); }
    for (auto const& [sig,group]:groups) ++histogram[(int)group.size()];
    assert(histogram[14]==40);
    uint64_t aggregate_bottom=0; int checked=0;
    for (int case_index=0;case_index<(int)CASES.size();++case_index) {
        if (requested_case>=0 && case_index!=requested_case) continue;
        auto const& data=CASES[case_index]; auto it=groups.find(data.signature); assert(it!=groups.end());
        auto group=it->second; std::sort(group.begin(),group.end()); assert(group.size()==14);
        TopEnumerator top[2];
        for(int mode=0;mode<2;++mode) { top[mode].sig=data.signature; top[mode].run(mode); assert((int)top[mode].solutions.size()==data.top_orders[mode]); assert(top[mode].nodes==data.top_nodes[mode]); }
        BottomGroupSolver solver; solver.initialize(group); uint64_t local_total=0;
        for(int orientation=0;orientation<4;++orientation) {
            if(requested_orientation>=0 && orientation!=requested_orientation) continue;
            auto const& solutions=top[orientation%2].solutions; uint64_t total=0;
            for(auto const& assignment:solutions) { assert(!solver.solve_top(assignment,orientation)); total+=solver.nodes; }
            assert(total==data.bottom_nodes[orientation]); local_total+=total;
            std::cout << "case="<<case_index<<" global="<<data.global_index<<" orientation="<<orientation<<" top_orders="<<solutions.size()<<" bottom_nodes="<<total<<" PASS\n";
        }
        aggregate_bottom+=local_total; ++checked;
    }
    if(requested_case<0 && requested_orientation<0) { assert(checked==40); assert(aggregate_bottom==18773058ULL); std::cout<<"aggregate_bottom_nodes="<<aggregate_bottom<<" PASS\n"; }
}

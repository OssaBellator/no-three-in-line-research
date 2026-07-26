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

const std::array<CaseData,48> CASES = {{
    {0, {{3,6,1536,24,2176,8224,4160}}, {{48312,11832}}, {{272757,81426}}, {{137237,43075,158725,35081}}},
    {1, {{3,258,1028,24,2176,8224,4160}}, {{37556,47164}}, {{182718,211972}}, {{76537,102592,87957,98280}}},
    {2, {{3,258,1536,24,2176,8224,4160}}, {{62600,36200}}, {{678960,317492}}, {{139716,76863,136172,89378}}},
    {3, {{3,516,1028,24,2176,8224,4160}}, {{50120,63336}}, {{243154,279368}}, {{105080,140411,109430,129068}}},
    {4, {{3,516,1536,24,2176,8224,4160}}, {{78232,39448}}, {{479900,249812}}, {{170004,81509,160823,88084}}},
    {5, {{3,768,1028,24,2049,8224,4160}}, {{29776,39988}}, {{136520,181788}}, {{80355,107302,75963,101518}}},
    {6, {{129,6,1536,2056,17,8224,4160}}, {{56156,33292}}, {{252461,182128}}, {{120047,82531,117388,70290}}},
    {7, {{129,6,1536,2056,144,8224,4160}}, {{38704,18592}}, {{251669,138820}}, {{92042,42727,78979,37992}}},
    {8, {{129,258,12,1032,2064,8224,4160}}, {{30725,27622}}, {{141106,122908}}, {{61604,57144,70099,55585}}},
    {9, {{129,258,516,2056,2064,8224,4160}}, {{33207,30618}}, {{173136,147010}}, {{71690,65890,69189,63079}}},
    {10, {{129,258,516,3072,2064,8224,4160}}, {{28945,27212}}, {{448663,349229}}, {{60526,60449,63206,54407}}},
    {11, {{129,258,1028,1032,2064,8224,4160}}, {{33207,30618}}, {{174639,148308}}, {{67771,63242,72104,65616}}},
    {12, {{129,260,1536,2056,17,8224,4160}}, {{28888,34724}}, {{297266,401164}}, {{66947,79547,56798,73878}}},
    {13, {{129,260,1536,2056,144,8224,4160}}, {{17986,17524}}, {{343202,343657}}, {{38624,39006,37135,31350}}},
    {14, {{129,514,1028,24,2049,8224,4160}}, {{18240,20830}}, {{86765,100770}}, {{38035,46404,37410,38066}}},
    {15, {{129,514,1028,24,2176,8224,4160}}, {{47470,22338}}, {{238798,114192}}, {{108410,50980,94604,47918}}},
    {16, {{129,768,1028,24,2049,8224,4160}}, {{25800,53612}}, {{224234,427842}}, {{59049,119248,50515,108804}}},
    {17, {{129,768,1028,24,2176,8224,4160}}, {{59500,55516}}, {{584924,517514}}, {{126994,133074,120545,106507}}},
    {18, {{130,6,1536,2056,17,8224,4160}}, {{64848,24344}}, {{277842,134264}}, {{172744,71509,186692,74987}}},
    {19, {{130,768,1028,24,2176,8224,4160}}, {{59500,55516}}, {{584924,517514}}, {{158787,170837,158210,134740}}},
    {20, {{257,6,1536,24,129,8224,4160}}, {{51632,7008}}, {{239714,52976}}, {{109373,14917,109949,15832}}},
    {21, {{257,6,1536,24,2049,8224,4160}}, {{51632,7008}}, {{245790,52352}}, {{140287,21414,144255,20364}}},
    {22, {{257,6,1536,24,2064,8224,4160}}, {{88880,7572}}, {{387648,54590}}, {{190472,17300,204242,18238}}},
    {23, {{257,6,1536,2056,129,8224,4160}}, {{32220,20544}}, {{425028,317084}}, {{73651,43179,63175,47404}}},
    {24, {{257,6,1536,2056,2064,8224,4160}}, {{62064,22884}}, {{338389,151614}}, {{141014,47894,132894,53182}}},
    {25, {{257,258,1028,24,2176,8224,4160}}, {{54464,16740}}, {{290123,120842}}, {{114874,34793,120718,42226}}},
    {26, {{257,258,1536,24,2176,8224,4160}}, {{66208,7944}}, {{863408,237026}}, {{134416,17023,156038,18172}}},
    {27, {{257,260,1536,24,2176,8224,4160}}, {{66208,7944}}, {{863578,237196}}, {{176008,23684,200240,22727}}},
    {28, {{257,516,1028,24,2176,8224,4160}}, {{64168,25876}}, {{548106,248318}}, {{140250,55076,141902,60370}}},
    {29, {{257,516,1536,24,2176,8224,4160}}, {{67636,9224}}, {{868258,236500}}, {{142291,20319,152241,20120}}},
    {30, {{258,6,1536,2056,17,8224,4160}}, {{64848,24344}}, {{278866,134472}}, {{134978,53539,144451,58971}}},
    {31, {{258,6,1536,2056,144,8224,4160}}, {{36332,14302}}, {{453668,242994}}, {{79493,28925,78003,36701}}},
    {32, {{258,260,1536,2056,17,8224,4160}}, {{38160,35928}}, {{201682,216598}}, {{84250,76614,85793,86096}}},
    {33, {{258,260,1536,2056,144,8224,4160}}, {{20378,21102}}, {{379113,397229}}, {{42037,44838,43918,44061}}},
    {34, {{258,514,1028,24,2049,8224,4160}}, {{19722,21120}}, {{93929,98798}}, {{38706,45869,43079,42047}}},
    {35, {{258,514,1028,24,2176,8224,4160}}, {{48444,19948}}, {{437926,195784}}, {{106320,43911,106734,49310}}},
    {36, {{258,516,12,2064,129,8224,4160}}, {{23220,21578}}, {{108365,98103}}, {{45335,43634,50899,44135}}},
    {37, {{258,516,1028,2064,129,8224,4160}}, {{28617,25299}}, {{316400,276606}}, {{56434,50437,59449,54033}}},
    {38, {{258,516,1032,2056,129,8224,4160}}, {{33207,30618}}, {{346029,321041}}, {{68695,63998,70863,64548}}},
    {39, {{258,516,1032,3072,129,8224,4160}}, {{28945,27212}}, {{421427,346041}}, {{57287,58270,64151,55513}}},
    {40, {{258,768,1028,24,2049,8224,4160}}, {{28256,40610}}, {{138499,197985}}, {{60738,82364,61820,98417}}},
    {41, {{258,768,1028,24,2176,8224,4160}}, {{74092,39456}}, {{718182,463866}}, {{151203,86341,166260,88160}}},
    {42, {{384,6,1536,24,129,8224,4160}}, {{85736,2688}}, {{381092,33033}}, {{199562,5423,178684,6941}}},
    {43, {{384,6,1536,24,2064,8224,4160}}, {{136944,2352}}, {{918506,81902}}, {{327146,5127,298490,6273}}},
    {44, {{384,6,1536,24,2176,8224,4160}}, {{116576,544}}, {{1151956,48020}}, {{346074,1918,331660,1633}}},
    {45, {{384,6,1536,2056,129,8224,4160}}, {{39308,7664}}, {{542468,191474}}, {{92185,16049,82224,16751}}},
    {46, {{384,6,1536,2056,2064,8224,4160}}, {{62336,9664}}, {{737944,227718}}, {{134806,20339,129136,21930}}},
    {47, {{384,260,1536,2056,17,8224,4160}}, {{25924,41392}}, {{298460,614176}}, {{71988,112310,78641,107160}}}
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
    assert(histogram[13]==48);
    uint64_t aggregate_bottom=0; int checked=0;
    for (int case_index=0;case_index<(int)CASES.size();++case_index) {
        if (requested_case>=0 && case_index!=requested_case) continue;
        auto const& data=CASES[case_index]; auto it=groups.find(data.signature); assert(it!=groups.end());
        auto group=it->second; std::sort(group.begin(),group.end()); assert(group.size()==13);
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
    if(requested_case<0 && requested_orientation<0) { assert(checked==48); assert(aggregate_bottom==16329713ULL); std::cout<<"aggregate_bottom_nodes="<<aggregate_bottom<<" PASS\n"; }
}

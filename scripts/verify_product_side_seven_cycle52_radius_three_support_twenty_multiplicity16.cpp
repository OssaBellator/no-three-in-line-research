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

const std::array<CaseData,38> CASES = {{
    {0, {{3,260,520,2056,144,8224,4160}}, {{33292,32772}}, {{165230,158456}}, {{88159,96048,93251,84060}}},
    {1, {{3,260,1028,24,2176,8224,4160}}, {{50120,63336}}, {{241958,277284}}, {{139922,190752,151097,172939}}},
    {2, {{3,260,1536,24,144,8224,4160}}, {{75808,46940}}, {{330748,200808}}, {{221494,152232,218245,133745}}},
    {3, {{3,260,1536,2056,17,8224,4160}}, {{37630,25880}}, {{190996,142449}}, {{100479,83487,98041,69472}}},
    {4, {{3,260,1536,2056,2176,8224,4160}}, {{20892,68488}}, {{457322,746982}}, {{56242,192579,57742,168065}}},
    {5, {{3,260,1536,3072,144,8224,4160}}, {{17190,38900}}, {{399526,536386}}, {{44688,111667,47126,96986}}},
    {6, {{3,514,1028,2056,144,8224,4160}}, {{20031,18316}}, {{107223,94197}}, {{47609,47545,50927,44998}}},
    {7, {{3,768,12,24,2176,8224,4160}}, {{145816,86096}}, {{525898,371572}}, {{433643,241721,447194,269591}}},
    {8, {{3,768,1028,1040,2176,8224,4160}}, {{46448,56792}}, {{575228,620290}}, {{134795,174197,137602,159539}}},
    {9, {{3,768,1536,24,2176,8224,4160}}, {{87344,92856}}, {{1066828,879040}}, {{236202,266064,257546,259597}}},
    {10, {{130,260,1028,2056,17,8224,4160}}, {{27650,21538}}, {{127116,100933}}, {{68466,59806,76280,55697}}},
    {11, {{130,260,1536,2056,144,8224,4160}}, {{17986,17524}}, {{343202,343657}}, {{48161,46940,48159,40063}}},
    {12, {{130,514,1028,24,2049,8224,4160}}, {{19722,21120}}, {{93875,98554}}, {{48771,58295,54197,53762}}},
    {13, {{130,768,12,2056,17,8224,4160}}, {{26232,8532}}, {{110924,36497}}, {{75144,23236,80428,26963}}},
    {14, {{130,768,1028,24,17,8224,4160}}, {{12760,44594}}, {{59300,173867}}, {{36211,124523,36800,121352}}},
    {15, {{130,768,1028,2056,2049,8224,4160}}, {{32322,31070}}, {{383741,297086}}, {{89653,98422,91038,78981}}},
    {16, {{130,768,1028,3072,17,8224,4160}}, {{47256,8916}}, {{482116,123971}}, {{131515,30784,153616,29712}}},
    {17, {{130,768,1536,2056,17,8224,4160}}, {{19364,31316}}, {{246402,380754}}, {{52286,86247,62577,87493}}},
    {18, {{257,6,520,24,2176,8224,4160}}, {{47256,8916}}, {{228140,57306}}, {{131164,30913,149870,29182}}},
    {19, {{257,6,1028,2056,144,8224,4160}}, {{27543,23483}}, {{141945,120923}}, {{65947,61111,74508,59856}}},
    {20, {{257,6,1536,1040,2176,8224,4160}}, {{26232,8532}}, {{532716,254634}}, {{74107,22680,78829,26303}}},
    {21, {{257,514,12,2056,144,8224,4160}}, {{30725,27622}}, {{136871,123580}}, {{76046,71030,84922,66013}}},
    {22, {{257,514,1028,24,144,8224,4160}}, {{28945,27212}}, {{125031,117584}}, {{73672,75773,78191,64801}}},
    {23, {{257,514,1028,2056,17,8224,4160}}, {{16133,19293}}, {{78256,91428}}, {{39153,52305,39456,41532}}},
    {24, {{257,514,1028,2056,2176,8224,4160}}, {{30725,27622}}, {{415575,342211}}, {{76869,74401,80895,65113}}},
    {25, {{257,514,1028,3072,144,8224,4160}}, {{28945,27212}}, {{421739,346899}}, {{70302,71732,78416,65657}}},
    {26, {{257,514,1536,2056,144,8224,4160}}, {{23220,21578}}, {{387983,378398}}, {{55493,53790,62063,53267}}},
    {27, {{257,768,1028,2056,144,8224,4160}}, {{18863,17537}}, {{290986,282307}}, {{45167,46008,51079,44601}}},
    {28, {{384,6,520,2056,17,8224,4160}}, {{46448,56792}}, {{204903,254090}}, {{135800,176208,137704,159908}}},
    {29, {{384,6,1028,24,2049,8224,4160}}, {{30348,7652}}, {{137144,47692}}, {{74652,23649,83161,23579}}},
    {30, {{384,6,1536,24,17,8224,4160}}, {{85328,13576}}, {{312404,78098}}, {{257176,44562,264294,45370}}},
    {31, {{384,6,1536,2056,2049,8224,4160}}, {{62336,9664}}, {{737018,226792}}, {{179121,29001,181271,30917}}},
    {32, {{384,6,1536,3072,17,8224,4160}}, {{145816,86096}}, {{1155440,978804}}, {{429438,239277,443911,265958}}},
    {33, {{384,514,12,24,2049,8224,4160}}, {{17190,38900}}, {{78126,155113}}, {{45100,112681,47213,96820}}},
    {34, {{384,514,1028,1040,2049,8224,4160}}, {{33292,32772}}, {{369513,330320}}, {{88427,97709,93259,83241}}},
    {35, {{384,514,1028,2056,144,8224,4160}}, {{16314,22494}}, {{263433,312720}}, {{41042,61585,39204,48315}}},
    {36, {{384,514,1536,24,2049,8224,4160}}, {{55036,9972}}, {{481984,213692}}, {{153745,26639,168670,29628}}},
    {37, {{384,768,1028,24,2049,8224,4160}}, {{21272,42564}}, {{206545,422392}}, {{55888,124820,64141,111696}}}
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
    assert(histogram[16]==38);
    uint64_t aggregate_bottom=0; int checked=0;
    for (int case_index=0;case_index<(int)CASES.size();++case_index) {
        if (requested_case>=0 && case_index!=requested_case) continue;
        auto const& data=CASES[case_index]; auto it=groups.find(data.signature); assert(it!=groups.end());
        auto group=it->second; std::sort(group.begin(),group.end()); assert(group.size()==16);
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
    if(requested_case<0 && requested_orientation<0) { assert(checked==38); assert(aggregate_bottom==15629863ULL); std::cout<<"aggregate_bottom_nodes="<<aggregate_bottom<<" PASS\n"; }
}

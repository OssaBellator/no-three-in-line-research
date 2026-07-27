#include <bits/stdc++.h>
using namespace std;

struct Lines { vector<vector<int>> cell_lines; int count; };

Lines make_lines(int n) {
    vector<vector<int>> cell_lines(n * n);
    int line_id = 0;
    for (int dx = 1; dx < n; ++dx) for (int dy = -(n - 1); dy < n; ++dy) {
        if (dy == 0 || gcd(abs(dx), abs(dy)) != 1) continue;
        for (int x = 0; x < n; ++x) for (int y = 0; y < n; ++y) {
            if (0 <= x-dx && x-dx < n && 0 <= y-dy && y-dy < n) continue;
            vector<int> points;
            for (int X=x,Y=y; 0<=X&&X<n&&0<=Y&&Y<n; X+=dx,Y+=dy)
                points.push_back(X*n+Y);
            if (points.size() >= 3) {
                for (int cell : points) cell_lines[cell].push_back(line_id);
                ++line_id;
            }
        }
    }
    return {move(cell_lines), line_id};
}

array<int,4> orbit_cells(int i, int j, int e, int n) {
    int I=n-1-i, J=n-1-j;
    if (!e) return {i*n+j, I*n+J, j*n+I, J*n+i};
    return {i*n+J, I*n+j, j*n+i, J*n+I};
}

long long det(pair<int,int> a, pair<int,int> b, pair<int,int> c) {
    return 1LL*(b.first-a.first)*(c.second-a.second)
         - 1LL*(b.second-a.second)*(c.first-a.first);
}

int main(int argc, char **argv) {
    const int max_support = argc > 1 ? atoi(argv[1]) : 5;
    const int shard = argc > 2 ? atoi(argv[2]) : 0;
    const int shards = argc > 3 ? atoi(argv[3]) : 1;
    if (max_support < 1 || max_support > 6 || shard < 0 || shards < 1 || shard >= shards) {
        cerr << "usage: checker [max_support<=6] [shard] [shards]\n";
        return 2;
    }
    const int n=36, m=18;
    const int sigma_one[n] = {
        22,36,24,16,25,9,14,6,32,8,26,17,7,33,19,3,35,27,
        10,2,34,18,4,30,20,11,29,5,31,23,28,12,21,13,1,15
    };
    const int expected_tau_one[n] = {
        2,17,21,14,9,29,24,27,31,18,11,5,3,30,1,33,25,15,
        22,12,4,36,7,34,32,26,19,6,10,13,8,28,23,16,20,35
    };
    const long long expected[7] = {0,3,225,9500,347811,11090546,315267140};

    vector<int> sigma(n), tau(n), inverse(n), rho(m), sign(m);
    for (int x=0; x<n; ++x) sigma[x]=sigma_one[x]-1;
    for (int x=0; x<n; ++x) inverse[sigma[x]]=x;
    for (int x=0; x<n; ++x) tau[x]=inverse[n-1-x];
    for (int x=0; x<n; ++x) if (tau[x] != expected_tau_one[x]-1) {
        cerr << "forced tau mismatch\n"; return 2;
    }
    for (int i=0; i<m; ++i) {
        int y=sigma[i]; rho[i]=y<m?y:n-1-y; sign[i]=y<m?0:1;
    }
    vector<int> sorted_rho=rho; sort(sorted_rho.begin(),sorted_rho.end());
    for (int i=0;i<m;++i) if (sorted_rho[i]!=i) { cerr<<"rho not permutation\n";return 2; }

    vector<pair<int,int>> selected;
    for (int x=0;x<n;++x) selected.push_back({x,sigma[x]});
    for (int x=0;x<n;++x) selected.push_back({x,tau[x]});
    int determinant_checks=0, zero_determinants=0;
    for (int a=0;a<2*n;++a) for (int b=a+1;b<2*n;++b) for (int c=b+1;c<2*n;++c) {
        ++determinant_checks;
        zero_determinants += det(selected[a],selected[b],selected[c])==0;
    }
    if (determinant_checks != 59640 || zero_determinants != 4) {
        cerr << "near-state determinant audit failed\n"; return 2;
    }

    auto geometry=make_lines(n);
    if (geometry.count != 70726) { cerr<<"line count mismatch\n"; return 2; }
    auto variable_id=[&](int i,int j,int e){return (i*m+j)*2+e;};
    vector<array<int,4>> blocks(m*m*2);
    for (int i=0;i<m;++i) for (int j=0;j<m;++j) for (int e=0;e<2;++e)
        blocks[variable_id(i,j,e)]=orbit_cells(i,j,e,n);

    vector<int> occupancy(geometry.count), owner(n*n,-1);
    for (int i=0;i<m;++i) for (int cell:blocks[variable_id(i,rho[i],sign[i])]) {
        if (owner[cell]!=-1) { cerr<<"duplicate base orbit\n"; return 2; }
        owner[cell]=i;
        for (int line:geometry.cell_lines[cell]) ++occupancy[line];
    }
    vector<int> bad_lines;
    for (int line=0;line<geometry.count;++line) if (occupancy[line]>2) bad_lines.push_back(line);
    if (bad_lines.size()!=4) { cerr<<"expected four overloaded lines\n"; return 2; }
    set<int> bad_owners;
    for (int cell=0;cell<n*n;++cell) if (owner[cell]>=0) {
        for (int line:geometry.cell_lines[cell])
            if (find(bad_lines.begin(),bad_lines.end(),line)!=bad_lines.end()) bad_owners.insert(owner[cell]);
    }
    if (bad_owners != set<int>({2,14,16})) { cerr<<"bad orbit-owner set mismatch\n"; return 2; }

    vector<vector<vector<int>>> permutations(max_support+1);
    for (int k=1;k<=max_support;++k) {
        vector<int> p(k); iota(p.begin(),p.end(),0);
        do permutations[k].push_back(p); while(next_permutation(p.begin(),p.end()));
    }
    vector<int> remove_mark(geometry.count), remove_delta(geometry.count);
    vector<int> add_mark(geometry.count), add_delta(geometry.count);
    int remove_generation=0, add_generation=0;
    long long checked[7]={};

    auto no_duplicate_reverse=[&](const vector<int>&support,const vector<int>&new_rho,const vector<int>&new_sign){
        vector<int> R=rho,E=sign;
        for (int q=0;q<(int)support.size();++q) R[support[q]]=new_rho[q],E[support[q]]=new_sign[q];
        for (int i=0;i<m;++i) { int j=R[i]; if (i<j && R[j]==i && (E[i]^E[j])) return false; }
        return true;
    };
    auto unexpected_repair=[&](const vector<int>&support,const vector<int>&new_rho,const vector<int>&new_sign){
        cerr << "unexpected repair at support " << support.size() << "\n";
        exit(3);
    };

    for (int k=1;k<=max_support;++k) {
        vector<int> support(k);
        long long subset_index=0;
        function<void(int,int)> enumerate_support=[&](int position,int lower) {
            if (position<k) {
                for (int x=lower;x<=m-(k-position);++x) { support[position]=x; enumerate_support(position+1,x+1); }
                return;
            }
            bool hits=false; for (int i:support) hits |= bad_owners.count(i)>0;
            if (!hits) return;
            if (k==max_support && shards>1 && subset_index++%shards!=shard) return;

            ++remove_generation;
            for (int i:support) for (int cell:blocks[variable_id(i,rho[i],sign[i])])
                for (int line:geometry.cell_lines[cell]) {
                    if (remove_mark[line]!=remove_generation) remove_mark[line]=remove_generation,remove_delta[line]=0;
                    --remove_delta[line];
                }
            vector<int> old_targets(k), new_rho(k), new_sign(k);
            for (int q=0;q<k;++q) old_targets[q]=rho[support[q]];

            for (const auto &permutation:permutations[k]) {
                for (int q=0;q<k;++q) new_rho[q]=old_targets[permutation[q]];
                for (int mask=0;mask<(1<<k);++mask) {
                    bool canonical=true, exact=true;
                    for (int q=0;q<k;++q) {
                        int i=support[q]; new_sign[q]=(mask>>q)&1;
                        if (new_rho[q]==i && new_sign[q]!=0) canonical=false;
                        int old_e=rho[i]==i?0:sign[i];
                        int new_e=new_rho[q]==i?0:new_sign[q];
                        if (new_rho[q]==rho[i] && new_e==old_e) exact=false;
                    }
                    if (!canonical || !exact) continue;
                    ++checked[k];
                    if (!no_duplicate_reverse(support,new_rho,new_sign)) continue;

                    ++add_generation;
                    bool valid=true;
                    for (int q=0;q<k && valid;++q) {
                        int i=support[q];
                        for (int cell:blocks[variable_id(i,new_rho[q],new_sign[q])]) {
                            if (owner[cell]!=-1 && find(support.begin(),support.end(),owner[cell])==support.end()) { valid=false; break; }
                            for (int line:geometry.cell_lines[cell]) {
                                int current=occupancy[line]
                                    +(remove_mark[line]==remove_generation?remove_delta[line]:0)
                                    +(add_mark[line]==add_generation?add_delta[line]:0);
                                if (current>=2) { valid=false; break; }
                                if (add_mark[line]!=add_generation) add_mark[line]=add_generation,add_delta[line]=0;
                                ++add_delta[line];
                            }
                            if (!valid) break;
                        }
                    }
                    if (valid) for (int line:bad_lines) {
                        int current=occupancy[line]
                            +(remove_mark[line]==remove_generation?remove_delta[line]:0)
                            +(add_mark[line]==add_generation?add_delta[line]:0);
                        if (current>2) { valid=false; break; }
                    }
                    if (valid) unexpected_repair(support,new_rho,new_sign);
                }
            }
        };
        enumerate_support(0,0);
        if (!(k==max_support && shards>1) && checked[k]!=expected[k]) {
            cerr << "candidate count mismatch at support " << k << "\n"; return 2;
        }
    }

    cout << "{\n  \"outcome\": \"no_swapped_orbit_repair_in_shard\",\n"
         << "  \"p\": 37,\n  \"max_pair_support\": " << max_support << ",\n"
         << "  \"shard\": " << shard << ",\n  \"shards\": " << shards << ",\n"
         << "  \"determinant_checks\": " << determinant_checks << ",\n"
         << "  \"zero_determinants_in_near_state\": " << zero_determinants << ",\n"
         << "  \"maximal_nonaxis_lines\": " << geometry.count << ",\n"
         << "  \"candidates_at_max_support_in_shard\": " << checked[max_support] << ",\n"
         << "  \"repair_found\": false,\n  \"asymptotic_seed_theorem_proved\": false\n}\n";
    return 0;
}

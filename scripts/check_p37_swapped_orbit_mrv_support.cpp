#include <algorithm>
#include <array>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

struct Lines {
    vector<vector<int>> cell_lines;
    int count;
};

Lines make_lines(int n) {
    vector<vector<int>> cell_lines(n * n);
    int line_id = 0;
    for (int dx = 1; dx < n; ++dx) {
        for (int dy = -(n - 1); dy < n; ++dy) {
            if (dy == 0 || gcd(abs(dx), abs(dy)) != 1) continue;
            for (int x = 0; x < n; ++x) {
                for (int y = 0; y < n; ++y) {
                    if (0 <= x - dx && x - dx < n &&
                        0 <= y - dy && y - dy < n) continue;
                    vector<int> points;
                    for (int X = x, Y = y;
                         0 <= X && X < n && 0 <= Y && Y < n;
                         X += dx, Y += dy) {
                        points.push_back(X * n + Y);
                    }
                    if (points.size() >= 3) {
                        for (int cell : points) cell_lines[cell].push_back(line_id);
                        ++line_id;
                    }
                }
            }
        }
    }
    return {move(cell_lines), line_id};
}

array<int, 4> orbit_cells(int i, int j, int orientation, int n) {
    int I = n - 1 - i;
    int J = n - 1 - j;
    if (orientation == 0) return {i * n + j, I * n + J, j * n + I, J * n + i};
    return {i * n + J, I * n + j, j * n + i, J * n + I};
}

long long determinant(pair<int, int> a, pair<int, int> b, pair<int, int> c) {
    return 1LL * (b.first - a.first) * (c.second - a.second)
         - 1LL * (b.second - a.second) * (c.first - a.first);
}

long long choose(int n, int k) {
    if (k < 0 || k > n) return 0;
    k = min(k, n - k);
    long long answer = 1;
    for (int i = 1; i <= k; ++i) answer = answer * (n - k + i) / i;
    return answer;
}

int main(int argc, char** argv) {
    int support_size = argc > 1 ? atoi(argv[1]) : 7;
    int shard = argc > 2 ? atoi(argv[2]) : 0;
    int shard_count = argc > 3 ? atoi(argv[3]) : 1;
    if (support_size < 7 || support_size > 11 ||
        shard < 0 || shard_count < 1 || shard >= shard_count) {
        cerr << "usage: checker [support 7..11] [shard] [shard_count]\n";
        return 2;
    }

    const int n = 36;
    const int m = 18;
    const int sigma_one[n] = {
        22,36,24,16,25,9,14,6,32,8,26,17,7,33,19,3,35,27,
        10,2,34,18,4,30,20,11,29,5,31,23,28,12,21,13,1,15
    };
    const int tau_one[n] = {
        2,17,21,14,9,29,24,27,31,18,11,5,3,30,1,33,25,15,
        22,12,4,36,7,34,32,26,19,6,10,13,8,28,23,16,20,35
    };

    vector<int> sigma(n), inverse(n), tau(n), rho(m), sign(m);
    for (int x = 0; x < n; ++x) sigma[x] = sigma_one[x] - 1;
    for (int x = 0; x < n; ++x) inverse[sigma[x]] = x;
    for (int x = 0; x < n; ++x) tau[x] = inverse[n - 1 - x];
    for (int x = 0; x < n; ++x) {
        if (tau[x] != tau_one[x] - 1) {
            cerr << "forced second layer mismatch\n";
            return 2;
        }
    }
    for (int i = 0; i < m; ++i) {
        int image = sigma[i];
        rho[i] = image < m ? image : n - 1 - image;
        sign[i] = image < m ? 0 : 1;
    }
    vector<int> sorted_rho = rho;
    sort(sorted_rho.begin(), sorted_rho.end());
    for (int i = 0; i < m; ++i) {
        if (sorted_rho[i] != i) {
            cerr << "pair map is not a permutation\n";
            return 2;
        }
    }

    vector<pair<int, int>> selected;
    for (int x = 0; x < n; ++x) selected.push_back({x, sigma[x]});
    for (int x = 0; x < n; ++x) selected.push_back({x, tau[x]});
    int determinant_checks = 0;
    int zero_determinants = 0;
    for (int a = 0; a < 2 * n; ++a) {
        for (int b = a + 1; b < 2 * n; ++b) {
            for (int c = b + 1; c < 2 * n; ++c) {
                ++determinant_checks;
                if (determinant(selected[a], selected[b], selected[c]) == 0) {
                    ++zero_determinants;
                }
            }
        }
    }
    if (determinant_checks != 59640 || zero_determinants != 4) {
        cerr << "near-state determinant audit failed\n";
        return 2;
    }

    Lines geometry = make_lines(n);
    if (geometry.count != 70726) {
        cerr << "maximal-line count mismatch\n";
        return 2;
    }
    auto variable_id = [m](int i, int j, int orientation) {
        return (i * m + j) * 2 + orientation;
    };

    vector<array<int, 4>> blocks(m * m * 2);
    vector<vector<pair<int, int>>> block_line_coefficients(m * m * 2);
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            for (int orientation = 0; orientation < 2; ++orientation) {
                int variable = variable_id(i, j, orientation);
                blocks[variable] = orbit_cells(i, j, orientation, n);
                unordered_map<int, int> coefficient;
                for (int cell : blocks[variable]) {
                    for (int line : geometry.cell_lines[cell]) ++coefficient[line];
                }
                block_line_coefficients[variable].assign(
                    coefficient.begin(), coefficient.end()
                );
            }
        }
    }

    vector<int> base_occupancy(geometry.count, 0);
    vector<int> base_owner(n * n, -1);
    for (int i = 0; i < m; ++i) {
        for (int cell : blocks[variable_id(i, rho[i], sign[i])]) {
            if (base_owner[cell] != -1) {
                cerr << "duplicate base orbit\n";
                return 2;
            }
            base_owner[cell] = i;
            for (int line : geometry.cell_lines[cell]) ++base_occupancy[line];
        }
    }

    vector<int> bad_lines;
    for (int line = 0; line < geometry.count; ++line) {
        if (base_occupancy[line] > 2) bad_lines.push_back(line);
    }
    if (bad_lines.size() != 4) {
        cerr << "expected four overloaded lines\n";
        return 2;
    }
    set<int> bad_owners;
    for (int cell = 0; cell < n * n; ++cell) {
        if (base_owner[cell] < 0) continue;
        for (int line : geometry.cell_lines[cell]) {
            if (find(bad_lines.begin(), bad_lines.end(), line) != bad_lines.end()) {
                bad_owners.insert(base_owner[cell]);
            }
        }
    }
    if (bad_owners != set<int>({2, 14, 16})) {
        cerr << "bad-owner set mismatch\n";
        return 2;
    }

    const int k = support_size;
    vector<int> support(k), new_target(k), new_sign(k);
    vector<char> assigned(k, false), target_used(k, false);
    vector<int> cell_occupancy(n * n, 0);
    vector<int> line_occupancy = base_occupancy;
    long long eligible_subset_index = 0;
    long long subsets_in_shard = 0;
    long long search_nodes = 0;
    long long complete_leaves = 0;
    bool repair_found = false;

    auto add_block = [&](int i, int j, int orientation, int delta) {
        int variable = variable_id(i, j, orientation);
        for (int cell : blocks[variable]) cell_occupancy[cell] += delta;
        for (auto [line, coefficient] : block_line_coefficients[variable]) {
            line_occupancy[line] += delta * coefficient;
        }
    };

    auto block_is_legal = [&](int support_position, int j, int orientation) {
        int i = support[support_position];
        int old_orientation = rho[i] == i ? 0 : sign[i];
        int canonical_new_orientation = j == i ? 0 : orientation;
        if (j == rho[i] && canonical_new_orientation == old_orientation) return false;
        if (j == i && orientation != 0) return false;

        int variable = variable_id(i, j, orientation);
        for (int cell : blocks[variable]) {
            if (cell_occupancy[cell] != 0) return false;
        }
        for (auto [line, coefficient] : block_line_coefficients[variable]) {
            if (line_occupancy[line] + coefficient > 2) return false;
        }
        return true;
    };

    function<void(int)> search = [&](int depth) {
        ++search_nodes;
        if (repair_found) return;
        if (depth == k) {
            ++complete_leaves;
            repair_found = true;
            return;
        }

        int chosen_position = -1;
        vector<pair<int, int>> chosen_candidates;
        size_t minimum_domain = static_cast<size_t>(-1);
        for (int position = 0; position < k; ++position) {
            if (assigned[position]) continue;
            vector<pair<int, int>> candidates;
            for (int target_position = 0; target_position < k; ++target_position) {
                if (target_used[target_position]) continue;
                int target = rho[support[target_position]];
                for (int orientation = 0; orientation < 2; ++orientation) {
                    if (block_is_legal(position, target, orientation)) {
                        candidates.push_back({target_position, orientation});
                    }
                }
            }
            if (candidates.empty()) return;
            if (candidates.size() < minimum_domain) {
                minimum_domain = candidates.size();
                chosen_position = position;
                chosen_candidates = move(candidates);
                if (minimum_domain == 1) break;
            }
        }

        assigned[chosen_position] = true;
        int source = support[chosen_position];
        for (auto [target_position, orientation] : chosen_candidates) {
            int target = rho[support[target_position]];
            target_used[target_position] = true;
            new_target[chosen_position] = target;
            new_sign[chosen_position] = orientation;
            add_block(source, target, orientation, 1);
            search(depth + 1);
            add_block(source, target, orientation, -1);
            target_used[target_position] = false;
            if (repair_found) break;
        }
        assigned[chosen_position] = false;
    };

    function<void(int, int)> enumerate_supports = [&](int position, int lower) {
        if (repair_found) return;
        if (position < k) {
            for (int value = lower; value <= m - (k - position); ++value) {
                support[position] = value;
                enumerate_supports(position + 1, value + 1);
                if (repair_found) return;
            }
            return;
        }

        bool hits_bad_owner = false;
        for (int value : support) hits_bad_owner |= bad_owners.count(value) != 0;
        if (!hits_bad_owner) return;
        long long index = eligible_subset_index++;
        if (index % shard_count != shard) return;
        ++subsets_in_shard;

        fill(cell_occupancy.begin(), cell_occupancy.end(), 0);
        line_occupancy = base_occupancy;
        for (int i = 0; i < m; ++i) {
            for (int cell : blocks[variable_id(i, rho[i], sign[i])]) {
                cell_occupancy[cell] = 1;
            }
        }
        for (int i : support) add_block(i, rho[i], sign[i], -1);

        for (int line : bad_lines) {
            if (line_occupancy[line] > 2) return;
        }
        fill(assigned.begin(), assigned.end(), false);
        fill(target_used.begin(), target_used.end(), false);
        search(0);
    };

    enumerate_supports(0, 0);

    long long eligible_total = choose(18, k) - choose(15, k);
    if (eligible_subset_index != eligible_total) {
        cerr << "eligible-subset count mismatch\n";
        return 2;
    }
    if (repair_found || complete_leaves != 0) {
        cerr << "unexpected repair at support " << k << "\n";
        return 3;
    }

    cout << "{\n"
         << "  \"outcome\": \"no_p37_swapped_orbit_repair_in_mrv_shard\",\n"
         << "  \"support\": " << k << ",\n"
         << "  \"shard\": " << shard << ",\n"
         << "  \"shards\": " << shard_count << ",\n"
         << "  \"eligible_subsets_total\": " << eligible_total << ",\n"
         << "  \"eligible_subsets_in_shard\": " << subsets_in_shard << ",\n"
         << "  \"mrv_nodes\": " << search_nodes << ",\n"
         << "  \"complete_feasible_leaves\": " << complete_leaves << ",\n"
         << "  \"repair_found\": false,\n"
         << "  \"determinant_checks_in_near_state\": " << determinant_checks << ",\n"
         << "  \"zero_determinants_in_near_state\": " << zero_determinants << ",\n"
         << "  \"maximal_nonaxis_lines\": " << geometry.count << ",\n"
         << "  \"asymptotic_seed_theorem_proved\": false\n"
         << "}\n";
    return 0;
}

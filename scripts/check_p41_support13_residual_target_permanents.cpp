#include <bits/stdc++.h>
using namespace std;

struct Option {
    int source;
    int target;
    int orientation;
    int orbit_id;
    vector<pair<int, uint8_t>> line_counts;
};

static string decimal(__uint128_t value) {
    if (value == 0) return "0";
    string result;
    while (value) {
        result.push_back(char('0' + value % 10));
        value /= 10;
    }
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    constexpr int n = 40;
    constexpr int m = 20;
    constexpr int support_size = 13;
    const int rho_one_based[m] = {
        19,20,13,14,10,6,11,2,16,1,8,4,15,7,18,12,3,17,5,9
    };
    const int base_orientation[m] = {
        1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1
    };
    vector<int> rho(m);
    for (int i = 0; i < m; ++i) rho[i] = rho_one_based[i] - 1;

    vector<vector<int>> cell_lines(n * n);
    int line_count = 0;
    for (int dx = 1; dx < n; ++dx) {
        for (int dy = -(n - 1); dy < n; ++dy) {
            if (dy == 0 || gcd(dx, abs(dy)) != 1) continue;
            for (int x = 0; x < n; ++x) {
                for (int y = 0; y < n; ++y) {
                    if (0 <= x - dx && x - dx < n &&
                        0 <= y - dy && y - dy < n) continue;
                    vector<int> cells;
                    for (int X = x, Y = y;
                         0 <= X && X < n && 0 <= Y && Y < n;
                         X += dx, Y += dy) {
                        cells.push_back(X * n + Y);
                    }
                    if (cells.size() >= 3) {
                        for (int cell : cells) cell_lines[cell].push_back(line_count);
                        ++line_count;
                    }
                }
            }
        }
    }
    if (line_count != 108190) {
        cerr << "unexpected maximal-line count " << line_count << '\n';
        return 2;
    }

    auto canonical_orbit_id = [&](int source, int target, int sign) {
        if (source == target) return source * m + source;
        if (source < target) return m * m + 2 * (source * m + target) + sign;
        return m * m + 2 * (target * m + source) + 1 - sign;
    };

    vector<Option> options;
    vector<vector<vector<int>>> by_source_target(
        m, vector<vector<int>>(m)
    );
    for (int source = 0; source < m; ++source) {
        for (int target = 0; target < m; ++target) {
            for (int sign = 0; sign < (source == target ? 1 : 2); ++sign) {
                const int reverse_source = n - 1 - source;
                const int reverse_target = n - 1 - target;
                array<int, 4> cells = !sign
                    ? array<int, 4>{
                        source * n + target,
                        reverse_source * n + reverse_target,
                        target * n + reverse_source,
                        reverse_target * n + source
                    }
                    : array<int, 4>{
                        source * n + reverse_target,
                        reverse_source * n + target,
                        target * n + source,
                        reverse_target * n + reverse_source
                    };
                unordered_map<int, int> counts;
                for (int cell : cells) {
                    for (int line : cell_lines[cell]) ++counts[line];
                }
                Option option{
                    source, target, sign,
                    canonical_orbit_id(source, target, sign), {}
                };
                for (auto [line, count] : counts) {
                    option.line_counts.push_back({line, static_cast<uint8_t>(count)});
                }
                const int id = static_cast<int>(options.size());
                options.push_back(move(option));
                by_source_target[source][target].push_back(id);
            }
        }
    }

    vector<int> base_option(m), base_occupancy(line_count, 0);
    for (int source = 0; source < m; ++source) {
        const int sign = rho[source] == source ? 0 : base_orientation[source];
        for (int id : by_source_target[source][rho[source]]) {
            if (options[id].orientation == sign) base_option[source] = id;
        }
        for (auto [line, count] : options[base_option[source]].line_counts) {
            base_occupancy[line] += count;
        }
    }

    vector<array<int, support_size>> supports;
    array<int, support_size> support;
    iota(support.begin(), support.end(), 0);
    while (true) {
        bool owner_hit = false;
        for (int source : support) {
            if (source == 14 || source == 17 || source == 19) owner_hit = true;
        }
        if (owner_hit) supports.push_back(support);
        int position = support_size - 1;
        while (position >= 0 &&
               support[position] == m - support_size + position) {
            --position;
        }
        if (position < 0) break;
        ++support[position];
        for (int next = position + 1; next < support_size; ++next) {
            support[next] = support[next - 1] + 1;
        }
    }
    if (supports.size() != 75140) {
        cerr << "unexpected owner-feasible support count\n";
        return 2;
    }

    vector<int> occupancy(line_count);
    vector<unsigned long long> permanent_dp(1 << support_size);
    vector<unsigned long long> weighted_dp(1 << support_size);
    vector<array<int, support_size>> zero_supports;
    array<int, support_size> minimum_support{}, maximum_support{};
    unsigned long long minimum_positive = ULLONG_MAX;
    unsigned long long maximum_permanent = 0;
    unsigned long long positive_supports = 0;
    __uint128_t total_target_permanent = 0;
    __uint128_t total_weighted_permanent = 0;

    for (const auto& current_support : supports) {
        vector<char> in_support(m, false);
        for (int source : current_support) in_support[source] = true;
        occupancy = base_occupancy;
        unordered_set<int> retained_orbits;
        for (int source = 0; source < m; ++source) {
            if (!in_support[source]) {
                retained_orbits.insert(options[base_option[source]].orbit_id);
            }
        }
        for (int source : current_support) {
            for (auto [line, count] : options[base_option[source]].line_counts) {
                occupancy[line] -= count;
            }
        }

        uint16_t row_mask[support_size]{};
        uint8_t orientation_weight[support_size][support_size]{};
        for (int row = 0; row < support_size; ++row) {
            const int source = current_support[row];
            for (int column = 0; column < support_size; ++column) {
                const int old_target_owner = current_support[column];
                if (source == old_target_owner) continue;
                const int target = rho[old_target_owner];
                int legal_orientations = 0;
                for (int id : by_source_target[source][target]) {
                    const Option& option = options[id];
                    if (retained_orbits.count(option.orbit_id)) continue;
                    bool legal = true;
                    for (auto [line, count] : option.line_counts) {
                        if (occupancy[line] + count > 2) {
                            legal = false;
                            break;
                        }
                    }
                    if (legal) ++legal_orientations;
                }
                if (legal_orientations) {
                    row_mask[row] |= uint16_t(1) << column;
                    orientation_weight[row][column] = legal_orientations;
                }
            }
        }

        fill(permanent_dp.begin(), permanent_dp.end(), 0);
        fill(weighted_dp.begin(), weighted_dp.end(), 0);
        permanent_dp[0] = 1;
        weighted_dp[0] = 1;
        for (int mask = 0; mask < (1 << support_size); ++mask) {
            const int row = __builtin_popcount(static_cast<unsigned>(mask));
            if (row == support_size) continue;
            unsigned available = row_mask[row] & ~static_cast<unsigned>(mask);
            while (available) {
                const int column = __builtin_ctz(available);
                const int next_mask = mask | (1 << column);
                permanent_dp[next_mask] += permanent_dp[mask];
                weighted_dp[next_mask] +=
                    weighted_dp[mask] * orientation_weight[row][column];
                available &= available - 1;
            }
        }

        const unsigned long long target_permanent = permanent_dp.back();
        const unsigned long long weighted_permanent = weighted_dp.back();
        if (target_permanent == 0) {
            zero_supports.push_back(current_support);
        } else {
            ++positive_supports;
            if (target_permanent < minimum_positive) {
                minimum_positive = target_permanent;
                minimum_support = current_support;
            }
            if (target_permanent > maximum_permanent) {
                maximum_permanent = target_permanent;
                maximum_support = current_support;
            }
        }
        total_target_permanent += target_permanent;
        total_weighted_permanent += weighted_permanent;
    }

    cout << "supports=" << supports.size()
         << " zero=" << zero_supports.size()
         << " positive=" << positive_supports
         << " min_positive=" << minimum_positive
         << " max=" << maximum_permanent
         << " total_target=" << decimal(total_target_permanent)
         << " total_signed_individual=" << decimal(total_weighted_permanent)
         << '\n';
    for (const auto& zero_support : zero_supports) {
        cout << "ZERO";
        for (int source : zero_support) cout << ' ' << source + 1;
        cout << '\n';
    }
    cout << "MINSET";
    for (int source : minimum_support) cout << ' ' << source + 1;
    cout << " count=" << minimum_positive << '\n';
    cout << "MAXSET";
    for (int source : maximum_support) cout << ' ' << source + 1;
    cout << " count=" << maximum_permanent << '\n';
    return 0;
}

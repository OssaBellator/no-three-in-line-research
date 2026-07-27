#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

struct Opt {
    int source;
    int target;
    int orientation;
    int orbit_id;
    vector<pair<int, uint8_t>> line_counts;
};

static uint64_t splitmix64(uint64_t x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

int main(int argc, char** argv) {
    const long long samples = argc > 1 ? atoll(argv[1]) : 100000;
    const int threads = argc > 2 ? atoi(argv[2]) : 16;
    const uint64_t seed = argc > 3 ? strtoull(argv[3], nullptr, 10) : 12345;
    const int mode = argc > 4 ? atoi(argv[4]) : 2;
    if (samples < 1 || threads < 1 || mode < 0 || mode > 2) {
        cerr << "usage: SAMPLES THREADS SEED MODE, MODE=0 single-cycle, 1 uniform derangement, 2 mixed\n";
        return 2;
    }

    constexpr int n = 40;
    constexpr int m = 20;
    constexpr int support_size = 13;
    const int rho_one_based[m] = {
        19,20,13,14,10,6,11,2,16,1,8,4,15,7,18,12,3,17,5,9
    };
    const int base_orientations[m] = {
        1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1
    };
    vector<int> rho(m), orientation(base_orientations, base_orientations + m);
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

    auto orbit_id = [&](int source, int target, int sign) {
        if (source == target) return source * m + source;
        if (source < target) return m * m + 2 * (source * m + target) + sign;
        return m * m + 2 * (target * m + source) + 1 - sign;
    };

    vector<Opt> options;
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
                Opt option{source, target, sign, orbit_id(source, target, sign), {}};
                option.line_counts.reserve(counts.size());
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
        const int sign = rho[source] == source ? 0 : orientation[source];
        base_option[source] = by_source_target[source][rho[source]][0];
        for (int id : by_source_target[source][rho[source]]) {
            if (options[id].orientation == sign) base_option[source] = id;
        }
        for (auto [line, count] : options[base_option[source]].line_counts) {
            base_occupancy[line] += count;
        }
    }

    atomic<bool> found(false);
    atomic<long long> done(0), owner_pass(0), orientation_nodes(0),
        empty_domains(0), duplicate_failures(0), capped(0);
    mutex answer_mutex;
    vector<int> answer_rho, answer_orientation, answer_support;
    string answer_cycle_type;

    omp_set_num_threads(threads);
#pragma omp parallel
    {
        vector<int> occupancy = base_occupancy;
        vector<int> labels(m);
        iota(labels.begin(), labels.end(), 0);
        long long local_owner_pass = 0;
        long long local_nodes = 0;
        long long local_empty = 0;
        long long local_duplicates = 0;
        long long local_capped = 0;

        while (!found.load(memory_order_relaxed)) {
            const long long trial = done.fetch_add(1);
            if (trial >= samples) break;
            mt19937_64 rng(splitmix64(seed ^ static_cast<uint64_t>(trial)));

            iota(labels.begin(), labels.end(), 0);
            shuffle(labels.begin(), labels.end(), rng);
            vector<int> support(labels.begin(), labels.begin() + support_size);
            sort(support.begin(), support.end());
            bool owner_hit = false;
            for (int source : support) {
                if (source == 14 || source == 17 || source == 19) owner_hit = true;
            }
            if (!owner_hit) continue;
            ++local_owner_pass;

            vector<int> image = support;
            string cycle_type;
            const bool single_cycle = mode == 0 || (mode == 2 && (rng() & 1));
            if (single_cycle) {
                shuffle(image.begin(), image.end(), rng);
                vector<int> derangement(m);
                iota(derangement.begin(), derangement.end(), 0);
                for (int q = 0; q < support_size; ++q) {
                    derangement[image[q]] = image[(q + 1) % support_size];
                }
                image.clear();
                for (int source : support) image.push_back(derangement[source]);
                cycle_type = "13";
            } else {
                do {
                    shuffle(image.begin(), image.end(), rng);
                } while ([&]() {
                    for (int q = 0; q < support_size; ++q) {
                        if (image[q] == support[q]) return true;
                    }
                    return false;
                }());
                vector<int> derangement(m, -1);
                for (int q = 0; q < support_size; ++q) {
                    derangement[support[q]] = image[q];
                }
                vector<char> visited(m, false);
                vector<int> lengths;
                for (int source : support) {
                    if (visited[source]) continue;
                    int current = source;
                    int length = 0;
                    do {
                        visited[current] = true;
                        ++length;
                        current = derangement[current];
                    } while (current != source);
                    lengths.push_back(length);
                }
                sort(lengths.rbegin(), lengths.rend());
                for (int length : lengths) {
                    cycle_type += to_string(length) + ",";
                }
            }

            vector<int> new_target = rho;
            for (int q = 0; q < support_size; ++q) {
                new_target[support[q]] = rho[image[q]];
            }

            vector<char> in_support(m, false);
            for (int source : support) in_support[source] = true;
            unordered_set<int> used_orbits;
            for (int source = 0; source < m; ++source) {
                if (!in_support[source]) {
                    used_orbits.insert(options[base_option[source]].orbit_id);
                }
            }
            for (int source : support) {
                for (auto [line, count] : options[base_option[source]].line_counts) {
                    occupancy[line] -= count;
                }
            }

            vector<vector<int>> candidates(m);
            bool initial_failure = false;
            for (int source : support) {
                for (int id : by_source_target[source][new_target[source]]) {
                    const Opt& option = options[id];
                    if (used_orbits.count(option.orbit_id)) continue;
                    bool legal = true;
                    for (auto [line, count] : option.line_counts) {
                        if (occupancy[line] + count > 2) {
                            legal = false;
                            break;
                        }
                    }
                    if (legal) candidates[source].push_back(id);
                }
                if (candidates[source].empty()) {
                    initial_failure = true;
                    ++local_empty;
                    break;
                }
            }

            vector<int> chosen(m, -1);
            vector<char> assigned(m, false);
            long long trial_nodes = 0;
            bool was_capped = false;
            function<bool(int)> search = [&](int depth) {
                ++local_nodes;
                ++trial_nodes;
                if (trial_nodes > 100000) {
                    was_capped = true;
                    return false;
                }
                if (depth == support_size) return true;

                int best_source = -1;
                vector<int> available, best_available;
                for (int source : support) {
                    if (assigned[source]) continue;
                    available.clear();
                    for (int id : candidates[source]) {
                        const Opt& option = options[id];
                        if (used_orbits.count(option.orbit_id)) continue;
                        bool legal = true;
                        for (auto [line, count] : option.line_counts) {
                            if (occupancy[line] + count > 2) {
                                legal = false;
                                break;
                            }
                        }
                        if (legal) available.push_back(id);
                    }
                    if (available.empty()) return false;
                    if (best_source < 0 || available.size() < best_available.size()) {
                        best_source = source;
                        best_available = available;
                    }
                }

                shuffle(best_available.begin(), best_available.end(), rng);
                assigned[best_source] = true;
                for (int id : best_available) {
                    const Opt& option = options[id];
                    if (!used_orbits.insert(option.orbit_id).second) {
                        ++local_duplicates;
                        continue;
                    }
                    for (auto [line, count] : option.line_counts) {
                        occupancy[line] += count;
                    }
                    chosen[best_source] = id;
                    if (search(depth + 1)) return true;
                    for (auto [line, count] : option.line_counts) {
                        occupancy[line] -= count;
                    }
                    used_orbits.erase(option.orbit_id);
                    chosen[best_source] = -1;
                }
                assigned[best_source] = false;
                return false;
            };

            const bool feasible = !initial_failure && search(0);
            if (was_capped) ++local_capped;
            if (feasible) {
                bool expected = false;
                if (found.compare_exchange_strong(expected, true)) {
                    lock_guard<mutex> lock(answer_mutex);
                    answer_support = support;
                    answer_rho = new_target;
                    answer_orientation.assign(m, 0);
                    for (int source = 0; source < m; ++source) {
                        answer_orientation[source] = in_support[source]
                            ? options[chosen[source]].orientation
                            : orientation[source];
                    }
                    answer_cycle_type = cycle_type;
                }
            }
            occupancy = base_occupancy;
        }

        owner_pass.fetch_add(local_owner_pass);
        orientation_nodes.fetch_add(local_nodes);
        empty_domains.fetch_add(local_empty);
        duplicate_failures.fetch_add(local_duplicates);
        capped.fetch_add(local_capped);
    }

    cerr << "samples_claimed=" << min(samples, done.load())
         << " owner_pass=" << owner_pass.load()
         << " orient_nodes=" << orientation_nodes.load()
         << " empty=" << empty_domains.load()
         << " duplicate=" << duplicate_failures.load()
         << " capped=" << capped.load() << '\n';

    if (found) {
        cout << "FOUND type=" << answer_cycle_type << "\nsupport=";
        for (int source : answer_support) cout << source + 1 << ',';
        cout << "\nrho=";
        for (int target : answer_rho) cout << target + 1 << ',';
        cout << "\ne=";
        for (int sign : answer_orientation) cout << sign << ',';
        cout << '\n';
        return 0;
    }
    cout << "NOTFOUND\n";
    return 0;
}

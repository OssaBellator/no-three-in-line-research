#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

struct Pt {
    int x, y;
    bool operator<(const Pt &other) const { return tie(x, y) < tie(other.x, other.y); }
    bool operator==(const Pt &other) const { return x == other.x && y == other.y; }
};

long long cross(Pt a, Pt b, Pt c) {
    return 1LL * (b.x - a.x) * (c.y - a.y) - 1LL * (b.y - a.y) * (c.x - a.x);
}

struct Node { string kind; int variant; vector<Pt> points; };

struct HittingSolver {
    int n = 0;
    vector<array<int, 3>> edges;
    vector<char> selected;
    int best = 0;

    bool hit(const array<int, 3> &edge) const {
        return selected[edge[0]] || selected[edge[1]] || selected[edge[2]];
    }

    int packing_lower_bound(const vector<int> &unhit) const {
        vector<char> used(n, 0);
        int count = 0;
        for (int index : unhit) {
            const auto &edge = edges[index];
            if (!used[edge[0]] && !used[edge[1]] && !used[edge[2]]) {
                used[edge[0]] = used[edge[1]] = used[edge[2]] = 1;
                ++count;
            }
        }
        return count;
    }

    void minimize(int count) {
        if (count >= best) return;
        vector<int> unhit;
        vector<int> frequency(n, 0);
        for (int index = 0; index < static_cast<int>(edges.size()); ++index) {
            if (!hit(edges[index])) {
                unhit.push_back(index);
                for (int vertex : edges[index]) ++frequency[vertex];
            }
        }
        if (unhit.empty()) {
            best = count;
            return;
        }
        if (count + packing_lower_bound(unhit) >= best) return;
        int chosen = unhit.front();
        int score = -1;
        for (int index : unhit) {
            int current = 0;
            for (int vertex : edges[index]) current += frequency[vertex];
            if (current > score) {
                score = current;
                chosen = index;
            }
        }
        auto branch = edges[chosen];
        sort(branch.begin(), branch.end(), [&](int first, int second) {
            return frequency[first] > frequency[second];
        });
        for (int vertex : branch) {
            selected[vertex] = 1;
            minimize(count + 1);
            selected[vertex] = 0;
        }
    }

    int minimum(int upper_bound) {
        best = upper_bound;
        selected.assign(n, 0);
        minimize(0);
        return best;
    }

    void enumerate_exact(int target, set<pair<unsigned long long, unsigned long long>> &output, int count = 0) {
        if (count > target) return;
        vector<int> unhit;
        vector<int> frequency(n, 0);
        for (int index = 0; index < static_cast<int>(edges.size()); ++index) {
            if (!hit(edges[index])) {
                unhit.push_back(index);
                for (int vertex : edges[index]) ++frequency[vertex];
            }
        }
        if (unhit.empty()) {
            if (count == target) {
                unsigned long long low = 0, high = 0;
                for (int vertex = 0; vertex < n; ++vertex) {
                    if (!selected[vertex]) continue;
                    if (vertex < 64) low |= 1ULL << vertex;
                    else high |= 1ULL << (vertex - 64);
                }
                output.insert({low, high});
            }
            return;
        }
        if (count + packing_lower_bound(unhit) > target) return;
        int chosen = unhit.front();
        int score = -1;
        for (int index : unhit) {
            int current = 0;
            for (int vertex : edges[index]) current += frequency[vertex];
            if (current > score) {
                score = current;
                chosen = index;
            }
        }
        auto branch = edges[chosen];
        sort(branch.begin(), branch.end(), [&](int first, int second) {
            return frequency[first] > frequency[second];
        });
        for (int vertex : branch) {
            selected[vertex] = 1;
            enumerate_exact(target, output, count + 1);
            selected[vertex] = 0;
        }
    }
};

bool legal_add_search(
    const vector<Pt> &base,
    const vector<int> &columns,
    multiset<int> &rows,
    vector<Pt> &chosen,
    int index,
    vector<Pt> &answer
) {
    if (index == static_cast<int>(columns.size())) {
        answer = chosen;
        return true;
    }
    int column = columns[index];
    int previous_row = (index && columns[index - 1] == column) ? chosen.back().y : -1000000000;
    vector<int> values(rows.begin(), rows.end());
    values.erase(unique(values.begin(), values.end()), values.end());
    for (int row : values) {
        if (row <= previous_row) continue;
        auto row_it = rows.find(row);
        if (row_it == rows.end()) continue;
        Pt point{column, row};
        if (binary_search(base.begin(), base.end(), point) || find(chosen.begin(), chosen.end(), point) != chosen.end()) continue;
        bool bad = false;
        for (int first = 0; first < static_cast<int>(base.size()) && !bad; ++first) {
            for (int second = first + 1; second < static_cast<int>(base.size()); ++second) {
                if (cross(base[first], base[second], point) == 0) { bad = true; break; }
            }
        }
        for (int chosen_index = 0; chosen_index < static_cast<int>(chosen.size()) && !bad; ++chosen_index) {
            for (Pt old : base) {
                if (cross(old, chosen[chosen_index], point) == 0) { bad = true; break; }
            }
        }
        for (int first = 0; first < static_cast<int>(chosen.size()) && !bad; ++first) {
            for (int second = first + 1; second < static_cast<int>(chosen.size()); ++second) {
                if (cross(chosen[first], chosen[second], point) == 0) { bad = true; break; }
            }
        }
        if (bad) continue;
        rows.erase(row_it);
        chosen.push_back(point);
        if (legal_add_search(base, columns, rows, chosen, index + 1, answer)) return true;
        chosen.pop_back();
        rows.insert(row);
    }
    return false;
}

bool try_deleted(const vector<Pt> &original, vector<Pt> deleted, vector<Pt> &added) {
    sort(deleted.begin(), deleted.end());
    vector<Pt> base;
    set_difference(original.begin(), original.end(), deleted.begin(), deleted.end(), back_inserter(base));
    map<int, int> column_counts;
    vector<int> columns, row_values;
    for (Pt point : deleted) {
        columns.push_back(point.x);
        row_values.push_back(point.y);
        ++column_counts[point.x];
    }
    sort(columns.begin(), columns.end(), [&](int first, int second) {
        if (column_counts[first] != column_counts[second]) return column_counts[first] > column_counts[second];
        return first < second;
    });
    multiset<int> rows(row_values.begin(), row_values.end());
    vector<Pt> chosen;
    return legal_add_search(base, columns, rows, chosen, 0, added);
}

int main() {
    vector<Pt> corrected_seventh = {
        {0,2},{0,79},{1,3},{1,61},{2,1},{2,2},{3,0},{3,3},{4,33},{4,77},{5,32},{5,35},
        {6,33},{6,34},{7,32},{7,35},{8,34},{8,105},{9,59},{9,60},{10,58},{10,61},{11,59},{11,60},
        {12,47},{12,48},{13,46},{13,77},{14,47},{14,48},{15,46},{15,49},{16,75},{16,76},{17,1},{17,74},
        {18,75},{18,76},{19,0},{19,74},{20,106},{20,107},{21,105},{21,108},{22,106},{22,107},{23,58},{23,108},
        {24,49},{24,82},{25,80},{25,81},{26,79},{26,82},{27,80},{27,81}
    };
    vector<Node> nodes = {
        {"P",0,{{0,0},{0,2},{1,1},{1,3},{2,1},{2,3},{3,0},{3,2}}},
        {"P",1,{{0,0},{0,3},{1,1},{1,2},{2,0},{2,3},{3,1},{3,2}}},
        {"P",2,{{0,1},{0,3},{1,0},{1,2},{2,0},{2,2},{3,1},{3,3}}},
        {"P",3,{{0,1},{0,2},{1,0},{1,3},{2,1},{2,2},{3,0},{3,3}}},
        {"Q",0,{{0,3},{0,5},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,1},{6,3}}},
        {"Q",1,{{0,1},{0,5},{1,0},{1,3},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,3},{5,6},{6,1},{6,5}}},
        {"Q",2,{{0,1},{0,3},{1,0},{1,6},{2,2},{2,4},{3,1},{3,5},{4,2},{4,4},{5,0},{5,6},{6,3},{6,5}}},
        {"Q",3,{{0,1},{0,5},{1,3},{1,6},{2,2},{2,4},{3,0},{3,6},{4,2},{4,4},{5,0},{5,3},{6,1},{6,5}}}
    };

    map<int, int> minimum_histogram;
    int attempts_at_most_seven = 0;
    long long minimum_sets_at_most_seven = 0;
    int successful_cores = 0;
    int successful_attempts = 0;
    vector<Pt> unique_deleted, unique_added;
    string unique_kind;
    int unique_variant = -1, unique_offset = 0, unique_minimum = 0;

    for (const Node &node : nodes) {
        for (int offset = -32; offset <= 32; ++offset) {
            vector<Pt> new_block;
            for (Pt local : node.points) new_block.push_back({28 + local.x, 79 + offset + local.y});
            vector<Pt> all = corrected_seventh;
            all.insert(all.end(), new_block.begin(), new_block.end());
            sort(all.begin(), all.end());
            vector<array<int, 3>> conflicts;
            int old_count = corrected_seventh.size();
            auto locate = [&](Pt point) {
                return static_cast<int>(lower_bound(all.begin(), all.end(), point) - all.begin());
            };
            for (int first = 0; first < old_count; ++first) {
                for (int second = first + 1; second < old_count; ++second) {
                    for (int fresh = 0; fresh < static_cast<int>(new_block.size()); ++fresh) {
                        if (cross(corrected_seventh[first], corrected_seventh[second], new_block[fresh]) == 0) {
                            conflicts.push_back({locate(corrected_seventh[first]), locate(corrected_seventh[second]), locate(new_block[fresh])});
                        }
                    }
                }
            }
            for (int first = 0; first < static_cast<int>(new_block.size()); ++first) {
                for (int second = first + 1; second < static_cast<int>(new_block.size()); ++second) {
                    for (Pt old : corrected_seventh) {
                        if (cross(new_block[first], new_block[second], old) == 0) {
                            conflicts.push_back({locate(new_block[first]), locate(new_block[second]), locate(old)});
                        }
                    }
                }
            }
            sort(conflicts.begin(), conflicts.end());
            conflicts.erase(unique(conflicts.begin(), conflicts.end()), conflicts.end());
            HittingSolver solver;
            solver.n = all.size();
            solver.edges = conflicts;
            int minimum = solver.minimum(new_block.size() + 1);
            ++minimum_histogram[minimum];
            if (minimum > 7) continue;
            ++attempts_at_most_seven;
            solver.selected.assign(solver.n, 0);
            set<pair<unsigned long long, unsigned long long>> masks;
            solver.enumerate_exact(minimum, masks);
            minimum_sets_at_most_seven += masks.size();
            bool attempt_success = false;
            for (auto mask : masks) {
                vector<Pt> core;
                for (int index = 0; index < static_cast<int>(all.size()); ++index) {
                    bool present = index < 64 ? ((mask.first >> index) & 1ULL) : ((mask.second >> (index - 64)) & 1ULL);
                    if (present) core.push_back(all[index]);
                }
                int extra_needed = 7 - core.size();
                vector<Pt> available;
                set_difference(all.begin(), all.end(), core.begin(), core.end(), back_inserter(available));
                bool core_success = false;
                vector<Pt> deleted, added;
                if (extra_needed == 0) {
                    vector<Pt> candidate_added;
                    if (try_deleted(all, core, candidate_added)) {
                        core_success = true;
                        deleted = core;
                        added = candidate_added;
                    }
                } else if (extra_needed == 1) {
                    for (Pt first : available) {
                        vector<Pt> candidate_deleted = core;
                        candidate_deleted.push_back(first);
                        vector<Pt> candidate_added;
                        if (try_deleted(all, candidate_deleted, candidate_added)) {
                            core_success = true;
                            deleted = candidate_deleted;
                            added = candidate_added;
                            break;
                        }
                    }
                } else if (extra_needed == 2) {
                    for (int first = 0; first < static_cast<int>(available.size()) && !core_success; ++first) {
                        for (int second = first + 1; second < static_cast<int>(available.size()); ++second) {
                            vector<Pt> candidate_deleted = core;
                            candidate_deleted.push_back(available[first]);
                            candidate_deleted.push_back(available[second]);
                            vector<Pt> candidate_added;
                            if (try_deleted(all, candidate_deleted, candidate_added)) {
                                core_success = true;
                                deleted = candidate_deleted;
                                added = candidate_added;
                                break;
                            }
                        }
                    }
                } else if (extra_needed == 3) {
                    for (int first = 0; first < static_cast<int>(available.size()) && !core_success; ++first) {
                        for (int second = first + 1; second < static_cast<int>(available.size()) && !core_success; ++second) {
                            for (int third = second + 1; third < static_cast<int>(available.size()); ++third) {
                                vector<Pt> candidate_deleted = core;
                                candidate_deleted.push_back(available[first]);
                                candidate_deleted.push_back(available[second]);
                                candidate_deleted.push_back(available[third]);
                                vector<Pt> candidate_added;
                                if (try_deleted(all, candidate_deleted, candidate_added)) {
                                    core_success = true;
                                    deleted = candidate_deleted;
                                    added = candidate_added;
                                    break;
                                }
                            }
                        }
                    }
                }
                if (core_success) {
                    ++successful_cores;
                    attempt_success = true;
                    unique_kind = node.kind;
                    unique_variant = node.variant;
                    unique_offset = offset;
                    unique_minimum = minimum;
                    sort(deleted.begin(), deleted.end());
                    sort(added.begin(), added.end());
                    unique_deleted = deleted;
                    unique_added = added;
                }
            }
            if (attempt_success) ++successful_attempts;
        }
    }

    map<int, int> expected = {{4,1},{5,6},{6,21},{7,68},{8,164},{9,2},{10,4},{11,34},{12,41},{13,107},{14,72}};
    assert(minimum_histogram == expected);
    assert(attempts_at_most_seven == 96);
    assert(minimum_sets_at_most_seven == 808);
    assert(successful_cores == 1 && successful_attempts == 1);
    assert(unique_kind == "P" && unique_variant == 1 && unique_offset == 31 && unique_minimum == 5);
    vector<Pt> expected_deleted = {{0,2},{1,3},{23,108},{24,49},{28,110},{28,113},{30,110}};
    vector<Pt> expected_added = {{0,110},{1,113},{23,2},{24,110},{28,3},{28,108},{30,49}};
    assert(unique_deleted == expected_deleted && unique_added == expected_added);

    vector<Pt> eighth_block;
    for (Pt local : nodes[1].points) eighth_block.push_back({28 + local.x, 79 + 31 + local.y});
    vector<Pt> corrected_eighth = corrected_seventh;
    corrected_eighth.insert(corrected_eighth.end(), eighth_block.begin(), eighth_block.end());
    sort(corrected_eighth.begin(), corrected_eighth.end());
    vector<Pt> after_delete;
    set_difference(corrected_eighth.begin(), corrected_eighth.end(), unique_deleted.begin(), unique_deleted.end(), back_inserter(after_delete));
    corrected_eighth = after_delete;
    corrected_eighth.insert(corrected_eighth.end(), unique_added.begin(), unique_added.end());
    sort(corrected_eighth.begin(), corrected_eighth.end());
    assert(corrected_eighth.size() == 64);
    for (int first = 0; first < 64; ++first) for (int second = first + 1; second < 64; ++second) for (int third = second + 1; third < 64; ++third) assert(cross(corrected_eighth[first], corrected_eighth[second], corrected_eighth[third]) != 0);

    int raw_ninth_extensions = 0;
    for (const Node &node : nodes) for (int offset = -32; offset <= 32; ++offset) {
        vector<Pt> candidate = corrected_eighth;
        for (Pt local : node.points) candidate.push_back({32 + local.x, 110 + offset + local.y});
        bool legal = true;
        for (int first = 0; first < static_cast<int>(candidate.size()) && legal; ++first)
            for (int second = first + 1; second < static_cast<int>(candidate.size()) && legal; ++second)
                for (int third = second + 1; third < static_cast<int>(candidate.size()); ++third)
                    if (cross(candidate[first], candidate[second], candidate[third]) == 0) { legal = false; break; }
        raw_ninth_extensions += legal;
    }
    assert(raw_ninth_extensions == 0);

    cout << "{\n"
         << "  \"raw_eighth_attempts\": 520,\n"
         << "  \"minimum_transversal_histogram\": {\"4\":1,\"5\":6,\"6\":21,\"7\":68,\"8\":164,\"9\":2,\"10\":4,\"11\":34,\"12\":41,\"13\":107,\"14\":72},\n"
         << "  \"attempts_with_minimum_at_most_seven\": 96,\n"
         << "  \"minimum_transversals_enumerated\": 808,\n"
         << "  \"degree_preserving_correctors_of_size_at_most_seven\": 1,\n"
         << "  \"unique_corrected_eighth_transition\": {\"block\":\"P1\",\"offset\":31,\"minimum_transversal_size\":5,\"corrector_size\":7},\n"
         << "  \"raw_ninth_attempts\": 520,\n"
         << "  \"raw_ninth_extensions\": 0,\n"
         << "  \"status\": \"passed\"\n"
         << "}\n";
}

#include <bits/stdc++.h>
using namespace std;

static int mod_value(int value, int prime) {
    value %= prime;
    if (value < 0) value += prime;
    return value;
}

struct Edge {
    int value[4];
};

static Edge make_edge(int prime, int row, int column) {
    return {{
        row,
        column,
        mod_value(row - column, prime),
        mod_value(row + column, prime),
    }};
}

static vector<int> signed_pair(int prime, int gap) {
    return {mod_value(-gap, prime), gap};
}

static bool is_matching(const vector<Edge>& edges) {
    for (int part = 0; part < 4; ++part) {
        set<int> used;
        for (const Edge& edge : edges) {
            if (!used.insert(edge.value[part]).second) return false;
        }
    }
    return true;
}

static bool directly_completable(
    int prime,
    array<vector<int>, 4> vertices
) {
    for (auto& part : vertices) sort(part.begin(), part.end());
    vector<int> columns = vertices[1];
    do {
        vector<int> differences(vertices[0].size());
        vector<int> sums(vertices[0].size());
        for (size_t index = 0; index < vertices[0].size(); ++index) {
            differences[index] = mod_value(
                vertices[0][index] - columns[index], prime
            );
            sums[index] = mod_value(
                vertices[0][index] + columns[index], prime
            );
        }
        sort(differences.begin(), differences.end());
        sort(sums.begin(), sums.end());
        if (differences == vertices[2] && sums == vertices[3]) return true;
    } while (next_permutation(columns.begin(), columns.end()));
    return false;
}

static bool has_order_two_absorber(
    int prime,
    const array<vector<int>, 4>& leftover
) {
    vector<Edge> available;
    for (int row = 0; row < prime; ++row) {
        for (int column = 0; column < prime; ++column) {
            Edge edge = make_edge(prime, row, column);
            bool disjoint = true;
            for (int part = 0; part < 4; ++part) {
                if (
                    edge.value[part] == leftover[part][0]
                    || edge.value[part] == leftover[part][1]
                ) {
                    disjoint = false;
                }
            }
            if (disjoint) available.push_back(edge);
        }
    }

    for (size_t first = 0; first < available.size(); ++first) {
        for (size_t second = first + 1; second < available.size(); ++second) {
            vector<Edge> old_matching = {
                available[first], available[second]
            };
            if (!is_matching(old_matching)) continue;

            array<vector<int>, 4> combined = leftover;
            bool disjoint = true;
            for (const Edge& edge : old_matching) {
                for (int part = 0; part < 4; ++part) {
                    if (
                        find(
                            combined[part].begin(),
                            combined[part].end(),
                            edge.value[part]
                        ) != combined[part].end()
                    ) {
                        disjoint = false;
                    }
                    combined[part].push_back(edge.value[part]);
                }
            }
            if (disjoint && directly_completable(prime, combined)) return true;
        }
    }
    return false;
}

struct AbsorberSearch {
    int prime;
    int old_order;
    int new_order;
    array<vector<int>, 4> leftover;
    vector<Edge> edges;
    array<vector<vector<int>>, 4> incidence;
    uint64_t used[4] = {};
    int required_bit[4][64];
    uint16_t all_required = 0;

    AbsorberSearch(
        int input_prime,
        int input_order,
        array<vector<int>, 4> input_leftover
    ) :
        prime(input_prime),
        old_order(input_order),
        new_order(input_order + 2),
        leftover(std::move(input_leftover))
    {
        memset(required_bit, -1, sizeof(required_bit));
        int bit = 0;
        for (int part = 0; part < 4; ++part) {
            for (int vertex : leftover[part]) {
                required_bit[part][vertex] = bit++;
            }
        }
        all_required = static_cast<uint16_t>((1u << bit) - 1u);

        for (int part = 0; part < 4; ++part) {
            incidence[part].assign(prime, {});
        }
        for (int row = 0; row < prime; ++row) {
            for (int column = 0; column < prime; ++column) {
                int id = static_cast<int>(edges.size());
                edges.push_back(make_edge(prime, row, column));
                for (int part = 0; part < 4; ++part) {
                    incidence[part][edges.back().value[part]].push_back(id);
                }
            }
        }
    }

    bool compatible(const Edge& edge) const {
        for (int part = 0; part < 4; ++part) {
            if ((used[part] >> edge.value[part]) & 1ULL) return false;
        }
        return true;
    }

    uint16_t required_mask(const Edge& edge) const {
        uint16_t result = 0;
        for (int part = 0; part < 4; ++part) {
            int bit = required_bit[part][edge.value[part]];
            if (bit >= 0) result |= static_cast<uint16_t>(1u << bit);
        }
        return result;
    }

    bool finish() const {
        array<vector<int>, 4> extra;
        for (int part = 0; part < 4; ++part) {
            for (int vertex = 0; vertex < prime; ++vertex) {
                if (
                    ((used[part] >> vertex) & 1ULL)
                    && required_bit[part][vertex] < 0
                ) {
                    extra[part].push_back(vertex);
                }
            }
            if (static_cast<int>(extra[part].size()) != old_order) return false;
        }
        return directly_completable(prime, extra);
    }

    bool search(uint16_t covered, int depth, int last_extra_row = -1) {
        if (depth == new_order) {
            return covered == all_required && finish();
        }

        int slots = new_order - depth;
        uint16_t remaining = static_cast<uint16_t>(all_required & ~covered);
        if (__builtin_popcount(static_cast<unsigned>(remaining)) > 4 * slots) {
            return false;
        }

        for (int part = 0; part < 4; ++part) {
            int needed = 0;
            for (int vertex : leftover[part]) {
                int bit = required_bit[part][vertex];
                if (((covered >> bit) & 1u) == 0u) ++needed;
            }
            if (needed > slots) return false;
        }

        if (remaining != 0u) {
            int best_part = -1;
            int best_vertex = -1;
            int best_count = INT_MAX;
            for (int part = 0; part < 4; ++part) {
                for (int vertex : leftover[part]) {
                    int bit = required_bit[part][vertex];
                    if ((covered >> bit) & 1u) continue;
                    int count = 0;
                    for (int id : incidence[part][vertex]) {
                        if (compatible(edges[id])) ++count;
                    }
                    if (count < best_count) {
                        best_count = count;
                        best_part = part;
                        best_vertex = vertex;
                    }
                }
            }
            if (best_count == 0) return false;

            for (int id : incidence[best_part][best_vertex]) {
                const Edge& edge = edges[id];
                if (!compatible(edge)) continue;
                for (int part = 0; part < 4; ++part) {
                    used[part] |= 1ULL << edge.value[part];
                }
                if (search(
                    static_cast<uint16_t>(covered | required_mask(edge)),
                    depth + 1,
                    -1
                )) {
                    return true;
                }
                for (int part = 0; part < 4; ++part) {
                    used[part] ^= 1ULL << edge.value[part];
                }
            }
            return false;
        }

        for (int row = last_extra_row + 1; row < prime; ++row) {
            if ((used[0] >> row) & 1ULL) continue;
            if (required_bit[0][row] >= 0) continue;
            for (int id : incidence[0][row]) {
                const Edge& edge = edges[id];
                if (!compatible(edge) || required_mask(edge) != 0u) continue;
                for (int part = 0; part < 4; ++part) {
                    used[part] |= 1ULL << edge.value[part];
                }
                if (search(covered, depth + 1, row)) return true;
                for (int part = 0; part < 4; ++part) {
                    used[part] ^= 1ULL << edge.value[part];
                }
            }
        }
        return false;
    }

    bool run() {
        return search(0, 0);
    }
};

struct ExpectedCensus {
    int prime;
    int noncompletable;
    int order_two_exceptions;
    vector<array<int, 3>> order_three_exceptions;
};

static bool verify_prime(const ExpectedCensus& expected) {
    const int prime = expected.prime;
    const int half = (prime - 1) / 2;
    int noncompletable = 0;
    vector<array<int, 3>> order_two_exceptions;

    for (int b = 1; b <= half; ++b) {
        for (int u = 1; u <= half; ++u) {
            for (int v = 1; v <= half; ++v) {
                if (
                    mod_value(u * u + v * v - 2 * (1 + b * b), prime)
                    != 0
                ) {
                    continue;
                }
                array<vector<int>, 4> leftover = {
                    signed_pair(prime, 1),
                    signed_pair(prime, b),
                    signed_pair(prime, u),
                    signed_pair(prime, v),
                };
                if (directly_completable(prime, leftover)) continue;
                ++noncompletable;
                if (!has_order_two_absorber(prime, leftover)) {
                    order_two_exceptions.push_back({b, u, v});
                }
            }
        }
    }

    if (
        noncompletable != expected.noncompletable
        || static_cast<int>(order_two_exceptions.size())
            != expected.order_two_exceptions
    ) {
        return false;
    }

    vector<array<int, 3>> order_three_exceptions;
    for (const auto& parameters : order_two_exceptions) {
        array<vector<int>, 4> leftover = {
            signed_pair(prime, 1),
            signed_pair(prime, parameters[0]),
            signed_pair(prime, parameters[1]),
            signed_pair(prime, parameters[2]),
        };
        AbsorberSearch order_three(prime, 3, leftover);
        if (!order_three.run()) order_three_exceptions.push_back(parameters);
    }
    if (order_three_exceptions != expected.order_three_exceptions) return false;

    for (const auto& parameters : order_three_exceptions) {
        array<vector<int>, 4> leftover = {
            signed_pair(prime, 1),
            signed_pair(prime, parameters[0]),
            signed_pair(prime, parameters[1]),
            signed_pair(prime, parameters[2]),
        };
        AbsorberSearch order_four(prime, 4, leftover);
        if (!order_four.run()) return false;
    }

    cout
        << "p=" << prime
        << ": noncompletable=" << noncompletable
        << ", order-two exceptions=" << order_two_exceptions.size()
        << ", order-three exceptions=" << order_three_exceptions.size()
        << ", order-four exceptions=0\n";
    return true;
}

int main() {
    const ExpectedCensus order_29 = {
        29,
        72,
        32,
        {
            {1, 11, 12}, {1, 12, 11}, {9, 13, 13},
            {12, 3, 7}, {12, 7, 3},
            {12, 8, 9}, {12, 9, 8}, {13, 5, 5},
        },
    };
    const ExpectedCensus order_31 = {
        31,
        85,
        41,
        {
            {1, 8, 8}, {1, 10, 11}, {1, 11, 10}, {2, 6, 6},
            {5, 8, 9}, {5, 9, 8},
            {6, 8, 14}, {6, 14, 8},
            {11, 5, 8}, {11, 8, 5},
            {14, 8, 12}, {14, 12, 8}, {15, 3, 3},
        },
    };

    if (!verify_prime(order_29)) return 1;
    if (!verify_prime(order_31)) return 2;
    cout << "PX157 order-four absorber census verified\n";
    return 0;
}

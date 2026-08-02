#include <bits/stdc++.h>
using namespace std;

static int mod_value(int value, int prime) {
    value %= prime;
    if (value < 0) value += prime;
    return value;
}

struct Edge {
    int value[4];
    int row;
    int column;
};

static Edge make_edge(int prime, int row, int column) {
    return {{
        row,
        column,
        mod_value(row - column, prime),
        mod_value(row + column, prime),
    }, row, column};
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

static array<set<int>, 4> vertex_sets(const vector<Edge>& edges) {
    array<set<int>, 4> result;
    for (const Edge& edge : edges) {
        for (int part = 0; part < 4; ++part) {
            result[part].insert(edge.value[part]);
        }
    }
    return result;
}

static bool directly_completable(
    int prime,
    array<vector<int>, 4> vertices,
    vector<pair<int, int>>* witness = nullptr
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
        vector<int> sorted_differences = differences;
        vector<int> sorted_sums = sums;
        sort(sorted_differences.begin(), sorted_differences.end());
        sort(sorted_sums.begin(), sorted_sums.end());
        if (
            sorted_differences == vertices[2]
            && sorted_sums == vertices[3]
        ) {
            if (witness != nullptr) {
                witness->clear();
                for (size_t index = 0; index < vertices[0].size(); ++index) {
                    witness->push_back({vertices[0][index], columns[index]});
                }
            }
            return true;
        }
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
    vector<int> chosen;
    vector<int> solution;
    vector<pair<int, int>> old_witness;

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

    bool finish() {
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

        vector<pair<int, int>> witness;
        if (!directly_completable(prime, extra, &witness)) return false;
        solution = chosen;
        old_witness = std::move(witness);
        return true;
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
                chosen.push_back(id);
                if (search(
                    static_cast<uint16_t>(covered | required_mask(edge)),
                    depth + 1,
                    -1
                )) {
                    return true;
                }
                chosen.pop_back();
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
                chosen.push_back(id);
                if (search(covered, depth + 1, row)) return true;
                chosen.pop_back();
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

static bool verify_absorber(
    int prime,
    const array<vector<int>, 4>& leftover,
    const vector<pair<int, int>>& old_pairs,
    const vector<pair<int, int>>& new_pairs
) {
    vector<Edge> old_matching;
    vector<Edge> new_matching;
    for (auto [row, column] : old_pairs) {
        old_matching.push_back(make_edge(prime, row, column));
    }
    for (auto [row, column] : new_pairs) {
        new_matching.push_back(make_edge(prime, row, column));
    }
    if (!is_matching(old_matching) || !is_matching(new_matching)) return false;

    auto old_vertices = vertex_sets(old_matching);
    auto new_vertices = vertex_sets(new_matching);
    for (int part = 0; part < 4; ++part) {
        set<int> expected = old_vertices[part];
        expected.insert(leftover[part].begin(), leftover[part].end());
        if (expected != new_vertices[part]) return false;
    }
    return true;
}

constexpr int RANK_MODULUS = 1000000007;
using LinearVector = array<int, 10>;

static long long rank_mod(long long value) {
    value %= RANK_MODULUS;
    if (value < 0) value += RANK_MODULUS;
    return value;
}

static int matrix_rank(
    array<array<int, 10>, 10> matrix,
    int columns
) {
    int rank = 0;
    for (int column = 0; column < columns && rank < 10; ++column) {
        int pivot = -1;
        for (int row = rank; row < 10; ++row) {
            if (rank_mod(matrix[row][column]) != 0) {
                pivot = row;
                break;
            }
        }
        if (pivot < 0) continue;
        swap(matrix[rank], matrix[pivot]);

        long long base = rank_mod(matrix[rank][column]);
        long long inverse = 1;
        long long power = RANK_MODULUS - 2;
        long long current = base;
        while (power > 0) {
            if (power & 1LL) inverse = inverse * current % RANK_MODULUS;
            current = current * current % RANK_MODULUS;
            power >>= 1LL;
        }

        for (int entry = column; entry < columns; ++entry) {
            matrix[rank][entry] = static_cast<int>(
                rank_mod(matrix[rank][entry]) * inverse % RANK_MODULUS
            );
        }
        for (int row = 0; row < 10; ++row) {
            if (row == rank) continue;
            long long factor = rank_mod(matrix[row][column]);
            for (int entry = column; entry < columns; ++entry) {
                matrix[row][entry] = static_cast<int>(rank_mod(
                    matrix[row][entry]
                    - factor * matrix[rank][entry]
                ));
            }
        }
        ++rank;
    }
    return rank;
}

static LinearVector add_vector(
    LinearVector first,
    const LinearVector& second,
    int sign
) {
    for (int index = 0; index < 10; ++index) {
        first[index] += sign * second[index];
    }
    return first;
}

static map<pair<int, int>, long long> template_rank_distribution() {
    vector<LinearVector> rows(5), columns(5), differences(5), sums(5);

    // Variables 0..2 are the three old row labels A_i.
    // Variables 3..5 are the three old column labels B_i.
    // Variables 6..9 are the external parameters 1,b,u,v.
    rows[0][6] = 1;
    rows[1][6] = -1;
    columns[0][7] = 1;
    columns[1][7] = -1;
    differences[3][8] = 1;
    differences[4][8] = -1;
    sums[3][9] = 1;
    sums[4][9] = -1;

    for (int index = 0; index < 3; ++index) {
        rows[2 + index][index] = 1;
        columns[2 + index][3 + index] = 1;
        differences[index][index] = 1;
        differences[index][3 + index] = -1;
        sums[index][index] = 1;
        sums[index][3 + index] = 1;
    }

    vector<array<int, 5>> permutations;
    array<int, 5> permutation = {0, 1, 2, 3, 4};
    do {
        permutations.push_back(permutation);
    } while (next_permutation(permutation.begin(), permutation.end()));

    map<pair<int, int>, long long> distribution;
    for (const auto& column_permutation : permutations) {
        for (const auto& difference_permutation : permutations) {
            for (const auto& sum_permutation : permutations) {
                array<array<int, 10>, 10> matrix{};
                int equation = 0;
                for (int row = 0; row < 5; ++row) {
                    matrix[equation++] = add_vector(
                        add_vector(
                            rows[row],
                            columns[column_permutation[row]],
                            -1
                        ),
                        differences[difference_permutation[row]],
                        -1
                    );
                    matrix[equation++] = add_vector(
                        add_vector(
                            rows[row],
                            columns[column_permutation[row]],
                            1
                        ),
                        sums[sum_permutation[row]],
                        -1
                    );
                }
                distribution[{
                    matrix_rank(matrix, 6),
                    matrix_rank(matrix, 10),
                }]++;
            }
        }
    }
    return distribution;
}

int main() {
    const int prime = 23;
    const vector<array<int, 3>> expected_order_two_exceptions = {
        {1, 1, 7}, {1, 5, 5}, {1, 7, 1},
        {2, 5, 10}, {2, 10, 5},
        {3, 5, 8}, {3, 8, 5},
        {7, 2, 2},
        {8, 5, 6}, {8, 6, 5},
        {10, 3, 3},
        {11, 5, 9}, {11, 9, 5},
    };

    int noncompletable = 0;
    vector<array<int, 3>> order_two_exceptions;
    for (int b = 1; b <= 11; ++b) {
        for (int u = 1; u <= 11; ++u) {
            for (int v = 1; v <= 11; ++v) {
                if (mod_value(u * u + v * v - 2 * (1 + b * b), prime) != 0) {
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
        noncompletable != 41
        || order_two_exceptions != expected_order_two_exceptions
    ) {
        return 1;
    }

    vector<array<int, 3>> order_three_exceptions;
    for (const auto& parameters : order_two_exceptions) {
        array<vector<int>, 4> leftover = {
            signed_pair(prime, 1),
            signed_pair(prime, parameters[0]),
            signed_pair(prime, parameters[1]),
            signed_pair(prime, parameters[2]),
        };
        AbsorberSearch search(prime, 3, leftover);
        if (!search.run()) order_three_exceptions.push_back(parameters);
    }
    if (order_three_exceptions != vector<array<int, 3>>{{1, 5, 5}}) {
        return 2;
    }

    array<vector<int>, 4> exceptional_leftover = {
        signed_pair(prime, 1),
        signed_pair(prime, 1),
        signed_pair(prime, 5),
        signed_pair(prime, 5),
    };
    const vector<pair<int, int>> old_matching = {
        {2, 0}, {4, 5}, {13, 13}, {15, 7},
    };
    const vector<pair<int, int>> new_matching = {
        {22, 0}, {1, 1}, {2, 7}, {4, 22},
        {13, 5}, {15, 13},
    };
    if (!verify_absorber(
        prime,
        exceptional_leftover,
        old_matching,
        new_matching
    )) {
        return 3;
    }
    AbsorberSearch order_four_search(prime, 4, exceptional_leftover);
    if (!order_four_search.run()) return 4;

    const map<pair<int, int>, long long> expected_rank_distribution = {
        {{0, 2}, 8},
        {{1, 3}, 288},
        {{2, 4}, 4504},
        {{3, 5}, 39360},
        {{4, 6}, 204864},
        {{5, 7}, 613632},
        {{6, 8}, 865344},
    };
    if (template_rank_distribution() != expected_rank_distribution) return 5;

    cout
        << "p=23: noncompletable=41, order-two exceptions=13, "
        << "order-three exceptions=1, order-four exceptions=0\n";
    cout << "unique order-three exception: (1,5,5)\n";
    cout
        << "all 1728000 abstract order-three templates impose exactly "
        << "two affine consistency conditions\n";
    return 0;
}

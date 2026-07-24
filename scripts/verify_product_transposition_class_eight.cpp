#include <algorithm>
#include <array>
#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using Permutation = std::array<int, 8>;
using Bits256 = std::array<std::uint64_t, 4>;

struct Point { int x; int y; };

long long determinant(Point a, Point b, Point c) {
    return 1LL * (b.x - a.x) * (c.y - a.y)
         - 1LL * (b.y - a.y) * (c.x - a.x);
}

Permutation compose(const Permutation& first, const Permutation& second) {
    Permutation result{};
    for (int i = 0; i < 8; ++i) result[i] = first[second[i]];
    return result;
}

std::vector<Permutation> affine_permutations() {
    std::vector<Permutation> result;
    for (int a : {1, 3, 5, 7}) {
        for (int b = 0; b < 8; ++b) {
            Permutation permutation{};
            for (int x = 0; x < 8; ++x) permutation[x] = (a * x + b) % 8;
            result.push_back(permutation);
        }
    }
    return result;
}

int flatten(int coarse, int fine, char mode) {
    return mode == 'c' ? 8 * coarse + fine : 2 * fine + coarse;
}

inline void setbit(Bits256& bits, int index) {
    bits[index >> 6] |= 1ULL << (index & 63);
}

inline void clearbit(Bits256& bits, int index) {
    bits[index >> 6] &= ~(1ULL << (index & 63));
}

inline bool intersects(const Bits256& first, const Bits256& second) {
    return ((first[0] & second[0])
        | (first[1] & second[1])
        | (first[2] & second[2])
        | (first[3] & second[3])) != 0;
}

struct SearchResult {
    bool feasible;
    long long nodes;
};

const std::vector<Bits256>& global_through() {
    constexpr int side = 16;
    constexpr int point_count = side * side;
    static const std::vector<Bits256> table = [] {
        std::array<Point, point_count> points{};
        for (int x = 0; x < side; ++x) {
            for (int y = 0; y < side; ++y) points[x * side + y] = {x, y};
        }
        std::vector<Bits256> result(point_count * point_count);
        for (int z = 0; z < point_count; ++z) {
            for (int anchor = 0; anchor < point_count; ++anchor) {
                if (anchor == z) continue;
                Bits256 mask{};
                for (int third = 0; third < point_count; ++third) {
                    if (third == anchor || third == z) continue;
                    if (determinant(points[anchor], points[z], points[third]) == 0) {
                        setbit(mask, third);
                    }
                }
                result[z * point_count + anchor] = mask;
            }
        }
        return result;
    }();
    return table;
}

SearchResult search_geometry(
    const Permutation& target,
    const Permutation& column_relative,
    const std::string& orientation
) {
    constexpr int n = 8;
    constexpr int side = 16;
    constexpr int point_count = side * side;
    const Permutation relative = {1, 0, 3, 2, 5, 4, 7, 6};

    std::array<std::array<int, 4>, n> pattern_columns{};
    for (int u = 0; u < n; ++u) {
        pattern_columns[u] = {
            flatten(0, target[u], orientation[1]),
            flatten(0, target[relative[u]], orientation[1]),
            flatten(1, column_relative[target[u]], orientation[1]),
            flatten(1, column_relative[target[relative[u]]], orientation[1]),
        };
        auto& columns = pattern_columns[u];
        std::sort(columns.begin(), columns.end());
        if (std::adjacent_find(columns.begin(), columns.end()) != columns.end()) {
            std::abort();
        }
    }

    // The first coarse row block has fixed abstract labels. In the second block,
    // assigning unused patterns to scalar rows is exactly the arbitrary P choice.
    struct Task { int row; int fixed_pattern; };
    std::array<Task, side> tasks{};
    int position = 0;
    for (int u = 0; u < n; ++u) {
        tasks[position++] = {flatten(0, u, orientation[0]), u};
    }
    for (int row_digit = 0; row_digit < n; ++row_digit) {
        tasks[position++] = {flatten(1, row_digit, orientation[0]), -1};
    }
    std::sort(tasks.begin(), tasks.begin() + n, [](Task first, Task second) {
        return first.row < second.row;
    });
    std::sort(tasks.begin() + n, tasks.end(), [](Task first, Task second) {
        return first.row < second.row;
    });

    const auto& through = global_through();

    std::array<std::array<int, side>, side + 1> fixed_suffix{};
    for (int depth = side - 1; depth >= 0; --depth) {
        fixed_suffix[depth] = fixed_suffix[depth + 1];
        if (tasks[depth].fixed_pattern >= 0) {
            for (int column : pattern_columns[tasks[depth].fixed_pattern]) {
                ++fixed_suffix[depth][column];
            }
        }
    }

    std::array<std::uint16_t, side> pattern_at_column{};
    for (int pattern = 0; pattern < n; ++pattern) {
        for (int column : pattern_columns[pattern]) {
            pattern_at_column[column] |= std::uint16_t(1u << pattern);
        }
    }

    std::array<int, side> column_degree{};
    Bits256 selected_bits{};
    std::array<int, 32> selected_list{};
    int selected_count = 0;
    int used_patterns = 0;
    long long nodes = 0;

    auto creates_triple = [&](int point) {
        for (int index = 0; index < selected_count; ++index) {
            const int anchor = selected_list[index];
            if (intersects(through[point * point_count + anchor], selected_bits)) {
                return true;
            }
        }
        return false;
    };

    std::function<bool(int)> search = [&](int depth) {
        ++nodes;
        if (depth == side) {
            return std::all_of(
                column_degree.begin(),
                column_degree.end(),
                [](int degree) { return degree == 2; }
            );
        }

        const Task task = tasks[depth];
        std::array<int, n> pattern_options{};
        int option_count = 0;
        if (task.fixed_pattern >= 0) {
            pattern_options[option_count++] = task.fixed_pattern;
        } else {
            for (int pattern = 0; pattern < n; ++pattern) {
                if (!(used_patterns & (1 << pattern))) {
                    pattern_options[option_count++] = pattern;
                }
            }
        }

        for (int option = 0; option < option_count; ++option) {
            const int pattern = pattern_options[option];
            const auto& columns = pattern_columns[pattern];
            std::array<std::pair<int, int>, 6> pairs{};
            int pair_count = 0;
            for (int first = 0; first < 4; ++first) {
                for (int second = first + 1; second < 4; ++second) {
                    pairs[pair_count++] = {columns[first], columns[second]};
                }
            }

            for (const auto [first_column, second_column] : pairs) {
                if (column_degree[first_column] >= 2
                    || column_degree[second_column] >= 2) {
                    continue;
                }

                const int first_point = task.row * side + first_column;
                const int second_point = task.row * side + second_column;
                if (creates_triple(first_point)) continue;
                setbit(selected_bits, first_point);
                selected_list[selected_count++] = first_point;
                const bool second_bad = creates_triple(second_point);
                if (second_bad) {
                    --selected_count;
                    clearbit(selected_bits, first_point);
                    continue;
                }

                setbit(selected_bits, second_point);
                selected_list[selected_count++] = second_point;
                ++column_degree[first_column];
                ++column_degree[second_column];
                if (task.fixed_pattern < 0) used_patterns |= 1 << pattern;

                bool possible = true;
                const int unused_mask = ((1 << n) - 1) ^ used_patterns;
                for (int column = 0; column < side; ++column) {
                    const int capacity = fixed_suffix[depth + 1][column]
                        + __builtin_popcount(
                            unsigned(pattern_at_column[column] & unused_mask)
                        );
                    if (column_degree[column] > 2
                        || column_degree[column] + capacity < 2) {
                        possible = false;
                        break;
                    }
                }

                if (possible && search(depth + 1)) return true;

                if (task.fixed_pattern < 0) used_patterns ^= 1 << pattern;
                --column_degree[first_column];
                --column_degree[second_column];
                --selected_count;
                clearbit(selected_bits, second_point);
                --selected_count;
                clearbit(selected_bits, first_point);
            }
        }
        return false;
    };

    return {search(0), nodes};
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: verifier <cc|cf|fc|ff>\n";
        return 2;
    }
    const std::string orientation = argv[1];
    if (orientation != "cc" && orientation != "cf"
        && orientation != "fc" && orientation != "ff") {
        return 2;
    }

    const auto affine = affine_permutations();
    long long total_nodes = 0;
    long long maximum_nodes = 0;
    int pair_count = 0;
    for (const auto& target : affine) {
        for (const auto& column_relative : affine) {
            const SearchResult result =
                search_geometry(target, column_relative, orientation);
            if (result.feasible) {
                std::cout << "FOUND o=" << orientation << '\n';
                return 0;
            }
            total_nodes += result.nodes;
            maximum_nodes = std::max(maximum_nodes, result.nodes);
            ++pair_count;
        }
    }

    std::cout
        << "NONE o=" << orientation
        << " pairs=" << pair_count
        << " total=" << total_nodes
        << " avg=" << (total_nodes / pair_count)
        << " max=" << maximum_nodes
        << '\n';
    return 0;
}

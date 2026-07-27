#include <algorithm>
#include <array>
#include <cstdint>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <utility>
#include <vector>

using Permutation = std::vector<int>;

struct Point { int x; int y; };

long long determinant(Point a, Point b, Point c) {
    return 1LL * (b.x - a.x) * (c.y - a.y)
         - 1LL * (b.y - a.y) * (c.x - a.x);
}

std::vector<Permutation> affine_permutations(int n) {
    std::vector<Permutation> result;
    for (int multiplier = 0; multiplier < n; ++multiplier) {
        if (std::gcd(multiplier, n) != 1) continue;
        for (int shift = 0; shift < n; ++shift) {
            Permutation permutation(n);
            for (int value = 0; value < n; ++value)
                permutation[value] = (multiplier * value + shift) % n;
            result.push_back(std::move(permutation));
        }
    }
    return result;
}

int flatten(int coarse, int fine, char mode, int n) {
    return mode == 'c' ? n * coarse + fine : 2 * fine + coarse;
}

struct ThroughTable {
    int side;
    int point_count;
    int words;
    std::vector<std::uint64_t> data;

    explicit ThroughTable(int requested_side)
        : side(requested_side),
          point_count(side * side),
          words((point_count + 63) / 64),
          data(static_cast<size_t>(point_count) * point_count * words) {
        std::vector<Point> points(point_count);
        for (int x = 0; x < side; ++x)
            for (int y = 0; y < side; ++y)
                points[x * side + y] = {x, y};

        for (int point = 0; point < point_count; ++point)
            for (int anchor = 0; anchor < point_count; ++anchor) {
                if (anchor == point) continue;
                size_t base =
                    (static_cast<size_t>(point) * point_count + anchor) * words;
                for (int third = 0; third < point_count; ++third) {
                    if (third == anchor || third == point) continue;
                    if (determinant(
                        points[anchor], points[point], points[third]
                    ) == 0)
                        data[base + (third >> 6)]
                            |= std::uint64_t(1) << (third & 63);
                }
            }
    }

    bool intersects(
        int point,
        int anchor,
        std::vector<std::uint64_t> const& selected
    ) const {
        size_t base =
            (static_cast<size_t>(point) * point_count + anchor) * words;
        for (int word = 0; word < words; ++word)
            if (data[base + word] & selected[word]) return true;
        return false;
    }
};

struct SearchResult {
    bool feasible = false;
    std::uint64_t nodes = 0;
    std::vector<int> points;
};

SearchResult search_geometry(
    int n,
    Permutation const& target,
    Permutation const& column_relative,
    std::string const& orientation,
    ThroughTable const& through
) {
    int side = 2 * n;
    Permutation relative(n);
    for (int value = 0; value < n; ++value) relative[value] = value ^ 1;

    std::vector<std::array<int, 4>> pattern_columns(n);
    for (int value = 0; value < n; ++value) {
        pattern_columns[value] = {
            flatten(0, target[value], orientation[1], n),
            flatten(0, target[relative[value]], orientation[1], n),
            flatten(1, column_relative[target[value]], orientation[1], n),
            flatten(
                1,
                column_relative[target[relative[value]]],
                orientation[1],
                n
            ),
        };
        auto& columns = pattern_columns[value];
        std::sort(columns.begin(), columns.end());
        if (std::adjacent_find(columns.begin(), columns.end()) != columns.end())
            return {};
    }

    struct Task { int row; int fixed_pattern; };
    std::vector<Task> tasks;
    tasks.reserve(side);
    for (int value = 0; value < n; ++value)
        tasks.push_back({flatten(0, value, orientation[0], n), value});
    for (int row_digit = 0; row_digit < n; ++row_digit)
        tasks.push_back({flatten(1, row_digit, orientation[0], n), -1});
    std::sort(tasks.begin(), tasks.begin() + n, [](Task first, Task second) {
        return first.row < second.row;
    });
    std::sort(tasks.begin() + n, tasks.end(), [](Task first, Task second) {
        return first.row < second.row;
    });

    std::vector<std::vector<int>> fixed_suffix(
        side + 1, std::vector<int>(side)
    );
    for (int depth = side - 1; depth >= 0; --depth) {
        fixed_suffix[depth] = fixed_suffix[depth + 1];
        if (tasks[depth].fixed_pattern >= 0)
            for (int column : pattern_columns[tasks[depth].fixed_pattern])
                ++fixed_suffix[depth][column];
    }

    std::vector<std::uint64_t> pattern_at_column(side);
    for (int pattern = 0; pattern < n; ++pattern)
        for (int column : pattern_columns[pattern])
            pattern_at_column[column] |= std::uint64_t(1) << pattern;

    std::vector<int> column_degree(side);
    std::vector<std::uint64_t> selected_bits(through.words);
    std::vector<int> selected_list(2 * side);
    int selected_count = 0;
    std::uint64_t used_patterns = 0;
    std::uint64_t nodes = 0;
    std::vector<int> witness;

    auto setbit = [&](int point) {
        selected_bits[point >> 6] |= std::uint64_t(1) << (point & 63);
    };
    auto clearbit = [&](int point) {
        selected_bits[point >> 6] &= ~(std::uint64_t(1) << (point & 63));
    };
    auto creates_triple = [&](int point) {
        for (int index = 0; index < selected_count; ++index)
            if (through.intersects(
                point, selected_list[index], selected_bits
            ))
                return true;
        return false;
    };

    std::function<bool(int)> search = [&](int depth) {
        ++nodes;
        if (depth == side) {
            if (!std::all_of(
                column_degree.begin(),
                column_degree.end(),
                [](int degree) { return degree == 2; }
            ))
                return false;
            witness.assign(
                selected_list.begin(), selected_list.begin() + selected_count
            );
            return true;
        }

        Task const task = tasks[depth];
        std::vector<int> pattern_options;
        if (task.fixed_pattern >= 0) {
            pattern_options.push_back(task.fixed_pattern);
        } else {
            for (int pattern = 0; pattern < n; ++pattern)
                if (!(used_patterns & (std::uint64_t(1) << pattern)))
                    pattern_options.push_back(pattern);
        }

        for (int pattern : pattern_options) {
            auto const& columns = pattern_columns[pattern];
            for (int first = 0; first < 4; ++first)
                for (int second = first + 1; second < 4; ++second) {
                    int first_column = columns[first];
                    int second_column = columns[second];
                    if (column_degree[first_column] >= 2
                        || column_degree[second_column] >= 2)
                        continue;

                    int first_point = task.row * side + first_column;
                    int second_point = task.row * side + second_column;
                    if (creates_triple(first_point)) continue;
                    setbit(first_point);
                    selected_list[selected_count++] = first_point;
                    if (creates_triple(second_point)) {
                        --selected_count;
                        clearbit(first_point);
                        continue;
                    }

                    setbit(second_point);
                    selected_list[selected_count++] = second_point;
                    ++column_degree[first_column];
                    ++column_degree[second_column];
                    if (task.fixed_pattern < 0)
                        used_patterns |= std::uint64_t(1) << pattern;

                    bool possible = true;
                    std::uint64_t unused =
                        ((std::uint64_t(1) << n) - 1) ^ used_patterns;
                    for (int column = 0; column < side; ++column) {
                        int capacity = fixed_suffix[depth + 1][column]
                            + __builtin_popcountll(
                                pattern_at_column[column] & unused
                            );
                        if (column_degree[column] > 2
                            || column_degree[column] + capacity < 2) {
                            possible = false;
                            break;
                        }
                    }

                    if (possible && search(depth + 1)) return true;

                    if (task.fixed_pattern < 0)
                        used_patterns ^= std::uint64_t(1) << pattern;
                    --column_degree[first_column];
                    --column_degree[second_column];
                    --selected_count;
                    clearbit(second_point);
                    --selected_count;
                    clearbit(first_point);
                }
        }
        return false;
    };

    bool feasible = search(0);
    return {feasible, nodes, witness};
}

int main(int argc, char** argv) {
    if (argc < 3 || argc > 5) {
        std::cerr
            << "usage: search N <cc|cf|fc|ff> [FIRST_PAIR] [PAIR_COUNT]\n";
        return 2;
    }

    int n = std::stoi(argv[1]);
    std::string orientation = argv[2];
    if (n < 2 || n > 20 || n % 2
        || (orientation != "cc" && orientation != "cf"
            && orientation != "fc" && orientation != "ff"))
        return 2;

    auto affine = affine_permutations(n);
    int total_pairs = static_cast<int>(affine.size() * affine.size());
    int first_pair = argc >= 4 ? std::stoi(argv[3]) : 0;
    int pair_count = argc >= 5 ? std::stoi(argv[4]) : total_pairs - first_pair;
    if (first_pair < 0 || pair_count < 0
        || first_pair + pair_count > total_pairs)
        return 2;

    ThroughTable through(2 * n);
    std::uint64_t total_nodes = 0;
    std::uint64_t maximum_nodes = 0;

    for (int pair = first_pair; pair < first_pair + pair_count; ++pair) {
        int target_index = pair / static_cast<int>(affine.size());
        int relative_index = pair % static_cast<int>(affine.size());
        SearchResult result = search_geometry(
            n,
            affine[target_index],
            affine[relative_index],
            orientation,
            through
        );
        total_nodes += result.nodes;
        maximum_nodes = std::max(maximum_nodes, result.nodes);
        if (result.feasible) {
            std::cout << "FOUND n=" << n
                      << " o=" << orientation
                      << " pair=" << pair
                      << " target=" << target_index
                      << " relative=" << relative_index
                      << " nodes=" << result.nodes
                      << " cells=";
            for (int point : result.points)
                std::cout << '(' << point / (2 * n)
                          << ',' << point % (2 * n) << ')';
            std::cout << '\n';
            return 0;
        }
    }

    std::cout << "NONE n=" << n
              << " o=" << orientation
              << " first=" << first_pair
              << " pairs=" << pair_count
              << " total=" << total_nodes
              << " avg=" << (pair_count ? total_nodes / pair_count : 0)
              << " max=" << maximum_nodes
              << '\n';
    return 0;
}

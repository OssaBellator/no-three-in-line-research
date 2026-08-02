#include <array>
#include <algorithm>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>

using Permutation = std::array<int, 6>;

struct Point {
    int x;
    int y;
};

long long determinant(Point a, Point b, Point c) {
    return 1LL * (b.x - a.x) * (c.y - a.y)
        - 1LL * (b.y - a.y) * (c.x - a.x);
}

Permutation compose(const Permutation& first, const Permutation& second) {
    Permutation result{};
    for (int index = 0; index < 6; ++index) {
        result[index] = first[second[index]];
    }
    return result;
}

std::vector<Permutation> affine_permutations() {
    std::vector<Permutation> result;
    for (int multiplier : {1, 5}) {
        for (int translation = 0; translation < 6; ++translation) {
            Permutation permutation{};
            for (int x = 0; x < 6; ++x) {
                permutation[x] = (multiplier * x + translation) % 6;
            }
            result.push_back(permutation);
        }
    }
    return result;
}

Permutation relative_representative(int type) {
    if (type == 0) {
        return {1, 2, 3, 4, 5, 0};  // (6)
    }
    if (type == 1) {
        return {1, 2, 3, 0, 5, 4};  // (4,2)
    }
    return {1, 2, 0, 4, 5, 3};      // (3,3)
}

std::vector<Point> build_host(
    const Permutation& target,
    const Permutation& row_relative,
    const Permutation& column_relative,
    const Permutation& inner_relative,
    const std::string& orientation
) {
    const Permutation identity = {0, 1, 2, 3, 4, 5};
    std::set<std::pair<int, int>> cells;

    for (int coarse_row = 0; coarse_row < 2; ++coarse_row) {
        for (int coarse_column = 0; coarse_column < 2; ++coarse_column) {
            for (int inner_layer = 0; inner_layer < 2; ++inner_layer) {
                const Permutation map = compose(
                    coarse_column ? column_relative : identity,
                    compose(
                        target,
                        compose(
                            inner_layer ? inner_relative : identity,
                            coarse_row ? row_relative : identity
                        )
                    )
                );
                for (int fine_row = 0; fine_row < 6; ++fine_row) {
                    const int fine_column = map[fine_row];
                    const int x = orientation[0] == 'c'
                        ? 6 * coarse_row + fine_row
                        : 2 * fine_row + coarse_row;
                    const int y = orientation[1] == 'c'
                        ? 6 * coarse_column + fine_column
                        : 2 * fine_column + coarse_column;
                    cells.emplace(x, y);
                }
            }
        }
    }

    if (cells.size() != 48) {
        std::abort();
    }

    std::vector<Point> result;
    for (const auto& [x, y] : cells) {
        result.push_back({x, y});
    }
    return result;
}

struct SearchResult {
    bool feasible;
    long long nodes;
    std::vector<Point> selected;
};

SearchResult search_degree_two_state(const std::vector<Point>& host) {
    constexpr int side = 12;
    const int cell_count = static_cast<int>(host.size());

    std::vector<std::vector<int>> rows(side);
    std::map<std::pair<int, int>, int> cell_index;
    for (int index = 0; index < cell_count; ++index) {
        rows[host[index].x].push_back(host[index].y);
        cell_index[{host[index].x, host[index].y}] = index;
    }

    std::vector<std::vector<unsigned long long>> forbidden_pairs(cell_count);
    for (int point_index = 0; point_index < cell_count; ++point_index) {
        const Point point = host[point_index];
        for (int first = 0; first < cell_count; ++first) {
            if (host[first].x >= point.x) {
                continue;
            }
            for (int second = first + 1; second < cell_count; ++second) {
                if (host[second].x >= point.x) {
                    continue;
                }
                if (determinant(host[first], host[second], point) == 0) {
                    forbidden_pairs[point_index].push_back(
                        (1ULL << first) | (1ULL << second)
                    );
                }
            }
        }
    }

    int remaining[side + 1][side]{};
    for (int row = side - 1; row >= 0; --row) {
        for (int column = 0; column < side; ++column) {
            remaining[row][column] = remaining[row + 1][column];
        }
        for (int column : rows[row]) {
            ++remaining[row][column];
        }
    }

    int column_degree[side]{};
    std::vector<Point> selected;
    unsigned long long selected_mask = 0;
    long long nodes = 0;

    std::function<bool(int)> search = [&](int row) {
        ++nodes;
        if (row == side) {
            return selected.size() == 24;
        }

        const auto& incident = rows[row];
        for (int first = 0; first < 4; ++first) {
            for (int second = first + 1; second < 4; ++second) {
                const int first_column = incident[first];
                const int second_column = incident[second];
                if (column_degree[first_column] >= 2
                    || column_degree[second_column] >= 2) {
                    continue;
                }

                const Point new_points[2] = {
                    {row, first_column},
                    {row, second_column},
                };
                bool creates_triple = false;
                for (const Point point : new_points) {
                    const int index = cell_index[{point.x, point.y}];
                    for (const unsigned long long pair_mask : forbidden_pairs[index]) {
                        if ((selected_mask & pair_mask) == pair_mask) {
                            creates_triple = true;
                            break;
                        }
                    }
                    if (creates_triple) {
                        break;
                    }
                }
                if (creates_triple) {
                    continue;
                }

                ++column_degree[first_column];
                ++column_degree[second_column];
                bool feasible_completion = true;
                for (int column = 0; column < side; ++column) {
                    if (column_degree[column] > 2
                        || column_degree[column] + remaining[row + 1][column] < 2) {
                        feasible_completion = false;
                        break;
                    }
                }

                if (feasible_completion) {
                    const int first_index = cell_index[{row, first_column}];
                    const int second_index = cell_index[{row, second_column}];
                    const unsigned long long added_mask
                        = (1ULL << first_index) | (1ULL << second_index);
                    selected_mask |= added_mask;
                    selected.push_back(new_points[0]);
                    selected.push_back(new_points[1]);
                    if (search(row + 1)) {
                        return true;
                    }
                    selected.pop_back();
                    selected.pop_back();
                    selected_mask ^= added_mask;
                }

                --column_degree[first_column];
                --column_degree[second_column];
            }
        }
        return false;
    };

    const bool feasible = search(0);
    return {feasible, nodes, selected};
}

void print_permutation(const Permutation& permutation) {
    std::cout << '(';
    for (int index = 0; index < 6; ++index) {
        if (index) {
            std::cout << ',';
        }
        std::cout << permutation[index];
    }
    std::cout << ')';
}

int main() {
    const auto affine = affine_permutations();
    const std::vector<std::string> orientations = {"cc", "cf", "fc", "ff"};
    const std::vector<std::string> type_names = {"6", "4+2", "3+3"};

    for (int type = 0; type < 3; ++type) {
        const Permutation inner_relative = relative_representative(type);
        for (const std::string& orientation : orientations) {
            int feasible_hosts = 0;
            long long total_nodes = 0;
            long long maximum_nodes = 0;
            Permutation witness_target{};
            Permutation witness_row{};
            Permutation witness_column{};
            std::vector<Point> witness_selected;

            for (const Permutation& target : affine) {
                for (const Permutation& row_relative : affine) {
                    for (const Permutation& column_relative : affine) {
                        const auto host = build_host(
                            target,
                            row_relative,
                            column_relative,
                            inner_relative,
                            orientation
                        );
                        const SearchResult result = search_degree_two_state(host);
                        total_nodes += result.nodes;
                        maximum_nodes = std::max(maximum_nodes, result.nodes);
                        if (result.feasible) {
                            ++feasible_hosts;
                            witness_target = target;
                            witness_row = row_relative;
                            witness_column = column_relative;
                            witness_selected = result.selected;
                        }
                    }
                }
            }

            std::cout
                << "type=" << type_names[type]
                << " orientation=" << orientation
                << " feasible_hosts=" << feasible_hosts
                << " total_nodes=" << total_nodes
                << " maximum_nodes=" << maximum_nodes
                << '\n';

            if (feasible_hosts) {
                std::cout << "T=";
                print_permutation(witness_target);
                std::cout << " P=";
                print_permutation(witness_row);
                std::cout << " Q=";
                print_permutation(witness_column);
                std::cout << '\n';
                for (const Point point : witness_selected) {
                    std::cout << '(' << point.x << ',' << point.y << ") ";
                }
                std::cout << '\n';
            }
        }
    }
}

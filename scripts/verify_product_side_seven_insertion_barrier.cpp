// Exact full-selector census for the side-seven insertion-recursion barrier.
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>

struct Point { int x, y; };

long long determinant(const Point& a, const Point& b, const Point& c) {
    return 1LL * (b.x - a.x) * (c.y - a.y)
         - 1LL * (b.y - a.y) * (c.x - a.x);
}

std::vector<int> identity(int n) {
    std::vector<int> result(n);
    std::iota(result.begin(), result.end(), 0);
    return result;
}

std::vector<int> compose(const std::vector<int>& first, const std::vector<int>& second) {
    std::vector<int> result(first.size());
    for (int i = 0; i < static_cast<int>(first.size()); ++i) {
        result[i] = first[second[i]];
    }
    return result;
}

struct SelectorSearch {
    int side = 0;
    int row_count = 0;
    std::vector<std::array<Point, 4>> rows;
    std::vector<std::array<std::pair<int, int>, 6>> options;
    std::vector<Point> selected;
    std::array<int, 32> column_degree{};
    long long nodes = 0;

    bool search(int row) {
        ++nodes;
        if (row == row_count) {
            for (int column = 0; column < row_count; ++column) {
                if (column_degree[column] != 2) return false;
            }
            return true;
        }

        for (int column = 0; column < row_count; ++column) {
            int available_rows = 0;
            for (int later = row; later < row_count; ++later) {
                for (const Point& point : rows[later]) {
                    if (point.y == column) {
                        ++available_rows;
                        break;
                    }
                }
            }
            if (column_degree[column] + available_rows < 2) return false;
        }

        for (const auto [left_index, right_index] : options[row]) {
            Point left = rows[row][left_index];
            Point right = rows[row][right_index];
            if (column_degree[left.y] >= 2 || column_degree[right.y] >= 2) continue;

            bool bad = false;
            for (int i = 0; i < static_cast<int>(selected.size()) && !bad; ++i) {
                for (int j = i + 1; j < static_cast<int>(selected.size()); ++j) {
                    if (determinant(selected[i], selected[j], left) == 0
                        || determinant(selected[i], selected[j], right) == 0) {
                        bad = true;
                        break;
                    }
                }
            }
            for (const Point& point : selected) {
                if (!bad && determinant(point, left, right) == 0) bad = true;
            }
            if (bad) continue;

            selected.push_back(left);
            selected.push_back(right);
            ++column_degree[left.y];
            ++column_degree[right.y];
            if (search(row + 1)) return true;
            --column_degree[left.y];
            --column_degree[right.y];
            selected.pop_back();
            selected.pop_back();
        }
        return false;
    }

    bool solve(std::vector<std::array<Point, 4>> host_rows) {
        rows = std::move(host_rows);
        row_count = static_cast<int>(rows.size());
        side = row_count / 2;
        nodes = 0;
        selected.clear();
        column_degree.fill(0);
        options.assign(row_count, {});
        for (int row = 0; row < row_count; ++row) {
            int index = 0;
            for (int left = 0; left < 4; ++left) {
                for (int right = left + 1; right < 4; ++right) {
                    options[row][index++] = {left, right};
                }
            }
        }
        return search(0);
    }
};

std::vector<std::array<Point, 4>> host_rows(
    int n,
    const std::vector<int>& h,
    const std::vector<int>& t,
    const std::vector<int>& p,
    const std::vector<int>& q,
    int orientation
) {
    const std::vector<int> id = identity(n);
    std::vector<int> maps[2][2][2];
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            for (int s = 0; s < 2; ++s) {
                maps[i][j][s] = compose(
                    j ? q : id,
                    compose(t, compose(s ? h : id, i ? p : id))
                );
            }
        }
    }

    std::vector<std::array<Point, 4>> result(2 * n);
    for (int x = 0; x < 2 * n; ++x) {
        int i = orientation < 2 ? x / n : x % 2;
        int u = orientation < 2 ? x % n : x / 2;
        int index = 0;
        std::set<int> columns;
        for (int j = 0; j < 2; ++j) {
            for (int s = 0; s < 2; ++s) {
                int v = maps[i][j][s][u];
                int y = orientation % 2 == 0 ? n * j + v : 2 * v + j;
                result[x][index++] = {x, y};
                columns.insert(y);
            }
        }
        assert(columns.size() == 4);
    }
    return result;
}

std::vector<std::vector<int>> extensions(const std::vector<int>& permutation) {
    int n = static_cast<int>(permutation.size());
    std::vector<std::vector<int>> result;
    for (int source = -1; source < n; ++source) {
        std::vector<int> extension(n + 1);
        for (int index = 0; index < n; ++index) extension[index] = permutation[index];
        if (source < 0) {
            extension[n] = n;
        } else {
            extension[n] = permutation[source];
            extension[source] = n;
        }
        result.push_back(extension);
    }
    return result;
}

std::vector<int> insert_cycle_label(const std::vector<int>& h, int source) {
    int n = static_cast<int>(h.size());
    std::vector<int> result(n + 1);
    for (int index = 0; index < n; ++index) result[index] = h[index];
    result[n] = h[source];
    result[source] = n;
    return result;
}

std::pair<long long, long long> insertion_case(
    const std::vector<int>& h6,
    const std::vector<int>& t6,
    const std::vector<int>& p6,
    const std::vector<int>& q6,
    const std::vector<int>& cycle_sources
) {
    auto t_extensions = extensions(t6);
    auto p_extensions = extensions(p6);
    auto q_extensions = extensions(q6);
    SelectorSearch search;
    long long hosts = 0;
    long long nodes = 0;

    for (int cycle_source : cycle_sources) {
        auto h = insert_cycle_label(h6, cycle_source);
        for (const auto& t : t_extensions) {
            for (const auto& p : p_extensions) {
                for (const auto& q : q_extensions) {
                    for (int orientation = 0; orientation < 4; ++orientation) {
                        ++hosts;
                        bool feasible = search.solve(host_rows(7, h, t, p, q, orientation));
                        assert(!feasible);
                        nodes += search.nodes;
                    }
                }
            }
        }
    }
    return {hosts, nodes};
}

void verify_cycle7() {
    auto result = insertion_case(
        {1, 2, 3, 4, 5, 0},
        {2, 1, 0, 5, 4, 3},
        {5, 4, 3, 2, 1, 0},
        {5, 4, 3, 2, 1, 0},
        {0, 1, 2, 3, 4, 5}
    );
    assert(result == std::make_pair(8232LL, 34170644LL));
}

void verify_cycle52() {
    auto result = insertion_case(
        {1, 4, 5, 0, 3, 2},
        {4, 5, 0, 1, 2, 3},
        {2, 4, 3, 5, 1, 0},
        {5, 4, 3, 2, 1, 0},
        {0, 1, 3, 4}
    );
    assert(result == std::make_pair(5488LL, 13077659LL));
}

void verify_cycle43() {
    auto result = insertion_case(
        {1, 2, 0, 4, 5, 3},
        {1, 3, 4, 2, 0, 5},
        {4, 5, 3, 2, 0, 1},
        {3, 1, 5, 2, 4, 0},
        {0, 1, 2, 3, 4, 5}
    );
    assert(result == std::make_pair(8232LL, 34754272LL));
}

void verify_affine222() {
    std::vector<std::vector<int>> affine;
    for (int multiplier : {1, 5}) {
        for (int shift = 0; shift < 6; ++shift) {
            std::vector<int> permutation(6);
            for (int value = 0; value < 6; ++value) {
                permutation[value] = (multiplier * value + shift) % 6;
            }
            affine.push_back(permutation);
        }
    }

    const std::vector<int> h = {1, 0, 3, 2, 5, 4};
    SelectorSearch search;
    long long hosts = 0;
    long long nodes = 0;
    for (const auto& t : affine) {
        for (const auto& p : affine) {
            for (const auto& q : affine) {
                for (int orientation = 0; orientation < 4; ++orientation) {
                    ++hosts;
                    bool feasible = search.solve(host_rows(6, h, t, p, q, orientation));
                    assert(!feasible);
                    nodes += search.nodes;
                }
            }
        }
    }
    assert(hosts == 6912);
    assert(nodes == 14345445);
}

int main(int argc, char** argv) {
    assert(argc == 2);
    std::string selected_case = argv[1];
    if (selected_case == "cycle7") verify_cycle7();
    else if (selected_case == "cycle52") verify_cycle52();
    else if (selected_case == "cycle43") verify_cycle43();
    else if (selected_case == "affine222") verify_affine222();
    else assert(false && "unknown case");
    std::cout << selected_case << ": PASS\n";
}

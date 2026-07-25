// Exact checks for PX501--PX503 side-seven local minima and product boxes.
#include <algorithm>
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
    for (int index = 0; index < static_cast<int>(first.size()); ++index) {
        result[index] = first[second[index]];
    }
    return result;
}

std::vector<std::array<Point, 4>> host_rows(
    const std::vector<int>& h,
    const std::vector<int>& t,
    const std::vector<int>& p,
    const std::vector<int>& q,
    int orientation
) {
    const auto id = identity(7);
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

    std::vector<std::array<Point, 4>> rows(14);
    for (int x = 0; x < 14; ++x) {
        const int i = orientation < 2 ? x / 7 : x % 2;
        const int u = orientation < 2 ? x % 7 : x / 2;
        int next = 0;
        std::set<int> columns;
        for (int j = 0; j < 2; ++j) {
            for (int s = 0; s < 2; ++s) {
                const int v = maps[i][j][s][u];
                const int y = orientation % 2 == 0 ? 7 * j + v : 2 * v + j;
                rows[x][next++] = {x, y};
                columns.insert(y);
            }
        }
        assert(columns.size() == 4);
    }
    return rows;
}

constexpr int PAIRS[6][2] = {
    {0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}
};

int triple_count(
    const std::vector<std::array<Point, 4>>& rows,
    const std::array<int, 14>& options
) {
    std::vector<Point> selected;
    for (int row = 0; row < 14; ++row) {
        selected.push_back(rows[row][PAIRS[options[row]][0]]);
        selected.push_back(rows[row][PAIRS[options[row]][1]]);
    }
    int result = 0;
    for (int first = 0; first < 28; ++first) {
        for (int second = first + 1; second < 28; ++second) {
            for (int third = second + 1; third < 28; ++third) {
                result += determinant(
                    selected[first], selected[second], selected[third]
                ) == 0;
            }
        }
    }
    return result;
}

struct ThresholdSearch {
    std::vector<std::array<Point, 4>> rows;
    std::vector<Point> selected;
    std::array<int, 14> column_degree{};
    long long nodes = 0;
    int bound = 0;

    int added_triples(const Point& left, const Point& right) const {
        int result = 0;
        for (int first = 0; first < static_cast<int>(selected.size()); ++first) {
            for (int second = first + 1;
                 second < static_cast<int>(selected.size()); ++second) {
                result += determinant(selected[first], selected[second], left) == 0;
                result += determinant(selected[first], selected[second], right) == 0;
            }
        }
        for (const Point& point : selected) {
            result += determinant(point, left, right) == 0;
        }
        return result;
    }

    bool search(int used_rows, int depth, int triples) {
        ++nodes;
        if (triples >= bound) return false;
        if (depth == 14) {
            for (int degree : column_degree) if (degree != 2) return false;
            return true;
        }

        for (int column = 0; column < 14; ++column) {
            int available = 0;
            for (int row = 0; row < 14; ++row) {
                if (used_rows >> row & 1) continue;
                for (const Point& point : rows[row]) {
                    if (point.y == column) {
                        ++available;
                        break;
                    }
                }
            }
            if (column_degree[column] + available < 2) return false;
        }

        int branch_row = -1;
        int best_count = 7;
        std::array<std::pair<int, int>, 6> branch_options{};
        int branch_count = 0;
        for (int row = 0; row < 14; ++row) {
            if (used_rows >> row & 1) continue;
            std::array<std::pair<int, int>, 6> choices{};
            int count = 0;
            for (int option = 0; option < 6; ++option) {
                const Point left = rows[row][PAIRS[option][0]];
                const Point right = rows[row][PAIRS[option][1]];
                if (column_degree[left.y] >= 2 || column_degree[right.y] >= 2) continue;
                const int added = added_triples(left, right);
                if (triples + added < bound) choices[count++] = {added, option};
            }
            if (count == 0) return false;
            if (count < best_count) {
                best_count = count;
                branch_row = row;
                branch_count = count;
                branch_options = choices;
                if (count == 1) break;
            }
        }

        std::sort(branch_options.begin(), branch_options.begin() + branch_count);
        for (int index = 0; index < branch_count; ++index) {
            const auto [added, option] = branch_options[index];
            const Point left = rows[branch_row][PAIRS[option][0]];
            const Point right = rows[branch_row][PAIRS[option][1]];
            selected.push_back(left);
            selected.push_back(right);
            ++column_degree[left.y];
            ++column_degree[right.y];
            if (search(used_rows | 1 << branch_row, depth + 1, triples + added)) {
                return true;
            }
            --column_degree[left.y];
            --column_degree[right.y];
            selected.pop_back();
            selected.pop_back();
        }
        return false;
    }

    bool solve(std::vector<std::array<Point, 4>> host, int strict_bound) {
        rows = std::move(host);
        selected.clear();
        column_degree.fill(0);
        nodes = 0;
        bound = strict_bound;
        return search(0, 0, 0);
    }
};

struct ZeroSearch {
    std::vector<std::array<Point, 4>> rows;
    std::vector<Point> selected;
    std::array<int, 14> column_degree{};
    long long nodes = 0;

    bool blocked(const Point& left, const Point& right) const {
        for (int first = 0; first < static_cast<int>(selected.size()); ++first) {
            for (int second = first + 1;
                 second < static_cast<int>(selected.size()); ++second) {
                if (determinant(selected[first], selected[second], left) == 0
                    || determinant(selected[first], selected[second], right) == 0) {
                    return true;
                }
            }
        }
        for (const Point& point : selected) {
            if (determinant(point, left, right) == 0) return true;
        }
        return false;
    }

    bool search(int used_rows, int depth) {
        ++nodes;
        if (depth == 14) {
            for (int degree : column_degree) if (degree != 2) return false;
            return true;
        }

        for (int column = 0; column < 14; ++column) {
            int available = 0;
            for (int row = 0; row < 14; ++row) {
                if (used_rows >> row & 1) continue;
                for (const Point& point : rows[row]) {
                    if (point.y == column) {
                        ++available;
                        break;
                    }
                }
            }
            if (column_degree[column] + available < 2) return false;
        }

        int branch_row = -1;
        int best_count = 7;
        std::array<int, 6> branch_options{};
        int branch_count = 0;
        for (int row = 0; row < 14; ++row) {
            if (used_rows >> row & 1) continue;
            std::array<int, 6> choices{};
            int count = 0;
            for (int option = 0; option < 6; ++option) {
                const Point left = rows[row][PAIRS[option][0]];
                const Point right = rows[row][PAIRS[option][1]];
                if (column_degree[left.y] >= 2 || column_degree[right.y] >= 2) continue;
                if (!blocked(left, right)) choices[count++] = option;
            }
            if (count == 0) return false;
            if (count < best_count) {
                best_count = count;
                branch_row = row;
                branch_count = count;
                branch_options = choices;
                if (count == 1) break;
            }
        }

        for (int index = 0; index < branch_count; ++index) {
            const int option = branch_options[index];
            const Point left = rows[branch_row][PAIRS[option][0]];
            const Point right = rows[branch_row][PAIRS[option][1]];
            selected.push_back(left);
            selected.push_back(right);
            ++column_degree[left.y];
            ++column_degree[right.y];
            if (search(used_rows | 1 << branch_row, depth + 1)) return true;
            --column_degree[left.y];
            --column_degree[right.y];
            selected.pop_back();
            selected.pop_back();
        }
        return false;
    }

    bool solve(std::vector<std::array<Point, 4>> host) {
        rows = std::move(host);
        selected.clear();
        column_degree.fill(0);
        nodes = 0;
        return search(0, 0);
    }
};

struct CaseData {
    std::string name;
    std::vector<int> h, t, p, q;
    std::array<int, 14> witness;
    int minimum;
    long long minimum_nodes;
    long long box_nodes;
    long long box_max_nodes;
};

const std::array<CaseData, 4> CASES = {{
    {"cycle7", {1,2,3,4,5,6,0}, {4,6,3,5,1,0,2},
     {5,4,0,6,2,1,3}, {6,0,5,1,2,3,4},
     {0,3,0,3,5,2,2,2,2,3,0,5,5,2},
     4, 22233, 34528876, 3574},
    {"cycle52", {1,2,3,4,0,6,5}, {6,4,5,2,3,1,0},
     {4,5,6,1,3,2,0}, {6,0,2,5,1,3,4},
     {2,2,2,2,2,2,2,2,2,2,2,5,0,2},
     3, 8465, 28332904, 3217},
    {"cycle43", {1,2,3,0,5,6,4}, {1,6,4,3,2,0,5},
     {3,5,4,2,1,0,6}, {1,0,6,5,3,4,2},
     {5,5,2,0,0,5,2,0,0,5,5,0,3,3},
     4, 14677, 30642717, 2881},
    {"cycle322", {1,2,0,4,3,6,5}, {6,4,5,2,0,1,3},
     {4,6,5,3,1,2,0}, {3,0,5,6,4,2,1},
     {5,0,3,1,0,5,0,5,5,0,4,3,5,0},
     3, 7983, 33129180, 2792}
}};

std::vector<std::vector<int>> one_swap_box(const std::vector<int>& permutation) {
    std::vector<std::vector<int>> result = {permutation};
    for (int first = 0; first < 7; ++first) {
        for (int second = first + 1; second < 7; ++second) {
            auto next = permutation;
            std::swap(next[first], next[second]);
            result.push_back(std::move(next));
        }
    }
    assert(result.size() == 22);
    return result;
}

void verify_case(const CaseData& data) {
    const auto centre = host_rows(data.h, data.t, data.p, data.q, 0);
    assert(triple_count(centre, data.witness) == data.minimum);

    ThresholdSearch threshold;
    assert(!threshold.solve(centre, data.minimum));
    assert(threshold.nodes == data.minimum_nodes);

    const auto t_box = one_swap_box(data.t);
    const auto p_box = one_swap_box(data.p);
    const auto q_box = one_swap_box(data.q);
    ZeroSearch zero;
    long long hosts = 0;
    long long nodes = 0;
    long long maximum_nodes = 0;

    for (const auto& t : t_box) {
        for (const auto& p : p_box) {
            for (const auto& q : q_box) {
                for (int orientation = 0; orientation < 4; ++orientation) {
                    ++hosts;
                    assert(!zero.solve(host_rows(data.h, t, p, q, orientation)));
                    nodes += zero.nodes;
                    maximum_nodes = std::max(maximum_nodes, zero.nodes);
                }
            }
        }
    }

    assert(hosts == 42592);
    assert(nodes == data.box_nodes);
    assert(maximum_nodes == data.box_max_nodes);
    std::cout << data.name << ": minimum=" << data.minimum
              << ", box_hosts=" << hosts
              << ", box_nodes=" << nodes << " PASS\n";
}

int main(int argc, char** argv) {
    assert(argc == 2);
    const std::string requested = argv[1];
    for (const auto& data : CASES) {
        if (requested == data.name) {
            verify_case(data);
            return 0;
        }
    }
    assert(false && "unknown side-seven class");
}

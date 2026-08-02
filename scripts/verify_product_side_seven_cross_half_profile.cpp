// Exact checks for PX508--PX511 cross-half obstruction counts.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

struct Point { int x, y; };

long long determinant(const Point& a, const Point& b, const Point& c) {
    return 1LL * (b.x - a.x) * (c.y - a.y)
         - 1LL * (b.y - a.y) * (c.x - a.x);
}

constexpr int PAIRS[6][2] = {
    {0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}
};

struct CaseData {
    std::string name;
    std::array<int, 7> h;
    std::array<int, 7> centre_p;
    std::array<int, 14> centre_options;
    std::array<long long, 4> top_clean;
    std::array<long long, 4> half_compatible;
};

const std::array<CaseData, 4> CASES = {{
    {"cycle7", {1,2,3,4,5,6,0}, {5,4,0,6,2,1,3},
     {0,3,0,3,5,2,2,2,2,3,0,5,5,2},
     {30972,55312,30972,55312}, {23743,43448,23743,43448}},
    {"cycle52", {1,2,3,4,0,6,5}, {4,5,6,1,3,2,0},
     {2,2,2,2,2,2,2,2,2,2,2,5,0,2},
     {16644,17170,16644,17170}, {14928,14797,14928,14797}},
    {"cycle43", {1,2,3,0,5,6,4}, {3,5,4,2,1,0,6},
     {5,5,2,0,0,5,2,0,0,5,5,0,3,3},
     {22264,88712,22264,88712}, {20804,80614,20804,80614}},
    {"cycle322", {1,2,0,4,3,6,5}, {4,6,5,3,1,2,0},
     {5,0,3,1,0,5,0,5,5,0,4,3,5,0},
     {142224,90128,142224,90128}, {125184,79756,125184,79756}}
}};

std::array<std::array<int, 2>, 14> centre_selector(const CaseData& data) {
    std::array<std::array<int, 2>, 14> selector{};
    std::array<int, 14> column_degree{};

    for (int scalar_row = 0; scalar_row < 14; ++scalar_row) {
        const int outer_row = scalar_row / 7;
        const int fine_row = scalar_row % 7;
        const int cycle_label = outer_row ? data.centre_p[fine_row] : fine_row;
        std::array<int, 4> adjacency{};
        int next = 0;
        for (int outer_column = 0; outer_column < 2; ++outer_column) {
            for (int layer = 0; layer < 2; ++layer) {
                adjacency[next++] = 7 * outer_column
                    + (layer ? data.h[cycle_label] : cycle_label);
            }
        }

        const int abstract_row = 7 * outer_row + cycle_label;
        for (int index = 0; index < 2; ++index) {
            const int column = adjacency[
                PAIRS[data.centre_options[scalar_row]][index]
            ];
            selector[abstract_row][index] = column;
            ++column_degree[column];
        }
    }

    for (int degree : column_degree) assert(degree == 2);
    return selector;
}

std::vector<std::array<int, 7>> all_permutations() {
    std::array<int, 7> permutation{};
    std::iota(permutation.begin(), permutation.end(), 0);
    std::vector<std::array<int, 7>> result;
    do {
        result.push_back(permutation);
    } while (std::next_permutation(permutation.begin(), permutation.end()));
    assert(result.size() == 5040);
    return result;
}

Point scalar_point(
    bool top,
    int cycle_label,
    int abstract_column,
    const std::array<int, 7>& a0,
    const std::array<int, 7>& a1,
    const std::array<int, 7>& bottom_order,
    int orientation
) {
    const int row_position = top ? cycle_label : bottom_order[cycle_label];
    const int x = orientation < 2
        ? (top ? row_position : 7 + row_position)
        : 2 * row_position + (top ? 0 : 1);

    const int outer_column = abstract_column / 7;
    const int fine_column = abstract_column % 7;
    const int column_position = outer_column ? a1[fine_column] : a0[fine_column];
    const int y = orientation % 2 == 0
        ? 7 * outer_column + column_position
        : 2 * column_position + outer_column;
    return {x, y};
}

bool no_three(const std::array<Point, 14>& points) {
    for (int first = 0; first < 14; ++first) {
        for (int second = first + 1; second < 14; ++second) {
            for (int third = second + 1; third < 14; ++third) {
                if (determinant(points[first], points[second], points[third]) == 0) {
                    return false;
                }
            }
        }
    }
    return true;
}

struct BottomSearch {
    const std::array<std::array<int, 2>, 14>* selector = nullptr;
    const std::array<int, 7>* a0 = nullptr;
    const std::array<int, 7>* a1 = nullptr;
    int orientation = 0;
    std::array<int, 7> bottom_order{};
    int used_positions = 0;
    std::vector<Point> selected;

    bool search(int cycle_label) {
        if (cycle_label == 7) return true;

        for (int position = 0; position < 7; ++position) {
            if (used_positions >> position & 1) continue;
            bottom_order[cycle_label] = position;
            const Point left = scalar_point(
                false, cycle_label, (*selector)[7 + cycle_label][0],
                *a0, *a1, bottom_order, orientation
            );
            const Point right = scalar_point(
                false, cycle_label, (*selector)[7 + cycle_label][1],
                *a0, *a1, bottom_order, orientation
            );

            bool bad = false;
            for (int first = 0; first < static_cast<int>(selected.size()) && !bad; ++first) {
                for (int second = first + 1;
                     second < static_cast<int>(selected.size()); ++second) {
                    if (determinant(selected[first], selected[second], left) == 0
                        || determinant(selected[first], selected[second], right) == 0) {
                        bad = true;
                        break;
                    }
                }
            }
            for (const Point& point : selected) {
                if (!bad && determinant(point, left, right) == 0) bad = true;
            }
            if (bad) continue;

            used_positions |= 1 << position;
            selected.push_back(left);
            selected.push_back(right);
            if (search(cycle_label + 1)) return true;
            selected.pop_back();
            selected.pop_back();
            used_positions &= ~(1 << position);
        }
        return false;
    }

    bool solve(
        const std::array<std::array<int, 2>, 14>& requested_selector,
        const std::array<int, 7>& requested_a0,
        const std::array<int, 7>& requested_a1,
        int requested_orientation
    ) {
        selector = &requested_selector;
        a0 = &requested_a0;
        a1 = &requested_a1;
        orientation = requested_orientation;
        used_positions = 0;
        selected.clear();
        return search(0);
    }
};

void verify_case(const CaseData& data) {
    const auto selector = centre_selector(data);
    const auto permutations = all_permutations();
    std::array<int, 7> unused_bottom_order{};
    BottomSearch bottom_search;

    for (int orientation = 0; orientation < 4; ++orientation) {
        long long top_clean = 0;
        long long half_compatible = 0;

        for (const auto& a0 : permutations) {
            for (const auto& a1 : permutations) {
                std::array<Point, 14> top_points{};
                int next = 0;
                for (int cycle_label = 0; cycle_label < 7; ++cycle_label) {
                    for (int index = 0; index < 2; ++index) {
                        top_points[next++] = scalar_point(
                            true, cycle_label, selector[cycle_label][index],
                            a0, a1, unused_bottom_order, orientation
                        );
                    }
                }
                if (!no_three(top_points)) continue;
                ++top_clean;
                if (bottom_search.solve(selector, a0, a1, orientation)) {
                    ++half_compatible;
                }
            }
        }

        assert(top_clean == data.top_clean[orientation]);
        assert(half_compatible == data.half_compatible[orientation]);
        std::cout << data.name << " orientation=" << orientation
                  << " top_clean=" << top_clean
                  << " half_compatible=" << half_compatible << "\n";
    }
    std::cout << data.name << ": PASS\n";
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

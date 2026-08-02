// Exact CSP checks for PX504--PX507 selector-coordinate orbits.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <string>

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
    std::array<long long, 4> expected_nodes;
};

const std::array<CaseData, 4> CASES = {{
    {"cycle7", {1,2,3,4,5,6,0}, {5,4,0,6,2,1,3},
     {0,3,0,3,5,2,2,2,2,3,0,5,5,2},
     {95187,128576,84090,118771}},
    {"cycle52", {1,2,3,4,0,6,5}, {4,5,6,1,3,2,0},
     {2,2,2,2,2,2,2,2,2,2,2,5,0,2},
     {123744,126196,124181,127384}},
    {"cycle43", {1,2,3,0,5,6,4}, {3,5,4,2,1,0,6},
     {5,5,2,0,0,5,2,0,0,5,5,0,3,3},
     {136854,311894,124166,264514}},
    {"cycle322", {1,2,0,4,3,6,5}, {4,6,5,3,1,2,0},
     {5,0,3,1,0,5,0,5,5,0,4,3,5,0},
     {93186,91698,124604,152878}}
}};

struct AbstractPoint {
    bool top;
    int cycle_label;
    int abstract_column;
};

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

    for (int row = 0; row < 14; ++row) {
        assert(selector[row][0] != selector[row][1]);
    }
    for (int degree : column_degree) assert(degree == 2);
    return selector;
}

struct CoordinateCSP {
    std::array<AbstractPoint, 28> points{};
    std::array<int, 21> assignment{};
    std::array<int, 21> answer{};
    std::array<int, 3> used_values{};
    int orientation = 0;
    long long nodes = 0;

    int group(int variable) const {
        return variable < 7 ? 0 : variable < 14 ? 1 : 2;
    }

    bool complete(const AbstractPoint& point) const {
        return assignment[point.abstract_column] >= 0
            && (point.top || assignment[14 + point.cycle_label] >= 0);
    }

    Point scalar_point(const AbstractPoint& point) const {
        const int row_position = point.top
            ? point.cycle_label
            : assignment[14 + point.cycle_label];
        const int x = orientation < 2
            ? (point.top ? row_position : 7 + row_position)
            : 2 * row_position + (point.top ? 0 : 1);

        const int outer_column = point.abstract_column / 7;
        const int column_position = assignment[point.abstract_column];
        const int y = orientation % 2 == 0
            ? 7 * outer_column + column_position
            : 2 * column_position + outer_column;
        return {x, y};
    }

    bool valid_partial_assignment() const {
        std::array<int, 28> complete_points{};
        int count = 0;
        for (int index = 0; index < 28; ++index) {
            if (complete(points[index])) complete_points[count++] = index;
        }

        for (int first = 0; first < count; ++first) {
            for (int second = first + 1; second < count; ++second) {
                for (int third = second + 1; third < count; ++third) {
                    if (determinant(
                        scalar_point(points[complete_points[first]]),
                        scalar_point(points[complete_points[second]]),
                        scalar_point(points[complete_points[third]])
                    ) == 0) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    bool allowed(int variable, int value) {
        if (used_values[group(variable)] >> value & 1) return false;
        assignment[variable] = value;
        const bool result = valid_partial_assignment();
        assignment[variable] = -1;
        return result;
    }

    bool search(int depth) {
        ++nodes;
        if (depth == 21) {
            answer = assignment;
            return true;
        }

        int branch_variable = -1;
        int best_count = 8;
        std::array<int, 7> branch_domain{};
        int branch_count = 0;

        for (int variable = 0; variable < 21; ++variable) {
            if (assignment[variable] >= 0) continue;
            std::array<int, 7> domain{};
            int count = 0;
            for (int value = 0; value < 7; ++value) {
                if (allowed(variable, value)) domain[count++] = value;
            }
            if (count == 0) return false;
            if (count < best_count) {
                best_count = count;
                branch_variable = variable;
                branch_count = count;
                branch_domain = domain;
                if (count == 1) break;
            }
        }

        for (int index = 0; index < branch_count; ++index) {
            const int value = branch_domain[index];
            assignment[branch_variable] = value;
            used_values[group(branch_variable)] |= 1 << value;
            if (search(depth + 1)) return true;
            used_values[group(branch_variable)] &= ~(1 << value);
            assignment[branch_variable] = -1;
        }
        return false;
    }

    bool solve(
        const std::array<std::array<int, 2>, 14>& selector,
        int requested_orientation
    ) {
        orientation = requested_orientation;
        assignment.fill(-1);
        used_values.fill(0);
        nodes = 0;

        int next = 0;
        for (int row = 0; row < 14; ++row) {
            for (int index = 0; index < 2; ++index) {
                points[next++] = {
                    row < 7,
                    row % 7,
                    selector[row][index]
                };
            }
        }
        return search(0);
    }
};

void verify_case(const CaseData& data) {
    const auto selector = centre_selector(data);
    CoordinateCSP solver;
    long long total_nodes = 0;
    for (int orientation = 0; orientation < 4; ++orientation) {
        assert(!solver.solve(selector, orientation));
        assert(solver.nodes == data.expected_nodes[orientation]);
        total_nodes += solver.nodes;
    }
    std::cout << data.name << ": coordinate CSP nodes="
              << total_nodes << " PASS\n";
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

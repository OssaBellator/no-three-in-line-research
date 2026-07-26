// Exact radius-two support-eight/ten coordinate census for PX523--PX528.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>

constexpr int PAIRS[6][2] = {
    {0,1}, {0,2}, {0,3}, {1,2}, {1,3}, {2,3}
};

using Selector = std::array<std::uint16_t, 14>;

struct SelectorHash {
    std::size_t operator()(const Selector& selector) const noexcept {
        std::uint64_t hash = 1469598103934665603ULL;
        for (std::uint16_t row : selector) {
            hash ^= row;
            hash *= 1099511628211ULL;
        }
        return hash;
    }
};

struct CaseData {
    std::string name;
    std::array<int, 7> h;
    std::array<int, 7> p;
    std::array<int, 14> options;
    int radius_one_count;
    int support_eight_count;
    std::vector<std::uint64_t> support_eight_nodes;
    int support_ten_count;
    std::vector<std::uint64_t> support_ten_nodes;
};

const std::array<CaseData, 4> CASES = {{
    {
        "cycle7",
        {1,2,3,4,5,6,0},
        {5,4,0,6,2,1,3},
        {0,3,0,3,5,2,2,2,2,3,0,5,5,2},
        1092,
        435,
        {19127017ULL,33614524ULL,67538237ULL,57041978ULL,64458064ULL,53624461ULL},
        400,
        {20597821ULL,23018169ULL,40816672ULL,46936004ULL,39311932ULL,61086054ULL}
    },
    {
        "cycle52",
        {1,2,3,4,0,6,5},
        {4,5,6,1,3,2,0},
        {2,2,2,2,2,2,2,2,2,2,2,5,0,2},
        364,
        533,
        {40030400ULL,57345887ULL,33981701ULL,44048868ULL,101572181ULL,69065925ULL},
        232,
        {27076183ULL,30286767ULL,58018025ULL,56658274ULL}
    },
    {
        "cycle43",
        {1,2,3,0,5,6,4},
        {3,5,4,2,1,0,6},
        {5,5,2,0,0,5,2,0,0,5,5,0,3,3},
        180,
        543,
        {42585761ULL,66347848ULL,76897952ULL,66169226ULL,103476284ULL,163009711ULL},
        328,
        {47475742ULL,35822742ULL,54770126ULL,76897799ULL,96188731ULL}
    },
    {
        "cycle322",
        {1,2,0,4,3,6,5},
        {4,6,5,3,1,2,0},
        {5,0,3,1,0,5,0,5,5,0,4,3,5,0},
        112,
        725,
        {26235664ULL,41988721ULL,22337561ULL,30670276ULL,78907092ULL,68401164ULL,110299561ULL,55229265ULL},
        904,
        {30876314ULL,41722256ULL,36689106ULL,58922044ULL,73943616ULL,69983797ULL,91619703ULL,79460595ULL,70781994ULL,57790370ULL}
    }
}};

Selector centre_selector(const CaseData& data) {
    Selector selector{};
    for (int scalar_row = 0; scalar_row < 14; ++scalar_row) {
        const int outer_row = scalar_row / 7;
        const int fine_row = scalar_row % 7;
        const int cycle_label = outer_row ? data.p[fine_row] : fine_row;
        const int adjacency[4] = {
            cycle_label,
            data.h[cycle_label],
            7 + cycle_label,
            7 + data.h[cycle_label]
        };
        const int abstract_row = 7 * outer_row + cycle_label;
        for (int index = 0; index < 2; ++index) {
            selector[abstract_row] |=
                1u << adjacency[PAIRS[data.options[scalar_row]][index]];
        }
    }
    return selector;
}

std::array<std::uint16_t, 14> abstract_host(const CaseData& data) {
    std::array<std::uint16_t, 14> host{};
    for (int outer_row = 0; outer_row < 2; ++outer_row) {
        for (int label = 0; label < 7; ++label) {
            host[7 * outer_row + label] =
                (1u << label)
                | (1u << data.h[label])
                | (1u << (7 + label))
                | (1u << (7 + data.h[label]));
        }
    }
    return host;
}

struct CycleEnumerator {
    Selector selector{};
    std::array<std::uint16_t, 14> host{};
    std::array<std::uint16_t, 14> selected_rows_at_column{};
    std::unordered_set<Selector, SelectorHash> neighbours;
    std::vector<int> rows;
    std::vector<int> columns;
    int start_row = 0;

    void search(int row, std::uint16_t used_rows, std::uint16_t used_columns) {
        std::uint16_t unselected = host[row] & ~selector[row];
        while (unselected) {
            const int column = __builtin_ctz(unselected);
            unselected &= unselected - 1;
            if (used_columns >> column & 1u) continue;

            std::uint16_t next_rows = selected_rows_at_column[column];
            while (next_rows) {
                const int next_row = __builtin_ctz(next_rows);
                next_rows &= next_rows - 1;
                if (next_row == start_row) {
                    if (rows.size() < 2) continue;
                    Selector flipped = selector;
                    for (std::size_t index = 0; index < columns.size(); ++index) {
                        const int old_column = columns[index];
                        flipped[rows[index]] ^= 1u << old_column;
                        flipped[rows[index + 1]] ^= 1u << old_column;
                    }
                    flipped[rows.back()] ^= 1u << column;
                    flipped[start_row] ^= 1u << column;
                    neighbours.insert(flipped);
                } else if (
                    !(used_rows >> next_row & 1u)
                    && next_row >= start_row
                ) {
                    rows.push_back(next_row);
                    columns.push_back(column);
                    search(
                        next_row,
                        used_rows | (1u << next_row),
                        used_columns | (1u << column)
                    );
                    columns.pop_back();
                    rows.pop_back();
                }
            }
        }
    }

    void run() {
        selected_rows_at_column.fill(0);
        neighbours.clear();
        for (int column = 0; column < 14; ++column) {
            for (int row = 0; row < 14; ++row) {
                if (selector[row] >> column & 1u) {
                    selected_rows_at_column[column] |= 1u << row;
                }
            }
        }
        for (start_row = 0; start_row < 14; ++start_row) {
            rows = {start_row};
            columns.clear();
            search(start_row, 1u << start_row, 0);
        }
    }
};

struct Point {
    int x;
    int y;
};

inline int determinant(const Point& a, const Point& b, const Point& c) {
    return (b.x - a.x) * (c.y - a.y)
        - (b.y - a.y) * (c.x - a.x);
}

struct AbstractPoint {
    bool top;
    std::uint8_t label;
    std::uint8_t column;
};

struct CoordinateCSP {
    struct Mask {
        std::uint64_t words[4]{};
        void add(const Mask& other) {
            for (int index = 0; index < 4; ++index) words[index] |= other.words[index];
        }
        bool contains(int point_id) const {
            return (words[point_id >> 6] >> (point_id & 63)) & 1ULL;
        }
    };

    static std::array<std::array<Mask, 196>, 196> line_masks;
    static bool line_masks_ready;

    std::array<AbstractPoint, 28> points{};
    std::array<std::int8_t, 21> assignment{};
    std::array<std::uint8_t, 3> used_values{};
    std::array<std::array<std::uint8_t, 2>, 21> touching{};
    std::array<std::uint8_t, 21> touching_count{};
    std::array<std::uint8_t, 28> complete{};
    std::array<std::uint8_t, 28> complete_points{};
    std::array<std::uint8_t, 28> point_ids{};
    int complete_count = 0;
    int orientation = 0;
    std::uint64_t nodes = 0;

    static void initialise_line_masks() {
        if (line_masks_ready) return;
        for (int first = 0; first < 196; ++first) {
            const Point a{first / 14, first % 14};
            for (int second = 0; second < 196; ++second) {
                if (first == second) continue;
                const Point b{second / 14, second % 14};
                for (int third = 0; third < 196; ++third) {
                    const Point c{third / 14, third % 14};
                    if (determinant(a, b, c) == 0) {
                        line_masks[first][second].words[third >> 6]
                            |= 1ULL << (third & 63);
                    }
                }
            }
        }
        line_masks_ready = true;
    }

    int group(int variable) const {
        return variable < 7 ? 0 : variable < 14 ? 1 : 2;
    }

    bool is_complete(int point_index) const {
        const AbstractPoint& point = points[point_index];
        return assignment[point.column] >= 0
            && (point.top || assignment[14 + point.label] >= 0);
    }

    int scalar_point_id(int point_index) const {
        const AbstractPoint& point = points[point_index];
        const int row_position = point.top
            ? point.label
            : assignment[14 + point.label];
        const int x = orientation < 2
            ? (point.top ? row_position : 7 + row_position)
            : 2 * row_position + (point.top ? 0 : 1);
        const int outer_column = point.column / 7;
        const int column_position = assignment[point.column];
        const int y = orientation % 2 == 0
            ? 7 * outer_column + column_position
            : 2 * column_position + outer_column;
        return 14 * x + y;
    }

    int newly_completed(int variable, std::array<std::uint8_t, 2>& result) const {
        int count = 0;
        for (int index = 0; index < touching_count[variable]; ++index) {
            const int point = touching[variable][index];
            if (!complete[point] && is_complete(point)) result[count++] = point;
        }
        return count;
    }

    bool candidate_is_valid(
        const Mask& dangerous,
        const std::array<std::uint8_t, 2>& newly,
        int new_count,
        std::array<std::uint8_t, 2>& new_ids
    ) const {
        if (new_count == 0) return true;
        new_ids[0] = scalar_point_id(newly[0]);
        if (dangerous.contains(new_ids[0])) return false;
        if (new_count == 2) {
            new_ids[1] = scalar_point_id(newly[1]);
            if (dangerous.contains(new_ids[1])) return false;
            for (int index = 0; index < complete_count; ++index) {
                const int old_id = point_ids[complete_points[index]];
                if (line_masks[new_ids[0]][old_id].contains(new_ids[1])) return false;
            }
        }
        return true;
    }

    bool allowed(int variable, int value, const Mask& dangerous) {
        const int variable_group = group(variable);
        if (used_values[variable_group] >> value & 1u) return false;
        assignment[variable] = value;
        std::array<std::uint8_t, 2> newly{};
        std::array<std::uint8_t, 2> new_ids{};
        const int count = newly_completed(variable, newly);
        const bool valid = candidate_is_valid(dangerous, newly, count, new_ids);
        assignment[variable] = -1;
        return valid;
    }

    bool search(int depth, const Mask& dangerous) {
        ++nodes;
        if (depth == 21) return true;

        int branch_variable = -1;
        int best_count = 8;
        std::array<std::int8_t, 7> branch_domain{};
        int branch_count = 0;
        for (int variable = 0; variable < 21; ++variable) {
            if (assignment[variable] >= 0) continue;
            std::array<std::int8_t, 7> domain{};
            int count = 0;
            for (int value = 0; value < 7; ++value) {
                if (allowed(variable, value, dangerous)) domain[count++] = value;
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

        const int variable_group = group(branch_variable);
        for (int index = 0; index < branch_count; ++index) {
            const int value = branch_domain[index];
            assignment[branch_variable] = value;
            used_values[variable_group] |= 1u << value;

            std::array<std::uint8_t, 2> newly{};
            std::array<std::uint8_t, 2> new_ids{};
            const int new_count = newly_completed(branch_variable, newly);
            assert(candidate_is_valid(dangerous, newly, new_count, new_ids));

            Mask child_dangerous = dangerous;
            for (int new_index = 0; new_index < new_count; ++new_index) {
                const int point = newly[new_index];
                const int point_id = new_ids[new_index];
                for (int old_index = 0; old_index < complete_count; ++old_index) {
                    child_dangerous.add(line_masks[point_id][
                        point_ids[complete_points[old_index]]
                    ]);
                }
                for (int earlier = 0; earlier < new_index; ++earlier) {
                    child_dangerous.add(line_masks[point_id][new_ids[earlier]]);
                }
                complete[point] = 1;
                point_ids[point] = point_id;
                complete_points[complete_count++] = point;
            }

            if (search(depth + 1, child_dangerous)) return true;

            for (int new_index = new_count - 1; new_index >= 0; --new_index) {
                --complete_count;
                complete[newly[new_index]] = 0;
            }
            used_values[variable_group] &= ~(1u << value);
            assignment[branch_variable] = -1;
        }
        return false;
    }

    bool solve(const Selector& selector, int requested_orientation) {
        initialise_line_masks();
        orientation = requested_orientation;
        assignment.fill(-1);
        used_values.fill(0);
        complete.fill(0);
        touching_count.fill(0);
        complete_count = 0;
        nodes = 0;

        int next_point = 0;
        for (int row = 0; row < 14; ++row) {
            std::uint16_t columns = selector[row];
            while (columns) {
                const int column = __builtin_ctz(columns);
                columns &= columns - 1;
                points[next_point] = {
                    row < 7,
                    static_cast<std::uint8_t>(row % 7),
                    static_cast<std::uint8_t>(column)
                };
                touching[column][touching_count[column]++] = next_point;
                if (row >= 7) {
                    const int row_variable = 14 + row % 7;
                    touching[row_variable][touching_count[row_variable]++] = next_point;
                }
                ++next_point;
            }
        }
        assert(next_point == 28);
        Mask empty{};
        return search(0, empty);
    }
};

std::array<std::array<CoordinateCSP::Mask, 196>, 196>
    CoordinateCSP::line_masks{};
bool CoordinateCSP::line_masks_ready = false;

int main(int argc, char** argv) {
    assert(argc == 4);
    const std::string requested = argv[1];
    const int support = std::stoi(argv[2]);
    const int shard = std::stoi(argv[3]);

    for (const CaseData& data : CASES) {
        if (requested != data.name) continue;
        const int expected_count = support == 8
            ? data.support_eight_count
            : support == 10
                ? data.support_ten_count
                : -1;
        const std::vector<std::uint64_t>& expected_nodes = support == 8
            ? data.support_eight_nodes
            : data.support_ten_nodes;
        assert(expected_count >= 0);
        assert(shard >= 0 && shard < static_cast<int>(expected_nodes.size()));

        const Selector centre = centre_selector(data);
        CycleEnumerator enumerator;
        enumerator.selector = centre;
        enumerator.host = abstract_host(data);
        enumerator.run();
        assert(static_cast<int>(enumerator.neighbours.size()) == data.radius_one_count);
        const std::unordered_set<Selector, SelectorHash> radius_one =
            enumerator.neighbours;

        std::set<Selector> layer;
        for (const Selector& parent : radius_one) {
            enumerator.selector = parent;
            enumerator.run();
            for (const Selector& child : enumerator.neighbours) {
                if (child == centre || radius_one.count(child)) continue;
                int difference = 0;
                for (int row = 0; row < 14; ++row) {
                    difference += __builtin_popcount(child[row] ^ centre[row]);
                }
                if (difference == support) layer.insert(child);
            }
        }
        assert(static_cast<int>(layer.size()) == expected_count);

        const int shard_count = expected_nodes.size();
        const int shard_size = (expected_count + shard_count - 1) / shard_count;
        const int first = shard * shard_size + 1;
        const int last = std::min(expected_count, first + shard_size - 1);

        std::uint64_t nodes = 0;
        int index = 0;
        int tested = 0;
        for (const Selector& selector : layer) {
            ++index;
            if (index < first || index > last) continue;
            ++tested;
            for (int orientation = 0; orientation < 4; ++orientation) {
                CoordinateCSP solver;
                const bool feasible = solver.solve(selector, orientation);
                assert(!feasible);
                nodes += solver.nodes;
            }
        }

        assert(tested == std::max(0, last - first + 1));
        assert(nodes == expected_nodes[shard]);
        std::cout
            << data.name
            << " support=" << support
            << " shard=" << shard << "/" << shard_count
            << " selectors=" << tested
            << " nodes=" << nodes
            << " PASS\n";
        return 0;
    }
    assert(false && "unknown side-seven class");
}

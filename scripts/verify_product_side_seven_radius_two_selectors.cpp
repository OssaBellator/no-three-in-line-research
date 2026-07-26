// Exact breadth-first selector census for PX519--PX522.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <unordered_set>
#include <vector>

constexpr int PAIRS[6][2] = {
    {0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}
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
    int expected_radius_one;
    int expected_radius_two;
    std::uint64_t expected_directed_moves;
    std::map<int, std::size_t> expected_histogram;
};

const std::array<CaseData, 4> CASES = {{
    {
        "cycle7",
        {1, 2, 3, 4, 5, 6, 0},
        {5, 4, 0, 6, 2, 1, 3},
        {0, 3, 0, 3, 5, 2, 2, 2, 2, 3, 0, 5, 5, 2},
        1092,
        947789,
        45106960ULL,
        {
            {8, 435}, {10, 400}, {12, 3606}, {14, 4424},
            {16, 18878}, {18, 25096}, {20, 66010}, {22, 82016},
            {24, 142965}, {26, 142576}, {28, 167190}, {30, 120256},
            {32, 94053}, {34, 45536}, {36, 24068}, {38, 7248},
            {40, 2552}, {42, 384}, {44, 96}
        }
    },
    {
        "cycle52",
        {1, 2, 3, 4, 0, 6, 5},
        {4, 5, 6, 1, 3, 2, 0},
        {2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 0, 2},
        364,
        26550,
        296416ULL,
        {
            {8, 533}, {10, 232}, {12, 1584}, {14, 1768},
            {16, 5315}, {18, 3704}, {20, 6762}, {22, 3544},
            {24, 1930}, {26, 776}, {28, 288}, {30, 56},
            {32, 45}, {34, 8}, {36, 4}, {40, 1}
        }
    },
    {
        "cycle43",
        {1, 2, 3, 0, 5, 6, 4},
        {3, 5, 4, 2, 1, 0, 6},
        {5, 5, 2, 0, 0, 5, 2, 0, 0, 5, 5, 0, 3, 3},
        180,
        10531,
        59644ULL,
        {
            {8, 543}, {10, 328}, {12, 1004}, {14, 2132},
            {16, 2013}, {18, 1168}, {20, 2072}, {22, 1232},
            {24, 39}
        }
    },
    {
        "cycle322",
        {1, 2, 0, 4, 3, 6, 5},
        {4, 6, 5, 3, 1, 2, 0},
        {5, 0, 3, 1, 0, 5, 0, 5, 5, 0, 4, 3, 5, 0},
        112,
        4433,
        14848ULL,
        {
            {8, 725}, {10, 904}, {12, 1202}, {14, 988},
            {16, 478}, {18, 132}, {20, 4}
        }
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

    void search(
        int row,
        std::uint16_t used_rows,
        std::uint16_t used_columns
    ) {
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

void verify_case(const CaseData& data) {
    const Selector centre = centre_selector(data);
    CycleEnumerator enumerator;
    enumerator.selector = centre;
    enumerator.host = abstract_host(data);
    enumerator.run();
    assert(
        static_cast<int>(enumerator.neighbours.size())
        == data.expected_radius_one
    );

    const std::unordered_set<Selector, SelectorHash> radius_one =
        enumerator.neighbours;
    std::unordered_set<Selector, SelectorHash> radius_two;
    std::uint64_t directed_moves = 0;

    for (const Selector& parent : radius_one) {
        enumerator.selector = parent;
        enumerator.run();
        directed_moves += enumerator.neighbours.size();
        for (const Selector& child : enumerator.neighbours) {
            if (child == centre || radius_one.count(child)) continue;
            radius_two.insert(child);
        }
    }

    assert(directed_moves == data.expected_directed_moves);
    assert(static_cast<int>(radius_two.size()) == data.expected_radius_two);

    std::map<int, std::size_t> histogram;
    for (const Selector& selector : radius_two) {
        int difference = 0;
        for (int row = 0; row < 14; ++row) {
            difference += __builtin_popcount(selector[row] ^ centre[row]);
        }
        ++histogram[difference];
    }
    assert(histogram == data.expected_histogram);

    std::cout
        << data.name
        << ": radius1=" << radius_one.size()
        << " radius2=" << radius_two.size()
        << " directed=" << directed_moves
        << " support8=" << histogram.at(8)
        << " PASS\n";
}

int main(int argc, char** argv) {
    assert(argc == 2);
    const std::string requested = argv[1];
    for (const CaseData& data : CASES) {
        if (requested == data.name) {
            verify_case(data);
            return 0;
        }
    }
    assert(false && "unknown side-seven class");
}

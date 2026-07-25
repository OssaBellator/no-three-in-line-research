// Exact checks for PX512--PX514 selector connectivity data.
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>

constexpr int PAIRS[6][2] = {
    {0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}
};

struct CaseData {
    std::string name;
    std::array<int, 7> h;
    std::array<int, 7> centre_p;
    std::array<int, 14> centre_options;
    std::map<int, int> expected_histogram;
};

const std::array<CaseData, 4> CASES = {{
    {"cycle7", {1,2,3,4,5,6,0}, {5,4,0,6,2,1,3},
     {0,3,0,3,5,2,2,2,2,3,0,5,5,2},
     {{4,32},{6,16},{8,12},{10,16},{12,8},{14,16},
      {16,128},{18,352},{20,384},{22,128}}},
    {"cycle52", {1,2,3,4,0,6,5}, {4,5,6,1,3,2,0},
     {2,2,2,2,2,2,2,2,2,2,2,5,0,2},
     {{4,36},{6,8},{8,32},{10,48},{12,96},{14,32},
      {16,32},{18,64},{20,16}}},
    {"cycle43", {1,2,3,0,5,6,4}, {3,5,4,2,1,0,6},
     {5,5,2,0,0,5,2,0,0,5,5,0,3,3},
     {{4,36},{6,12},{8,16},{10,84},{12,32}}},
    {"cycle322", {1,2,0,4,3,6,5}, {4,6,5,3,1,2,0},
     {5,0,3,1,0,5,0,5,5,0,4,3,5,0},
     {{4,42},{6,28},{8,30},{10,12}}}
}};

using Selector = std::array<unsigned, 14>;

Selector centre_selector(const CaseData& data) {
    Selector selector{};
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
            selector[abstract_row] |= 1u << column;
            ++column_degree[column];
        }
    }

    for (int row = 0; row < 14; ++row) {
        assert(__builtin_popcount(selector[row]) == 2);
    }
    for (int degree : column_degree) assert(degree == 2);
    return selector;
}

std::array<unsigned, 14> abstract_host(const CaseData& data) {
    std::array<unsigned, 14> host{};
    for (int outer_row = 0; outer_row < 2; ++outer_row) {
        for (int cycle_label = 0; cycle_label < 7; ++cycle_label) {
            const int row = 7 * outer_row + cycle_label;
            for (int outer_column = 0; outer_column < 2; ++outer_column) {
                host[row] |= 1u << (7 * outer_column + cycle_label);
                host[row] |= 1u << (7 * outer_column + data.h[cycle_label]);
            }
            assert(__builtin_popcount(host[row]) == 4);
        }
    }
    return host;
}

struct CycleEnumerator {
    Selector selector{};
    std::array<unsigned, 14> host{};
    std::array<unsigned, 14> selected_rows_at_column{};
    std::set<Selector> neighbours;
    std::vector<int> rows;
    std::vector<int> columns;
    int start_row = 0;

    void search(int row, unsigned used_rows, unsigned used_columns) {
        unsigned unselected = host[row] & ~selector[row];
        while (unselected) {
            const int column = __builtin_ctz(unselected);
            unselected &= unselected - 1;
            if (used_columns >> column & 1u) continue;

            unsigned next_rows = selected_rows_at_column[column];
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
                } else if (!(used_rows >> next_row & 1u) && next_row >= start_row) {
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

long long one_cycle_count(int length) {
    long long b_previous_previous = 2;
    long long b_previous = 8;
    long long b = length == 0 ? b_previous_previous : b_previous;
    for (int index = 2; index <= length; ++index) {
        b = 8 * b_previous - 4 * b_previous_previous;
        b_previous_previous = b_previous;
        b_previous = b;
    }

    long long power_four = 1;
    for (int index = 0; index < length; ++index) power_four *= 4;
    return 2 + 2 * power_four + b;
}

void check_selector_counts() {
    assert(one_cycle_count(2) == 90);
    assert(one_cycle_count(3) == 546);
    assert(one_cycle_count(4) == 3618);
    assert(one_cycle_count(5) == 25218);
    assert(one_cycle_count(7) == 1323522);

    const long long cycle7 = one_cycle_count(7);
    const long long cycle52 = one_cycle_count(5) * one_cycle_count(2);
    const long long cycle43 = one_cycle_count(4) * one_cycle_count(3);
    const long long cycle322 = one_cycle_count(3)
        * one_cycle_count(2) * one_cycle_count(2);

    assert(cycle7 == 1323522);
    assert(cycle52 == 2269620);
    assert(cycle43 == 1975428);
    assert(cycle322 == 4422600);
    assert(cycle7 + cycle52 + cycle43 + cycle322 == 9991170);
}

void verify_case(const CaseData& data) {
    CycleEnumerator enumerator;
    enumerator.selector = centre_selector(data);
    enumerator.host = abstract_host(data);
    enumerator.run();

    std::map<int, int> histogram;
    for (const Selector& neighbour : enumerator.neighbours) {
        std::array<int, 14> column_degree{};
        int symmetric_difference = 0;
        for (int row = 0; row < 14; ++row) {
            assert(__builtin_popcount(neighbour[row]) == 2);
            symmetric_difference += __builtin_popcount(
                neighbour[row] ^ enumerator.selector[row]
            );
            for (int column = 0; column < 14; ++column) {
                if (neighbour[row] >> column & 1u) ++column_degree[column];
            }
        }
        for (int degree : column_degree) assert(degree == 2);
        ++histogram[symmetric_difference];
    }

    assert(histogram == data.expected_histogram);
    int total = 0;
    for (const auto [length, count] : histogram) total += count;
    assert(total == static_cast<int>(enumerator.neighbours.size()));
    std::cout << data.name << ": neighbours=" << total << " PASS\n";
}

int main() {
    check_selector_counts();
    int total_neighbours = 0;
    for (const CaseData& data : CASES) {
        verify_case(data);
        for (const auto [length, count] : data.expected_histogram) {
            (void) length;
            total_neighbours += count;
        }
    }
    assert(total_neighbours == 1748);
    std::cout << "PX512--PX514 selector cycle-graph verifier: PASS\n";
}

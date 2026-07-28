#include "product_side_seven_cache_engine.hpp"

#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

struct WitnessBottomSolver : BottomGroupSolver {
    uint64_t witness_active = 0;

    bool dfs_witness(int depth, uint64_t active) {
        ++nodes;
        if (depth == N) {
            witness_active = active;
            return active != 0;
        }
        int best_z = -1, best_size = 8, domain_size = 0;
        std::array<int8_t,N> best_domain{};
        std::array<uint64_t,N> best_masks{};
        for (int z = 0; z < N; ++z) if (bottom[z] < 0) {
            int size = 0;
            std::array<int8_t,N> domain{};
            std::array<uint64_t,N> masks{};
            for (int value = 0; value < N; ++value) if (!((used >> value) & 1u)) {
                bottom[z] = int8_t(value);
                uint64_t child = transition(z, active);
                bottom[z] = -1;
                if (child) {
                    domain[size] = int8_t(value);
                    masks[size] = child;
                    ++size;
                }
            }
            if (size == 0) return false;
            if (size < best_size) {
                best_size = size;
                best_z = z;
                domain_size = size;
                best_domain = domain;
                best_masks = masks;
            }
        }
        for (int index = 0; index < domain_size; ++index) {
            int value = best_domain[index];
            bottom[best_z] = int8_t(value);
            used |= uint8_t(1u << value);
            if (dfs_witness(depth + 1, best_masks[index])) return true;
            used &= uint8_t(~(1u << value));
            bottom[best_z] = -1;
        }
        return false;
    }

    bool solve_top_witness(Assignment const& assignment, int orientation) {
        prepare_top(assignment, orientation);
        bottom.fill(-1);
        used = 0;
        nodes = 0;
        witness_active = 0;
        return dfs_witness(0, all);
    }
};

static void print_signature(Signature const& signature) {
    for (int row = 0; row < N; ++row) {
        if (row) std::cout << ',';
        std::cout << signature[row];
    }
}

static void print_assignment(Assignment const& assignment) {
    for (int column = 0; column < SIDE; ++column) {
        if (column) std::cout << ',';
        std::cout << int(assignment[column]);
    }
}

static void verify_and_print_witness(
    int requested_case,
    int selector,
    int orientation,
    int top_index,
    uint64_t prefix_bottom_nodes,
    Signature const& signature,
    State const& state,
    Assignment const& top,
    WitnessBottomSolver const& solver
) {
    std::vector<Point> points;
    std::set<std::pair<int,int>> distinct;
    std::array<int,SIDE> row_count{}, column_count{};
    for (int row = 0; row < SIDE; ++row) {
        uint16_t mask = state[row];
        while (mask) {
            int column = __builtin_ctz(unsigned(mask));
            mask &= uint16_t(mask - 1);
            int x;
            if (row < N) x = orientation < 2 ? row : 2 * row;
            else x = orientation < 2
                ? N + solver.bottom[row % N]
                : 2 * solver.bottom[row % N] + 1;
            int y = orientation % 2 == 0
                ? N * (column / N) + top[column]
                : 2 * top[column] + column / N;
            points.push_back({x,y});
            distinct.insert({x,y});
            ++row_count[x];
            ++column_count[y];
        }
    }
    assert(points.size() == 28 && distinct.size() == 28);
    for (int value : row_count) assert(value == 2);
    for (int value : column_count) assert(value == 2);
    for (int first = 0; first < 28; ++first)
        for (int second = first + 1; second < 28; ++second)
            for (int third = second + 1; third < 28; ++third)
                assert(det(points[first], points[second], points[third]) != 0);

    std::cout << "FEASIBLE case=" << requested_case
              << " selector=" << selector
              << " orientation=" << orientation
              << " top_index=" << top_index
              << " prefix_bottom_nodes=" << prefix_bottom_nodes
              << " witness_nodes=" << solver.nodes
              << " signature=";
    print_signature(signature);
    std::cout << " top=";
    print_assignment(top);
    std::cout << " bottom=";
    for (int z = 0; z < N; ++z) {
        if (z) std::cout << ',';
        std::cout << int(solver.bottom[z]);
    }
    std::cout << " state=";
    for (int row = 0; row < SIDE; ++row) {
        if (row) std::cout << ',';
        std::cout << state[row];
    }
    std::cout << " points=";
    for (size_t index = 0; index < points.size(); ++index) {
        if (index) std::cout << ';';
        std::cout << points[index].x << ',' << points[index].y;
    }
    std::cout << " PASS\n";
}

int main(int argc, char** argv) {
    if (argc != 5) {
        std::cerr << "usage: " << argv[0]
                  << " CASE SELECTOR ORIENTATION MULTIPLICITY\n";
        return 64;
    }
    int requested_case = std::stoi(argv[1]);
    int selector = std::stoi(argv[2]);
    int orientation = std::stoi(argv[3]);
    int multiplicity = std::stoi(argv[4]);
    if (requested_case < 0 || selector < 0 || selector >= multiplicity
        || orientation < 0 || orientation >= 4
        || multiplicity <= 0 || multiplicity > 63) return 64;

    auto layer = generate_layer();
    std::map<Signature,std::vector<State>> groups;
    std::map<int,int> histogram;
    for (auto const& state : layer) {
        Signature signature{};
        for (int row = 0; row < N; ++row) signature[row] = state[row];
        groups[signature].push_back(state);
    }
    for (auto const& [signature,group] : groups)
        ++histogram[int(group.size())];
    assert(histogram[multiplicity] > requested_case);

    int case_index = 0;
    for (auto const& [signature,unsorted_group] : groups) {
        if (int(unsorted_group.size()) != multiplicity) continue;
        if (case_index++ != requested_case) continue;
        auto group = unsorted_group;
        std::sort(group.begin(), group.end());
        State const& state = group[selector];

        TopEnumerator top[2];
        for (int mode = 0; mode < 2; ++mode) {
            top[mode].sig = signature;
            top[mode].run(mode);
        }

        WitnessBottomSolver solver;
        solver.initialize(std::vector<State>{state});
        uint64_t bottom_nodes = 0;
        auto const& assignments = top[orientation % 2].solutions;
        for (int top_index = 0; top_index < int(assignments.size()); ++top_index) {
            if (solver.solve_top_witness(assignments[top_index], orientation)) {
                verify_and_print_witness(
                    requested_case, selector, orientation, top_index,
                    bottom_nodes, signature, state, assignments[top_index], solver
                );
                return 0;
            }
            bottom_nodes += solver.nodes;
        }

        std::cout << "INFEASIBLE case=" << requested_case
                  << " selector=" << selector
                  << " orientation=" << orientation
                  << " signature=";
        print_signature(signature);
        std::cout << " top_orders=" << top[0].solutions.size() << ','
                  << top[1].solutions.size()
                  << " top_nodes=" << top[0].nodes << ',' << top[1].nodes
                  << " bottom_nodes=" << bottom_nodes << " PASS\n";
        return 0;
    }
    return 66;
}

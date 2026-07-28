#include "product_side_seven_cache_engine.hpp"

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>

static void print_signature(Signature const& signature) {
    std::cout << '[';
    for (int row = 0; row < N; ++row) {
        if (row) std::cout << ',';
        std::cout << signature[row];
    }
    std::cout << ']';
}

int main(int argc, char** argv) {
    if (argc != 6) {
        std::cerr << "usage: " << argv[0]
                  << " CASE ORIENTATION MULTIPLICITY FIRST_TOP TOP_COUNT\n";
        return 64;
    }

    const int requested_case = std::stoi(argv[1]);
    const int requested_orientation = std::stoi(argv[2]);
    const int multiplicity = std::stoi(argv[3]);
    const size_t first_top = std::stoull(argv[4]);
    const size_t top_count = std::stoull(argv[5]);
    if (requested_case < 0 || requested_orientation < 0
        || requested_orientation >= 4 || multiplicity <= 0
        || multiplicity > 63 || top_count == 0) {
        std::cerr << "invalid parameters\n";
        return 64;
    }

    auto layer = generate_layer();
    std::map<Signature, std::vector<State>> groups;
    std::map<int, int> histogram;
    for (auto const& state : layer) {
        Signature signature{};
        for (int row = 0; row < N; ++row) signature[row] = state[row];
        groups[signature].push_back(state);
    }
    for (auto const& [signature, group] : groups)
        ++histogram[static_cast<int>(group.size())];

    auto hist_it = histogram.find(multiplicity);
    if (hist_it == histogram.end() || requested_case >= hist_it->second) {
        std::cerr << "case outside multiplicity tier\n";
        return 65;
    }

    int case_index = 0;
    for (auto const& [signature, unsorted_group] : groups) {
        if (static_cast<int>(unsorted_group.size()) != multiplicity) continue;
        if (case_index++ != requested_case) continue;

        auto group = unsorted_group;
        std::sort(group.begin(), group.end());

        TopEnumerator top[2];
        for (int mode = 0; mode < 2; ++mode) {
            top[mode].sig = signature;
            top[mode].run(mode);
        }

        auto const& solutions = top[requested_orientation % 2].solutions;
        if (first_top > solutions.size() || top_count > solutions.size() - first_top) {
            std::cerr << "top range exceeds clean-top family\n";
            return 65;
        }

        BottomGroupSolver solver;
        solver.initialize(group);
        uint64_t bottom_nodes = 0;
        const size_t end_top = first_top + top_count;
        for (size_t top_index = first_top; top_index < end_top; ++top_index) {
            if (solver.solve_top(solutions[top_index], requested_orientation)) {
                std::cerr << "FEASIBLE selector at global case "
                          << requested_case << " orientation "
                          << requested_orientation << " top_index "
                          << top_index << "\n";
                return 2;
            }
            bottom_nodes += solver.nodes;
        }

        std::cout << "case=" << requested_case
                  << " orientation=" << requested_orientation
                  << " first_top=" << first_top
                  << " top_count=" << top_count
                  << " clean_top_count=" << solutions.size()
                  << " signature=";
        print_signature(signature);
        std::cout << " top_orders=" << top[0].solutions.size() << ','
                  << top[1].solutions.size() << " top_nodes="
                  << top[0].nodes << ',' << top[1].nodes
                  << " bottom_nodes=" << bottom_nodes
                  << " INFEASIBLE\n";
        return 0;
    }

    std::cerr << "case not found\n";
    return 66;
}

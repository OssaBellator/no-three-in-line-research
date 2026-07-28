#include "product_side_seven_cache_engine.hpp"

#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>

static uint64_t mix(uint64_t hash, uint64_t value) {
    hash ^= value;
    hash *= 1099511628211ULL;
    return hash;
}

int main() {
    constexpr int requested_case = 1287;
    auto layer = generate_layer();
    std::map<Signature,std::vector<State>> groups;
    for (auto const& state : layer) {
        Signature signature{};
        for (int row = 0; row < N; ++row) signature[row] = state[row];
        groups[signature].push_back(state);
    }

    int case_index = 0;
    for (auto const& [signature, unsorted_group] : groups) {
        if (unsorted_group.size() != 2) continue;
        if (case_index++ != requested_case) continue;
        auto group = unsorted_group;
        std::sort(group.begin(), group.end());
        std::vector<State> selector_group{group[1]};

        TopEnumerator top[2];
        for (int mode = 0; mode < 2; ++mode) {
            top[mode].sig = signature;
            top[mode].run(mode);
        }

        BottomGroupSolver solver;
        solver.initialize(selector_group);
        std::array<uint64_t,4> bottom_nodes{};
        for (int orientation = 0; orientation < 4; ++orientation) {
            for (auto const& assignment : top[orientation % 2].solutions) {
                if (solver.solve_top(assignment, orientation)) {
                    std::cerr << "FEASIBLE selector=1 orientation=" << orientation << "\n";
                    return 2;
                }
                bottom_nodes[orientation] += solver.nodes;
            }
        }

        uint64_t digest = 1469598103934665603ULL;
        digest = mix(digest, requested_case);
        for (auto value : signature) digest = mix(digest, value);
        for (int mode = 0; mode < 2; ++mode) {
            digest = mix(digest, top[mode].solutions.size());
            digest = mix(digest, top[mode].nodes);
        }
        for (auto value : bottom_nodes) digest = mix(digest, value);

        std::cout << "case=1287 selector=1 signature=";
        for (int row = 0; row < N; ++row) {
            if (row) std::cout << ',';
            std::cout << signature[row];
        }
        std::cout << " top_orders=" << top[0].solutions.size() << ','
                  << top[1].solutions.size()
                  << " top_nodes=" << top[0].nodes << ',' << top[1].nodes
                  << " bottom_nodes=" << bottom_nodes[0] << ','
                  << bottom_nodes[1] << ',' << bottom_nodes[2] << ','
                  << bottom_nodes[3]
                  << " digest=" << digest << " INFEASIBLE\n";
        return 0;
    }
    return 1;
}

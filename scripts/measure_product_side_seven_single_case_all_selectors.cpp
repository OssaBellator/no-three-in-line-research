#define main single_selector_orientation_main
#include "measure_product_side_seven_single_selector_orientation.cpp"
#undef main

#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: " << argv[0] << " CASE MULTIPLICITY\n";
        return 64;
    }
    int requested_case = std::stoi(argv[1]);
    int multiplicity = std::stoi(argv[2]);
    if (requested_case < 0 || multiplicity <= 0 || multiplicity > 63) return 64;

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

        TopEnumerator top[2];
        for (int mode = 0; mode < 2; ++mode) {
            top[mode].sig = signature;
            top[mode].run(mode);
        }

        uint64_t digest = 1469598103934665603ULL;
        digest = mix(digest, requested_case);
        for (auto value : signature) digest = mix(digest, value);
        for (int mode = 0; mode < 2; ++mode) {
            digest = mix(digest, top[mode].solutions.size());
            digest = mix(digest, top[mode].nodes);
        }

        int constructive_selectors = 0;
        int infeasible_selectors = 0;
        std::array<uint64_t,4> certified_rejection_nodes{};
        for (int selector = 0; selector < multiplicity; ++selector) {
            WitnessBottomSolver solver;
            solver.initialize(std::vector<State>{group[selector]});
            std::array<uint64_t,4> orientation_nodes{};
            bool selector_constructive = false;
            for (int orientation = 0; orientation < 4; ++orientation) {
                auto const& assignments = top[orientation % 2].solutions;
                bool orientation_constructive = false;
                uint64_t bottom_nodes = 0;
                for (int top_index = 0; top_index < int(assignments.size()); ++top_index) {
                    if (solver.solve_top_witness(assignments[top_index], orientation)) {
                        verify_and_print_witness(
                            requested_case, selector, orientation, top_index,
                            bottom_nodes, signature, group[selector],
                            assignments[top_index], solver
                        );
                        digest = mix(digest, selector);
                        digest = mix(digest, orientation);
                        digest = mix(digest, top_index);
                        digest = mix(digest, bottom_nodes);
                        digest = mix(digest, solver.nodes);
                        for (auto value : assignments[top_index])
                            digest = mix(digest, uint8_t(value));
                        for (auto value : solver.bottom)
                            digest = mix(digest, uint8_t(value));
                        orientation_constructive = true;
                        selector_constructive = true;
                        break;
                    }
                    bottom_nodes += solver.nodes;
                }
                if (!orientation_constructive) {
                    orientation_nodes[orientation] = bottom_nodes;
                    std::cout << "INFEASIBLE case=" << requested_case
                              << " selector=" << selector
                              << " orientation=" << orientation
                              << " signature=";
                    print_signature(signature);
                    std::cout << " top_orders=" << top[0].solutions.size() << ','
                              << top[1].solutions.size()
                              << " top_nodes=" << top[0].nodes << ',' << top[1].nodes
                              << " bottom_nodes=" << bottom_nodes << " PASS\n";
                    digest = mix(digest, selector);
                    digest = mix(digest, orientation);
                    digest = mix(digest, bottom_nodes);
                }
            }
            if (selector_constructive) {
                ++constructive_selectors;
            } else {
                ++infeasible_selectors;
                for (int orientation = 0; orientation < 4; ++orientation)
                    certified_rejection_nodes[orientation] += orientation_nodes[orientation];
            }
        }

        uint64_t rejection_total = 0;
        for (auto value : certified_rejection_nodes) {
            rejection_total += value;
            digest = mix(digest, value);
        }
        digest = mix(digest, infeasible_selectors);
        digest = mix(digest, constructive_selectors);
        std::cout << "FINAL case=" << requested_case
                  << " signature=";
        print_signature(signature);
        std::cout << " top_orders=" << top[0].solutions.size() << ','
                  << top[1].solutions.size()
                  << " top_nodes=" << top[0].nodes << ',' << top[1].nodes
                  << " infeasible_selectors=" << infeasible_selectors
                  << " constructive_selectors=" << constructive_selectors
                  << " rejection_nodes=";
        for (int orientation = 0; orientation < 4; ++orientation) {
            if (orientation) std::cout << ',';
            std::cout << certified_rejection_nodes[orientation];
        }
        std::cout << " rejection_total=" << rejection_total
                  << " digest=" << digest << " PASS\n";
        return 0;
    }
    return 66;
}

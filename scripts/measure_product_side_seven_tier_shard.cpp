#include "product_side_seven_tier_shard_digest.hpp"

#include <cstdlib>
#include <iomanip>
#include <sstream>

int main(int argc, char** argv) {
    if (argc < 3 || argc > 4) {
        std::cerr << "usage: " << argv[0]
                  << " FIRST_CASE CASE_COUNT [MULTIPLICITY]\n";
        return 64;
    }

    const int first_case = std::stoi(argv[1]);
    const int case_count = std::stoi(argv[2]);
    const int multiplicity = argc == 4 ? std::stoi(argv[3]) : 3;
    if (first_case < 0 || case_count <= 0 || multiplicity <= 0 || multiplicity > 63) {
        std::cerr << "invalid shard parameters\n";
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
    if (hist_it == histogram.end()) {
        std::cerr << "no signatures at multiplicity " << multiplicity << "\n";
        return 65;
    }
    const int signature_count = hist_it->second;
    if (first_case + case_count > signature_count) {
        std::cerr << "shard exceeds multiplicity tier: first=" << first_case
                  << " count=" << case_count
                  << " tier=" << signature_count << "\n";
        return 65;
    }

    uint64_t digest = 1469598103934665603ULL;
    std::array<uint64_t, 2> aggregate_top_orders{};
    std::array<uint64_t, 2> aggregate_top_nodes{};
    std::array<uint64_t, 4> aggregate_bottom_nodes{};
    int case_index = 0;
    int checked = 0;

    for (auto const& [signature, unsorted_group] : groups) {
        if (static_cast<int>(unsorted_group.size()) != multiplicity) continue;
        const bool selected = case_index >= first_case
            && case_index < first_case + case_count;
        if (selected) {
            auto group = unsorted_group;
            std::sort(group.begin(), group.end());

            TopEnumerator top[2];
            for (int mode = 0; mode < 2; ++mode) {
                top[mode].sig = signature;
                top[mode].run(mode);
            }

            BottomGroupSolver solver;
            solver.initialize(group);
            std::array<uint64_t, 4> bottom_nodes{};
            for (int orientation = 0; orientation < 4; ++orientation) {
                auto const& solutions = top[orientation % 2].solutions;
                for (auto const& assignment : solutions) {
                    if (solver.solve_top(assignment, orientation)) {
                        std::cerr << "FEASIBLE selector at global case " << case_index
                                  << " orientation " << orientation << "\n";
                        return 2;
                    }
                    bottom_nodes[orientation] += solver.nodes;
                }
            }

            digest = tier_shard_digest_mix(digest, case_index);
            for (auto value : signature) digest = tier_shard_digest_mix(digest, value);
            for (int mode = 0; mode < 2; ++mode) {
                digest = tier_shard_digest_mix(digest, top[mode].solutions.size());
                aggregate_top_orders[mode] += top[mode].solutions.size();
            }
            for (int mode = 0; mode < 2; ++mode) {
                digest = tier_shard_digest_mix(digest, top[mode].nodes);
                aggregate_top_nodes[mode] += top[mode].nodes;
            }
            for (int orientation = 0; orientation < 4; ++orientation) {
                digest = tier_shard_digest_mix(digest, bottom_nodes[orientation]);
                aggregate_bottom_nodes[orientation] += bottom_nodes[orientation];
            }

            std::cout << "case=" << case_index << " signature=";
            print_sig(signature);
            std::cout << " top_orders=" << top[0].solutions.size() << ','
                      << top[1].solutions.size()
                      << " top_nodes=" << top[0].nodes << ',' << top[1].nodes
                      << " bottom_nodes=" << bottom_nodes[0] << ','
                      << bottom_nodes[1] << ',' << bottom_nodes[2] << ','
                      << bottom_nodes[3] << " INFEASIBLE\n";
            ++checked;
        }
        ++case_index;
    }

    if (case_index != signature_count || checked != case_count) {
        std::cerr << "internal shard accounting mismatch\n";
        return 70;
    }

    uint64_t total_bottom = 0;
    for (auto value : aggregate_bottom_nodes) total_bottom += value;

    std::cout << "\nconst TierShardDigestExpectations EXPECTED = {\n"
              << "    " << multiplicity << ",\n"
              << "    " << signature_count << ",\n"
              << "    " << first_case << ",\n"
              << "    " << case_count << ",\n"
              << "    {{" << aggregate_top_orders[0] << "ULL,"
              << aggregate_top_orders[1] << "ULL}},\n"
              << "    {{" << aggregate_top_nodes[0] << "ULL,"
              << aggregate_top_nodes[1] << "ULL}},\n"
              << "    {{" << aggregate_bottom_nodes[0] << "ULL,"
              << aggregate_bottom_nodes[1] << "ULL,"
              << aggregate_bottom_nodes[2] << "ULL,"
              << aggregate_bottom_nodes[3] << "ULL}},\n"
              << "    " << digest << "ULL\n"
              << "};\n"
              << "aggregate_bottom_nodes=" << total_bottom << "\n";
    return 0;
}

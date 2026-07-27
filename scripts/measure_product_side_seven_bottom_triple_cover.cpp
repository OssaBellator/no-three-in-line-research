#include "product_side_seven_cache_engine.hpp"

#include <cstdlib>
#include <iomanip>
#include <set>

std::vector<int> cover_edges(State const& state) {
    std::vector<int> edges;
    for (int row = 0; row < SIDE; ++row) {
        uint16_t mask = state[row];
        while (mask) {
            int column = __builtin_ctz(unsigned(mask));
            mask &= uint16_t(mask - 1);
            edges.push_back(SIDE * row + column);
        }
    }
    return edges;
}

Point cover_point(
    int edge,
    Assignment const& top,
    std::array<int8_t, N> const& bottom,
    int orientation
) {
    int row = edge / SIDE;
    int column = edge % SIDE;
    int x = row < N
        ? (orientation < 2 ? row : 2 * row)
        : (orientation < 2 ? N + bottom[row % N] : 2 * bottom[row % N] + 1);
    int y = orientation % 2 == 0
        ? N * (column / N) + top[column]
        : 2 * top[column] + column / N;
    return {x, y};
}

uint64_t cover_mix(uint64_t hash, uint64_t value) {
    hash ^= value;
    return hash * 1099511628211ULL;
}

struct TripleCoverage {
    std::array<uint8_t, 3> triple{};
    std::array<uint64_t, 79> words{};
};

uint64_t intersection_size(
    std::array<uint64_t, 79> const& first,
    std::array<uint64_t, 79> const& second
) {
    uint64_t total = 0;
    for (size_t index = 0; index < first.size(); ++index)
        total += __builtin_popcountll(first[index] & second[index]);
    return total;
}

bool empty_words(std::array<uint64_t, 79> const& words) {
    for (auto word : words) if (word) return false;
    return true;
}

int main(int argc, char** argv) {
    if (argc < 4 || argc > 5) {
        std::cerr << "usage: " << argv[0]
                  << " MULTIPLICITY CASE_INDEX ORIENTATION [TOP_COUNT]\n";
        return 64;
    }

    int multiplicity = std::stoi(argv[1]);
    int requested_case = std::stoi(argv[2]);
    int orientation = std::stoi(argv[3]);
    int requested_top_count = argc == 5 ? std::stoi(argv[4]) : 1;
    if (multiplicity <= 0 || multiplicity > 63 || requested_case < 0
        || orientation < 0 || orientation >= 4 || requested_top_count <= 0) {
        std::cerr << "invalid parameters\n";
        return 64;
    }

    auto layer = generate_layer();
    std::map<Signature, std::vector<State>> groups;
    for (auto const& state : layer) {
        Signature signature{};
        for (int row = 0; row < N; ++row) signature[row] = state[row];
        groups[signature].push_back(state);
    }

    Signature signature{};
    std::vector<State> group;
    int case_index = 0;
    int signature_count = 0;
    for (auto const& [candidate_signature, candidate_group] : groups) {
        if (static_cast<int>(candidate_group.size()) != multiplicity) continue;
        if (case_index == requested_case) {
            signature = candidate_signature;
            group = candidate_group;
            std::sort(group.begin(), group.end());
        }
        ++case_index;
        ++signature_count;
    }
    if (group.empty()) {
        std::cerr << "case exceeds multiplicity tier: case=" << requested_case
                  << " signatures=" << signature_count << "\n";
        return 65;
    }

    TopEnumerator top;
    top.sig = signature;
    top.run(orientation % 2);
    size_t top_count = std::min<size_t>(requested_top_count, top.solutions.size());

    std::vector<std::array<int8_t, N>> bottom_permutations;
    std::array<int8_t, N> bottom{};
    for (int value = 0; value < N; ++value)
        bottom[value] = static_cast<int8_t>(value);
    do {
        bottom_permutations.push_back(bottom);
    } while (std::next_permutation(bottom.begin(), bottom.end()));
    assert(bottom_permutations.size() == 5040);

    uint64_t digest = 1469598103934665603ULL;
    digest = cover_mix(digest, multiplicity);
    digest = cover_mix(digest, requested_case);
    digest = cover_mix(digest, orientation);
    for (auto value : signature) digest = cover_mix(digest, value);

    std::set<std::array<uint8_t, 3>> triple_dictionary;
    std::set<std::vector<std::array<uint8_t, 3>>> cover_dictionary;
    uint64_t total_cover_entries = 0;

    for (size_t top_index = 0; top_index < top_count; ++top_index) {
        auto const& top_assignment = top.solutions[top_index];
        digest = cover_mix(digest, top_index);
        for (auto value : top_assignment)
            digest = cover_mix(digest, static_cast<uint8_t>(value));

        for (int selector = 0; selector < multiplicity; ++selector) {
            auto edges = cover_edges(group[selector]);
            assert(edges.size() == 28);
            std::vector<TripleCoverage> coverages;

            for (size_t i = 0; i < edges.size(); ++i)
                for (size_t j = i + 1; j < edges.size(); ++j)
                    for (size_t k = j + 1; k < edges.size(); ++k) {
                        TripleCoverage coverage;
                        coverage.triple = {
                            static_cast<uint8_t>(edges[i]),
                            static_cast<uint8_t>(edges[j]),
                            static_cast<uint8_t>(edges[k])
                        };
                        for (size_t permutation = 0;
                             permutation < bottom_permutations.size();
                             ++permutation) {
                            auto const& assignment = bottom_permutations[permutation];
                            if (det(
                                cover_point(edges[i], top_assignment, assignment, orientation),
                                cover_point(edges[j], top_assignment, assignment, orientation),
                                cover_point(edges[k], top_assignment, assignment, orientation)
                            ) == 0)
                                coverage.words[permutation / 64]
                                    |= uint64_t(1) << (permutation % 64);
                        }
                        if (!empty_words(coverage.words))
                            coverages.push_back(coverage);
                    }

            std::array<uint64_t, 79> uncovered{};
            uncovered.fill(~uint64_t(0));
            uncovered.back() = (uint64_t(1) << (5040 - 64 * 78)) - 1;
            std::vector<std::array<uint8_t, 3>> chosen;

            while (!empty_words(uncovered)) {
                size_t best = coverages.size();
                uint64_t best_gain = 0;
                for (size_t index = 0; index < coverages.size(); ++index) {
                    uint64_t gain = intersection_size(
                        coverages[index].words, uncovered
                    );
                    if (gain > best_gain) {
                        best_gain = gain;
                        best = index;
                    }
                }
                if (best == coverages.size() || best_gain == 0) {
                    std::cerr << "FEASIBLE selector=" << selector
                              << " top_index=" << top_index << "\n";
                    return 2;
                }
                chosen.push_back(coverages[best].triple);
                triple_dictionary.insert(coverages[best].triple);
                for (size_t word = 0; word < uncovered.size(); ++word)
                    uncovered[word] &= ~coverages[best].words[word];
            }

            for (auto const& triple : chosen)
                for (auto edge : triple) digest = cover_mix(digest, edge);
            digest = cover_mix(digest, chosen.size());
            total_cover_entries += chosen.size();
            cover_dictionary.insert(chosen);

            std::cout << "top_index=" << top_index
                      << " selector=" << selector
                      << " available_triples=" << coverages.size()
                      << " greedy_cover=" << chosen.size()
                      << " triple_dictionary=" << triple_dictionary.size()
                      << " cover_dictionary=" << cover_dictionary.size()
                      << " digest=" << digest << "\n";
        }
    }

    std::cout << "FINAL multiplicity=" << multiplicity
              << " case=" << requested_case
              << " orientation=" << orientation
              << " top_orders=" << top_count
              << " selector_covers=" << top_count * multiplicity
              << " cover_entries=" << total_cover_entries
              << " triple_dictionary=" << triple_dictionary.size()
              << " cover_dictionary=" << cover_dictionary.size()
              << " digest=" << digest << " PASS\n";
    return 0;
}

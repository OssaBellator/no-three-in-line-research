#include "product_side_seven_cache_engine.hpp"

#include <cstdlib>
#include <set>

namespace {
constexpr int MULTIPLICITY = 2;
constexpr int GLOBAL_CASE = 0;
constexpr int ORIENTATION = 3;
constexpr int TOP_INDEX = 35;

using Triple = std::array<uint8_t, 3>;

struct TripleCoverage {
    Triple triple{};
    std::array<uint64_t, 79> words{};
};

uint64_t mix(uint64_t hash, uint64_t value) {
    hash ^= value;
    return hash * 1099511628211ULL;
}

std::vector<int> selector_edges(State const& state) {
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

Point scalar_point(
    int edge,
    Assignment const& top,
    std::array<int8_t, N> const& bottom
) {
    int row = edge / SIDE;
    int column = edge % SIDE;
    int x = row < N ? 2 * row : 2 * bottom[row % N] + 1;
    int y = 2 * top[column] + column / N;
    return {x, y};
}

bool empty_words(std::array<uint64_t, 79> const& words) {
    for (auto word : words) if (word) return false;
    return true;
}

uint64_t intersection_size(
    std::array<uint64_t, 79> const& first,
    std::array<uint64_t, 79> const& second
) {
    uint64_t total = 0;
    for (size_t index = 0; index < first.size(); ++index)
        total += __builtin_popcountll(first[index] & second[index]);
    return total;
}

std::vector<std::array<int8_t, N>> bottom_permutations() {
    std::vector<std::array<int8_t, N>> result;
    std::array<int8_t, N> bottom{};
    for (int value = 0; value < N; ++value) bottom[value] = int8_t(value);
    do result.push_back(bottom);
    while (std::next_permutation(bottom.begin(), bottom.end()));
    assert(result.size() == 5040);
    return result;
}

std::vector<Triple> greedy_cover(
    State const& state,
    Assignment const& top,
    std::vector<std::array<int8_t, N>> const& bottoms
) {
    auto edges = selector_edges(state);
    assert(edges.size() == 28);
    std::vector<TripleCoverage> coverages;
    for (size_t i = 0; i < edges.size(); ++i)
        for (size_t j = i + 1; j < edges.size(); ++j)
            for (size_t k = j + 1; k < edges.size(); ++k) {
                TripleCoverage coverage;
                coverage.triple = {
                    uint8_t(edges[i]), uint8_t(edges[j]), uint8_t(edges[k])
                };
                for (size_t permutation = 0; permutation < bottoms.size(); ++permutation) {
                    auto const& bottom = bottoms[permutation];
                    if (det(
                        scalar_point(edges[i], top, bottom),
                        scalar_point(edges[j], top, bottom),
                        scalar_point(edges[k], top, bottom)
                    ) == 0)
                        coverage.words[permutation / 64]
                            |= uint64_t(1) << (permutation % 64);
                }
                if (!empty_words(coverage.words)) coverages.push_back(coverage);
            }

    std::array<uint64_t, 79> uncovered{};
    uncovered.fill(~uint64_t(0));
    uncovered.back() = (uint64_t(1) << (5040 - 64 * 78)) - 1;
    std::vector<Triple> chosen;
    while (!empty_words(uncovered)) {
        size_t best = coverages.size();
        uint64_t best_gain = 0;
        for (size_t index = 0; index < coverages.size(); ++index) {
            uint64_t gain = intersection_size(coverages[index].words, uncovered);
            if (gain > best_gain) {
                best_gain = gain;
                best = index;
            }
        }
        assert(best != coverages.size() && best_gain > 0);
        chosen.push_back(coverages[best].triple);
        for (size_t word = 0; word < uncovered.size(); ++word)
            uncovered[word] &= ~coverages[best].words[word];
    }
    return chosen;
}

uint16_t syntactic_support(std::vector<Triple> const& cover) {
    uint16_t mask = 0;
    for (auto const& triple : cover)
        for (auto edge : triple)
            mask |= uint16_t(1u << (edge % SIDE));
    return mask;
}

bool cover_valid(
    std::vector<Triple> const& cover,
    Assignment const& top,
    std::vector<std::array<int8_t, N>> const& bottoms,
    uint64_t& tested_bottoms
) {
    for (auto const& bottom : bottoms) {
        ++tested_bottoms;
        bool covered = false;
        for (auto const& triple : cover) {
            int first = triple[0], second = triple[1], third = triple[2];
            if (det(
                scalar_point(first, top, bottom),
                scalar_point(second, top, bottom),
                scalar_point(third, top, bottom)
            ) == 0) {
                covered = true;
                break;
            }
        }
        if (!covered) return false;
    }
    return true;
}

struct AssumptionTopEnumerator {
    Signature signature{};
    Assignment reference{};
    Assignment assignment{};
    std::array<uint8_t, 2> used{};
    std::vector<Assignment> solutions;
    uint64_t nodes = 0;

    bool clean_partial() const {
        std::array<Point, 14> points{};
        int count = 0;
        for (int row = 0; row < N; ++row) {
            uint16_t mask = signature[row];
            while (mask) {
                int column = __builtin_ctz(unsigned(mask));
                mask &= uint16_t(mask - 1);
                if (assignment[column] >= 0)
                    points[count++] = {
                        row,
                        2 * assignment[column] + column / N
                    };
            }
        }
        for (int i = 0; i < count; ++i)
            for (int j = i + 1; j < count; ++j)
                for (int k = j + 1; k < count; ++k)
                    if (det(points[i], points[j], points[k]) == 0) return false;
        return true;
    }

    void dfs(int depth) {
        ++nodes;
        if (depth == SIDE) {
            solutions.push_back(assignment);
            return;
        }
        int best = -1, best_size = 8, domain_size = 0;
        std::array<int8_t, N> best_domain{};
        for (int variable = 0; variable < SIDE; ++variable)
            if (assignment[variable] < 0) {
                int block = variable / N, size = 0;
                std::array<int8_t, N> domain{};
                for (int value = 0; value < N; ++value)
                    if (!((used[block] >> value) & 1u)) {
                        assignment[variable] = int8_t(value);
                        if (clean_partial()) domain[size++] = int8_t(value);
                        assignment[variable] = -1;
                    }
                if (size == 0) return;
                if (size < best_size) {
                    best_size = size;
                    best = variable;
                    domain_size = size;
                    best_domain = domain;
                }
            }
        int block = best / N;
        for (int index = 0; index < domain_size; ++index) {
            int value = best_domain[index];
            assignment[best] = int8_t(value);
            used[block] |= uint8_t(1u << value);
            dfs(depth + 1);
            used[block] &= uint8_t(~(1u << value));
            assignment[best] = -1;
        }
    }

    void run(Signature const& sig, Assignment const& top, uint16_t keep_mask) {
        signature = sig;
        reference = top;
        assignment.fill(-1);
        used.fill(0);
        solutions.clear();
        nodes = 0;
        int depth = 0;
        for (int column = 0; column < SIDE; ++column)
            if ((keep_mask >> column) & 1u) {
                int value = reference[column], block = column / N;
                assert(!((used[block] >> value) & 1u));
                assignment[column] = int8_t(value);
                used[block] |= uint8_t(1u << value);
                ++depth;
            }
        assert(clean_partial());
        dfs(depth);
    }
};

void locate_case(
    std::vector<State> const& layer,
    Signature& signature,
    std::vector<State>& group
) {
    std::map<Signature, std::vector<State>> groups;
    for (auto const& state : layer) {
        Signature sig{};
        for (int row = 0; row < N; ++row) sig[row] = state[row];
        groups[sig].push_back(state);
    }
    int index = 0;
    for (auto const& [sig, candidate] : groups) {
        if (candidate.size() != MULTIPLICITY) continue;
        if (index == GLOBAL_CASE) {
            signature = sig;
            group = candidate;
            std::sort(group.begin(), group.end());
            return;
        }
        ++index;
    }
    assert(false && "missing case");
}

struct MinimizedCover {
    std::vector<Triple> cover;
    uint16_t syntactic_mask = 0;
    uint16_t semantic_mask = 0;
};

MinimizedCover minimize_selector(
    int selector,
    Signature const& signature,
    State const& state,
    Assignment const& reference,
    std::vector<std::array<int8_t, N>> const& bottoms,
    uint64_t& digest
) {
    MinimizedCover result;
    result.cover = greedy_cover(state, reference, bottoms);
    assert(result.cover.size() == 7);
    result.syntactic_mask = syntactic_support(result.cover);
    result.semantic_mask = result.syntactic_mask;

    digest = mix(digest, selector);
    for (auto const& triple : result.cover)
        for (auto edge : triple) digest = mix(digest, edge);
    digest = mix(digest, result.syntactic_mask);

    for (int column = 0; column < SIDE; ++column) {
        if (!((result.semantic_mask >> column) & 1u)) continue;
        uint16_t candidate = uint16_t(result.semantic_mask & ~(1u << column));
        AssumptionTopEnumerator top;
        top.run(signature, reference, candidate);
        bool valid = true;
        uint64_t tested_bottoms = 0;
        size_t checked_extensions = 0;
        for (auto const& extension : top.solutions) {
            ++checked_extensions;
            if (!cover_valid(result.cover, extension, bottoms, tested_bottoms)) {
                valid = false;
                break;
            }
        }
        std::cout << "selector=" << selector
                  << " delete_column=" << column
                  << " candidate_mask=" << candidate
                  << " retained=" << __builtin_popcount(unsigned(candidate))
                  << " clean_extensions=" << top.solutions.size()
                  << " checked_extensions=" << checked_extensions
                  << " top_nodes=" << top.nodes
                  << " tested_bottoms=" << tested_bottoms
                  << " valid=" << valid << "\n";
        digest = mix(digest, column);
        digest = mix(digest, candidate);
        digest = mix(digest, top.solutions.size());
        digest = mix(digest, checked_extensions);
        digest = mix(digest, top.nodes);
        digest = mix(digest, tested_bottoms);
        digest = mix(digest, valid);
        if (valid) result.semantic_mask = candidate;
    }

    std::cout << "selector=" << selector
              << " syntactic_mask=" << result.syntactic_mask
              << " syntactic_size="
              << __builtin_popcount(unsigned(result.syntactic_mask))
              << " semantic_mask=" << result.semantic_mask
              << " semantic_size="
              << __builtin_popcount(unsigned(result.semantic_mask)) << "\n";
    digest = mix(digest, result.semantic_mask);
    return result;
}
} // namespace

int main() {
    auto layer = generate_layer();
    Signature signature{};
    std::vector<State> group;
    locate_case(layer, signature, group);

    TopEnumerator top;
    top.sig = signature;
    top.run(ORIENTATION % 2);
    assert(top.solutions.size() > TOP_INDEX);
    Assignment reference = top.solutions[TOP_INDEX];
    auto bottoms = bottom_permutations();

    uint64_t digest = 1469598103934665603ULL;
    digest = mix(digest, GLOBAL_CASE);
    digest = mix(digest, ORIENTATION);
    digest = mix(digest, TOP_INDEX);
    for (auto value : signature) digest = mix(digest, value);
    for (auto value : reference) digest = mix(digest, uint8_t(value));

    std::array<MinimizedCover, MULTIPLICITY> minimized;
    for (int selector = 0; selector < MULTIPLICITY; ++selector)
        minimized[selector] = minimize_selector(
            selector, signature, group[selector], reference, bottoms, digest
        );

    uint16_t pair_mask = uint16_t(
        minimized[0].semantic_mask | minimized[1].semantic_mask
    );
    AssumptionTopEnumerator extensions;
    extensions.run(signature, reference, pair_mask);
    uint64_t tested_bottoms = 0;
    for (auto const& extension : extensions.solutions)
        for (int selector = 0; selector < MULTIPLICITY; ++selector)
            assert(cover_valid(
                minimized[selector].cover, extension, bottoms, tested_bottoms
            ));
    digest = mix(digest, pair_mask);
    digest = mix(digest, extensions.solutions.size());
    digest = mix(digest, extensions.nodes);
    digest = mix(digest, tested_bottoms);

    std::cout << "FINAL case=" << GLOBAL_CASE
              << " orientation=" << ORIENTATION
              << " top_index=" << TOP_INDEX
              << " selector0_mask=" << minimized[0].semantic_mask
              << " selector1_mask=" << minimized[1].semantic_mask
              << " pair_mask=" << pair_mask
              << " pair_size=" << __builtin_popcount(unsigned(pair_mask))
              << " clean_extensions=" << extensions.solutions.size()
              << " top_nodes=" << extensions.nodes
              << " tested_bottoms=" << tested_bottoms
              << " digest=" << digest << " PASS\n";
    return 0;
}

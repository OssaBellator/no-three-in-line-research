#define main semantic_cover_core_top35_main
#include "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.cpp"
#undef main

#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <vector>

namespace {
constexpr int EXPANSION_REFERENCES = 16;

struct RelaxedPartialKey {
    uint16_t mask = 0;
    Assignment values{};
    bool operator<(RelaxedPartialKey const& other) const {
        if (mask != other.mask) return mask < other.mask;
        return values < other.values;
    }
};

RelaxedPartialKey relaxed_key(uint16_t mask, Assignment const& assignment) {
    RelaxedPartialKey key;
    key.mask = mask;
    key.values.fill(-1);
    for (int column = 0; column < SIDE; ++column)
        if ((mask >> column) & 1u) key.values[column] = assignment[column];
    return key;
}

MinimizedCover minimize_selector_relaxed(
    int selector,
    Signature const& signature,
    State const& state,
    Assignment const& reference,
    std::vector<std::array<int8_t, N>> const& bottoms,
    uint64_t& digest
) {
    MinimizedCover result;
    result.cover = greedy_cover(state, reference, bottoms);
    result.syntactic_mask = syntactic_support(result.cover);
    result.semantic_mask = result.syntactic_mask;

    digest = mix(digest, selector);
    digest = mix(digest, result.cover.size());
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
        digest = mix(digest, column);
        digest = mix(digest, candidate);
        digest = mix(digest, top.solutions.size());
        digest = mix(digest, checked_extensions);
        digest = mix(digest, top.nodes);
        digest = mix(digest, tested_bottoms);
        digest = mix(digest, valid);
        if (valid) result.semantic_mask = candidate;
    }

    digest = mix(digest, result.semantic_mask);
    return result;
}

void print_counts(std::map<int, int> const& counts) {
    bool first = true;
    for (auto const& [value, count] : counts) {
        if (!first) std::cout << ',';
        first = false;
        std::cout << value << ':' << count;
    }
}

void print_indices(std::vector<int> const& indices) {
    for (size_t index = 0; index < indices.size(); ++index) {
        if (index) std::cout << ',';
        std::cout << indices[index];
    }
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
    assert(top.solutions.size() == 35112);
    assert(top.nodes == 97189);
    auto bottoms = bottom_permutations();

    uint64_t digest = 1469598103934665603ULL;
    std::set<RelaxedPartialKey> baseline_vocabulary;
    std::set<Assignment> baseline_union;

    for (int top_index = 0; top_index < 192; ++top_index) {
        Assignment const& reference = top.solutions[top_index];
        digest = mix(digest, top_index);
        for (auto value : reference) digest = mix(digest, uint8_t(value));

        std::array<MinimizedCover, MULTIPLICITY> minimized;
        for (int selector = 0; selector < MULTIPLICITY; ++selector)
            minimized[selector] = minimize_selector_relaxed(
                selector, signature, group[selector], reference, bottoms, digest
            );

        uint16_t pair_mask = uint16_t(
            minimized[0].semantic_mask | minimized[1].semantic_mask
        );
        baseline_vocabulary.insert(relaxed_key(pair_mask, reference));

        AssumptionTopEnumerator extensions;
        extensions.run(signature, reference, pair_mask);
        baseline_union.insert(
            extensions.solutions.begin(), extensions.solutions.end()
        );
        digest = mix(digest, pair_mask);
        digest = mix(digest, extensions.solutions.size());
        digest = mix(digest, extensions.nodes);
    }

    assert(baseline_vocabulary.size() == 150);
    assert(baseline_union.size() == 204);

    std::vector<int> selected_indices;
    for (size_t top_index = 0;
         top_index < top.solutions.size()
         && selected_indices.size() < EXPANSION_REFERENCES;
         ++top_index) {
        if (!baseline_union.count(top.solutions[top_index]))
            selected_indices.push_back(int(top_index));
    }
    assert(selected_indices.size() == EXPANSION_REFERENCES);

    std::set<RelaxedPartialKey> expanded_vocabulary = baseline_vocabulary;
    std::set<Assignment> expanded_union = baseline_union;
    uint64_t extension_sum = 0;
    uint64_t bottom_checks = 0;
    int new_reference_keys = 0;
    std::map<int, int> pair_size_counts;

    for (int top_index : selected_indices) {
        Assignment const& reference = top.solutions[top_index];
        digest = mix(digest, 0xfeed0000ULL + uint64_t(top_index));
        for (auto value : reference) digest = mix(digest, uint8_t(value));

        std::array<MinimizedCover, MULTIPLICITY> minimized;
        for (int selector = 0; selector < MULTIPLICITY; ++selector)
            minimized[selector] = minimize_selector_relaxed(
                selector, signature, group[selector], reference, bottoms, digest
            );

        uint16_t pair_mask = uint16_t(
            minimized[0].semantic_mask | minimized[1].semantic_mask
        );
        int pair_size = __builtin_popcount(unsigned(pair_mask));
        ++pair_size_counts[pair_size];
        bool new_key = expanded_vocabulary.insert(
            relaxed_key(pair_mask, reference)
        ).second;
        if (new_key) ++new_reference_keys;

        AssumptionTopEnumerator extensions;
        extensions.run(signature, reference, pair_mask);
        extension_sum += extensions.solutions.size();
        assert(std::find(
            extensions.solutions.begin(), extensions.solutions.end(), reference
        ) != extensions.solutions.end());
        for (auto const& extension : extensions.solutions) {
            expanded_union.insert(extension);
            for (int selector = 0; selector < MULTIPLICITY; ++selector)
                assert(cover_valid(
                    minimized[selector].cover,
                    extension,
                    bottoms,
                    bottom_checks
                ));
        }

        digest = mix(digest, pair_mask);
        digest = mix(digest, new_key);
        digest = mix(digest, extensions.solutions.size());
        digest = mix(digest, extensions.nodes);
        std::cout << "REFERENCE top_index=" << top_index
                  << " pair_mask=" << pair_mask
                  << " pair_size=" << pair_size
                  << " new_key=" << new_key
                  << " clean_extensions=" << extensions.solutions.size()
                  << " top_nodes=" << extensions.nodes << "\n";
    }

    size_t new_distinct_keys = expanded_vocabulary.size()
        - baseline_vocabulary.size();
    size_t union_growth = expanded_union.size() - baseline_union.size();
    assert(new_distinct_keys > 0);
    assert(union_growth >= EXPANSION_REFERENCES);
    digest = mix(digest, new_distinct_keys);
    digest = mix(digest, extension_sum);
    digest = mix(digest, union_growth);
    digest = mix(digest, bottom_checks);

    std::cout << "FINAL baseline_references=192 baseline_vocabulary=150"
              << " baseline_union=204 expansion_references="
              << EXPANSION_REFERENCES << " selected_indices=";
    print_indices(selected_indices);
    std::cout << " new_reference_keys=" << new_reference_keys
              << " new_distinct_keys=" << new_distinct_keys
              << " expanded_vocabulary=" << expanded_vocabulary.size()
              << " extension_sum=" << extension_sum
              << " union_growth=" << union_growth
              << " expanded_union=" << expanded_union.size()
              << " remaining_uncovered="
              << top.solutions.size() - expanded_union.size()
              << " pair_size_counts=";
    print_counts(pair_size_counts);
    std::cout << " bottom_checks=" << bottom_checks
              << " digest=" << digest << " PASS\n";
    return 0;
}

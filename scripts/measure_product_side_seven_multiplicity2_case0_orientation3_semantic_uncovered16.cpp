#define main semantic_vocabulary_full192_relaxed_main
#include "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full192_relaxed.cpp"
#undef main

#include <cassert>
#include <iostream>
#include <set>
#include <vector>

namespace {
constexpr int EXPANSION_REFERENCES = 16;

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

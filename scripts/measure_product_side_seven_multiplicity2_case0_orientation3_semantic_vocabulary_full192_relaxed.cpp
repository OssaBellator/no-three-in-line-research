#define main semantic_vocabulary_full128_relaxed_main
#include "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full128_relaxed.cpp"
#undef main

int main() {
    auto layer = generate_layer();
    Signature signature{};
    std::vector<State> group;
    locate_case(layer, signature, group);

    TopEnumerator top;
    top.sig = signature;
    top.run(ORIENTATION % 2);
    assert(top.solutions.size() >= 192);
    auto bottoms = bottom_permutations();

    uint64_t digest = 1469598103934665603ULL;
    std::set<RelaxedPartialKey> vocabulary;
    std::set<RelaxedPartialKey> baseline128_vocabulary;
    std::set<Assignment> covered_top_orders;
    uint64_t extension_sum = 0;
    uint64_t bottom_checks = 0;
    std::map<int,int> pair_size_counts;
    std::map<int,int> new_pair_size_counts;
    std::array<std::map<int,int>,2> cover_size_counts;
    std::array<std::map<int,int>,2> new_cover_size_counts;
    int equal_selector_masks = 0;
    int new_equal_selector_masks = 0;
    int reused_baseline128_references = 0;

    for (int top_index = 0; top_index < 192; ++top_index) {
        Assignment const& reference = top.solutions[top_index];
        digest = mix(digest, top_index);
        for (auto value : reference) digest = mix(digest, uint8_t(value));

        std::array<MinimizedCover, MULTIPLICITY> minimized;
        for (int selector = 0; selector < MULTIPLICITY; ++selector) {
            minimized[selector] = minimize_selector_relaxed(
                selector, signature, group[selector], reference, bottoms, digest
            );
            ++cover_size_counts[selector][int(minimized[selector].cover.size())];
            if (top_index >= 128)
                ++new_cover_size_counts[selector][int(minimized[selector].cover.size())];
        }

        bool equal = minimized[0].semantic_mask == minimized[1].semantic_mask;
        if (equal) ++equal_selector_masks;
        if (top_index >= 128 && equal) ++new_equal_selector_masks;
        uint16_t pair_mask = uint16_t(
            minimized[0].semantic_mask | minimized[1].semantic_mask
        );
        int pair_size = __builtin_popcount(unsigned(pair_mask));
        ++pair_size_counts[pair_size];
        if (top_index >= 128) ++new_pair_size_counts[pair_size];

        RelaxedPartialKey key = relaxed_key(pair_mask, reference);
        if (top_index >= 128 && baseline128_vocabulary.count(key))
            ++reused_baseline128_references;
        vocabulary.insert(key);

        AssumptionTopEnumerator extensions;
        extensions.run(signature, reference, pair_mask);
        extension_sum += extensions.solutions.size();
        for (auto const& extension : extensions.solutions) {
            covered_top_orders.insert(extension);
            for (int selector = 0; selector < MULTIPLICITY; ++selector)
                assert(cover_valid(
                    minimized[selector].cover, extension, bottoms, bottom_checks
                ));
        }
        digest = mix(digest, minimized[0].semantic_mask);
        digest = mix(digest, minimized[1].semantic_mask);
        digest = mix(digest, pair_mask);
        digest = mix(digest, extensions.solutions.size());
        digest = mix(digest, extensions.nodes);

        if (top_index == 127) {
            baseline128_vocabulary = vocabulary;
            assert(baseline128_vocabulary.size() == 102);
            assert(equal_selector_masks == 40);
            assert(extension_sum == 316);
            assert(covered_top_orders.size() == 164);
            assert(bottom_checks == 3185280);
            assert(cover_size_counts[0] == std::map<int,int>({{7,125},{12,3}}));
            assert(cover_size_counts[1] == std::map<int,int>({{7,128}}));
        }
    }

    std::map<uint16_t,int> mask_counts;
    for (auto const& key : vocabulary) {
        ++mask_counts[key.mask];
        digest = mix(digest, key.mask);
        for (auto value : key.values) digest = mix(digest, uint8_t(value + 1));
    }
    digest = mix(digest, extension_sum);
    digest = mix(digest, covered_top_orders.size());
    digest = mix(digest, bottom_checks);
    digest = mix(digest, reused_baseline128_references);

    std::cout << "FINAL references=192"
              << " vocabulary=" << vocabulary.size()
              << " baseline128_vocabulary=" << baseline128_vocabulary.size()
              << " new_distinct_keys=" << vocabulary.size() - baseline128_vocabulary.size()
              << " reused_baseline128_references=" << reused_baseline128_references
              << " equal_selector_masks=" << equal_selector_masks
              << " new_equal_selector_masks=" << new_equal_selector_masks
              << " pair_size_counts=";
    print_counts(pair_size_counts);
    std::cout << " new_pair_size_counts=";
    print_counts(new_pair_size_counts);
    std::cout << " selector0_cover_sizes=";
    print_counts(cover_size_counts[0]);
    std::cout << " selector1_cover_sizes=";
    print_counts(cover_size_counts[1]);
    std::cout << " new_selector0_cover_sizes=";
    print_counts(new_cover_size_counts[0]);
    std::cout << " new_selector1_cover_sizes=";
    print_counts(new_cover_size_counts[1]);
    std::cout << " mask_classes=" << mask_counts.size()
              << " extension_sum=" << extension_sum
              << " new_extension_sum=" << extension_sum - 316
              << " covered_union=" << covered_top_orders.size()
              << " new_covered_union=" << covered_top_orders.size() - 164
              << " overlap=" << extension_sum - covered_top_orders.size()
              << " bottom_checks=" << bottom_checks
              << " new_bottom_checks=" << bottom_checks - 3185280
              << " digest=" << digest << " PASS\n";
    return 0;
}

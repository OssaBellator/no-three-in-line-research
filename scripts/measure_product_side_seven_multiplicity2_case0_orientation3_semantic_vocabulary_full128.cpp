#define main semantic_cover_core_top35_main
#include "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.cpp"
#undef main

namespace {
struct Full128PartialKey {
    uint16_t mask = 0;
    Assignment values{};
    bool operator<(Full128PartialKey const& other) const {
        if (mask != other.mask) return mask < other.mask;
        return values < other.values;
    }
};

Full128PartialKey full128_key(uint16_t mask, Assignment const& assignment) {
    Full128PartialKey key;
    key.mask = mask;
    key.values.fill(-1);
    for (int column = 0; column < SIDE; ++column)
        if ((mask >> column) & 1u) key.values[column] = assignment[column];
    return key;
}

void print_size_counts(std::map<int,int> const& counts) {
    bool first = true;
    for (auto const& [size,count] : counts) {
        if (!first) std::cout << ',';
        first = false;
        std::cout << size << ':' << count;
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
    assert(top.solutions.size() >= 128);
    auto bottoms = bottom_permutations();

    uint64_t digest = 1469598103934665603ULL;
    std::set<Full128PartialKey> vocabulary;
    std::set<Full128PartialKey> baseline_vocabulary;
    std::set<Assignment> covered_top_orders;
    uint64_t extension_sum = 0;
    uint64_t bottom_checks = 0;
    std::map<int,int> pair_size_counts;
    std::map<int,int> new_pair_size_counts;
    int equal_selector_masks = 0;
    int new_equal_selector_masks = 0;
    int reused_baseline_references = 0;

    for (int top_index = 0; top_index < 128; ++top_index) {
        Assignment const& reference = top.solutions[top_index];
        digest = mix(digest, top_index);
        for (auto value : reference) digest = mix(digest, uint8_t(value));

        std::array<MinimizedCover, MULTIPLICITY> minimized;
        for (int selector = 0; selector < MULTIPLICITY; ++selector)
            minimized[selector] = minimize_selector(
                selector, signature, group[selector], reference, bottoms, digest
            );

        bool equal = minimized[0].semantic_mask == minimized[1].semantic_mask;
        if (equal) ++equal_selector_masks;
        if (top_index >= 64 && equal) ++new_equal_selector_masks;
        uint16_t pair_mask = uint16_t(
            minimized[0].semantic_mask | minimized[1].semantic_mask
        );
        int pair_size = __builtin_popcount(unsigned(pair_mask));
        ++pair_size_counts[pair_size];
        if (top_index >= 64) ++new_pair_size_counts[pair_size];

        Full128PartialKey key = full128_key(pair_mask, reference);
        if (top_index >= 64 && baseline_vocabulary.count(key))
            ++reused_baseline_references;
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

        if (top_index == 63) {
            baseline_vocabulary = vocabulary;
            assert(baseline_vocabulary.size() == 49);
            assert(equal_selector_masks == 30);
            assert(extension_sum == 169);
            assert(covered_top_orders.size() == 92);
            assert(bottom_checks == 1703520);
        }

        std::cout << "top_index=" << top_index
                  << " selector0_mask=" << minimized[0].semantic_mask
                  << " selector1_mask=" << minimized[1].semantic_mask
                  << " pair_mask=" << pair_mask
                  << " pair_size=" << pair_size
                  << " clean_extensions=" << extensions.solutions.size()
                  << " vocabulary=" << vocabulary.size()
                  << " covered_union=" << covered_top_orders.size()
                  << " digest=" << digest << "\n";
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
    digest = mix(digest, reused_baseline_references);

    std::cout << "FINAL references=128"
              << " vocabulary=" << vocabulary.size()
              << " baseline_vocabulary=" << baseline_vocabulary.size()
              << " new_distinct_keys=" << vocabulary.size() - baseline_vocabulary.size()
              << " reused_baseline_references=" << reused_baseline_references
              << " equal_selector_masks=" << equal_selector_masks
              << " new_equal_selector_masks=" << new_equal_selector_masks
              << " pair_size_counts=";
    print_size_counts(pair_size_counts);
    std::cout << " new_pair_size_counts=";
    print_size_counts(new_pair_size_counts);
    std::cout << " mask_classes=" << mask_counts.size()
              << " extension_sum=" << extension_sum
              << " new_extension_sum=" << extension_sum - 169
              << " covered_union=" << covered_top_orders.size()
              << " new_covered_union=" << covered_top_orders.size() - 92
              << " overlap=" << extension_sum - covered_top_orders.size()
              << " bottom_checks=" << bottom_checks
              << " new_bottom_checks=" << bottom_checks - 1703520
              << " digest=" << digest << " PASS\n";
    return 0;
}

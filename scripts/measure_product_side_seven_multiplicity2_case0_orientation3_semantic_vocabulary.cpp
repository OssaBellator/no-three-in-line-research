#define main semantic_cover_core_top35_main
#include "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.cpp"
#undef main

namespace {
struct PartialKey {
    uint16_t mask = 0;
    Assignment values{};
    bool operator<(PartialKey const& other) const {
        if (mask != other.mask) return mask < other.mask;
        return values < other.values;
    }
};

PartialKey partial_key(uint16_t mask, Assignment const& assignment) {
    PartialKey key;
    key.mask = mask;
    key.values.fill(-1);
    for (int column = 0; column < SIDE; ++column)
        if ((mask >> column) & 1u) key.values[column] = assignment[column];
    return key;
}
} // namespace

int main() {
    const std::array<int, 12> top_indices = {0,1,6,7,9,50,51,56,57,60,61,63};

    auto layer = generate_layer();
    Signature signature{};
    std::vector<State> group;
    locate_case(layer, signature, group);

    TopEnumerator top;
    top.sig = signature;
    top.run(ORIENTATION % 2);
    auto bottoms = bottom_permutations();

    uint64_t digest = 1469598103934665603ULL;
    std::set<PartialKey> vocabulary;
    std::set<Assignment> covered_top_orders;
    uint64_t extension_sum = 0;
    uint64_t bottom_checks = 0;

    for (int top_index : top_indices) {
        Assignment const& reference = top.solutions[top_index];
        digest = mix(digest, top_index);
        for (auto value : reference) digest = mix(digest, uint8_t(value));

        std::array<MinimizedCover, MULTIPLICITY> minimized;
        for (int selector = 0; selector < MULTIPLICITY; ++selector)
            minimized[selector] = minimize_selector(
                selector, signature, group[selector], reference, bottoms, digest
            );

        uint16_t pair_mask = uint16_t(
            minimized[0].semantic_mask | minimized[1].semantic_mask
        );
        assert(minimized[0].semantic_mask == minimized[1].semantic_mask);
        PartialKey key = partial_key(pair_mask, reference);
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
        digest = mix(digest, pair_mask);
        digest = mix(digest, extensions.solutions.size());
        digest = mix(digest, extensions.nodes);
        std::cout << "top_index=" << top_index
                  << " pair_mask=" << pair_mask
                  << " pair_size=" << __builtin_popcount(unsigned(pair_mask))
                  << " clean_extensions=" << extensions.solutions.size()
                  << " vocabulary=" << vocabulary.size()
                  << " covered_union=" << covered_top_orders.size()
                  << " digest=" << digest << "\n";
    }

    std::array<int, 2> mask_counts{};
    for (auto const& key : vocabulary) {
        if (key.mask == 6936) ++mask_counts[0];
        else if (key.mask == 6920) ++mask_counts[1];
        else assert(false);
        digest = mix(digest, key.mask);
        for (auto value : key.values) digest = mix(digest, uint8_t(value + 1));
    }
    digest = mix(digest, extension_sum);
    digest = mix(digest, covered_top_orders.size());
    digest = mix(digest, bottom_checks);

    std::cout << "FINAL references=" << top_indices.size()
              << " vocabulary=" << vocabulary.size()
              << " mask6936_keys=" << mask_counts[0]
              << " mask6920_keys=" << mask_counts[1]
              << " extension_sum=" << extension_sum
              << " covered_union=" << covered_top_orders.size()
              << " overlap=" << extension_sum - covered_top_orders.size()
              << " bottom_checks=" << bottom_checks
              << " digest=" << digest << " PASS\n";
    return 0;
}

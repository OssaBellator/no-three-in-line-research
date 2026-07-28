#define main semantic_cover_core_top35_main
#include "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.cpp"
#undef main

namespace {
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

void print_counts(std::map<int,int> const& counts) {
    bool first = true;
    for (auto const& [value,count] : counts) {
        if (!first) std::cout << ',';
        first = false;
        std::cout << value << ':' << count;
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
    std::set<RelaxedPartialKey> vocabulary;
    std::set<RelaxedPartialKey> baseline_vocabulary;
    std::set<Assignment> covered_top_orders;
    uint64_t extension_sum = 0;
    uint64_t bottom_checks = 0;
    std::map<int,int> pair_size_counts;
    std::map<int,int> new_pair_size_counts;
    std::array<std::map<int,int>,2> cover_size_counts;
    std::array<std::map<int,int>,2> new_cover_size_counts;
    int equal_selector_masks = 0;
    int new_equal_selector_masks = 0;
    int reused_baseline_references = 0;

    for (int top_index = 0; top_index < 128; ++top_index) {
        Assignment const& reference = top.solutions[top_index];
        digest = mix(digest, top_index);
        for (auto value : reference) digest = mix(digest, uint8_t(value));

        std::array<MinimizedCover, MULTIPLICITY> minimized;
        for (int selector = 0; selector < MULTIPLICITY; ++selector) {
            minimized[selector] = minimize_selector_relaxed(
                selector, signature, group[selector], reference, bottoms, digest
            );
            ++cover_size_counts[selector][int(minimized[selector].cover.size())];
            if (top_index >= 64)
                ++new_cover_size_counts[selector][int(minimized[selector].cover.size())];
        }

        bool equal = minimized[0].semantic_mask == minimized[1].semantic_mask;
        if (equal) ++equal_selector_masks;
        if (top_index >= 64 && equal) ++new_equal_selector_masks;
        uint16_t pair_mask = uint16_t(
            minimized[0].semantic_mask | minimized[1].semantic_mask
        );
        int pair_size = __builtin_popcount(unsigned(pair_mask));
        ++pair_size_counts[pair_size];
        if (top_index >= 64) ++new_pair_size_counts[pair_size];

        RelaxedPartialKey key = relaxed_key(pair_mask, reference);
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
            assert(cover_size_counts[0].size() == 1 && cover_size_counts[0][7] == 64);
            assert(cover_size_counts[1].size() == 1 && cover_size_counts[1][7] == 64);
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
    digest = mix(digest, reused_baseline_references);

    std::cout << "FINAL references=128"
              << " vocabulary=" << vocabulary.size()
              << " baseline_vocabulary=" << baseline_vocabulary.size()
              << " new_distinct_keys=" << vocabulary.size() - baseline_vocabulary.size()
              << " reused_baseline_references=" << reused_baseline_references
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
              << " new_extension_sum=" << extension_sum - 169
              << " covered_union=" << covered_top_orders.size()
              << " new_covered_union=" << covered_top_orders.size() - 92
              << " overlap=" << extension_sum - covered_top_orders.size()
              << " bottom_checks=" << bottom_checks
              << " new_bottom_checks=" << bottom_checks - 1703520
              << " digest=" << digest << " PASS\n";
    return 0;
}

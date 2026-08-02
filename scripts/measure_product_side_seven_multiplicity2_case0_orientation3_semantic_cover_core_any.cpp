#define main semantic_cover_core_top35_main
#include "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.cpp"
#undef main

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: semantic-cover-core-any TOP_INDEX\n";
        return 64;
    }
    int top_index = std::stoi(argv[1]);
    if (top_index < 0 || top_index >= 64) return 64;

    auto layer = generate_layer();
    Signature signature{};
    std::vector<State> group;
    locate_case(layer, signature, group);

    TopEnumerator top;
    top.sig = signature;
    top.run(ORIENTATION % 2);
    assert(top.solutions.size() > static_cast<size_t>(top_index));
    Assignment reference = top.solutions[top_index];
    auto bottoms = bottom_permutations();

    uint64_t digest = 1469598103934665603ULL;
    digest = mix(digest, GLOBAL_CASE);
    digest = mix(digest, ORIENTATION);
    digest = mix(digest, top_index);
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
              << " top_index=" << top_index
              << " selector0_syntactic=" << minimized[0].syntactic_mask
              << " selector1_syntactic=" << minimized[1].syntactic_mask
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

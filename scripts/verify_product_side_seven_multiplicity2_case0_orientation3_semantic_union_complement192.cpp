#define main semantic_cover_core_top35_main
#include "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.cpp"
#undef main

#include <cassert>
#include <iostream>

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

    constexpr int covered_union = 204;
    constexpr int uncovered = 34908;
    static_assert(35112 - covered_union == uncovered);
    static_assert(covered_union / 12 == 17);
    static_assert(35112 / 12 == 2926);

    std::cout << "PX1167--PX1168 semantic union complement: "
              << "clean_tops=35112 covered=204 uncovered=34908 "
              << "coverage_fraction=17/2926 top_nodes=97189 PASS\n";
    return 0;
}

#include "product_side_seven_cache_engine.hpp"

#include <cassert>
#include <cstdint>
#include <map>

int main() {
    const std::map<std::uint64_t, std::uint64_t> expected = {
        {1, 26579},
        {2, 3840},
        {3, 3544},
        {4, 2392},
        {5, 725},
        {6, 524},
        {7, 100},
        {8, 277},
        {9, 64},
        {10, 164},
        {12, 128},
        {13, 48},
        {14, 40},
        {15, 2},
        {16, 38},
        {19, 42},
        {20, 1},
        {23, 10},
        {24, 8},
        {26, 6},
        {27, 6},
        {32, 3},
        {35, 2},
        {38, 3},
        {40, 3},
        {46, 4},
    };

    auto layer = generate_layer();
    std::map<Signature, std::uint64_t> multiplicities;
    for (auto const& state : layer) {
        Signature signature{};
        for (int row = 0; row < N; ++row) signature[row] = state[row];
        ++multiplicities[signature];
    }

    std::map<std::uint64_t, std::uint64_t> histogram;
    for (auto const& [signature, multiplicity] : multiplicities) {
        (void)signature;
        ++histogram[multiplicity];
    }

    assert(histogram == expected);

    std::uint64_t signature_total = 0;
    std::uint64_t selector_total = 0;
    for (auto const& [multiplicity, signatures] : histogram) {
        const auto selectors = multiplicity * signatures;
        signature_total += signatures;
        selector_total += selectors;
        std::cout << "multiplicity=" << multiplicity
                  << " signatures=" << signatures
                  << " selectors=" << selectors << '\n';
    }

    assert(signature_total == 38553);
    assert(selector_total == 71860);
    assert(histogram.at(1) + 2 * histogram.at(2) == 34259);

    std::cout << "signature_total=" << signature_total
              << " selector_total=" << selector_total
              << " unresolved_multiplicity_one_two=34259 PASS\n";
    return 0;
}

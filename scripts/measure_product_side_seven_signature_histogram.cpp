#include "product_side_seven_cache_engine.hpp"

#include <cstdint>
#include <map>

int main() {
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
    std::cout << "signature_total=" << signature_total
              << " selector_total=" << selector_total << '\n';
    return 0;
}

#define main product_affine_eight_main
#include "verify_product_transposition_class_eight.cpp"
#undef main

#include <set>

std::vector<Permutation> bit_affine_permutations() {
    std::set<Permutation> unique;
    std::array<int, 3> coordinate_order = {0, 1, 2};
    do {
        for (int translation = 0; translation < 8; ++translation) {
            Permutation permutation{};
            for (int input = 0; input < 8; ++input) {
                int output = translation;
                for (int output_bit = 0; output_bit < 3; ++output_bit) {
                    if ((input >> coordinate_order[output_bit]) & 1) {
                        output ^= 1 << output_bit;
                    }
                }
                permutation[input] = output;
            }
            unique.insert(permutation);
        }
    } while (std::next_permutation(coordinate_order.begin(), coordinate_order.end()));
    return {unique.begin(), unique.end()};
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: verifier <cc|cf|fc|ff>\n";
        return 2;
    }
    const std::string orientation = argv[1];
    if (orientation != "cc" && orientation != "cf"
        && orientation != "fc" && orientation != "ff") {
        return 2;
    }

    const auto group = bit_affine_permutations();
    if (group.size() != 48) {
        std::abort();
    }

    long long total_nodes = 0;
    long long maximum_nodes = 0;
    int pair_count = 0;
    for (const auto& target : group) {
        for (const auto& column_relative : group) {
            const SearchResult result =
                search_geometry(target, column_relative, orientation);
            if (result.feasible) {
                std::cout << "FOUND o=" << orientation << '\n';
                return 1;
            }
            total_nodes += result.nodes;
            maximum_nodes = std::max(maximum_nodes, result.nodes);
            ++pair_count;
        }
    }

    std::cout
        << "NONE o=" << orientation
        << " pairs=" << pair_count
        << " total=" << total_nodes
        << " max=" << maximum_nodes
        << '\n';
    return 0;
}

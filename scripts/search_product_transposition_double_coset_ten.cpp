#define main affine_search_main
#include "search_product_transposition_affine_columns.cpp"
#undef main

#include <set>

Permutation compose_double_coset(
    Permutation const& first,
    Permutation const& second
) {
    Permutation result(first.size());
    for (size_t index = 0; index < first.size(); ++index)
        result[index] = first[second[index]];
    return result;
}

std::vector<Permutation> transposition_double_coset(
    std::vector<Permutation> const& affine,
    int distance
) {
    int n = static_cast<int>(affine.front().size());
    Permutation transposition(n);
    std::iota(transposition.begin(), transposition.end(), 0);
    std::swap(transposition[0], transposition[distance]);

    std::set<Permutation> unique;
    for (auto const& left : affine)
        for (auto const& right : affine)
            unique.insert(compose_double_coset(
                left,
                compose_double_coset(transposition, right)
            ));
    return {unique.begin(), unique.end()};
}

int main(int argc, char** argv) {
    if (argc < 3 || argc > 5) {
        std::cerr
            << "usage: search <cc|cf|fc|ff> <1|2|5> [FIRST_PAIR] [PAIR_COUNT]\n";
        return 2;
    }

    std::string orientation = argv[1];
    int distance = std::stoi(argv[2]);
    if ((orientation != "cc" && orientation != "cf"
         && orientation != "fc" && orientation != "ff")
        || (distance != 1 && distance != 2 && distance != 5))
        return 2;

    constexpr int n = 10;
    auto affine = affine_permutations(n);
    auto column_maps = transposition_double_coset(affine, distance);
    int expected_maps = distance == 5 ? 200 : 800;
    if (static_cast<int>(column_maps.size()) != expected_maps) return 3;

    int total_pairs = static_cast<int>(affine.size() * column_maps.size());
    int first_pair = argc >= 4 ? std::stoi(argv[3]) : 0;
    int pair_count = argc >= 5 ? std::stoi(argv[4]) : total_pairs - first_pair;
    if (first_pair < 0 || pair_count < 0
        || first_pair + pair_count > total_pairs)
        return 2;

    ThroughTable through(2 * n);
    std::uint64_t total_nodes = 0;
    std::uint64_t maximum_nodes = 0;

    for (int pair = first_pair; pair < first_pair + pair_count; ++pair) {
        int target_index = pair / static_cast<int>(column_maps.size());
        int column_index = pair % static_cast<int>(column_maps.size());
        SearchResult result = search_geometry(
            n,
            affine[target_index],
            column_maps[column_index],
            orientation,
            through
        );
        total_nodes += result.nodes;
        maximum_nodes = std::max(maximum_nodes, result.nodes);
        if (result.feasible) {
            std::cout << "FOUND n=10"
                      << " o=" << orientation
                      << " distance=" << distance
                      << " maps=" << column_maps.size()
                      << " pair=" << pair
                      << " target=" << target_index
                      << " column=" << column_index
                      << " nodes=" << result.nodes
                      << " T=";
            for (int value : affine[target_index]) std::cout << value << ',';
            std::cout << " Q=";
            for (int value : column_maps[column_index])
                std::cout << value << ',';
            std::cout << " cells=";
            for (int point : result.points)
                std::cout << '(' << point / (2 * n)
                          << ',' << point % (2 * n) << ')';
            std::cout << '\n';
            return 0;
        }
    }

    std::cout << "NONE n=10"
              << " o=" << orientation
              << " distance=" << distance
              << " maps=" << column_maps.size()
              << " first=" << first_pair
              << " pairs=" << pair_count
              << " total=" << total_nodes
              << " avg=" << (pair_count ? total_nodes / pair_count : 0)
              << " max=" << maximum_nodes
              << '\n';
    return 0;
}

#define main affine_search_main
#include "search_product_transposition_affine_columns.cpp"
#undef main

#include <unordered_set>

struct SplitMix64 {
    std::uint64_t state;

    explicit SplitMix64(std::uint64_t seed) : state(seed) {}

    std::uint64_t next() {
        std::uint64_t value = (state += 0x9e3779b97f4a7c15ULL);
        value = (value ^ (value >> 30)) * 0xbf58476d1ce4e5b9ULL;
        value = (value ^ (value >> 27)) * 0x94d049bb133111ebULL;
        return value ^ (value >> 31);
    }
};

void deterministic_shuffle(Permutation& permutation, SplitMix64& generator) {
    for (int index = static_cast<int>(permutation.size()) - 1;
         index > 0;
         --index) {
        int other = static_cast<int>(
            generator.next() % static_cast<std::uint64_t>(index + 1)
        );
        std::swap(permutation[index], permutation[other]);
    }
}

std::string permutation_key(Permutation const& permutation) {
    std::string result;
    for (int value : permutation) {
        result += std::to_string(value);
        result.push_back(',');
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 5) {
        std::cerr << "usage: sample N <cc|cf|fc|ff> SAMPLES SEED\n";
        return 2;
    }

    int n = std::stoi(argv[1]);
    std::string orientation = argv[2];
    int requested_samples = std::stoi(argv[3]);
    std::uint64_t seed = std::stoull(argv[4]);
    if (n < 2 || n > 20 || n % 2 || requested_samples < 0
        || (orientation != "cc" && orientation != "cf"
            && orientation != "fc" && orientation != "ff"))
        return 2;

    SplitMix64 generator(seed);
    ThroughTable through(2 * n);
    std::unordered_set<std::string> affine;
    for (auto const& permutation : affine_permutations(n))
        affine.insert(permutation_key(permutation));

    Permutation target(n);
    Permutation relative(n);
    std::uint64_t total_nodes = 0;
    std::uint64_t maximum_nodes = 0;
    int accepted = 0;
    int draws = 0;

    while (accepted < requested_samples) {
        std::iota(target.begin(), target.end(), 0);
        std::iota(relative.begin(), relative.end(), 0);
        deterministic_shuffle(target, generator);
        deterministic_shuffle(relative, generator);
        ++draws;

        if (affine.count(permutation_key(target))
            || affine.count(permutation_key(relative)))
            continue;

        SearchResult result = search_geometry(
            n, target, relative, orientation, through
        );
        total_nodes += result.nodes;
        maximum_nodes = std::max(maximum_nodes, result.nodes);
        if (result.feasible) {
            std::cout << "FOUND n=" << n
                      << " o=" << orientation
                      << " sample=" << accepted
                      << " seed=" << seed
                      << " draws=" << draws
                      << " nodes=" << result.nodes
                      << " T=";
            for (int value : target) std::cout << value << ',';
            std::cout << " Q=";
            for (int value : relative) std::cout << value << ',';
            std::cout << " cells=";
            for (int point : result.points)
                std::cout << '(' << point / (2 * n)
                          << ',' << point % (2 * n) << ')';
            std::cout << '\n';
            return 0;
        }
        ++accepted;
    }

    std::cout << "NONE n=" << n
              << " o=" << orientation
              << " samples=" << requested_samples
              << " seed=" << seed
              << " draws=" << draws
              << " total=" << total_nodes
              << " max=" << maximum_nodes
              << '\n';
    return 0;
}

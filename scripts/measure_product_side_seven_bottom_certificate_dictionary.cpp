#include "product_side_seven_cache_engine.hpp"

#include <cstdlib>
#include <iomanip>
#include <optional>
#include <set>

std::vector<int> certificate_edges(State const& state) {
    std::vector<int> edges;
    for (int row = 0; row < SIDE; ++row) {
        uint16_t mask = state[row];
        while (mask) {
            int column = __builtin_ctz(unsigned(mask));
            mask &= uint16_t(mask - 1);
            edges.push_back(SIDE * row + column);
        }
    }
    return edges;
}

Point certificate_point(
    int edge,
    Assignment const& top,
    std::array<int8_t, N> const& bottom,
    int orientation
) {
    int row = edge / SIDE;
    int column = edge % SIDE;
    int x = row < N
        ? (orientation < 2 ? row : 2 * row)
        : (orientation < 2 ? N + bottom[row % N] : 2 * bottom[row % N] + 1);
    int y = orientation % 2 == 0
        ? N * (column / N) + top[column]
        : 2 * top[column] + column / N;
    return {x, y};
}

std::optional<std::array<uint8_t, 3>> first_bad_triple(
    State const& state,
    Assignment const& top,
    std::array<int8_t, N> const& bottom,
    int orientation
) {
    auto edges = certificate_edges(state);
    for (size_t i = 0; i < edges.size(); ++i)
        for (size_t j = i + 1; j < edges.size(); ++j)
            for (size_t k = j + 1; k < edges.size(); ++k)
                if (det(
                    certificate_point(edges[i], top, bottom, orientation),
                    certificate_point(edges[j], top, bottom, orientation),
                    certificate_point(edges[k], top, bottom, orientation)
                ) == 0)
                    return std::array<uint8_t, 3>{
                        static_cast<uint8_t>(edges[i]),
                        static_cast<uint8_t>(edges[j]),
                        static_cast<uint8_t>(edges[k])
                    };
    return std::nullopt;
}

uint64_t dictionary_mix(uint64_t hash, uint64_t value) {
    hash ^= value;
    return hash * 1099511628211ULL;
}

int main(int argc, char** argv) {
    if (argc < 4 || argc > 5) {
        std::cerr << "usage: " << argv[0]
                  << " MULTIPLICITY CASE_INDEX ORIENTATION [TOP_COUNT]\n";
        return 64;
    }

    int multiplicity = std::stoi(argv[1]);
    int requested_case = std::stoi(argv[2]);
    int orientation = std::stoi(argv[3]);
    int requested_top_count = argc == 5 ? std::stoi(argv[4]) : 0;
    if (multiplicity <= 0 || multiplicity > 63 || requested_case < 0
        || orientation < 0 || orientation >= 4 || requested_top_count < 0) {
        std::cerr << "invalid parameters\n";
        return 64;
    }

    auto layer = generate_layer();
    std::map<Signature, std::vector<State>> groups;
    for (auto const& state : layer) {
        Signature signature{};
        for (int row = 0; row < N; ++row) signature[row] = state[row];
        groups[signature].push_back(state);
    }

    Signature signature{};
    std::vector<State> group;
    int signature_count = 0;
    for (auto const& [candidate_signature, candidate_group] : groups) {
        if (static_cast<int>(candidate_group.size()) != multiplicity) continue;
        if (signature_count == requested_case) {
            signature = candidate_signature;
            group = candidate_group;
            std::sort(group.begin(), group.end());
        }
        ++signature_count;
    }
    if (group.empty()) {
        std::cerr << "case exceeds multiplicity tier: case=" << requested_case
                  << " signatures=" << signature_count << "\n";
        return 65;
    }

    TopEnumerator top;
    top.sig = signature;
    top.run(orientation % 2);
    size_t top_count = requested_top_count == 0
        ? top.solutions.size()
        : std::min<size_t>(requested_top_count, top.solutions.size());

    std::set<std::array<uint8_t, 3>> dictionary;
    uint64_t digest = 1469598103934665603ULL;
    uint64_t obligations = 0;

    digest = dictionary_mix(digest, multiplicity);
    digest = dictionary_mix(digest, requested_case);
    digest = dictionary_mix(digest, orientation);
    for (auto value : signature) digest = dictionary_mix(digest, value);

    for (size_t top_index = 0; top_index < top_count; ++top_index) {
        auto const& top_assignment = top.solutions[top_index];
        digest = dictionary_mix(digest, top_index);
        for (auto value : top_assignment)
            digest = dictionary_mix(digest, static_cast<uint8_t>(value));

        std::array<int8_t, N> bottom{};
        for (int value = 0; value < N; ++value)
            bottom[value] = static_cast<int8_t>(value);
        do {
            for (int selector = 0; selector < multiplicity; ++selector) {
                auto triple = first_bad_triple(
                    group[selector], top_assignment, bottom, orientation
                );
                if (!triple) {
                    std::cerr << "FEASIBLE selector=" << selector
                              << " top_index=" << top_index << " bottom=";
                    for (auto value : bottom) std::cerr << int(value);
                    std::cerr << "\n";
                    return 2;
                }
                dictionary.insert(*triple);
                for (auto edge : *triple) digest = dictionary_mix(digest, edge);
                ++obligations;
            }
        } while (std::next_permutation(bottom.begin(), bottom.end()));

        std::cout << "top_orders=" << (top_index + 1)
                  << " dictionary=" << dictionary.size()
                  << " obligations=" << obligations
                  << " digest=" << digest << "\n";
    }

    uint64_t projected_bytes = 48
        + top_count * SIDE
        + dictionary.size() * 3
        + obligations;
    std::cout << "FINAL multiplicity=" << multiplicity
              << " case=" << requested_case
              << " orientation=" << orientation
              << " top_orders=" << top_count
              << " available_top_orders=" << top.solutions.size()
              << " dictionary=" << dictionary.size()
              << " obligations=" << obligations
              << " projected_bytes=" << projected_bytes
              << " digest=" << digest << " PASS\n";
    return 0;
}

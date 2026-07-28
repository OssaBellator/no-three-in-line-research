#define main semantic_cover_core_top35_main
#include "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_cover_core.cpp"
#undef main

#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>

namespace {
struct RelaxedPartialKey {
    uint16_t mask = 0;
    Assignment values{};
    bool operator<(RelaxedPartialKey const& other) const {
        if (mask != other.mask) return mask < other.mask;
        return values < other.values;
    }
};

struct KeyRecord {
    RelaxedPartialKey key;
    std::array<MinimizedCover, MULTIPLICITY> minimized;
    std::set<Assignment> extensions;
    int first_reference = -1;
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
    State const& state,
    Signature const& signature,
    Assignment const& reference,
    std::vector<std::array<int8_t,N>> const& bottoms
) {
    MinimizedCover result;
    result.cover = greedy_cover(state, reference, bottoms);
    result.syntactic_mask = syntactic_support(result.cover);
    result.semantic_mask = result.syntactic_mask;
    for (int column = 0; column < SIDE; ++column) {
        if (!((result.semantic_mask >> column) & 1u)) continue;
        uint16_t candidate = uint16_t(result.semantic_mask & ~(1u << column));
        AssumptionTopEnumerator top;
        top.run(signature, reference, candidate);
        bool valid = true;
        uint64_t tested_bottoms = 0;
        for (auto const& extension : top.solutions) {
            if (!cover_valid(result.cover, extension, bottoms, tested_bottoms)) {
                valid = false;
                break;
            }
        }
        if (valid) result.semantic_mask = candidate;
    }
    return result;
}

void print_histogram(std::map<int,int> const& histogram) {
    bool first = true;
    for (auto const& [value,count] : histogram) {
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
    assert(top.solutions.size() >= 192);
    auto bottoms = bottom_permutations();

    std::map<RelaxedPartialKey,KeyRecord> records_by_key;
    uint64_t validation_checks = 0;
    for (int reference_index = 0; reference_index < 192; ++reference_index) {
        Assignment const& reference = top.solutions[reference_index];
        std::array<MinimizedCover,MULTIPLICITY> minimized;
        for (int selector = 0; selector < MULTIPLICITY; ++selector)
            minimized[selector] = minimize_selector_relaxed(
                group[selector], signature, reference, bottoms
            );
        uint16_t pair_mask = uint16_t(
            minimized[0].semantic_mask | minimized[1].semantic_mask
        );
        RelaxedPartialKey key = relaxed_key(pair_mask, reference);
        if (records_by_key.count(key)) continue;

        KeyRecord record;
        record.key = key;
        record.minimized = minimized;
        record.first_reference = reference_index;
        AssumptionTopEnumerator extensions;
        extensions.run(signature, reference, pair_mask);
        for (auto const& extension : extensions.solutions) {
            for (int selector = 0; selector < MULTIPLICITY; ++selector)
                assert(cover_valid(
                    record.minimized[selector].cover,
                    extension,
                    bottoms,
                    validation_checks
                ));
            record.extensions.insert(extension);
        }
        assert(!record.extensions.empty());
        records_by_key.emplace(key, std::move(record));
    }
    assert(records_by_key.size() == 150);

    std::vector<KeyRecord> records;
    std::set<Assignment> universe;
    for (auto const& [key,record] : records_by_key) {
        records.push_back(record);
        universe.insert(record.extensions.begin(), record.extensions.end());
    }
    assert(universe.size() == 204);

    std::set<Assignment> uncovered = universe;
    std::vector<int> greedy_basis;
    std::vector<int> greedy_gains;
    while (!uncovered.empty()) {
        int best_index = -1;
        int best_gain = -1;
        for (int index = 0; index < int(records.size()); ++index) {
            int gain = 0;
            for (auto const& assignment : records[index].extensions)
                if (uncovered.count(assignment)) ++gain;
            if (gain > best_gain) {
                best_gain = gain;
                best_index = index;
            }
        }
        assert(best_index >= 0 && best_gain > 0);
        greedy_basis.push_back(best_index);
        greedy_gains.push_back(best_gain);
        for (auto const& assignment : records[best_index].extensions)
            uncovered.erase(assignment);
    }

    // Deterministic reverse deletion turns the greedy basis into an irredundant cover.
    std::vector<int> basis = greedy_basis;
    for (int position = int(basis.size()) - 1; position >= 0; --position) {
        std::map<Assignment,int> counts;
        for (int index : basis)
            for (auto const& assignment : records[index].extensions)
                ++counts[assignment];
        bool removable = true;
        for (auto const& assignment : records[basis[position]].extensions)
            if (counts[assignment] == 1) {
                removable = false;
                break;
            }
        if (removable) basis.erase(basis.begin() + position);
    }

    std::map<Assignment,int> final_counts;
    std::map<int,int> mask_sizes;
    std::map<int,int> extension_sizes;
    uint64_t digest = 1469598103934665603ULL;
    for (int index : basis) {
        auto const& record = records[index];
        ++mask_sizes[__builtin_popcount(unsigned(record.key.mask))];
        ++extension_sizes[int(record.extensions.size())];
        digest = mix(digest, index);
        digest = mix(digest, record.first_reference);
        digest = mix(digest, record.key.mask);
        for (auto value : record.key.values) digest = mix(digest, uint8_t(value + 1));
        digest = mix(digest, record.extensions.size());
        for (auto const& assignment : record.extensions) {
            ++final_counts[assignment];
            for (auto value : assignment) digest = mix(digest, uint8_t(value));
        }
    }
    assert(final_counts.size() == universe.size());
    int unique_covered = 0;
    int maximum_overlap = 0;
    uint64_t incidence_sum = 0;
    for (auto const& [assignment,count] : final_counts) {
        if (count == 1) ++unique_covered;
        maximum_overlap = std::max(maximum_overlap, count);
        incidence_sum += count;
        digest = mix(digest, count);
    }
    assert(unique_covered > 0); // irredundancy witness

    std::cout << "FINAL references=192 vocabulary=150 universe=204"
              << " greedy_basis=" << greedy_basis.size()
              << " irredundant_basis=" << basis.size()
              << " greedy_gains=";
    for (size_t index = 0; index < greedy_gains.size(); ++index) {
        if (index) std::cout << ',';
        std::cout << greedy_gains[index];
    }
    std::cout << " basis_indices=";
    for (size_t position = 0; position < basis.size(); ++position) {
        if (position) std::cout << ',';
        std::cout << basis[position];
    }
    std::cout << " first_references=";
    for (size_t position = 0; position < basis.size(); ++position) {
        if (position) std::cout << ',';
        std::cout << records[basis[position]].first_reference;
    }
    std::cout << " mask_sizes=";
    print_histogram(mask_sizes);
    std::cout << " extension_sizes=";
    print_histogram(extension_sizes);
    std::cout << " incidence_sum=" << incidence_sum
              << " unique_covered=" << unique_covered
              << " maximum_overlap=" << maximum_overlap
              << " validation_checks=" << validation_checks
              << " digest=" << digest << " PASS\n";
    return 0;
}

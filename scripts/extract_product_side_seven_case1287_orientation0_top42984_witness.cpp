#include "product_side_seven_cache_engine.hpp"

#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <vector>

struct WitnessBottomSolver : BottomGroupSolver {
    uint64_t witness_active = 0;

    bool dfs_witness(int depth, uint64_t active) {
        ++nodes;
        if (depth == N) {
            witness_active = active;
            return active != 0;
        }
        int best_z = -1, best_size = 8, domain_size = 0;
        std::array<int8_t,N> best_domain{};
        std::array<uint64_t,N> best_masks{};
        for (int z = 0; z < N; ++z) if (bottom[z] < 0) {
            int size = 0;
            std::array<int8_t,N> domain{};
            std::array<uint64_t,N> masks{};
            for (int value = 0; value < N; ++value) if (!((used >> value) & 1u)) {
                bottom[z] = int8_t(value);
                uint64_t child = transition(z, active);
                bottom[z] = -1;
                if (child) {
                    domain[size] = int8_t(value);
                    masks[size] = child;
                    ++size;
                }
            }
            if (size == 0) return false;
            if (size < best_size) {
                best_size = size;
                best_z = z;
                domain_size = size;
                best_domain = domain;
                best_masks = masks;
            }
        }
        for (int i = 0; i < domain_size; ++i) {
            int value = best_domain[i];
            bottom[best_z] = int8_t(value);
            used |= uint8_t(1u << value);
            if (dfs_witness(depth + 1, best_masks[i])) return true;
            used &= uint8_t(~(1u << value));
            bottom[best_z] = -1;
        }
        return false;
    }

    bool solve_top_witness(Assignment const& top_assignment, int ori) {
        prepare_top(top_assignment, ori);
        bottom.fill(-1);
        used = 0;
        nodes = 0;
        witness_active = 0;
        return dfs_witness(0, all);
    }
};

int main() {
    constexpr int requested_case = 1287;
    constexpr int requested_top = 42984;
    constexpr int orientation = 0;

    auto layer = generate_layer();
    std::map<Signature,std::vector<State>> groups;
    for (auto const& state : layer) {
        Signature signature{};
        for (int row = 0; row < N; ++row) signature[row] = state[row];
        groups[signature].push_back(state);
    }

    int case_index = 0;
    for (auto const& [signature, unsorted_group] : groups) {
        if (unsorted_group.size() != 2) continue;
        if (case_index++ != requested_case) continue;
        auto group = unsorted_group;
        std::sort(group.begin(), group.end());

        TopEnumerator top;
        top.sig = signature;
        top.run(0);
        assert(requested_top < int(top.solutions.size()));
        Assignment const& top_assignment = top.solutions[requested_top];

        WitnessBottomSolver solver;
        solver.initialize(group);
        bool feasible = solver.solve_top_witness(top_assignment, orientation);
        assert(feasible);
        assert(solver.witness_active != 0);
        int candidate_index = __builtin_ctzll(solver.witness_active);
        State const& state = group[candidate_index];

        std::vector<Point> points;
        for (int row = 0; row < SIDE; ++row) {
            uint16_t mask = state[row];
            while (mask) {
                int column = __builtin_ctz(unsigned(mask));
                mask &= uint16_t(mask - 1);
                int x = row < N ? row : N + solver.bottom[row % N];
                int y = N * (column / N) + top_assignment[column];
                points.push_back({x,y});
            }
        }
        assert(points.size() == 28);
        std::set<std::pair<int,int>> distinct;
        std::array<int,SIDE> row_count{}, column_count{};
        for (auto point : points) {
            assert(0 <= point.x && point.x < SIDE);
            assert(0 <= point.y && point.y < SIDE);
            distinct.insert({point.x, point.y});
            ++row_count[point.x];
            ++column_count[point.y];
        }
        assert(distinct.size() == 28);
        assert(std::all_of(row_count.begin(), row_count.end(), [](int value){return value == 2;}));
        assert(std::all_of(column_count.begin(), column_count.end(), [](int value){return value == 2;}));
        for (int first = 0; first < 28; ++first)
            for (int second = first + 1; second < 28; ++second)
                for (int third = second + 1; third < 28; ++third)
                    assert(det(points[first], points[second], points[third]) != 0);

        std::cout << "FEASIBLE case=1287 orientation=0 top_index=42984 candidate="
                  << candidate_index << " nodes=" << solver.nodes << " signature=";
        for (int row = 0; row < N; ++row) {
            if (row) std::cout << ',';
            std::cout << signature[row];
        }
        std::cout << " top=";
        for (int column = 0; column < SIDE; ++column) {
            if (column) std::cout << ',';
            std::cout << int(top_assignment[column]);
        }
        std::cout << " bottom=";
        for (int z = 0; z < N; ++z) {
            if (z) std::cout << ',';
            std::cout << int(solver.bottom[z]);
        }
        std::cout << " state=";
        for (int row = 0; row < SIDE; ++row) {
            if (row) std::cout << ',';
            std::cout << state[row];
        }
        std::cout << " points=";
        for (size_t index = 0; index < points.size(); ++index) {
            if (index) std::cout << ';';
            std::cout << points[index].x << ',' << points[index].y;
        }
        std::cout << " PASS\n";
        return 0;
    }
    return 1;
}

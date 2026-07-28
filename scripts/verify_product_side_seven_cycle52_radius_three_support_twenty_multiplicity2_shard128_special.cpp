#include "product_side_seven_cache_engine.hpp"

#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <vector>

const std::array<CaseData,9> INFEASIBLE_CASES = {{
    CaseData{1280, {130,768,1028,24,2176,96,4160}, {106848,49440}, {498276ULL,218070ULL}, {158511ULL,77185ULL,149294ULL,70805ULL}},
    CaseData{1281, {130,768,1028,24,2176,96,12288}, {130512,24288}, {1108544ULL,219804ULL}, {203202ULL,35771ULL,181050ULL,38264ULL}},
    CaseData{1282, {130,768,1028,24,2176,4128,4160}, {91456,80572}, {495214ULL,420824ULL}, {132246ULL,117506ULL,126646ULL,109946ULL}},
    CaseData{1283, {130,768,1028,24,2176,4128,8256}, {59500,55516}, {582800ULL,517168ULL}, {84637ULL,82552ULL,81695ULL,71705ULL}},
    CaseData{1284, {130,768,1028,24,2176,8224,96}, {79124,112012}, {375770ULL,479020ULL}, {124323ULL,167571ULL,108462ULL,162794ULL}},
    CaseData{1285, {130,768,1028,24,2176,8224,4128}, {76784,67192}, {750074ULL,622746ULL}, {111755ULL,108647ULL,105497ULL,91196ULL}},
    CaseData{1286, {130,768,1028,24,2176,8224,8256}, {91456,80572}, {495214ULL,420824ULL}, {132246ULL,117506ULL,126646ULL,109946ULL}},
    CaseData{1288, {130,768,1028,24,2176,8256,4128}, {59500,55516}, {584916ULL,517506ULL}, {84642ULL,82539ULL,81687ULL,71708ULL}},
    CaseData{1289, {130,768,1028,24,2176,8256,4160}, {76784,67192}, {750074ULL,622746ULL}, {111755ULL,108647ULL,105497ULL,91196ULL}},
}};

const Signature SPECIAL_SIGNATURE = {130,768,1028,24,2176,8224,12288};
const Assignment WITNESS_TOP = {4,6,3,1,2,5,0,2,0,3,5,4,1,6};
const std::array<int8_t,N> WITNESS_BOTTOM = {6,5,4,3,2,0,1};
const State WITNESS_STATE = {130,768,1028,24,2176,8224,12288,257,6,520,3072,17,96,4160};
const std::array<uint64_t,4> SELECTOR_ONE_BOTTOM = {99110ULL,53920ULL,97697ULL,47125ULL};

int main() {
    auto layer = generate_layer();
    std::map<Signature,std::vector<State>> groups;
    std::map<int,int> histogram;
    for (auto const& state : layer) {
        Signature signature{};
        for (int row = 0; row < N; ++row) signature[row] = state[row];
        groups[signature].push_back(state);
    }
    for (auto const& [signature,group] : groups)
        ++histogram[int(group.size())];
    assert(histogram[2] == 3840);

    std::array<uint64_t,4> aggregate_bottom{};
    for (auto const& data : INFEASIBLE_CASES) {
        auto iterator = groups.find(data.signature);
        assert(iterator != groups.end());
        auto group = iterator->second;
        std::sort(group.begin(), group.end());
        assert(group.size() == 2);

        TopEnumerator top[2];
        for (int mode = 0; mode < 2; ++mode) {
            top[mode].sig = data.signature;
            top[mode].run(mode);
            assert(int(top[mode].solutions.size()) == data.top_orders[mode]);
            assert(top[mode].nodes == data.top_nodes[mode]);
        }

        BottomGroupSolver solver;
        solver.initialize(group);
        for (int orientation = 0; orientation < 4; ++orientation) {
            uint64_t total = 0;
            for (auto const& assignment : top[orientation % 2].solutions) {
                assert(!solver.solve_top(assignment, orientation));
                total += solver.nodes;
            }
            assert(total == data.bottom_nodes[orientation]);
            aggregate_bottom[orientation] += total;
        }
    }

    auto special_iterator = groups.find(SPECIAL_SIGNATURE);
    assert(special_iterator != groups.end());
    auto special_group = special_iterator->second;
    std::sort(special_group.begin(), special_group.end());
    assert(special_group.size() == 2);
    assert(special_group[0] == WITNESS_STATE);

    TopEnumerator special_top[2];
    const std::array<int,2> expected_top_orders = {79488,40560};
    const std::array<uint64_t,2> expected_top_nodes = {933498ULL,588812ULL};
    for (int mode = 0; mode < 2; ++mode) {
        special_top[mode].sig = SPECIAL_SIGNATURE;
        special_top[mode].run(mode);
        assert(int(special_top[mode].solutions.size()) == expected_top_orders[mode]);
        assert(special_top[mode].nodes == expected_top_nodes[mode]);
    }
    assert(special_top[0].solutions[42984] == WITNESS_TOP);

    std::vector<Point> points;
    std::array<int,SIDE> row_count{}, column_count{};
    std::set<std::pair<int,int>> distinct;
    for (int row = 0; row < SIDE; ++row) {
        uint16_t mask = WITNESS_STATE[row];
        while (mask) {
            int column = __builtin_ctz(unsigned(mask));
            mask &= uint16_t(mask - 1);
            int x = row < N ? row : N + WITNESS_BOTTOM[row % N];
            int y = N * (column / N) + WITNESS_TOP[column];
            points.push_back({x,y});
            distinct.insert({x,y});
            ++row_count[x];
            ++column_count[y];
        }
    }
    assert(points.size() == 28 && distinct.size() == 28);
    for (int value : row_count) assert(value == 2);
    for (int value : column_count) assert(value == 2);
    for (int first = 0; first < 28; ++first)
        for (int second = first + 1; second < 28; ++second)
            for (int third = second + 1; third < 28; ++third)
                assert(det(points[first],points[second],points[third]) != 0);

    std::vector<State> selector_one{special_group[1]};
    BottomGroupSolver selector_one_solver;
    selector_one_solver.initialize(selector_one);
    for (int orientation = 0; orientation < 4; ++orientation) {
        uint64_t total = 0;
        for (auto const& assignment : special_top[orientation % 2].solutions) {
            assert(!selector_one_solver.solve_top(assignment, orientation));
            total += selector_one_solver.nodes;
        }
        assert(total == SELECTOR_ONE_BOTTOM[orientation]);
        aggregate_bottom[orientation] += total;
    }

    const std::array<uint64_t,4> expected_aggregate = {
        1242427ULL,951844ULL,1164171ULL,864685ULL
    };
    assert(aggregate_bottom == expected_aggregate);
    assert(aggregate_bottom[0] + aggregate_bottom[1]
        + aggregate_bottom[2] + aggregate_bottom[3] == 4223127ULL);

    std::cout << "shard128 cases=1280-1289 infeasible_selectors=19 "
              << "constructive_selectors=1 rejection_nodes=4223127 "
              << "witness_case=1287 orientation=0 top_index=42984 PASS\n";
    return 0;
}

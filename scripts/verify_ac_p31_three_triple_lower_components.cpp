#define main verify_ac_p31_switch_frontier_base_main
#include "verify_ac_p31_switch_frontier.cpp"
#undef main

int main() {
    std::vector<int> red = {12,15,24,9,27,20,4,28,25,29,6,2,8,13,1,18,7,19,23,11,26,30,10,5,14,3,21,22,17,16};
    std::vector<int> blue = {17,10,21,22,7,15,8,23,28,13,9,4,20,26,30,12,27,24,29,5,14,1,2,11,18,6,3,16,25,19};
    std::string state = encode(red, blue);
    assert(potential(state) == 3);

    std::vector<std::pair<int, size_t>> checks = {
        {3,1}, {4,2}, {5,5}, {6,16}, {7,80}, {8,1159}
    };
    for (auto [barrier, expected_size] : checks) {
        auto [size, has_lower] = component(state, barrier, 3);
        assert(size == expected_size);
        assert(!has_lower);
    }

    std::cout << "AC p31 three-triple lower-component audit\n";
    std::cout << "component_sizes: 1,2,5,16,80,1159\n";
    std::cout << "certified_barrier_lower_bound: 9\n";
}

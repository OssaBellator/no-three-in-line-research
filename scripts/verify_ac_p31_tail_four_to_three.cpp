#define main verify_ac_p31_switch_frontier_base_main
#include "verify_ac_p31_switch_frontier.cpp"
#undef main

int main() {
    std::vector<int> red = {17,15,24,9,23,18,4,28,25,13,6,2,8,20,1,12,7,19,29,11,5,30,27,26,14,3,21,16,22,10};
    std::vector<int> blue = {12,25,23,18,7,15,8,2,28,1,9,4,20,29,30,16,27,24,26,5,14,21,6,11,22,10,3,13,17,19};
    std::string state = encode(red, blue);
    assert(potential(state) == 4);

    std::vector<std::pair<int, size_t>> lower = {
        {4,1}, {5,2}, {6,10}, {7,29}, {8,286}, {9,2033}
    };
    for (auto [barrier, expected_size] : lower) {
        auto [size, has_lower] = component(state, barrier, 4);
        assert(size == expected_size);
        assert(!has_lower);
    }

    std::vector<std::string> words = {
        "r:21,24","b:22,29","b:4,22","r:2,30","b:2,6","r:6,30",
        "r:8,14","r:19,26","b:14,19","r:14,26","r:5,26","r:19,26",
        "b:8,23","r:16,30","r:6,30","b:2,6","r:2,30","b:1,16",
        "b:1,30","r:10,14","b:2,26","r:1,6","r:6,8","r:5,8",
        "b:4,8","b:4,23","b:4,22","b:23,29","b:26,29","b:4,25",
        "b:10,22","b:10,28","r:28,29","b:28,30","r:29,30","r:5,29",
        "r:5,23","b:1,30","b:1,8","b:3,8","b:3,23"
    };
    std::vector<int> expected = {
        4,7,10,8,10,10,8,8,8,10,9,10,10,9,9,9,9,8,10,9,10,
        7,8,8,7,10,10,9,9,8,8,10,9,10,8,10,8,9,10,9,8,3
    };
    assert(words.size() + 1 == expected.size());
    for (size_t index = 0; index < words.size(); ++index) {
        Move move = parse(words[index]);
        assert(legal(state, move));
        state = apply(state, move);
        assert(potential(state) == expected[index + 1]);
    }
    assert(*std::max_element(expected.begin(), expected.end()) == 10);
    assert(potential(state) == 3);

    std::cout << "AC p31 four-to-three exact audit\n";
    std::cout << "lower_components: 1,2,10,29,286,2033\n";
    std::cout << "switches: " << words.size() << "\n";
    std::cout << "maximum_potential: 10\n";
    std::cout << "terminal_potential: 3\n";
}

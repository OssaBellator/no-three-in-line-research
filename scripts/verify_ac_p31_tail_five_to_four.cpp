#define main verify_ac_p31_switch_frontier_base_main
#include "verify_ac_p31_switch_frontier.cpp"
#undef main

int main() {
    std::vector<int> red = {17,20,24,18,23,15,4,6,25,13,9,2,8,28,1,12,7,19,29,5,26,30,27,11,14,3,21,16,22,10};
    std::vector<int> blue = {12,15,26,9,7,25,8,28,21,1,6,4,20,29,30,16,27,24,5,23,14,18,2,3,22,10,11,13,17,19};
    std::string state = encode(red, blue);
    assert(potential(state) == 5);

    std::vector<std::pair<int, size_t>> lower = {
        {5,1}, {6,2}, {7,18}, {8,68}, {9,501}
    };
    for (auto [barrier, expected_size] : lower) {
        auto [size, has_lower] = component(state, barrier, 5);
        assert(size == expected_size);
        assert(!has_lower);
    }

    std::vector<std::string> words = {
        "r:20,24","b:3,23","b:24,27","b:19,20","b:3,8","b:3,9",
        "r:8,14","b:19,23","r:21,24","r:2,14","r:2,26","r:2,30",
        "r:21,30","r:21,24","b:3,23","r:3,27","b:23,27","b:11,23",
        "r:24,30","r:2,30","r:2,26","r:21,24","r:2,11","r:2,30",
        "r:6,30","b:2,6","r:2,30","b:4,11","r:4,6","b:4,22",
        "b:22,27","r:3,27"
    };
    std::vector<int> expected = {
        5,7,10,10,9,10,9,10,9,10,10,9,10,10,10,9,10,
        10,8,10,8,10,10,10,10,9,10,7,10,10,10,8,4
    };
    assert(words.size() + 1 == expected.size());
    for (size_t index = 0; index < words.size(); ++index) {
        Move move = parse(words[index]);
        assert(legal(state, move));
        state = apply(state, move);
        assert(potential(state) == expected[index + 1]);
    }
    assert(*std::max_element(expected.begin(), expected.end()) == 10);
    assert(potential(state) == 4);

    std::cout << "AC p31 five-to-four exact audit\n";
    std::cout << "lower_components: 1,2,18,68,501\n";
    std::cout << "switches: " << words.size() << "\n";
    std::cout << "maximum_potential: 10\n";
    std::cout << "terminal_potential: 4\n";
}

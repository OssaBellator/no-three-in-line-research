#include <algorithm>
#include <array>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;

constexpr int M = 8;
constexpr int N = 16;
constexpr int Q = 1 << M;
using Rho = array<uint8_t, M>;

struct RhoHash {
  size_t operator()(Rho const &rho) const noexcept {
    size_t h = 0;
    for (auto value : rho) h = h * 13 + value + 1;
    return h;
  }
};
struct Point { int x, y; };
struct Assignment { array<Point, 4> points; };

bool collinear(Point a, Point b, Point c) {
  return 1LL * (b.x - a.x) * (c.y - a.y) ==
         1LL * (b.y - a.y) * (c.x - a.x);
}

vector<Rho> hamilton_cycles() {
  vector<Rho> out;
  array<int, M - 1> tail{};
  iota(tail.begin(), tail.end(), 1);
  do {
    array<int, M> order{};
    order[0] = 0;
    for (int i = 1; i < M; ++i) order[i] = tail[i - 1];
    Rho rho{};
    for (int i = 0; i < M; ++i) rho[order[i]] = order[(i + 1) % M];
    out.push_back(rho);
  } while (next_permutation(tail.begin(), tail.end()));
  return out;
}

Rho switched(Rho const &rho, uint8_t mask) {
  int start = 0;
  while (!(mask & (1 << start))) ++start;
  array<int, 3> source{};
  int count = 0;
  int current = start;
  for (int step = 0; step < M; ++step) {
    if (mask & (1 << current)) source[count++] = current;
    current = rho[current];
  }
  Rho out = rho;
  int b0 = rho[source[0]], b1 = rho[source[1]], b2 = rho[source[2]];
  out[source[0]] = b1;
  out[source[1]] = b2;
  out[source[2]] = b0;
  return out;
}

template <class K, class V>
void print_map(map<K, V> const &values) {
  cout << "{";
  bool first = true;
  for (auto const &[key, value] : values) {
    if (!first) cout << ",";
    first = false;
    cout << "\"" << key << "\":" << value;
  }
  cout << "}";
}

int main() {
  auto cycles = hamilton_cycles();
  unordered_map<Rho, int, RhoHash> cycle_id;
  for (int i = 0; i < (int)cycles.size(); ++i) cycle_id[cycles[i]] = i;

  vector<uint8_t> pair_masks;
  vector<uint8_t> triple_masks;
  for (int a = 0; a < M; ++a)
    for (int b = a + 1; b < M; ++b) {
      pair_masks.push_back((1 << a) | (1 << b));
      for (int c = b + 1; c < M; ++c)
        triple_masks.push_back((1 << a) | (1 << b) | (1 << c));
    }
  array<uint32_t, M> incident_pairs{};
  for (int i = 0; i < (int)pair_masks.size(); ++i)
    for (int source = 0; source < M; ++source)
      if (pair_masks[i] & (1 << source)) incident_pairs[source] |= 1u << i;
  array<uint64_t, 56> meeting_triples{};
  for (int i = 0; i < 56; ++i)
    for (int j = 0; j < 56; ++j)
      if (triple_masks[i] & triple_masks[j]) meeting_triples[i] |= 1ull << j;

  auto reversal = [](int x) { return N - 1 - x; };
  vector<Assignment> assignments;
  int assignment_id[M][M][2];
  fill(&assignment_id[0][0][0], &assignment_id[0][0][0] + M * M * 2, -1);
  for (int source = 0; source < M; ++source)
    for (int target = 0; target < M; ++target) {
      if (source == target) continue;
      for (int orientation = 0; orientation < 2; ++orientation) {
        Point q0{source, orientation ? reversal(target) : target};
        Point q1{reversal(source), orientation ? target : reversal(target)};
        assignment_id[source][target][orientation] = assignments.size();
        assignments.push_back({{q0, q1, Point{reversal(q0.y), q0.x},
                                Point{reversal(q1.y), q1.x}}});
      }
    }

  int assignment_count = assignments.size();
  vector<uint8_t> pair_count(assignment_count * assignment_count);
  vector<uint8_t> triple_count((size_t)assignment_count * assignment_count * assignment_count);
  for (int a = 0; a < assignment_count; ++a)
    for (int b = a + 1; b < assignment_count; ++b) {
      int count = 0;
      for (int x = 0; x < 4; ++x)
        for (int y = x + 1; y < 4; ++y)
          for (int z = 0; z < 4; ++z)
            count += collinear(assignments[a].points[x], assignments[a].points[y],
                               assignments[b].points[z]);
      for (int x = 0; x < 4; ++x)
        for (int y = x + 1; y < 4; ++y)
          for (int z = 0; z < 4; ++z)
            count += collinear(assignments[b].points[x], assignments[b].points[y],
                               assignments[a].points[z]);
      pair_count[a * assignment_count + b] = pair_count[b * assignment_count + a] = count;
    }
  for (int a = 0; a < assignment_count; ++a)
    for (int b = a + 1; b < assignment_count; ++b)
      for (int c = b + 1; c < assignment_count; ++c) {
        int count = 0;
        for (int x = 0; x < 4; ++x)
          for (int y = 0; y < 4; ++y)
            for (int z = 0; z < 4; ++z)
              count += collinear(assignments[a].points[x], assignments[b].points[y],
                                 assignments[c].points[z]);
        int order[6][3] = {{a,b,c},{a,c,b},{b,a,c},{b,c,a},{c,a,b},{c,b,a}};
        for (auto &p : order)
          triple_count[((size_t)p[0] * assignment_count + p[1]) * assignment_count + p[2]] = count;
      }

  int state_count = cycles.size() * Q;
  vector<uint16_t> defects(state_count);
  vector<uint32_t> pair_flaws(state_count);
  vector<uint64_t> triple_flaws(state_count);
  map<int, vector<int>> levels;
  vector<vector<int>> clean_codes(cycles.size());
  vector<int> selected(M);
  for (int cycle = 0; cycle < (int)cycles.size(); ++cycle)
    for (int code = 0; code < Q; ++code) {
      int state = cycle * Q + code;
      for (int source = 0; source < M; ++source)
        selected[source] = assignment_id[source][cycles[cycle][source]][(code >> source) & 1];
      int defect = 0, pair_index = 0, triple_index = 0;
      uint32_t pair_mask = 0;
      uint64_t triple_mask = 0;
      for (int i = 0; i < M; ++i)
        for (int j = i + 1; j < M; ++j, ++pair_index) {
          int value = pair_count[selected[i] * assignment_count + selected[j]];
          defect += value;
          if (value) pair_mask |= 1u << pair_index;
        }
      for (int i = 0; i < M; ++i)
        for (int j = i + 1; j < M; ++j)
          for (int k = j + 1; k < M; ++k, ++triple_index) {
            int value = triple_count[((size_t)selected[i] * assignment_count + selected[j]) *
                                     assignment_count + selected[k]];
            defect += value;
            if (value) triple_mask |= 1ull << triple_index;
          }
      defects[state] = defect;
      pair_flaws[state] = pair_mask;
      triple_flaws[state] = triple_mask;
      levels[defect].push_back(state);
      if (!pair_mask) clean_codes[cycle].push_back(code);
    }

  const int infinity = 30000;
  vector<int16_t> distance(state_count, infinity);
  vector<int> next_state(state_count, -1);
  deque<int> queue;
  for (int state : levels[0]) {
    distance[state] = 0;
    queue.push_back(state);
  }
  auto relax_predecessors = [&](int target) {
    int next_distance = distance[target] + 1;
    int cycle = target / Q;
    int code = target % Q;
    for (int source = 0; source < M; ++source) {
      int predecessor = target ^ (1 << source);
      if ((pair_flaws[predecessor] & incident_pairs[source]) &&
          distance[predecessor] > next_distance) {
        distance[predecessor] = next_distance;
        next_state[predecessor] = target;
        queue.push_back(predecessor);
      }
    }
    for (int triple_index = 0; triple_index < 56; ++triple_index) {
      uint8_t mask = triple_masks[triple_index];
      Rho predecessor_cycle = switched(cycles[cycle], mask);
      int base = cycle_id[predecessor_cycle] * Q;
      int outside = code & ~mask;
      array<int, 3> sources{};
      int count = 0;
      for (int source = 0; source < M; ++source)
        if (mask & (1 << source)) sources[count++] = source;
      for (int old_bits = 0; old_bits < 8; ++old_bits) {
        int predecessor_code = outside;
        for (int k = 0; k < 3; ++k)
          predecessor_code |= ((old_bits >> k) & 1) << sources[k];
        int predecessor = base + predecessor_code;
        if (((triple_flaws[predecessor] >> triple_index) & 1ull) &&
            distance[predecessor] > next_distance) {
          distance[predecessor] = next_distance;
          next_state[predecessor] = target;
          queue.push_back(predecessor);
        }
      }
    }
  };
  while (!queue.empty()) {
    int target = queue.front();
    queue.pop_front();
    relax_predecessors(target);
  }

  vector<int> sharp;
  for (int state : levels[4]) if (distance[state] == 5) sharp.push_back(state);
  map<string, long long> support_type;
  map<int, long long> first_neighbour_minimum;
  map<string, long long> shortest_move_profile;
  set<int> sharp_cycles;
  set<pair<int, int>> complement_orbits;
  for (int state : sharp) {
    int cycle = state / Q, code = state % Q;
    int pair_bits = __builtin_popcount(pair_flaws[state]);
    int triple_bits = __builtin_popcountll(triple_flaws[state]);
    support_type[string("pair=") + to_string(pair_bits) + ",triple=" + to_string(triple_bits)]++;
    sharp_cycles.insert(cycle);
    complement_orbits.insert(minmax(state, cycle * Q + (code ^ (Q - 1))));

    int minimum = 1000;
    for (int source = 0; source < M; ++source)
      if (pair_flaws[state] & incident_pairs[source])
        minimum = min(minimum, (int)defects[state ^ (1 << source)]);
    for (int triple_index = 0; triple_index < 56; ++triple_index)
      if ((triple_flaws[state] >> triple_index) & 1ull) {
        uint8_t mask = triple_masks[triple_index];
        Rho target_cycle = switched(cycles[cycle], mask);
        int base = cycle_id[target_cycle] * Q;
        int outside = code & ~mask;
        array<int, 3> sources{};
        int count = 0;
        for (int source = 0; source < M; ++source)
          if (mask & (1 << source)) sources[count++] = source;
        for (int fresh = 0; fresh < 8; ++fresh) {
          int target_code = outside;
          for (int k = 0; k < 3; ++k)
            target_code |= ((fresh >> k) & 1) << sources[k];
          minimum = min(minimum, (int)defects[base + target_code]);
        }
      }
    first_neighbour_minimum[minimum]++;

    string profile;
    int current = state;
    for (int step = 0; step < 5; ++step) {
      int target = next_state[current];
      if (target < 0) return 3;
      if (step) profile += ",";
      profile += (current / Q == target / Q ? "F" : "R");
      current = target;
    }
    shortest_move_profile[profile]++;
  }

  vector<int16_t> macro_state_distance(state_count, infinity);
  vector<int16_t> macro_cycle_distance(cycles.size(), infinity);
  deque<int> cycle_queue;
  for (int state : levels[0]) {
    macro_state_distance[state] = 0;
    int cycle = state / Q;
    if (macro_cycle_distance[cycle] > 0) {
      macro_cycle_distance[cycle] = 0;
      cycle_queue.push_back(cycle);
    }
  }
  while (!cycle_queue.empty()) {
    int target_cycle = cycle_queue.front();
    cycle_queue.pop_front();
    int next_distance = macro_cycle_distance[target_cycle] + 1;
    for (int triple_index = 0; triple_index < 56; ++triple_index) {
      Rho predecessor_rho = switched(cycles[target_cycle], triple_masks[triple_index]);
      int predecessor_cycle = cycle_id[predecessor_rho];
      bool improved_cycle = false;
      for (int code : clean_codes[predecessor_cycle]) {
        int state = predecessor_cycle * Q + code;
        if (macro_state_distance[state] > next_distance &&
            (triple_flaws[state] & meeting_triples[triple_index])) {
          macro_state_distance[state] = next_distance;
          improved_cycle = true;
        }
      }
      if (improved_cycle && macro_cycle_distance[predecessor_cycle] > next_distance) {
        macro_cycle_distance[predecessor_cycle] = next_distance;
        cycle_queue.push_back(predecessor_cycle);
      }
    }
  }

  map<int, long long> macro_distance_distribution;
  map<int, long long> sharp_macro_distance;
  long long clean_states = 0, macro_unreachable = 0;
  int macro_maximum = 0;
  for (int cycle = 0; cycle < (int)cycles.size(); ++cycle)
    for (int code : clean_codes[cycle]) {
      ++clean_states;
      int state = cycle * Q + code;
      if (macro_state_distance[state] >= infinity) {
        ++macro_unreachable;
      } else {
        ++macro_distance_distribution[macro_state_distance[state]];
        macro_maximum = max(macro_maximum, (int)macro_state_distance[state]);
      }
    }
  for (int state : sharp)
    if (!pair_flaws[state]) ++sharp_macro_distance[macro_state_distance[state]];

  bool ok = state_count == 1290240 && sharp.size() == 44 && sharp_cycles.size() == 14 &&
            complement_orbits.size() == 22 &&
            support_type == map<string, long long>{{"pair=0,triple=1",32},{"pair=1,triple=0",12}} &&
            first_neighbour_minimum == map<int,long long>{{4,4},{8,8},{12,8},{16,20},{20,4}} &&
            shortest_move_profile == map<string,long long>{{"F,R,R,R,R",12},{"R,R,R,R,R",32}} &&
            clean_states == 404080 && macro_unreachable == 0 && macro_maximum == 3 &&
            macro_distance_distribution == map<int,long long>{{0,28},{1,66844},{2,303576},{3,33632}} &&
            sharp_macro_distance == map<int,long long>{{1,12},{2,4},{3,16}};
  if (!ok) {
    cerr << "verification mismatch\n";
    return 1;
  }

  cout << "{\n"
       << "  \"m\": 8,\n"
       << "  \"sharp_five_step_states\": 44,\n"
       << "  \"sharp_distinct_hamilton_cycles\": 14,\n"
       << "  \"sharp_orientation_complement_orbits\": 22,\n"
       << "  \"sharp_support_type_distribution\": ";
  print_map(support_type);
  cout << ",\n  \"sharp_minimum_first_neighbour_defect\": ";
  print_map(first_neighbour_minimum);
  cout << ",\n  \"sharp_shortest_move_profile\": ";
  print_map(shortest_move_profile);
  cout << ",\n  \"parity_clean_states\": " << clean_states
       << ",\n  \"parity_clean_macro_unreachable\": " << macro_unreachable
       << ",\n  \"parity_clean_macro_maximum_distance\": " << macro_maximum
       << ",\n  \"parity_clean_macro_distance_distribution\": ";
  print_map(macro_distance_distribution);
  cout << ",\n  \"sharp_three_owner_macro_distance_distribution\": ";
  print_map(sharp_macro_distance);
  cout << ",\n  \"verified\": true,\n"
       << "  \"asymptotic_seed_theorem_proved\": false\n"
       << "}\n";
}

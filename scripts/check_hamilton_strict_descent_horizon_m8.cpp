#include <algorithm>
#include <array>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
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
    for (int i = 0; i < M; ++i)
      rho[order[i]] = order[(i + 1) % M];
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
        Assignment assignment{{q0, q1, Point{reversal(q0.y), q0.x},
                               Point{reversal(q1.y), q1.x}}};
        assignment_id[source][target][orientation] = assignments.size();
        assignments.push_back(assignment);
      }
    }

  const int assignment_count = assignments.size();
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
      pair_count[a * assignment_count + b] =
          pair_count[b * assignment_count + a] = count;
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
        int permutations[6][3] = {{a,b,c},{a,c,b},{b,a,c},{b,c,a},{c,a,b},{c,b,a}};
        for (auto &p : permutations)
          triple_count[((size_t)p[0] * assignment_count + p[1]) * assignment_count + p[2]] = count;
      }

  const int state_count = cycles.size() * Q;
  vector<uint16_t> defects(state_count);
  vector<uint32_t> pair_flaws(state_count);
  vector<uint64_t> triple_flaws(state_count);
  map<int, vector<int>> levels;
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
    }

  const int infinity = 30000;
  vector<int16_t> distance(state_count, infinity);
  deque<int> queue;
  map<int, long long> horizon_distribution;
  map<int, map<int, long long>> by_defect_level;
  long long relaxation_count = 0;

  auto relax_predecessors = [&](int target) {
    int next_distance = distance[target] + 1;
    int cycle = target / Q;
    int code = target % Q;
    for (int source = 0; source < M; ++source) {
      int predecessor = target ^ (1 << source);
      if ((pair_flaws[predecessor] & incident_pairs[source]) &&
          distance[predecessor] > next_distance) {
        distance[predecessor] = next_distance;
        queue.push_back(predecessor);
        ++relaxation_count;
      }
    }
    for (int triple_index = 0; triple_index < (int)triple_masks.size(); ++triple_index) {
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
          queue.push_back(predecessor);
          ++relaxation_count;
        }
      }
    }
  };

  bool first_level = true;
  int maximum_horizon = 0;
  long long unreachable = 0;
  for (auto &[defect, states] : levels) {
    if (!first_level) {
      for (int state : states) {
        if (distance[state] >= infinity) {
          ++unreachable;
          continue;
        }
        ++horizon_distribution[distance[state]];
        ++by_defect_level[defect][distance[state]];
        maximum_horizon = max(maximum_horizon, (int)distance[state]);
      }
    }
    for (int state : states)
      if (distance[state] != 0) {
        distance[state] = 0;
        queue.push_back(state);
      }
    while (!queue.empty()) {
      int target = queue.front();
      queue.pop_front();
      relax_predecessors(target);
    }
    first_level = false;
  }

  const map<int, long long> expected_horizon = {
      {1, 1232660}, {2, 53444}, {3, 3616}, {4, 448}, {5, 44}};
  const map<int, long long> expected_level_four = {
      {1, 4}, {2, 32}, {3, 88}, {4, 204}, {5, 44}};
  bool high_levels_immediate = true;
  for (auto const &[defect, distribution] : by_defect_level)
    if (defect >= 40 && distribution != map<int, long long>{{1, (long long)levels[defect].size()}})
      high_levels_immediate = false;

  if (state_count != 1290240 || levels.size() != 46 || unreachable != 0 ||
      maximum_horizon != 5 || horizon_distribution != expected_horizon ||
      by_defect_level[4] != expected_level_four || !high_levels_immediate) {
    cerr << "verification mismatch\n";
    return 1;
  }

  cout << "{\n"
       << "  \"m\": 8,\n"
       << "  \"states\": " << state_count << ",\n"
       << "  \"defect_levels\": " << levels.size() << ",\n"
       << "  \"unreachable_to_strictly_lower\": " << unreachable << ",\n"
       << "  \"maximum_strict_descent_horizon\": " << maximum_horizon << ",\n"
       << "  \"relaxations\": " << relaxation_count << ",\n"
       << "  \"strict_descent_horizon_distribution\": {\"1\":1232660,\"2\":53444,\"3\":3616,\"4\":448,\"5\":44},\n"
       << "  \"minimum_positive_level_distribution\": {\"1\":4,\"2\":32,\"3\":88,\"4\":204,\"5\":44},\n"
       << "  \"every_state_with_at_least_40_triples_has_immediate_descent\": true,\n"
       << "  \"verified\": true\n"
       << "}\n";
}

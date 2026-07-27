#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

struct Point { int x, y; };
struct Assignment { int source, target, orientation; array<Point, 4> points; };

bool collinear(Point a, Point b, Point c) {
  return 1LL * (b.x - a.x) * (c.y - a.y) ==
         1LL * (b.y - a.y) * (c.x - a.x);
}

vector<vector<int>> hamilton_cycles(int m) {
  vector<int> tail;
  for (int i = 1; i < m; ++i) tail.push_back(i);
  vector<vector<int>> result;
  do {
    vector<int> order{0};
    order.insert(order.end(), tail.begin(), tail.end());
    vector<int> rho(m);
    for (int i = 0; i < m; ++i) rho[order[i]] = order[(i + 1) % m];
    result.push_back(rho);
  } while (next_permutation(tail.begin(), tail.end()));
  return result;
}

map<int, long long> expected_distribution(int m) {
  if (m == 4) return {{0,16},{4,44},{8,32},{12,4}};
  if (m == 5) return {{0,16},{4,108},{8,212},{12,152},{16,72},{20,96},{24,88},{28,20},{40,4}};
  if (m == 6) return {{4,84},{8,796},{12,1360},{16,1584},{20,1276},{24,1168},{28,584},{32,212},{36,168},{40,144},{44,184},{48,72},{52,40},{56,4},{80,4}};
  if (m == 7) return {{0,36},{4,156},{8,1304},{12,5132},{16,10820},{20,13800},{24,14504},{28,13848},{32,11224},{36,7060},{40,4412},{44,3072},{48,2452},{52,1596},{56,1004},{60,588},{64,332},{68,200},{72,68},{76,8},{80,8},{84,108},{88,220},{92,152},{96,48},{100,8}};
  if (m == 8) return {{0,28},{4,372},{8,2540},{12,13004},{16,37912},{20,78160},{24,121120},{28,153488},{32,170620},{36,165372},{40,139272},{44,105256},{48,77544},{52,57392},{56,45456},{60,35904},{64,26584},{68,19236},{72,12228},{76,7168},{80,4496},{84,3040},{88,2444},{92,2680},{96,2580},{100,1896},{104,1384},{108,740},{112,552},{116,300},{120,140},{124,112},{128,64},{132,44},{136,16},{140,100},{144,192},{148,336},{152,292},{156,120},{160,16},{164,4},{168,8},{172,12},{176,12},{184,4}};
  return {};
}

map<int, long long> expected_valid_per_cycle(int m) {
  if (m == 4) return {{0,4},{8,2}};
  if (m == 5) return {{0,22},{8,2}};
  if (m == 6) return {{0,120}};
  if (m == 7) return {{0,710},{2,8},{10,2}};
  if (m == 8) return {{0,5030},{2,6},{4,4}};
  return {};
}

struct Result {
  int m;
  long long cycles, states, valid_states, valid_cycles;
  int minimum;
  map<int, long long> distribution, valid_per_cycle;
  vector<int> first_rho, first_orientation;
};

Result audit(int m) {
  int n = 2 * m;
  auto reversal = [n](int x) { return n - 1 - x; };
  vector<Assignment> assignments;
  vector<vector<array<int,2>>> id(m, vector<array<int,2>>(m, array<int,2>{-1,-1}));
  for (int source = 0; source < m; ++source)
    for (int target = 0; target < m; ++target) if (source != target)
      for (int orientation = 0; orientation < 2; ++orientation) {
        Point q0{source, orientation ? reversal(target) : target};
        Point q1{reversal(source), orientation ? target : reversal(target)};
        Assignment assignment{source, target, orientation,
          {q0, q1, Point{reversal(q0.y), q0.x}, Point{reversal(q1.y), q1.x}}};
        id[source][target][orientation] = assignments.size();
        assignments.push_back(assignment);
      }

  int assignment_count = assignments.size();
  vector<uint8_t> pair_count(assignment_count * assignment_count, 0);
  vector<uint8_t> triple_count(assignment_count * assignment_count * assignment_count, 0);

  for (int a = 0; a < assignment_count; ++a)
    for (int b = a + 1; b < assignment_count; ++b) {
      int count = 0;
      for (int x = 0; x < 4; ++x)
        for (int y = x + 1; y < 4; ++y)
          for (int z = 0; z < 4; ++z)
            count += collinear(assignments[a].points[x], assignments[a].points[y], assignments[b].points[z]);
      for (int x = 0; x < 4; ++x)
        for (int y = x + 1; y < 4; ++y)
          for (int z = 0; z < 4; ++z)
            count += collinear(assignments[b].points[x], assignments[b].points[y], assignments[a].points[z]);
      pair_count[a * assignment_count + b] = pair_count[b * assignment_count + a] = count;
    }

  for (int a = 0; a < assignment_count; ++a)
    for (int b = a + 1; b < assignment_count; ++b)
      for (int c = b + 1; c < assignment_count; ++c) {
        int count = 0;
        for (int x = 0; x < 4; ++x)
          for (int y = 0; y < 4; ++y)
            for (int z = 0; z < 4; ++z)
              count += collinear(assignments[a].points[x], assignments[b].points[y], assignments[c].points[z]);
        int p[6][3] = {{a,b,c},{a,c,b},{b,a,c},{b,c,a},{c,a,b},{c,b,a}};
        for (auto &q : p)
          triple_count[(q[0] * assignment_count + q[1]) * assignment_count + q[2]] = count;
      }

  auto cycles = hamilton_cycles(m);
  Result result{m, (long long)cycles.size(), 0, 0, 0, 1 << 30, {}, {}, {}, {}};
  vector<int> selected(m);
  for (const auto &rho : cycles) {
    int cycle_valid = 0;
    for (int mask = 0; mask < (1 << m); ++mask) {
      for (int source = 0; source < m; ++source)
        selected[source] = id[source][rho[source]][(mask >> source) & 1];
      int defects = 0;
      for (int i = 0; i < m; ++i)
        for (int j = i + 1; j < m; ++j)
          defects += pair_count[selected[i] * assignment_count + selected[j]];
      for (int i = 0; i < m; ++i)
        for (int j = i + 1; j < m; ++j)
          for (int k = j + 1; k < m; ++k)
            defects += triple_count[(selected[i] * assignment_count + selected[j]) * assignment_count + selected[k]];
      ++result.states;
      ++result.distribution[defects];
      result.minimum = min(result.minimum, defects);
      if (defects == 0) {
        ++result.valid_states;
        ++cycle_valid;
        if (result.first_rho.empty()) {
          result.first_rho = rho;
          for (int source = 0; source < m; ++source)
            result.first_orientation.push_back((mask >> source) & 1);
        }
      }
    }
    ++result.valid_per_cycle[cycle_valid];
    if (cycle_valid) ++result.valid_cycles;
  }
  return result;
}

int main() {
  vector<Result> results;
  for (int m = 4; m <= 8; ++m) {
    Result result = audit(m);
    long long expected_states = (1LL << m);
    for (int x = 1; x < m; ++x) expected_states *= x;
    if (result.states != expected_states ||
        result.distribution != expected_distribution(m) ||
        result.valid_per_cycle != expected_valid_per_cycle(m)) {
      cerr << "verification mismatch at m=" << m << "\n";
      return 1;
    }
    for (auto [defects, count] : result.distribution)
      if (defects % 4 != 0) {
        cerr << "non-quarter-turn defect count at m=" << m << "\n";
        return 2;
      }
    results.push_back(result);
  }

  cout << "{\n  \"cases\": [\n";
  for (size_t i = 0; i < results.size(); ++i) {
    const auto &r = results[i];
    cout << "    {\"m\": " << r.m << ", \"hamilton_cycles\": " << r.cycles
         << ", \"states\": " << r.states << ", \"minimum_triples\": " << r.minimum
         << ", \"valid_states\": " << r.valid_states
         << ", \"valid_cycles\": " << r.valid_cycles << "}";
    cout << (i + 1 == results.size() ? "\n" : ",\n");
  }
  cout << "  ],\n  \"all_defect_counts_divisible_by_four\": true,\n"
       << "  \"asymptotic_seed_theorem_proved\": false\n}\n";
}

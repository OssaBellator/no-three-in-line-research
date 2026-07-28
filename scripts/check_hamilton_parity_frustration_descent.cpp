#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

struct Point {
  int x;
  int y;
};

long long cross(Point a, Point b, Point c) {
  return 1LL * (b.x - a.x) * (c.y - a.y) -
         1LL * (b.y - a.y) * (c.x - a.x);
}

array<Point, 4> orbit_block(int m, int source, int target, int orientation) {
  const int n = 2 * m;
  auto reversal = [n](int x) { return n - 1 - x; };
  Point q0{source, orientation ? reversal(target) : target};
  Point q1{reversal(source), orientation ? target : reversal(target)};
  return {q0, q1, Point{reversal(q0.y), q0.x},
          Point{reversal(q1.y), q1.x}};
}

bool two_owner_bad(int m, int sa, int ta, int ea,
                   int sb, int tb, int eb) {
  auto a = orbit_block(m, sa, ta, ea);
  auto b = orbit_block(m, sb, tb, eb);
  array<Point, 8> points{};
  for (int i = 0; i < 4; ++i) {
    points[i] = a[i];
    points[i + 4] = b[i];
  }
  for (int i = 0; i < 8; ++i)
    for (int j = i + 1; j < 8; ++j)
      for (int k = j + 1; k < 8; ++k)
        if (cross(points[i], points[j], points[k]) == 0) return true;
  return false;
}

struct RelationTable {
  int m;
  vector<int8_t> data;

  explicit RelationTable(int size) : m(size), data(m * m * m * m, 0) {
    for (int a = 0; a < m; ++a)
      for (int ta = 0; ta < m; ++ta) {
        if (ta == a) continue;
        for (int b = a + 1; b < m; ++b)
          for (int tb = 0; tb < m; ++tb) {
            if (tb == b || tb == ta) continue;
            const bool bad_equal = two_owner_bad(m, a, ta, 0, b, tb, 0);
            const bool bad_unequal = two_owner_bad(m, a, ta, 0, b, tb, 1);
            const int value = bad_equal && bad_unequal ? 3
                              : bad_equal             ? 2
                              : bad_unequal           ? 1
                                                       : 0;
            data[index(a, ta, b, tb)] = static_cast<int8_t>(value);
          }
      }
  }

  int index(int a, int ta, int b, int tb) const {
    return ((a * m + ta) * m + b) * m + tb;
  }

  int get(int a, int ta, int b, int tb) const {
    return data[index(a, ta, b, tb)];
  }
};

struct Constraint {
  int a;
  int b;
  int required_xor;
};

struct CycleInfo {
  bool pair_safe = false;
  int frustration = -1;
  vector<Constraint> constraints;
  vector<int> optimal_orientations;
};

CycleInfo classify_cycle(int m, const vector<int>& rho,
                         const RelationTable& relation) {
  CycleInfo info;
  for (int a = 0; a < m; ++a)
    for (int b = a + 1; b < m; ++b) {
      const int value = relation.get(a, rho[a], b, rho[b]);
      if (value == 3) return info;
      if (value != 0)
        info.constraints.push_back({a, b, value == 1 ? 0 : 1});
    }

  info.pair_safe = true;
  info.frustration = static_cast<int>(info.constraints.size());
  for (int orientation = 0; orientation < (1 << m); ++orientation) {
    int violated = 0;
    for (const Constraint& edge : info.constraints) {
      const int parity = ((orientation >> edge.a) & 1) ^
                         ((orientation >> edge.b) & 1);
      violated += parity != edge.required_xor;
      if (violated > info.frustration) break;
    }
    if (violated < info.frustration) {
      info.frustration = violated;
      info.optimal_orientations = {orientation};
    } else if (violated == info.frustration) {
      info.optimal_orientations.push_back(orientation);
    }
  }
  return info;
}

uint64_t encode_cycle(const vector<int>& rho) {
  uint64_t code = 0;
  for (int target : rho) code = (code << 4) | target;
  return code;
}

vector<int> switched(const vector<int>& rho, array<int, 3> sources) {
  array<int, 3> cyclic{};
  int found = 0;
  int current = *min_element(sources.begin(), sources.end());
  for (int step = 0; step < static_cast<int>(rho.size()); ++step) {
    if (current == sources[0] || current == sources[1] || current == sources[2])
      cyclic[found++] = current;
    current = rho[current];
  }
  if (found != 3) throw runtime_error("source triple not found on Hamilton cycle");
  vector<int> out = rho;
  out[cyclic[0]] = rho[cyclic[1]];
  out[cyclic[1]] = rho[cyclic[2]];
  out[cyclic[2]] = rho[cyclic[0]];
  return out;
}

struct CaseResult {
  long long hamilton_cycles = 0;
  long long pair_safe_cycles = 0;
  long long positive_frustration_cycles = 0;
  long long pair_safe_successor_rotations = 0;
  long long strict_descent_rotations = 0;
  long long optimal_violated_edge_checks = 0;
  int maximum_strict_descent_horizon = 0;
  int minimum_descent_rotations_per_positive_cycle = 0;
  int minimum_descent_rotations_hitting_each_optimal_violated_edge = 0;
};

CaseResult run_case(int m) {
  const RelationTable relation(m);
  vector<vector<int>> cycles;
  vector<int> tail(m - 1);
  iota(tail.begin(), tail.end(), 1);
  do {
    vector<int> order(m);
    order[0] = 0;
    for (int i = 1; i < m; ++i) order[i] = tail[i - 1];
    vector<int> rho(m);
    for (int i = 0; i < m; ++i)
      rho[order[i]] = order[(i + 1) % m];
    cycles.push_back(move(rho));
  } while (next_permutation(tail.begin(), tail.end()));

  unordered_map<uint64_t, int> index;
  index.reserve(2 * cycles.size());
  for (int i = 0; i < static_cast<int>(cycles.size()); ++i)
    index[encode_cycle(cycles[i])] = i;

  vector<CycleInfo> info;
  info.reserve(cycles.size());
  for (const auto& rho : cycles) info.push_back(classify_cycle(m, rho, relation));

  vector<array<int, 3>> triples;
  for (int a = 0; a < m; ++a)
    for (int b = a + 1; b < m; ++b)
      for (int c = b + 1; c < m; ++c) triples.push_back({a, b, c});

  CaseResult result;
  result.hamilton_cycles = cycles.size();
  result.minimum_descent_rotations_per_positive_cycle = 1 << 30;
  result.minimum_descent_rotations_hitting_each_optimal_violated_edge = 1 << 30;

  for (int source = 0; source < static_cast<int>(cycles.size()); ++source) {
    if (!info[source].pair_safe) continue;
    ++result.pair_safe_cycles;

    vector<array<int, 3>> descent_triples;
    for (array<int, 3> triple : triples) {
      const int target = index.at(encode_cycle(switched(cycles[source], triple)));
      if (!info[target].pair_safe) continue;
      ++result.pair_safe_successor_rotations;
      if (info[target].frustration < info[source].frustration) {
        ++result.strict_descent_rotations;
        descent_triples.push_back(triple);
      }
    }

    if (info[source].frustration == 0) continue;
    ++result.positive_frustration_cycles;
    if (descent_triples.empty()) {
      cerr << "no one-step frustration descent at m=" << m
           << " cycle index=" << source << '\n';
      exit(1);
    }
    result.maximum_strict_descent_horizon = 1;
    result.minimum_descent_rotations_per_positive_cycle = min(
        result.minimum_descent_rotations_per_positive_cycle,
        static_cast<int>(descent_triples.size()));

    for (int orientation : info[source].optimal_orientations)
      for (const Constraint& edge : info[source].constraints) {
        const int parity = ((orientation >> edge.a) & 1) ^
                           ((orientation >> edge.b) & 1);
        if (parity == edge.required_xor) continue;
        ++result.optimal_violated_edge_checks;
        int hitting = 0;
        for (array<int, 3> triple : descent_triples)
          if (triple[0] == edge.a || triple[1] == edge.a ||
              triple[2] == edge.a || triple[0] == edge.b ||
              triple[1] == edge.b || triple[2] == edge.b)
            ++hitting;
        if (hitting == 0) {
          cerr << "no targeted frustration descent at m=" << m
               << " cycle index=" << source << '\n';
          exit(2);
        }
        result.minimum_descent_rotations_hitting_each_optimal_violated_edge = min(
            result.minimum_descent_rotations_hitting_each_optimal_violated_edge,
            hitting);
      }
  }

  return result;
}

const vector<CaseResult> expected = {
    {24, 24, 2, 240, 20, 48, 1, 10, 9},
    {120, 120, 8, 2400, 148, 272, 1, 18, 14},
    {720, 720, 56, 25200, 1624, 2752, 1, 25, 20},
    {5040, 4560, 1018, 239040, 34102, 97224, 1, 19, 13},
    {40320, 37440, 5752, 3009600, 292584, 1001344, 1, 28, 19},
};

bool equal_case(const CaseResult& a, const CaseResult& b) {
  return tie(a.hamilton_cycles, a.pair_safe_cycles,
             a.positive_frustration_cycles,
             a.pair_safe_successor_rotations, a.strict_descent_rotations,
             a.optimal_violated_edge_checks,
             a.maximum_strict_descent_horizon,
             a.minimum_descent_rotations_per_positive_cycle,
             a.minimum_descent_rotations_hitting_each_optimal_violated_edge) ==
         tie(b.hamilton_cycles, b.pair_safe_cycles,
             b.positive_frustration_cycles,
             b.pair_safe_successor_rotations, b.strict_descent_rotations,
             b.optimal_violated_edge_checks,
             b.maximum_strict_descent_horizon,
             b.minimum_descent_rotations_per_positive_cycle,
             b.minimum_descent_rotations_hitting_each_optimal_violated_edge);
}

int main() {
  vector<CaseResult> cases;
  for (int m = 5; m <= 9; ++m) {
    CaseResult result = run_case(m);
    if (!equal_case(result, expected[m - 5])) {
      cerr << "frustration-descent ledger mismatch at m=" << m << '\n';
      return 3;
    }
    cases.push_back(result);
  }

  cout << "{\n"
       << "  \"minimum_pair_size\": 5,\n"
       << "  \"maximum_pair_size\": 9,\n"
       << "  \"cases\": [\n";
  for (int i = 0; i < static_cast<int>(cases.size()); ++i) {
    const CaseResult& result = cases[i];
    cout << "    {\n"
         << "      \"m\": " << i + 5 << ",\n"
         << "      \"hamilton_cycles\": " << result.hamilton_cycles << ",\n"
         << "      \"pair_safe_cycles\": " << result.pair_safe_cycles << ",\n"
         << "      \"positive_frustration_cycles\": "
         << result.positive_frustration_cycles << ",\n"
         << "      \"pair_safe_successor_rotations\": "
         << result.pair_safe_successor_rotations << ",\n"
         << "      \"strict_descent_rotations\": "
         << result.strict_descent_rotations << ",\n"
         << "      \"optimal_violated_edge_checks\": "
         << result.optimal_violated_edge_checks << ",\n"
         << "      \"maximum_strict_descent_horizon\": "
         << result.maximum_strict_descent_horizon << ",\n"
         << "      \"minimum_descent_rotations_per_positive_cycle\": "
         << result.minimum_descent_rotations_per_positive_cycle << ",\n"
         << "      \"minimum_descent_rotations_hitting_each_optimal_violated_edge\": "
         << result.minimum_descent_rotations_hitting_each_optimal_violated_edge
         << "\n    }" << (i + 1 == static_cast<int>(cases.size()) ? "\n" : ",\n");
  }
  cout << "  ],\n"
       << "  \"one_step_pair_safe_frustration_descent_verified\": true,\n"
       << "  \"targeted_optimal_violated_edge_descent_verified\": true,\n"
       << "  \"asymptotic_descent_theorem_proved\": false\n"
       << "}\n";
}

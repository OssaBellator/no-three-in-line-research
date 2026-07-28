#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <tuple>
#include <unordered_map>
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

bool is_optimal(const CycleInfo& info, int orientation) {
  return binary_search(info.optimal_orientations.begin(),
                       info.optimal_orientations.end(), orientation);
}

bool violates(const Constraint& edge, int orientation) {
  const int parity = ((orientation >> edge.a) & 1) ^
                     ((orientation >> edge.b) & 1);
  return parity != edge.required_xor;
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

bool triple_meets(array<int, 3> triple, int a, int b) {
  return triple[0] == a || triple[1] == a || triple[2] == a ||
         triple[0] == b || triple[1] == b || triple[2] == b;
}

bool target_clears_edge(const RelationTable& relation,
                        const vector<int>& target_cycle,
                        const Constraint& source_edge,
                        int orientation) {
  const int value = relation.get(source_edge.a, target_cycle[source_edge.a],
                                 source_edge.b, target_cycle[source_edge.b]);
  if (value == 0) return true;
  if (value == 3) return false;
  const int required = value == 1 ? 0 : 1;
  const int parity = ((orientation >> source_edge.a) & 1) ^
                     ((orientation >> source_edge.b) & 1);
  return parity == required;
}

struct CaseResult {
  long long hamilton_cycles = 0;
  long long pair_safe_cycles = 0;
  long long positive_frustration_cycles = 0;
  long long optimal_oriented_states = 0;
  long long optimal_violated_edge_checks = 0;
  long long sign_preserving_descent_transitions = 0;
  long long targeted_sign_preserving_descent_transitions = 0;
  long long clearing_sign_preserving_descent_transitions = 0;
  int minimum_sign_preserving_descents_per_optimal_state = 0;
  int minimum_targeted_sign_preserving_descents_per_violated_edge = 0;
  int minimum_clearing_sign_preserving_descents_per_violated_edge = 0;
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
  result.minimum_sign_preserving_descents_per_optimal_state = 1 << 30;
  result.minimum_targeted_sign_preserving_descents_per_violated_edge = 1 << 30;
  result.minimum_clearing_sign_preserving_descents_per_violated_edge = 1 << 30;

  for (int source = 0; source < static_cast<int>(cycles.size()); ++source) {
    if (!info[source].pair_safe) continue;
    ++result.pair_safe_cycles;
    if (info[source].frustration == 0) continue;
    ++result.positive_frustration_cycles;

    vector<pair<array<int, 3>, int>> descent;
    for (array<int, 3> triple : triples) {
      const int target = index.at(encode_cycle(switched(cycles[source], triple)));
      if (info[target].pair_safe &&
          info[target].frustration < info[source].frustration)
        descent.push_back({triple, target});
    }

    for (int orientation : info[source].optimal_orientations) {
      ++result.optimal_oriented_states;
      int preserving = 0;
      for (auto [triple, target] : descent) {
        (void)triple;
        if (is_optimal(info[target], orientation)) {
          ++preserving;
          ++result.sign_preserving_descent_transitions;
        }
      }
      if (preserving == 0) {
        cerr << "no sign-preserving descent at m=" << m
             << " cycle index=" << source << '\n';
        exit(1);
      }
      result.minimum_sign_preserving_descents_per_optimal_state = min(
          result.minimum_sign_preserving_descents_per_optimal_state, preserving);

      for (const Constraint& edge : info[source].constraints) {
        if (!violates(edge, orientation)) continue;
        ++result.optimal_violated_edge_checks;
        int targeted = 0;
        int clearing = 0;
        for (auto [triple, target] : descent) {
          if (!triple_meets(triple, edge.a, edge.b)) continue;
          if (!is_optimal(info[target], orientation)) continue;
          ++targeted;
          ++result.targeted_sign_preserving_descent_transitions;
          if (target_clears_edge(relation, cycles[target], edge, orientation)) {
            ++clearing;
            ++result.clearing_sign_preserving_descent_transitions;
          }
        }
        if (targeted == 0 || clearing == 0) {
          cerr << "no targeted clearing sign-preserving descent at m=" << m
               << " cycle index=" << source << '\n';
          exit(2);
        }
        result.minimum_targeted_sign_preserving_descents_per_violated_edge = min(
            result.minimum_targeted_sign_preserving_descents_per_violated_edge,
            targeted);
        result.minimum_clearing_sign_preserving_descents_per_violated_edge = min(
            result.minimum_clearing_sign_preserving_descents_per_violated_edge,
            clearing);
      }
    }
  }
  return result;
}

const vector<CaseResult> expected = {
    {24, 24, 2, 48, 48, 244, 244, 244, 3, 3, 3},
    {120, 120, 8, 272, 272, 2596, 2596, 2596, 5, 5, 5},
    {720, 720, 56, 2752, 2752, 37020, 37020, 37020, 6, 6, 6},
    {5040, 4560, 1018, 93980, 97224, 1642058, 1681654, 1680944, 5, 5, 5},
    {40320, 37440, 5752, 977312, 1001344, 24730616, 25074724,
     25068372, 4, 4, 4},
};

bool equal_case(const CaseResult& a, const CaseResult& b) {
  return tie(a.hamilton_cycles, a.pair_safe_cycles,
             a.positive_frustration_cycles, a.optimal_oriented_states,
             a.optimal_violated_edge_checks,
             a.sign_preserving_descent_transitions,
             a.targeted_sign_preserving_descent_transitions,
             a.clearing_sign_preserving_descent_transitions,
             a.minimum_sign_preserving_descents_per_optimal_state,
             a.minimum_targeted_sign_preserving_descents_per_violated_edge,
             a.minimum_clearing_sign_preserving_descents_per_violated_edge) ==
         tie(b.hamilton_cycles, b.pair_safe_cycles,
             b.positive_frustration_cycles, b.optimal_oriented_states,
             b.optimal_violated_edge_checks,
             b.sign_preserving_descent_transitions,
             b.targeted_sign_preserving_descent_transitions,
             b.clearing_sign_preserving_descent_transitions,
             b.minimum_sign_preserving_descents_per_optimal_state,
             b.minimum_targeted_sign_preserving_descents_per_violated_edge,
             b.minimum_clearing_sign_preserving_descents_per_violated_edge);
}

int main() {
  vector<CaseResult> cases;
  for (int m = 5; m <= 9; ++m) {
    CaseResult result = run_case(m);
    if (!equal_case(result, expected[m - 5])) {
      cerr << "sign-preserving frustration-descent ledger mismatch at m="
           << m << '\n';
      return 3;
    }
    cases.push_back(result);
  }

  cout << "{\n"
       << "  \"minimum_pair_size\": 5,\n"
       << "  \"maximum_pair_size\": 9,\n"
       << "  \"cases\": [\n";
  for (int i = 0; i < static_cast<int>(cases.size()); ++i) {
    const CaseResult& r = cases[i];
    cout << "    {\n"
         << "      \"m\": " << i + 5 << ",\n"
         << "      \"hamilton_cycles\": " << r.hamilton_cycles << ",\n"
         << "      \"pair_safe_cycles\": " << r.pair_safe_cycles << ",\n"
         << "      \"positive_frustration_cycles\": "
         << r.positive_frustration_cycles << ",\n"
         << "      \"optimal_oriented_states\": "
         << r.optimal_oriented_states << ",\n"
         << "      \"optimal_violated_edge_checks\": "
         << r.optimal_violated_edge_checks << ",\n"
         << "      \"sign_preserving_descent_transitions\": "
         << r.sign_preserving_descent_transitions << ",\n"
         << "      \"targeted_sign_preserving_descent_transitions\": "
         << r.targeted_sign_preserving_descent_transitions << ",\n"
         << "      \"clearing_sign_preserving_descent_transitions\": "
         << r.clearing_sign_preserving_descent_transitions << ",\n"
         << "      \"minimum_sign_preserving_descents_per_optimal_state\": "
         << r.minimum_sign_preserving_descents_per_optimal_state << ",\n"
         << "      \"minimum_targeted_sign_preserving_descents_per_violated_edge\": "
         << r.minimum_targeted_sign_preserving_descents_per_violated_edge << ",\n"
         << "      \"minimum_clearing_sign_preserving_descents_per_violated_edge\": "
         << r.minimum_clearing_sign_preserving_descents_per_violated_edge
         << "\n    }"
         << (i + 1 == static_cast<int>(cases.size()) ? "\n" : ",\n");
  }
  cout << "  ],\n"
       << "  \"identical_orientation_strict_descent_verified\": true,\n"
       << "  \"every_optimal_violated_edge_has_clearing_descent_verified\": true,\n"
       << "  \"maximum_orientation_hamming_change\": 0,\n"
       << "  \"asymptotic_sign_preserving_descent_theorem_proved\": false\n"
       << "}\n";
}

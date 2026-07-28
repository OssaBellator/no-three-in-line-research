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

int two_owner_atomic_count(int m, int sa, int ta, int ea,
                           int sb, int tb, int eb) {
  auto a = orbit_block(m, sa, ta, ea);
  auto b = orbit_block(m, sb, tb, eb);
  array<Point, 8> points{};
  array<int, 8> owner{};
  for (int i = 0; i < 4; ++i) {
    points[i] = a[i];
    points[i + 4] = b[i];
    owner[i] = 0;
    owner[i + 4] = 1;
  }
  int count = 0;
  for (int i = 0; i < 8; ++i)
    for (int j = i + 1; j < 8; ++j)
      for (int k = j + 1; k < 8; ++k) {
        if (owner[i] == owner[j] && owner[j] == owner[k]) continue;
        count += cross(points[i], points[j], points[k]) == 0;
      }
  return count;
}

int three_owner_atomic_count(int m, int sa, int ta, int ea,
                             int sb, int tb, int eb,
                             int sc, int tc, int ec) {
  auto a = orbit_block(m, sa, ta, ea);
  auto b = orbit_block(m, sb, tb, eb);
  auto c = orbit_block(m, sc, tc, ec);
  int count = 0;
  for (Point x : a)
    for (Point y : b)
      for (Point z : c) count += cross(x, y, z) == 0;
  return count;
}

struct GeometryTable {
  int m;
  size_t six_size;
  vector<int8_t> relation;
  vector<uint8_t> pair_count;
  vector<uint8_t> triple_count;

  explicit GeometryTable(int size)
      : m(size),
        six_size(static_cast<size_t>(m) * m * m * m * m * m),
        relation(static_cast<size_t>(m) * m * m * m, 0),
        pair_count(static_cast<size_t>(m) * m * m * m * 4, 0),
        triple_count(six_size * 8, 0) {
    for (int a = 0; a < m; ++a)
      for (int ta = 0; ta < m; ++ta) {
        if (ta == a) continue;
        for (int b = a + 1; b < m; ++b)
          for (int tb = 0; tb < m; ++tb) {
            if (tb == b || tb == ta) continue;
            const size_t id = index4(a, ta, b, tb);
            for (int ea = 0; ea < 2; ++ea)
              for (int eb = 0; eb < 2; ++eb)
                pair_count[id * 4 + ea * 2 + eb] =
                    static_cast<uint8_t>(two_owner_atomic_count(
                        m, a, ta, ea, b, tb, eb));
            const bool bad_equal = pair_count[id * 4] > 0;
            const bool bad_unequal = pair_count[id * 4 + 1] > 0;
            relation[id] = bad_equal && bad_unequal ? 3
                           : bad_equal             ? 2
                           : bad_unequal           ? 1
                                                    : 0;
          }
      }

    for (int a = 0; a < m; ++a)
      for (int ta = 0; ta < m; ++ta) {
        if (ta == a) continue;
        for (int b = a + 1; b < m; ++b)
          for (int tb = 0; tb < m; ++tb) {
            if (tb == b || tb == ta) continue;
            for (int c = b + 1; c < m; ++c)
              for (int tc = 0; tc < m; ++tc) {
                if (tc == c || tc == ta || tc == tb) continue;
                const size_t id = index6(a, ta, b, tb, c, tc);
                for (int mask = 0; mask < 8; ++mask)
                  triple_count[id * 8 + mask] =
                      static_cast<uint8_t>(three_owner_atomic_count(
                          m, a, ta, mask & 1,
                          b, tb, (mask >> 1) & 1,
                          c, tc, (mask >> 2) & 1));
              }
          }
      }
  }

  size_t index4(int a, int ta, int b, int tb) const {
    return ((static_cast<size_t>(a) * m + ta) * m + b) * m + tb;
  }

  size_t index6(int a, int ta, int b, int tb, int c, int tc) const {
    return (((((static_cast<size_t>(a) * m + ta) * m + b) * m + tb) * m + c) *
            m + tc);
  }

  int get_relation(int a, int ta, int b, int tb) const {
    return relation[index4(a, ta, b, tb)];
  }

  int get_pair_count(int a, int ta, int ea,
                     int b, int tb, int eb) const {
    return pair_count[index4(a, ta, b, tb) * 4 + ea * 2 + eb];
  }

  int get_triple_count(int a, int ta, int ea,
                       int b, int tb, int eb,
                       int c, int tc, int ec) const {
    return triple_count[index6(a, ta, b, tb, c, tc) * 8 +
                        ea + 2 * eb + 4 * ec];
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
                         const GeometryTable& geometry) {
  CycleInfo info;
  for (int a = 0; a < m; ++a)
    for (int b = a + 1; b < m; ++b) {
      const int value = geometry.get_relation(a, rho[a], b, rho[b]);
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

bool target_clears_edge(const GeometryTable& geometry,
                        const vector<int>& target_cycle,
                        const Constraint& source_edge,
                        int orientation) {
  const int value = geometry.get_relation(
      source_edge.a, target_cycle[source_edge.a],
      source_edge.b, target_cycle[source_edge.b]);
  if (value == 0) return true;
  if (value == 3) return false;
  const int required = value == 1 ? 0 : 1;
  const int parity = ((orientation >> source_edge.a) & 1) ^
                     ((orientation >> source_edge.b) & 1);
  return parity == required;
}

int exact_z2(int m, const vector<int>& rho, int orientation,
             const GeometryTable& geometry) {
  int count = 0;
  for (int a = 0; a < m; ++a)
    for (int b = a + 1; b < m; ++b)
      count += geometry.get_pair_count(
          a, rho[a], (orientation >> a) & 1,
          b, rho[b], (orientation >> b) & 1);
  return count;
}

int exact_z3(int m, const vector<int>& rho, int orientation,
             const GeometryTable& geometry) {
  int count = 0;
  for (int a = 0; a < m; ++a)
    for (int b = a + 1; b < m; ++b)
      for (int c = b + 1; c < m; ++c)
        count += geometry.get_triple_count(
            a, rho[a], (orientation >> a) & 1,
            b, rho[b], (orientation >> b) & 1,
            c, rho[c], (orientation >> c) & 1);
  return count;
}

struct CaseResult {
  long long optimal_oriented_states = 0;
  long long optimal_violated_edge_checks = 0;
  long long z2_descent_transitions = 0;
  long long targeted_clearing_z2_descent_transitions = 0;
  int minimum_z2_descents_per_optimal_state = 0;
  int minimum_targeted_clearing_z2_descents_per_violated_edge = 0;
  long long states_without_z3_strict_descent = 0;
  long long states_without_z3_nonincrease = 0;
  long long states_without_total_atomic_descent = 0;
  long long violated_edges_without_targeted_total_atomic_descent = 0;
  long long total_atomic_descent_transitions = 0;
  long long targeted_total_atomic_descent_transitions = 0;
  int minimum_total_atomic_descents_when_nonempty = 0;
  int minimum_targeted_total_atomic_descents_when_nonempty = 0;
};

CaseResult run_case(int m) {
  const GeometryTable geometry(m);
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
  for (const auto& rho : cycles) info.push_back(classify_cycle(m, rho, geometry));

  vector<array<int, 3>> triples;
  for (int a = 0; a < m; ++a)
    for (int b = a + 1; b < m; ++b)
      for (int c = b + 1; c < m; ++c) triples.push_back({a, b, c});

  const int orientation_count = 1 << m;
  vector<int16_t> z2_cache(cycles.size() * orientation_count, -1);
  vector<int16_t> z3_cache(cycles.size() * orientation_count, -1);
  auto z2 = [&](int cycle, int orientation) {
    int16_t& value = z2_cache[static_cast<size_t>(cycle) * orientation_count +
                              orientation];
    if (value < 0) value = exact_z2(m, cycles[cycle], orientation, geometry);
    return static_cast<int>(value);
  };
  auto z3 = [&](int cycle, int orientation) {
    int16_t& value = z3_cache[static_cast<size_t>(cycle) * orientation_count +
                              orientation];
    if (value < 0) value = exact_z3(m, cycles[cycle], orientation, geometry);
    return static_cast<int>(value);
  };

  CaseResult result;
  result.minimum_z2_descents_per_optimal_state = 1 << 30;
  result.minimum_targeted_clearing_z2_descents_per_violated_edge = 1 << 30;
  result.minimum_total_atomic_descents_when_nonempty = 1 << 30;
  result.minimum_targeted_total_atomic_descents_when_nonempty = 1 << 30;

  for (int source = 0; source < static_cast<int>(cycles.size()); ++source) {
    if (!info[source].pair_safe || info[source].frustration == 0) continue;

    vector<pair<array<int, 3>, int>> descent;
    for (array<int, 3> triple : triples) {
      const int target = index.at(encode_cycle(switched(cycles[source], triple)));
      if (info[target].pair_safe &&
          info[target].frustration < info[source].frustration)
        descent.push_back({triple, target});
    }

    for (int orientation : info[source].optimal_orientations) {
      ++result.optimal_oriented_states;
      const int source_z2 = z2(source, orientation);
      const int source_z3 = z3(source, orientation);
      int z2_choices = 0;
      int z3_strict_choices = 0;
      int z3_nonincrease_choices = 0;
      int total_choices = 0;

      for (auto [triple, target] : descent) {
        (void)triple;
        if (!is_optimal(info[target], orientation)) continue;
        const int target_z2 = z2(target, orientation);
        const int target_z3 = z3(target, orientation);
        if (target_z2 < source_z2) {
          ++z2_choices;
          ++result.z2_descent_transitions;
        }
        if (target_z3 < source_z3) ++z3_strict_choices;
        if (target_z3 <= source_z3) ++z3_nonincrease_choices;
        if (target_z2 + target_z3 < source_z2 + source_z3) {
          ++total_choices;
          ++result.total_atomic_descent_transitions;
        }
      }

      if (z2_choices == 0) {
        cerr << "no exact two-owner atomic descent at m=" << m << '\n';
        exit(1);
      }
      result.minimum_z2_descents_per_optimal_state = min(
          result.minimum_z2_descents_per_optimal_state, z2_choices);
      result.states_without_z3_strict_descent += z3_strict_choices == 0;
      result.states_without_z3_nonincrease += z3_nonincrease_choices == 0;
      result.states_without_total_atomic_descent += total_choices == 0;
      if (total_choices > 0)
        result.minimum_total_atomic_descents_when_nonempty = min(
            result.minimum_total_atomic_descents_when_nonempty, total_choices);

      for (const Constraint& edge : info[source].constraints) {
        if (!violates(edge, orientation)) continue;
        ++result.optimal_violated_edge_checks;
        int clearing_z2_choices = 0;
        int clearing_total_choices = 0;
        for (auto [triple, target] : descent) {
          if (!triple_meets(triple, edge.a, edge.b)) continue;
          if (!is_optimal(info[target], orientation)) continue;
          if (!target_clears_edge(geometry, cycles[target], edge, orientation))
            continue;
          const int target_z2 = z2(target, orientation);
          const int target_z3 = z3(target, orientation);
          if (target_z2 < source_z2) {
            ++clearing_z2_choices;
            ++result.targeted_clearing_z2_descent_transitions;
          }
          if (target_z2 + target_z3 < source_z2 + source_z3) {
            ++clearing_total_choices;
            ++result.targeted_total_atomic_descent_transitions;
          }
        }
        if (clearing_z2_choices == 0) {
          cerr << "no targeted exact two-owner atomic descent at m=" << m
               << '\n';
          exit(2);
        }
        result.minimum_targeted_clearing_z2_descents_per_violated_edge = min(
            result.minimum_targeted_clearing_z2_descents_per_violated_edge,
            clearing_z2_choices);
        result.violated_edges_without_targeted_total_atomic_descent +=
            clearing_total_choices == 0;
        if (clearing_total_choices > 0)
          result.minimum_targeted_total_atomic_descents_when_nonempty = min(
              result.minimum_targeted_total_atomic_descents_when_nonempty,
              clearing_total_choices);
      }
    }
  }
  return result;
}

const vector<CaseResult> expected = {
    {48, 48, 244, 244, 3, 3, 30, 20, 14, 14, 92, 92, 1, 1},
    {272, 272, 2596, 2596, 5, 5, 24, 0, 0, 0, 1698, 1698, 1, 1},
    {2752, 2752, 37020, 37020, 6, 6, 460, 174, 170, 170,
     17042, 17042, 1, 1},
    {93980, 97224, 1639152, 1675180, 5, 5, 15360, 6182, 4308, 4482,
     714424, 733614, 1, 1},
    {977312, 1001344, 24714106, 25035496, 4, 4, 91208, 34388, 26164,
     26760, 10963384, 11134050, 1, 1},
};

bool equal_case(const CaseResult& a, const CaseResult& b) {
  return tie(a.optimal_oriented_states, a.optimal_violated_edge_checks,
             a.z2_descent_transitions,
             a.targeted_clearing_z2_descent_transitions,
             a.minimum_z2_descents_per_optimal_state,
             a.minimum_targeted_clearing_z2_descents_per_violated_edge,
             a.states_without_z3_strict_descent,
             a.states_without_z3_nonincrease,
             a.states_without_total_atomic_descent,
             a.violated_edges_without_targeted_total_atomic_descent,
             a.total_atomic_descent_transitions,
             a.targeted_total_atomic_descent_transitions,
             a.minimum_total_atomic_descents_when_nonempty,
             a.minimum_targeted_total_atomic_descents_when_nonempty) ==
         tie(b.optimal_oriented_states, b.optimal_violated_edge_checks,
             b.z2_descent_transitions,
             b.targeted_clearing_z2_descent_transitions,
             b.minimum_z2_descents_per_optimal_state,
             b.minimum_targeted_clearing_z2_descents_per_violated_edge,
             b.states_without_z3_strict_descent,
             b.states_without_z3_nonincrease,
             b.states_without_total_atomic_descent,
             b.violated_edges_without_targeted_total_atomic_descent,
             b.total_atomic_descent_transitions,
             b.targeted_total_atomic_descent_transitions,
             b.minimum_total_atomic_descents_when_nonempty,
             b.minimum_targeted_total_atomic_descents_when_nonempty);
}

int main() {
  vector<CaseResult> cases;
  for (int m = 5; m <= 9; ++m) {
    CaseResult result = run_case(m);
    if (!equal_case(result, expected[m - 5])) {
      cerr << "atomic collateral ledger mismatch at m=" << m << '\n';
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
         << "      \"optimal_oriented_states\": "
         << r.optimal_oriented_states << ",\n"
         << "      \"optimal_violated_edge_checks\": "
         << r.optimal_violated_edge_checks << ",\n"
         << "      \"z2_descent_transitions\": "
         << r.z2_descent_transitions << ",\n"
         << "      \"targeted_clearing_z2_descent_transitions\": "
         << r.targeted_clearing_z2_descent_transitions << ",\n"
         << "      \"minimum_z2_descents_per_optimal_state\": "
         << r.minimum_z2_descents_per_optimal_state << ",\n"
         << "      \"minimum_targeted_clearing_z2_descents_per_violated_edge\": "
         << r.minimum_targeted_clearing_z2_descents_per_violated_edge << ",\n"
         << "      \"states_without_z3_strict_descent\": "
         << r.states_without_z3_strict_descent << ",\n"
         << "      \"states_without_z3_nonincrease\": "
         << r.states_without_z3_nonincrease << ",\n"
         << "      \"states_without_total_atomic_descent\": "
         << r.states_without_total_atomic_descent << ",\n"
         << "      \"violated_edges_without_targeted_total_atomic_descent\": "
         << r.violated_edges_without_targeted_total_atomic_descent << ",\n"
         << "      \"total_atomic_descent_transitions\": "
         << r.total_atomic_descent_transitions << ",\n"
         << "      \"targeted_total_atomic_descent_transitions\": "
         << r.targeted_total_atomic_descent_transitions << ",\n"
         << "      \"minimum_total_atomic_descents_when_nonempty\": "
         << r.minimum_total_atomic_descents_when_nonempty << ",\n"
         << "      \"minimum_targeted_total_atomic_descents_when_nonempty\": "
         << r.minimum_targeted_total_atomic_descents_when_nonempty
         << "\n    }"
         << (i + 1 == static_cast<int>(cases.size()) ? "\n" : ",\n");
  }
  cout << "  ],\n"
       << "  \"exact_two_owner_atomic_descent_verified\": true,\n"
       << "  \"universal_total_atomic_descent_refuted_in_audited_range\": true,\n"
       << "  \"asymptotic_atomic_descent_theorem_proved\": false\n"
       << "}\n";
}

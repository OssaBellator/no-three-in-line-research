#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
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

struct Dsu {
  vector<int> parent;

  explicit Dsu(int n) : parent(n, -1) {}

  int find(int x) {
    return parent[x] < 0 ? x : parent[x] = find(parent[x]);
  }

  void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (parent[a] > parent[b]) swap(a, b);
    parent[a] += parent[b];
    parent[b] = a;
  }
};

struct CaseResult {
  long long hamilton_cycles = 0;
  long long pair_safe_cycles = 0;
  long long parity_satisfiable_cycles = 0;
  int maximum_constraint_count = 0;
  int maximum_cyclomatic_rank = 0;
  int maximum_frustration_index = 0;
  map<int, long long> constraint_count_distribution;
  map<int, long long> cyclomatic_rank_distribution;
  map<int, long long> frustration_index_distribution;
};

CaseResult run_case(int m) {
  const RelationTable relation(m);
  vector<int> tail(m - 1);
  iota(tail.begin(), tail.end(), 1);
  CaseResult result;

  do {
    vector<int> order(m);
    order[0] = 0;
    for (int i = 1; i < m; ++i) order[i] = tail[i - 1];
    vector<int> rho(m);
    for (int i = 0; i < m; ++i)
      rho[order[i]] = order[(i + 1) % m];

    ++result.hamilton_cycles;
    struct Edge {
      int a;
      int b;
      int required_xor;
    };
    vector<Edge> edges;
    Dsu dsu(m);
    bool locally_impossible = false;

    for (int a = 0; a < m && !locally_impossible; ++a)
      for (int b = a + 1; b < m; ++b) {
        const int value = relation.get(a, rho[a], b, rho[b]);
        if (value == 3) {
          locally_impossible = true;
          break;
        }
        if (value != 0) {
          edges.push_back({a, b, value == 1 ? 0 : 1});
          dsu.unite(a, b);
        }
      }

    if (locally_impossible) continue;
    ++result.pair_safe_cycles;

    int components = 0;
    for (int vertex = 0; vertex < m; ++vertex)
      if (dsu.find(vertex) == vertex) ++components;

    const int q = static_cast<int>(edges.size());
    const int beta = q - m + components;
    int frustration = q;
    for (int orientation = 0; orientation < (1 << m); ++orientation) {
      int violated = 0;
      for (const Edge& edge : edges) {
        const int parity = ((orientation >> edge.a) & 1) ^
                           ((orientation >> edge.b) & 1);
        violated += parity != edge.required_xor;
        if (violated >= frustration) break;
      }
      frustration = min(frustration, violated);
    }

    // Satisfying a spanning forest leaves at most one possible violation per chord.
    assert(frustration <= beta);
    result.parity_satisfiable_cycles += frustration == 0;
    result.maximum_constraint_count = max(result.maximum_constraint_count, q);
    result.maximum_cyclomatic_rank = max(result.maximum_cyclomatic_rank, beta);
    result.maximum_frustration_index =
        max(result.maximum_frustration_index, frustration);
    ++result.constraint_count_distribution[q];
    ++result.cyclomatic_rank_distribution[beta];
    ++result.frustration_index_distribution[frustration];
  } while (next_permutation(tail.begin(), tail.end()));

  return result;
}

const vector<CaseResult> expected = {
    {6, 6, 6, 1, 0, 0, {{0,4},{1,2}}, {{0,6}}, {{0,6}}},
    {24, 24, 22, 3, 1, 1, {{0,6},{1,8},{2,6},{3,4}},
     {{0,22},{1,2}}, {{0,22},{1,2}}},
    {120, 120, 112, 4, 1, 1, {{0,28},{1,36},{2,32},{3,16},{4,8}},
     {{0,112},{1,8}}, {{0,112},{1,8}}},
    {720, 720, 664, 6, 2, 1,
     {{0,116},{1,206},{2,222},{3,90},{4,62},{5,16},{6,8}},
     {{0,664},{1,52},{2,4}}, {{0,664},{1,56}}},
    {5040, 4560, 3542, 10, 4, 2,
     {{0,626},{1,1244},{2,1048},{3,736},{4,398},{5,280},{6,96},
      {7,62},{8,48},{9,14},{10,8}},
     {{0,3542},{1,728},{2,214},{3,68},{4,8}},
     {{0,3542},{1,940},{2,78}}},
    {40320, 37440, 31688, 11, 4, 3,
     {{0,4988},{1,10142},{2,9316},{3,6212},{4,3316},{5,1914},
      {6,848},{7,398},{8,208},{9,76},{10,20},{11,2}},
     {{0,31688},{1,4492},{2,1022},{3,220},{4,18}},
     {{0,31688},{1,5478},{2,272},{3,2}}},
};

bool equal_case(const CaseResult& a, const CaseResult& b) {
  return a.hamilton_cycles == b.hamilton_cycles &&
         a.pair_safe_cycles == b.pair_safe_cycles &&
         a.parity_satisfiable_cycles == b.parity_satisfiable_cycles &&
         a.maximum_constraint_count == b.maximum_constraint_count &&
         a.maximum_cyclomatic_rank == b.maximum_cyclomatic_rank &&
         a.maximum_frustration_index == b.maximum_frustration_index &&
         a.constraint_count_distribution == b.constraint_count_distribution &&
         a.cyclomatic_rank_distribution == b.cyclomatic_rank_distribution &&
         a.frustration_index_distribution == b.frustration_index_distribution;
}

void print_distribution(const map<int, long long>& distribution) {
  cout << '{';
  bool first = true;
  for (auto [value, count] : distribution) {
    if (!first) cout << ", ";
    first = false;
    cout << '"' << value << "\": " << count;
  }
  cout << '}';
}

int main() {
  vector<CaseResult> cases;
  for (int m = 4; m <= 9; ++m) {
    CaseResult result = run_case(m);
    if (!equal_case(result, expected[m - 4])) {
      cerr << "frustration ledger mismatch at m=" << m << '\n';
      return 1;
    }
    cases.push_back(move(result));
  }

  cout << "{\n"
       << "  \"minimum_pair_size\": 4,\n"
       << "  \"maximum_pair_size\": 9,\n"
       << "  \"cases\": [\n";
  for (int i = 0; i < static_cast<int>(cases.size()); ++i) {
    const int m = i + 4;
    const CaseResult& result = cases[i];
    cout << "    {\n"
         << "      \"m\": " << m << ",\n"
         << "      \"hamilton_cycles\": " << result.hamilton_cycles << ",\n"
         << "      \"pair_safe_cycles\": " << result.pair_safe_cycles << ",\n"
         << "      \"parity_satisfiable_cycles\": "
         << result.parity_satisfiable_cycles << ",\n"
         << "      \"maximum_constraint_count\": "
         << result.maximum_constraint_count << ",\n"
         << "      \"maximum_cyclomatic_rank\": "
         << result.maximum_cyclomatic_rank << ",\n"
         << "      \"maximum_frustration_index\": "
         << result.maximum_frustration_index << ",\n"
         << "      \"constraint_count_distribution\": ";
    print_distribution(result.constraint_count_distribution);
    cout << ",\n      \"cyclomatic_rank_distribution\": ";
    print_distribution(result.cyclomatic_rank_distribution);
    cout << ",\n      \"frustration_index_distribution\": ";
    print_distribution(result.frustration_index_distribution);
    cout << "\n    }" << (i + 1 == static_cast<int>(cases.size()) ? "\n" : ",\n");
  }
  cout << "  ],\n"
       << "  \"forest_basis_bound_verified\": true,\n"
       << "  \"asymptotic_clean_seed_theorem_proved\": false\n"
       << "}\n";
}

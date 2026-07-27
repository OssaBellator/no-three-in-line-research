#include <algorithm>
#include <array>
#include <iostream>
#include <map>
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

bool directed_cycle_on_three_assignments(int m, int u, int v, int w) {
  const int source[3] = {u / m, v / m, w / m};
  const int target[3] = {u % m, v % m, w % m};
  for (int start = 0; start < 3; ++start) {
    int current = target[start];
    for (int step = 1; step <= 3; ++step) {
      int index = -1;
      for (int i = 0; i < 3; ++i)
        if (source[i] == current) index = i;
      if (index < 0) break;
      current = target[index];
      if (current == source[start]) return true;
    }
  }
  return false;
}

struct Result {
  long long one_xor_pairs = 0;
  long long impossible_pairs = 0;
  int maximum_constraint_degree = 0;
  long long compatible_constraint_triangles = 0;
  long long compatible_frustrated_triangles = 0;
};

Result analyse(int m) {
  const int vertex_count = m * m;
  vector<vector<pair<int, int>>> adjacency(vertex_count);
  vector<int> degree(vertex_count);
  Result result;

  for (int sa = 0; sa < m; ++sa)
    for (int ta = 0; ta < m; ++ta) {
      if (sa == ta) continue;
      for (int sb = sa + 1; sb < m; ++sb)
        for (int tb = 0; tb < m; ++tb) {
          if (sb == tb || ta == tb) continue;
          const bool equal = two_owner_bad(m, sa, ta, 0, sb, tb, 0);
          const bool unequal = two_owner_bad(m, sa, ta, 0, sb, tb, 1);
          if (equal && unequal) {
            ++result.impossible_pairs;
            continue;
          }
          if (equal == unequal) continue;
          const int u = sa * m + ta;
          const int v = sb * m + tb;
          const int required_xor = equal ? 1 : 0;
          adjacency[u].push_back({v, required_xor});
          adjacency[v].push_back({u, required_xor});
          ++degree[u];
          ++degree[v];
          ++result.one_xor_pairs;
        }
    }

  result.maximum_constraint_degree =
      *max_element(degree.begin(), degree.end());

  for (int u = 0; u < vertex_count; ++u) {
    unordered_map<int, int> forward;
    for (auto [v, parity] : adjacency[u])
      if (v > u) forward[v] = parity;
    for (auto [v, parity_uv] : adjacency[u]) {
      if (v <= u) continue;
      for (auto [w, parity_vw] : adjacency[v]) {
        if (w <= v) continue;
        auto it = forward.find(w);
        if (it == forward.end()) continue;
        if (directed_cycle_on_three_assignments(m, u, v, w)) continue;
        ++result.compatible_constraint_triangles;
        if ((parity_uv ^ parity_vw ^ it->second) != 0)
          ++result.compatible_frustrated_triangles;
      }
    }
  }
  return result;
}

int main() {
  const map<int, array<long long, 5>> expected = {
      {4,  {8,    0,  2,   0,     0}},
      {5,  {26,   0,  5,   2,     2}},
      {6,  {45,   0,  6,   2,     2}},
      {7,  {75,   0, 10,   6,     6}},
      {8,  {128,  4, 13,  58,    58}},
      {9,  {164,  4, 15,  58,    58}},
      {10, {221,  4, 19,  74,    74}},
      {20, {1648, 8, 46, 1534, 1406}},
      {30, {4453,12, 89, 4776, 4340}},
      {40, {9056,24,115,10706, 9910}},
      {50, {15875,32,143,21992,20556}},
      {60, {24404,44,168,36150,33954}}};

  cout << "{\n  \"cases\": [\n";
  bool first = true;
  for (auto const &[m, values] : expected) {
    Result result = analyse(m);
    const array<long long, 5> actual = {
        result.one_xor_pairs,
        result.impossible_pairs,
        result.maximum_constraint_degree,
        result.compatible_constraint_triangles,
        result.compatible_frustrated_triangles};
    if (actual != values) {
      cerr << "verification mismatch at m=" << m << '\n';
      return 1;
    }
    if (!first) cout << ",\n";
    first = false;
    cout << "    {\"m\": " << m
         << ", \"one_xor_pairs\": " << actual[0]
         << ", \"impossible_pairs\": " << actual[1]
         << ", \"maximum_constraint_degree\": " << actual[2]
         << ", \"compatible_constraint_triangles\": " << actual[3]
         << ", \"compatible_frustrated_triangles\": " << actual[4]
         << '}';
  }
  cout << "\n  ],\n"
       << "  \"maximum_pair_size\": 60,\n"
       << "  \"asymptotic_seed_theorem_proved\": false\n}\n";
}

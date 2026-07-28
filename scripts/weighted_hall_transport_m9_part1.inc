#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <numeric>
#include <queue>
#include <set>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;

struct Point { int x, y; };
long long cross(Point a, Point b, Point c) {
  return 1LL * (b.x - a.x) * (c.y - a.y) -
         1LL * (b.y - a.y) * (c.x - a.x);
}
array<Point, 4> orbit_block(int m, int s, int t, int e) {
  const int n = 2 * m;
  auto J = [n](int x) { return n - 1 - x; };
  Point q0{s, e ? J(t) : t};
  Point q1{J(s), e ? t : J(t)};
  return {q0, q1, Point{J(q0.y), q0.x}, Point{J(q1.y), q1.x}};
}
bool two_owner_bad(int m, int sa, int ta, int ea,
                   int sb, int tb, int eb) {
  auto a = orbit_block(m, sa, ta, ea);
  auto b = orbit_block(m, sb, tb, eb);
  array<Point, 8> p{};
  for (int i = 0; i < 4; ++i) { p[i] = a[i]; p[i + 4] = b[i]; }
  for (int i = 0; i < 8; ++i)
    for (int j = i + 1; j < 8; ++j)
      for (int k = j + 1; k < 8; ++k)
        if (cross(p[i], p[j], p[k]) == 0) return true;
  return false;
}
bool three_owner_bad(int m,
                     int a, int ta, int ea,
                     int b, int tb, int eb,
                     int c, int tc, int ec) {
  auto A = orbit_block(m, a, ta, ea);
  auto B = orbit_block(m, b, tb, eb);
  auto C = orbit_block(m, c, tc, ec);
  for (Point x : A)
    for (Point y : B)
      for (Point z : C)
        if (cross(x, y, z) == 0) return true;
  return false;
}

struct RelationTable {
  int m;
  vector<int8_t> data;
  explicit RelationTable(int size)
      : m(size), data(static_cast<size_t>(m) * m * m * m, 0) {
    for (int a = 0; a < m; ++a)
      for (int ta = 0; ta < m; ++ta) {
        if (ta == a) continue;
        for (int b = a + 1; b < m; ++b)
          for (int tb = 0; tb < m; ++tb) {
            if (tb == b || tb == ta) continue;
            const bool eq = two_owner_bad(m, a, ta, 0, b, tb, 0);
            const bool un = two_owner_bad(m, a, ta, 0, b, tb, 1);
            data[index(a, ta, b, tb)] = eq && un ? 3 : eq ? 2 : un ? 1 : 0;
          }
      }
  }
  size_t index(int a, int ta, int b, int tb) const {
    return ((static_cast<size_t>(a) * m + ta) * m + b) * m + tb;
  }
  int get(int a, int ta, int b, int tb) const {
    return data[index(a, ta, b, tb)];
  }
};

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

struct CycleInfo {
  bool clean = false;
  int components = 0;
  int fibre = 0;
  array<int8_t, 9> component{};
  array<int8_t, 9> colour{};
};

struct FlowEdge { int to, reverse; long long capacity; };
struct Dinic {
  vector<vector<FlowEdge>> graph;
  vector<int> level, next;
  explicit Dinic(int n) : graph(n), level(n), next(n) {}
  void add_edge(int from, int to, long long capacity) {
    FlowEdge a{to, static_cast<int>(graph[to].size()), capacity};
    FlowEdge b{from, static_cast<int>(graph[from].size()), 0};
    graph[from].push_back(a);
    graph[to].push_back(b);
  }
  bool bfs(int source, int sink) {
    fill(level.begin(), level.end(), -1);
    queue<int> q;
    level[source] = 0;
    q.push(source);
    while (!q.empty()) {
      int u = q.front(); q.pop();
      for (const FlowEdge& edge : graph[u])
        if (edge.capacity > 0 && level[edge.to] < 0) {
          level[edge.to] = level[u] + 1;
          q.push(edge.to);
        }
    }
    return level[sink] >= 0;
  }
  long long dfs(int u, int sink, long long pushed) {
    if (u == sink) return pushed;
    for (int& i = next[u]; i < static_cast<int>(graph[u].size()); ++i) {
      FlowEdge& edge = graph[u][i];
      if (edge.capacity > 0 && level[edge.to] == level[u] + 1) {
        long long sent = dfs(edge.to, sink, min(pushed, edge.capacity));
        if (sent > 0) {
          edge.capacity -= sent;
          graph[edge.to][edge.reverse].capacity += sent;
          return sent;
        }
      }
    }
    return 0;
  }
  long long max_flow(int source, int sink) {
    long long flow = 0;
    while (bfs(source, sink)) {
      fill(next.begin(), next.end(), 0);
      while (long long sent = dfs(source, sink, numeric_limits<long long>::max()/4))
        flow += sent;
    }
    return flow;
  }
  vector<char> source_side(int source) const {
    vector<char> seen(graph.size(), false);
    queue<int> q;
    seen[source] = true;
    q.push(source);
    while (!q.empty()) {
      int u = q.front(); q.pop();
      for (const FlowEdge& edge : graph[u])
        if (edge.capacity > 0 && !seen[edge.to]) {
          seen[edge.to] = true;
          q.push(edge.to);
        }
    }
    return seen;
  }
};

bool fraction_greater(long long a, long long b, long long c, long long d) {
  return a * d > c * b;
}
struct RatioResult {
  long long numerator = 0, denominator = 1;
  int subset_size = 0;
  long long subset_supply = 0, subset_capacity = 1;
  int conceptual_cuts = 1;
};

RatioResult optimum_ratio(const vector<int>& weights,
                          const vector<vector<int>>& neighbours,
                          const vector<int>& target_ids,
                          const vector<int>& target_capacities,
                          vector<int>& target_position) {
  const int nx = static_cast<int>(weights.size());
  const int ny = static_cast<int>(target_ids.size());
  for (int j = 0; j < ny; ++j) target_position[target_ids[j]] = j;

  long long all_supply = accumulate(weights.begin(), weights.end(), 0LL);
  long long all_capacity = accumulate(target_capacities.begin(), target_capacities.end(), 0LL);
  long long divisor = gcd(all_supply, all_capacity);
  long long p = all_supply / divisor;
  long long q = all_capacity / divisor;

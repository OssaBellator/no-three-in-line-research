#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;

constexpr int M = 7;
constexpr int N = 14;
constexpr int Q = 1 << M;
constexpr int P = N * N;
using Rho = array<uint8_t, M>;

struct StateData {
  int triples = 0;
  vector<uint8_t> owners;
};

struct ArrHash {
  size_t operator()(Rho const &a) const noexcept {
    size_t h = 0;
    for (auto x : a) h = h * 11 + x + 1;
    return h;
  }
};

struct LineKey {
  int A, B, C;
  bool operator==(LineKey const &o) const {
    return A == o.A && B == o.B && C == o.C;
  }
};

struct LineHash {
  size_t operator()(LineKey const &k) const noexcept {
    return ((uint64_t)(k.A + 30) * 1000003u) ^
           ((uint64_t)(k.B + 30) * 1009u) ^ (uint32_t)(k.C + 1000);
  }
};

LineKey normline(int a, int b) {
  int x1 = a / N, y1 = a % N, x2 = b / N, y2 = b % N;
  int A = y2 - y1, B = x1 - x2, C = -(A * x1 + B * y1);
  int g = std::gcd(std::gcd(abs(A), abs(B)), abs(C));
  A /= g;
  B /= g;
  C /= g;
  if (A < 0 || (A == 0 && B < 0)) A = -A, B = -B, C = -C;
  return {A, B, C};
}

vector<Rho> cycles() {
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

array<int, 4> orbit(int source, int target, int orientation) {
  auto J = [](int x) { return N - 1 - x; };
  array<pair<int, int>, 2> sigma{};
  sigma[0] = {source, orientation ? J(target) : target};
  sigma[1] = {J(source), orientation ? target : J(target)};
  array<int, 4> cells{};
  cells[0] = sigma[0].first * N + sigma[0].second;
  cells[1] = sigma[1].first * N + sigma[1].second;
  cells[2] = J(sigma[0].second) * N + sigma[0].first;
  cells[3] = J(sigma[1].second) * N + sigma[1].first;
  sort(cells.begin(), cells.end());
  return cells;
}

Rho switched(Rho const &rho, uint8_t mask) {
  int start = 0;
  while (!(mask & (1 << start))) ++start;
  array<int, 3> source{};
  int count = 0, current = start;
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
  vector<array<uint16_t, P>> pair_id(P);
  unordered_map<LineKey, int, LineHash> line_ids;
  vector<bitset<256>> line_points;
  for (int i = 0; i < P; ++i) {
    for (int j = i + 1; j < P; ++j) {
      auto key = normline(i, j);
      auto it = line_ids.find(key);
      int id;
      if (it == line_ids.end()) {
        id = (int)line_points.size();
        line_ids.emplace(key, id);
        line_points.emplace_back();
      } else {
        id = it->second;
      }
      pair_id[i][j] = pair_id[j][i] = id;
      line_points[id].set(i);
      line_points[id].set(j);
    }
  }

  auto rhos = cycles();
  unordered_map<Rho, int, ArrHash> rho_id;
  for (int i = 0; i < (int)rhos.size(); ++i) rho_id[rhos[i]] = i;

  array<array<array<array<int, 4>, 2>, M>, M> blocks{};
  for (int s = 0; s < M; ++s)
    for (int t = 0; t < M; ++t)
      if (s != t)
        for (int e = 0; e < 2; ++e) blocks[s][t][e] = orbit(s, t, e);

  int state_count = (int)rhos.size() * Q;
  vector<StateData> data(state_count);
  vector<uint16_t> line_pair_count(line_points.size());
  vector<int> touched;
  touched.reserve(600);
  uint64_t occurrence_two = 0, occurrence_three = 0;
  int maximum_owner_load = 0, defective = 0, only_two_owner = 0;

  for (int ri = 0; ri < (int)rhos.size(); ++ri) {
    for (int code = 0; code < Q; ++code) {
      int state = ri * Q + code;
      bitset<256> selected;
      array<int8_t, P> owner;
      owner.fill(-1);
      array<int, 4 * M> points{};
      int point_count = 0;
      for (int source = 0; source < M; ++source) {
        int sign = (code >> source) & 1;
        for (int cell : blocks[source][rhos[ri][source]][sign]) {
          selected.set(cell);
          owner[cell] = source;
          points[point_count++] = cell;
        }
      }
      sort(points.begin(), points.end());
      touched.clear();
      for (int i = 0; i < point_count; ++i) {
        for (int j = i + 1; j < point_count; ++j) {
          int line = pair_id[points[i]][points[j]];
          if (line_pair_count[line]++ == 0) touched.push_back(line);
        }
      }

      bool has_three_owner = false, has_flaw = false;
      for (int line : touched) {
        int pairs = line_pair_count[line];
        line_pair_count[line] = 0;
        if (pairs < 3) continue;
        int load = (1 + (int)sqrt(1 + 8.0 * pairs)) / 2;
        data[state].triples += load * (load - 1) * (load - 2) / 6;
        vector<int> cells;
        for (int cell = 0; cell < P; ++cell)
          if (selected.test(cell) && line_points[line].test(cell)) cells.push_back(cell);
        array<int, M> owner_load{};
        for (int cell : cells) ++owner_load[owner[cell]];
        for (int value : owner_load) maximum_owner_load = max(maximum_owner_load, value);
        for (int a = 0; a < (int)cells.size(); ++a)
          for (int b = a + 1; b < (int)cells.size(); ++b)
            for (int c = b + 1; c < (int)cells.size(); ++c) {
              uint8_t mask = (1 << owner[cells[a]]) | (1 << owner[cells[b]]) |
                             (1 << owner[cells[c]]);
              data[state].owners.push_back(mask);
              int owner_count = __builtin_popcount((unsigned)mask);
              if (owner_count == 2) {
                ++occurrence_two;
              } else if (owner_count == 3) {
                ++occurrence_three;
                has_three_owner = true;
              } else {
                cerr << "impossible owner count\n";
                return 2;
              }
              has_flaw = true;
            }
      }
      if (data[state].triples) ++defective;
      if (has_flaw && !has_three_owner) ++only_two_owner;
    }
  }

  auto neighbours = [&](int state, vector<uint32_t> &out) {
    out.clear();
    int ri = state / Q, code = state % Q;
    array<bool, 128> seen{};
    uint8_t flip_sources = 0;
    vector<uint8_t> rotations;
    for (uint8_t mask : data[state].owners) {
      if (seen[mask]) continue;
      seen[mask] = true;
      if (__builtin_popcount((unsigned)mask) == 2)
        flip_sources |= mask;
      else
        rotations.push_back(mask);
    }
    for (int source = 0; source < M; ++source)
      if (flip_sources & (1 << source)) out.push_back(state ^ (1 << source));
    for (uint8_t mask : rotations) {
      Rho changed_rho = switched(rhos[ri], mask);
      int base = rho_id[changed_rho] * Q;
      array<int, 3> sources{};
      int count = 0;
      for (int source = 0; source < M; ++source)
        if (mask & (1 << source)) sources[count++] = source;
      for (int fresh = 0; fresh < 8; ++fresh) {
        int changed_code = code;
        for (int k = 0; k < 3; ++k) {
          changed_code &= ~(1 << sources[k]);
          changed_code |= ((fresh >> k) & 1) << sources[k];
        }
        out.push_back(base + changed_code);
      }
    }
  };

  int global_minimum = 100000;
  for (auto const &state : data) global_minimum = min(global_minimum, state.triples);
  vector<int> targets;
  for (int state = 0; state < state_count; ++state)
    if (data[state].triples == global_minimum) targets.push_back(state);

  vector<uint32_t> indegree(state_count), outdegree(state_count);
  uint64_t edge_count = 0;
  vector<int> local_minima;
  vector<uint32_t> temporary;
  for (int source = 0; source < state_count; ++source) {
    neighbours(source, temporary);
    sort(temporary.begin(), temporary.end());
    temporary.erase(unique(temporary.begin(), temporary.end()), temporary.end());
    outdegree[source] = temporary.size();
    bool lower = false;
    for (uint32_t target : temporary) {
      ++indegree[target];
      ++edge_count;
      if (data[target].triples < data[source].triples) lower = true;
    }
    if (!lower && data[source].triples > global_minimum) local_minima.push_back(source);
  }

  vector<uint64_t> offset(state_count + 1), reverse_offset(state_count + 1);
  for (int state = 0; state < state_count; ++state) {
    offset[state + 1] = offset[state] + outdegree[state];
    reverse_offset[state + 1] = reverse_offset[state] + indegree[state];
  }
  vector<uint32_t> edges(edge_count), reverse_edges(edge_count);
  vector<uint64_t> cursor = reverse_offset;
  for (int source = 0; source < state_count; ++source) {
    neighbours(source, temporary);
    sort(temporary.begin(), temporary.end());
    temporary.erase(unique(temporary.begin(), temporary.end()), temporary.end());
    copy(temporary.begin(), temporary.end(), edges.begin() + offset[source]);
    for (uint32_t target : temporary) reverse_edges[cursor[target]++] = source;
  }

  vector<int16_t> distance(state_count, -1);
  deque<int> queue;
  for (int target : targets) {
    distance[target] = 0;
    queue.push_back(target);
  }
  while (!queue.empty()) {
    int target = queue.front();
    queue.pop_front();
    for (uint64_t pos = reverse_offset[target]; pos < reverse_offset[target + 1]; ++pos) {
      int source = reverse_edges[pos];
      if (distance[source] < 0) {
        distance[source] = distance[target] + 1;
        queue.push_back(source);
      }
    }
  }

  map<int, int> distance_distribution, local_distance_distribution;
  for (int value : distance) ++distance_distribution[value];
  for (int state : local_minima) ++local_distance_distribution[distance[state]];

  vector<int> mark(state_count);
  int stamp = 0;
  map<int, int> descent_horizon;
  for (int root : local_minima) {
    int baseline = data[root].triples;
    vector<int> frontier{root}, next;
    mark[root] = ++stamp;
    int found = 0;
    for (int depth = 1; depth <= 5 && !found; ++depth) {
      next.clear();
      for (int state : frontier) {
        for (uint64_t pos = offset[state]; pos < offset[state + 1]; ++pos) {
          int target = edges[pos];
          if (data[target].triples < baseline) {
            found = depth;
            break;
          }
          if (mark[target] != stamp) {
            mark[target] = stamp;
            next.push_back(target);
          }
        }
        if (found) break;
      }
      frontier.swap(next);
    }
    if (!found) {
      cerr << "descent horizon exceeds five\n";
      return 3;
    }
    ++descent_horizon[found];
  }
  descent_horizon[1] = state_count - targets.size() - local_minima.size();

  int no_move = 0;
  for (int state = 0; state < state_count; ++state)
    if (data[state].triples && outdegree[state] == 0) ++no_move;

  bool ok = state_count == 92160 && defective == 92124 && global_minimum == 0 &&
            targets.size() == 36 && occurrence_two == 344064 &&
            occurrence_three == 2219520 && only_two_owner == 56 &&
            maximum_owner_load == 2 && edge_count == 4427088 && no_move == 0 &&
            *max_element(distance.begin(), distance.end()) == 4 &&
            distance_distribution == map<int, int>{{0, 36}, {1, 1576}, {2, 31112},
                                                   {3, 58712}, {4, 724}} &&
            local_minima.size() == 6676 &&
            local_distance_distribution == map<int, int>{{2, 1344}, {3, 5060},
                                                         {4, 272}} &&
            descent_horizon == map<int, int>{{1, 85448}, {2, 5936}, {3, 692},
                                             {4, 48}};
  if (!ok) {
    cerr << "verification mismatch\n";
    return 1;
  }

  cout << "{\n"
       << "  \"m\": 7,\n"
       << "  \"states\": 92160,\n"
       << "  \"global_minimum_triples\": 0,\n"
       << "  \"global_minimum_states\": 36,\n"
       << "  \"directed_edges\": 4427088,\n"
       << "  \"maximum_distance_to_global_minimum\": 4,\n"
       << "  \"maximum_strict_descent_horizon\": 4,\n"
       << "  \"verified\": true\n"
       << "}\n";
}

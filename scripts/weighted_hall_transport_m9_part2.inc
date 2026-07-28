  int last_subset = nx;
  long long last_supply = all_supply;
  long long last_capacity = all_capacity;
  int conceptual_cuts = 1;  // the p/q=0 closure is known analytically.

  for (;;) {
    ++conceptual_cuts;
    const int source = nx + ny;
    const int sink = source + 1;
    Dinic flow(sink + 1);
    const long long infinite = numeric_limits<long long>::max()/8;
    long long total_source_capacity = 0;
    for (int i = 0; i < nx; ++i) {
      long long capacity = q * weights[i];
      flow.add_edge(source, i, capacity);
      total_source_capacity += capacity;
      for (int target : neighbours[i])
        flow.add_edge(i, nx + target_position[target], infinite);
    }
    for (int j = 0; j < ny; ++j)
      flow.add_edge(nx + j, sink, p * target_capacities[j]);

    long long gain = total_source_capacity - flow.max_flow(source, sink);
    if (gain == 0) {
      for (int target : target_ids) target_position[target] = -1;
      return {p, q, last_subset, last_supply, last_capacity, conceptual_cuts};
    }

    vector<char> side = flow.source_side(source);
    vector<char> used_target(ny, false);
    long long supply = 0, capacity = 0;
    int subset = 0;
    for (int i = 0; i < nx; ++i)
      if (side[i]) {
        supply += weights[i];
        ++subset;
        for (int target : neighbours[i]) used_target[target_position[target]] = true;
      }
    for (int j = 0; j < ny; ++j)
      if (used_target[j]) capacity += target_capacities[j];
    divisor = gcd(supply, capacity);
    p = supply / divisor;
    q = capacity / divisor;
    last_subset = subset;
    last_supply = supply;
    last_capacity = capacity;
  }
}

struct Candidate { int triple_index, ta, tb, tc, mask; };
struct Flaw { array<int,3> sources{}, targets{}, orientations{}; };
struct Audit {
  long long clean_states = 0;
  long long flaws = 0;
  long long proper = 0;
  int maximum_sources = 0;
  int maximum_cuts = 0;
  long long worst_p = 0, worst_q = 1;
  long long global_p = 0, global_q = 1;
  long long penalty_p = 1, penalty_q = 1;
  Flaw worst{};
  int worst_sources = 0, worst_subset = 0;
  long long worst_supply = 0, worst_capacity = 1;
};
void merge_audit(Audit& total, const Audit& part) {
  total.flaws += part.flaws;
  total.proper += part.proper;
  total.maximum_sources = max(total.maximum_sources, part.maximum_sources);
  total.maximum_cuts = max(total.maximum_cuts, part.maximum_cuts);
  if (fraction_greater(part.worst_p, part.worst_q, total.worst_p, total.worst_q)) {
    total.worst_p = part.worst_p; total.worst_q = part.worst_q;
    total.worst = part.worst; total.worst_sources = part.worst_sources;
    total.worst_subset = part.worst_subset;
    total.worst_supply = part.worst_supply; total.worst_capacity = part.worst_capacity;
  }
  if (fraction_greater(part.global_p, part.global_q, total.global_p, total.global_q)) {
    total.global_p = part.global_p; total.global_q = part.global_q;
  }
  if (fraction_greater(part.penalty_p, part.penalty_q, total.penalty_p, total.penalty_q)) {
    total.penalty_p = part.penalty_p; total.penalty_q = part.penalty_q;
  }
}

Audit run_case(int m) {
  RelationTable relation(m);
  vector<vector<int>> cycles;
  vector<int> tail(m - 1);
  iota(tail.begin(), tail.end(), 1);
  do {
    vector<int> order(m), rho(m);
    order[0] = 0;
    for (int i = 1; i < m; ++i) order[i] = tail[i - 1];
    for (int i = 0; i < m; ++i) rho[order[i]] = order[(i + 1) % m];
    cycles.push_back(move(rho));
  } while (next_permutation(tail.begin(), tail.end()));

  unordered_map<uint64_t, int> cycle_index;
  cycle_index.reserve(2 * cycles.size());
  for (int i = 0; i < static_cast<int>(cycles.size()); ++i)
    cycle_index[encode_cycle(cycles[i])] = i;

  vector<array<int,3>> triples;
  for (int a = 0; a < m; ++a)
    for (int b = a + 1; b < m; ++b)
      for (int c = b + 1; c < m; ++c) triples.push_back({a,b,c});
  const int triple_count = static_cast<int>(triples.size());

  vector<vector<int>> successor(cycles.size(), vector<int>(triple_count));
  for (int i = 0; i < static_cast<int>(cycles.size()); ++i)
    for (int t = 0; t < triple_count; ++t)
      successor[i][t] = cycle_index.at(encode_cycle(switched(cycles[i], triples[t])));

  vector<vector<char>> meets(triple_count, vector<char>(triple_count, false));
  for (int s = 0; s < triple_count; ++s)
    for (int t = 0; t < triple_count; ++t)
      for (int x : triples[s])
        for (int y : triples[t])
          if (x == y) meets[s][t] = true;

  vector<CycleInfo> info(cycles.size());
  Audit total;
  for (int ci = 0; ci < static_cast<int>(cycles.size()); ++ci) {
    vector<vector<pair<int,int>>> adjacency(m);
    bool impossible = false;
    for (int a = 0; a < m; ++a)
      for (int b = a + 1; b < m; ++b) {
        int value = relation.get(a, cycles[ci][a], b, cycles[ci][b]);
        if (value == 3) impossible = true;
        else if (value != 0) {
          int parity = value == 1 ? 0 : 1;
          adjacency[a].push_back({b, parity});
          adjacency[b].push_back({a, parity});
        }
      }
    if (impossible) continue;
    array<int8_t,9> component{}, colour{};
    component.fill(-1); colour.fill(-1);
    bool satisfiable = true;
    int components = 0;
    for (int root = 0; root < m; ++root)
      if (component[root] < 0) {
        vector<int> queue_vertices{root};
        component[root] = components;
        colour[root] = 0;
        for (size_t head = 0; head < queue_vertices.size(); ++head) {
          int u = queue_vertices[head];
          for (auto [v, parity] : adjacency[u]) {
            int wanted = colour[u] ^ parity;
            if (component[v] < 0) {
              component[v] = components;
              colour[v] = wanted;
              queue_vertices.push_back(v);
            } else if (colour[v] != wanted) satisfiable = false;
          }
        }
        ++components;
      }
    if (!satisfiable) continue;
    info[ci].clean = true;
    info[ci].components = components;
    info[ci].fibre = 1 << components;
    info[ci].component = component;
    info[ci].colour = colour;
    total.clean_states += info[ci].fibre;
  }

  const int key_count = triple_count * m * m * m;
  vector<vector<int>> source_lists(key_count);
  auto key = [m](int s, int ta, int tb, int tc) {
    return ((s * m + ta) * m + tb) * m + tc;
  };
  for (int ci = 0; ci < static_cast<int>(cycles.size()); ++ci)
    for (int s = 0; s < triple_count; ++s) {
      auto S = triples[s];
      source_lists[key(s, cycles[ci][S[0]], cycles[ci][S[1]], cycles[ci][S[2]])]
          .push_back(ci);
    }

  vector<Candidate> candidates;
  for (int s = 0; s < triple_count; ++s) {
    auto S = triples[s];
    for (int ta = 0; ta < m; ++ta)
      for (int tb = 0; tb < m; ++tb)
        for (int tc = 0; tc < m; ++tc) {
          if (source_lists[key(s,ta,tb,tc)].empty()) continue;
          for (int mask = 0; mask < 4; ++mask) {
            if (three_owner_bad(m,
                                S[0],ta,mask&1,
                                S[1],tb,(mask>>1)&1,
                                S[2],tc,(mask>>2)&1))
              candidates.push_back({s,ta,tb,tc,mask});
          }
        }
  }

  int thread_count = 1;
#ifdef _OPENMP
  thread_count = omp_get_max_threads();
#endif
  vector<Audit> partial(thread_count);

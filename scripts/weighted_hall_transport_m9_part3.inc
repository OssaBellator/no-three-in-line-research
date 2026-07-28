#pragma omp parallel for schedule(static)
  for (int candidate_index = 0;
       candidate_index < static_cast<int>(candidates.size());
       ++candidate_index) {
    int thread = 0;
#ifdef _OPENMP
    thread = omp_get_thread_num();
#endif
    Audit& audit = partial[thread];
    const Candidate candidate = candidates[candidate_index];
    const auto S = triples[candidate.triple_index];
    const auto& raw = source_lists[key(candidate.triple_index,
                                       candidate.ta,candidate.tb,candidate.tc)];
    vector<int> sources, weights;
    for (int cycle : raw) {
      if (!info[cycle].clean) continue;
      array<int,9> root_value{};
      root_value.fill(-1);
      bool compatible = true;
      int distinct_components = 0;
      for (int k = 0; k < 3; ++k) {
        int owner = S[k];
        int component = info[cycle].component[owner];
        int value = ((candidate.mask >> k) & 1) ^ info[cycle].colour[owner];
        if (root_value[component] < 0) {
          root_value[component] = value;
          ++distinct_components;
        } else if (root_value[component] != value) compatible = false;
      }
      if (!compatible) continue;
      sources.push_back(cycle);
      weights.push_back(1 << (info[cycle].components - distinct_components));
    }
    if (sources.empty()) continue;

    // The complementary sign mask has identical compatibility and transport.
    audit.flaws += 2;
    audit.maximum_sources = max(audit.maximum_sources,
                                static_cast<int>(sources.size()));

    vector<vector<int>> neighbours(sources.size());
    vector<int> all_targets;
    for (int i = 0; i < static_cast<int>(sources.size()); ++i) {
      vector<int> local;
      local.reserve(triple_count);
      for (int t = 0; t < triple_count; ++t)
        if (meets[candidate.triple_index][t]) {
          int target = successor[sources[i]][t];
          if (info[target].clean) local.push_back(target);
        }
      sort(local.begin(), local.end());
      local.erase(unique(local.begin(), local.end()), local.end());
      neighbours[i] = local;
      all_targets.insert(all_targets.end(), local.begin(), local.end());
    }
    sort(all_targets.begin(), all_targets.end());
    all_targets.erase(unique(all_targets.begin(), all_targets.end()), all_targets.end());
    vector<int> capacities;
    capacities.reserve(all_targets.size());
    for (int target : all_targets) capacities.push_back(info[target].fibre);

    vector<int> target_position(cycles.size(), -1);
    RatioResult ratio = optimum_ratio(weights, neighbours, all_targets,
                                       capacities, target_position);
    audit.maximum_cuts = max(audit.maximum_cuts, ratio.conceptual_cuts);

    long long global_supply = accumulate(weights.begin(), weights.end(), 0LL);
    long long global_capacity = accumulate(capacities.begin(), capacities.end(), 0LL);
    long long divisor = gcd(global_supply, global_capacity);
    long long global_p = global_supply / divisor;
    long long global_q = global_capacity / divisor;

    if (fraction_greater(ratio.numerator, ratio.denominator,
                         global_p, global_q)) {
      audit.proper += 2;
      long long penalty_p = ratio.numerator * global_q;
      long long penalty_q = ratio.denominator * global_p;
      divisor = gcd(penalty_p, penalty_q);
      penalty_p /= divisor; penalty_q /= divisor;
      if (fraction_greater(penalty_p, penalty_q,
                           audit.penalty_p, audit.penalty_q)) {
        audit.penalty_p = penalty_p; audit.penalty_q = penalty_q;
      }
    }
    if (fraction_greater(global_p, global_q,
                         audit.global_p, audit.global_q)) {
      audit.global_p = global_p; audit.global_q = global_q;
    }
    if (fraction_greater(ratio.numerator, ratio.denominator,
                         audit.worst_p, audit.worst_q)) {
      audit.worst_p = ratio.numerator; audit.worst_q = ratio.denominator;
      audit.worst.sources = S;
      audit.worst.targets = {candidate.ta,candidate.tb,candidate.tc};
      audit.worst.orientations = {candidate.mask&1,
                                  (candidate.mask>>1)&1,
                                  (candidate.mask>>2)&1};
      audit.worst_sources = sources.size();
      audit.worst_subset = ratio.subset_size;
      audit.worst_supply = ratio.subset_supply;
      audit.worst_capacity = ratio.subset_capacity;
    }
  }

  for (const Audit& part : partial) merge_audit(total, part);
  return total;
}

struct Expected {
  long long clean_states, flaws, proper;
  int maximum_sources, maximum_cuts;
  long long worst_p, worst_q, global_p, global_q, penalty_p, penalty_q;
  int worst_sources, worst_subset;
  long long worst_supply, worst_capacity;
};
const array<Expected,6> expected = {{
  {80,52,0,1,2,1,24,1,24,1,1,1,1,2,48},
  {376,368,0,1,2,1,37,1,37,1,1,1,1,4,148},
  {3576,1692,884,2,3,4,215,4,215,964,665,2,2,16,860},
  {36736,5100,4864,6,5,12,931,12,931,724,427,6,6,96,7448},
  {404080,12048,11952,24,6,1,93,265,26714,10338,4891,15,2,64,5952},
  {6727728,25540,25520,120,8,223,29271,501,66848,226808,108915,96,77,3568,468336}
}};
bool matches_expected(const Audit& a, const Expected& e) {
  return tie(a.clean_states,a.flaws,a.proper,a.maximum_sources,a.maximum_cuts,
             a.worst_p,a.worst_q,a.global_p,a.global_q,a.penalty_p,a.penalty_q,
             a.worst_sources,a.worst_subset,a.worst_supply,a.worst_capacity) ==
         tie(e.clean_states,e.flaws,e.proper,e.maximum_sources,e.maximum_cuts,
             e.worst_p,e.worst_q,e.global_p,e.global_q,e.penalty_p,e.penalty_q,
             e.worst_sources,e.worst_subset,e.worst_supply,e.worst_capacity);
}

int main(int argc, char** argv) {
  int first = 4, last = 9;
  if (argc > 1) first = last = atoi(argv[1]);
  cout << "{\n  \"cases\": [\n";
  for (int m = first; m <= last; ++m) {
    Audit audit = run_case(m);
    if (!matches_expected(audit, expected[m-4])) {
      cerr << "compressed Hall ledger mismatch at m=" << m << '\n';
      return 3;
    }
    cout << "    {\"m\":" << m
         << ",\"clean_signed_states\":" << audit.clean_states
         << ",\"atomic_signed_assignment_flaws\":" << audit.flaws
         << ",\"maximum_source_cycles_per_flaw\":" << audit.maximum_sources
         << ",\"proper_hall_bottleneck_flaws\":" << audit.proper
         << ",\"optimal_charge_numerator\":" << audit.worst_p
         << ",\"optimal_charge_denominator\":" << audit.worst_q
         << ",\"m_cubed_scaled_charge\":"
         << static_cast<double>(audit.worst_p) * m * m * m / audit.worst_q
         << ",\"global_worst_numerator\":" << audit.global_p
         << ",\"global_worst_denominator\":" << audit.global_q
         << ",\"maximum_merging_penalty_numerator\":" << audit.penalty_p
         << ",\"maximum_merging_penalty_denominator\":" << audit.penalty_q
         << ",\"maximum_dinkelbach_cuts\":" << audit.maximum_cuts
         << ",\"worst_flaw_source_owners\":["
         << audit.worst.sources[0] << ',' << audit.worst.sources[1] << ','
         << audit.worst.sources[2] << "]"
         << ",\"worst_flaw_targets\":["
         << audit.worst.targets[0] << ',' << audit.worst.targets[1] << ','
         << audit.worst.targets[2] << "]"
         << ",\"worst_flaw_orientations\":["
         << audit.worst.orientations[0] << ',' << audit.worst.orientations[1]
         << ',' << audit.worst.orientations[2] << "]"
         << ",\"worst_flaw_source_cycles\":" << audit.worst_sources
         << ",\"worst_hall_subset_size\":" << audit.worst_subset
         << ",\"worst_hall_supply\":" << audit.worst_supply
         << ",\"worst_hall_capacity\":" << audit.worst_capacity
         << "}" << (m < last ? "," : "") << "\n";
  }
  cout << "  ],\n"
       << "  \"compressed_three_arc_source_generation\": true,\n"
       << "  \"global_sign_complement_reduction\": true,\n"
       << "  \"exact_mincut_transport\": true,\n"
       << "  \"all_regression_ledgers_verified\": true,\n"
       << "  \"asymptotic_expansion_proved\": false\n"
       << "}\n";
}

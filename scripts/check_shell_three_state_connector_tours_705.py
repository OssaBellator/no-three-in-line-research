#!/usr/bin/env python3
from collections import Counter
from itertools import product

STATES = 3


def repetitions(setup, gains, burden):
    return max(
        (setup + burden[state]) // gains[state] + 1
        for state in range(STATES)
    )


def brute_repetitions(setup, gains, burden):
    count = 1
    while not all(
        count * gains[state] - burden[state] > setup
        for state in range(STATES)
    ):
        count += 1
    return count


# Each of the two directed Hamiltonian tours on three components contains three
# disjoint directed edges. Enumerate the 2^(3*3)=512 cost patterns of one tour,
# with every edge/state burden in {1,2}, and retain its burden vector and its
# edgewise-worst scalar charge.
one_tour_patterns = Counter()
for values in product((1, 2), repeat=9):
    edges = tuple(values[3 * index:3 * index + 3] for index in range(3))
    burden = tuple(
        sum(edge[state] for edge in edges)
        for state in range(STATES)
    )
    edgewise_worst = sum(max(edge) for edge in edges)
    one_tour_patterns[(burden, edgewise_worst)] += 1
assert sum(one_tour_patterns.values()) == 512

robust_gap_histogram = Counter()
robust_optimum_histogram = Counter()
statewise_lower_histogram = Counter()
edgewise_overcharge_histogram = Counter()
robust_incompatibility_cases = 0
edgewise_strict_cases = 0
burden_pair_weights = Counter()

table_count = 0
for (first_burden, first_edgewise), first_weight in one_tour_patterns.items():
    for (second_burden, second_edgewise), second_weight in one_tour_patterns.items():
        weight = first_weight * second_weight
        table_count += weight
        burdens = (first_burden, second_burden)

        statewise_optima = tuple(
            min(burden[state] for burden in burdens)
            for state in range(STATES)
        )
        statewise_lower_bound = max(statewise_optima)
        robust_optimum = min(max(burden) for burden in burdens)
        robust_gap = robust_optimum - statewise_lower_bound
        assert robust_gap >= 0
        robust_gap_histogram[robust_gap] += weight
        robust_optimum_histogram[robust_optimum] += weight
        statewise_lower_histogram[statewise_lower_bound] += weight
        robust_incompatibility_cases += weight * int(robust_gap > 0)

        edgewise_worst_optimum = min(first_edgewise, second_edgewise)
        edgewise_overcharge = edgewise_worst_optimum - robust_optimum
        assert edgewise_overcharge >= 0
        edgewise_overcharge_histogram[edgewise_overcharge] += weight
        edgewise_strict_cases += weight * int(edgewise_overcharge > 0)
        burden_pair_weights[burdens] += weight

assert table_count == 2 ** 18 == 262144
assert robust_gap_histogram == {0: 199456, 1: 57492, 2: 5112, 3: 84}
assert robust_optimum_histogram == {3: 1023, 4: 60417, 5: 172143, 6: 28561}
assert statewise_lower_histogram == {3: 3375, 4: 107217, 5: 139455, 6: 12097}
assert robust_incompatibility_cases == 62688
assert edgewise_overcharge_histogram == {0: 137740, 1: 120324, 2: 4080}
assert edgewise_strict_cases == 124404
assert len(burden_pair_weights) == 4096

repetition_checks = 0
robust_loss_tour_not_repetition_optimal = 0
for burdens, weight in burden_pair_weights.items():
    robust_optimum = min(max(burden) for burden in burdens)
    robust_tours = {
        index for index, burden in enumerate(burdens)
        if max(burden) == robust_optimum
    }
    for gains in product((1, 2, 3), repeat=STATES):
        for setup in range(4):
            required = tuple(
                repetitions(setup, gains, burden)
                for burden in burdens
            )
            assert all(
                required[index] == brute_repetitions(setup, gains, burden)
                for index, burden in enumerate(burdens)
            )
            repetition_optimum = min(required)
            repetition_tours = {
                index for index, value in enumerate(required)
                if value == repetition_optimum
            }
            robust_loss_tour_not_repetition_optimal += weight * int(
                robust_tours.isdisjoint(repetition_tours)
            )
            repetition_checks += weight

assert repetition_checks == 262144 * 27 * 4 == 28311552
assert robust_loss_tour_not_repetition_optimal == 1601388

opposing_burdens = ((3, 3, 6), (3, 6, 3))
assert max(
    min(burden[state] for burden in opposing_burdens)
    for state in range(STATES)
) == 3
assert min(map(max, opposing_burdens)) == 6

repetition_burdens = ((3, 3, 4), (3, 5, 3))
assert tuple(
    repetitions(0, (1, 2, 1), burden)
    for burden in repetition_burdens
) == (5, 4)
assert max(repetition_burdens[0]) < max(repetition_burdens[1])

print({
    "components": 3,
    "uncertainty_states": STATES,
    "directed_burden_tables": table_count,
    "robust_gap_histogram": dict(sorted(robust_gap_histogram.items())),
    "statewise_optima_incompatible_cases": robust_incompatibility_cases,
    "edgewise_worst_overcharge_histogram": dict(sorted(edgewise_overcharge_histogram.items())),
    "edgewise_worst_strict_cases": edgewise_strict_cases,
    "repetition_formula_checks": repetition_checks,
    "robust_loss_tour_not_repetition_optimal_cases": robust_loss_tour_not_repetition_optimal,
    "opposing_tour_example": opposing_burdens,
    "repetition_objective_counterexample": {
        "burdens": repetition_burdens,
        "gains": (1, 2, 1),
        "setup": 0,
        "required_repetitions": (5, 4),
    },
    "exact_repetition_objective": "min_T max_u (floor((S+L_u(T))/G_u)+1)",
    "remaining_gap": "supply a coordinate macro graph with three-state connector burdens and positive robust gains",
    "evidence_level": "exact_three_state_robust_connector_tour_interface",
    "status": "passed",
})

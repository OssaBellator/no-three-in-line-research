#!/usr/bin/env python3
from collections import Counter
from itertools import product

COMPONENTS = (0, 1, 2)
DIRECTED_EDGES = tuple(
    (first, second)
    for first in COMPONENTS
    for second in COMPONENTS
    if first != second
)
TOURS = (
    ((0, 1), (1, 2), (2, 0)),
    ((0, 2), (2, 1), (1, 0)),
)
UNCERTAINTY_STATES = (0, 1)


def tour_burden(costs, tour):
    return tuple(
        sum(costs[edge][state] for edge in tour)
        for state in UNCERTAINTY_STATES
    )


def repetitions(setup, gains, burden):
    return max(
        (setup + burden[state]) // gains[state] + 1
        for state in UNCERTAINTY_STATES
    )


robust_gap_histogram = Counter()
robust_optimum_histogram = Counter()
statewise_lower_histogram = Counter()
edgewise_overcharge_histogram = Counter()
robust_incompatibility_cases = 0
edgewise_strict_cases = 0
repetition_checks = 0
robust_loss_tour_not_repetition_optimal = 0

for values in product((1, 2), repeat=12):
    costs = {
        edge: (values[2 * index], values[2 * index + 1])
        for index, edge in enumerate(DIRECTED_EDGES)
    }
    burdens = tuple(tour_burden(costs, tour) for tour in TOURS)

    statewise_optima = tuple(
        min(burden[state] for burden in burdens)
        for state in UNCERTAINTY_STATES
    )
    statewise_lower_bound = max(statewise_optima)
    robust_optimum = min(max(burden) for burden in burdens)
    robust_gap = robust_optimum - statewise_lower_bound
    assert robust_gap >= 0
    robust_gap_histogram[robust_gap] += 1
    robust_optimum_histogram[robust_optimum] += 1
    statewise_lower_histogram[statewise_lower_bound] += 1
    robust_incompatibility_cases += int(robust_gap > 0)

    edgewise_worst_optimum = min(
        sum(max(costs[edge]) for edge in tour)
        for tour in TOURS
    )
    edgewise_overcharge = edgewise_worst_optimum - robust_optimum
    assert edgewise_overcharge >= 0
    edgewise_overcharge_histogram[edgewise_overcharge] += 1
    edgewise_strict_cases += int(edgewise_overcharge > 0)

    robust_tours = {
        index for index, burden in enumerate(burdens)
        if max(burden) == robust_optimum
    }
    for gains in product((1, 2, 3), repeat=2):
        for setup in range(4):
            required = tuple(
                repetitions(setup, gains, burden)
                for burden in burdens
            )
            for index, burden in enumerate(burdens):
                brute = 1
                while not all(
                    brute * gains[state] - burden[state] > setup
                    for state in UNCERTAINTY_STATES
                ):
                    brute += 1
                assert required[index] == brute
            repetition_optimum = min(required)
            repetition_tours = {
                index for index, value in enumerate(required)
                if value == repetition_optimum
            }
            robust_loss_tour_not_repetition_optimal += int(
                robust_tours.isdisjoint(repetition_tours)
            )
            repetition_checks += 1

assert robust_gap_histogram == {0: 3452, 1: 582, 2: 60, 3: 2}
assert robust_optimum_histogram == {3: 127, 4: 1665, 5: 2079, 6: 225}
assert statewise_lower_histogram == {3: 225, 4: 2079, 5: 1665, 6: 127}
assert robust_incompatibility_cases == 644
assert edgewise_overcharge_histogram == {0: 2980, 1: 1116}
assert edgewise_strict_cases == 1116
assert repetition_checks == 4096 * 9 * 4 == 147456
assert robust_loss_tour_not_repetition_optimal == 5640

opposing_costs = {
    (0, 1): (1, 1),
    (0, 2): (1, 1),
    (1, 0): (1, 1),
    (1, 2): (1, 1),
    (2, 0): (1, 2),
    (2, 1): (2, 1),
}
opposing_burdens = tuple(tour_burden(opposing_costs, tour) for tour in TOURS)
assert opposing_burdens == ((3, 4), (4, 3))
assert max(
    min(burden[state] for burden in opposing_burdens)
    for state in UNCERTAINTY_STATES
) == 3
assert min(map(max, opposing_burdens)) == 4

repetition_costs = {
    (0, 1): (1, 1),
    (0, 2): (1, 1),
    (1, 0): (1, 1),
    (1, 2): (1, 2),
    (2, 0): (1, 2),
    (2, 1): (2, 1),
}
repetition_burdens = tuple(tour_burden(repetition_costs, tour) for tour in TOURS)
assert repetition_burdens == ((3, 5), (4, 3))
assert tuple(repetitions(0, (1, 2), burden) for burden in repetition_burdens) == (4, 5)
assert max(repetition_burdens[1]) < max(repetition_burdens[0])

print({
    "components": len(COMPONENTS),
    "uncertainty_states": len(UNCERTAINTY_STATES),
    "directed_burden_tables": 4**6,
    "robust_gap_histogram": dict(sorted(robust_gap_histogram.items())),
    "statewise_optima_incompatible_cases": robust_incompatibility_cases,
    "edgewise_worst_overcharge_histogram": dict(sorted(edgewise_overcharge_histogram.items())),
    "edgewise_worst_strict_cases": edgewise_strict_cases,
    "repetition_formula_checks": repetition_checks,
    "robust_loss_tour_not_repetition_optimal_cases": robust_loss_tour_not_repetition_optimal,
    "opposing_tour_example": opposing_burdens,
    "exact_repetition_objective": "min_T max_u (floor((S+L_u(T))/G_u)+1)",
    "remaining_gap": "supply a coordinate macro graph with connector-path burden vectors and positive bundle-gain vectors",
    "evidence_level": "exact_finite_uncertainty_robust_connector_tour_interface",
    "status": "passed",
})

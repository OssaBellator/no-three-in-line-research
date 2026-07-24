#!/usr/bin/env python3
"""Verify OP4l current-syndrome source-factor payment."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import product


Weight = Fraction


@dataclass(frozen=True)
class PaymentSystem:
    factor_weights: tuple[Weight, ...]
    neighborhoods: tuple[frozenset[int], ...]
    gains: tuple[Weight, ...]
    rank: int = 3

    def validate(self) -> None:
        assert self.factor_weights
        assert self.neighborhoods
        assert len(self.neighborhoods) == len(self.gains)
        assert self.rank >= 2
        assert all(weight > 0 for weight in self.factor_weights)
        assert all(gain > 0 for gain in self.gains)
        assert all(neighbors for neighbors in self.neighborhoods)
        assert all(
            0 <= factor < len(self.factor_weights)
            for neighbors in self.neighborhoods
            for factor in neighbors
        )
        for index, gain in enumerate(self.gains):
            assert gain <= self.destroyed_weight(index)
        assert max(self.factor_degrees(), default=0) <= self.rank

    def destroyed_weight(self, correction: int) -> Weight:
        return sum(
            (
                self.factor_weights[factor]
                for factor in self.neighborhoods[correction]
            ),
            Fraction(),
        )

    def factor_degrees(self) -> tuple[int, ...]:
        return tuple(
            sum(
                factor in neighbors
                for neighbors in self.neighborhoods
            )
            for factor in range(len(self.factor_weights))
        )

    @property
    def total_gain(self) -> Weight:
        return sum(self.gains, Fraction())


@dataclass(frozen=True)
class Payment:
    incidence: tuple[tuple[Weight, ...], ...]
    factor_loads: tuple[Weight, ...]
    total: Weight
    congestion: Weight
    scale: Weight


def proportional_payment(system: PaymentSystem) -> Payment:
    system.validate()
    destroyed = tuple(
        system.destroyed_weight(index)
        for index in range(len(system.gains))
    )
    normalized_loads = tuple(
        sum(
            (
                system.gains[index] / destroyed[index]
                for index, neighbors in enumerate(system.neighborhoods)
                if factor in neighbors
            ),
            Fraction(),
        )
        for factor in range(len(system.factor_weights))
    )
    congestion = max(normalized_loads, default=Fraction())
    scale = max(Fraction(1), congestion)
    incidence = tuple(
        tuple(
            (
                gain * system.factor_weights[factor]
                / (scale * destroyed[index])
                if factor in system.neighborhoods[index]
                else Fraction()
            )
            for factor in range(len(system.factor_weights))
        )
        for index, gain in enumerate(system.gains)
    )
    factor_loads = tuple(
        sum(
            (
                incidence[index][factor]
                for index in range(len(system.gains))
            ),
            Fraction(),
        )
        for factor in range(len(system.factor_weights))
    )
    total = sum(factor_loads, Fraction())

    for index, row in enumerate(incidence):
        assert sum(row, Fraction()) == system.gains[index] / scale
    assert all(
        load <= capacity
        for load, capacity in zip(factor_loads, system.factor_weights)
    )
    assert congestion <= system.rank
    assert scale <= system.rank
    assert total == system.total_gain / scale
    assert total * system.rank >= system.total_gain
    return Payment(
        incidence=incidence,
        factor_loads=factor_loads,
        total=total,
        congestion=congestion,
        scale=scale,
    )


def add_edge(
    residual: dict[tuple[str, int], dict[tuple[str, int], Weight]],
    left: tuple[str, int],
    right: tuple[str, int],
    capacity: Weight,
) -> None:
    residual.setdefault(left, {})
    residual.setdefault(right, {})
    residual[left][right] = residual[left].get(right, Fraction()) + capacity
    residual[right].setdefault(left, Fraction())


def maximum_payment(system: PaymentSystem) -> tuple[Weight, tuple[Weight, ...]]:
    system.validate()
    source = ("source", 0)
    sink = ("sink", 0)
    residual: dict[
        tuple[str, int],
        dict[tuple[str, int], Weight],
    ] = {}
    for correction, gain in enumerate(system.gains):
        correction_node = ("correction", correction)
        add_edge(residual, source, correction_node, gain)
        for factor in system.neighborhoods[correction]:
            add_edge(
                residual,
                correction_node,
                ("factor", factor),
                system.total_gain,
            )
    for factor, weight in enumerate(system.factor_weights):
        add_edge(residual, ("factor", factor), sink, weight)

    value = Fraction()
    while True:
        parent: dict[tuple[str, int], tuple[str, int] | None] = {
            source: None
        }
        queue = deque([source])
        while queue and sink not in parent:
            node = queue.popleft()
            for neighbor, capacity in residual[node].items():
                if capacity > 0 and neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)
        if sink not in parent:
            break
        increment = system.total_gain
        cursor = sink
        while parent[cursor] is not None:
            previous = parent[cursor]
            assert previous is not None
            increment = min(increment, residual[previous][cursor])
            cursor = previous
        cursor = sink
        while parent[cursor] is not None:
            previous = parent[cursor]
            assert previous is not None
            residual[previous][cursor] -= increment
            residual[cursor][previous] += increment
            cursor = previous
        value += increment

    factor_loads = tuple(
        weight - residual[("factor", factor)][sink]
        for factor, weight in enumerate(system.factor_weights)
    )
    assert sum(factor_loads, Fraction()) == value
    assert all(
        load <= capacity
        for load, capacity in zip(factor_loads, system.factor_weights)
    )
    return value, factor_loads


def hall_deficit(
    system: PaymentSystem,
) -> tuple[Weight, frozenset[int]]:
    system.validate()
    best_deficit = Fraction()
    best_set: frozenset[int] = frozenset()
    correction_count = len(system.gains)
    for mask in range(1 << correction_count):
        selected = frozenset(
            index
            for index in range(correction_count)
            if mask & (1 << index)
        )
        gain = sum(
            (system.gains[index] for index in selected),
            Fraction(),
        )
        neighbors = set().union(
            *(
                system.neighborhoods[index]
                for index in selected
            )
        ) if selected else set()
        capacity = sum(
            (system.factor_weights[factor] for factor in neighbors),
            Fraction(),
        )
        deficit = gain - capacity
        if deficit > best_deficit:
            best_deficit = deficit
            best_set = selected
    return best_deficit, best_set


def verify_overload(
    system: PaymentSystem,
    deficit: Weight,
    selected: frozenset[int],
) -> None:
    if deficit == 0:
        return
    assert selected
    neighbor_set = set().union(
        *(system.neighborhoods[index] for index in selected)
    )
    multiplicities = {
        factor: sum(
            factor in system.neighborhoods[index]
            for index in selected
        )
        for factor in neighbor_set
    }
    overload = sum(
        (
            (multiplicity - 1) * system.factor_weights[factor]
            for factor, multiplicity in multiplicities.items()
        ),
        Fraction(),
    )
    repeated_weight = sum(
        (
            system.factor_weights[factor]
            for factor, multiplicity in multiplicities.items()
            if multiplicity >= 2
        ),
        Fraction(),
    )
    assert overload >= deficit
    assert repeated_weight * (system.rank - 1) >= deficit


def occurrence_weights(
    factor_loads: tuple[Weight, ...],
    occurrences: tuple[int, ...],
) -> tuple[Weight, ...]:
    assert occurrences
    multiplicities = {
        factor: occurrences.count(factor)
        for factor in set(occurrences)
    }
    weights = tuple(
        factor_loads[factor] / multiplicities[factor]
        for factor in occurrences
    )
    for factor, multiplicity in multiplicities.items():
        assert sum(
            (
                weight
                for source, weight in zip(occurrences, weights)
                if source == factor
            ),
            Fraction(),
        ) == factor_loads[factor]
        assert multiplicity >= 1
    return weights


def verify_core_gate(factor_loads: tuple[Weight, ...]) -> int:
    total = sum(factor_loads, Fraction())
    assert total > 0
    cases = 0
    for mask in range(1 << len(factor_loads)):
        core = {
            factor
            for factor in range(len(factor_loads))
            if mask & (1 << factor)
        }
        core_weight = sum(
            (factor_loads[factor] for factor in core),
            Fraction(),
        )
        outside = total - core_weight
        if core_weight >= total / 2:
            occurrences = tuple(
                factor
                for factor in sorted(core)
                for _ in range(factor + 1)
            )
            if occurrences:
                distributed = occurrence_weights(
                    factor_loads,
                    occurrences,
                )
                assert sum(distributed, Fraction()) == core_weight
        else:
            assert outside > total / 2
        cases += 1
    return cases


def gain_choices(destroyed: Weight) -> tuple[Weight, ...]:
    return tuple(
        sorted(
            {
                Fraction(1, 2) * destroyed,
                destroyed,
            }
        )
    )


def verify_system(system: PaymentSystem) -> int:
    proportional = proportional_payment(system)
    maximum, factor_loads = maximum_payment(system)
    deficit, selected = hall_deficit(system)
    assert maximum == system.total_gain - deficit
    assert maximum >= proportional.total
    assert maximum * system.rank >= system.total_gain
    if deficit == 0:
        assert maximum == system.total_gain
    else:
        assert maximum < system.total_gain
    verify_overload(system, deficit, selected)

    for factor, degree in enumerate(system.factor_degrees()):
        if degree:
            clause = tuple(
                index
                for index, neighbors in enumerate(system.neighborhoods)
                if factor in neighbors
            )
            assert 1 <= len(clause) <= system.rank
            all_current = tuple(False for _ in system.gains)
            assert not any(all_current[index] for index in clause)
            for correction in clause:
                singleton = tuple(
                    index == correction
                    for index in range(len(system.gains))
                )
                assert any(singleton[index] for index in clause)

    core_cases = verify_core_gate(proportional.factor_loads)
    if any(factor_loads):
        occurrence_list = tuple(
            factor
            for factor, load in enumerate(factor_loads)
            if load > 0
            for _ in range(2)
        )
        distributed = occurrence_weights(factor_loads, occurrence_list)
        assert sum(distributed, Fraction()) == maximum
    return core_cases


def verify_exhaustive_systems() -> tuple[int, int]:
    systems = 0
    core_cases = 0
    for correction_count in range(1, 4):
        for factor_count in range(1, 4):
            masks = tuple(range(1, 1 << factor_count))
            for neighborhood_masks in product(
                masks,
                repeat=correction_count,
            ):
                neighborhoods = tuple(
                    frozenset(
                        factor
                        for factor in range(factor_count)
                        if mask & (1 << factor)
                    )
                    for mask in neighborhood_masks
                )
                degrees = tuple(
                    sum(
                        factor in neighbors
                        for neighbors in neighborhoods
                    )
                    for factor in range(factor_count)
                )
                if max(degrees, default=0) > 3:
                    continue
                for integer_weights in product(
                    (1, 2),
                    repeat=factor_count,
                ):
                    weights = tuple(
                        Fraction(weight) for weight in integer_weights
                    )
                    destroyed = tuple(
                        sum(
                            (weights[factor] for factor in neighbors),
                            Fraction(),
                        )
                        for neighbors in neighborhoods
                    )
                    for gains in product(
                        *(gain_choices(value) for value in destroyed)
                    ):
                        system = PaymentSystem(
                            factor_weights=weights,
                            neighborhoods=neighborhoods,
                            gains=tuple(gains),
                        )
                        core_cases += verify_system(system)
                        systems += 1
    return systems, core_cases


def verify_sharp_example() -> None:
    system = PaymentSystem(
        factor_weights=(Fraction(1),),
        neighborhoods=(
            frozenset({0}),
            frozenset({0}),
            frozenset({0}),
        ),
        gains=(Fraction(1), Fraction(1), Fraction(1)),
    )
    proportional = proportional_payment(system)
    maximum, _ = maximum_payment(system)
    deficit, selected = hall_deficit(system)
    assert proportional.total == 1
    assert proportional.scale == 3
    assert maximum == 1
    assert deficit == 2
    assert selected == frozenset({0, 1, 2})
    verify_overload(system, deficit, selected)


def main() -> None:
    systems, core_cases = verify_exhaustive_systems()
    verify_sharp_example()
    print(
        "phase syndrome payment verified:",
        f"{systems} weighted incidence systems,",
        f"{core_cases} core splits,",
        "sharp rank-three congestion",
    )


if __name__ == "__main__":
    main()

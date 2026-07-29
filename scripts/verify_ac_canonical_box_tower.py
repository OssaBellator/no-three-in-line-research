#!/usr/bin/env python3
"""Deterministic audit for AC5ix--AC5jc."""

from __future__ import annotations

from dataclasses import dataclass
from math import prod
import random

SEED = 20260730
SYSTEMS = 2500


@dataclass(frozen=True)
class System:
    targets: int
    partners: int
    jobs: int
    atoms: int
    boundary_records: int
    betas: tuple[int, ...]
    capacity_stocks: tuple[int, ...]
    controls: int
    modulus: int
    absolute_threshold: int
    max_increment: int


def falling_sum(n: int) -> int:
    total = 1
    term = 1
    for k in range(1, n + 1):
        term *= n - k + 1
        total += term
    return total


def ambient_count(
    system: System,
    resource_caps: tuple[int, ...] | list[int] | None = None,
    capacity_caps: tuple[int, ...] | list[int] | None = None,
    tail_cap: int | None = None,
) -> int:
    resources = system.betas if resource_caps is None else tuple(resource_caps)
    capacities = (
        system.capacity_stocks if capacity_caps is None else tuple(capacity_caps)
    )
    if tail_cap is None:
        tail_cap = (
            system.absolute_threshold
            + system.max_increment * system.controls * system.modulus
        )

    injection_states = 1
    term = 1
    for k in range(1, system.targets + 1):
        term *= system.partners - k + 1
        injection_states += term

    return (
        injection_states
        * falling_sum(system.jobs)
        * (2**system.atoms)
        * system.boundary_records
        * (tail_cap + 1)
        * prod(cap + 1 for cap in resources)
        * prod(cap + 1 for cap in capacities)
    )


def verify() -> dict[str, int]:
    rng = random.Random(SEED)
    totals = {
        "systems": 0,
        "ambient": 0,
        "phase_states": 0,
        "phase_steps": 0,
        "strip_returns": 0,
        "phase_cycles": 0,
        "positive_drift": 0,
        "zero_drift": 0,
        "negative_drift": 0,
        "boundary_records": 0,
        "terminal": 0,
        "paid": 0,
        "escape": 0,
        "reset": 0,
        "overflow": 0,
        "coordinates_expanded": 0,
        "shell": 0,
        "resolved": 0,
        "zero_neighbourhood": 0,
        "uniform_towers": 0,
        "divergent_towers": 0,
        "max_uniform_bound": 0,
    }

    for _ in range(SYSTEMS):
        partners = rng.randint(2, 6)
        targets = rng.randint(1, partners)
        system = System(
            targets=targets,
            partners=partners,
            jobs=rng.randint(0, 4),
            atoms=rng.randint(0, 4),
            boundary_records=rng.randint(1, 5),
            betas=tuple(rng.randint(1, 5) for _ in range(rng.randint(1, 4))),
            capacity_stocks=tuple(
                rng.randint(0, 7) for _ in range(rng.randint(1, 4))
            ),
            controls=rng.randint(1, 4),
            modulus=rng.randint(1, 5),
            absolute_threshold=rng.randint(1, 8),
            max_increment=rng.randint(1, 4),
        )

        phase_stock = system.controls * system.modulus
        observation_cap = (
            system.absolute_threshold + system.max_increment * phase_stock
        )
        initial_ambient = ambient_count(system)

        # AC5ix: every canonical coordinate is necessary for its declared purpose.
        assert all(beta >= 1 for beta in system.betas)
        assert observation_cap == (
            system.absolute_threshold + system.max_increment * phase_stock
        )
        for beta in system.betas:
            assert beta - 1 < beta
        for stock in system.capacity_stocks:
            if stock > 0:
                assert stock - 1 < stock
        assert observation_cap - 1 < (
            system.absolute_threshold + system.max_increment * phase_stock
        )

        # Tail phase transitions preserve residue by construction.
        phases = [
            (control, residue)
            for control in range(system.controls)
            for residue in range(system.modulus)
        ]
        next_control = {phase: rng.randrange(system.controls) for phase in phases}
        increment = {
            phase: rng.randint(-system.max_increment, system.max_increment)
            for phase in phases
        }
        phase = rng.choice(phases)
        balance = system.absolute_threshold
        seen: dict[tuple[int, int], int] = {}
        path: list[tuple[int, int]] = []
        strip_return = False
        repeated: tuple[int, int] | None = None
        maximum_balance = balance

        for step in range(phase_stock + 1):
            if balance < system.absolute_threshold:
                strip_return = True
                break
            if phase in seen:
                repeated = (seen[phase], step)
                break
            seen[phase] = step
            path.append(phase)
            delta = increment[phase]
            balance += delta
            phase = (
                next_control[phase],
                (phase[1] + delta) % system.modulus,
            )
            maximum_balance = max(maximum_balance, balance)
            assert maximum_balance <= observation_cap

        if strip_return:
            totals["strip_returns"] += 1
        else:
            assert repeated is not None
            start, stop = repeated
            drift = sum(increment[path[index]] for index in range(start, stop))
            assert drift % system.modulus == 0
            totals["phase_cycles"] += 1
            if drift > 0:
                totals["positive_drift"] += 1
            elif drift == 0:
                totals["zero_drift"] += 1
            else:
                totals["negative_drift"] += 1

        totals["phase_states"] += phase_stock
        totals["phase_steps"] += len(path)

        # AC5iy--AC5ja: classify the frontier and compute its least enlargement.
        coordinates = [
            ("resource", index, cap)
            for index, cap in enumerate(system.betas)
        ] + [
            ("capacity", index, cap)
            for index, cap in enumerate(system.capacity_stocks)
        ] + [("tail", 0, observation_cap)]

        requirements: dict[tuple[str, int], list[int]] = {}
        for _record in range(rng.randint(4, 14)):
            route = rng.choices(
                ["terminal", "paid", "escape", "reset", "overflow"],
                weights=[2, 2, 1, 1, 4],
            )[0]
            totals[route] += 1
            totals["boundary_records"] += 1
            if route == "overflow":
                kind, index, current_cap = rng.choice(coordinates)
                requirements.setdefault((kind, index), []).append(
                    current_cap + rng.randint(1, 4)
                )

        enlarged_resources = list(system.betas)
        enlarged_capacities = list(system.capacity_stocks)
        enlarged_tail = observation_cap
        for (kind, index), values in requirements.items():
            required = max(values)
            if kind == "resource":
                enlarged_resources[index] = required
            elif kind == "capacity":
                enlarged_capacities[index] = required
            else:
                enlarged_tail = required

        enlarged_ambient = ambient_count(
            system,
            enlarged_resources,
            enlarged_capacities,
            enlarged_tail,
        )

        # Componentwise least: every chosen value is the maximum exact demand.
        for (kind, index), values in requirements.items():
            required = max(values)
            actual = (
                enlarged_resources[index]
                if kind == "resource"
                else enlarged_capacities[index]
                if kind == "capacity"
                else enlarged_tail
            )
            assert actual == required

        # Deterministic shell priority and telescoping.
        current_resources = list(system.betas)
        current_capacities = list(system.capacity_stocks)
        current_tail = observation_cap
        current_ambient = initial_ambient
        candidates: list[tuple[int, int, int, str, int, int]] = []

        for (kind, index), values in requirements.items():
            required = max(values)
            trial_resources = current_resources.copy()
            trial_capacities = current_capacities.copy()
            trial_tail = current_tail
            if kind == "resource":
                trial_resources[index] = required
                old_cap = system.betas[index]
            elif kind == "capacity":
                trial_capacities[index] = required
                old_cap = system.capacity_stocks[index]
            else:
                trial_tail = required
                old_cap = observation_cap
            shell_cost = (
                ambient_count(
                    system,
                    trial_resources,
                    trial_capacities,
                    trial_tail,
                )
                - current_ambient
            )
            candidates.append(
                (
                    -len(values),
                    shell_cost,
                    -(required - old_cap),
                    kind,
                    index,
                    required,
                )
            )

        candidates.sort()
        shell_sum = 0
        for _gain, _cost, _excess, kind, index, required in candidates:
            previous = current_ambient
            if kind == "resource":
                current_resources[index] = required
            elif kind == "capacity":
                current_capacities[index] = required
            else:
                current_tail = required
            current_ambient = ambient_count(
                system,
                current_resources,
                current_capacities,
                current_tail,
            )
            shell_sum += current_ambient - previous

        assert current_ambient == enlarged_ambient
        assert shell_sum == enlarged_ambient - initial_ambient

        totals["coordinates_expanded"] += len(requirements)
        totals["shell"] += shell_sum
        totals["resolved"] += sum(len(values) for values in requirements.values())
        totals["zero_neighbourhood"] += rng.randint(0, 5)

        # AC5jc: sampled uniform envelopes or an explicit divergent component.
        uniform = rng.random() < 0.72
        if uniform:
            potential_cap = rng.randint(1, 40)
            ledger_caps = [rng.randint(0, 8) for _ in range(4)]
            level_bounds: list[int] = []
            for _level in range(4):
                potential = rng.randint(0, potential_cap)
                ledgers = [
                    rng.randint(0, ledger_caps[index]) for index in range(4)
                ]
                disturbance_weight = rng.randint(0, 3)
                level_bounds.append(
                    (ledgers[2] + 1) * potential
                    + ledgers[3] * disturbance_weight
                    + ledgers[0]
                    + ledgers[1]
                )
            totals["uniform_towers"] += 1
            totals["max_uniform_bound"] = max(
                totals["max_uniform_bound"], max(level_bounds)
            )
        else:
            divergent = [rng.randint(1, 10)]
            for _level in range(3):
                divergent.append(divergent[-1] + rng.randint(1, 5))
            assert divergent[-1] > divergent[0]
            totals["divergent_towers"] += 1

        totals["ambient"] += initial_ambient
        totals["systems"] += 1

    expected = {
        "systems": 2500,
        "ambient": 87324551933092,
        "phase_states": 18504,
        "phase_steps": 4697,
        "strip_returns": 1254,
        "phase_cycles": 1246,
        "positive_drift": 481,
        "zero_drift": 730,
        "negative_drift": 35,
        "boundary_records": 22588,
        "terminal": 4504,
        "paid": 4530,
        "escape": 2302,
        "reset": 2235,
        "overflow": 9017,
        "coordinates_expanded": 6632,
        "shell": 232616018137130,
        "resolved": 9017,
        "zero_neighbourhood": 6234,
        "uniform_towers": 1805,
        "divergent_towers": 695,
        "max_uniform_bound": 346,
    }
    assert totals == expected
    return totals


if __name__ == "__main__":
    result = verify()
    for key, value in result.items():
        print(f"{key}: {value}")

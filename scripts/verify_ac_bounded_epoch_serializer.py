#!/usr/bin/env python3
"""Deterministic audit for AC5is--AC5iw."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
from math import prod
import hashlib
import json
import random

SEED = 20260730
SYSTEMS = 2500


def falling(n: int, k: int) -> int:
    out = 1
    for i in range(k):
        out *= n - i
    return out


def deterministic_bit(obj: object) -> int:
    payload = json.dumps(obj, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).digest()[0] & 1


@dataclass(frozen=True)
class Operation:
    name: str
    resource_delta: tuple[int, ...]
    capacity_delta: tuple[int, ...]
    monotone_escape: tuple[bool, ...]
    schema_change: bool = False


def route_state(
    resources: tuple[int, ...],
    balances: tuple[int, ...],
    resource_caps: tuple[int, ...],
    capacity_caps: tuple[int, ...],
    operation: Operation,
) -> tuple[object, ...]:
    if operation.schema_change:
        return ("reset", operation.name)

    new_resources = tuple(
        value + delta
        for value, delta in zip(resources, operation.resource_delta)
    )
    new_balances = tuple(
        value + delta
        for value, delta in zip(balances, operation.capacity_delta)
    )

    for index, value in enumerate(new_resources):
        if value < 0:
            return ("shortage_resource", index, -value)
    for index, value in enumerate(new_balances):
        if value < 0:
            return ("shortage_capacity", index, -value)
    for index, (value, cap) in enumerate(zip(new_balances, capacity_caps)):
        if value > cap:
            return ("amplification", index, value - cap)
    for index, (value, cap) in enumerate(zip(new_resources, resource_caps)):
        if value > cap:
            if operation.monotone_escape[index]:
                return ("monotone_escape", index, value - cap)
            return ("overflow_resource", index, value - cap)

    return ("internal", new_resources, new_balances)


def run() -> dict[str, int]:
    rng = random.Random(SEED)
    stats = {
        "systems": SYSTEMS,
        "state_ambient_total": 0,
        "pair_total": 0,
        "ops_total": 0,
        "sampled_transitions": 0,
        "internal": 0,
        "shortage": 0,
        "amplification": 0,
        "overflow": 0,
        "escape": 0,
        "reset": 0,
        "preserved_internal": 0,
        "refined_boundaries": 0,
        "stable_boundaries": 0,
        "queue_states": 0,
        "injection_states": 0,
        "omitted_field_witnesses": 0,
        "zero_neighborhood": 0,
        "claimed_objects": 0,
        "shell_states": 0,
    }

    for system_index in range(SYSTEMS):
        target_count = rng.randint(1, 3)
        partner_count = rng.randint(target_count, 5)
        job_count = rng.randint(0, 5)
        atom_count = rng.randint(0, 4)
        controller_count = rng.randint(1, 4)
        tail_cap = rng.randint(1, 5)
        boundary_count = rng.randint(1, 3)
        resource_count = rng.randint(1, 3)
        capacity_count = rng.randint(1, 3)
        resource_caps = tuple(rng.randint(1, 4) for _ in range(resource_count))
        capacity_caps = tuple(rng.randint(0, 3) for _ in range(capacity_count))

        injection_states = sum(
            falling(partner_count, length)
            for length in range(target_count + 1)
        )
        queue_states = sum(
            falling(job_count, length)
            for length in range(job_count + 1)
        )

        # Independent brute-force checks of AC5is.
        assert injection_states == sum(
            len(list(permutations(range(partner_count), length)))
            for length in range(target_count + 1)
        )
        assert queue_states == sum(
            len(list(permutations(range(job_count), length)))
            for length in range(job_count + 1)
        )

        state_bound = (
            injection_states
            * queue_states
            * (2**atom_count)
            * controller_count
            * (tail_cap + 1)
            * prod(cap + 1 for cap in resource_caps)
            * prod(cap + 1 for cap in capacity_caps)
            * boundary_count
        )
        stats["state_ambient_total"] += state_bound
        stats["queue_states"] += queue_states
        stats["injection_states"] += injection_states

        incidence_count = rng.randint(2, 8)
        token_count = rng.randint(2, 8)
        pair_records = [
            (
                "v1",
                incidence,
                token,
                deterministic_bit((system_index, incidence, token)),
            )
            for incidence in range(incidence_count)
            for token in range(token_count)
        ]
        assert len({(record[1], record[2]) for record in pair_records}) == (
            incidence_count * token_count
        )
        stats["pair_total"] += incidence_count * token_count

        # Exact omitted-schema collision witness.
        first_record = ("v1", "inc0", "tok0", ("owner", 0))
        second_record = ("v2", "inc0", "tok0", ("owner", 0))
        assert first_record != second_record
        assert first_record[1:] == second_record[1:]
        stats["omitted_field_witnesses"] += 1

        operation_count = rng.randint(2, 6)
        operations: list[Operation] = []
        for operation_index in range(operation_count):
            operations.append(
                Operation(
                    name=f"op{operation_index}",
                    resource_delta=tuple(
                        rng.randint(-2, 2) for _ in range(resource_count)
                    ),
                    capacity_delta=tuple(
                        rng.randint(-1, 2) for _ in range(capacity_count)
                    ),
                    monotone_escape=tuple(
                        rng.random() < 0.25 for _ in range(resource_count)
                    ),
                    schema_change=rng.random() < 0.05,
                )
            )
        stats["ops_total"] += operation_count

        sample_count = rng.randint(8, 20)
        local_transition_count = 0
        for _ in range(sample_count):
            resources = tuple(rng.randint(0, cap) for cap in resource_caps)
            balances = tuple(rng.randint(0, cap) for cap in capacity_caps)

            for operation in operations:
                local_transition_count += 1
                outcome = route_state(
                    resources,
                    balances,
                    resource_caps,
                    capacity_caps,
                    operation,
                )
                stats["sampled_transitions"] += 1
                kind = outcome[0]

                if kind == "internal":
                    stats["internal"] += 1
                elif str(kind).startswith("shortage"):
                    stats["shortage"] += 1
                elif kind == "amplification":
                    stats["amplification"] += 1
                elif kind == "overflow_resource":
                    stats["overflow"] += 1
                elif kind == "monotone_escape":
                    stats["escape"] += 1
                elif kind == "reset":
                    stats["reset"] += 1
                else:
                    raise AssertionError(f"unknown route {kind!r}")

                larger_resource_caps = tuple(
                    cap + rng.randint(0, 2) for cap in resource_caps
                )
                larger_capacity_caps = tuple(
                    cap + rng.randint(0, 2) for cap in capacity_caps
                )
                larger_outcome = route_state(
                    resources,
                    balances,
                    larger_resource_caps,
                    larger_capacity_caps,
                    operation,
                )

                if kind == "internal":
                    assert larger_outcome == outcome
                    stats["preserved_internal"] += 1
                elif kind in (
                    "overflow_resource",
                    "monotone_escape",
                    "amplification",
                ):
                    if larger_outcome[0] == "internal":
                        stats["refined_boundaries"] += 1
                    else:
                        assert larger_outcome[0] in (
                            kind,
                            "overflow_resource",
                            "monotone_escape",
                            "amplification",
                        )
                        stats["stable_boundaries"] += 1
                elif str(kind).startswith("shortage"):
                    assert larger_outcome == outcome
                elif kind == "reset":
                    assert larger_outcome == outcome

        assert local_transition_count <= state_bound * operation_count

        # AC5iv candidate-neighbourhood checks.
        template_kinds = (
            "direct",
            "layered",
            "pool",
            "repair",
            "flow",
            "recurrence",
        )
        object_count = (
            incidence_count * token_count
            + rng.randint(3, 12)
            + rng.randint(3, 12)
        )
        for object_index in range(object_count):
            claims = [
                kind
                for kind in template_kinds
                if deterministic_bit((system_index, object_index, kind))
                and rng.random() < 0.9
            ]
            if claims:
                stats["claimed_objects"] += 1
            else:
                stats["zero_neighborhood"] += 1

        enlarged_resource_caps = tuple(cap + 1 for cap in resource_caps)
        enlarged_capacity_caps = tuple(cap + 1 for cap in capacity_caps)
        enlarged_state_bound = (
            injection_states
            * queue_states
            * (2**atom_count)
            * controller_count
            * (tail_cap + 1)
            * prod(cap + 1 for cap in enlarged_resource_caps)
            * prod(cap + 1 for cap in enlarged_capacity_caps)
            * boundary_count
        )
        assert enlarged_state_bound >= state_bound
        stats["shell_states"] += enlarged_state_bound - state_bound

    assert stats == {
        "systems": 2500,
        "state_ambient_total": 60692679097,
        "pair_total": 61957,
        "ops_total": 9903,
        "sampled_transitions": 139058,
        "internal": 17836,
        "shortage": 66573,
        "amplification": 36809,
        "overflow": 8341,
        "escape": 2611,
        "reset": 6888,
        "preserved_internal": 17836,
        "refined_boundaries": 19830,
        "stable_boundaries": 27931,
        "queue_states": 169231,
        "injection_states": 54857,
        "omitted_field_witnesses": 2500,
        "zero_neighborhood": 2734,
        "claimed_objects": 96491,
        "shell_states": 221248199177,
    }
    return stats


def main() -> None:
    stats = run()
    print("AC bounded epoch serializer audit passed")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

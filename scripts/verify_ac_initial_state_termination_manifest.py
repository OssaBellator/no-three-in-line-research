#!/usr/bin/env python3
"""Deterministic audit for AC5kh--AC5km."""

from __future__ import annotations

from collections import defaultdict
import hashlib
import random

SEED = 20260805
SYSTEMS = 3200
SECTIONS = (
    "schema",
    "serializer",
    "frontier",
    "fairness",
    "rank",
    "stratification",
    "exception",
)


def verify() -> dict[str, int]:
    rng = random.Random(SEED)
    totals: defaultdict[str, int] = defaultdict(int)

    for system_index in range(SYSTEMS):
        route_class = system_index % 8
        records = {section: True for section in SECTIONS}
        if route_class > 0:
            records[SECTIONS[route_class - 1]] = False

        failure: str | None = None
        for section in SECTIONS:
            if not records[section]:
                failure = section
                break

        if route_class == 0:
            assert failure is None
            payload = "|".join(
                f"{section}:{records[section]}" for section in SECTIONS
            ) + f"|{rng.randint(0, 10**9)}"
            digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
            assert len(digest) == 64

            state = (
                rng.randint(0, 5),
                rng.randint(0, 7),
                rng.randint(0, 9),
            )
            remaining_exceptions = rng.randint(0, 8)
            steps = 0
            exceptions_used = 0

            while state != (0, 0, 0):
                if remaining_exceptions > 0 and rng.random() < 0.1:
                    state = (
                        rng.randint(0, 5),
                        rng.randint(0, 7),
                        rng.randint(0, 9),
                    )
                    remaining_exceptions -= 1
                    exceptions_used += 1
                    steps += 1
                else:
                    old_state = state
                    deficit, restart, repair = state
                    if deficit > 0:
                        state = (
                            deficit - 1,
                            rng.randint(0, 7),
                            rng.randint(0, 9),
                        )
                    elif restart > 0:
                        state = (
                            deficit,
                            restart - 1,
                            rng.randint(0, 9),
                        )
                    else:
                        state = (deficit, restart, repair - 1)
                    assert state < old_state
                    steps += 1
                assert steps < 10000

            totals["valid_manifests"] += 1
            totals["proof_digests"] += 1
            totals["trajectory_steps"] += steps
            totals["exceptions_used"] += exceptions_used

        else:
            expected_failure = SECTIONS[route_class - 1]
            assert failure == expected_failure
            totals[f"failure_{failure}"] += 1

            earlier_before = tuple(
                records[section] for section in SECTIONS[: route_class - 1]
            )
            records[failure] = True
            earlier_after = tuple(
                records[section] for section in SECTIONS[: route_class - 1]
            )
            assert earlier_before == earlier_after
            totals["monotone_refinements"] += 1

        totals["systems"] += 1

    expected = {
        "valid_manifests": 400,
        "proof_digests": 400,
        "trajectory_steps": 6340,
        "exceptions_used": 538,
        "systems": 3200,
        "failure_schema": 400,
        "monotone_refinements": 2800,
        "failure_serializer": 400,
        "failure_frontier": 400,
        "failure_fairness": 400,
        "failure_rank": 400,
        "failure_stratification": 400,
        "failure_exception": 400,
    }
    result = dict(totals)
    assert result == expected
    return result


if __name__ == "__main__":
    result = verify()
    for key, value in result.items():
        print(f"{key}: {value}")

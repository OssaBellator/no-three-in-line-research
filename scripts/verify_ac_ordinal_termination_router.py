#!/usr/bin/env python3
"""Deterministic audit for AC5jp--AC5ju."""

from __future__ import annotations

from collections import defaultdict
import random

SEED = 20260802
SYSTEMS = 2500


def verify() -> dict[str, int]:
    rng = random.Random(SEED)
    totals: defaultdict[str, int] = defaultdict(int)

    for system_index in range(SYSTEMS):
        route_class = system_index % 5
        edge_count = rng.randint(20, 60)
        valid_progress_edges = 0
        bad_progress_found = False

        for edge_index in range(edge_count):
            source = (
                rng.randint(0, 5),
                rng.randint(0, 6),
                rng.randint(0, 8),
            )
            deficit, restart, repair = source
            edge_type = rng.choice(
                ["supply", "restart", "repair", "exception"]
            )

            if route_class == 1 and edge_index == 0:
                edge_type = "repair"
                target = (deficit, restart, repair + 1)
            elif edge_type == "supply" and deficit > 0:
                target = (
                    rng.randint(0, deficit - 1),
                    rng.randint(0, 8),
                    rng.randint(0, 10),
                )
            elif edge_type == "restart" and restart > 0:
                target = (
                    deficit,
                    rng.randint(0, restart - 1),
                    rng.randint(0, 10),
                )
            elif edge_type == "repair" and repair > 0:
                target = (
                    deficit,
                    restart,
                    rng.randint(0, repair - 1),
                )
            else:
                edge_type = "exception"
                target = (
                    rng.randint(0, 7),
                    rng.randint(0, 8),
                    rng.randint(0, 10),
                )

            if edge_type == "exception":
                totals["exception_edges"] += 1
            elif not target < source:
                bad_progress_found = True
                totals["bad_progress_edges"] += 1
            else:
                valid_progress_edges += 1
                totals[edge_type] += 1

        if route_class == 1:
            assert bad_progress_found
            totals["edge_fail_systems"] += 1
        else:
            assert not bad_progress_found
        totals["valid_progress_edges"] += valid_progress_edges

        # AC5jr global exceptional-address quotient.
        address_count = rng.randint(1, 10)
        stocks = [rng.randint(1, 5) for _ in range(address_count)]
        unique_stock = sum(stocks)
        references: list[int] = []
        for address in range(address_count):
            references.extend([address] * rng.randint(1, 4))
        raw_stock = sum(stocks[address] for address in references)

        if route_class == 2:
            totals["address_conflict"] += 1
        elif route_class == 3:
            totals["unbounded_address_universe"] += 1
        elif route_class == 1:
            totals["finite_stock_edge_blocked"] += unique_stock
        else:
            assert raw_stock >= unique_stock
            totals["unique_exception_stock"] += unique_stock
            totals["raw_exception_refs"] += raw_stock
            totals["alias_removed"] += raw_stock - unique_stock

            # AC5js sampled ordinal descent with finitely many exceptional jumps.
            state = (
                rng.randint(0, 5),
                rng.randint(0, 7),
                rng.randint(0, 9),
            )
            remaining_exception_stock = unique_stock
            steps = 0
            exception_steps = 0
            progress_steps = 0

            while steps < 10000:
                if state == (0, 0, 0):
                    break
                if remaining_exception_stock > 0 and rng.random() < 0.08:
                    state = (
                        rng.randint(0, 5),
                        rng.randint(0, 7),
                        rng.randint(0, 9),
                    )
                    remaining_exception_stock -= 1
                    exception_steps += 1
                    steps += 1
                    continue

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
                progress_steps += 1
                steps += 1

            assert steps < 10000
            assert state == (0, 0, 0)
            assert exception_steps <= unique_stock
            totals["simulated_progress"] += progress_steps
            totals["simulated_exceptions"] += exception_steps
            totals["trajectory_steps"] += steps
            totals["terminated_systems"] += 1

        totals["systems"] += 1

    expected = {
        "exception_edges": 35259,
        "restart": 21227,
        "supply": 20868,
        "repair": 22154,
        "valid_progress_edges": 64249,
        "unique_exception_stock": 16331,
        "raw_exception_refs": 40851,
        "alias_removed": 24520,
        "simulated_progress": 14841,
        "simulated_exceptions": 1309,
        "trajectory_steps": 16150,
        "terminated_systems": 1000,
        "systems": 2500,
        "bad_progress_edges": 500,
        "edge_fail_systems": 500,
        "finite_stock_edge_blocked": 8478,
        "address_conflict": 500,
        "unbounded_address_universe": 500,
    }
    result = dict(totals)
    assert result == expected
    return result


if __name__ == "__main__":
    result = verify()
    for key, value in result.items():
        print(f"{key}: {value}")

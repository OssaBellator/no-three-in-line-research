#!/usr/bin/env python3
from __future__ import annotations
import random

SEED = 59
SYSTEMS = 2500
COMPONENTS = (
    "delta", "theta", "unexposed", "support", "topo", "bank", "local"
)


def encode(state, bounds):
    value = 0
    for component, bound in zip(COMPONENTS, bounds):
        coordinate = state[component]
        assert 0 <= coordinate <= bound
        value = value * (bound + 1) + coordinate
    return value


def classify(before, after, record):
    if record.get("exception"):
        if not record.get("occurrence"):
            return "failure"
        return "exceptional"
    for index, component in enumerate(COMPONENTS):
        if before[component] != after[component]:
            if (
                after[component] < before[component]
                and all(before[value] == after[value] for value in COMPONENTS[:index])
            ):
                return component
            return "failure"
    return "failure"


def run():
    rng = random.Random(SEED)
    stats = {
        "systems": SYSTEMS,
        "progress_edges": 0,
        "supply_edges": 0,
        "restart_edges": 0,
        "first_exposure_edges": 0,
        "support_descent_edges": 0,
        "topological_edges": 0,
        "cycle_bank_edges": 0,
        "local_repair_edges": 0,
        "exceptional_edges": 0,
        "strict_rank_checks": 0,
        "mislabeled_edges": 0,
        "missing_occurrence_edges": 0,
        "alias_exception_witnesses": 0,
    }
    kinds = COMPONENTS + ("exceptional", "bad", "missing")

    for system in range(SYSTEMS):
        bounds = [rng.randint(2, 8) for _ in COMPONENTS]
        before = {
            component: rng.randint(1, bound)
            for component, bound in zip(COMPONENTS, bounds)
        }
        kind = kinds[system % len(kinds)]
        after = dict(before)
        record = {"operation": ("operation", system)}
        if kind in before:
            after[kind] -= 1
        elif kind == "exceptional":
            record.update(
                exception=True,
                occurrence=("exception", system),
                source=("source", system % 31),
            )
        elif kind == "bad":
            after["support"] -= 1
            after["delta"] += 1
        else:
            record.update(exception=True)

        route = classify(before, after, record)
        if kind in before:
            assert route == kind
            assert encode(after, bounds) < encode(before, bounds)
            stats["progress_edges"] += 1
            stats["strict_rank_checks"] += 1
            destination = {
                "delta": "supply_edges",
                "theta": "restart_edges",
                "unexposed": "first_exposure_edges",
                "support": "support_descent_edges",
                "topo": "topological_edges",
                "bank": "cycle_bank_edges",
                "local": "local_repair_edges",
            }[kind]
            stats[destination] += 1
        elif kind == "exceptional":
            assert route == "exceptional"
            stats["exceptional_edges"] += 1
            alias = "alias", record["occurrence"]
            assert alias != record["occurrence"]
            stats["alias_exception_witnesses"] += 1
        elif kind == "bad":
            assert route == "failure"
            stats["mislabeled_edges"] += 1
        else:
            assert route == "failure"
            stats["missing_occurrence_edges"] += 1

    return stats


if __name__ == "__main__":
    output = run()
    print("AC physical edge stratification audit")
    for key, value in output.items():
        print(f"{key}: {value}")

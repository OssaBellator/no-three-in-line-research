#!/usr/bin/env python3
"""Finite checks for CMR1254--CMR1261."""

from itertools import combinations
import random


def last_creation_times(history, universe):
    result = {}
    for item in universe:
        if item not in history[-1]:
            continue
        last = 0
        for index in range(1, len(history)):
            if item not in history[index - 1] and item in history[index]:
                last = index
        result[item] = last
    return result


def check_last_creation_partition():
    rng = random.Random(1254)
    checked = 0
    live_items = 0
    for universe_size in range(1, 120):
        universe = set(range(universe_size))
        for length in range(1, 40):
            history = []
            current = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            history.append(set(current))
            for _ in range(1, length):
                for item in universe:
                    if rng.random() < 0.08:
                        if item in current:
                            current.remove(item)
                        else:
                            current.add(item)
                history.append(set(current))
            last = last_creation_times(history, universe)
            classes = {}
            for item, time in last.items():
                classes.setdefault(time, set()).add(item)
                assert item in history[-1]
                if time:
                    assert item not in history[time - 1]
                    assert item in history[time]
                    assert all(item in history[index] for index in range(time, len(history)))
                else:
                    assert all(item in state for state in history)
            assert sum(len(group) for group in classes.values()) == len(history[-1])
            live_items += len(history[-1])
            checked += 1
    return checked, live_items


def check_transition_updates():
    rng = random.Random(1257)
    checked = 0
    created_total = 0
    retired_total = 0
    for universe_size in range(1, 300):
        universe = set(range(universe_size))
        for _ in range(300):
            old = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            new = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            retired = old - new
            created = new - old
            survived = old & new
            assert len(new) - len(old) == len(created) - len(retired)
            assert old == retired | survived
            assert new == created | survived
            assert retired.isdisjoint(survived)
            assert created.isdisjoint(survived)
            created_total += len(created)
            retired_total += len(retired)
            checked += 1
    return checked, created_total, retired_total


def check_owner_credit_loads():
    rng = random.Random(1258)
    checked = 0
    owned_credits = 0
    for cell_count in range(3, 100):
        cells = tuple(range(cell_count))
        possible = list(combinations(cells, 3))
        for _ in range(160):
            target_count = rng.randint(0, min(300, len(possible)))
            targets = set(rng.sample(possible, target_count))
            owner_groups = {cell: [] for cell in cells}
            for target in targets:
                owner = rng.choice(target)
                owner_groups[owner].append(target)
            degree = {
                cell: sum(cell in target for target in targets)
                for cell in cells
            }
            for cell in cells:
                assert len(owner_groups[cell]) <= degree[cell]
                assert all(cell in target for target in owner_groups[cell])
                owned_credits += len(owner_groups[cell])
            checked += 1
    return checked, owned_credits


def check_owner_removal_retires_credits():
    rng = random.Random(1259)
    checked = 0
    retired = 0
    for cell_count in range(3, 100):
        cells = tuple(range(cell_count))
        possible = list(combinations(cells, 3))
        for _ in range(200):
            targets = set(rng.sample(possible, rng.randint(0, min(250, len(possible)))))
            owner = rng.choice(cells)
            credits = {target for target in targets if owner in target and rng.random() < 0.6}
            later = {target for target in targets if owner not in target}
            assert credits.isdisjoint(later)
            assert len(targets - later) >= len(credits)
            retired += len(credits)
            checked += 1
    return checked, retired


def check_layer_reassignment_invariance():
    rng = random.Random(1260)
    checked = 0
    for cell_count in range(3, 100):
        cells = tuple(range(cell_count))
        for _ in range(300):
            triple = tuple(rng.sample(cells, 3))
            labels_before = {cell: rng.randint(0, 1) for cell in triple}
            labels_after = {cell: 1 - labels_before[cell] if rng.random() < 0.5 else labels_before[cell] for cell in triple}
            physical_before = set(labels_before)
            physical_after = set(labels_after)
            assert physical_before == physical_after
            created = physical_after - physical_before
            assert not created
            checked += 1
    return checked


def main():
    creation = check_last_creation_partition()
    updates = check_transition_updates()
    owners = check_owner_credit_loads()
    removal = check_owner_removal_retires_credits()
    print(
        "verified collateral credit ledger:",
        creation[0],
        "histories with",
        creation[1],
        "live credits,",
        updates[0],
        "transitions creating",
        updates[1],
        "and retiring",
        updates[2],
        "credits,",
        owners[0],
        "owner-load cases with",
        owners[1],
        "owned credits,",
        removal[0],
        "owner removals retiring",
        removal[1],
        "credits, and",
        check_layer_reassignment_invariance(),
        "layer-reassignment cases",
    )


if __name__ == "__main__":
    main()

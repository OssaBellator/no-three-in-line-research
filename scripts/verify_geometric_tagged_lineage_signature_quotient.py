#!/usr/bin/env python3
"""Finite audit for tagged-lineage signature quotient and recycling cycles."""

from __future__ import annotations

from itertools import product
from math import prod
from random import Random


def count_vector(named: dict[int, int], p: int) -> tuple[int, ...]:
    counts = [0] * p
    for sig in named.values():
        counts[sig] += 1
    return tuple(counts)


def exhaustive_state_stock() -> tuple[int, int]:
    systems = 0
    states = 0
    for p in range(1, 6):
        for caps in product(range(4), repeat=p):
            enumerated = list(product(*[range(c + 1) for c in caps]))
            assert len(enumerated) == prod(c + 1 for c in caps)
            for u in enumerated:
                assert all(0 <= u[i] <= caps[i] for i in range(p))
            systems += 1
            states += len(enumerated)
    return systems, states


def named_quotient_checks(seed: int = 20260727, systems: int = 50000) -> tuple[int, int, int]:
    rng = Random(seed)
    transitions = 0
    retired_lineages = 0
    recreation_checks = 0

    for _ in range(systems):
        p = rng.randint(1, 7)
        caps = [rng.randint(1, 5) for _ in range(p)]
        weights = [rng.randint(1, 9) for _ in range(p)]

        next_id = 0
        named: dict[int, int] = {}
        for sig, cap in enumerate(caps):
            for _ in range(rng.randint(0, cap)):
                named[next_id] = sig
                next_id += 1

        retired: set[int] = set()
        static_phi = rng.randint(0, 30)

        for _step in range(rng.randint(1, 35)):
            before_counts = count_vector(named, p)
            ids_by_sig: list[list[int]] = [[] for _ in range(p)]
            for lid, sig in named.items():
                ids_by_sig[sig].append(lid)

            destroy_counts = [rng.randint(0, len(ids_by_sig[sig])) for sig in range(p)]
            remaining = [before_counts[sig] - destroy_counts[sig] for sig in range(p)]
            create_counts = [rng.randint(0, caps[sig] - remaining[sig]) for sig in range(p)]

            for sig in range(p):
                chosen = ids_by_sig[sig][: destroy_counts[sig]]
                for lid in chosen:
                    assert lid not in retired
                    retired.add(lid)
                    del named[lid]
                    retired_lineages += 1

            for sig in range(p):
                for _ in range(create_counts[sig]):
                    named[next_id] = sig
                    assert next_id not in retired
                    next_id += 1
                    recreation_checks += 1

            after_counts = count_vector(named, p)
            expected = tuple(
                before_counts[sig] - destroy_counts[sig] + create_counts[sig]
                for sig in range(p)
            )
            assert after_counts == expected
            assert all(after_counts[sig] <= caps[sig] for sig in range(p))

            D = sum(destroy_counts[sig] * weights[sig] for sig in range(p))
            N = sum(create_counts[sig] * weights[sig] for sig in range(p))
            T_before = static_phi + sum(before_counts[sig] * weights[sig] for sig in range(p))
            U_before = sum(before_counts[sig] * weights[sig] for sig in range(p))
            T_after = static_phi + sum(after_counts[sig] * weights[sig] for sig in range(p))
            U_after = sum(after_counts[sig] * weights[sig] for sig in range(p))
            assert T_after == T_before - D + N
            assert U_after == U_before - D + N
            assert T_after - U_after == T_before - U_before == static_phi
            transitions += 1

    return transitions, retired_lineages, recreation_checks


def rename_invariance(seed: int = 17, systems: int = 30000) -> int:
    rng = Random(seed)
    checks = 0
    for _ in range(systems):
        p = rng.randint(1, 6)
        caps = [rng.randint(1, 5) for _ in range(p)]
        counts = [rng.randint(0, cap) for cap in caps]

        named_a: dict[int, int] = {}
        named_b: dict[int, int] = {}
        a_id = 0
        b_id = 10000
        for sig, count in enumerate(counts):
            for _ in range(count):
                named_a[a_id] = sig
                named_b[b_id] = sig
                a_id += 1
                b_id += rng.randint(1, 3)

        assert count_vector(named_a, p) == count_vector(named_b, p)

        destroy = [rng.randint(0, counts[sig]) for sig in range(p)]
        remaining = [counts[sig] - destroy[sig] for sig in range(p)]
        create = [rng.randint(0, caps[sig] - remaining[sig]) for sig in range(p)]
        expected = tuple(remaining[sig] + create[sig] for sig in range(p))

        for named in (named_a, named_b):
            ids_by_sig = [[] for _ in range(p)]
            for lid, sig in named.items():
                ids_by_sig[sig].append(lid)
            for sig in range(p):
                for lid in ids_by_sig[sig][: destroy[sig]]:
                    del named[lid]
            new_id = max(named.keys(), default=0) + 100
            for sig in range(p):
                for _ in range(create[sig]):
                    named[new_id] = sig
                    new_id += 1
            assert count_vector(named, p) == expected
        checks += 1
    return checks


def cycle_erasure_checks(seed: int = 91, systems: int = 30000) -> tuple[int, int]:
    rng = Random(seed)
    repeated = 0
    erased_steps = 0
    for _ in range(systems):
        n = rng.randint(1, 80)
        nxt = [rng.randrange(n) for _ in range(n)]
        terminal = [rng.randrange(5) for _ in range(n)]
        start = rng.randrange(n)
        horizon = rng.randint(n + 1, 4 * n + 10)

        path = [start]
        for _step in range(horizon):
            path.append(nxt[path[-1]])

        seen: dict[int, int] = {}
        pair = None
        for j, state in enumerate(path):
            if state in seen:
                pair = (seen[state], j)
                break
            seen[state] = j
        assert pair is not None
        i, j = pair
        assert path[i] == path[j]

        replay = path[i]
        for _ in range(len(path) - 1 - j):
            replay = nxt[replay]
        assert replay == path[-1]
        assert terminal[path[i]] == terminal[path[j]]
        repeated += 1
        erased_steps += j - i
    return repeated, erased_steps


def main() -> None:
    stock_systems, states = exhaustive_state_stock()
    transitions, retired, recreated = named_quotient_checks()
    rename = rename_invariance()
    repeated, erased = cycle_erasure_checks()
    print("tagged-lineage signature-quotient audit passed")
    print(f"  capacity systems: {stock_systems}")
    print(f"  exact quotient states: {states}")
    print(f"  tagged-only transitions: {transitions}")
    print(f"  retired lineage ids: {retired}")
    print(f"  new lineage recreations: {recreated}")
    print(f"  rename-invariance systems: {rename}")
    print(f"  repeated quotient states: {repeated}")
    print(f"  erased recycling steps: {erased}")


if __name__ == "__main__":
    main()

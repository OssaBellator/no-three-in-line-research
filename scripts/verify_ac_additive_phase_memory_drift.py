#!/usr/bin/env python3
"""Finite audit for AC3rf--AC3rj additive phase-memory drift."""

from __future__ import annotations

from itertools import product
from math import comb, gcd
from random import Random


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def step(state: tuple[int, ...], edge: int) -> tuple[int, ...] | None:
    if state[edge] == 0:
        return None
    m = len(state)
    out = list(state)
    out[edge] -= 1
    out[(edge + 1) % m] += 1
    return tuple(out)


def element_order(value: int, modulus: int) -> int:
    if modulus == 1 or value % modulus == 0:
        return 1
    return modulus // gcd(value, modulus)


def exhaustive_return_audit() -> dict[str, int]:
    counts = {
        "occupancies": 0,
        "path_nodes": 0,
        "returns": 0,
        "return_edges": 0,
    }
    patterns = [
        lambda m: [i - (m // 2) for i in range(m)],
        lambda m: [(-1) ** i for i in range(m)],
        lambda m: [0] * m,
    ]
    for m in range(1, 5):
        for total in range(0, 5):
            expected = comb(total + m - 1, m - 1)
            states = list(compositions(total, m))
            assert len(states) == expected
            counts["occupancies"] += len(states)
            for start in states:
                stack = [(start, (), [start])]
                while stack:
                    state, word, visited = stack.pop()
                    counts["path_nodes"] += 1
                    if word and state == start:
                        edge_counts = [word.count(i) for i in range(m)]
                        assert len(set(edge_counts)) == 1
                        k = edge_counts[0]
                        assert k >= 1
                        assert len(word) == k * m
                        counts["returns"] += 1
                        counts["return_edges"] += len(word)
                        for make_delta in patterns:
                            delta = make_delta(m)
                            cycle_drift = sum(delta)
                            observed = sum(delta[i] for i in word)
                            assert observed == k * cycle_drift
                            for modulus in range(1, 9):
                                gamma = [(2 * i + 1) % modulus for i in range(m)]
                                complete = sum(gamma) % modulus
                                mod_observed = sum(gamma[i] for i in word) % modulus
                                assert mod_observed == (k * complete) % modulus
                                order = element_order(complete, modulus)
                                assert ((k * complete) % modulus == 0) == (k % order == 0)
                    if len(word) == 7:
                        continue
                    for edge in range(m):
                        nxt = step(state, edge)
                        if nxt is not None:
                            stack.append((nxt, word + (edge,), visited + [nxt]))
    return counts


def random_zero_drift_audit(rng: Random, trials: int = 30000) -> dict[str, int]:
    repeats = 0
    transitions = 0
    for _ in range(trials):
        m = rng.randint(1, 8)
        total = rng.randint(1, 12)
        state = list(rng.choice(list(compositions(total, m))))
        delta = [rng.randint(-4, 4) for _ in range(max(0, m - 1))]
        delta.append(-sum(delta))
        h = rng.randint(-1000, 1000)
        seen: dict[tuple[int, ...], int] = {tuple(state): h}
        for _ in range(rng.randint(1, 250)):
            legal = [i for i, x in enumerate(state) if x > 0]
            edge = rng.choice(legal)
            state[edge] -= 1
            state[(edge + 1) % m] += 1
            h += delta[edge]
            transitions += 1
            key = tuple(state)
            if key in seen:
                assert seen[key] == h
                repeats += 1
            else:
                seen[key] = h
        assert len(seen) <= comb(total + m - 1, m - 1)
    return {"random_transitions": transitions, "zero_drift_repeats": repeats}


def bounded_drift_audit(rng: Random, trials: int = 50000) -> dict[str, int]:
    return_blocks = 0
    modular_tests = 0
    for _ in range(trials):
        drift = rng.choice([i for i in range(-12, 13) if i])
        lower = rng.randint(-50, 0)
        upper = rng.randint(0, 50)
        h = rng.randint(lower, upper)
        direction = 1 if drift > 0 else -1
        max_blocks = (upper - lower) // abs(drift)
        blocks = 0
        while True:
            k = rng.randint(1, 5)
            nxt = h + k * drift
            if not (lower <= nxt <= upper):
                break
            assert (nxt - h) * direction > 0
            h = nxt
            blocks += 1
        assert blocks <= max_blocks
        return_blocks += blocks

        modulus = rng.randint(1, 100)
        gamma = rng.randrange(modulus)
        order = element_order(gamma, modulus)
        assert 1 <= order <= modulus
        for k in range(1, min(30, 2 * modulus + 1)):
            assert ((k * gamma) % modulus == 0) == (k % order == 0)
            modular_tests += 1
    return {"bounded_return_blocks": return_blocks, "modular_tests": modular_tests}


def main() -> None:
    rng = Random(0xAC3F)
    counts = exhaustive_return_audit()
    counts.update(random_zero_drift_audit(rng))
    counts.update(bounded_drift_audit(rng))
    print("AC additive phase-memory drift audit passed")
    for key, value in counts.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

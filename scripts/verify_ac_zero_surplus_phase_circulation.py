#!/usr/bin/env python3
from __future__ import annotations

import math
import random

SEED = 20260727
RNG = random.Random(SEED)


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def step(state: tuple[int, ...], edge: int) -> tuple[int, ...]:
    m = len(state)
    assert state[edge] > 0
    out = list(state)
    out[edge] -= 1
    out[(edge + 1) % m] += 1
    return tuple(out)


def phi(state: tuple[int, ...]) -> int:
    m = len(state)
    return sum(i * x for i, x in enumerate(state)) % m if m > 1 else 0


def check_return(edges: list[int], states: list[tuple[int, ...]]) -> None:
    assert states[0] == states[-1]
    m = len(states[0])
    counts = [edges.count(i) for i in range(m)]
    assert min(counts) == max(counts)
    assert sum(counts) == counts[0] * m


def exhaustive_checks() -> tuple[int, int, int]:
    stocks = 0
    paths = 0
    returns = 0
    for m in range(1, 5):
        for B in range(0, 4):
            occs = list(compositions(B, m))
            assert len(occs) == math.comb(B + m - 1, m - 1)
            stocks += len(occs)
            for start in occs:
                stack = [(start, [], [start])]
                while stack:
                    state, edges, states = stack.pop()
                    paths += 1
                    if edges and state == start:
                        check_return(edges, states)
                        returns += 1
                    if len(edges) == 5:
                        continue
                    for i, x in enumerate(state):
                        if x == 0:
                            continue
                        nxt = step(state, i)
                        if m > 1:
                            assert phi(nxt) == (phi(state) + 1) % m
                        stack.append((nxt, edges + [i], states + [nxt]))
    return stocks, paths, returns


def first_repeat(states: list[tuple[tuple[int, ...], int]]):
    latest: dict[tuple[tuple[int, ...], int], int] = {}
    for j, state in enumerate(states):
        if state in latest:
            return latest[state], j
        latest[state] = j
    return None


def random_composition(total: int, parts: int) -> tuple[int, ...]:
    out = [0] * parts
    for _ in range(total):
        out[RNG.randrange(parts)] += 1
    return tuple(out)


def random_history_checks(trials: int = 20_000) -> tuple[int, int, int]:
    repeated = 0
    return_steps = 0
    max_simple = 0
    for _ in range(trials):
        m = RNG.randint(1, 9)
        B = RNG.randint(1, 18)
        q = RNG.randint(1, 6)
        state = random_composition(B, m)
        xi = RNG.randrange(q)
        decorated = [(state, xi)]
        edges: list[int] = []
        n_phase = q * math.comb(B + m - 1, m - 1)
        for _t in range(min(n_phase + 3, 350)):
            legal = [i for i, x in enumerate(state) if x > 0]
            edge = RNG.choice(legal)
            state = step(state, edge)
            xi = (xi + 1 + edge) % q
            edges.append(edge)
            decorated.append((state, xi))
            rep = first_repeat(decorated)
            if rep is not None:
                i, j = rep
                assert j - i <= n_phase
                internal = decorated[i:j]
                assert len(internal) == len(set(internal))
                segment_edges = edges[i:j]
                segment_states = [s for s, _ in decorated[i : j + 1]]
                check_return(segment_edges, segment_states)
                repeated += 1
                return_steps += j - i
                max_simple = max(max_simple, j - i)
                break
    return repeated, return_steps, max_simple


def quotient_decomposition_checks(trials: int = 8_000) -> tuple[int, int]:
    removed_cycles = 0
    residual_steps = 0
    for _ in range(trials):
        m = RNG.randint(1, 7)
        B = RNG.randint(1, 12)
        q = RNG.randint(1, 5)
        occ = random_composition(B, m)
        xi = RNG.randrange(q)
        states = [(occ, xi)]
        edges: list[int] = []
        for _t in range(RNG.randint(10, 100)):
            legal = [i for i, x in enumerate(occ) if x > 0]
            e = RNG.choice(legal)
            occ = step(occ, e)
            xi = (xi + e + 1) % q
            edges.append(e)
            states.append((occ, xi))

        while True:
            seen = {}
            pair = None
            for j, st in enumerate(states):
                if st in seen:
                    pair = (seen[st], j)
                    break
                seen[st] = j
            if pair is None:
                break
            i, j = pair
            segment_edges = edges[i:j]
            segment_states = [s for s, _ in states[i : j + 1]]
            check_return(segment_edges, segment_states)
            states = states[: i + 1] + states[j + 1 :]
            edges = edges[:i] + edges[j:]
            removed_cycles += 1
        n_phase = q * math.comb(B + m - 1, m - 1)
        assert len(states) - 1 <= n_phase - 1
        residual_steps += len(states) - 1
    return removed_cycles, residual_steps


def main() -> None:
    stocks, paths, returns = exhaustive_checks()
    repeated, return_steps, max_simple = random_history_checks()
    removed, residual = quotient_decomposition_checks()
    print(
        "PASS AC zero-surplus phase audit:",
        f"{stocks} phase occupancies;",
        f"{paths} exhaustive path nodes;",
        f"{returns} exhaustive returns;",
        f"{repeated} random repeated states;",
        f"{return_steps} return transitions;",
        f"max simple cycle {max_simple};",
        f"{removed} quotient cycles removed;",
        f"{residual} residual transitions.",
    )


if __name__ == "__main__":
    main()

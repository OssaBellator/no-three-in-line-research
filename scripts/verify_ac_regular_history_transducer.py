#!/usr/bin/env python3
"""Finite audit for AC3so--AC3ss."""

from collections import defaultdict
from itertools import product
import random

SEED = 20260727


def extend(delta, state, word):
    for symbol in word:
        state = delta[state][symbol]
    return state


def exhaustive_automata(counts):
    for q in range(1, 4):
        for s in range(1, 3):
            for flat in product(range(q), repeat=q * s):
                delta = [list(flat[i * s:(i + 1) * s]) for i in range(q)]
                counts["automata"] += 1

                for start in range(q):
                    for ell in range(4):
                        for word in product(range(s), repeat=ell):
                            mid = extend(delta, start, word)
                            for m in range(3):
                                for continuation in product(range(s), repeat=m):
                                    assert extend(delta, mid, continuation) == extend(
                                        delta, start, word + continuation
                                    )
                                    counts["continuations"] += 1

                transformations = set()
                for ell in range(4):
                    for word in product(range(s), repeat=ell):
                        transformations.add(
                            tuple(extend(delta, state, word) for state in range(q))
                        )
                assert len(transformations) <= q ** q
                counts["transformations"] += len(transformations)


def sampled_decorated_transducers(counts):
    rng = random.Random(SEED)
    for _ in range(5000):
        q = rng.randint(1, 8)
        s = rng.randint(1, 4)
        x_size = rng.randint(1, 5)
        width = rng.randint(0, 8)
        delta = [[rng.randrange(q) for _ in range(s)] for _ in range(q)]

        states = [
            (x, h, automaton)
            for x in range(x_size)
            for h in range(width + 1)
            for automaton in range(q)
        ]
        n_reg = x_size * (width + 1) * q
        assert len(states) == n_reg

        transition = {
            (state, symbol): (
                rng.randrange(x_size),
                rng.randrange(width + 1),
                delta[state[2]][symbol],
            )
            for state in states
            for symbol in range(s)
        }

        current = rng.choice(states)
        seen = {current: 0}
        path = [current]
        events = []
        repeat = None

        for time in range(1, n_reg + 2):
            symbol = rng.randrange(s)
            events.append(symbol)
            current = transition[(current, symbol)]
            path.append(current)
            if current in seen:
                repeat = (seen[current], time)
                break
            seen[current] = time

        assert repeat is not None
        start, end = repeat
        assert end - start <= n_reg
        assert extend(delta, path[start][2], events[start:end]) == path[start][2]
        assert len(set(path[start:end])) == end - start

        counts["sample_systems"] += 1
        counts["states"] += n_reg
        counts["cycle_steps"] += end - start


def main():
    counts = defaultdict(int)
    exhaustive_automata(counts)
    sampled_decorated_transducers(counts)

    print("AC regular-history transducer audit passed")
    print(f"  deterministic automata: {counts['automata']}")
    print(f"  continuation identities: {counts['continuations']}")
    print(f"  induced transformations: {counts['transformations']}")
    print(f"  sampled decorated systems: {counts['sample_systems']}")
    print(f"  exact augmented states: {counts['states']}")
    print(f"  extracted simple-cycle steps: {counts['cycle_steps']}")


if __name__ == "__main__":
    main()

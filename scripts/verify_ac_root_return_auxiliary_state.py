#!/usr/bin/env python3
"""Finite audit for AC3tn--AC3tr."""

from collections import defaultdict
import random

SEED = 20260727


def compose(first, second):
    """Return second o first for partial maps represented by None."""
    result = []
    for value in first:
        result.append(None if value is None else second[value])
    return tuple(result)


def simulate(word, start, gates):
    state = start
    for gate in word:
        state = gates[gate][state]
        assert state is not None
    return state


def least_ending_repeat(states):
    first = {}
    for end, state in enumerate(states):
        if state in first:
            return first[state], end
        first[state] = end
    return None


def erase_cycles(word, start, gates):
    original_end = simulate(word, start, gates)
    word = list(word)
    removed = 0

    while True:
        states = [start]
        for gate in word:
            next_state = gates[gate][states[-1]]
            assert next_state is not None
            states.append(next_state)

        repeat = least_ending_repeat(states)
        if repeat is None:
            break

        begin, end = repeat
        assert states[begin] == states[end]
        del word[begin:end]
        removed += 1
        assert simulate(word, start, gates) == original_end

    return tuple(word), removed


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(30000):
        a = rng.randint(1, 8)
        k = rng.randint(1, 6)
        length_cap = rng.randint(1, 25)
        gate_lengths = [rng.randint(1, length_cap) for _ in range(k)]

        # Gate zero is total, so arbitrarily long legal histories exist.
        gates = [tuple(rng.randrange(a) for _ in range(a))]
        for _gate in range(1, k):
            row = []
            for _state in range(a):
                row.append(None if rng.random() < 0.25 else rng.randrange(a))
            gates.append(tuple(row))

        assert len(set(gates)) <= (a + 1) ** a

        for _check in range(8):
            first = rng.choice(gates)
            second = rng.choice(gates)
            combined = compose(first, second)
            for state in range(a):
                middle = first[state]
                expected = None if middle is None else second[middle]
                assert combined[state] == expected
            counts["composition_checks"] += a

        start = rng.randrange(a)
        word = []
        states = [start]

        for _step in range(3 * a + 5):
            state = states[-1]
            legal = [index for index, gate in enumerate(gates) if gate[state] is not None]
            chosen = rng.choice(legal)
            word.append(chosen)
            states.append(gates[chosen][state])

        begin, end = least_ending_repeat(states)
        assert end <= a
        assert 1 <= end - begin <= a
        assert states[begin] == states[end]
        assert len(set(states[begin:end])) == end - begin

        cycle_word = word[begin:end]
        assert simulate(cycle_word, states[begin], gates) == states[begin]
        edge_length = sum(gate_lengths[gate] for gate in cycle_word)
        assert edge_length <= a * length_cap

        residual, removed = erase_cycles(word, start, gates)
        assert len(residual) < a
        assert sum(gate_lengths[gate] for gate in residual) < a * length_cap

        counts["systems"] += 1
        counts["gate_addresses"] += k
        counts["generated_gate_steps"] += len(word)
        counts["cycle_gate_steps"] += len(cycle_word)
        counts["cycle_edge_steps"] += edge_length
        counts["erased_cycles"] += removed
        counts["residual_gate_steps"] += len(residual)

    print("AC root-return auxiliary-state audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()

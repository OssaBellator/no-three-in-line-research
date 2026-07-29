#!/usr/bin/env python3
"""Finite audit for AC3uw--AC3va."""

from itertools import product


def endpoint_walk(increments, start):
    states = [tuple(start)]
    cur = list(start)
    for inc in increments:
        cur = [x + d for x, d in zip(cur, inc)]
        if any(x < 0 for x in cur):
            return None
        states.append(tuple(cur))
    return states


def canonical_low_pair(states, beta):
    candidates = []
    q = len(beta)
    for i in range(q):
        h = min(state[i] for state in states[:-1])
        if h < beta[i]:
            positions = [t for t, state in enumerate(states[:-1]) if state[i] == h]
            candidates.append((i, h, min(positions)))
    return min(candidates) if candidates else None


def rotate_increments(increments, pos):
    return increments[pos:] + increments[:pos]


def classify(increments, start, beta):
    states = endpoint_walk(increments, start)
    assert states is not None and states[-1] == states[0]
    pair = canonical_low_pair(states, beta)
    if pair is None:
        return "buffer-rich", None
    i, h, pos = pair
    rotated = rotate_increments(increments, pos)
    rotated_states = endpoint_walk(rotated, states[pos])
    assert rotated_states[-1] == rotated_states[0]
    assert rotated_states[0][i] == h
    values = [state[i] for state in rotated_states]
    if all(value == h for value in values):
        assert all(inc[i] == 0 for inc in rotated)
        return "face", (i, h)

    a = next(t for t in range(1, len(values)) if values[t] != h)
    assert values[a] > h and values[a - 1] == h
    b = next(t for t in range(a + 1, len(values)) if values[t] == h)
    assert all(values[t] > h for t in range(a, b))
    return "excursion", (i, h, a, b)


def audit_capacity_one(excursions, recreated):
    """Each nonrecreated lineage may close at most one excursion."""
    spent = set()
    recreation_gates = 0
    for lineage in excursions:
        if lineage in recreated:
            recreation_gates += 1
            continue
        assert lineage not in spent
        spent.add(lineage)
    return len(spent), recreation_gates


def main():
    increments_1d = [(x,) for x in range(-2, 3)]
    checked = 0
    faces = 0
    excursions = 0

    for length in range(1, 7):
        for word in product(increments_1d, repeat=length):
            if sum(v[0] for v in word) != 0:
                continue
            for start in range(5):
                states = endpoint_walk(list(word), (start,))
                if states is None or states[-1] != states[0]:
                    continue
                kind, _ = classify(list(word), (start,), (3,))
                checked += 1
                faces += kind == "face"
                excursions += kind == "excursion"

    increments_2d = list(product(range(-1, 2), repeat=2))
    for length in range(1, 6):
        for word in product(increments_2d, repeat=length):
            if any(sum(v[i] for v in word) != 0 for i in range(2)):
                continue
            for start in product(range(3), repeat=2):
                states = endpoint_walk(list(word), start)
                if states is None or states[-1] != states[0]:
                    continue
                classify(list(word), start, (2, 2))
                checked += 1
                if checked > 120000:
                    break
            if checked > 120000:
                break
        if checked > 120000:
            break

    spent, gates = audit_capacity_one(
        excursions=[("i0", 0, "u0"), ("i0", 0, "u1"), ("i0", 0, "u0")],
        recreated={("i0", 0, "u0")},
    )
    assert spent == 1 and gates == 2

    assert checked > 10000
    assert faces > 0
    assert excursions > 0
    print("AC low-buffer recurrence audit passed")
    print(f"  closed walks checked: {checked}")
    print(f"  one-dimensional face cases: {faces}")
    print(f"  one-dimensional excursion cases: {excursions}")
    print(f"  nonrecreated tickets spent: {spent}")
    print(f"  recreation gates exposed: {gates}")


if __name__ == "__main__":
    main()

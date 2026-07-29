#!/usr/bin/env python3
"""Finite audit for AC3vb--AC3vf."""

from itertools import product


def first_recreation_gate(states, atoms):
    """Return the canonical least-atom first-destruction/restoration gate."""
    n = len(states) - 1
    assert states[0] == states[-1]
    changed = []
    for a in atoms:
        for i in range(n):
            if a in states[i] and a not in states[i + 1]:
                changed.append((a, i))
                break
    if not changed:
        return None
    a, d = min(changed)
    j = (d + 1) % n
    while j != d:
        before = states[j]
        after = states[(j + 1) % n]
        if a not in before and a in after:
            return a, d, j
        j = (j + 1) % n
    raise AssertionError("exact return must restore the destroyed atom")


def main():
    atoms = tuple(range(4))
    checked = 0
    tickets = set()
    # Closed walks of length 4 on the Boolean atom cube.
    for raw in product(range(1 << len(atoms)), repeat=4):
        states = [frozenset(a for a in atoms if mask >> a & 1) for mask in raw]
        states.append(states[0])
        gate = first_recreation_gate(states, atoms)
        checked += 1
        if gate is None:
            assert all(states[i] == states[i + 1] for i in range(4))
            continue
        a, d, r = gate
        assert a in states[d] and a not in states[d + 1]
        assert a not in states[r] and a in states[(r + 1) % 4]
        # The address is atom plus restoration edge. Capacity one is an external
        # contract, but the finite address stock is exact.
        tickets.add((a, r))
    assert len(tickets) <= len(atoms) * 4
    print("AC finite recreation-cycle audit passed")
    print(f"  closed walks checked: {checked}")
    print(f"  restoration addresses: {len(tickets)}")
    print(f"  address bound: {len(atoms) * 4}")


if __name__ == "__main__":
    main()

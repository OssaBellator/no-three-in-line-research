#!/usr/bin/env python3
"""Finite audit for BDA5bg--BDA5bk."""

from itertools import product


def canonical_support_gate(states):
    n = len(states) - 1
    assert states[0] == states[-1]
    atoms = sorted(set().union(*states))
    choices = []
    for atom in atoms:
        for i in range(n):
            if atom in states[i] and atom not in states[i + 1]:
                choices.append((atom, i))
                break
    if not choices:
        return None
    atom, i = min(choices)
    for step in range(1, n + 1):
        j = (i + step) % n
        if atom not in states[j] and atom in states[(j + 1) % n]:
            return atom, i, j
    raise AssertionError("closed support cycle did not restore atom")


def main():
    checked = 0
    gate_addresses = set()
    # Simple profile cycles are represented here by support words; the
    # denominator/profile labels are held fixed.
    for masks in product(range(8), repeat=5):
        if masks[0] != masks[-1]:
            continue
        states = [frozenset(i for i in range(3) if m >> i & 1) for m in masks]
        gate = canonical_support_gate(states)
        checked += 1
        if gate is None:
            assert all(states[i] == states[i + 1] for i in range(4))
        else:
            atom, destroy, restore = gate
            assert atom in states[destroy]
            assert atom not in states[destroy + 1]
            assert atom not in states[restore]
            assert atom in states[(restore + 1) % 4]
            gate_addresses.add((atom, restore))
    assert len(gate_addresses) <= 3 * 4
    print("BDA cycle-lineage audit passed")
    print(f"  closed support words checked: {checked}")
    print(f"  canonical gate addresses: {len(gate_addresses)}")
    print("  address bound: 12")


if __name__ == "__main__":
    main()

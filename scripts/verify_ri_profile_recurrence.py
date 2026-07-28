#!/usr/bin/env python3
"""Finite audit for RI5ay--RI5bc."""

from itertools import product


def canonical_gate(states):
    n = len(states) - 1
    assert states[0] == states[-1]
    atoms = sorted(set().union(*(s[0] for s in states)))
    for atom in atoms:
        for i in range(n):
            if atom in states[i][0] and atom not in states[i + 1][0]:
                for step in range(1, n + 1):
                    j = (i + step) % n
                    if atom not in states[j][0] and atom in states[(j + 1) % n][0]:
                        return ("occurrence", atom, i, j)
    # Support fixed: use the least changing finite label.
    width = len(states[0][1])
    for k in range(width):
        for i in range(n):
            if states[i][1][k] != states[i + 1][1][k]:
                return ("label", k, i, None)
    return None


def main():
    checked = 0
    occurrence_gates = set()
    label_gates = set()
    # Rank-three profiles need at most six support vertices.  Use three here for
    # exhaustive support checking and two finite labels.
    for masks in product(range(8), repeat=4):
        for labels in product(range(4), repeat=4):
            if masks[0] != masks[-1] or labels[0] != labels[-1]:
                continue
            states = []
            for mask, lab in zip(masks, labels):
                support = frozenset(i for i in range(3) if mask >> i & 1)
                states.append((support, (lab // 2, lab % 2)))
            gate = canonical_gate(states)
            checked += 1
            if gate is None:
                assert all(states[i] == states[i + 1] for i in range(3))
            elif gate[0] == "occurrence":
                _, atom, d, r = gate
                occurrence_gates.add((atom, r))
                assert atom in states[d][0] and atom not in states[d + 1][0]
                assert atom not in states[r][0] and atom in states[(r + 1) % 3][0]
            else:
                _, field, edge, _ = gate
                label_gates.add((field, edge))
                assert states[edge][1][field] != states[edge + 1][1][field]
    print("RI exact-profile recurrence audit passed")
    print(f"  closed profile words checked: {checked}")
    print(f"  occurrence gate addresses: {len(occurrence_gates)}")
    print(f"  label gate addresses: {len(label_gates)}")


if __name__ == "__main__":
    main()

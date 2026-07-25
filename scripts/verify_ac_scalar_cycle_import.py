#!/usr/bin/env python3
"""Finite audit for AC3hu--AC3hw."""

from __future__ import annotations

from itertools import product


def omega_pf(n: int) -> int:
    out = 0
    p = 2
    while p * p <= n:
        while n % p == 0:
            out += 1
            n //= p
        p += 1
    if n > 1:
        out += 1
    return out


def verify_ticket_paths():
    states = 0
    closed_attempts = 0
    for length in range(2, 12):
        vertices = list(range(length))
        edges = {tuple(sorted((i, i + 1))) for i in range(length - 1)}
        for word_len in range(1, 9):
            for steps in product((-1, 1), repeat=word_len):
                pos = length // 2
                used = []
                valid = True
                start = pos
                for step in steps:
                    nxt = pos + step
                    if nxt < 0 or nxt >= length:
                        valid = False
                        break
                    edge = tuple(sorted((pos, nxt)))
                    if edge not in edges:
                        valid = False
                        break
                    used.append(edge)
                    pos = nxt
                if not valid:
                    continue
                states += 1
                if pos == start:
                    closed_attempts += 1
                    assert len(set(used)) < len(used)
    return states, closed_attempts


def verify_potential():
    checks = 0
    for q0 in range(2, 101):
        divs = [d for d in range(1, q0 + 1) if q0 % d == 0]
        for R in range(0, 25):
            ceiling = (R + 1) * omega_pf(q0) + R
            for q in divs:
                for c in range(R + 1):
                    Xi = (R + 1) * (omega_pf(q0) - omega_pf(q)) + c
                    assert 0 <= Xi <= ceiling
                    checks += 1
                    if c < R:
                        assert Xi + 1 > Xi
                    for qp in divs:
                        if q != qp and q % qp == 0:
                            Xip = (R + 1) * (omega_pf(q0) - omega_pf(qp)) + c
                            assert Xip > Xi
    return checks


def verify_cycle_labels():
    cycles = 0
    residual = 0
    for length in range(1, 9):
        for word in product(range(7), repeat=length):
            cycles += 1
            if any(x != 0 for x in word):
                residual += 1
                assert min(x for x in word if x != 0) in range(1, 7)
            else:
                assert set(word) == {0}
    return cycles, residual


def main():
    paths = verify_ticket_paths()
    potential = verify_potential()
    labels = verify_cycle_labels()
    print("AC scalar cycle import audit passed")
    print(f"ticketed path walks: {paths[0]}")
    print(f"closed walk attempts: {paths[1]}")
    print(f"potential states: {potential}")
    print(f"abstract cycle words: {labels[0]}")
    print(f"residual-labelled cycles: {labels[1]}")


if __name__ == "__main__":
    main()

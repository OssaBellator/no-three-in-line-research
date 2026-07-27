#!/usr/bin/env python3
"""Finite audit for AC3ru--AC3ry.

Checks the primitive zero-sum relation bound, finite count-vector stock,
zero-sum-free residual bound, exact translation decomposition, and the
ticketed mixed-sign occurrence budget.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import comb
import random


def subset_sum_zero(seq: tuple[int, ...], proper_only: bool = False) -> bool:
    n = len(seq)
    upper = (1 << n) - 1
    for mask in range(1, upper + (0 if proper_only else 1)):
        if proper_only and mask == upper:
            continue
        if sum(seq[i] for i in range(n) if (mask >> i) & 1) == 0:
            return True
    return False


def primitive_zero_sum(seq: tuple[int, ...]) -> bool:
    return bool(seq) and sum(seq) == 0 and not subset_sum_zero(seq, proper_only=True)


def zero_sum_free(seq: tuple[int, ...]) -> bool:
    return not subset_sum_zero(seq)


def greedy_opposite_sign_order(seq: tuple[int, ...]) -> list[int]:
    pos = [x for x in seq if x > 0]
    neg = [x for x in seq if x < 0]
    if not pos:
        return neg
    if not neg:
        return pos
    out = [pos.pop()]
    current = out[0]
    while pos and neg:
        nxt = neg.pop() if current > 0 else pos.pop()
        out.append(nxt)
        current += nxt
    out.extend(pos)
    out.extend(neg)
    return out


def extract_primitive_relations(seq: list[int]) -> tuple[list[tuple[int, ...]], list[int]]:
    remaining = list(seq)
    relations: list[tuple[int, ...]] = []
    while True:
        n = len(remaining)
        found: tuple[int, ...] | None = None
        for mask in range(1, 1 << n):
            sub = tuple(remaining[i] for i in range(n) if (mask >> i) & 1)
            if sum(sub) != 0:
                continue
            changed = True
            work = list(sub)
            while changed:
                changed = False
                for j in range(len(work)):
                    candidate = work[:j] + work[j + 1 :]
                    if candidate and sum(candidate) == 0:
                        work = candidate
                        changed = True
                        break
            found = tuple(work)
            break
        if found is None:
            return relations, remaining
        for x in found:
            remaining.remove(x)
        relations.append(found)


def main() -> None:
    stats: Counter[str] = Counter()

    alphabets = [
        (-2, -1, 1, 2),
        (-3, -1, 2, 4),
        (-4, -2, 1, 3),
    ]
    for alphabet in alphabets:
        P = max(x for x in alphabet if x > 0)
        N = max(-x for x in alphabet if x < 0)
        for length in range(1, 9):
            for seq in product(alphabet, repeat=length):
                if primitive_zero_sum(seq):
                    assert length <= P + N
                    stats["primitive_relations"] += 1
                if zero_sum_free(seq):
                    ordered = greedy_opposite_sign_order(seq)
                    partials: list[int] = []
                    total = 0
                    for x in ordered:
                        total += x
                        partials.append(total)
                    assert 0 not in partials
                    assert len(partials) == len(set(partials))
                    assert length <= P + N + abs(sum(seq))
                    stats["zero_sum_free_sequences"] += 1

        s = len(alphabet)
        safe_stock = comb(P + N + s, s) - 1
        count_vectors = set()
        for length in range(1, P + N + 1):
            for seq in product(alphabet, repeat=length):
                if primitive_zero_sum(seq):
                    count_vectors.add(tuple(seq.count(x) for x in alphabet))
        assert len(count_vectors) <= safe_stock
        stats["primitive_count_vectors"] += len(count_vectors)

    rng = random.Random(20260727)
    for _ in range(40_000):
        alphabet = sorted(
            set(rng.sample(range(-8, 0), rng.randint(1, 4)))
            | set(rng.sample(range(1, 9), rng.randint(1, 4)))
        )
        P = max(x for x in alphabet if x > 0)
        N = max(-x for x in alphabet if x < 0)
        seq = [rng.choice(alphabet) for _ in range(rng.randint(1, 16))]
        relations, residual = extract_primitive_relations(seq)
        assert sum(seq) == sum(residual)
        assert all(sum(rel) == 0 and len(rel) <= P + N for rel in relations)
        assert zero_sum_free(tuple(residual))
        assert len(residual) <= P + N + abs(sum(residual))
        stats["random_decompositions"] += 1
        stats["extracted_relations"] += len(relations)

        R = rng.randint(abs(sum(residual)), abs(sum(residual)) + 30)
        ticket_count = len(relations)
        total_occurrences = sum(len(rel) for rel in relations) + len(residual)
        assert total_occurrences <= (P + N) * ticket_count + P + N + R
        stats["ticket_budget_checks"] += 1

    print("AC mixed-sign translation relation audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()

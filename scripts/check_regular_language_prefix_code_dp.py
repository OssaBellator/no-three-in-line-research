#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import product

P0 = Fraction(3, 4)
P1 = Fraction(2, 3)
RISKS = (Fraction(1, 32), Fraction(1, 16), Fraction(1, 8))
ROOT_MULTIPLICITIES = (3, 2, 1)
START = 1  # state 1 means the previous symbol was not zero
DEAD = 2


def transition(state, bit):
    if state == DEAD:
        return DEAD
    if bit == 0:
        return DEAD if state == 0 else 0
    return 1


def proper_subcounts(counts):
    for sub in product(*(range(x + 1) for x in counts)):
        if all(x == 0 for x in sub) or sub == counts:
            continue
        yield sub


@lru_cache(None)
def constrained_value(state, counts):
    if state == DEAD or sum(counts) == 0:
        return None
    if sum(counts) == 1:
        cls = next(i for i, value in enumerate(counts) if value)
        return RISKS[cls]
    best = None
    for left in proper_subcounts(counts):
        right = tuple(counts[i] - left[i] for i in range(len(counts)))
        vl = constrained_value(transition(state, 0), left)
        vr = constrained_value(transition(state, 1), right)
        if vl is None or vr is None:
            continue
        candidate = max(vl / P0, vr / P1)
        if best is None or candidate < best:
            best = candidate
    return best


@lru_cache(None)
def unconstrained_value(counts):
    if sum(counts) == 1:
        cls = next(i for i, value in enumerate(counts) if value)
        return RISKS[cls]
    best = None
    for left in proper_subcounts(counts):
        right = tuple(counts[i] - left[i] for i in range(len(counts)))
        candidate = max(unconstrained_value(left) / P0, unconstrained_value(right) / P1)
        if best is None or candidate < best:
            best = candidate
    return best


def canonical_split(state, counts):
    target = constrained_value(state, counts)
    candidates = []
    for left in proper_subcounts(counts):
        right = tuple(counts[i] - left[i] for i in range(len(counts)))
        vl = constrained_value(transition(state, 0), left)
        vr = constrained_value(transition(state, 1), right)
        if vl is None or vr is None:
            continue
        candidate = max(vl / P0, vr / P1)
        if candidate == target:
            candidates.append((left, right))
    assert candidates
    return min(candidates)


def reconstruct(state, labels, prefix=""):
    total = sum(len(group) for group in labels)
    if total == 1:
        for cls, group in enumerate(labels):
            if group:
                return [(group[0], cls, prefix)]
    counts = tuple(len(group) for group in labels)
    left_counts, right_counts = canonical_split(state, counts)
    left_labels = tuple(tuple(group[:left_counts[i]]) for i, group in enumerate(labels))
    right_labels = tuple(tuple(group[left_counts[i]:]) for i, group in enumerate(labels))
    return (
        reconstruct(transition(state, 0), left_labels, prefix + "0")
        + reconstruct(transition(state, 1), right_labels, prefix + "1")
    )


def is_prefix_free(words):
    return all(not b.startswith(a) for a in words for b in words if a != b)


def main():
    constrained = constrained_value(START, ROOT_MULTIPLICITIES)
    unconstrained = unconstrained_value(ROOT_MULTIPLICITIES)
    assert constrained == Fraction(243, 1024)
    assert unconstrained == Fraction(3, 16)
    assert constrained > unconstrained

    labels = (
        ("a1", "a2", "a3"),
        ("b1", "b2"),
        ("c1",),
    )
    code = reconstruct(START, labels)
    words = [word for _, _, word in code]
    assert len(code) == 6
    assert is_prefix_free(words)
    assert all("00" not in word for word in words)

    loads = []
    for _, cls, word in code:
        survival = (P0 ** word.count("0")) * (P1 ** word.count("1"))
        loads.append(RISKS[cls] / survival)
    assert max(loads) == constrained

    all_states = []
    for state in (0, 1, DEAD):
        for counts in product(*(range(x + 1) for x in ROOT_MULTIPLICITIES)):
            if sum(counts):
                all_states.append((state, counts, constrained_value(state, counts)))
    feasible_states = sum(value is not None for _, _, value in all_states)

    print({
        "automaton": "forbid 00",
        "multiplicities": ROOT_MULTIPLICITIES,
        "unconstrained_optimum": str(unconstrained),
        "constrained_optimum": str(constrained),
        "canonical_code": [(label, word) for label, _, word in code],
        "feasible_product_states": feasible_states,
        "cached_states": constrained_value.cache_info().currsize,
    })


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checks for CMR870--CMR877."""

from collections import Counter
from math import ceil
import random


def maximal_disjoint_family(supports):
    selected = []
    used = set()
    for support in supports:
        if support.isdisjoint(used):
            selected.append(support)
            used.update(support)
    return selected, used


def check_packing_cover():
    rng = random.Random(872)
    checked = 0
    for universe_size in range(9, 200):
        universe = list(range(universe_size))
        for _ in range(100):
            count = rng.randint(1, min(100, 3 * universe_size))
            supports = []
            seen = set()
            while len(supports) < count:
                support = frozenset(rng.sample(universe, 9))
                if support not in seen:
                    seen.add(support)
                    supports.append(support)
            selected, cover = maximal_disjoint_family(supports)
            assert len(cover) == 9 * len(selected)
            assert all(support & cover for support in supports)
            threshold = len(selected) + 1
            assert len(cover) <= 9 * (threshold - 1)
            loads = Counter()
            for support in supports:
                witness = min(support & cover)
                loads[witness] += 1
            assert max(loads.values()) >= ceil(len(supports) / len(cover))
            checked += 1
    return checked


def support_of_triple(triple):
    support = set()
    for layer, source, target in triple:
        support.add(("cell", source, target))
        support.add(("source", layer, source))
        support.add(("target", layer, target))
    return frozenset(support)


def valid_triple(triple):
    cells = {(source, target) for _, source, target in triple}
    if len(cells) != 3:
        return False
    for layer in (0, 1):
        edges = [(source, target) for ell, source, target in triple if ell == layer]
        if len({source for source, _ in edges}) != len(edges):
            return False
        if len({target for _, target in edges}) != len(edges):
            return False
    return True


def random_triple(side, rng, forbidden_support=frozenset()):
    edges = [
        (layer, source, target)
        for layer in (0, 1)
        for source in range(side)
        for target in range(side)
    ]
    for _ in range(10000):
        triple = frozenset(rng.sample(edges, 3))
        support = support_of_triple(triple)
        if valid_triple(triple) and support.isdisjoint(forbidden_support):
            return triple
    return None


def check_support_compatibility():
    rng = random.Random(875)
    checked = 0
    for side in range(3, 30):
        for _ in range(200):
            triples = []
            used = set()
            while True:
                triple = random_triple(side, rng, frozenset(used))
                if triple is None:
                    break
                triples.append(triple)
                used.update(support_of_triple(triple))
                if len(triples) >= min(side // 3, 8):
                    break
            union = set().union(*triples) if triples else set()
            cells = {(source, target) for _, source, target in union}
            assert len(cells) == len(union)
            for layer in (0, 1):
                edges = [(source, target) for ell, source, target in union if ell == layer]
                assert len({source for source, _ in edges}) == len(edges)
                assert len({target for _, target in edges}) == len(edges)
            chosen_deletions = [min(triple) for triple in triples]
            assert len(chosen_deletions) == len(set(chosen_deletions))
            checked += 1
    return checked


def check_multiplicity_and_thresholds():
    checked = 0
    for episodes in range(1, 10000):
        for threshold in range(2, 20):
            distinct = ceil(episodes / (threshold - 1))
            assert (threshold - 1) * distinct >= episodes
            for packing_threshold in range(2, 10):
                cover_size = 9 * (packing_threshold - 1)
                concentration = ceil(distinct / cover_size)
                assert concentration * cover_size >= distinct
                checked += 1
    return checked


def check_support_size():
    rng = random.Random(870)
    checked = 0
    for side in range(2, 50):
        for _ in range(1000):
            triple = random_triple(side, rng)
            assert triple is not None
            assert len(support_of_triple(triple)) == 9
            checked += 1
    return checked


def main():
    print(
        "verified new-triple support packing:",
        check_support_size(),
        "support cases,",
        check_packing_cover(),
        "packing/cover cases,",
        check_support_compatibility(),
        "compatibility cases, and",
        check_multiplicity_and_thresholds(),
        "threshold cases",
    )


if __name__ == "__main__":
    main()

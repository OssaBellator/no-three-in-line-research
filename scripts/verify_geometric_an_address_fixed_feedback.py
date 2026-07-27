#!/usr/bin/env python3
"""Finite audit for GC2ev--GC2ez."""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import random

SEED = 20260727


def falling(t, rank):
    value = 1
    for offset in range(rank):
        value *= t - offset
    return value


def least_repeat(path):
    first = {}
    for index, state in enumerate(path):
        if state in first:
            return first[state], index
        first[state] = index
    return None


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for system_index in range(45000):
        n = rng.randint(3, 10)
        l_cert = rng.randint(1, 5)
        delta_cap = l_cert * (n * n - 2)
        k_tri = comb(n * n, 2)
        k_an = rng.randint(1, 12)

        lineage_count = rng.randint(1, 80)
        fibres = [0] * k_an
        address_incidences = 0
        for _lineage in range(lineage_count):
            weight = rng.randint(1, 50)
            addresses = [address for address in range(k_an) if rng.random() < 0.25]
            if not addresses:
                addresses = [rng.randrange(k_an)]
            chosen = min(addresses)
            fibres[chosen] += weight
            address_incidences += len(addresses)

        star_weight = sum(fibres)
        source_weight = max(fibres)
        assert source_weight * k_an >= star_weight

        epsilon = Fraction(rng.randint(1, 4), 5)
        threshold = (1 - epsilon) * source_weight
        k_fix = rng.randint(1, 20)
        t = rng.randint(7, 12)
        rank_stocks = [falling(t, rank) for rank in (1, 2, 3)]

        # Force all three branches to receive substantial coverage.
        branch = system_index % 3
        if branch == 0:
            fixed_atoms = [0] * k_fix
            inventories = [0, 0, 0]
            fixed_total = 0
            expected_an = Fraction(0, 1)
            assert fixed_total + expected_an <= threshold
            decrease = source_weight - fixed_total - expected_an
            assert decrease >= epsilon * source_weight
            counts["descent_branches"] += 1

        elif branch == 1:
            target = threshold / 2 + 1
            fixed_total = int(target) + 1
            fixed_atoms = [0] * k_fix
            for unit in range(fixed_total):
                fixed_atoms[unit % k_fix] += 1
            inventories = [0, 0, 0]
            expected_an = Fraction(0, 1)
            assert Fraction(fixed_total, 1) > threshold / 2
            heaviest = max(fixed_atoms)
            assert heaviest * k_fix >= fixed_total
            assert Fraction(heaviest, 1) > threshold / (2 * k_fix)
            counts["fixed_atom_branches"] += 1

        else:
            fixed_atoms = [0] * k_fix
            fixed_total = 0
            target = threshold / 2
            inventories = [0, 0, 0]
            chosen_rank = rng.randrange(3)
            stock = rank_stocks[chosen_rank]
            needed = target * stock / 128
            inventories[chosen_rank] = int(needed) + 1
            expected_an = sum(
                Fraction(128 * inventories[index], rank_stocks[index])
                for index in range(3)
            )
            assert expected_an > threshold / 2
            contributions = [
                Fraction(128 * inventories[index], rank_stocks[index])
                for index in range(3)
            ]
            rank = max(range(3), key=lambda index: contributions[index])
            assert contributions[rank] > threshold / 6
            prescription_weight = Fraction(inventories[rank], rank_stocks[rank])
            assert prescription_weight > threshold / 768
            exact_weight = prescription_weight / k_tri
            assert exact_weight > threshold / (768 * k_tri)
            counts["matching_certificate_branches"] += 1

        if fixed_total:
            assert sum(fixed_atoms) == fixed_total
            assert max(fixed_atoms) * k_fix >= fixed_total

        # Check the integrated strict constants algebraically.
        birth_weight = rng.randint(1, 1000)
        anchor_lower = Fraction(
            3 * birth_weight,
            2 * n * n * (2 * delta_cap - 1),
        )
        actual_anchor = anchor_lower + Fraction(1, 10**6)
        extracted_source = actual_anchor / k_an

        descent_bound = Fraction(
            3 * epsilon * birth_weight,
            2 * k_an * n * n * (2 * delta_cap - 1),
        )
        assert epsilon * extracted_source > descent_bound

        fixed_bound = Fraction(
            3 * (1 - epsilon) * birth_weight,
            4 * k_an * k_fix * n * n * (2 * delta_cap - 1),
        )
        assert (1 - epsilon) * extracted_source / (2 * k_fix) > fixed_bound

        certificate_bound = Fraction(
            (1 - epsilon) * birth_weight,
            512 * k_an * n * n * (2 * delta_cap - 1) * k_tri,
        )
        assert (1 - epsilon) * extracted_source / (768 * k_tri) > certificate_bound

        counts["systems"] += 1
        counts["lineages"] += lineage_count
        counts["address_incidences"] += address_incidences
        counts["fixed_atoms"] += k_fix

    # Independent finite-signature quotient audit.
    for _ in range(6000):
        signature_count = rng.randint(1, 4)
        capacities = [rng.randint(0, 3) for _ in range(signature_count)]
        contexts = rng.randint(1, 3)
        multiplicities = list(product(*[range(capacity + 1) for capacity in capacities]))
        states = [
            (context, vector)
            for context in range(contexts)
            for vector in multiplicities
        ]
        state_count = len(states)
        event_count = rng.randint(1, 4)
        transition = [
            [rng.randrange(state_count) for _ in range(event_count)]
            for _state in states
        ]

        current = rng.randrange(state_count)
        path = [current]
        for _step in range(state_count):
            event = rng.randrange(event_count)
            current = transition[current][event]
            path.append(current)

        begin, end = least_repeat(path)
        assert end <= state_count
        assert 1 <= end - begin <= state_count

        counts["feedback_systems"] += 1
        counts["feedback_states"] += state_count
        counts["feedback_cycle_steps"] += end - begin

    print("GC AN-address and fixed-feedback audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()

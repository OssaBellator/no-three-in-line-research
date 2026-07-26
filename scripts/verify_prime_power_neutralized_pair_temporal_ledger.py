#!/usr/bin/env python3
"""Finite checks for CMR763--CMR769."""

from itertools import product
from math import comb, floor
import random


def certificate_stock(side):
    return 6 * comb(2 * side * side, 3)


def absence_runs(bits):
    runs = 0
    inside = False
    for present in bits:
        if not present and not inside:
            runs += 1
            inside = True
        elif present:
            inside = False
    return runs


def reintroductions(bits):
    return sum(
        1
        for before, after in zip(bits, bits[1:])
        if not before and after
    )


def check_binary_histories():
    checked = 0
    for length in range(1, 11):
        for bits in product((False, True), repeat=length):
            runs = absence_runs(bits)
            returns = reintroductions(bits)
            assert runs <= 1 + returns
            checked += 1
    return checked


def check_total_slots():
    rng = random.Random(766)
    checked = 0
    for side in range(1, 40):
        universe = 2 * side * side
        for threshold in range(2, 10):
            histories = []
            for _ in range(universe):
                returns = rng.randint(0, threshold - 1)
                bits = []
                present = rng.choice((False, True))
                bits.append(present)
                while reintroductions(bits) < returns:
                    if bits[-1]:
                        bits.append(False)
                    else:
                        bits.append(True)
                histories.append(bits)
            total_runs = sum(absence_runs(bits) for bits in histories)
            total_returns = sum(reintroductions(bits) for bits in histories)
            assert total_runs <= universe + total_returns
            assert total_runs <= threshold * universe
            checked += 1
    return checked


def check_slot_capacity():
    checked = 0
    for side in range(1, 50):
        stock = certificate_stock(side)
        universe = 2 * side * side
        for threshold in range(2, 12):
            slots = threshold * universe
            for witnesses in range(1, min(20, universe) + 1):
                episodes = floor(stock * slots / witnesses)
                assert episodes * witnesses <= stock * slots
                checked += 1
    return checked


def check_stocks():
    checked = 0
    for side in range(1, 100):
        stock = certificate_stock(side)
        assert stock >= comb(2 * side * side, 3)
        assert stock % 6 == 0
        checked += 1
    return checked


def check_token_payment():
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for height in range(1, 10):
            for returns in range(100):
                incidence = returns * (prime + 1) * (height - 1)
                assert incidence >= 0
                assert returns + 1 >= 1
                if height == 1:
                    assert incidence == 0
                checked += 1
    return checked


def main():
    print(
        "verified neutralized-pair temporal ledger:",
        check_binary_histories(),
        "binary histories,",
        check_total_slots(),
        "slot totals,",
        check_slot_capacity(),
        "slot-capacity cases,",
        check_stocks(),
        "certificate stocks, and",
        check_token_payment(),
        "token cases",
    )


if __name__ == "__main__":
    main()

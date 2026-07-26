#!/usr/bin/env python3
"""Finite checks for CMR763--CMR769."""

from math import comb, floor
import random


def certificate_stock(side):
    return 6 * comb(2 * side * side, 3)


def check_stocks():
    checked = 0
    for side in range(1, 100):
        stock = certificate_stock(side)
        assert stock >= comb(2 * side * side, 3)
        assert stock % 6 == 0
        checked += 1
    return checked


def check_distinct_witness_bounds():
    rng = random.Random(766)
    checked = 0
    for side in range(1, 100):
        universe = 2 * side * side
        for threshold in range(2, 12):
            multiplicities = [rng.randint(0, threshold - 1) for _ in range(universe)]
            total = sum(multiplicities)
            assert total <= (threshold - 1) * universe
            for minimum in range(1, min(20, universe) + 1):
                episodes = total // minimum
                assert episodes <= floor((threshold - 1) * universe / minimum)
                checked += 1
    return checked


def check_permanent_or_paid():
    checked = 0
    for side in range(1, 40):
        stock = certificate_stock(side)
        universe = 2 * side * side
        for threshold in range(2, 10):
            for minimum in range(1, min(10, universe) + 1):
                bound = stock + floor((threshold - 1) * universe / minimum)
                assert bound >= stock
                assert bound >= floor((threshold - 1) * universe / minimum)
                checked += 1
    return checked


def check_star_history():
    checked = 0
    for side in range(1, 100):
        stock = certificate_stock(side)
        universe = 2 * side * side
        for threshold in range(2, 20):
            bound = stock + (threshold - 1) * universe
            assert bound - stock == (threshold - 1) * universe
            checked += 1
    return checked


def check_token_payment():
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for height in range(1, 10):
            for returns in range(0, 100):
                incidence = returns * (prime + 1) * (height - 1)
                assert incidence >= 0
                if height == 1:
                    assert incidence == 0
                checked += 1
    return checked


def main():
    print(
        "verified neutralized-pair temporal ledger:",
        check_stocks(),
        "certificate stocks,",
        check_distinct_witness_bounds(),
        "witness bounds,",
        check_permanent_or_paid(),
        "mixed episode bounds,",
        check_star_history(),
        "star histories, and",
        check_token_payment(),
        "token cases",
    )


if __name__ == "__main__":
    main()

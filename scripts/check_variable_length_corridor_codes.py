#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement


RHO = [Fraction(1, 5), Fraction(1, 4), Fraction(3, 10), Fraction(1, 3), Fraction(2, 5), Fraction(1, 2), Fraction(3, 5)]
B = 2
P = Fraction(3, 4)
MAX_LEN = 9


def kraft(lengths):
    return sum(Fraction(1, B ** ell) for ell in lengths)


def risk(lengths):
    return max(rho / (P ** ell) for rho, ell in zip(RHO, lengths))


def L_of(R, rho):
    ell = 0
    while rho / (P ** (ell + 1)) <= R:
        ell += 1
        if ell > MAX_LEN + 5:
            break
    return ell


def main():
    best = None
    best_lengths = None
    feasible_count = 0
    for increasing in combinations_with_replacement(range(1, MAX_LEN + 1), len(RHO)):
        lengths = tuple(reversed(increasing))
        if kraft(lengths) > 1:
            continue
        feasible_count += 1
        r = risk(lengths)
        if best is None or r < best:
            best, best_lengths = r, lengths

    assert best is not None

    breakpoints = sorted({rho / (P ** ell) for rho in RHO for ell in range(1, MAX_LEN + 1)})
    theorem_best = None
    theorem_lengths = None
    for R in breakpoints:
        L = [L_of(R, rho) for rho in RHO]
        feasible = min(L) >= 1 and sum(Fraction(1, B ** ell) for ell in L) <= 1
        if feasible:
            theorem_best = R
            theorem_lengths = tuple(L)
            break

    assert theorem_best == best
    assert kraft(theorem_lengths) <= 1
    assert risk(theorem_lengths) <= theorem_best

    print({
        "all_checks_passed": True,
        "feasible_length_vectors": feasible_count,
        "optimal_risk": str(best),
        "one_optimal_length_vector": best_lengths,
        "kraft_test_lengths": theorem_lengths,
    })


if __name__ == "__main__":
    main()

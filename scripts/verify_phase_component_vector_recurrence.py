#!/usr/bin/env python3
"""Finite checks for OP4ap--OP4ar."""

from itertools import product
from math import gcd, lcm


def order_scalar(h, x):
    return h // gcd(h, x)


def main():
    checks = 0
    for h in range(1, 13):
        for kappa in range(1, 5):
            for omega in product(range(h), repeat=kappa):
                component_lcm = 1
                g = h
                for x in omega:
                    component_lcm = lcm(component_lcm, order_scalar(h, x))
                    g = gcd(g, x)
                formula = h // g
                assert component_lcm == formula

                phases = [tuple((j * x) % h for x in omega) for j in range(formula)]
                assert len(set(phases)) == formula
                assert all((formula * x) % h == 0 for x in omega)
                if formula > 1:
                    assert all(any((j * x) % h for x in omega) for j in range(1, formula))
                assert len(phases) - 1 == formula - 1
                checks += 1

    print(f"verified {checks} normalized component vectors")


if __name__ == "__main__":
    main()

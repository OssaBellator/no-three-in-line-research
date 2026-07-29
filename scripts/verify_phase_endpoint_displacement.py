#!/usr/bin/env python3
"""Verify exact endpoint-displacement orbit sizes and ticket counts."""

from math import gcd


def main():
    checked = 0
    for h in range(1, 13):
        for omega in range(h):
            order = 1 if omega == 0 else h // gcd(h, omega)
            phases = [(j * omega) % h for j in range(order)]
            assert len(set(phases)) == order
            assert phases[0] == 0
            assert (order * omega) % h == 0
            if omega != 0:
                assert all((j * omega) % h != 0 for j in range(1, order))
            assert len(phases[1:]) == order - 1
            checked += 1
    print(f"verified {checked} endpoint-displacement orbits")


if __name__ == "__main__":
    main()

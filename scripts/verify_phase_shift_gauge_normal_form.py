#!/usr/bin/env python3
"""Finite checks for OP4ai--OP4al."""

from __future__ import annotations

from collections import defaultdict
from itertools import product


def transform_path(shifts: tuple[int, ...], h: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    r = len(shifts)
    if r == 1:
        return shifts, ()
    phi = [0] * (r + 1)
    for i in range(1, r):
        phi[i] = (phi[i - 1] + shifts[i - 1]) % h
    phi[r] = 0
    out = tuple((shifts[i] + phi[i] - phi[i + 1]) % h for i in range(r))
    return out, tuple(phi[1:r])


def transform_cycle(shifts: tuple[int, ...], h: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    r = len(shifts)
    phi = [0] * r
    for i in range(1, r):
        phi[i] = (phi[i - 1] + shifts[i - 1]) % h
    out = tuple(
        (shifts[i] + phi[i] - phi[(i + 1) % r]) % h
        for i in range(r)
    )
    return out, tuple(phi[1:])


def main() -> None:
    path_words = 0
    cycle_words = 0
    orbit_checks = 0
    for h in range(2, 8):
        for r in range(1, 6):
            path_classes: dict[int, list[tuple[int, ...]]] = defaultdict(list)
            cycle_classes: dict[int, list[tuple[int, ...]]] = defaultdict(list)
            for shifts in product(range(h), repeat=r):
                omega = sum(shifts) % h

                normal_path, phi_path = transform_path(shifts, h)
                assert normal_path[:-1] == (0,) * (r - 1)
                assert normal_path[-1] == omega
                if r > 1:
                    reconstructed = [0]
                    for i in range(r - 1):
                        reconstructed.append((reconstructed[-1] + shifts[i]) % h)
                    assert tuple(reconstructed[1:]) == phi_path
                path_classes[omega].append(shifts)
                path_words += 1

                normal_cycle, phi_cycle = transform_cycle(shifts, h)
                assert normal_cycle[:-1] == (0,) * (r - 1)
                assert normal_cycle[-1] == omega
                reconstructed_cycle = [0]
                for i in range(r - 1):
                    reconstructed_cycle.append((reconstructed_cycle[-1] + shifts[i]) % h)
                assert tuple(reconstructed_cycle[1:]) == phi_cycle
                if omega == 0:
                    assert normal_cycle == (0,) * r
                cycle_classes[omega].append(shifts)
                cycle_words += 1

            for classes in (path_classes, cycle_classes):
                assert set(classes) == set(range(h))
                for omega, words in classes.items():
                    assert len(words) == h ** (r - 1)
                    normal_forms = {
                        transform_path(word, h)[0]
                        if classes is path_classes
                        else transform_cycle(word, h)[0]
                        for word in words
                    }
                    assert len(normal_forms) == 1
                    assert next(iter(normal_forms))[-1] == omega
                    orbit_checks += 1

    print(
        f"verified {path_words} path words, {cycle_words} cycle words "
        f"and {orbit_checks} gauge orbits"
    )


if __name__ == "__main__":
    main()

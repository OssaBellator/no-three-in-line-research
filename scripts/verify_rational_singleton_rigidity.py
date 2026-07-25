#!/usr/bin/env python3
"""Exhaust RI5k binary current/target mixtures on single cycles."""


def verify(maximum_length=10):
    checked = 0
    for length in range(2, maximum_length + 1):
        current = tuple(range(length))
        target = tuple((column + 1) % length for column in range(length))

        for mask in range(1 << length):
            mixed = tuple(
                target[column] if mask & (1 << column) else current[column]
                for column in range(length)
            )
            is_matching = len(set(mixed)) == length
            is_extreme = mask == 0 or mask == (1 << length) - 1
            assert is_matching == is_extreme
            checked += 1
    return checked


def main():
    checked = verify()
    print(f"Rational singleton rigidity: verified {checked} mixtures")


if __name__ == "__main__":
    main()

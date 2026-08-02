#!/usr/bin/env python3
"""Finite arithmetic checks for corrected PX324--PX329."""

from itertools import product


def main() -> None:
    for destroyed in range(1, 41):
        for external in range(41):
            for internal in range(21):
                total = external + internal
                if destroyed > total:
                    assert total - destroyed < 0
                if destroyed > internal and destroyed <= total:
                    budget = total - destroyed + 1
                    assert 1 <= budget <= external
                    assert total - budget - destroyed == -1
                if destroyed <= internal:
                    assert total - external - destroyed == internal - destroyed >= 0

    supports = set()
    for mask in product((0, 1), repeat=3):
        support = sum(mask)
        if support:
            supports.add(support)
            assert 1 <= support <= 3
    assert supports == {1, 2, 3}

    for blocker_count in range(1, 30):
        vector = (blocker_count, 0)
        for deeper in range(blocker_count):
            new_vector = (vector[0] - 1, deeper + 1)
            assert new_vector < vector
            vector = new_vector

    print("PX324--PX329 corrected external blocker-forest verifier: PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Arithmetic checks for CMR234--CMR236."""

from math import comb


def near_line_bound(r: int) -> int:
    return 2 * comb(r + 2, 2) * comb(3 * r + 2, 2)


def required_half_size(r: int) -> int:
    return near_line_bound(r) * (r + 1) - r * r + 2


def fifth_root_floor(value: int) -> int:
    answer = 0
    while (answer + 1) ** 5 <= value:
        answer += 1
    return answer


def verify_fixed_surplus() -> None:
    assert near_line_bound(0) == 2
    assert required_half_size(0) == 4
    for r in range(1, 1001):
        count = near_line_bound(r)
        threshold = required_half_size(r)
        assert count <= 60 * r**4
        assert threshold <= 120 * r**5 + 2

        lower = (threshold + r - count) * (r + 1)
        upper = (threshold + 1) * r + 1
        assert lower > upper


def verify_growing_surplus() -> None:
    samples = list(range(240, 5000))
    samples.extend([10_000, 100_000, 1_000_000, 10_000_000])
    for h in samples:
        r = fifth_root_floor(h // 240)
        assert 240 * r**5 <= h
        assert required_half_size(r) <= h


def main() -> None:
    verify_fixed_surplus()
    verify_growing_surplus()
    print(
        "verified near-transversal resilience: O(r^5) thresholds and "
        "the floor((h/240)^(1/5)) surplus"
    )


if __name__ == "__main__":
    main()

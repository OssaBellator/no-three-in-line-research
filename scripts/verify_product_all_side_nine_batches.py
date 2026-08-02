#!/usr/bin/env python3
"""Verify batch repair for both distinct successful 3 x 3 crossed hosts."""
from __future__ import annotations

from collections import Counter

from verify_product_batch_repair import census


def main() -> None:
    family_a = ((0, 2, 1), (1, 0, 2))
    family_b = ((1, 2, 0), (2, 0, 1))

    for outer, inner in ((family_a, family_b), (family_b, family_a)):
        census(
            outer=outer,
            inner=inner,
            orientation="cf",
            expected_states=6840,
            expected_edges=1359432,
            expected_solutions=2,
            expected_one_step=6814,
            expected_profiles=Counter({(3, 3, 0): 20, (3, 4, 0): 4}),
        )

    print(
        "both distinct successful 3x3 cf hosts have repair radius two "
        "and maximum uphill barrier one"
    )


if __name__ == "__main__":
    main()

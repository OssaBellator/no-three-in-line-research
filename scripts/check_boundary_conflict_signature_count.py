#!/usr/bin/env python3
"""Exhaustively verify the PP3bwf conflict-signature counts."""

from __future__ import annotations

from itertools import combinations, permutations, product


def parity(word: tuple[int, ...]) -> int:
    value = 0
    for bit in word:
        value ^= bit
    return value


def signatures(owner_count: int) -> set[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]]:
    owners = tuple(range(owner_count))
    result: set[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]] = set()
    for length in range(1, owner_count + 1):
        for owner_word in permutations(owners, length):
            for boundary_gap_count in range(length):
                for gap_positions in combinations(range(length - 1), boundary_gap_count):
                    boundary_gaps = set(gap_positions)
                    bridge_word = tuple(
                        1 if gap in boundary_gaps else 0 for gap in range(length - 1)
                    )
                    edge_count = length + 1 + boundary_gap_count
                    for label_word in product((0, 1), repeat=edge_count):
                        if parity(label_word) == 1:
                            result.add((owner_word, bridge_word, label_word))
    return result


def formula(owner_count: int) -> int:
    total = 0
    falling = 1
    for length in range(1, owner_count + 1):
        falling *= owner_count - length + 1
        total += falling * (2**length) * (3 ** (length - 1))
    return total


def main() -> None:
    expected = {1: 2, 2: 28, 3: 510}
    rows = []
    for owner_count, target in expected.items():
        enumerated = len(signatures(owner_count))
        closed_form = formula(owner_count)
        if enumerated != target or closed_form != target:
            raise SystemExit(
                f"check failed for r={owner_count}: "
                f"enumerated={enumerated}, formula={closed_form}, expected={target}"
            )
        rows.append(
            {
                "owner_count": owner_count,
                "enumerated_signatures": enumerated,
                "closed_form_signatures": closed_form,
            }
        )

    import json

    print(json.dumps({"rows": rows, "all_checks_passed": True}, indent=2))


if __name__ == "__main__":
    main()

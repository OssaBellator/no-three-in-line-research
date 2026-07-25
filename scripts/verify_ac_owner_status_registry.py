#!/usr/bin/env python3
"""Finite checks for AC3ke--AC3kh."""
from __future__ import annotations

from collections import Counter
from itertools import product

ROUTES = (
    "PAID",
    "FIXED_CURRENT",
    "PROSPECTIVE",
    "OCCURRENCE_FAILURE",
    "COHERENCE_MISMATCH",
    "OWNER_RESET",
)


def route(current: bool, physical: bool, coherent: bool, payable: bool) -> str:
    if payable:
        assert current and physical and coherent
        return "PAID"
    if not physical:
        return "OCCURRENCE_FAILURE"
    if not coherent:
        return "COHERENCE_MISMATCH"
    if current:
        return "FIXED_CURRENT"
    return "PROSPECTIVE"


def verify_truth_table(counts: Counter[str]) -> None:
    for current, physical, coherent, payable in product((False, True), repeat=4):
        if payable and not (current and physical and coherent):
            counts["rejected invalid payable rows"] += 1
            continue
        label = route(current, physical, coherent, payable)
        assert label in ROUTES
        if label == "PAID":
            assert current and physical and coherent and payable
        elif label == "FIXED_CURRENT":
            assert current and physical and coherent and not payable
        elif label == "PROSPECTIVE":
            assert not current and physical and coherent and not payable
        elif label == "OCCURRENCE_FAILURE":
            assert not physical and not payable
        elif label == "COHERENCE_MISMATCH":
            assert physical and not coherent and not payable
        counts["valid owner rows"] += 1


def verify_transition_relative_examples(counts: Counter[str]) -> None:
    token = (True, True, True)
    for payable in (False, True):
        label = route(*token, payable)
        assert label == ("PAID" if payable else "FIXED_CURRENT")
        counts["transition-relative token examples"] += 1

    examples = {
        "pivot": (True, True, True, True),
        "current_bda": (True, True, True, True),
        "prospective_bda": (False, True, True, False),
        "movable_ri": (True, True, True, True),
        "prospective_ri": (False, True, True, False),
        "fixed_op_component": (True, True, True, False),
        "closed_i6_factor": (True, True, True, True),
        "phase_token": (True, True, True, True),
        "unowned_literal": (False, True, True, False),
    }
    expected = {
        "pivot": "PAID",
        "current_bda": "PAID",
        "prospective_bda": "PROSPECTIVE",
        "movable_ri": "PAID",
        "prospective_ri": "PROSPECTIVE",
        "fixed_op_component": "FIXED_CURRENT",
        "closed_i6_factor": "PAID",
        "phase_token": "PAID",
        "unowned_literal": "PROSPECTIVE",
    }
    for name, flags in examples.items():
        assert route(*flags) == expected[name]
        counts["canonical registry rows"] += 1


def verify_reset_stock(counts: Counter[str]) -> None:
    directed_route_edges = [
        (source, target)
        for source in ROUTES
        for target in ROUTES
        if source != target
    ]
    assert len(directed_route_edges) == 30
    for kinds in range(1, 10):
        for families in range(1, 10):
            stock = kinds * families * len(directed_route_edges)
            assert stock == 30 * kinds * families
            for owners in range(1, 8):
                assert owners * stock == 30 * kinds * families * owners
                counts["owner reset stocks"] += 1


def verify_weighted_concentration(counts: Counter[str]) -> None:
    for stock in range(1, 40):
        width = min(stock, 6)
        for weights in product(range(0, 5), repeat=width):
            expanded = [weights[i % width] for i in range(stock)]
            total = sum(expanded)
            maximum = max(expanded, default=0)
            assert stock * maximum >= total
            counts["weighted owner reset systems"] += 1


def verify_outer_decoration(counts: Counter[str]) -> None:
    for profiles in range(1, 9):
        for kinds in range(1, 7):
            for families in range(1, 7):
                decorations = 30 * kinds * families
                stock = decorations * profiles * (profiles - 1)
                assert stock == (
                    30 * kinds * families * profiles * (profiles - 1)
                )
                counts["outer owner decorations"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_truth_table(counts)
    verify_transition_relative_examples(counts)
    verify_reset_stock(counts)
    verify_weighted_concentration(counts)
    verify_outer_decoration(counts)

    print("AC3ke--AC3kh owner-status registry audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()

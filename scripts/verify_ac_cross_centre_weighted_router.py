#!/usr/bin/env python3
"""Verify AC3al--AC3am weighted cross-centre dispersion."""

from __future__ import annotations

from itertools import combinations, product


Scope = tuple[int, ...]


def maximum_weight_disjoint(
    scopes: tuple[Scope, ...],
    weights: tuple[int, ...],
    indices: tuple[int, ...] | None = None,
) -> int:
    if indices is None:
        indices = tuple(range(len(scopes)))
    best = 0
    for mask in range(1 << len(indices)):
        used: set[int] = set()
        total = 0
        valid = True
        for offset, index in enumerate(indices):
            if not (mask & (1 << offset)):
                continue
            scope = set(scopes[index])
            if used & scope:
                valid = False
                break
            used.update(scope)
            total += weights[index]
        if valid:
            best = max(best, total)
    return best


def verify_weighted_residual_dispersion() -> int:
    checked = 0
    blocks = range(3)
    scope_options = tuple(
        scope
        for rank in (1, 2)
        for scope in combinations(blocks, rank)
    )
    for size in range(1, 6):
        for scopes in product(scope_options, repeat=size):
            degrees = {
                block: sum(block in scope for scope in scopes)
                for block in blocks
            }
            for weights in product((1, 2), repeat=size):
                total = sum(weights)
                for threshold in range(1, size + 1):
                    if max(degrees.values(), default=0) > threshold:
                        continue
                    selected = maximum_weight_disjoint(scopes, weights)
                    assert selected * (2 * threshold - 1) >= total
                checked += 1
    return checked


def verify_common_residual_router() -> int:
    checked = 0
    label_count = 2
    secondary_blocks = range(2)
    records = tuple(
        (label, secondary)
        for label in range(label_count)
        for secondary in (None, *secondary_blocks)
    )
    for size in range(1, 6):
        for family in product(records, repeat=size):
            secondaries = tuple(record[1] for record in family)
            for weights in product((1, 2), repeat=size):
                total = sum(weights)
                classes: dict[tuple[int, int], list[int]] = {}
                for index, (label, secondary) in enumerate(family):
                    rank = 1 if secondary is None else 2
                    classes.setdefault((label, rank), []).append(index)

                chosen_key = max(
                    classes,
                    key=lambda key: sum(weights[i] for i in classes[key]),
                )
                chosen = tuple(classes[chosen_key])
                chosen_weight = sum(weights[i] for i in chosen)
                assert chosen_weight * (2 * label_count) >= total

                if chosen_key[1] == 1:
                    assert all(secondaries[i] is None for i in chosen)
                    checked += 1
                    continue

                assert all(secondaries[i] is not None for i in chosen)
                for threshold in range(1, size + 1):
                    multiplicities = {
                        block: sum(
                            secondaries[i] == block for i in chosen
                        )
                        for block in secondary_blocks
                    }
                    if max(multiplicities.values(), default=0) > threshold:
                        continue

                    selected_weight = sum(
                        max(
                            (
                                weights[i]
                                for i in chosen
                                if secondaries[i] == block
                            ),
                            default=0,
                        )
                        for block in secondary_blocks
                    )
                    assert selected_weight * threshold >= chosen_weight
                    assert (
                        selected_weight
                        * (2 * label_count)
                        * threshold
                        >= total
                    )
                checked += 1
    return checked


def main() -> None:
    residual = verify_weighted_residual_dispersion()
    common = verify_common_residual_router()
    print(
        "AC weighted cross-centre routing verified:",
        f"{residual} residual-scope systems,",
        f"{common} common-literal labelled systems",
    )


if __name__ == "__main__":
    main()

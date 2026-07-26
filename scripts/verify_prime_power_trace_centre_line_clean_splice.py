#!/usr/bin/env python3
"""Finite checks for CMR1566--CMR1573."""

from __future__ import annotations

from collections import Counter
from itertools import permutations
from random import Random


Edge = tuple[int, int]


def line_cells(side: int, target: Edge, witness: Edge) -> set[Edge]:
    source_0, target_0 = target
    source_1, target_1 = witness
    delta_source = source_1 - source_0
    delta_target = target_1 - target_0
    if delta_source == 0 or delta_target == 0:
        raise ValueError("trace line must be nonaxis")
    return {
        (source, image)
        for source in range(side)
        for image in range(side)
        if (source - source_0) * delta_target
        == (image - target_0) * delta_source
    }


def is_partial_matching(edges: set[Edge]) -> bool:
    return (
        len({source for source, _image in edges}) == len(edges)
        and len({image for _source, image in edges}) == len(edges)
    )


def has_derangement_extension(side: int, prescribed: set[Edge]) -> bool:
    if not is_partial_matching(prescribed):
        return False
    for state in permutations(range(side)):
        if any(state[index] == index for index in range(side)):
            continue
        if all(state[source] == image for source, image in prescribed):
            return True
    return False


def verify_centre_batching() -> tuple[int, int]:
    rng = Random(1567)
    systems = 0
    occurrences = 0
    for side in range(2, 25):
        centres = [
            (source, image)
            for source in range(side)
            for image in range(side)
        ]
        for threshold in range(2, 12):
            for _ in range(100):
                count = rng.randint(0, (threshold + 2) * side * side)
                history = [rng.choice(centres) for _ in range(count)]
                multiplicities = Counter(history)
                maximum = max(multiplicities.values(), default=0)
                if count:
                    assert maximum >= (
                        count + side * side - 1
                    ) // (side * side)
                else:
                    assert maximum == 0
                if maximum < threshold:
                    assert count <= (threshold - 1) * side * side
                systems += 1
                occurrences += count
    return systems, occurrences


def verify_rooted_line_classes() -> tuple[int, int, int]:
    total = 0
    strong = 0
    singleton = 0

    for side in range(4, 8):
        opposite = {(index, index) for index in range(side)}
        seen: set[tuple[Edge, frozenset[Edge]]] = set()

        for target in [
            (source, image)
            for source in range(side)
            for image in range(side)
            if source != image
        ]:
            target_source, target_image = target
            for witness in [
                (source, image)
                for source in range(side)
                for image in range(side)
                if source != target_source and image != target_image
            ]:
                line = frozenset(line_cells(side, target, witness))
                key = (target, line)
                if key in seen:
                    continue
                seen.add(key)

                deleted_trace = set(line) - opposite - {target}
                assert is_partial_matching(deleted_trace)
                assert all(
                    source != target_source and image != target_image
                    for source, image in deleted_trace
                )

                target_trace = deleted_trace | {target}
                assert is_partial_matching(target_trace)

                extendable = has_derangement_extension(side, target_trace)
                unmatched_sources = set(range(side)) - {
                    source for source, _image in target_trace
                }
                unmatched_targets = set(range(side)) - {
                    image for _source, image in target_trace
                }
                is_singleton = (
                    len(unmatched_sources) == 1
                    and unmatched_sources == unmatched_targets
                )

                assert extendable != is_singleton
                total += 1
                strong += int(extendable)
                singleton += int(is_singleton)

    return total, strong, singleton


def main() -> None:
    systems, occurrences = verify_centre_batching()
    total, strong, singleton = verify_rooted_line_classes()
    print(
        "verified trace-centre batching and rooted line cleaning: "
        f"{systems} batching systems with {occurrences} occurrences, "
        f"and {total} rooted line classes "
        f"({strong} strong, {singleton} singleton)"
    )


if __name__ == "__main__":
    main()

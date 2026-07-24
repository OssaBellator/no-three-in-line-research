#!/usr/bin/env python3
"""Verify AC3y--AC3z one-block sensitivity and behavioral quotients."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product
from math import prod


Phase = tuple[int, ...]
Behavior = tuple[int, ...]


def all_phases(sizes: tuple[int, ...]) -> tuple[Phase, ...]:
    return tuple(product(*(range(size) for size in sizes)))


def mismatch(phase: Phase, forbidden: Phase) -> tuple[int, ...]:
    return tuple(
        int(value != forbidden[index])
        for index, value in enumerate(phase)
    )


def discharge(
    sizes: tuple[int, ...],
    forbidden: Phase,
) -> tuple[Phase, ...]:
    return tuple(
        phase
        for phase in all_phases(sizes)
        if phase != forbidden
    )


def hamming_distance(left: Phase, right: Phase) -> int:
    return sum(
        left[index] != right[index]
        for index in range(len(left))
    )


def literal_invariant(
    phases: tuple[Phase, ...],
    forbidden: Phase,
    behavior: dict[Phase, Behavior],
) -> bool:
    return all(
        behavior[left] == behavior[right]
        for left, right in combinations(phases, 2)
        if mismatch(left, forbidden) == mismatch(right, forbidden)
    )


def edge_invariant(
    phases: tuple[Phase, ...],
    forbidden: Phase,
    behavior: dict[Phase, Behavior],
) -> bool:
    return all(
        behavior[left] == behavior[right]
        for left, right in combinations(phases, 2)
        if mismatch(left, forbidden) == mismatch(right, forbidden)
        and hamming_distance(left, right) == 1
    )


def canonical_path(left: Phase, right: Phase) -> tuple[Phase, ...]:
    current = list(left)
    path = [left]
    for index in range(len(left)):
        if current[index] == right[index]:
            continue
        current[index] = right[index]
        path.append(tuple(current))
    return tuple(path)


def sensitive_edge(
    left: Phase,
    right: Phase,
    behavior: dict[Phase, Behavior],
    component: int,
    forbidden: Phase,
) -> tuple[int, Phase, Phase]:
    assert mismatch(left, forbidden) == mismatch(right, forbidden)
    assert behavior[left][component] != behavior[right][component]
    path = canonical_path(left, right)
    for before, after in zip(path, path[1:]):
        assert mismatch(before, forbidden) == mismatch(
            after,
            forbidden,
        )
        if behavior[before][component] != behavior[after][component]:
            differing = tuple(
                index
                for index in range(len(before))
                if before[index] != after[index]
            )
            assert len(differing) == 1
            return differing[0], before, after
    raise AssertionError("a changing component must change on the path")


def contexts(
    sizes: tuple[int, ...],
    coordinate: int,
) -> tuple[tuple[int, ...], ...]:
    other_sizes = (
        sizes[:coordinate]
        + sizes[coordinate + 1 :]
    )
    return tuple(product(*(range(size) for size in other_sizes)))


def insert_coordinate(
    context: tuple[int, ...],
    coordinate: int,
    value: int,
) -> Phase:
    return (
        context[:coordinate]
        + (value,)
        + context[coordinate:]
    )


def coordinate_partition(
    sizes: tuple[int, ...],
    forbidden: Phase,
    behavior: dict[Phase, Behavior],
    coordinate: int,
) -> tuple[dict[int, int], tuple[tuple[int, ...], ...]]:
    phase_class = {forbidden[coordinate]: 0}
    signature_class: dict[tuple[Behavior, ...], int] = {}
    classes: list[list[int]] = [[forbidden[coordinate]]]

    for value in range(sizes[coordinate]):
        if value == forbidden[coordinate]:
            continue
        signature = tuple(
            behavior[
                insert_coordinate(context, coordinate, value)
            ]
            for context in contexts(sizes, coordinate)
        )
        if signature not in signature_class:
            signature_class[signature] = len(classes)
            classes.append([])
        class_id = signature_class[signature]
        phase_class[value] = class_id
        classes[class_id].append(value)

    return phase_class, tuple(tuple(group) for group in classes)


def quotient_data(
    sizes: tuple[int, ...],
    forbidden: Phase,
    behavior: dict[Phase, Behavior],
) -> tuple[
    tuple[dict[int, int], ...],
    tuple[tuple[tuple[int, ...], ...], ...],
]:
    partitions = tuple(
        coordinate_partition(
            sizes,
            forbidden,
            behavior,
            coordinate,
        )
        for coordinate in range(len(sizes))
    )
    return (
        tuple(partition[0] for partition in partitions),
        tuple(partition[1] for partition in partitions),
    )


def quotient_code(
    phase: Phase,
    class_maps: tuple[dict[int, int], ...],
) -> tuple[int, ...]:
    return tuple(
        class_maps[index][value]
        for index, value in enumerate(phase)
    )


def find_context_difference(
    sizes: tuple[int, ...],
    behavior: dict[Phase, Behavior],
    coordinate: int,
    left_value: int,
    right_value: int,
) -> tuple[tuple[int, ...], Behavior, Behavior] | None:
    for context in contexts(sizes, coordinate):
        left = insert_coordinate(
            context,
            coordinate,
            left_value,
        )
        right = insert_coordinate(
            context,
            coordinate,
            right_value,
        )
        if behavior[left] != behavior[right]:
            return context, behavior[left], behavior[right]
    return None


def verify_boolean_behavior_system(
    sizes: tuple[int, ...],
    forbidden: Phase | None = None,
) -> None:
    if forbidden is None:
        forbidden = tuple(0 for _ in sizes)
    assert len(forbidden) == len(sizes)
    assert all(
        0 <= forbidden[index] < size
        for index, size in enumerate(sizes)
    )
    phases = discharge(sizes, forbidden)

    for table in range(1 << len(phases)):
        behavior = {
            phase: ((table >> index) & 1,)
            for index, phase in enumerate(phases)
        }
        invariant = literal_invariant(
            phases,
            forbidden,
            behavior,
        )
        assert invariant == edge_invariant(
            phases,
            forbidden,
            behavior,
        )

        class_maps, classes = quotient_data(
            sizes,
            forbidden,
            behavior,
        )
        class_counts = tuple(len(groups) for groups in classes)
        effective_size = prod(class_counts) - 1
        codes = {
            quotient_code(phase, class_maps)
            for phase in phases
        }
        assert len(codes) == effective_size

        for left, right in combinations(phases, 2):
            if quotient_code(left, class_maps) == quotient_code(
                right,
                class_maps,
            ):
                assert behavior[left] == behavior[right]

        assert invariant == all(
            count <= 2
            for count in class_counts
        )

        for coordinate, groups in enumerate(classes):
            nonforbidden_groups = groups[1:]
            for left_group, right_group in combinations(
                nonforbidden_groups,
                2,
            ):
                witness = find_context_difference(
                    sizes,
                    behavior,
                    coordinate,
                    left_group[0],
                    right_group[0],
                )
                assert witness is not None
                context, left_record, right_record = witness
                left = insert_coordinate(
                    context,
                    coordinate,
                    left_group[0],
                )
                right = insert_coordinate(
                    context,
                    coordinate,
                    right_group[0],
                )
                assert mismatch(left, forbidden) == mismatch(
                    right,
                    forbidden,
                )
                assert hamming_distance(left, right) == 1
                assert left_record != right_record


def chart_options(size: int) -> tuple[tuple[int, ...], ...]:
    coarse = (0,) + tuple(1 for _ in range(size - 1))
    exact = tuple(range(size))
    options = {coarse, exact}
    if size >= 4:
        options.add((0, 1, 1) + tuple(range(2, size - 1)))
    return tuple(sorted(options))


def verify_chart_audit() -> None:
    sizes = (4, 3)
    forbidden = (0, 0)
    phases = discharge(sizes, forbidden)

    for table in range(1 << len(phases)):
        behavior = {
            phase: ((table >> index) & 1,)
            for index, phase in enumerate(phases)
        }
        class_maps, _ = quotient_data(
            sizes,
            forbidden,
            behavior,
        )

        for charts in product(*(chart_options(size) for size in sizes)):
            chart_complete = all(
                charts[coordinate][left]
                != charts[coordinate][right]
                or class_maps[coordinate][left]
                == class_maps[coordinate][right]
                for coordinate, size in enumerate(sizes)
                for left, right in combinations(range(size), 2)
            )

            if chart_complete:
                for left, right in combinations(phases, 2):
                    left_code = tuple(
                        charts[index][value]
                        for index, value in enumerate(left)
                    )
                    right_code = tuple(
                        charts[index][value]
                        for index, value in enumerate(right)
                    )
                    if left_code == right_code:
                        assert behavior[left] == behavior[right]
                continue

            found = False
            for coordinate, size in enumerate(sizes):
                for left_value, right_value in combinations(
                    range(1, size),
                    2,
                ):
                    if (
                        charts[coordinate][left_value]
                        != charts[coordinate][right_value]
                        or class_maps[coordinate][left_value]
                        == class_maps[coordinate][right_value]
                    ):
                        continue
                    witness = find_context_difference(
                        sizes,
                        behavior,
                        coordinate,
                        left_value,
                        right_value,
                    )
                    assert witness is not None
                    found = True
                    break
                if found:
                    break
            assert found


def verify_weighted_localization() -> None:
    sizes = (3, 3, 2)
    forbidden = (0, 0, 0)
    phases = discharge(sizes, forbidden)
    behavior = {
        phase: (
            (phase[0] + phase[1] + phase[2]) % 2,
            (2 * phase[0] + phase[1]) % 3,
            int(phase[0] == 2 or phase[1] == 2),
        )
        for phase in phases
    }
    buckets: defaultdict[tuple[int, int], int] = defaultdict(int)
    total = 0
    serial = 0

    for kind in range(3):
        for left, right in combinations(phases, 2):
            if (
                mismatch(left, forbidden)
                != mismatch(right, forbidden)
                or behavior[left][kind] == behavior[right][kind]
            ):
                continue
            coordinate, before, after = sensitive_edge(
                left,
                right,
                behavior,
                kind,
                forbidden,
            )
            assert hamming_distance(before, after) == 1
            assert mismatch(before, forbidden) == mismatch(
                after,
                forbidden,
            )
            assert behavior[before][kind] != behavior[after][kind]
            weight = 1 + (5 * serial + 2) % 13
            serial += 1
            buckets[(coordinate, kind)] += weight
            total += weight

    assert total > 0
    assert len(buckets) <= 3 * len(sizes)
    assert max(buckets.values()) * 3 * len(sizes) >= total


def verify_monotone_refinement() -> None:
    sizes = (3, 3, 2)
    forbidden = (0, 0, 0)
    phases = discharge(sizes, forbidden)
    scalar_components = (
        {
            phase: sum(mismatch(phase, forbidden))
            for phase in phases
        },
        {
            phase: phase[0]
            for phase in phases
        },
        {
            phase: (phase[1], phase[2])
            for phase in phases
        },
    )
    previous_maps: tuple[dict[int, int], ...] | None = None
    previous_count = 0

    for length in range(1, len(scalar_components) + 1):
        behavior = {
            phase: tuple(
                scalar_components[index][phase]
                for index in range(length)
            )
            for phase in phases
        }
        class_maps, classes = quotient_data(
            sizes,
            forbidden,
            behavior,
        )
        class_count = sum(len(groups) for groups in classes)
        assert class_count >= previous_count

        if previous_maps is not None:
            for coordinate, size in enumerate(sizes):
                for left, right in combinations(range(size), 2):
                    if (
                        class_maps[coordinate][left]
                        == class_maps[coordinate][right]
                    ):
                        assert (
                            previous_maps[coordinate][left]
                            == previous_maps[coordinate][right]
                        )
        previous_maps = class_maps
        previous_count = class_count

    assert previous_count <= sum(sizes)


def verify_record_witness_types() -> None:
    """Recover legality, private-cost, and common-cost discrepancies."""

    # Record format: fixed cost, then private values; -1 represents bottom.
    left = (4, -1, 7)
    legality = (4, 3, 7)
    private_cost = (4, -1, 9)
    common_cost = (6, -1, 7)

    assert left[1] == -1 and legality[1] != -1
    assert left[2] != -1 and private_cost[2] != -1
    assert left[2] != private_cost[2]
    assert left[0] != common_cost[0]

    # A cost discrepancy can localize to a legality edge on its path.
    sizes = (3, 3)
    forbidden = (0, 0)
    phases = discharge(sizes, forbidden)
    behavior = {
        phase: (0,)
        for phase in phases
    }
    behavior[(1, 1)] = (5,)
    behavior[(2, 1)] = (-1,)
    behavior[(2, 2)] = (7,)
    _, before, after = sensitive_edge(
        (1, 1),
        (2, 2),
        behavior,
        0,
        forbidden,
    )
    assert {
        behavior[before][0],
        behavior[after][0],
    } == {-1, 5}


def main() -> None:
    for sizes, forbidden in (
        ((2,), (0,)),
        ((3,), (2,)),
        ((2, 2), (0, 0)),
        ((3, 2), (1, 0)),
        ((1, 3, 2), (0, 2, 1)),
        ((2, 2, 2), (1, 0, 1)),
        ((3, 2, 2), (0, 0, 0)),
    ):
        verify_boolean_behavior_system(sizes, forbidden)
    verify_chart_audit()
    verify_weighted_localization()
    verify_monotone_refinement()
    verify_record_witness_types()
    print("AC one-block phase sensitivity: verified")


if __name__ == "__main__":
    main()

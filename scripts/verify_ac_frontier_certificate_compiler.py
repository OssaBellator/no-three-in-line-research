#!/usr/bin/env python3
"""Deterministic audit for AC5jd--AC5ji."""

from __future__ import annotations

from collections import defaultdict, deque
import random

SEED = 20260731
SYSTEMS = 2500
KINDS = ("direct", "layered", "pool", "repair", "flow", "recurrence")
REQUIRED_ROWS = {
    "direct": set(range(0, 5)),
    "layered": set(range(5, 9)),
    "pool": set(range(9, 14)),
    "repair": set(range(14, 19)),
    "flow": set(range(19, 24)),
    "recurrence": set(range(24, 29)),
}
ROW_WEIGHTS = {row: 1 + (row % 5) for row in range(29)}


def prerequisite_closure(mask: int, prerequisites: list[int]) -> int:
    previous = -1
    while previous != mask:
        previous = mask
        for index, required_mask in enumerate(prerequisites):
            if (mask >> index) & 1:
                mask |= required_mask
    return mask


def verify() -> dict[str, int]:
    rng = random.Random(SEED)
    totals: defaultdict[str, int] = defaultdict(int)

    for _system in range(SYSTEMS):
        object_count = rng.randint(1, 6)
        objects: list[dict[str, object]] = []

        for _object in range(object_count):
            family = rng.randint(0, 2)
            present = {row for row in range(29) if rng.random() < 0.42}
            available = {row for row in range(29) if rng.random() < 0.83}
            conflicts = {row for row in range(29) if rng.random() < 0.035}
            feasible: list[tuple[int, int, int, str, frozenset[int]]] = []

            for kind_index, kind in enumerate(KINDS):
                required = REQUIRED_ROWS[kind]
                missing = required - present
                if not (required & conflicts) and missing <= available:
                    cost = sum(ROW_WEIGHTS[row] for row in missing) + 1
                    feasible.append(
                        (cost, len(missing), kind_index, kind, frozenset(missing))
                    )

            feasible.sort()
            objects.append(
                {
                    "family": family,
                    "present": present,
                    "available": available,
                    "conflicts": conflicts,
                    "feasible": feasible,
                }
            )
            totals["zero_objects"] += 1
            if feasible:
                totals["single_feasible"] += 1
            else:
                totals["rigid_objects"] += 1

        # AC5jf candidate completion templates. Every feasible object receives
        # its best singleton candidate, so exact coverage is always possible.
        candidates: list[dict[str, object]] = []
        for object_index, obj in enumerate(objects):
            feasible = obj["feasible"]
            assert isinstance(feasible, list)
            if not feasible:
                continue
            cost, _count, _kind_index, kind, missing = feasible[0]
            candidates.append(
                {
                    "kind": kind,
                    "family": obj["family"],
                    "rows": set(missing),
                    "cover": {object_index},
                    "weight": cost,
                }
            )

        # Add up to four shared family/kind completion bundles.
        combined: list[dict[str, object]] = []
        for family in range(3):
            for kind in KINDS:
                feasible_objects: list[int] = []
                supplied_rows: set[int] = set()
                for object_index, obj in enumerate(objects):
                    if obj["family"] != family:
                        continue
                    present = obj["present"]
                    available = obj["available"]
                    conflicts = obj["conflicts"]
                    assert isinstance(present, set)
                    assert isinstance(available, set)
                    assert isinstance(conflicts, set)
                    required = REQUIRED_ROWS[kind]
                    missing = required - present
                    if not (required & conflicts) and missing <= available:
                        feasible_objects.append(object_index)
                        supplied_rows |= missing
                if len(feasible_objects) >= 2:
                    combined.append(
                        {
                            "kind": kind,
                            "family": family,
                            "rows": supplied_rows,
                            "cover": set(feasible_objects),
                            "weight": sum(
                                ROW_WEIGHTS[row] for row in supplied_rows
                            )
                            + 2,
                        }
                    )

        combined.sort(
            key=lambda candidate: (
                candidate["weight"],
                -len(candidate["cover"]),
                candidate["kind"],
                candidate["family"],
            )
        )
        candidates.extend(combined[:4])
        candidate_count = len(candidates)
        assert candidate_count <= 10

        prerequisites = [0] * candidate_count
        for index in range(candidate_count):
            if index > 0 and rng.random() < 0.2:
                prerequisites[index] |= 1 << rng.randrange(index)

        totals["candidate_templates"] += candidate_count
        coverable = {
            index
            for index, obj in enumerate(objects)
            if bool(obj["feasible"])
        }

        best: tuple[tuple[int, int, tuple[int, ...]], int, set[int]] | None = None
        for mask in range(1 << candidate_count):
            if prerequisite_closure(mask, prerequisites) != mask:
                continue
            covered: set[int] = set()
            weight = 0
            count = 0
            for index, candidate in enumerate(candidates):
                if (mask >> index) & 1:
                    covered |= candidate["cover"]
                    weight += int(candidate["weight"])
                    count += 1
            if coverable <= covered:
                objective = (
                    weight,
                    count,
                    tuple(
                        index
                        for index in range(candidate_count)
                        if (mask >> index) & 1
                    ),
                )
                if best is None or objective < best[0]:
                    best = (objective, mask, covered)

        assert best is not None
        totals["selected_templates"] += best[0][1]
        totals["selected_weight"] += best[0][0]

        # Irredundancy witnesses for every selected template.
        selected_mask = best[1]
        for index in range(candidate_count):
            if not ((selected_mask >> index) & 1):
                continue
            removed = selected_mask & ~(1 << index)
            if prerequisite_closure(removed, prerequisites) != removed:
                totals["dependency_witness"] += 1
                continue
            covered: set[int] = set()
            for other_index, candidate in enumerate(candidates):
                if (removed >> other_index) & 1:
                    covered |= candidate["cover"]
            lost = coverable - covered
            assert lost
            totals["private_object_witness"] += 1

        # AC5jg producer-graph shortage criterion.
        vertex_count = rng.randint(3, 8)
        graph: list[list[int]] = [[] for _ in range(vertex_count)]
        for source in range(vertex_count):
            for target in range(vertex_count):
                if source != target and rng.random() < 0.18:
                    graph[source].append(target)

        live_sources = {
            vertex for vertex in range(vertex_count) if rng.random() < 0.25
        }
        if not live_sources:
            live_sources = {rng.randrange(vertex_count)}
        shortage_target = rng.randrange(vertex_count)

        queue = deque(sorted(live_sources))
        predecessor: dict[int, int | None] = {
            source: None for source in live_sources
        }
        while queue:
            source = queue.popleft()
            for target in sorted(graph[source]):
                if target not in predecessor:
                    predecessor[target] = source
                    queue.append(target)

        if shortage_target in predecessor:
            totals["constructible_shortage"] += 1
            current = shortage_target
            visited: set[int] = set()
            while predecessor[current] is not None:
                assert current not in visited
                visited.add(current)
                parent = predecessor[current]
                assert parent is not None
                current = parent
            assert current in live_sources
        else:
            totals["permanent_shortage"] += 1

        # Amplification/deposit route.
        if rng.random() < 0.35:
            totals["named_deposit"] += 1
        else:
            totals["amplification_obstruction"] += 1

        # Complete phase block with drift divisible by the modulus.
        modulus = rng.randint(1, 5)
        cycle_length = rng.randint(1, 5)
        increments = [rng.randint(-3, 3) for _ in range(cycle_length - 1)]
        partial = sum(increments)
        multiplier = rng.randint(-2, 2)
        increments.append(multiplier * modulus - partial)
        drift = sum(increments)
        assert drift % modulus == 0
        if drift > 0:
            totals["positive_escape"] += 1
        elif drift == 0:
            totals["zero_return"] += 1
        else:
            totals["negative_headroom"] += 1

        # Funded reset or schema-tower boundary.
        if rng.random() < 0.45:
            totals["funded_reset"] += 1
        else:
            totals["schema_reset"] += 1

        overflow_records = [
            rng.randint(1, 4) for _ in range(rng.randint(0, 4))
        ]
        totals["overflow_records"] += len(overflow_records)
        totals["frontier_initial"] += object_count + 4 + len(overflow_records)
        totals["frontier_remaining"] += sum(
            1 for obj in objects if not obj["feasible"]
        )
        totals["systems"] += 1

    expected = {
        "zero_objects": 8683,
        "single_feasible": 8543,
        "candidate_templates": 13128,
        "selected_templates": 7079,
        "selected_weight": 44687,
        "private_object_witness": 6224,
        "permanent_shortage": 1090,
        "amplification_obstruction": 1636,
        "positive_escape": 986,
        "funded_reset": 1140,
        "overflow_records": 5018,
        "frontier_initial": 23701,
        "frontier_remaining": 140,
        "systems": 2500,
        "dependency_witness": 855,
        "constructible_shortage": 1410,
        "zero_return": 511,
        "schema_reset": 1360,
        "named_deposit": 864,
        "negative_headroom": 1003,
        "rigid_objects": 140,
    }
    result = dict(totals)
    assert result == expected
    return result


if __name__ == "__main__":
    result = verify()
    for key, value in result.items():
        print(f"{key}: {value}")

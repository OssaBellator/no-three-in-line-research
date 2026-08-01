#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations

N = 5
LEFT_RESOURCE = 0
EDGES = {(left, right) for left in range(N) for right in range(N)}

# One-free-resource lift of experiments/binary-resource-star-conditioning-example.json.
CONFLICTS = (
    ((0, 0), (1, 1)),
    ((0, 0), (1, 2)),
    ((0, 0), (1, 3)),
    ((0, 1), (1, 0)),
    ((0, 3), (2, 0)),
    ((0, 3), (3, 1)),
)
FIBRES = {(0, column): set() for column in range(N)}
for first, second in CONFLICTS:
    centre, partner = (first, second) if first[0] == LEFT_RESOURCE else (second, first)
    FIBRES[centre].add(partner)


def decoded_pair(syndrome, choice, columns, second_row):
    return (
        (0, columns[choice]),
        (second_row, columns[(choice + syndrome + 1) % 4]),
    )


def residual_matchings(pair):
    centre = pair[0]
    rows = [row for row in range(N) if row not in {pair[0][0], pair[1][0]}]
    columns = [column for column in range(N) if column not in {pair[0][1], pair[1][1]}]
    forbidden = FIBRES[centre]
    out = []
    for image in permutations(columns):
        matching = tuple(zip(rows, image))
        if all(cell in EDGES and cell not in forbidden for cell in matching):
            out.append(matching)
    return tuple(out)


def blocker_number(matchings):
    used = sorted(set().union(*(set(matching) for matching in matchings)))
    for size in range(1, len(used) + 1):
        for subset in combinations(used, size):
            forbidden = set(subset)
            if all(forbidden.intersection(matching) for matching in matchings):
                return size
    raise AssertionError("nonempty matching family must have a blocker")


conflict_sets = {frozenset(conflict) for conflict in CONFLICTS}
records = []
for second_row in range(1, N):
    for columns in permutations(range(N), 4):
        pair_records = []
        valid = True
        for syndrome in range(3):
            for choice in range(4):
                pair = decoded_pair(syndrome, choice, columns, second_row)
                if frozenset(pair) in conflict_sets:
                    valid = False
                    break
                matchings = residual_matchings(pair)
                if not matchings:
                    valid = False
                    break
                pair_records.append(
                    {
                        "key": (syndrome, choice),
                        "pair": pair,
                        "matching_count": len(matchings),
                        "blocker_number": blocker_number(matchings),
                    }
                )
            if not valid:
                break
        if valid:
            records.append(
                {
                    "second_row": second_row,
                    "columns": columns,
                    "pairs": tuple(pair_records),
                    "minimum_blocker": min(record["blocker_number"] for record in pair_records),
                    "total_matchings": sum(record["matching_count"] for record in pair_records),
                }
            )

assert len(records) == 96
minimum_distribution = Counter(record["minimum_blocker"] for record in records)
assert minimum_distribution == {1: 24, 2: 72}
assert max(record["minimum_blocker"] for record in records) == 2

best = max(records, key=lambda record: (record["minimum_blocker"], record["total_matchings"]))
assert best["second_row"] == 1
assert best["columns"] == (1, 2, 3, 4)
assert best["total_matchings"] == 64
assert sorted(record["blocker_number"] for record in best["pairs"]) == [2, 2, 2] + [3] * 9
assert sorted(record["matching_count"] for record in best["pairs"]) == [3, 3, 4] + [6] * 9

print(
    {
        "source_fixture": "one-free-resource lift of binary-resource-star-conditioning-example.json",
        "candidate_embeddings_checked": 4 * 120,
        "valid_complete_choice_grid_embeddings": len(records),
        "uniformly_single_exclusion_robust_embeddings": minimum_distribution[2],
        "fragile_embeddings": minimum_distribution[1],
        "best_embedding": {
            "second_left_resource": best["second_row"],
            "choice_columns": best["columns"],
            "total_conditional_matchings": best["total_matchings"],
            "minimum_blocker_number": best["minimum_blocker"],
            "blocker_distribution": sorted(record["blocker_number"] for record in best["pairs"]),
        },
        "remaining_gap": "the extra free resource is a finite source-typed lift, not an endpoint resource supplied by the asymptotic prime-patching host",
        "evidence_level": "source_typed_five_resource_hall_fixture",
        "status": "passed",
    }
)

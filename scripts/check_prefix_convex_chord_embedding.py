#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations
from math import factorial

N = 30
J = 9


def profile_count(size, binary):
    unary = size - 1 - 2 * binary
    if unary < 0:
        return 0
    return factorial(size - 1) // (
        factorial(unary) * factorial(binary) * factorial(binary + 1)
    )


ROOT_TYPES = ("L", "U", "B")
count = [[{kind: 0 for kind in ROOT_TYPES} for _ in range(N + 1)] for _ in range(N + 1)]
risk_total = [[{kind: 0 for kind in ROOT_TYPES} for _ in range(N + 1)] for _ in range(N + 1)]
span_total = [[{kind: 0 for kind in ROOT_TYPES} for _ in range(N + 1)] for _ in range(N + 1)]
count[1][0]["L"] = 1

for size in range(2, N + 1):
    for binary in range((size - 1) // 2 + 1):
        for child_type in ROOT_TYPES:
            child_count = count[size - 1][binary][child_type]
            if child_count:
                count[size][binary]["U"] += child_count
                risk_total[size][binary]["U"] += (
                    risk_total[size - 1][binary][child_type]
                    + int(child_type == "U") * child_count
                )
                span_total[size][binary]["U"] += (
                    span_total[size - 1][binary][child_type]
                    + int(child_type == "U") * (size - 1) * child_count
                )
        if binary:
            for left_size in range(1, size - 1):
                right_size = size - 1 - left_size
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for left_type in ROOT_TYPES:
                        left_count = count[left_size][left_binary][left_type]
                        if not left_count:
                            continue
                        for right_type in ROOT_TYPES:
                            right_count = count[right_size][right_binary][right_type]
                            if not right_count:
                                continue
                            count[size][binary]["B"] += left_count * right_count
                            risk_total[size][binary]["B"] += (
                                risk_total[left_size][left_binary][left_type] * right_count
                                + risk_total[right_size][right_binary][right_type] * left_count
                            )
                            span_total[size][binary]["B"] += (
                                span_total[left_size][left_binary][left_type] * right_count
                                + span_total[right_size][right_binary][right_type] * left_count
                            )

family = sum(count[N][J].values())
aggregate_risk = sum(risk_total[N][J].values())
aggregate_span = sum(span_total[N][J].values())
assert family == profile_count(N, J) == 168212023980
assert aggregate_risk == 638045608200
assert aggregate_span == 4963626417750


@lru_cache(None)
def trees(size):
    out = []
    if size == 1:
        out.append(("L",))
    if size >= 2:
        out.extend(("U", child) for child in trees(size - 1))
        for left_size in range(1, size - 1):
            right_size = size - 1 - left_size
            out.extend(
                ("B", left, right)
                for left in trees(left_size)
                for right in trees(right_size)
            )
    return tuple(out)


def assign_preorder_intervals(tree, start=0):
    kind = tree[0]
    if kind == "L":
        return start + 1, [(start, start)], []
    if kind == "U":
        end, intervals, uu_edges = assign_preorder_intervals(tree[1], start + 1)
        parent_interval = (start, end - 1)
        child_interval = intervals[0]
        edges = list(uu_edges)
        if tree[1][0] == "U":
            edges.append((parent_interval, child_interval))
        return end, [parent_interval] + intervals, edges
    end_left, left_intervals, left_edges = assign_preorder_intervals(tree[1], start + 1)
    end, right_intervals, right_edges = assign_preorder_intervals(tree[2], end_left)
    parent_interval = (start, end - 1)
    return end, [parent_interval] + left_intervals + right_intervals, left_edges + right_edges


def laminar(first, second):
    a, b = first
    c, d = second
    return b < c or d < a or (a <= c and d <= b) or (c <= a and b <= d)


def parabola_collinear(i, j, k):
    a, b, c = (i, i * i), (j, j * j), (k, k * k)
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


checked_trees = 0
checked_uu_edges = 0
for size in range(1, 10):
    for tree in trees(size):
        end, intervals, uu_edges = assign_preorder_intervals(tree)
        assert end == size
        assert all(laminar(first, second) for first, second in combinations(intervals, 2))
        for parent, child in uu_edges:
            assert parent[0] <= child[0] <= child[1] <= parent[1]
            checked_uu_edges += 1
        for i, j, k in combinations(range(size), 3):
            assert not parabola_collinear(i, j, k)
        checked_trees += 1

assert checked_trees == 539

print({
    "profile_family_size": family,
    "aggregate_ancestry_risk": aggregate_risk,
    "aggregate_interval_span": aggregate_span,
    "convex_embedding": "encoded node k maps to (k,k^2); every subtree is its preorder interval",
    "structural_result": "all subtree intervals are laminar, so their chords are nested or disjoint",
    "collinear_support_triples_in_convex_embedding": 0,
    "finite_audit_trees_through_size_9": checked_trees,
    "finite_audit_unary_unary_edges": checked_uu_edges,
    "conclusion": "positive interval-span and nesting risk coexist with zero support-point collinear triples in the canonical convex embedding",
    "remaining_gap": "interval span is not itself a geometric collinearity risk; actual support-chord coordinates need additional incidence structure",
    "evidence_level": "exact_coordinate_embedding_mismatch",
    "status": "passed",
})

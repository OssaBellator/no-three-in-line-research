#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
from math import factorial

N = 30
J = 9
ROOT_TYPES = ("L", "U", "B")


def profile_count(n, j):
    unary = n - 1 - 2 * j
    if unary < 0:
        return 0
    return factorial(n - 1) // (
        factorial(unary) * factorial(j) * factorial(j + 1)
    )


# dp[n][j][root_type][risk] counts ordered unary-binary trees by total nodes,
# binary nodes, root type, and unary-to-unary edges.
dp = [
    [
        {root_type: defaultdict(int) for root_type in ROOT_TYPES}
        for _ in range(N + 1)
    ]
    for _ in range(N + 1)
]
dp[1][0]["L"][0] = 1

for nodes in range(2, N + 1):
    for binary in range((nodes - 1) // 2 + 1):
        for child_type in ROOT_TYPES:
            for risk, count in dp[nodes - 1][binary][child_type].items():
                dp[nodes][binary]["U"][risk + int(child_type == "U")] += count

        if binary:
            for left_nodes in range(1, nodes - 1):
                right_nodes = nodes - 1 - left_nodes
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for left_type in ROOT_TYPES:
                        for left_risk, left_count in dp[left_nodes][left_binary][left_type].items():
                            for right_type in ROOT_TYPES:
                                for right_risk, right_count in dp[right_nodes][right_binary][right_type].items():
                                    dp[nodes][binary]["B"][left_risk + right_risk] += left_count * right_count


def distribution(nodes, binary):
    out = defaultdict(int)
    for root_type in ROOT_TYPES:
        for risk, count in dp[nodes][binary][root_type].items():
            out[risk] += count
    return dict(sorted(out.items()))


def find_tree(nodes, binary, risk, requested_type=None):
    types = (requested_type,) if requested_type else ROOT_TYPES
    for root_type in types:
        if not dp[nodes][binary][root_type].get(risk, 0):
            continue
        if root_type == "L":
            return ("L",)
        if root_type == "U":
            for child_type in ROOT_TYPES:
                extra = int(child_type == "U")
                if risk >= extra and dp[nodes - 1][binary][child_type].get(risk - extra, 0):
                    child = find_tree(nodes - 1, binary, risk - extra, child_type)
                    if child is not None:
                        return ("U", child)
        if root_type == "B":
            for left_nodes in range(1, nodes - 1):
                right_nodes = nodes - 1 - left_nodes
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for left_type in ROOT_TYPES:
                        for left_risk in range(risk + 1):
                            if not dp[left_nodes][left_binary][left_type].get(left_risk, 0):
                                continue
                            for right_type in ROOT_TYPES:
                                if not dp[right_nodes][right_binary][right_type].get(risk - left_risk, 0):
                                    continue
                                left = find_tree(left_nodes, left_binary, left_risk, left_type)
                                right = find_tree(right_nodes, right_binary, risk - left_risk, right_type)
                                if left is not None and right is not None:
                                    return ("B", left, right)
    return None


def tree_stats(tree):
    kind = tree[0]
    if kind == "L":
        return {
            "nodes": 1,
            "binary": 0,
            "unary": 0,
            "leaves": 1,
            "risk": 0,
            "root": "L",
        }
    if kind == "U":
        child = tree_stats(tree[1])
        return {
            "nodes": child["nodes"] + 1,
            "binary": child["binary"],
            "unary": child["unary"] + 1,
            "leaves": child["leaves"],
            "risk": child["risk"] + int(child["root"] == "U"),
            "root": "U",
        }
    left = tree_stats(tree[1])
    right = tree_stats(tree[2])
    return {
        "nodes": left["nodes"] + right["nodes"] + 1,
        "binary": left["binary"] + right["binary"] + 1,
        "unary": left["unary"] + right["unary"],
        "leaves": left["leaves"] + right["leaves"],
        "risk": left["risk"] + right["risk"],
        "root": "B",
    }


def encode(tree):
    if tree[0] == "L":
        return "L"
    if tree[0] == "U":
        return f"U({encode(tree[1])})"
    return f"B({encode(tree[1])},{encode(tree[2])})"


size_two = ("U", ("L",))
assert tree_stats(size_two) == {
    "nodes": 2,
    "binary": 0,
    "unary": 1,
    "leaves": 1,
    "risk": 0,
    "root": "U",
}
assert profile_count(2, 0) == 1

risk_distribution = distribution(N, J)
family = sum(risk_distribution.values())
assert family == profile_count(N, J) == 168212023980
assert risk_distribution == {
    0: 367479684,
    1: 4491418360,
    2: 20211382620,
    3: 44097562080,
    4: 51447155760,
    5: 33242777568,
    6: 11872420560,
    7: 2261413440,
    8: 212007510,
    9: 8314020,
    10: 92378,
}

total_risk = sum(risk * count for risk, count in risk_distribution.items())
assert total_risk == 638045608200
assert Fraction(total_risk, family) == Fraction(110, 29)

good_count = sum(count for risk, count in risk_distribution.items() if risk <= 5)
assert good_count == 153857776072

witness = find_tree(N, J, 0)
assert witness is not None
stats = tree_stats(witness)
assert stats["nodes"] == N
assert stats["binary"] == J
assert stats["unary"] == N - 1 - 2 * J == 11
assert stats["leaves"] == J + 1 == 10
assert stats["risk"] == 0
encoding = encode(witness)

print({
    "grading_correction": {
        "z_marks": "total nodes",
        "counterexample_to_leaf_grading": "U(L) has z-degree 2 and one leaf",
    },
    "profile": {
        "total_nodes": N,
        "binary_nodes": J,
        "unary_nodes": 11,
        "leaves": 10,
        "family_size": family,
    },
    "unary_unary_risk_distribution": risk_distribution,
    "aggregate_risk": total_risk,
    "expected_risk": str(Fraction(total_risk, family)),
    "objects_with_risk_at_most_5": good_count,
    "canonical_zero_risk_witness": encoding,
    "evidence_level": "independently_enumerated_combinatorial_model",
    "status": "passed",
})

#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

N = 30
J = 9
ROOT_TYPES = ("L", "U", "B")


def profile_count(size, binary):
    unary = size - 1 - 2 * binary
    if unary < 0:
        return 0
    return factorial(size - 1) // (
        factorial(unary) * factorial(binary) * factorial(binary + 1)
    )


count = [[{kind: 0 for kind in ROOT_TYPES} for _ in range(N + 1)] for _ in range(N + 1)]
risk_total = [[{kind: 0 for kind in ROOT_TYPES} for _ in range(N + 1)] for _ in range(N + 1)]
span_total = [[{kind: 0 for kind in ROOT_TYPES} for _ in range(N + 1)] for _ in range(N + 1)]
count[1][0]["L"] = 1

for size in range(2, N + 1):
    for binary in range((size - 1) // 2 + 1):
        for child_type in ROOT_TYPES:
            child_count = count[size - 1][binary][child_type]
            if not child_count:
                continue
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
assert Fraction(aggregate_risk, family) == Fraction(110, 29)
assert aggregate_span == 4963626417750
assert Fraction(aggregate_span, family) == Fraction(7186475, 243542)

print({
    "profile": {"original_leaves": N, "encoded_size": N, "encoded_binary_nodes": J},
    "family_size": family,
    "ancestry_edge_risk_total": aggregate_risk,
    "mean_ancestry_edge_risk": str(Fraction(aggregate_risk, family)),
    "support_interval_span_total": aggregate_span,
    "mean_support_interval_span": str(Fraction(aggregate_span, family)),
    "coordinate_label": "encoded child size, equivalently canonical inorder support-interval span",
    "remaining_gap": "the canonical intervals are not yet embedded as actual prime-patching support chords",
    "evidence_level": "ancestry_aware_coordinate_dp",
    "status": "passed",
})

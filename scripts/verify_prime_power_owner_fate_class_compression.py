#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from math import lcm


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise AssertionError(msg)


def key(item):
    return tuple(item[name] for name in ("owner", "fate", "collision", "line", "interface", "provenance"))


credits = [
    dict(owner="A", fate="self", collision="clean", line="L1", interface="I0", provenance="p", a=Fraction(1, 3)),
    dict(owner="A", fate="self", collision="clean", line="L1", interface="I0", provenance="p", a=Fraction(1, 6)),
    dict(owner="A", fate="child", collision="clean", line="L1", interface="I0", provenance="p", a=Fraction(1, 4)),
    dict(owner="B", fate="self", collision="hit", line="L2", interface="I1", provenance="q", a=Fraction(2, 5)),
]
weights = {
    key(credits[0]): Fraction(7, 5),
    key(credits[2]): Fraction(3, 2),
    key(credits[3]): Fraction(9, 7),
}
grouped = {}
for credit in credits:
    grouped[key(credit)] = grouped.get(key(credit), Fraction()) + credit["a"]
require(grouped[key(credits[0])] == Fraction(1, 2), "exact class sum")
lhs = sum(credit["a"] * weights[key(credit)] for credit in credits)
rhs = sum(coefficient * weights[class_key] for class_key, coefficient in grouped.items())
require(lhs == rhs, "lossless weighted compression")
projected = lambda class_key: (class_key[0], class_key[2], class_key[3], class_key[4], class_key[5])
require(
    projected(key(credits[0])) == projected(key(credits[2])) and key(credits[0]) != key(credits[2]),
    "projection warning",
)
rows = [
    {"self": Fraction(1, 3), "child": Fraction(1, 4)},
    {"self": Fraction(2, 5), "child": Fraction(1, 5)},
]
upper = {name: max(row.get(name, Fraction()) for row in rows) for name in {"self", "child"}}
for row in rows:
    require(all(row.get(name, Fraction()) <= upper[name] for name in upper), "upper fibre domination")
denominator = 1
for value in [*grouped.values(), *weights.values(), lhs]:
    denominator = lcm(denominator, value.denominator)
require(
    denominator * lhs
    == sum(denominator * coefficient * weights[class_key] for class_key, coefficient in grouped.items()),
    "integer clearing",
)
print(f"verified owner-fate compression classes={len(grouped)} denominator={denominator}")

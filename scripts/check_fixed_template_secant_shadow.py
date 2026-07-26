#!/usr/bin/env python3
"""Check fixed-template secant-shadow descent in a tied matching block."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter
from pathlib import Path
from typing import Iterable, Sequence

Point = tuple[int, int]
Line = tuple[int, int, int]


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    pts = list(points)
    return len(set(pts)) == len(pts) and all(
        not collinear(a, b, c) for a, b, c in itertools.combinations(pts, 3)
    )


def source_from_layers(layers: Sequence[Sequence[int]]) -> set[Point]:
    return {(column, row) for layer in layers for column, row in enumerate(layer)}


def normalized_line(a: Point, b: Point) -> Line:
    x1, y1 = a
    x2, y2 = b
    aa = y1 - y2
    bb = x2 - x1
    cc = x1 * y2 - x2 * y1
    divisor = math.gcd(math.gcd(abs(aa), abs(bb)), abs(cc))
    if divisor:
        aa //= divisor
        bb //= divisor
        cc //= divisor
    if aa < 0 or (aa == 0 and bb < 0):
        aa, bb, cc = -aa, -bb, -cc
    return aa, bb, cc


def on_line(line: Line, point: Point) -> bool:
    aa, bb, cc = line
    x, y = point
    return aa * x + bb * y + cc == 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    q = int(data["q"])
    template = {tuple(point) for point in data["template"]}
    initial_layer = tuple(data["initial_layer"])
    opposite_layer = tuple(data["opposite_layer"])
    replacement_layer = tuple(data["replacement_layer"])

    assert no_three(template), "template is not internally no-three"
    before = source_from_layers([initial_layer, opposite_layer])
    after = source_from_layers([replacement_layer, opposite_layer])
    assert no_three(before), "initial source is not no-three"
    assert no_three(after), "replacement source is not no-three"

    lines = {normalized_line(a, b) for a, b in itertools.combinations(template, 2)}
    assert len(lines) == math.comb(len(template), 2)

    rectangle = {(x, y) for x in range(q) for y in range(q)}
    shadow = {
        point
        for point in rectangle - template
        if any(on_line(line, point) for line in lines)
    }

    initial_selected = {(i, initial_layer[i]) for i in range(q)}
    final_selected = {(i, replacement_layer[i]) for i in range(q)}
    initial_bad = len(initial_selected & shadow)
    final_bad = len(final_selected & shadow)
    clean_replacements = q - final_bad
    assert initial_bad == q
    assert clean_replacements > 0

    before_shadow = len(before & shadow)
    after_shadow = len(after & shadow)
    assert after_shadow - before_shadow == final_bad - initial_bad

    nonaxis_traces = []
    axis_lines = 0
    for line in lines:
        aa, bb, _ = line
        trace_size = sum(on_line(line, point) for point in rectangle)
        if aa == 0 or bb == 0:
            axis_lines += 1
        else:
            nonaxis_traces.append(trace_size)

    full_nonaxis = sum(size == q for size in nonaxis_traces)
    assert full_nonaxis <= 2

    print("endpoint side", q)
    print("template size", len(template))
    print("template secant lines", len(lines))
    print("axis secant lines", axis_lines)
    print("nonaxis secant lines", len(nonaxis_traces))
    print("nonaxis trace-size counts", sorted(Counter(nonaxis_traces).items()))
    print("full nonaxis traces", full_nonaxis)
    print("secant-shadow cells", len(shadow))
    print("initial selected bad witnesses", initial_bad)
    print("final selected bad witnesses", final_bad)
    print("secant-clean replacements", clean_replacements)
    print("full-source shadow count before", before_shadow)
    print("full-source shadow count after", after_shadow)
    print("exact shadow change", after_shadow - before_shadow)
    print("outcome fixed_template_secant_shadow_descent")


if __name__ == "__main__":
    main()

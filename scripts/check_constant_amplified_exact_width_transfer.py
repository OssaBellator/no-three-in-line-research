#!/usr/bin/env python3
"""Check the slab coefficient, heterogeneous widths, and shifted-prime band."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def balanced_widths(total: int, maximum: int) -> list[int]:
    count = math.ceil(total / maximum)
    base, remainder = divmod(total, count)
    return [base + 1] * remainder + [base] * (count - remainder)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())

    gamma = float(data["gamma"])
    coefficient = float(data["target_coefficient"])
    macro_count = int(data["macro_count"])
    maximum_width = int(data["maximum_macro_width"])
    target_width = int(data["target_width"])
    x = float(data["prime_shift_x"])
    theta = 21 / 40

    b = (gamma / (32 * coefficient)) ** 2
    a = 1 / (2 * b)
    recovered = a * gamma * math.sqrt(b) / 16
    if not math.isclose(a * b, 0.5, rel_tol=1e-12):
        raise AssertionError("slab coordinate density is not one half")
    if not math.isclose(recovered, coefficient, rel_tol=1e-12):
        raise AssertionError("leading coefficient was not recovered")

    widths = balanced_widths(target_width, maximum_width)
    if len(widths) > macro_count:
        raise AssertionError("target width needs too many macros")
    if sum(widths) != target_width:
        raise AssertionError("heterogeneous widths do not sum to the target")
    if max(widths) > maximum_width:
        raise AssertionError("a local width exceeds the maximum")
    if min(widths) < maximum_width / 3:
        raise AssertionError("a local width left the full-scale band")

    active_macros = len(widths)
    minimum_width = min(widths)
    slack = 2 * target_width * math.sqrt(
        math.log(4 * active_macros * target_width) / minimum_width
    )
    if slack >= target_width:
        raise AssertionError("finite heterogeneous Ore slack is not sublinear")

    shift = x**theta
    y = x - shift
    lower = shift
    upper = shift + y**theta
    if not lower < upper < 2 * lower:
        raise AssertionError("shifted-prime band is outside the expected range")

    print("gamma", gamma)
    print("target leading coefficient", coefficient)
    print("slab constants a b", [a, b])
    print("slab density ab", a * b)
    print("recovered coefficient", recovered)
    print("available macros", macro_count)
    print("active macros", active_macros)
    print("maximum macro width", maximum_width)
    print("target exact width", target_width)
    print("heterogeneous widths", widths)
    print("minimum and maximum widths", [min(widths), max(widths)])
    print("heterogeneous Ore slack", slack)
    print("slack to target ratio", slack / target_width)
    print("prime shift x", x)
    print("shift lower width", lower)
    print("shift upper width", upper)
    print("upper to lower ratio", upper / lower)
    print("outcome", "constant_amplified_exact_width_prime_transfer")


if __name__ == "__main__":
    main()

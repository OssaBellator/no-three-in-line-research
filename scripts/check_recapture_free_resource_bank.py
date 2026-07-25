#!/usr/bin/env python3
"""Check the recapture-free resource-bank support endpoint."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()
    data = json.loads(args.instance.read_text(encoding="utf-8"))

    q = int(data["q"])
    lambda_src = float(data["lambda_src"])
    high_support = float(data["high_support"])
    recapture_support = int(data.get("recapture_support", 0))
    unary = [int(x) for x in data["unary_degrees"]]
    binary = [int(x) for x in data["binary_degrees"]]
    if len(unary) != q or len(binary) != q:
        raise ValueError("degree lists must have length q")
    if recapture_support != 0:
        raise AssertionError("the selected bank is not recapture-free")

    d1 = max(unary, default=0)
    d2 = max(binary, default=0)
    local_mass = lambda_src + d1 / q + d2 / (q * (q - 1))

    if local_mass <= 1 / 24 and high_support < 1:
        outcome = "zero_insertion_paid_completion"
    else:
        rho = float(data.get("core_fraction", 0.1))
        unary_high = sum(d >= rho * q for d in unary)
        binary_high = sum(d >= rho * q * q for d in binary)
        if unary_high >= rho * q:
            outcome = "foreign_unary_linear_core"
        elif binary_high >= rho * q:
            outcome = "foreign_binary_linear_core"
        else:
            outcome = "source_or_host_failure"

    result = {
        "q": q,
        "recapture_support": recapture_support,
        "max_foreign_unary_degree": d1,
        "max_foreign_binary_degree": d2,
        "local_mass": local_mass,
        "local_mass_threshold": 1 / 24,
        "high_support": high_support,
        "outcome": outcome,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

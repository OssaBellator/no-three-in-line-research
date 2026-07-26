#!/usr/bin/env python3
"""Check finite monotone termination of repeated fixed-infrastructure attempts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    initial = int(data["initial_potential"])
    repair_credits = [int(value) for value in data["repair_credits"]]
    final_outcome = str(data["final_outcome"])

    if initial < 0:
        raise AssertionError("potential must be nonnegative")
    if any(credit <= 0 for credit in repair_credits):
        raise AssertionError("every failed attempt must produce positive credit")
    if final_outcome != "patch_installed":
        raise AssertionError("stored terminal attempt is not successful")

    values = [initial]
    current = initial
    for credit in repair_credits:
        current -= credit
        if current < 0:
            raise AssertionError("repair sequence drove the potential below zero")
        if current >= values[-1]:
            raise AssertionError("failed attempt did not strictly decrease the potential")
        values.append(current)

    if len(repair_credits) > initial:
        raise AssertionError("integer descent exceeded the trivial initial-potential bound")

    print("initial potential", initial)
    print("repair credits", repair_credits)
    print("potential values", values)
    print("failed attempts", len(repair_credits))
    print("trivial failure bound", initial)
    print("terminal outcome", final_outcome)
    print("outcome", "monotone_fixed_infrastructure_allocation_termination")


if __name__ == "__main__":
    main()

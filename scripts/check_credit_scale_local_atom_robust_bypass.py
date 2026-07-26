#!/usr/bin/env python3
"""Check the finite inequalities in docs/230."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()

    data = json.loads(args.instance.read_text())
    R = int(data["R"])
    xi = float(data["xi"])
    s = int(data["inserted_state_size"])
    d_m = int(data["local_unary_movement_degree"])
    d_f = int(data["local_unary_refill_degree"])
    binary_weights = [int(x) for x in data["binary_atom_weights"]]
    marked_credit = int(data["marked_credit"])
    local_atom_weights = [int(x) for x in data["local_atom_weights"]]
    failed_loss = int(data["failed_domain_unary_loss"])
    fibre = int(data["failed_domain_largest_cell_type_fibre"])

    binary_domain_loss = s * (s - 1)
    unary_domain_loss = d_m + d_f
    margin = xi * R
    combined_domain_loss = unary_domain_loss + binary_domain_loss
    star_lower_bound = xi * R / (2 * s)

    assert len(local_atom_weights) <= 10
    assert max(local_atom_weights, default=0) <= marked_credit
    assert combined_domain_loss <= margin
    assert failed_loss > margin
    assert fibre > star_lower_bound

    print("R", R)
    print("xi margin", f"{margin:.6f}")
    print("inserted state size", s)
    print("binary atom weighted multiplicity", sum(binary_weights))
    print("binary simple domain loss", binary_domain_loss)
    print("local unary movement degree", d_m)
    print("local unary refill degree", d_f)
    print("combined robust domain loss", combined_domain_loss)
    print("local atom count", len(local_atom_weights))
    print("marked removal credit", marked_credit)
    print("failed unary domain loss", failed_loss)
    print("source-star lower bound", f"{star_lower_bound:.6f}")
    print("stored source-star fibre", fibre)
    print("outcome robust_atom_bypass_or_composite_source_star")


if __name__ == "__main__":
    main()

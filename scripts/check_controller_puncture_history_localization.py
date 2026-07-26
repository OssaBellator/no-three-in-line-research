#!/usr/bin/env python3
"""Finite diagnostics for docs/231."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

Record = Tuple[str, str, str, str, str, str]
# centre, candidate, side, controller, label, partner


def maximum_centre_candidate_matching(records: List[Record]) -> List[Record]:
    by_centre: Dict[str, List[Record]] = defaultdict(list)
    for rec in records:
        by_centre[rec[0]].append(rec)

    owner: Dict[str, str] = {}
    chosen: Dict[str, Record] = {}

    def augment(centre: str, seen: set[str]) -> bool:
        for rec in by_centre[centre]:
            candidate = rec[1]
            if candidate in seen:
                continue
            seen.add(candidate)
            previous = owner.get(candidate)
            if previous is None or augment(previous, seen):
                owner[candidate] = centre
                chosen[centre] = rec
                return True
        return False

    for centre in by_centre:
        augment(centre, set())
    return list(chosen.values())


def greedy_full_resource_matching(records: List[Record]) -> List[Record]:
    used_partner: set[str] = set()
    used_controller: set[str] = set()
    used_label: set[str] = set()
    selected: List[Record] = []
    for rec in records:
        _, _, _, controller, label, partner = rec
        if partner in used_partner or controller in used_controller or label in used_label:
            continue
        selected.append(rec)
        used_partner.add(partner)
        used_controller.add(controller)
        used_label.add(label)
    return selected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()
    data = json.loads(args.instance.read_text())

    H = int(data["centres"])
    W = int(data["star_width"])
    D = int(data.get("threshold", W))

    repeated: List[Record] = []
    diffuse: List[Record] = []
    for i in range(H):
        centre = f"p{i}"
        for j in range(W):
            repeated_candidate = "z_shared" if j == 0 else f"zr_{i}_{j}"
            repeated.append(
                (centre, repeated_candidate, "M", f"er_{i}_{j}", f"Ar_{i}_{j}", f"qr_{i}_{j}")
            )
            diffuse.append(
                (centre, f"zd_{i}_{j}", "M", f"ed_{i}_{j}", f"Ad_{i}_{j}", f"qd_{i}_{j}")
            )

    assert len(repeated) == H * W
    assert len(diffuse) == H * W

    repeated_degrees = Counter(rec[1] for rec in repeated)
    diffuse_degrees = Counter(rec[1] for rec in diffuse)
    repeated_max = max(repeated_degrees.values())
    diffuse_max = max(diffuse_degrees.values())

    assert repeated_max >= D
    assert diffuse_max < D

    candidate_matching = maximum_centre_candidate_matching(diffuse)
    candidate_lower = H * W / (W + D)
    assert len(candidate_matching) >= candidate_lower

    one_side = [rec for rec in candidate_matching if rec[2] == "M"]
    partner_degree = max(Counter(rec[5] for rec in one_side).values(), default=0)
    controller_degree = max(Counter(rec[3] for rec in one_side).values(), default=0)
    label_degree = max(Counter(rec[4] for rec in one_side).values(), default=0)
    assert max(partner_degree, controller_degree, label_degree) < D

    full_matching = greedy_full_resource_matching(one_side)
    resource_lower = len(candidate_matching) / (6 * D)
    assert len(full_matching) >= resource_lower

    print("puncture centres", H)
    print("designated width per centre", W)
    print("history incidence records", H * W)
    print("threshold", D)
    print("repeated exact candidate degree", repeated_max)
    print("diffuse maximum candidate degree", diffuse_max)
    print("diffuse centre-entry matching", len(candidate_matching))
    print("candidate theorem lower bound", f"{candidate_lower:.6f}")
    print("maximum matched partner degree", partner_degree)
    print("maximum matched controller degree", controller_degree)
    print("maximum matched label degree", label_degree)
    print("full chronological resource matching", len(full_matching))
    print("resource theorem lower bound", f"{resource_lower:.6f}")
    print("outcome repeated_candidate_or_full_chronological_matching")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Check the exact fixed-centre Xi five-chain normal form on a finite instance."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any


Arc = tuple[int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def require_number(value: Any, label: str, minimum: float = 0.0) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value < minimum:
        raise ValueError(f"{label}: expected number >= {minimum}")
    return float(value)


def cycle_arcs(order: tuple[int, ...]) -> set[Arc]:
    return {
        (order[i], order[(i + 1) % len(order)])
        for i in range(len(order))
    }


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")

        n = require_int(payload.get("n"), "n", minimum=7)
        b = require_int(payload.get("block_size"), "block_size", minimum=7)
        if b > n:
            raise ValueError("block_size must not exceed n")

        raw_chain = payload.get("chain")
        if not isinstance(raw_chain, list) or len(raw_chain) != 5:
            raise ValueError("chain: expected five indices [r,p,c,s,t]")
        chain = tuple(require_int(x, f"chain[{i}]") for i, x in enumerate(raw_chain))
        if len(set(chain)) != 5 or any(x >= n for x in chain):
            raise ValueError("chain indices must be distinct and lie in [0,n)")
        r, p, c, s, t = chain

        weights = payload.get("weights")
        if not isinstance(weights, dict):
            raise ValueError("weights: expected object")

        a_in = require_number(weights.get("rank2_in", 0), "weights.rank2_in")
        a_out = require_number(weights.get("rank2_out", 0), "weights.rank2_out")
        beta_l = require_number(weights.get("rank3_left", 0), "weights.rank3_left")
        beta_m = require_number(weights.get("rank3_middle", 0), "weights.rank3_middle")
        beta_r = require_number(weights.get("rank3_right", 0), "weights.rank3_right")
        det_in = require_number(weights.get("rank4_deterministic_in", 0), "weights.rank4_deterministic_in")
        det_out = require_number(weights.get("rank4_deterministic_out", 0), "weights.rank4_deterministic_out")
        boundary = require_number(weights.get("rank4_boundary_default", 0), "weights.rank4_boundary_default")
        remote = require_number(weights.get("rank4_remote_default", 0), "weights.rank4_remote_default")

        removal_credit = require_number(payload.get("removal_credit"), "removal_credit", minimum=1e-12)
        residual_objective = require_number(payload.get("residual_objective", 0), "residual_objective")
        tau = require_number(payload.get("tau", 0.5), "tau")
        if not 0 < tau < 1:
            raise ValueError("tau must lie in (0,1)")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    chain_set = set(chain)
    outside = [x for x in range(n) if x not in chain_set]
    fixed_chain_arcs = {(r, p), (p, c), (c, s), (s, t)}

    def gamma_in(arc: Arc) -> float:
        if arc == (s, t):
            return det_in
        u, v = arc
        if (u == t and v in outside) or (v == r and u in outside):
            return boundary
        if u in outside and v in outside and u != v:
            return remote
        return 0.0

    def gamma_out(arc: Arc) -> float:
        if arc == (r, p):
            return det_out
        u, v = arc
        if (u == t and v in outside) or (v == r and u in outside):
            return boundary
        if u in outside and v in outside and u != v:
            return remote
        return 0.0

    boundary_mass = 0.0
    for u in outside:
        for arc in ((t, u), (u, r)):
            boundary_mass += gamma_in(arc) + gamma_out(arc)

    remote_mass = 0.0
    for u in outside:
        for v in outside:
            if u != v:
                remote_mass += gamma_in((u, v)) + gamma_out((u, v))

    deterministic_23 = a_in + a_out + beta_l + beta_m + beta_r
    deterministic_4 = det_in + det_out
    boundary_probability = 1.0 / (n - 5)
    remote_probability = (b - 6) / ((n - 5) * (n - 6))
    formula_rank4 = (
        deterministic_4
        + boundary_probability * boundary_mass
        + remote_probability * remote_mass
    )
    formula_centre = deterministic_23 + formula_rank4

    selected_block_count = 0
    total_cycles = 0
    rank4_total = 0.0
    boundary_hits = 0
    remote_hits = 0
    boundary_trials = 0
    remote_trials = 0

    boundary_arcs = {(t, u) for u in outside} | {(u, r) for u in outside}
    remote_arcs = {(u, v) for u in outside for v in outside if u != v}

    for extra in itertools.combinations(outside, b - 5):
        selected_block_count += 1
        block = set(chain) | set(extra)
        cycles_for_block = 0

        # Fix c as the canonical first vertex so each directed cycle is enumerated once.
        rest = sorted(block - {c})
        for perm in itertools.permutations(rest):
            order = (c,) + perm
            arcs = cycle_arcs(order)
            if not fixed_chain_arcs.issubset(arcs):
                continue
            cycles_for_block += 1
            total_cycles += 1

            rank4_cost = 0.0
            for arc in arcs:
                if p not in arc and c not in arc:
                    rank4_cost += gamma_in(arc)
                if c not in arc and s not in arc:
                    rank4_cost += gamma_out(arc)
            rank4_total += rank4_cost
            boundary_hits += len(arcs & boundary_arcs)
            remote_hits += len(arcs & remote_arcs)
            boundary_trials += len(boundary_arcs)
            remote_trials += len(remote_arcs)

        expected_cycles = 1
        for x in range(2, b - 4):
            expected_cycles *= x
        if cycles_for_block != expected_cycles:
            raise SystemExit(
                f"check failed: block {sorted(block)} has {cycles_for_block} cycles, "
                f"expected {(b - 5)}!={expected_cycles}"
            )

    if total_cycles == 0:
        raise SystemExit("check failed: no conditional cycles enumerated")

    enumerated_rank4 = rank4_total / total_cycles
    if abs(enumerated_rank4 - formula_rank4) > 1e-9:
        raise SystemExit(
            f"check failed: rank-four expectation {enumerated_rank4} != formula {formula_rank4}"
        )

    observed_boundary_probability = boundary_hits / boundary_trials
    observed_remote_probability = remote_hits / remote_trials
    if abs(observed_boundary_probability - boundary_probability) > 1e-9:
        raise SystemExit("check failed: boundary probability mismatch")
    if abs(observed_remote_probability - remote_probability) > 1e-9:
        raise SystemExit("check failed: remote probability mismatch")

    paid_objective = residual_objective + formula_centre / removal_credit
    deterministic_local = deterministic_23 + deterministic_4
    deterministic_bound = tau * removal_credit / 4.0
    boundary_threshold = (3 * tau / 8.0) * removal_credit * (n - 5)
    remote_threshold = (
        (3 * tau / 8.0)
        * removal_credit
        * (n - 5)
        * (n - 6)
        / (b - 6)
    )

    if paid_objective < 1:
        outcome = "paid_five_chain_completion"
    elif residual_objective > 1 - tau + 1e-12:
        outcome = "residual_source_or_offcentre_core"
    elif deterministic_local > deterministic_bound + 1e-12:
        outcome = "deterministic_local_credit_core"
    elif boundary_mass >= boundary_threshold - 1e-12:
        outcome = "boundary_rank4_partner_core"
    elif remote_mass >= remote_threshold - 1e-12:
        outcome = "remote_rank4_partner_core"
    else:
        raise SystemExit("check failed: failed paid criterion but no quantitative alternative")

    result = {
        "outcome": outcome,
        "n": n,
        "block_size": b,
        "chain": list(chain),
        "selected_block_count": selected_block_count,
        "conditional_cycle_count": total_cycles,
        "cycles_per_block": total_cycles // selected_block_count,
        "expected_cycles_per_block": expected_cycles,
        "boundary_arc_probability_formula": boundary_probability,
        "boundary_arc_probability_enumerated": observed_boundary_probability,
        "remote_arc_probability_formula": remote_probability,
        "remote_arc_probability_enumerated": observed_remote_probability,
        "deterministic_rank2_rank3_cost": deterministic_23,
        "deterministic_rank4_cost": deterministic_4,
        "boundary_partner_mass": boundary_mass,
        "remote_partner_mass": remote_mass,
        "rank4_expected_cost_formula": formula_rank4,
        "rank4_expected_cost_enumerated": enumerated_rank4,
        "centre_xi_expected_cost": formula_centre,
        "removal_credit": removal_credit,
        "residual_objective": residual_objective,
        "paid_objective": paid_objective,
        "tau": tau,
        "deterministic_local_bound": deterministic_bound,
        "boundary_mass_threshold": boundary_threshold,
        "remote_mass_threshold": remote_threshold,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

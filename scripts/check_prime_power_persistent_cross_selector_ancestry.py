#!/usr/bin/env python3
"""Check persistent-blocker, cross-signature and fixed-selector ancestry."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from typing import Any, Iterable

Edge = tuple[int, int]


class PersistentCrossError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise PersistentCrossError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def matchings(edges: Iterable[Edge], m: int) -> list[tuple[Edge, ...]]:
    edge_set = set(edges)
    out: list[tuple[Edge, ...]] = []
    for perm in itertools.permutations(range(m)):
        matching = tuple((i, perm[i]) for i in range(m))
        if all(e in edge_set for e in matching):
            out.append(matching)
    return out


def maximum_matching_size(edges: Iterable[Edge], m: int) -> int:
    edge_set = set(edges)
    best = 0

    def visit(row: int, used: set[int], size: int) -> None:
        nonlocal best
        if row == m:
            best = max(best, size)
            return
        visit(row + 1, used, size)
        for col in range(m):
            if col not in used and (row, col) in edge_set:
                used.add(col)
                visit(row + 1, used, size + 1)
                used.remove(col)

    visit(0, set(), 0)
    return best


def maximum_matchings(edges: Iterable[Edge], m: int) -> list[tuple[Edge, ...]]:
    edge_set = set(edges)
    nu = maximum_matching_size(edge_set, m)
    out: list[tuple[Edge, ...]] = []

    def visit(row: int, used: set[int], chosen: list[Edge]) -> None:
        if row == m:
            if len(chosen) == nu:
                out.append(tuple(chosen))
            return
        if len(chosen) + (m - row) < nu:
            return
        visit(row + 1, used, chosen)
        for col in range(m):
            if col not in used and (row, col) in edge_set:
                used.add(col)
                chosen.append((row, col))
                visit(row + 1, used, chosen)
                chosen.pop()
                used.remove(col)

    visit(0, set(), [])
    return out


def remove_vertices(edges: Iterable[Edge], row: int, col: int) -> set[Edge]:
    return {e for e in edges if e[0] != row and e[1] != col}


def maximum_allowed_audit() -> dict[str, int]:
    m = 3
    universe = [(i, j) for i in range(m) for j in range(m)]
    graph_count = 0
    edge_cases = 0
    allowed_cases = 0
    deficient_cases = 0
    max_matching_instances = 0
    partner_incidences = 0
    for mask in range(1 << len(universe)):
        edges = {universe[k] for k in range(len(universe)) if mask >> k & 1}
        if not edges:
            continue
        graph_count += 1
        nu = maximum_matching_size(edges, m)
        maxima = maximum_matchings(edges, m)
        require(maxima and all(len(M) == nu for M in maxima), "maximum family mismatch")
        max_matching_instances += len(maxima)
        for e in sorted(edges):
            edge_cases += 1
            u, v = e
            residual_nu = maximum_matching_size(remove_vertices(edges, u, v), m)
            is_allowed = any(e in M for M in maxima)
            require(is_allowed == (1 + residual_nu == nu), "CMR522 criterion failed")
            if is_allowed:
                allowed_cases += 1
            else:
                deficient_cases += 1
                require(residual_nu == nu - 2, "CMR523 deficiency not exact")
                for M in maxima:
                    through_u = [f for f in M if f[0] == u]
                    through_v = [f for f in M if f[1] == v]
                    require(len(through_u) == len(through_v) == 1, "endpoint not saturated")
                    require(through_u[0] != through_v[0], "partner edges not distinct")
                    require(e not in M, "forbidden edge used")
                    partner_incidences += 2
    return {
        "side_three_graphs": graph_count,
        "edge_cases": edge_cases,
        "maximum_allowed_cases": allowed_cases,
        "two_endpoint_deficiency_cases": deficient_cases,
        "maximum_matching_instances": max_matching_instances,
        "deficiency_partner_incidences": partner_incidences,
    }


def collinear(a: Edge, b: Edge, c: Edge) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def compatible_pair(a: Edge, b: Edge) -> bool:
    return a[0] != b[0] and a[1] != b[1]


def line_key(a: Edge, b: Edge) -> tuple[int, int, int]:
    A = b[1] - a[1]
    B = a[0] - b[0]
    C = -(A * a[0] + B * a[1])
    g = math.gcd(math.gcd(abs(A), abs(B)), abs(C))
    if g:
        A, B, C = A // g, B // g, C // g
    if A < 0 or (A == 0 and B < 0) or (A == 0 and B == 0 and C < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def derangements(n: int) -> list[tuple[int, ...]]:
    return [p for p in itertools.permutations(range(n)) if all(p[i] != i for i in range(n))]


def pair_bank_audit() -> dict[str, int]:
    m = 5
    n = m - 2
    ders = derangements(n)
    require(len(ders) == 2, "D_3 must equal two")
    central_count = 0
    pair_types = 0
    cylinder_states = 0
    injective_lines = 0
    disjoint_pairs = 0
    for u in range(m):
        for v in range(m):
            central_count += 1
            seen_lines: set[tuple[int, int, int]] = set()
            cylinders: dict[tuple[int, int], set[tuple[Edge, ...]]] = {}
            for x in range(m):
                if x == u:
                    continue
                for y in range(m):
                    if y == v:
                        continue
                    row_arm = (u, y)
                    col_arm = (x, v)
                    require(compatible_pair(row_arm, col_arm), "cross pair incompatible")
                    key = line_key(row_arm, col_arm)
                    require(key not in seen_lines, "pair-line map not injective")
                    seen_lines.add(key)
                    injective_lines += 1
                    pair_types += 1
                    rows = [r for r in range(m) if r not in {u, x}]
                    cols = [c for c in range(m) if c not in {y, v}]
                    states: set[tuple[Edge, ...]] = set()
                    for p in ders:
                        residual = tuple((rows[i], cols[p[i]]) for i in range(n))
                        state = tuple(sorted((row_arm, col_arm, *residual)))
                        require(len({r for r, _ in state}) == m, "cylinder row collision")
                        require(len({c for _, c in state}) == m, "cylinder column collision")
                        states.add(state)
                    require(len(states) == len(ders), "wrong cylinder size")
                    cylinders[(x, y)] = states
                    cylinder_states += len(states)
            types = sorted(cylinders)
            for i, a in enumerate(types):
                for b in types[i + 1 :]:
                    require(cylinders[a].isdisjoint(cylinders[b]), "pair cylinders intersect")
                    disjoint_pairs += 1
    return {
        "central_cells": central_count,
        "cross_pair_types": pair_types,
        "injective_pair_lines": injective_lines,
        "cylinder_state_occurrences": cylinder_states,
        "pairwise_disjoint_cylinder_checks": disjoint_pairs,
    }


def max_bipartite_matching_support(edges: set[tuple[int, int]], left: int, right: int) -> int:
    best = 0
    for k in range(1, min(left, right) + 1):
        for subset in itertools.combinations(edges, k):
            if len({a for a, _ in subset}) == k and len({b for _, b in subset}) == k:
                best = k
    return best


def partner_support_audit() -> dict[str, int]:
    left = right = 3
    universe = [(i, j) for i in range(left) for j in range(right)]
    profiles = 0
    two_arm = 0
    one_arm = 0
    support_edges = 0
    threshold = 2
    for mask in range(1, 1 << len(universe)):
        E = {universe[i] for i in range(len(universe)) if mask >> i & 1}
        profiles += 1
        support_edges += len(E)
        nu = max_bipartite_matching_support(E, left, right)
        if nu >= threshold:
            two_arm += 1
        else:
            degrees = Counter([("L", a) for a, _ in E] + [("R", b) for _, b in E])
            d = max(degrees.values())
            require(d >= math.ceil(len(E) / (threshold - 1)), "CMR530 star bound failed")
            one_arm += 1
    return {
        "partner_support_profiles": profiles,
        "partner_support_edges": support_edges,
        "two_arm_bank_profiles": two_arm,
        "one_arm_star_profiles": one_arm,
    }


def joint_runs(history: list[set[Edge]], F: set[Edge], selected: list[int]) -> int:
    selected_set = set(selected)
    runs = 0
    active = False
    for t, available in enumerate(history):
        all_absent = F.isdisjoint(available)
        if all_absent and t in selected_set and not active:
            runs += 1
            active = True
        elif not all_absent:
            active = False
    return runs


def reintroductions(history: list[set[Edge]], e: Edge) -> int:
    return sum(e not in history[i - 1] and e in history[i] for i in range(1, len(history)))


def temporal_audit() -> dict[str, int]:
    F = {(0, 0), (0, 1), (1, 0)}
    edges = sorted(F)
    T = 5
    histories = 0
    selected_subsets = 0
    recurrent_joint_runs = 0
    reintroduction_endpoints = 0
    for masks in itertools.product(range(1 << T), repeat=len(edges)):
        history: list[set[Edge]] = []
        for t in range(T):
            available = {edges[i] for i, mask in enumerate(masks) if mask >> t & 1}
            history.append(available)
        joint_absent = [t for t, A in enumerate(history) if F.isdisjoint(A)]
        histories += 1
        for r in range(1, len(joint_absent) + 1):
            for selected in itertools.combinations(joint_absent, r):
                selected_subsets += 1
                rho = joint_runs(history, F, list(selected))
                I = sum(reintroductions(history, e) for e in F)
                require(rho <= 1 + I, "CMR538 joint-run bound failed")
                if len(selected) >= 3:
                    persistent = any(
                        sum(1 for s in selected if a <= s <= b) >= 3
                        and all(F.isdisjoint(history[t]) for t in range(a, b + 1))
                        for a in range(T) for b in range(a, T)
                    )
                    if persistent:
                        recurrent_joint_runs += 1
                    elif I > 0:
                        reintroduction_endpoints += 1
                    else:
                        raise PersistentCrossError("temporal endpoint missing")
    return {
        "three_edge_availability_histories": histories,
        "selected_joint_absence_subsets": selected_subsets,
        "joint_persistent_endpoint_instances": recurrent_joint_runs,
        "joint_reintroduction_endpoint_instances": reintroduction_endpoints,
    }


def signature_stock_audit() -> dict[str, int]:
    p, h, t = 2, 3, 8
    sides = [8, 4, 2, 1]
    require(len(sides) == h + 1, "epoch count")
    pair_stock = sum(m * m * (m - 1) ** 2 for m in sides)
    trace_stock = sum(2 * m * m * (m - 1) for m in sides)
    refined_stock_bound = sum(2 * m**4 * (m - 1) ** 2 for m in sides)
    require(pair_stock <= (h + 1) * t * t * (t - 1) ** 2, "pair stock bound")
    require(trace_stock <= 2 * (h + 1) * t * t * (t - 1), "trace stock bound")
    require(refined_stock_bound <= 2 * (h + 1) * t**4 * (t - 1) ** 2, "refined bound")
    lam = 4
    return {
        "envelope_epochs": len(sides),
        "exact_pair_signature_stock": pair_stock,
        "exact_trace_signature_stock": trace_stock,
        "exact_refined_trace_stock_bound": refined_stock_bound,
        "finite_pair_episode_bound_lambda4": (lam - 1) * pair_stock,
        "finite_trace_episode_bound_lambda4": (lam - 1) * trace_stock,
        "finite_refined_trace_episode_bound_lambda4": (lam - 1) * refined_stock_bound,
    }


def selector_arithmetic_audit() -> dict[str, int]:
    n, q = 5, 4
    p2 = n * (n - 1)
    p3 = p2 * (n - 2)
    H = math.ceil(q * (n - 1) / 4)
    failed_profiles = 0
    unavailable_profiles = 0
    collateral_profiles = 0
    rank_zero_profiles = 0
    rank_one_profiles = 0
    for V0 in range(p3 + 1):
        for V1 in range(p2 + 1):
            S_num = V0 / p3 + V1 / p2
            for B in range(n * n + 1):
                lhs = (30 / 11) * S_num + 2 / q + B / (q * (n - 1))
                if lhs + 1e-12 < 1:
                    continue
                failed_profiles += 1
                collateral = S_num + 1e-12 >= 11 / 120
                unavailable = B >= H
                require(collateral or unavailable, "CMR546 polarization failed")
                if unavailable:
                    unavailable_profiles += 1
                else:
                    collateral_profiles += 1
                    rz = V0 + 1e-12 >= (11 / 240) * p3
                    ro = V1 + 1e-12 >= (11 / 240) * p2
                    require(rz or ro, "CMR548 rank split failed")
                    if rz:
                        rank_zero_profiles += 1
                    else:
                        rank_one_profiles += 1
    lam = 3
    N0 = p3 * p3 // 6
    N1 = p2 * p2
    require(N0 == math.comb(n, 3) ** 2 * math.factorial(3), "rank-zero stock")
    require(N1 == 2 * math.comb(n, 2) ** 2 * math.factorial(2), "rank-one stock")
    return {
        "selector_failed_integer_profiles": failed_profiles,
        "selector_unavailable_profiles": unavailable_profiles,
        "selector_collateral_profiles": collateral_profiles,
        "selector_rank_zero_profiles": rank_zero_profiles,
        "selector_rank_one_profiles": rank_one_profiles,
        "unavailable_threshold_H": H,
        "finite_unavailable_history_bound_lambda3": math.floor((lam - 1) * n * n / H),
        "rank_zero_atom_stock": N0,
        "rank_one_atom_stock": N1,
        "finite_rank_zero_history_bound_lambda3_floor": math.floor((40 / 11) * (lam - 1) * p3),
        "finite_rank_one_history_bound_lambda3_floor": math.floor((240 / 11) * (lam - 1) * p2),
    }


def line_separation_audit() -> dict[str, int]:
    m = 7
    paid_pairs = 0
    rank_one_atoms = 0
    for z1 in itertools.product(range(m), repeat=2):
        for z2 in itertools.product(range(m), repeat=2):
            if z1 >= z2 or not compatible_pair(z1, z2):
                continue
            paid_line = line_key(z1, z2)
            paid_pairs += 1
            residual = [
                e for e in itertools.product(range(m), repeat=2)
                if e[0] not in {z1[0], z2[0]} and e[1] not in {z1[1], z2[1]}
                and line_key(z1, e) != paid_line
            ]
            for z in (z1, z2):
                for a, b in itertools.combinations(residual, 2):
                    if compatible_pair(a, b) and collinear(z, a, b):
                        require(line_key(z, a) != paid_line, "rank-one line equals paid line")
                        rank_one_atoms += 1
    return {
        "side_seven_compatible_paid_pairs": paid_pairs,
        "rank_one_separated_line_atoms": rank_one_atoms,
    }


CONTRACT = {
    "schema": "prime-power-persistent-cross-selector-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(522, 552)],
    "operations": [
        "persistent-blocker-trace-contact",
        "persistent-blocker-maximum-absorption",
        "persistent-blocker-two-endpoint-deficiency",
        "persistent-cross-pair-cylinder",
        "persistent-cross-pair-recurrence",
        "persistent-cross-two-arm-bank",
        "persistent-cross-one-arm-line-star",
        "persistent-cross-weighted-selector",
        "persistent-cross-trace-token-signature",
        "persistent-cross-joint-absence-payment",
        "cross-envelope-epoch-assignment",
        "cross-signature-finite-stock",
        "cross-signature-joint-persistence",
        "refined-trace-fixed-selector",
        "fixed-selector-unavailable-stock",
        "fixed-selector-collateral-polarization",
        "fixed-selector-rank-zero-target-recurrence",
        "fixed-selector-rank-one-secant-recurrence",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "35bfc31201b5fffb46b37e9c36ffd4c1e9e01c6d1ccdb2b592818b9dc8bdcc80"


def validate_report(report: dict[str, Any]) -> None:
    require(report["contract_sha256"] == EXPECTED_CONTRACT_SHA256, "contract seal")
    require(report["census"]["maximum_allowed_cases"] > 0, "missing allowed cases")
    require(report["census"]["two_endpoint_deficiency_cases"] > 0, "missing deficiency")
    require(report["census"]["two_arm_bank_profiles"] > 0, "missing pair bank")
    require(report["census"]["one_arm_star_profiles"] > 0, "missing line star")
    require(report["census"]["joint_persistent_endpoint_instances"] > 0, "missing persistence")
    require(report["census"]["joint_reintroduction_endpoint_instances"] > 0, "missing reintroduction")
    require(report["census"]["selector_unavailable_profiles"] > 0, "missing unavailable selector")
    require(report["census"]["selector_collateral_profiles"] > 0, "missing collateral selector")
    require(report["census"]["rank_one_separated_line_atoms"] > 0, "missing rank-one geometry")
    require(report["all_n_proved_by_checker"] == 0, "honesty flag")


def mutation_audit(report: dict[str, Any]) -> int:
    mutations = [
        lambda x: x.update(contract_sha256="0" * 64),
        lambda x: x["census"].update(maximum_allowed_cases=0),
        lambda x: x["census"].update(two_endpoint_deficiency_cases=0),
        lambda x: x["census"].update(two_arm_bank_profiles=0),
        lambda x: x["census"].update(one_arm_star_profiles=0),
        lambda x: x["census"].update(joint_persistent_endpoint_instances=0),
        lambda x: x["census"].update(joint_reintroduction_endpoint_instances=0),
        lambda x: x["census"].update(selector_unavailable_profiles=0),
        lambda x: x["census"].update(selector_collateral_profiles=0),
        lambda x: x["census"].update(rank_one_separated_line_atoms=0),
        lambda x: x.update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutator in mutations:
        bad = copy.deepcopy(report)
        mutator(bad)
        try:
            validate_report(bad)
        except PersistentCrossError:
            rejected += 1
    require(rejected == len(mutations), "corruption accepted")
    return rejected


def main() -> None:
    contract_sha256 = digest(CONTRACT)
    require(contract_sha256 == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    census: dict[str, int] = {}
    for audit in (
        maximum_allowed_audit,
        pair_bank_audit,
        partner_support_audit,
        temporal_audit,
        signature_stock_audit,
        selector_arithmetic_audit,
        line_separation_audit,
    ):
        census.update(audit())
    report: dict[str, Any] = {
        "checker": "prime-power-persistent-cross-selector-ancestry",
        "contract_sha256": contract_sha256,
        "census": census,
        "persistent_blocker_absorption_deficiency_ancestry_proved": 1,
        "persistent_cross_pair_bank_ancestry_proved": 1,
        "cross_signature_ancestry_exact": 1,
        "refined_trace_fixed_selector_exact": 1,
        "fixed_selector_obstruction_stock_exact": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_returned_edge_operations_proved": 0,
        "all_envelope_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    validate_report(report)
    report["census"]["rejected_corruptions"] = mutation_audit(report)
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()

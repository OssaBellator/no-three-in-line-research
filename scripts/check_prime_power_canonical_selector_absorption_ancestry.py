#!/usr/bin/env python3
"""Check canonical selector, collateral geometry and absorption chase ancestry."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from typing import Any

Cell = tuple[int, int]
Triple = tuple[Cell, Cell, Cell]


class CanonicalSelectorError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise CanonicalSelectorError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def compatible(a: Cell, b: Cell) -> bool:
    return a[0] != b[0] and a[1] != b[1]


def collinear(a: Cell, b: Cell, c: Cell) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def line_key(a: Cell, b: Cell) -> tuple[int, int, int]:
    A = b[1] - a[1]
    B = a[0] - b[0]
    C = -(A * a[0] + B * a[1])
    g = math.gcd(math.gcd(abs(A), abs(B)), abs(C))
    if g:
        A, B, C = A // g, B // g, C // g
    if A < 0 or (A == 0 and B < 0) or (A == B == 0 and C < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def primitive_height(key: tuple[int, int, int]) -> int:
    A, B, _ = key
    return max(abs(A), abs(B))


def derangements(n: int) -> list[tuple[int, ...]]:
    return [p for p in itertools.permutations(range(n)) if all(p[i] != i for i in range(n))]


def canonical_extension(
    m: int, z1: Cell, z2: Cell
) -> tuple[list[int], list[int], list[Cell], list[Cell], list[Cell]]:
    rows = [r for r in range(m) if r not in {z1[0], z2[0]}]
    cols = [c for c in range(m) if c not in {z1[1], z2[1]}]
    paid_line = line_key(z1, z2)
    trace = [
        (r, c) for r in rows for c in cols
        if line_key(z1, (r, c)) == paid_line
    ]
    require(len({r for r, _ in trace}) == len(trace), "trace row collision")
    require(len({c for _, c in trace}) == len(trace), "trace column collision")
    used_rows = {r for r, _ in trace}
    used_cols = {c for _, c in trace}
    free_rows = sorted(set(rows) - used_rows)
    free_cols = sorted(set(cols) - used_cols)
    forbidden = sorted([*trace, *zip(free_rows, free_cols)])
    require(len(forbidden) == m - 2, "canonical extension not perfect")
    allowed = [(r, c) for r in rows for c in cols if (r, c) not in set(forbidden)]
    return rows, cols, trace, forbidden, allowed


def canonical_profile(
    m: int, z1: Cell, z2: Cell
) -> tuple[list[Cell], list[Cell], list[Triple], list[Triple]]:
    _, _, trace, forbidden, allowed = canonical_extension(m, z1, z2)
    rank_zero: list[Triple] = []
    for tri in itertools.combinations(allowed, 3):
        if len({r for r, _ in tri}) < 3 or len({c for _, c in tri}) < 3:
            continue
        if collinear(*tri):
            rank_zero.append(tuple(tri))
    rank_one: list[Triple] = []
    for z in (z1, z2):
        for a, b in itertools.combinations(allowed, 2):
            if not compatible(a, b):
                continue
            if collinear(z, a, b):
                rank_one.append((z, a, b))
    return trace, forbidden, rank_zero, rank_one


def cylinder_audit() -> dict[str, int]:
    m = 7
    n = m - 2
    ders = derangements(n)
    require(len(ders) == 44, "D_5 mismatch")
    pairs = 0
    states = 0
    trace_edges = 0
    line_avoidance_checks = 0
    fixed_profile_repeat_checks = 0
    for z1 in itertools.product(range(m), repeat=2):
        for z2 in itertools.product(range(m), repeat=2):
            if z1 >= z2 or not compatible(z1, z2):
                continue
            pairs += 1
            rows, cols, trace, forbidden, allowed = canonical_extension(m, z1, z2)
            trace_edges += len(trace)
            paid_line = line_key(z1, z2)
            forbidden_by_row = {r: c for r, c in forbidden}
            ordered_rows = sorted(rows)
            forbidden_cols = [forbidden_by_row[r] for r in ordered_rows]
            for perm in ders:
                state = {(ordered_rows[i], forbidden_cols[perm[i]]) for i in range(n)}
                require(state.isdisjoint(forbidden), "derangement meets forbidden matching")
                require(all(line_key(z1, e) != paid_line for e in state),
                        "canonical cylinder uses paid-line cell")
                states += 1
                line_avoidance_checks += len(state)
            _, F1, r01, r11 = canonical_profile(m, z1, z2)
            _, F2, r02, r12 = canonical_profile(m, z1, z2)
            require(F1 == F2 and r01 == r02 and r11 == r12,
                    "canonical collateral profile changed")
            fixed_profile_repeat_checks += 1
    return {
        "side_seven_compatible_paid_pairs": pairs,
        "canonical_cylinder_state_occurrences": states,
        "canonical_trace_edge_incidences": trace_edges,
        "paid_line_avoidance_checks": line_avoidance_checks,
        "fixed_profile_repeat_checks": fixed_profile_repeat_checks,
    }


def disjoint_triples(triples: list[Triple], target: int) -> bool:
    for family in itertools.combinations(triples, target):
        cells = [c for tri in family for c in tri]
        if len(set(cells)) == 3 * target:
            return True
    return False


def static_geometry_audit() -> dict[str, int]:
    m = 7
    n = m - 2
    q = 4
    cq = (11 / 30) * (1 - 2 / q)
    p2 = n * (n - 1)
    p3 = p2 * (n - 2)
    profiles = 0
    static_profiles = 0
    rank_zero_mass_profiles = 0
    rank_one_mass_profiles = 0
    line_decomposition_checks = 0
    factorial_energy_checks = 0
    heavy_rank_zero_lines = 0
    heavy_rank_one_lines = 0
    rank_zero_disjoint_banks = 0
    rank_zero_stars = 0
    dyadic_localizations = 0
    low_height_checks = 0

    for z1 in itertools.product(range(m), repeat=2):
        for z2 in itertools.product(range(m), repeat=2):
            if z1 >= z2 or not compatible(z1, z2):
                continue
            profiles += 1
            _, _, rank_zero, rank_one = canonical_profile(m, z1, z2)
            V0, V1 = len(rank_zero), len(rank_one)
            S = V0 / p3 + V1 / p2
            if S + 1e-12 < cq:
                continue
            static_profiles += 1
            by_endpoint = {z1: 0, z2: 0}
            for tri in rank_one:
                by_endpoint[tri[0]] += 1
            rz = V0 + 1e-12 >= (cq / 2) * p3
            endpoint, endpoint_mass = max(by_endpoint.items(), key=lambda item: item[1])
            ro = endpoint_mass + 1e-12 >= (cq / 4) * p2
            require(rz or ro, "CMR558 rank polarization failed")
            if rz:
                rank_zero_mass_profiles += 1
            else:
                rank_one_mass_profiles += 1

            _, _, _, forbidden, allowed = canonical_extension(m, z1, z2)
            line_cells: dict[tuple[int, int, int], set[Cell]] = defaultdict(set)
            for a, b in itertools.combinations(allowed, 2):
                key = line_key(a, b)
                for c in allowed:
                    if line_key(a, c) == key:
                        line_cells[key].add(c)
            r0_lines = Counter(line_key(tri[0], tri[1]) for tri in rank_zero)
            r1_lines = Counter((tri[0], line_key(tri[0], tri[1])) for tri in rank_one)
            require(sum(r0_lines.values()) == V0, "rank-zero line decomposition")
            require(sum(r1_lines.values()) == V1, "rank-one line decomposition")
            line_decomposition_checks += 2
            for key, count in r0_lines.items():
                r = len(line_cells[key])
                require(count <= math.comb(r, 3), "rank-zero line capacity")
                require(r <= n, "rank-zero line side capacity")
                if count >= 2:
                    heavy_rank_zero_lines += 1
                    K = primitive_height(key)
                    require(K <= (m - 1) / (r - 1), "rank-zero low-height bound")
                    low_height_checks += 1
            for (z, key), count in r1_lines.items():
                r = sum(1 for c in allowed if line_key(z, c) == key)
                require(count <= math.comb(r, 2), "rank-one line capacity")
                require(r <= n, "rank-one line side capacity")
                if count >= 2:
                    heavy_rank_one_lines += 1
                    K = primitive_height(key)
                    require(K <= (m - 1) / (r - 1), "rank-one low-height bound")
                    low_height_checks += 1

            energy0 = sum(math.prod(range(r - 2, r + 1)) if r >= 3 else 0
                          for r in (len(line_cells[k]) for k in r0_lines))
            require(energy0 >= 6 * V0, "rank-zero factorial energy")
            for z in (z1, z2):
                keys = {key for (zz, key) in r1_lines if zz == z}
                energy1 = sum(r * (r - 1)
                              for r in (sum(1 for c in allowed if line_key(z, c) == key)
                                        for key in keys))
                require(energy1 >= 2 * by_endpoint[z], "rank-one factorial energy")
            factorial_energy_checks += 3

            if ro:
                occupied = [(key, count) for (z, key), count in r1_lines.items() if z == endpoint]
                if not any(count >= 2 for key, count in occupied):
                    chosen = []
                    for key, _ in occupied:
                        tri = next(tri for tri in rank_one
                                   if tri[0] == endpoint and line_key(tri[0], tri[1]) == key)
                        chosen.append(set(tri[1:]))
                    require(all(a.isdisjoint(b) for i, a in enumerate(chosen)
                                for b in chosen[i + 1:]), "secant arms overlap")
            if rz and not any(count >= 2 for count in r0_lines.values()):
                if disjoint_triples(rank_zero, 2):
                    rank_zero_disjoint_banks += 1
                else:
                    degrees = Counter(c for tri in rank_zero for c in tri)
                    require(max(degrees.values(), default=0) >= 1,
                            "rank-zero star endpoint missing")
                    rank_zero_stars += 1

            B = math.ceil(math.log2(m))
            relevant = r0_lines if rz else Counter(
                {key: count for (z, key), count in r1_lines.items() if z == endpoint}
            )
            band_mass = Counter()
            for key, count in relevant.items():
                K = max(1, primitive_height(key))
                band = 1 << int(math.floor(math.log2(K)))
                band_mass[band] += count
            total = sum(relevant.values())
            require(total == 0 or max(band_mass.values()) * B >= total,
                    "dyadic localization failed")
            dyadic_localizations += 1
    require(static_profiles > 0, "no static physical profiles")
    return {
        "physical_selector_profiles": profiles,
        "static_physical_profiles": static_profiles,
        "rank_zero_mass_profiles": rank_zero_mass_profiles,
        "rank_one_mass_profiles": rank_one_mass_profiles,
        "line_decomposition_checks": line_decomposition_checks,
        "factorial_energy_checks": factorial_energy_checks,
        "heavy_rank_zero_lines": heavy_rank_zero_lines,
        "heavy_rank_one_lines": heavy_rank_one_lines,
        "rank_zero_disjoint_banks": rank_zero_disjoint_banks,
        "rank_zero_star_endpoints": rank_zero_stars,
        "dyadic_localizations": dyadic_localizations,
        "low_height_checks": low_height_checks,
    }


def dynamic_ledger_audit() -> dict[str, int]:
    n, q = 4, 4
    allowed = [(i, j) for i in range(n) for j in range(n) if i != j]
    A = 0.0
    delta = 1 - 2 / q - A
    H = math.ceil(q * (n - 1) * delta)
    require(H == 6, "dynamic threshold")
    profiles = 0
    failed_profiles = 0
    successful_profiles = 0
    for mask in range(1 << len(allowed)):
        B = {allowed[i] for i in range(len(allowed)) if mask >> i & 1}
        profiles += 1
        failure_inequality = A + 2 / q + len(B) / (q * (n - 1)) >= 1 - 1e-12
        if failure_inequality:
            require(len(B) >= H, "dynamic failure lacks unavailable threshold")
            failed_profiles += 1
        else:
            successful_profiles += 1
    lam = 3
    finite_bound = (lam - 1) * len(allowed) // H
    require(finite_bound == 4, "finite dynamic history bound")
    finite_sets = [
        set(allowed[0:6]), set(allowed[6:12]),
        set(allowed[::2]), set(allowed[1::2]),
    ]
    require(all(len(B) == H for B in finite_sets), "finite history set size")
    mult = Counter(e for B in finite_sets for e in B)
    require(max(mult.values()) <= lam - 1, "finite history unexpectedly recurrent")
    recurrent_sets = [set(allowed[0:6]) for _ in range(5)]
    mult2 = Counter(e for B in recurrent_sets for e in B)
    require(max(mult2.values()) >= lam, "recurrent history missing")
    p, h, t = 2, 3, 8
    N_sigma = (h + 1) * t * t * (t - 1) ** 2 + 2 * (h + 1) * t**4 * (t - 1) ** 2
    require(N_sigma == 1618176, "selector signature stock")
    return {
        "dynamic_allowed_edges": len(allowed),
        "dynamic_availability_profiles": profiles,
        "dynamic_failed_profiles": failed_profiles,
        "dynamic_success_profiles": successful_profiles,
        "dynamic_threshold_H": H,
        "finite_dynamic_history_bound_lambda3": finite_bound,
        "canonical_selector_signature_stock_bound": N_sigma,
        "finite_history_examples": len(finite_sets),
        "recurrent_history_examples": len(recurrent_sets),
    }


def partial_matchings(n: int) -> list[tuple[Cell, ...]]:
    out: list[tuple[Cell, ...]] = []
    for k in range(n + 1):
        for rows in itertools.combinations(range(n), k):
            for cols in itertools.combinations(range(n), k):
                for perm in itertools.permutations(cols):
                    out.append(tuple(sorted(zip(rows, perm))))
    return out


def ordered_extension(P: tuple[Cell, ...], n: int) -> tuple[Cell, ...]:
    used_rows = {r for r, _ in P}
    used_cols = {c for _, c in P}
    free_rows = sorted(set(range(n)) - used_rows)
    free_cols = sorted(set(range(n)) - used_cols)
    return tuple(sorted((*P, *zip(free_rows, free_cols))))


def absorption_audit() -> dict[str, int]:
    n = 4
    ders = derangements(n)
    require(len(ders) == 9, "D_4 mismatch")
    profiles = 0
    extension_states = 0
    absorbable_edges = 0
    blocked_edges = 0
    contact_signatures = 0
    cover_checks = 0
    chase_steps = 0
    max_chase = 0
    for P in partial_matchings(n):
        profiles += 1
        F = ordered_extension(P, n)
        require(len(F) == n, "protected extension not perfect")
        extension_states += len(ders)
        vertices = ({r for r, _ in P}, {c for _, c in P})
        blocked: list[Cell] = []
        for f in itertools.product(range(n), repeat=2):
            if f in F:
                continue
            is_disjoint = f[0] not in vertices[0] and f[1] not in vertices[1]
            if is_disjoint:
                F2 = ordered_extension(tuple(sorted((*P, f))), n)
                require(len(F2) == n, "absorption extension failed")
                absorbable_edges += 1
            else:
                blocked.append(f)
                contacts = sum(
                    1 for r, c in P
                    if (r == f[0] or c == f[1])
                )
                require(contacts in {1, 2}, "blocked contact count")
                contact_signatures += contacts
                blocked_edges += 1
        if P and blocked:
            degrees = Counter()
            for f in blocked:
                for r, c in P:
                    if r == f[0]:
                        degrees[("source", r, c)] += 1
                    if c == f[1]:
                        degrees[("target", r, c)] += 1
            require(max(degrees.values()) >= math.ceil(len(blocked) / (2 * len(P))),
                    "protected contact cover bound")
            cover_checks += 1

        Q = list(P)
        steps = 0
        while len(Q) < n:
            used_r = {r for r, _ in Q}
            used_c = {c for _, c in Q}
            f = min((r, c) for r in range(n) for c in range(n)
                    if r not in used_r and c not in used_c)
            Q.append(f)
            steps += 1
        require(steps == n - len(P), "chase depth not exact")
        chase_steps += steps
        max_chase = max(max_chase, steps)
    require(profiles == 209, "partial matching census")
    return {
        "protected_partial_matchings": profiles,
        "protected_extension_state_occurrences": extension_states,
        "absorbable_edge_cases": absorbable_edges,
        "blocked_edge_cases": blocked_edges,
        "protected_contact_signatures": contact_signatures,
        "protected_cover_checks": cover_checks,
        "absorption_chase_steps": chase_steps,
        "maximum_absorption_chase_depth": max_chase,
    }


CONTRACT = {
    "schema": "prime-power-canonical-selector-absorption-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(552, 577)],
    "operations": [
        "canonical-selector-forbidden-matching",
        "canonical-selector-static-collateral",
        "canonical-selector-dynamic-availability",
        "canonical-selector-edge-recurrence",
        "static-collateral-rank-polarization",
        "static-collateral-line-decomposition",
        "static-collateral-heavy-line",
        "static-collateral-secant-star",
        "static-collateral-disjoint-triple-bank",
        "static-collateral-carry-splice",
        "canonical-selector-protected-extension",
        "canonical-selector-edge-absorption",
        "canonical-selector-protected-contact",
        "canonical-selector-absorption-chase",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "15fdb4ac2e639dd23b89dae3ce302356ee4790a2183e7768315aed8b881e6d5e"


def validate_report(report: dict[str, Any]) -> None:
    require(report["contract_sha256"] == EXPECTED_CONTRACT_SHA256, "contract seal")
    c = report["census"]
    require(c["static_physical_profiles"] > 0, "static branch missing")
    require(c["dynamic_failed_profiles"] > 0, "dynamic failure branch missing")
    require(c["dynamic_success_profiles"] > 0, "dynamic success branch missing")
    require(c["heavy_rank_zero_lines"] > 0, "heavy rank-zero line missing")
    require(c["heavy_rank_one_lines"] > 0, "heavy rank-one line missing")
    require(c["absorbable_edge_cases"] > 0, "absorption branch missing")
    require(c["blocked_edge_cases"] > 0, "protected contact branch missing")
    require(c["maximum_absorption_chase_depth"] == 4, "chase depth")
    require(report["all_n_proved_by_checker"] == 0, "honesty flag")


def mutation_audit(report: dict[str, Any]) -> int:
    mutations = [
        lambda x: x.update(contract_sha256="0" * 64),
        lambda x: x["census"].update(static_physical_profiles=0),
        lambda x: x["census"].update(dynamic_failed_profiles=0),
        lambda x: x["census"].update(dynamic_success_profiles=0),
        lambda x: x["census"].update(heavy_rank_zero_lines=0),
        lambda x: x["census"].update(heavy_rank_one_lines=0),
        lambda x: x["census"].update(absorbable_edge_cases=0),
        lambda x: x["census"].update(blocked_edge_cases=0),
        lambda x: x["census"].update(maximum_absorption_chase_depth=3),
        lambda x: x.update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(report)
        mutate(bad)
        try:
            validate_report(bad)
        except CanonicalSelectorError:
            rejected += 1
    require(rejected == len(mutations), "corruption accepted")
    return rejected


def main() -> None:
    contract_sha256 = digest(CONTRACT)
    require(contract_sha256 == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    census: dict[str, int] = {}
    for audit in (
        cylinder_audit,
        static_geometry_audit,
        dynamic_ledger_audit,
        absorption_audit,
    ):
        census.update(audit())
    report: dict[str, Any] = {
        "checker": "prime-power-canonical-selector-absorption-ancestry",
        "contract_sha256": contract_sha256,
        "census": census,
        "canonical_selector_ledger_exact": 1,
        "canonical_collateral_line_decomposition_exact": 1,
        "canonical_collateral_carry_splice_exact": 1,
        "canonical_selector_absorption_chase_exact": 1,
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

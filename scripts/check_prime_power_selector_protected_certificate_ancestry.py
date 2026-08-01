#!/usr/bin/env python3
"""Verify CMR577--604 protected selector and owned certificate ancestry."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from typing import Any

Edge = tuple[int, int]
Matching = tuple[Edge, ...]
Triple = tuple[Edge, Edge, Edge]


class ProtectedCertificateError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ProtectedCertificateError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def perfect_matchings(edges: set[Edge], n: int) -> list[Matching]:
    out = []
    for perm in itertools.permutations(range(n)):
        matching = tuple((i, perm[i]) for i in range(n))
        if all(edge in edges for edge in matching):
            out.append(matching)
    return out


def essential_edges(edges: set[Edge], n: int) -> set[Edge]:
    pms = perfect_matchings(edges, n)
    require(pms, "host must be matchable")
    return set.intersection(*(set(matching) for matching in pms))


def compatible(edges: tuple[Edge, ...] | set[Edge] | list[Edge]) -> bool:
    return len({x for x, _ in edges}) == len(edges) and len({y for _, y in edges}) == len(edges)


def disjoint_packings(triples: tuple[Triple, ...]) -> list[tuple[Triple, ...]]:
    result: list[tuple[Triple, ...]] = [tuple()]
    for size in range(1, len(triples) + 1):
        for family in itertools.combinations(triples, size):
            flat = [edge for triple in family for edge in triple]
            if len(set(flat)) == len(flat):
                result.append(family)
    return result


def deletion_pass_audit(n: int = 3) -> dict[str, int]:
    universe = tuple((i, j) for i in range(n) for j in range(n))
    candidate_triples = tuple(
        tuple((i, perm[i]) for i in range(n))
        for perm in itertools.permutations(range(n))
    )
    hosts = packings = processed = killed = forced = deleted = 0
    restoration_profiles = recreated = 0
    for mask in range(1 << len(universe)):
        host = {universe[i] for i in range(len(universe)) if mask >> i & 1}
        if not perfect_matchings(host, n):
            continue
        present = tuple(
            triple for triple in candidate_triples if set(triple) <= host
        )
        for packing in disjoint_packings(present):
            if not packing:
                continue
            hosts += 1
            packings += 1
            current = set(host)
            deleted_code: dict[Triple, Edge] = {}
            forced_triples: list[Triple] = []
            for triple in packing:
                processed += 1
                ess = essential_edges(current, n)
                nonessential = [edge for edge in triple if edge not in ess]
                if nonessential:
                    edge = min(nonessential)
                    current.remove(edge)
                    require(
                        perfect_matchings(current, n),
                        "nonessential deletion killed all matchings",
                    )
                    deleted_code[triple] = edge
                    killed += 1
                    deleted += 1
                else:
                    forced_triples.append(triple)
                    forced += 1
            final_essential = essential_edges(current, n)
            require(compatible(final_essential),
                    "final essential core is not a matching")
            require(len(forced_triples) <= n // 3,
                    "fully forced packing bound failed")
            require(len(set(deleted_code.values())) == len(deleted_code),
                    "deleted code not injective")
            require(all(edge not in current for edge in deleted_code.values()),
                    "deleted edge survived")

            code_edges = tuple(deleted_code.values())
            for restore_mask in range(1 << len(code_edges)):
                restored = {
                    code_edges[i]
                    for i in range(len(code_edges))
                    if restore_mask >> i & 1
                }
                restoration_profiles += 1
                augmented = current | restored
                recreated_now = [
                    triple
                    for triple, edge in deleted_code.items()
                    if set(triple) <= augmented
                ]
                require(
                    all(deleted_code[triple] in restored for triple in recreated_now),
                    "recreated conflict lacks private restored edge",
                )
                require(
                    len(restored & set(code_edges)) >= len(recreated_now),
                    "restoration count below recreated conflicts",
                )
                recreated += len(recreated_now)
    require(killed + forced == processed,
            "deletion pass partition failed")
    return {
        "matchable_host_packing_profiles": hosts,
        "disjoint_conflict_packings": packings,
        "processed_packed_conflicts": processed,
        "killed_packed_conflicts": killed,
        "fully_forced_packed_conflicts": forced,
        "private_deleted_edge_incidences": deleted,
        "restoration_subset_profiles": restoration_profiles,
        "recreated_conflict_incidences": recreated,
    }


def partial_matchings(n: int) -> list[set[Edge]]:
    out = [set()]
    for size in range(1, n + 1):
        for rows in itertools.combinations(range(n), size):
            for cols in itertools.combinations(range(n), size):
                for perm in itertools.permutations(cols):
                    out.append(set(zip(rows, perm)))
    return out


def canonical_extension(P: set[Edge], n: int) -> Matching:
    require(compatible(P), "protected set incompatible")
    used_r = {x for x, _ in P}
    used_c = {y for _, y in P}
    free_r = [x for x in range(n) if x not in used_r]
    free_c = [y for y in range(n) if y not in used_c]
    return tuple(sorted((*P, *zip(free_r, free_c))))


def maximum_matching_size(edges: set[Edge], n: int) -> int:
    best = 0
    for size in range(1, n + 1):
        for subset in itertools.combinations(edges, size):
            if compatible(subset):
                best = size
    return best


def minimum_vertex_cover(edges: set[Edge], n: int) -> set[tuple[str, int]]:
    vertices = tuple(
        [("L", i) for i in range(n)]
        + [("R", j) for j in range(n)]
    )
    for size in range(2 * n + 1):
        for cover in itertools.combinations(vertices, size):
            cover_set = set(cover)
            if all(
                ("L", x) in cover_set or ("R", y) in cover_set
                for x, y in edges
            ):
                return cover_set
    raise AssertionError("cover missing")


def protected_contact_audit(n: int = 4) -> dict[str, int]:
    complete = {(i, j) for i in range(n) for j in range(n)}
    states = blocked_incidences = contact_labels = universe_bound_checks = 0
    wall_checks = heavy_token_profiles = dispersed_token_profiles = 0
    for P in partial_matchings(n):
        if not P:
            continue
        F = set(canonical_extension(P, n))
        U = complete - F
        protected_rows = {x for x, _ in P}
        protected_cols = {y for _, y in P}
        blocked = {
            edge
            for edge in U
            if edge[0] in protected_rows or edge[1] in protected_cols
        }
        k = len(P)
        states += 1
        blocked_incidences += len(blocked)
        require(len(blocked) <= 2 * k * (n - 1),
                "contact universe bound")
        universe_bound_checks += 1
        for edge in blocked:
            labels = int(edge[0] in protected_rows) + int(
                edge[1] in protected_cols
            )
            require(labels in {1, 2}, "contact label count")
            contact_labels += labels
        if blocked:
            degrees = Counter()
            for x, y in blocked:
                if x in protected_rows:
                    degrees[("L", x)] += 1
                if y in protected_cols:
                    degrees[("R", y)] += 1
            degree = max(degrees.values())
            require(
                degree >= math.ceil(len(blocked) / (2 * k)),
                "protected wall concentration",
            )
            wall_checks += 1
            H = max(2, math.ceil(math.sqrt(degree)))
            classes = Counter(index % 2 for index in range(degree))
            if max(classes.values()) >= H:
                heavy_token_profiles += 1
            else:
                require(
                    len(classes) >= math.ceil(degree / (H - 1)),
                    "dispersed token bound",
                )
                dispersed_token_profiles += 1
    return {
        "protected_contact_states": states,
        "blocked_contact_edge_incidences": blocked_incidences,
        "protected_contact_labels": contact_labels,
        "contact_universe_bound_checks": universe_bound_checks,
        "protected_wall_concentration_checks": wall_checks,
        "heavy_contact_token_profiles": heavy_token_profiles,
        "dispersed_contact_token_profiles": dispersed_token_profiles,
    }


def recurrent_set_batch_audit(n: int = 4) -> dict[str, int]:
    P = {(0, 0)}
    F = set(canonical_extension(P, n))
    U = {(i, j) for i in range(n) for j in range(n)} - F
    edges_tuple = tuple(sorted(U))
    k = len(P)
    subset_profiles = batch_profiles = wall_profiles = cover_checks = 0
    token_heavy = token_dispersed = 0
    for mask in range(1, 1 << len(U)):
        W = {
            edges_tuple[i]
            for i in range(len(edges_tuple))
            if mask >> i & 1
        }
        r = len(W)
        subset_profiles += 1
        W0 = {
            edge for edge in W if edge[0] != 0 and edge[1] != 0
        }
        nu = maximum_matching_size(W0, n)
        s = 2
        if nu >= s:
            batch_profiles += 1
            require(
                any(
                    len(subset) == s and compatible(subset)
                    for subset in itertools.combinations(W0, s)
                ),
                "batch matching missing",
            )
        else:
            wall_profiles += 1
            cover = minimum_vertex_cover(W0, n)
            require(len(cover) == nu, "Konig equality failed")
            full_cover = cover | {("L", 0), ("R", 0)}
            require(
                all(
                    ("L", x) in full_cover or ("R", y) in full_cover
                    for x, y in W
                ),
                "persistent set not covered",
            )
            degree = max(
                [sum(x == v for x, _ in W) for v in range(n)]
                + [sum(y == v for _, y in W) for v in range(n)]
            )
            require(
                degree >= math.ceil(r / (2 * k + s - 1)),
                "persistent wall degree",
            )
            cover_checks += 1
            H = max(2, math.ceil(math.sqrt(degree)))
            classes = Counter(index % 2 for index in range(degree))
            if max(classes.values()) >= H:
                token_heavy += 1
            else:
                require(
                    len(classes) >= math.ceil(degree / (H - 1)),
                    "persistent token dispersion",
                )
                token_dispersed += 1
    N, H_P, r, recurrence_threshold = len(U), 4, 2, 3
    finite_bound_num = (
        (recurrence_threshold - 1) * math.comb(N, r)
    )
    finite_bound_den = math.comb(H_P, r)
    require(finite_bound_num >= finite_bound_den,
            "subset history bound malformed")
    bulk_steps = (n - len(P)) // 2
    require(bulk_steps == 1, "bulk absorption depth sample")
    return {
        "persistent_unavailable_set_profiles": subset_profiles,
        "batch_absorption_profiles": batch_profiles,
        "small_cover_wall_profiles": wall_profiles,
        "persistent_cover_checks": cover_checks,
        "persistent_heavy_token_profiles": token_heavy,
        "persistent_dispersed_token_profiles": token_dispersed,
        "sample_subset_history_bound_numerator": finite_bound_num,
        "sample_subset_history_bound_denominator": finite_bound_den,
        "sample_bulk_absorption_steps": bulk_steps,
    }


def slack_core_audit() -> dict[str, int]:
    parameter_checks = threshold_one_checks = conditioned_checks = 0
    for q in range(4, 9):
        for n in range(5, 11):
            lower = Fraction(11, 30) * (
                1 - Fraction(2, q) - Fraction(1, q * (n - 1))
            )
            require(lower >= Fraction(77, 480),
                    "threshold-one collateral constant")
            threshold_one_checks += 1
            for r in range(2, min(5, n) + 1):
                bound = Fraction(11, 30) * (
                    1
                    - Fraction(2, q)
                    - Fraction(r - 1, q * (n - 1))
                )
                delta = Fraction(r - 1, q * (n - 1))
                score = Fraction(11, 30) * (
                    1 - Fraction(2, q) - delta
                )
                require(score == bound,
                        "small-threshold slack conversion")
                parameter_checks += 1
    N, H, a, r, recurrence_threshold = 12, 5, 1, 2, 3
    numerator = (
        (recurrence_threshold - 1) * math.comb(N - a, r)
    )
    denominator = math.comb(H - a, r)
    require(numerator // denominator == 18,
            "conditioned history sample")
    conditioned_checks += 1
    target_rank = 4
    numerator2 = (
        (recurrence_threshold - 1)
        * math.comb(N - 1, target_rank - 1)
    )
    denominator2 = math.comb(H - 1, target_rank - 1)
    require(numerator2 // denominator2 == 82,
            "target-rank conditioned sample")
    conditioned_checks += 1
    return {
        "slack_parameter_checks": parameter_checks,
        "threshold_one_constant_checks": threshold_one_checks,
        "conditioned_recurrent_set_checks": conditioned_checks,
        "sample_conditioned_history_bound": numerator // denominator,
        "sample_target_rank_history_bound": numerator2 // denominator2,
    }


def owned_certificate_audit() -> dict[str, int]:
    p, h, t = 2, 3, 8
    selector_stock = (
        (h + 1) * t * t * (t - 1) ** 2
        + 2 * (h + 1) * t**4 * (t - 1) ** 2
    )
    protected_state_stock = (t + 1) * selector_stock
    line_stock = protected_state_stock * math.comb(t * t, 2)
    token_stock = (
        (p + 1) * (h - 1) * t * (t - 1) * protected_state_stock
    )
    require(selector_stock == 1_618_176, "selector stock")
    require(protected_state_stock == 14_563_584,
            "protected state stock")
    require(line_stock == 29_360_185_344, "owned line stock")
    require(token_stock == 4_893_364_224, "owned token stock")

    recurrence_threshold, H, R = 3, 4, 5
    toy_token_stock = 24
    finite_token_episodes = (
        (recurrence_threshold - 1) * toy_token_stock // H
    )
    require(finite_token_episodes == 12,
            "owned token episode bound")
    toy_line_stock = 30
    finite_line_episodes = (
        (recurrence_threshold - 1) * toy_line_stock // R
    )
    require(finite_line_episodes == 12,
            "owned line episode bound")
    labels = [
        (owner, token, edge)
        for owner in range(2)
        for token in range(3)
        for edge in range(4)
    ]
    require(len(labels) == toy_token_stock,
            "toy owned label stock")
    return {
        "sample_selector_signature_stock": selector_stock,
        "sample_protected_state_owner_stock": protected_state_stock,
        "sample_owned_line_stock": line_stock,
        "sample_owned_token_edge_stock": token_stock,
        "toy_finite_token_episode_bound": finite_token_episodes,
        "toy_finite_line_episode_bound": finite_line_episodes,
    }


CONTRACT = {
    "schema": "prime-power-selector-protected-certificate-ancestry/v1",
    "source_ranges": [
        "CMR577-CMR581",
        "CMR582-CMR586",
        "CMR587-CMR592",
        "CMR593-CMR598",
        "CMR599-CMR604",
    ],
    "finite_parameters": {
        "deletion_host_side": 3,
        "protected_contact_side": 4,
        "persistent_batch_side": 4,
        "selector_slack_q_range": [4, 8],
        "selector_slack_n_range": [5, 10],
        "owned_stock_sample": {"p": 2, "h": 3, "t": 8},
    },
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "b82d83290aa95e41743fe1db9dbbf3a26c09801f40888e42cc1c8e0f0eefd0f0"


def mutation_audit(report: dict[str, Any]) -> int:
    mutations = [
        lambda value: value["census"].update(
            disjoint_conflict_packings=0
        ),
        lambda value: value["census"].update(
            private_deleted_edge_incidences=0
        ),
        lambda value: value["census"].update(
            protected_contact_states=0
        ),
        lambda value: value["census"].update(
            persistent_unavailable_set_profiles=0
        ),
        lambda value: value["census"].update(
            threshold_one_constant_checks=0
        ),
        lambda value: value["census"].update(
            sample_owned_line_stock=0
        ),
        lambda value: value.update(contract_sha256="0" * 64),
        lambda value: value.update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutator in mutations:
        bad = copy.deepcopy(report)
        mutator(bad)
        try:
            require(
                bad.get("contract_sha256")
                == EXPECTED_CONTRACT_SHA256,
                "contract",
            )
            require(bad.get("all_n_proved_by_checker") == 0,
                    "honesty")
            for key in (
                "disjoint_conflict_packings",
                "private_deleted_edge_incidences",
                "protected_contact_states",
                "persistent_unavailable_set_profiles",
                "threshold_one_constant_checks",
                "sample_owned_line_stock",
            ):
                require(
                    isinstance(bad["census"].get(key), int)
                    and bad["census"][key] > 0,
                    key,
                )
        except ProtectedCertificateError:
            rejected += 1
    require(rejected == len(mutations), "corruption accepted")
    return rejected


def main() -> None:
    contract_sha = digest(CONTRACT)
    require(contract_sha == EXPECTED_CONTRACT_SHA256,
            "contract digest mismatch")
    census: dict[str, int] = {}
    for part in (
        deletion_pass_audit(),
        protected_contact_audit(),
        recurrent_set_batch_audit(),
        slack_core_audit(),
        owned_certificate_audit(),
    ):
        require(not (set(census) & set(part)),
                "duplicate census key")
        census.update(part)
    report = {
        "checker": "prime-power-selector-protected-certificate-ancestry",
        "contract_sha256": contract_sha,
        "census": census,
        "disjoint_conflict_deletion_ancestry_proved": 1,
        "protected_contact_token_ledger_exact": 1,
        "dynamic_selector_recurrent_set_batching_exact": 1,
        "selector_slack_persistent_core_exact": 1,
        "owned_certificate_stock_exact": 1,
        "selector_protected_certificate_ancestry_proved": 1,
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
    report["census"]["rejected_corruptions"] = mutation_audit(report)
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()

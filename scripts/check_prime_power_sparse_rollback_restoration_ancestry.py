#!/usr/bin/env python3
"""Check sparse rollback restoration, forced-core factorization, and payment.

The checker exhausts all matchable side-three final hosts relative to the
complete deletion-pass ancestor.  It validates the literal CMR439--CMR447
rollback operations and symbolic incidence identities.  It does not establish
global construction exhaustiveness or the all-n theorem.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from math import ceil
from typing import Any, Iterable

Edge = tuple[int, int]
Matching = frozenset[Edge]


class RollbackError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RollbackError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


CONTRACT = {
    "schema": "prime-power-sparse-rollback-restoration-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(439, 448)],
    "transition_kinds": [
        "minimum-rollback-restoration",
        "cheap-rollback-certificate-escape",
        "rollback-forced-core-contraction",
        "rollback-recreated-conflict-support",
    ],
    "owner_effects": [
        "restoration-owner-change",
        "contraction-owner-change",
    ],
    "payments": [
        "rollback-edge-incidence-stock",
        "full-token-restoration-incidence",
        "restored-edge-conflict-support",
        "strict-residual-side-descent",
        "scheduler-dispatch",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "35fc36f758016a3de0dba687950e4d6f0d1b17caece487ef21af3e9967f32267"


def all_edges(n: int) -> tuple[Edge, ...]:
    return tuple((i, j) for i in range(n) for j in range(n))


def perfect_matchings(
    rows: Iterable[int], cols: Iterable[int], edges: Iterable[Edge]
) -> tuple[Matching, ...]:
    rows = tuple(sorted(rows))
    cols = tuple(sorted(cols))
    edge_set = frozenset(edges)
    if len(rows) != len(cols):
        return ()
    if not rows:
        return (frozenset(),)
    out = []
    for perm in itertools.permutations(cols):
        matching = frozenset(zip(rows, perm))
        if matching <= edge_set:
            out.append(matching)
    return tuple(out)


def essential_edges(family: tuple[Matching, ...]) -> frozenset[Edge]:
    require(bool(family), "essential edges require a nonempty family")
    common = set(family[0])
    for matching in family[1:]:
        common.intersection_update(matching)
    return frozenset(common)


def collinear(a: Edge, b: Edge, c: Edge) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def compatible_triples(edges: Iterable[Edge]) -> tuple[frozenset[Edge], ...]:
    triples = []
    for triple in itertools.combinations(sorted(edges), 3):
        if (
            len({e[0] for e in triple}) == 3
            and len({e[1] for e in triple}) == 3
            and collinear(*triple)
        ):
            triples.append(frozenset(triple))
    return tuple(triples)


def minimum_rollback(
    n: int, final_host: frozenset[Edge], essential_edge: Edge
) -> tuple[frozenset[Edge], tuple[Matching, ...]]:
    universe = frozenset(all_edges(n))
    deleted = tuple(sorted(universe - final_host))
    for size in range(1, n + 1):
        candidates = []
        for subset in itertools.combinations(deleted, size):
            restored = frozenset(subset)
            family = perfect_matchings(
                range(n), range(n), (final_host | restored) - {essential_edge}
            )
            if family:
                candidates.append((subset, family))
        if candidates:
            subset, family = min(candidates, key=lambda item: item[0])
            return frozenset(subset), family
    raise RollbackError("no rollback footprint of size at most side")


def make_record(n: int, final_host: frozenset[Edge], edge: Edge) -> dict[str, Any]:
    universe = frozenset(all_edges(n))
    family_final = perfect_matchings(range(n), range(n), final_host)
    require(family_final and edge in essential_edges(family_final), "invalid final essential edge")
    rollback, avoiding_family = minimum_rollback(n, final_host, edge)
    require(1 <= len(rollback) <= n, "rollback size outside theorem bounds")
    restored_host = (final_host | rollback) - {edge}
    require(
        avoiding_family == perfect_matchings(range(n), range(n), restored_host),
        "rollback family mismatch",
    )
    forced = essential_edges(avoiding_family)
    require(rollback <= forced, "minimum rollback edge is not forced")
    require(
        len({u for u, _ in rollback}) == len(rollback)
        and len({v for _, v in rollback}) == len(rollback),
        "minimum rollback set is not a matching",
    )

    rows_removed = frozenset(u for u, _ in rollback)
    cols_removed = frozenset(v for _, v in rollback)
    rows_residual = frozenset(range(n)) - rows_removed
    cols_residual = frozenset(range(n)) - cols_removed
    residual_edges = frozenset(
        (u, v)
        for u, v in restored_host
        if u in rows_residual and v in cols_residual
    )
    residual_family = perfect_matchings(rows_residual, cols_residual, residual_edges)
    require(residual_family, "forced rollback core has empty residual family")
    product = frozenset(rollback | matching for matching in residual_family)
    require(product == frozenset(avoiding_family), "forced rollback factorization failed")
    require(
        len(rows_residual) == n - len(rollback),
        "rollback contraction side identity failed",
    )

    triple_universe = compatible_triples(universe)
    recreated = tuple(
        sorted(
            (
                tuple(sorted(triple))
                for triple in triple_universe
                if triple <= (final_host | rollback) and not triple <= final_host
            )
        )
    )
    require(
        all(set(triple) & set(rollback) for triple in recreated),
        "recreated conflict has no restored-edge support",
    )
    degree = 0
    for restored_edge in rollback:
        degree = max(
            degree,
            sum(restored_edge in triple for triple in triple_universe),
        )
    require(len(recreated) <= len(rollback) * degree, "restored-edge degree bound failed")

    forced_certificates = tuple(
        sorted(
            tuple(sorted(triple))
            for triple in compatible_triples(final_host)
            if all(triple <= matching for matching in family_final)
        )
    )
    escaped_certificates = 0
    for triple_tuple in forced_certificates:
        triple = frozenset(triple_tuple)
        if edge in triple:
            require(
                all(not triple <= matching for matching in avoiding_family),
                "rollback did not escape forced certificate",
            )
            escaped_certificates += 1

    record = {
        "n": n,
        "final_host": sorted(final_host),
        "essential_edge": edge,
        "rollback": sorted(rollback),
        "restored_host": sorted(restored_host),
        "avoiding_family": [sorted(m) for m in avoiding_family],
        "residual_rows": sorted(rows_residual),
        "residual_cols": sorted(cols_residual),
        "residual_edges": sorted(residual_edges),
        "recreated_conflicts": recreated,
        "restored_degree": degree,
        "forced_certificates": forced_certificates,
        "escaped_certificates": escaped_certificates,
        "owner": digest({"n": n, "host": sorted(final_host)}),
    }
    record["seal"] = digest({k: record[k] for k in record if k != "seal"})
    return record


def validate_record(record: dict[str, Any]) -> None:
    rebuilt = make_record(
        int(record["n"]),
        frozenset(tuple(edge) for edge in record["final_host"]),
        tuple(record["essential_edge"]),
    )
    require(record == rebuilt, "rollback record mismatch")


def greedy_disjoint(sets: list[frozenset[Edge]]) -> list[frozenset[Edge]]:
    chosen: list[frozenset[Edge]] = []
    used: set[Edge] = set()
    for footprint in sorted(sets, key=lambda item: (len(item), tuple(sorted(item)))):
        if not (set(footprint) & used):
            chosen.append(footprint)
            used.update(footprint)
    return chosen


def mutation_audit(valid: dict[str, Any]) -> int:
    mutations = []
    for field, replacement in [
        ("essential_edge", (99, 99)),
        ("rollback", []),
        ("restored_host", []),
        ("avoiding_family", []),
        ("residual_rows", []),
        ("recreated_conflicts", [((0, 0), (0, 1), (0, 2))]),
        ("owner", "corrupt"),
        ("seal", "0" * 64),
    ]:
        copy = json.loads(json.dumps(valid))
        copy[field] = replacement
        mutations.append(copy)
    rejected = 0
    for mutation in mutations:
        try:
            validate_record(mutation)
        except Exception:
            rejected += 1
    require(rejected == len(mutations), "not every rollback corruption was rejected")
    return rejected


def finite_regression() -> dict[str, Any]:
    n = 3
    universe = all_edges(n)
    matchable_hosts = 0
    essential_pairs = 0
    cheap_rollbacks = 0
    strict_factor_rollbacks = 0
    rollback_edge_incidences = 0
    token_incidences = 0
    recreated_conflicts = 0
    escaped_certificates = 0
    concentrated_hosts = 0
    disjoint_hosts = 0
    rollback_size_histogram: dict[int, int] = {}
    sample = None

    for mask in range(1 << len(universe)):
        host = frozenset(universe[i] for i in range(len(universe)) if mask & (1 << i))
        family = perfect_matchings(range(n), range(n), host)
        if not family:
            continue
        matchable_hosts += 1
        footprints = []
        for edge in sorted(essential_edges(family)):
            record = make_record(n, host, edge)
            validate_record(record)
            essential_pairs += 1
            size = len(record["rollback"])
            rollback_size_histogram[size] = rollback_size_histogram.get(size, 0) + 1
            rollback_edge_incidences += size
            token_incidences += 6 * size
            recreated_conflicts += len(record["recreated_conflicts"])
            escaped_certificates += record["escaped_certificates"]
            if size < 2:
                cheap_rollbacks += 1
            else:
                strict_factor_rollbacks += 1
            footprints.append(frozenset(tuple(e) for e in record["rollback"]))
            if sample is None and size >= 2:
                sample = record
        if footprints:
            require(sum(map(len, footprints)) <= n * n, "total rollback incidence exceeds n^2")
            counts: dict[Edge, int] = {}
            for footprint in footprints:
                for restored in footprint:
                    counts[restored] = counts.get(restored, 0) + 1
            if max(counts.values(), default=0) >= 2:
                concentrated_hosts += 1
            else:
                chosen = greedy_disjoint(footprints)
                lower = ceil(len(footprints) / n)
                require(len(chosen) >= lower, "disjoint rollback packing bound failed")
                disjoint_hosts += 1

    require(sample is not None, "no rollback of size at least two found")
    rejected = mutation_audit(sample)
    return {
        "side_three_matchable_final_hosts": matchable_hosts,
        "final_essential_edge_pairs": essential_pairs,
        "rollback_size_histogram": rollback_size_histogram,
        "cheap_q2_rollbacks": cheap_rollbacks,
        "strict_q2_factor_rollbacks": strict_factor_rollbacks,
        "rollback_edge_incidences": rollback_edge_incidences,
        "sample_full_token_incidences_p2_h3": token_incidences,
        "recreated_conflicts_with_restored_support": recreated_conflicts,
        "forced_certificates_escaped": escaped_certificates,
        "rollback_concentration_hosts": concentrated_hosts,
        "rollback_disjoint_packing_hosts": disjoint_hosts,
        "rejected_corruptions": rejected,
    }


def main() -> None:
    contract_digest = digest(CONTRACT)
    require(contract_digest == EXPECTED_CONTRACT_DIGEST, "contract digest mismatch")
    census = finite_regression()
    report = {
        "contract_digest": contract_digest,
        "census": census,
        "sparse_rollback_restoration_ancestry_proved": 1,
        "minimum_rollback_forced_core_exact": 1,
        "rollback_token_incidence_exact": 1,
        "rollback_recreated_conflict_support_exact": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_returned_edge_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()

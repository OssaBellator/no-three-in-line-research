#!/usr/bin/env python3
"""Check essential-return Hall-wall extraction, factorization, and tree stock.

This executable finite checker validates the literal CMR727--CMR747 operations
on exhaustive small bipartite hosts.  It proves only the reported finite and
symbolic identities and permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from functools import lru_cache
from math import comb
from typing import Any, Iterable

Edge = tuple[int, int]
Matching = frozenset[Edge]


class HallWallError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise HallWallError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


CONTRACT = {
    "schema": "prime-power-essential-return-unit-wall-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(727, 748)],
    "transition_kinds": [
        "essential-return-unit-wall-extraction",
        "essential-unit-wall-factor-split",
        "unit-wall-local-edge-deletion",
        "unit-wall-forced-target-dispatch",
        "unit-wall-factor-tree-split",
    ],
    "owner_effects": [
        "same-essential-return-owner",
        "factor-child-owner-change",
        "host-owner-change",
    ],
    "payments": [
        "canonical-wall-stock",
        "strict-factor-side-mass-descent",
        "factor-edge-deletion-stock",
        "tree-edge-token-stock",
        "tree-certificate-stock",
        "scheduler-dispatch",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_DIGEST = "97e448a12314e894018ee0065b9e58b0b4d0172c22f1b619ad7329989f7be0e5"


def all_edges(n: int) -> tuple[Edge, ...]:
    return tuple((i, j) for i in range(n) for j in range(n))


def perfect_matchings(
    rows: Iterable[int], cols: Iterable[int], edges: Iterable[Edge]
) -> tuple[Matching, ...]:
    row_tuple = tuple(sorted(rows))
    col_tuple = tuple(sorted(cols))
    edge_set = frozenset(edges)
    if len(row_tuple) != len(col_tuple):
        return ()
    if not row_tuple:
        return (frozenset(),)
    out: list[Matching] = []
    for perm in itertools.permutations(col_tuple):
        candidate = frozenset(zip(row_tuple, perm))
        if candidate <= edge_set:
            out.append(candidate)
    return tuple(out)


def complete_matchings(n: int) -> tuple[Matching, ...]:
    return perfect_matchings(range(n), range(n), all_edges(n))


def neighbour_set(edges: frozenset[Edge], source: frozenset[int]) -> frozenset[int]:
    return frozenset(v for u, v in edges if u in source)


def max_matching_size(n: int, edges: frozenset[Edge]) -> int:
    best = 0
    rows = tuple(range(n))
    cols = tuple(range(n))
    for k in range(1, n + 1):
        found = False
        for row_subset in itertools.combinations(rows, k):
            for col_subset in itertools.combinations(cols, k):
                if perfect_matchings(row_subset, col_subset, edges):
                    found = True
                    break
            if found:
                break
        if found:
            best = k
    return best


def essential_edges(matchings: tuple[Matching, ...]) -> frozenset[Edge]:
    require(bool(matchings), "essentiality requires a nonempty family")
    common = set(matchings[0])
    for matching in matchings[1:]:
        common.intersection_update(matching)
    return frozenset(common)


def canonical_minimal_wall(n: int, avoiding_edges: frozenset[Edge]) -> tuple[frozenset[int], frozenset[int]]:
    candidates: list[tuple[int, tuple[int, ...], frozenset[int]]] = []
    for size in range(1, n + 1):
        for source_tuple in itertools.combinations(range(n), size):
            source = frozenset(source_tuple)
            target = neighbour_set(avoiding_edges, source)
            if len(target) < size:
                candidates.append((size, source_tuple, target))
        if candidates:
            break
    require(bool(candidates), "no deficient Hall set found")
    _, source_tuple, target = min(candidates)
    return frozenset(source_tuple), target


def collinear(a: Edge, b: Edge, c: Edge) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def compatible_triples(edges: Iterable[Edge]) -> tuple[frozenset[Edge], ...]:
    edge_tuple = tuple(sorted(edges))
    triples: list[frozenset[Edge]] = []
    for triple in itertools.combinations(edge_tuple, 3):
        rows = {edge[0] for edge in triple}
        cols = {edge[1] for edge in triple}
        if len(rows) == len(cols) == 3 and collinear(*triple):
            triples.append(frozenset(triple))
    return tuple(triples)


def active_triples(matchings: tuple[Matching, ...], triples: Iterable[frozenset[Edge]]) -> frozenset[frozenset[Edge]]:
    return frozenset(triple for triple in triples if any(triple <= matching for matching in matchings))


def canonical_stored_avoidance(n: int, edge: Edge) -> Matching:
    choices = [matching for matching in complete_matchings(n) if edge not in matching]
    require(bool(choices), "complete host must provide stored avoidance")
    return min(choices, key=lambda matching: tuple(sorted(matching)))


def make_wall_record(n: int, host: frozenset[Edge], edge: Edge) -> dict[str, Any]:
    family = perfect_matchings(range(n), range(n), host)
    require(family and edge in essential_edges(family), "edge must be essential")
    avoiding_host = host - {edge}
    require(max_matching_size(n, avoiding_host) == n - 1, "deficiency must equal one")
    source, target = canonical_minimal_wall(n, avoiding_host)
    u, v = edge
    require(len(target) == len(source) - 1, "unit wall size failure")
    require(u in source and v not in target, "essential endpoints not aligned with wall")
    require(neighbour_set(host, source) == target | {v}, "essential edge must uniquely repair wall")
    for x in source:
        require(
            neighbour_set(avoiding_host, source - {x}) == target,
            "minimal wall robustness failed",
        )
    if len(source) >= 2:
        for y in target:
            require(
                sum((x, y) in avoiding_host for x in source) >= 2,
                "nontrivial wall target has degree below two",
            )

    stored = canonical_stored_avoidance(n, edge)
    missing_wall_edges = tuple(
        sorted((x, y) for x, y in stored if x in source and y not in target)
    )
    require(bool(missing_wall_edges), "stored avoidance supplies no wall witness")
    require(all(f not in host for f in missing_wall_edges), "stored wall witness unexpectedly present")
    witness = missing_wall_edges[0]

    rows_a = source - {u}
    cols_a = target
    rows_b = frozenset(range(n)) - source
    cols_b = frozenset(range(n)) - (target | {v})
    edges_a = frozenset((x, y) for x, y in host if x in rows_a and y in cols_a)
    edges_b = frozenset((x, y) for x, y in host if x in rows_b and y in cols_b)
    family_a = perfect_matchings(rows_a, cols_a, edges_a)
    family_b = perfect_matchings(rows_b, cols_b, edges_b)
    require(family_a and family_b, "wall factors must be matchable")
    product = frozenset(frozenset({edge}) | ma | mb for ma in family_a for mb in family_b)
    require(product == frozenset(family), "exact wall factor product failed")
    require(len(rows_a) + len(rows_b) == n - 1, "strict side mass identity failed")

    triples = compatible_triples(host)
    active = active_triples(family, triples)
    target_cases = []
    for triple in sorted((q for q in active if edge in q), key=lambda q: tuple(sorted(q))):
        local = tuple(sorted(triple - {edge}))
        require(len(local) == 2, "target rank after contraction must be two")
        require(all(f in edges_a or f in edges_b for f in local), "target edge outside factors")
        local_essential: list[bool] = []
        for f in local:
            factor_family = family_a if f in edges_a else family_b
            local_essential.append(all(f in matching for matching in factor_family))
        if all(local_essential):
            require(all(triple <= matching for matching in family), "forced wall certificate not global")
            target_cases.append(("forced", tuple(sorted(triple)), None))
        else:
            deletable = min(f for f, forced in zip(local, local_essential) if not forced)
            child_host = host - {deletable}
            child_family = perfect_matchings(range(n), range(n), child_host)
            require(child_family, "local deletion killed all matchings")
            require(not any(triple <= matching for matching in child_family), "target survived local deletion")
            require(
                active_triples(child_family, triples) <= active,
                "deletion activated a previously inactive target",
            )
            target_cases.append(("deleted", tuple(sorted(triple)), deletable))

    signature = {
        "owner": digest({"n": n, "host": sorted(host)}),
        "essential_edge": edge,
        "source_wall": sorted(source),
        "target_wall": sorted(target),
        "stored_witness": witness,
    }
    record = {
        "n": n,
        "host": sorted(host),
        "family": [sorted(matching) for matching in family],
        "edge": edge,
        "source": sorted(source),
        "target": sorted(target),
        "stored": sorted(stored),
        "witness": witness,
        "factor_a_rows": sorted(rows_a),
        "factor_a_cols": sorted(cols_a),
        "factor_a_edges": sorted(edges_a),
        "factor_b_rows": sorted(rows_b),
        "factor_b_cols": sorted(cols_b),
        "factor_b_edges": sorted(edges_b),
        "signature": signature,
        "target_cases": target_cases,
    }
    record["seal"] = digest({k: record[k] for k in record if k != "seal"})
    return record


def validate_record(record: dict[str, Any]) -> None:
    n = record["n"]
    host = frozenset(tuple(edge) for edge in record["host"])
    edge = tuple(record["edge"])
    rebuilt = make_wall_record(n, host, edge)
    require(record == rebuilt, "wall record mismatch")


@lru_cache(maxsize=None)
def max_tree_metrics(side: int) -> tuple[int, int, int, int, int, int]:
    """Return max splits, nodes, leaves, depth, edge-stock, certificate-stock."""
    if side <= 0:
        return (0, 1, 1, 0, 0, 0)
    best = (0, 1, 1, 0, side * side, comb(side * side, 3))
    for a in range(side):
        b = side - 1 - a
        ma = max_tree_metrics(a)
        mb = max_tree_metrics(b)
        candidate = (
            1 + ma[0] + mb[0],
            1 + ma[1] + mb[1],
            ma[2] + mb[2],
            1 + max(ma[3], mb[3]),
            side * side + ma[4] + mb[4],
            comb(side * side, 3) + ma[5] + mb[5],
        )
        best = tuple(max(x, y) for x, y in zip(best, candidate))
    return best


def tree_audit(max_side: int = 7) -> dict[str, Any]:
    split_pairs = 0
    samples = []
    for side in range(1, max_side + 1):
        split_pairs += side
        splits, nodes, leaves, depth, edge_stock, cert_stock = max_tree_metrics(side)
        edge_bound = sum(j * j for j in range(1, side + 1))
        cert_bound = sum(comb(j * j, 3) for j in range(1, side + 1))
        require(splits <= side, "tree split bound failed")
        require(nodes <= 2 * side + 1, "tree node bound failed")
        require(leaves <= side + 1, "tree leaf bound failed")
        require(depth <= side, "tree depth bound failed")
        require(edge_stock <= edge_bound, "tree edge-stock bound failed")
        require(cert_stock <= cert_bound, "tree certificate-stock bound failed")
        samples.append(
            {
                "side": side,
                "max_splits": splits,
                "max_nodes": nodes,
                "max_leaves": leaves,
                "max_depth": depth,
                "max_edge_stock": edge_stock,
                "edge_bound": edge_bound,
                "max_certificate_stock": cert_stock,
                "certificate_bound": cert_bound,
            }
        )
    return {"split_pairs_checked": split_pairs, "samples": samples}


def mutation_audit(valid: dict[str, Any]) -> int:
    mutations = []
    for field, replacement in [
        ("edge", (99, 99)),
        ("source", []),
        ("target", []),
        ("witness", (99, 99)),
        ("factor_a_edges", []),
        ("factor_b_edges", []),
        ("signature", {"corrupt": True}),
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
    require(rejected == len(mutations), "not every corruption was rejected")
    return rejected


def finite_regression() -> dict[str, Any]:
    n = 3
    universe = all_edges(n)
    hosts = 0
    essential_pairs = 0
    singleton_walls = 0
    robust_walls = 0
    forced_targets = 0
    deleted_targets = 0
    factor_state_incidences = 0
    sample_record = None

    for mask in range(1 << len(universe)):
        host = frozenset(universe[i] for i in range(len(universe)) if mask & (1 << i))
        family = perfect_matchings(range(n), range(n), host)
        if not family:
            continue
        hosts += 1
        for edge in sorted(essential_edges(family)):
            record = make_wall_record(n, host, edge)
            validate_record(record)
            essential_pairs += 1
            if len(record["source"]) == 1:
                singleton_walls += 1
            else:
                robust_walls += 1
            for kind, _, _ in record["target_cases"]:
                forced_targets += kind == "forced"
                deleted_targets += kind == "deleted"
            factor_state_incidences += len(record["family"])
            if sample_record is None and len(record["source"]) > 1:
                sample_record = record

    require(sample_record is not None, "no nontrivial wall sample found")
    tree = tree_audit()
    rejected = mutation_audit(sample_record)
    return {
        "side_three_matchable_hosts": hosts,
        "essential_return_host_edge_pairs": essential_pairs,
        "singleton_unit_walls": singleton_walls,
        "robust_unit_walls": robust_walls,
        "forced_wall_target_cases": forced_targets,
        "deletable_wall_target_cases": deleted_targets,
        "full_family_state_incidences": factor_state_incidences,
        "tree_split_pairs_checked": tree["split_pairs_checked"],
        "side_seven_tree_metrics": tree["samples"][-1],
        "rejected_corruptions": rejected,
    }


def main() -> None:
    contract_digest = digest(CONTRACT)
    require(contract_digest == EXPECTED_CONTRACT_DIGEST, "contract digest mismatch")
    census = finite_regression()
    report = {
        "contract_digest": contract_digest,
        "census": census,
        "essential_return_unit_wall_ancestry_proved": 1,
        "unit_wall_factorization_exact": 1,
        "unit_wall_target_normalization_exact": 1,
        "unit_wall_factor_tree_stock_exact": 1,
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

#!/usr/bin/env python3
"""Verify canonical generation and contraction of asymmetric two-layer contexts.

An asymmetric context has independent surviving row and column domains in each
labelled layer. Each layer is a perfect matching on its own domain pair; the
layers retain physical-cell disjointness in the original grid coordinates.

The checker generates the exact feasible family, triple universe, canonical
anchor, empty/clean/dirty dispatch, deleted/required extensions, forced-set
contractions, and composition of two successive forced-triple contractions.
It does not prove global context generation, recurrence termination, or the
all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, permutations
from typing import Any, Iterable

from check_prime_power_required_prefix_parent_generation import (
    Edge,
    State,
    Triple,
    all_host_edges,
    exact_edge,
    exact_mask,
    exact_required,
    generate_exact_triple_universe,
)

EXPECTED_CONTRACT_SHA256 = "8a12029b565cd8b9d51dba236f3cff782ed45ef3544fffd3ccddab8b0a32a0b9"


class AsymmetricContextGenerationError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AsymmetricContextGenerationError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_domain(
    n: int,
    raw: Iterable[int],
    path: str,
) -> tuple[int, ...]:
    require(not isinstance(raw, (str, bytes)), f"{path}: iterable required")
    values = tuple(raw)
    require(values == tuple(sorted(values)), f"{path}: canonical order required")
    require(len(values) == len(set(values)), f"{path}: duplicate coordinate")
    require(
        all(isinstance(value, int) and not isinstance(value, bool)
            and 0 <= value < n for value in values),
        f"{path}: coordinate outside ambient side",
    )
    return values


def exact_domains(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    require(isinstance(n, int) and not isinstance(n, bool) and n >= 1,
            "ambient side must be a positive integer")
    row_domains = tuple(row_domains_raw)
    column_domains = tuple(column_domains_raw)
    require(len(row_domains) == 2 and len(column_domains) == 2,
            "exactly two layer domains required")
    domains = []
    for layer in (0, 1):
        rows = exact_domain(n, row_domains[layer], f"row_domains[{layer}]")
        columns = exact_domain(
            n, column_domains[layer], f"column_domains[{layer}]"
        )
        require(len(rows) == len(columns),
                f"layer {layer}: row/column domain sizes differ")
        domains.append((rows, columns))
    return tuple(domains)


def exact_asymmetric_context(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> tuple[
    tuple[tuple[tuple[int, ...], tuple[int, ...]], ...],
    tuple[Edge, ...],
    tuple[Edge, ...],
]:
    domains = exact_domains(n, row_domains_raw, column_domains_raw)
    deleted = exact_mask(n, deleted_raw)
    required = exact_required(n, required_raw)
    require(set(deleted).isdisjoint(required),
            "deleted and required edges must be disjoint")
    for path, edges in (("deleted", deleted), ("required", required)):
        for index, edge in enumerate(edges):
            layer, row, column = edge
            rows, columns = domains[layer]
            require(
                row in rows and column in columns,
                f"{path}[{index}]: edge outside layer domain",
            )
    return domains, deleted, required


def asymmetric_host_edges(
    domains: tuple[tuple[tuple[int, ...], tuple[int, ...]], ...],
) -> tuple[Edge, ...]:
    return tuple(
        (layer, row, column)
        for layer in (0, 1)
        for row in domains[layer][0]
        for column in domains[layer][1]
    )


def generate_asymmetric_family(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> tuple[State, ...]:
    domains, deleted, required = exact_asymmetric_context(
        n, row_domains_raw, column_domains_raw, deleted_raw, required_raw
    )
    deleted_set = set(deleted)
    required_set = set(required)
    layer_states: list[list[tuple[Edge, ...]]] = []
    for layer in (0, 1):
        rows, columns = domains[layer]
        required_layer = {edge for edge in required_set if edge[0] == layer}
        candidates: list[tuple[Edge, ...]] = []
        for image in permutations(columns):
            state = tuple(
                (layer, rows[index], image[index])
                for index in range(len(rows))
            )
            if deleted_set.isdisjoint(state) and required_layer <= set(state):
                candidates.append(state)
        layer_states.append(candidates)

    family: list[State] = []
    for left in layer_states[0]:
        for right in layer_states[1]:
            state = tuple(sorted(left + right))
            physical = tuple((edge[1], edge[2]) for edge in state)
            if len(physical) == len(set(physical)):
                family.append(state)
    return tuple(sorted(family))


def state_triples(
    state: State,
    universe: tuple[Triple, ...],
) -> tuple[Triple, ...]:
    edge_set = set(state)
    return tuple(triple for triple in universe if set(triple) <= edge_set)


def exact_asymmetric_manifest(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    domains, deleted, required = exact_asymmetric_context(
        n, row_domains_raw, column_domains_raw, deleted_raw, required_raw
    )
    family = generate_asymmetric_family(
        n,
        tuple(domain[0] for domain in domains),
        tuple(domain[1] for domain in domains),
        deleted,
        required,
    )
    universe = generate_exact_triple_universe(family)
    anchor = None if not family else family[0]
    anchor_triples = () if anchor is None else state_triples(anchor, universe)
    if not family:
        dispatch_mode = "infeasible-asymmetric-context-terminal"
        canonical_target = None
    elif not anchor_triples:
        dispatch_mode = "clean-asymmetric-anchor-terminal"
        canonical_target = None
    else:
        dispatch_mode = "dirty-asymmetric-anchor-canonical-target"
        canonical_target = anchor_triples[0]

    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-asymmetric-context-generation-v1",
        "ambient_side": n,
        "layer_domains": [
            {
                "layer": layer,
                "rows": list(domains[layer][0]),
                "columns": list(domains[layer][1]),
                "matching_size": len(domains[layer][0]),
            }
            for layer in (0, 1)
        ],
        "deleted_edges": [list(edge) for edge in deleted],
        "required_edges": [list(edge) for edge in required],
        "feasible_family": [
            [list(edge) for edge in state] for state in family
        ],
        "exact_triple_universe": [
            [list(edge) for edge in triple] for triple in universe
        ],
        "canonical_anchor": (
            None if anchor is None else [list(edge) for edge in anchor]
        ),
        "dispatch_mode": dispatch_mode,
        "canonical_target": (
            None if canonical_target is None
            else [list(edge) for edge in canonical_target]
        ),
        "claims": {
            "host_edges": len(asymmetric_host_edges(domains)),
            "layer_zero_matching_size": len(domains[0][0]),
            "layer_one_matching_size": len(domains[1][0]),
            "feasible_states": len(family),
            "realizable_collinear_triples": len(universe),
            "asymmetric_context_family_generated": 1,
            "family_generation_duplicate_free": 1,
            "asymmetric_triple_universe_generated": 1,
            "canonical_asymmetric_anchor_generated": int(bool(family)),
            "empty_clean_dirty_dispatch_exhaustive": 1,
            "canonical_target_generated_from_anchor": int(bool(anchor_triples)),
            "local_asymmetric_candidate_response_complete": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def validate_asymmetric_manifest(
    manifest: Any,
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
) -> dict[str, int]:
    expected = exact_asymmetric_manifest(
        n, row_domains_raw, column_domains_raw, deleted_raw, required_raw
    )
    require(isinstance(manifest, dict) and manifest == expected,
            "asymmetric context manifest mismatch")
    return copy.deepcopy(expected["claims"])


def validate_deletion_extension(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    edge_raw: Iterable[int],
) -> None:
    domains, deleted, required = exact_asymmetric_context(
        n, row_domains_raw, column_domains_raw, deleted_raw, required_raw
    )
    edge = exact_edge(edge_raw, n, "extension_edge")
    require(edge in asymmetric_host_edges(domains),
            "extension edge outside asymmetric host")
    require(edge not in set(deleted) | set(required),
            "deletion extension edge already classified")
    rows = tuple(domain[0] for domain in domains)
    columns = tuple(domain[1] for domain in domains)
    parent = generate_asymmetric_family(n, rows, columns, deleted, required)
    child_deleted = tuple(sorted(deleted + (edge,)))
    child = generate_asymmetric_family(
        n, rows, columns, child_deleted, required
    )
    direct = tuple(state for state in parent if edge not in set(state))
    require(child == direct, "asymmetric deletion extension identity failed")
    require(
        set(generate_exact_triple_universe(child))
        <= set(generate_exact_triple_universe(parent)),
        "asymmetric deletion extension created a triple",
    )


def validate_required_extension(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    edge_raw: Iterable[int],
) -> None:
    domains, deleted, required = exact_asymmetric_context(
        n, row_domains_raw, column_domains_raw, deleted_raw, required_raw
    )
    edge = exact_edge(edge_raw, n, "extension_edge")
    require(edge in asymmetric_host_edges(domains),
            "extension edge outside asymmetric host")
    require(edge not in set(deleted) | set(required),
            "required extension edge already classified")
    child_required = tuple(sorted(required + (edge,)))
    exact_required(n, child_required)
    rows = tuple(domain[0] for domain in domains)
    columns = tuple(domain[1] for domain in domains)
    parent = generate_asymmetric_family(n, rows, columns, deleted, required)
    child = generate_asymmetric_family(
        n, rows, columns, deleted, child_required
    )
    direct = tuple(state for state in parent if edge in set(state))
    require(child == direct, "asymmetric required extension identity failed")
    require(
        set(generate_exact_triple_universe(child))
        <= set(generate_exact_triple_universe(parent)),
        "asymmetric required extension created a triple",
    )


def exact_forced_set(
    n: int,
    raw: Iterable[Iterable[int]],
) -> tuple[Edge, ...]:
    forced = exact_required(n, raw)
    require(forced, "forced set must be nonempty")
    return forced


def contract_forced_set(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    forced_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    domains, deleted, required = exact_asymmetric_context(
        n, row_domains_raw, column_domains_raw, deleted_raw, required_raw
    )
    forced = exact_forced_set(n, forced_raw)
    require(set(forced) <= set(required),
            "forced set must be contained in required context")
    rows = tuple(domain[0] for domain in domains)
    columns = tuple(domain[1] for domain in domains)
    parent = generate_asymmetric_family(n, rows, columns, deleted, required)
    require(parent, "forced contraction parent must be feasible")

    child_rows: list[tuple[int, ...]] = []
    child_columns: list[tuple[int, ...]] = []
    for layer in (0, 1):
        part = tuple(edge for edge in forced if edge[0] == layer)
        removed_rows = {edge[1] for edge in part}
        removed_columns = {edge[2] for edge in part}
        child_rows.append(tuple(
            row for row in rows[layer] if row not in removed_rows
        ))
        child_columns.append(tuple(
            column for column in columns[layer] if column not in removed_columns
        ))

    child_deleted: set[Edge] = set()
    for edge in deleted:
        layer, row, column = edge
        if row in child_rows[layer] and column in child_columns[layer]:
            child_deleted.add(edge)
    blockers: set[Edge] = set()
    for layer, row, column in forced:
        opposite = 1 - layer
        blocker = (opposite, row, column)
        if (row in child_rows[opposite]
                and column in child_columns[opposite]):
            blockers.add(blocker)
            child_deleted.add(blocker)

    child_required = tuple(sorted(set(required) - set(forced)))
    child_deleted_tuple = tuple(sorted(child_deleted))
    child = generate_asymmetric_family(
        n,
        tuple(child_rows),
        tuple(child_columns),
        child_deleted_tuple,
        child_required,
    )
    restricted = tuple(sorted(
        tuple(edge for edge in state if edge not in set(forced))
        for state in parent
    ))
    require(child == restricted,
            "forced-set restriction differs from generated child context")
    adjoined = tuple(sorted(
        tuple(sorted(state + forced)) for state in child
    ))
    require(adjoined == parent, "forced-set adjoin is not inverse")

    parent_universe = generate_exact_triple_universe(parent)
    child_universe = generate_exact_triple_universe(child)
    require(
        child_universe == tuple(
            triple for triple in parent_universe
            if set(triple).isdisjoint(forced)
        ),
        "forced-set child triple universe transport failed",
    )

    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-asymmetric-forced-set-contraction-v1",
        "ambient_side": n,
        "parent_row_domains": [list(rows[layer]) for layer in (0, 1)],
        "parent_column_domains": [
            list(columns[layer]) for layer in (0, 1)
        ],
        "parent_deleted_edges": [list(edge) for edge in deleted],
        "parent_required_edges": [list(edge) for edge in required],
        "forced_edges": [list(edge) for edge in forced],
        "child_row_domains": [
            list(child_rows[layer]) for layer in (0, 1)
        ],
        "child_column_domains": [
            list(child_columns[layer]) for layer in (0, 1)
        ],
        "child_deleted_edges": [
            list(edge) for edge in child_deleted_tuple
        ],
        "child_required_edges": [
            list(edge) for edge in child_required
        ],
        "opposite_layer_blockers": [
            list(edge) for edge in sorted(blockers)
        ],
        "child_family": [
            [list(edge) for edge in state] for state in child
        ],
        "child_triple_universe": [
            [list(edge) for edge in triple] for triple in child_universe
        ],
        "claims": {
            "parent_feasible_states": len(parent),
            "child_feasible_states": len(child),
            "forced_edges": len(forced),
            "parent_state_cardinality": (
                len(rows[0]) + len(rows[1])
            ),
            "child_state_cardinality": (
                len(child_rows[0]) + len(child_rows[1])
            ),
            "asymmetric_forced_set_contraction_exact": 1,
            "opposite_layer_blockers_exact": 1,
            "deleted_required_transport_exact": 1,
            "restriction_adjoin_bijection": 1,
            "child_triple_universe_transport_exact": 1,
            "original_grid_coordinates_preserved": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def exact_contraction_composition(
    n: int,
    row_domains_raw: Iterable[Iterable[int]],
    column_domains_raw: Iterable[Iterable[int]],
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    first_raw: Iterable[Iterable[int]],
    second_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    first = exact_forced_set(n, first_raw)
    second = exact_forced_set(n, second_raw)
    require(set(first).isdisjoint(second),
            "composed forced sets must be disjoint")
    combined = tuple(sorted(first + second))
    exact_required(n, combined)

    first_manifest = contract_forced_set(
        n, row_domains_raw, column_domains_raw,
        deleted_raw, required_raw, first
    )
    sequential_manifest = contract_forced_set(
        n,
        first_manifest["child_row_domains"],
        first_manifest["child_column_domains"],
        first_manifest["child_deleted_edges"],
        first_manifest["child_required_edges"],
        second,
    )
    direct_manifest = contract_forced_set(
        n, row_domains_raw, column_domains_raw,
        deleted_raw, required_raw, combined
    )

    sequential_signature = {
        "row_domains": sequential_manifest["child_row_domains"],
        "column_domains": sequential_manifest["child_column_domains"],
        "deleted_edges": sequential_manifest["child_deleted_edges"],
        "required_edges": sequential_manifest["child_required_edges"],
        "family": sequential_manifest["child_family"],
        "triple_universe": sequential_manifest["child_triple_universe"],
    }
    direct_signature = {
        "row_domains": direct_manifest["child_row_domains"],
        "column_domains": direct_manifest["child_column_domains"],
        "deleted_edges": direct_manifest["child_deleted_edges"],
        "required_edges": direct_manifest["child_required_edges"],
        "family": direct_manifest["child_family"],
        "triple_universe": direct_manifest["child_triple_universe"],
    }
    require(
        sequential_signature == direct_signature,
        "sequential and direct asymmetric contractions differ",
    )
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-asymmetric-contraction-composition-v1",
        "ambient_side": n,
        "first_forced_set": [list(edge) for edge in first],
        "second_forced_set": [list(edge) for edge in second],
        "combined_forced_set": [list(edge) for edge in combined],
        "composed_child": sequential_signature,
        "claims": {
            "sequential_direct_domains_equal": 1,
            "sequential_direct_deleted_masks_equal": 1,
            "sequential_direct_required_sets_equal": 1,
            "sequential_direct_families_equal": 1,
            "sequential_direct_triple_universes_equal": 1,
            "forced_contraction_composition_exact": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-asymmetric-context-generation-v1",
        "source_theorems": [
            "CMR2852", "CMR2853", "CMR2854", "CMR2855",
            "CMR2856", "CMR2857", "CMR2863",
        ],
        "claims": {
            "asymmetric_context_family_generated": 1,
            "family_generation_duplicate_free": 1,
            "asymmetric_triple_universe_generated": 1,
            "canonical_asymmetric_anchor_generated": 1,
            "empty_clean_dirty_dispatch_exhaustive": 1,
            "asymmetric_deletion_extension_exact": 1,
            "asymmetric_required_extension_exact": 1,
            "asymmetric_forced_set_contraction_exact": 1,
            "forced_contraction_composition_exact": 1,
            "local_asymmetric_candidate_response_complete": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["contract_sha256"] = digest(result)
    return result


def validate_contract() -> dict[str, int]:
    contract = contract_manifest()
    require(
        contract["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
        "built-in contract digest drift",
    )
    return copy.deepcopy(contract["claims"])


def all_coordinate_subsets(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        subset
        for size in range(n + 1)
        for subset in combinations(range(n), size)
    )


def exhaustive_domain_regression() -> dict[str, int]:
    n = 3
    subsets = all_coordinate_subsets(n)
    hosts = feasible = infeasible = clean = dirty = 0
    state_occurrences = extension_checks = 0
    contraction_contexts: set[tuple[Any, ...]] = set()

    for rows0 in subsets:
        for columns0 in subsets:
            if len(rows0) != len(columns0):
                continue
            for rows1 in subsets:
                for columns1 in subsets:
                    if len(rows1) != len(columns1):
                        continue
                    rows = (rows0, rows1)
                    columns = (columns0, columns1)
                    manifest = exact_asymmetric_manifest(
                        n, rows, columns, (), ()
                    )
                    hosts += 1
                    claims = manifest["claims"]
                    state_occurrences += claims["feasible_states"]
                    if claims["feasible_states"]:
                        feasible += 1
                        clean += int(
                            manifest["dispatch_mode"]
                            == "clean-asymmetric-anchor-terminal"
                        )
                        dirty += int(
                            manifest["dispatch_mode"]
                            == "dirty-asymmetric-anchor-canonical-target"
                        )
                    else:
                        infeasible += 1

                    domains = exact_domains(n, rows, columns)
                    family = generate_asymmetric_family(
                        n, rows, columns, (), ()
                    )
                    for edge in asymmetric_host_edges(domains):
                        validate_deletion_extension(
                            n, rows, columns, (), (), edge
                        )
                        validate_required_extension(
                            n, rows, columns, (), (), edge
                        )
                        extension_checks += 2
                    for state in family:
                        for triple in generate_exact_triple_universe((state,)):
                            contraction_contexts.add(
                                (rows, columns, triple)
                            )

    for rows, columns, triple in contraction_contexts:
        contract_forced_set(
            n, rows, columns, (), triple, triple
        )

    require(
        (hosts, feasible, infeasible, clean, dirty, state_occurrences)
        == (400, 391, 9, 347, 44, 781),
        "side-three asymmetric domain census drift",
    )
    require(extension_checks == 4320,
            "side-three asymmetric extension census drift")
    require(len(contraction_contexts) == 116,
            "side-three asymmetric contraction census drift")
    return {
        "side_three_asymmetric_domain_hosts": hosts,
        "side_three_feasible_domain_hosts": feasible,
        "side_three_infeasible_domain_hosts": infeasible,
        "side_three_clean_anchors": clean,
        "side_three_dirty_anchors": dirty,
        "side_three_state_occurrences": state_occurrences,
        "side_three_extension_checks": extension_checks,
        "side_three_forced_triple_contractions": len(contraction_contexts),
    }


def composition_regression() -> dict[str, int]:
    n = 4
    rows = (tuple(range(n)), tuple(range(n)))
    columns = rows
    family = generate_asymmetric_family(n, rows, columns, (), ())
    seen: set[tuple[Triple, Triple]] = set()
    compositions = 0
    for state in family:
        triples = generate_exact_triple_universe((state,))
        for first, second in combinations(triples, 2):
            if not set(first).isdisjoint(second):
                continue
            key = (first, second)
            if key in seen:
                continue
            seen.add(key)
            required = tuple(sorted(first + second))
            exact_contraction_composition(
                n, rows, columns, (), required, first, second
            )
            compositions += 1
    require(compositions == 152,
            "side-four contraction composition census drift")
    return {
        "side_four_two_triple_contraction_compositions": compositions,
    }


def mutation_tests() -> int:
    n = 3
    rows = ((0, 1), (0, 1, 2))
    columns = ((0, 1), (0, 1, 2))
    manifest = exact_asymmetric_manifest(n, rows, columns, (), ())
    rejected = 0

    malformed = [
        lambda: exact_asymmetric_manifest(
            n, ((1, 0), rows[1]), columns, (), ()
        ),
        lambda: exact_asymmetric_manifest(
            n, rows, ((0,), columns[1]), (), ()
        ),
        lambda: exact_asymmetric_manifest(
            n, rows, columns, ((0, 2, 0),), ()
        ),
        lambda: exact_asymmetric_manifest(
            n, rows, columns, (), ((0, 2, 0),)
        ),
    ]
    for call in malformed:
        try:
            call()
        except ValueError:
            rejected += 1
        else:
            raise AsymmetricContextGenerationError("malformed context accepted")

    def corrupt(mutator: Any) -> None:
        nonlocal rejected
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        try:
            validate_asymmetric_manifest(
                candidate, n, rows, columns, (), ()
            )
        except AsymmetricContextGenerationError:
            rejected += 1
        else:
            raise AsymmetricContextGenerationError(
                "corrupted asymmetric manifest accepted"
            )

    corrupt(lambda data: data["feasible_family"].pop())
    corrupt(lambda data: data["exact_triple_universe"].clear())
    corrupt(lambda data: data.update(canonical_anchor=None))
    corrupt(lambda data: data["claims"].update(
        local_asymmetric_candidate_response_complete=1
    ))
    corrupt(lambda data: data["claims"].update(all_n_proved_by_checker=1))
    corrupt(lambda data: data.update(manifest_sha256="0" * 64))

    require(rejected == 10, "mutation rejection census drift")
    return rejected


def self_test() -> dict[str, Any]:
    return {
        **validate_contract(),
        **exhaustive_domain_regression(),
        **composition_regression(),
        "rejected_mutations": mutation_tests(),
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the asymmetric residual host after a forced labelled triple.

A conditioned required-prefix context contains a compatible labelled triple in
all states. Removing that triple leaves layer-specific row and column domains,
the inherited deleted/required edges, and opposite-layer blockers at the
prescribed physical cells. The restriction/adjoin maps are exact inverses.

Because three labelled edges are removed from a two-layer saturated state, the
residual state cardinality is odd and the two layer matching sizes are unequal.
It therefore cannot be a standard equal-layer square host. This checker records
the exact asymmetric host instead. It does not prove global context generation,
recurrence termination, or the all-n conjecture.
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
    context_family,
    exact_context,
    exact_prescription,
    generate_exact_triple_universe,
)

EXPECTED_CONTRACT_SHA256 = "fcc593f5812912d031ed90ab37e0fae105a35302a48b757f3fe69a7e80a0403b"


class ResidualHostContractionError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ResidualHostContractionError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_conditioned_inputs(
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[Iterable[int]],
) -> tuple[tuple[Edge, ...], tuple[Edge, ...], Triple]:
    deleted, required = exact_context(n, deleted_raw, required_raw)
    prescription = exact_prescription(n, prescription_raw)
    require(
        set(prescription) <= set(required),
        "forced prescription must be contained in the required context",
    )
    family = context_family(n, deleted, required)
    require(family, "conditioned context must contain a feasible state")
    return deleted, required, prescription


def surviving_domains(
    n: int,
    prescription: Triple,
) -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    domains: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for layer in (0, 1):
        part = tuple(edge for edge in prescription if edge[0] == layer)
        removed_rows = {edge[1] for edge in part}
        removed_columns = {edge[2] for edge in part}
        rows = tuple(row for row in range(n) if row not in removed_rows)
        columns = tuple(column for column in range(n) if column not in removed_columns)
        require(
            len(rows) == len(columns),
            f"layer {layer}: surviving row/column sizes differ",
        )
        domains.append((rows, columns))
    return tuple(domains)


def transported_context(
    n: int,
    deleted: tuple[Edge, ...],
    required: tuple[Edge, ...],
    prescription: Triple,
) -> dict[str, Any]:
    domains = surviving_domains(n, prescription)
    residual_deleted: set[Edge] = set()
    for edge in deleted:
        layer, row, column = edge
        rows, columns = domains[layer]
        if row in rows and column in columns:
            residual_deleted.add(edge)

    blockers: set[Edge] = set()
    for layer, row, column in prescription:
        opposite = 1 - layer
        rows, columns = domains[opposite]
        blocker = (opposite, row, column)
        if row in rows and column in columns:
            blockers.add(blocker)
            residual_deleted.add(blocker)

    residual_required = tuple(sorted(set(required) - set(prescription)))
    require(
        set(residual_deleted).isdisjoint(residual_required),
        "transported deleted and required edges intersect",
    )
    for edge in residual_required:
        layer, row, column = edge
        rows, columns = domains[layer]
        require(
            row in rows and column in columns,
            "transported required edge lies outside its surviving domain",
        )

    return {
        "domains": domains,
        "deleted": tuple(sorted(residual_deleted)),
        "required": residual_required,
        "opposite_layer_blockers": tuple(sorted(blockers)),
    }


def generate_residual_family(
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[Iterable[int]],
) -> tuple[State, ...]:
    deleted, required, prescription = exact_conditioned_inputs(
        n, deleted_raw, required_raw, prescription_raw
    )
    transport = transported_context(n, deleted, required, prescription)
    domains = transport["domains"]
    residual_deleted = set(transport["deleted"])
    residual_required = set(transport["required"])

    layer_states: list[list[tuple[Edge, ...]]] = []
    for layer in (0, 1):
        rows, columns = domains[layer]
        required_layer = {edge for edge in residual_required if edge[0] == layer}
        candidates: list[tuple[Edge, ...]] = []
        for image in permutations(columns):
            state = tuple(
                (layer, rows[index], image[index])
                for index in range(len(rows))
            )
            if residual_deleted.isdisjoint(state) and required_layer <= set(state):
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


def exact_residual_manifest(
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    deleted, required, prescription = exact_conditioned_inputs(
        n, deleted_raw, required_raw, prescription_raw
    )
    parent = context_family(n, deleted, required)
    transport = transported_context(n, deleted, required, prescription)
    residual = generate_residual_family(n, deleted, required, prescription)
    prescription_set = set(prescription)

    restricted = tuple(sorted(
        tuple(edge for edge in state if edge not in prescription_set)
        for state in parent
    ))
    require(
        restricted == residual,
        "restriction map does not equal the generated asymmetric residual family",
    )
    adjoined = tuple(sorted(
        tuple(sorted(state + prescription))
        for state in residual
    ))
    require(adjoined == parent, "adjoin map is not inverse to restriction")

    parent_universe = generate_exact_triple_universe(parent)
    residual_universe = generate_exact_triple_universe(residual)
    expected_residual_universe = tuple(
        triple
        for triple in parent_universe
        if set(triple).isdisjoint(prescription_set)
    )
    require(
        residual_universe == expected_residual_universe,
        "residual triple universe is not the exact disjoint restriction",
    )

    domains = transport["domains"]
    layer_counts = tuple(
        sum(edge[0] == layer for edge in prescription)
        for layer in (0, 1)
    )
    matching_sizes = tuple(len(domains[layer][0]) for layer in (0, 1))
    require(sum(layer_counts) == 3, "forced prescription size drift")
    require(layer_counts[0] != layer_counts[1],
            "odd prescription unexpectedly balanced across layers")
    require(matching_sizes[0] != matching_sizes[1],
            "residual layer matching sizes unexpectedly equal")
    require(sum(matching_sizes) == 2 * n - 3,
            "residual state cardinality drift")
    require(all(len(state) == 2 * n - 3 for state in residual),
            "residual state has wrong cardinality")

    domain_records = [
        {
            "layer": layer,
            "rows": list(domains[layer][0]),
            "columns": list(domains[layer][1]),
            "matching_size": matching_sizes[layer],
        }
        for layer in (0, 1)
    ]
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-asymmetric-residual-host-contraction-v1",
        "side": n,
        "parent_deleted_edges": [list(edge) for edge in deleted],
        "parent_required_edges": [list(edge) for edge in required],
        "forced_prescription": [list(edge) for edge in prescription],
        "prescription_layer_counts": list(layer_counts),
        "residual_layer_domains": domain_records,
        "transported_deleted_edges": [
            list(edge) for edge in transport["deleted"]
        ],
        "transported_required_edges": [
            list(edge) for edge in transport["required"]
        ],
        "opposite_layer_blockers": [
            list(edge) for edge in transport["opposite_layer_blockers"]
        ],
        "parent_conditioned_family": [
            [list(edge) for edge in state] for state in parent
        ],
        "residual_family": [
            [list(edge) for edge in state] for state in residual
        ],
        "residual_triple_universe": [
            [list(edge) for edge in triple] for triple in residual_universe
        ],
        "canonical_residual_anchor": (
            None if not residual else [list(edge) for edge in residual[0]]
        ),
        "claims": {
            "parent_feasible_states": len(parent),
            "residual_feasible_states": len(residual),
            "parent_state_cardinality": 2 * n,
            "residual_state_cardinality": 2 * n - 3,
            "layer_zero_residual_matching_size": matching_sizes[0],
            "layer_one_residual_matching_size": matching_sizes[1],
            "surviving_layer_domains_generated": 1,
            "opposite_layer_blockers_exact": 1,
            "deleted_required_transport_exact": 1,
            "restriction_adjoin_bijection": 1,
            "residual_triple_universe_generated": 1,
            "triple_universe_disjoint_restriction_exact": 1,
            "original_grid_coordinates_preserved": 1,
            "residual_layer_sizes_unequal": 1,
            "standard_equal_layer_square_host_representability": 0,
            "asymmetric_residual_host_generated": 1,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["manifest_sha256"] = digest(result)
    return result


def validate_residual_manifest(
    manifest: Any,
    n: int,
    deleted_raw: Iterable[Iterable[int]],
    required_raw: Iterable[Iterable[int]],
    prescription_raw: Iterable[Iterable[int]],
) -> dict[str, int]:
    expected = exact_residual_manifest(
        n, deleted_raw, required_raw, prescription_raw
    )
    require(isinstance(manifest, dict) and manifest == expected,
            "asymmetric residual manifest mismatch")
    return copy.deepcopy(expected["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "canonical-asymmetric-residual-host-contraction-v1",
        "source_theorems": [
            "CMR864", "CMR868", "CMR2799", "CMR2840", "CMR2841",
            "CMR2845", "CMR2847", "CMR2848", "CMR2849",
        ],
        "residual_host_semantics": {
            "layer_domains": "independent surviving row and column sets",
            "layer_state": "perfect matching on each surviving domain pair",
            "cross_layer_constraint": "physical-cell disjointness",
            "prescribed_cell_effect": "opposite-layer blocker edge",
            "geometry": "original integer grid coordinates retained",
        },
        "claims": {
            "surviving_layer_domains_generated": 1,
            "opposite_layer_blockers_exact": 1,
            "deleted_required_transport_exact": 1,
            "restriction_adjoin_bijection": 1,
            "residual_triple_universe_generated": 1,
            "triple_universe_disjoint_restriction_exact": 1,
            "triple_contraction_residual_cardinality_odd": 1,
            "residual_layer_sizes_unequal": 1,
            "standard_equal_layer_square_host_representability": 0,
            "asymmetric_residual_host_generated": 1,
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


def scenario_census(
    n: int,
    maximum_deleted_size: int,
    maximum_extra_required: int,
) -> dict[str, int]:
    host = all_host_edges(n)
    seen: set[tuple[Any, ...]] = set()
    scenarios = parent_occurrences = residual_occurrences = 0
    residual_triples = blockers = 0
    layer_distributions = {"3+0": 0, "2+1": 0, "1+2": 0, "0+3": 0}

    for deleted_size in range(maximum_deleted_size + 1):
        for deleted in combinations(host, deleted_size):
            unrestricted = context_family(n, deleted, ())
            for state in unrestricted:
                state_universe = generate_exact_triple_universe((state,))
                for prescription in state_universe:
                    remaining = tuple(
                        edge for edge in state if edge not in set(prescription)
                    )
                    for extra_size in range(maximum_extra_required + 1):
                        for extra in combinations(remaining, extra_size):
                            required = tuple(sorted(prescription + extra))
                            key = (deleted, required, prescription)
                            if key in seen:
                                continue
                            seen.add(key)
                            manifest = exact_residual_manifest(
                                n, deleted, required, prescription
                            )
                            claims = manifest["claims"]
                            scenarios += 1
                            parent_occurrences += claims["parent_feasible_states"]
                            residual_occurrences += claims["residual_feasible_states"]
                            residual_triples += len(
                                manifest["residual_triple_universe"]
                            )
                            blockers += len(manifest["opposite_layer_blockers"])
                            counts = manifest["prescription_layer_counts"]
                            layer_distributions[f"{counts[0]}+{counts[1]}"] += 1

    return {
        "scenarios": scenarios,
        "parent_state_occurrences": parent_occurrences,
        "residual_state_occurrences": residual_occurrences,
        "residual_triples": residual_triples,
        "opposite_layer_blockers": blockers,
        "prescription_distribution_3_plus_0": layer_distributions["3+0"],
        "prescription_distribution_2_plus_1": layer_distributions["2+1"],
        "prescription_distribution_1_plus_2": layer_distributions["1+2"],
        "prescription_distribution_0_plus_3": layer_distributions["0+3"],
    }


def exhaustive_regression() -> dict[str, int]:
    side_three = scenario_census(3, 1, 1)
    side_four = scenario_census(4, 0, 1)
    require(
        side_three == {
            "scenarios": 376,
            "parent_state_occurrences": 416,
            "residual_state_occurrences": 416,
            "residual_triples": 0,
            "opposite_layer_blockers": 1128,
            "prescription_distribution_3_plus_0": 188,
            "prescription_distribution_2_plus_1": 0,
            "prescription_distribution_1_plus_2": 0,
            "prescription_distribution_0_plus_3": 188,
        },
        "side-three residual census drift",
    )
    require(
        side_four == {
            "scenarios": 1056,
            "parent_state_occurrences": 2592,
            "residual_state_occurrences": 2592,
            "residual_triples": 1904,
            "opposite_layer_blockers": 3168,
            "prescription_distribution_3_plus_0": 168,
            "prescription_distribution_2_plus_1": 360,
            "prescription_distribution_1_plus_2": 360,
            "prescription_distribution_0_plus_3": 168,
        },
        "side-four residual census drift",
    )
    return {
        **{f"side_three_{key}": value for key, value in side_three.items()},
        **{f"side_four_{key}": value for key, value in side_four.items()},
    }


def mutation_tests() -> int:
    n = 4
    family = context_family(n, (), ())
    state, prescription, manifest = next(
        (state, triple, candidate)
        for state in family
        for triple in generate_exact_triple_universe((state,))
        if sum(edge[0] == 0 for edge in triple) == 2
        for candidate in (exact_residual_manifest(n, (), triple, triple),)
        if candidate["residual_triple_universe"]
    )
    required = prescription
    rejected = 0

    malformed = [
        lambda: exact_residual_manifest(n, (), (), prescription),
        lambda: exact_residual_manifest(
            n, (), tuple(reversed(required)), prescription
        ),
        lambda: exact_residual_manifest(
            n, (), required, tuple(reversed(prescription))
        ),
        lambda: exact_residual_manifest(
            n, ((0, 0, 0),), tuple(sorted(required + ((0, 0, 0),))),
            prescription,
        ),
    ]
    for call in malformed:
        try:
            call()
        except (ValueError, StopIteration):
            rejected += 1
        else:
            raise ResidualHostContractionError("malformed contraction input accepted")

    def corrupted(mutator: Any) -> None:
        nonlocal rejected
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        try:
            validate_residual_manifest(candidate, n, (), required, prescription)
        except ResidualHostContractionError:
            rejected += 1
        else:
            raise ResidualHostContractionError("corrupted residual manifest accepted")

    corrupted(lambda data: data["opposite_layer_blockers"].pop())
    corrupted(lambda data: data["residual_family"].pop())
    corrupted(lambda data: data["residual_triple_universe"].clear())
    corrupted(lambda data: data["claims"].update(
        standard_equal_layer_square_host_representability=1
    ))
    corrupted(lambda data: data["claims"].update(all_n_proved_by_checker=1))
    corrupted(lambda data: data.update(manifest_sha256="0" * 64))

    require(rejected == 10, "mutation rejection census drift")
    return rejected


def self_test() -> dict[str, Any]:
    return {
        **validate_contract(),
        **exhaustive_regression(),
        "rejected_mutations": mutation_tests(),
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()

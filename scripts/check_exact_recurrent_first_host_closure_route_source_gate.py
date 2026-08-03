#!/usr/bin/env python3
"""Compile source-backed closure-route obligations for the first residual host."""

from __future__ import annotations

import argparse
import copy
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
STATES = ("00", "01", "10", "11")
MENUS = {
    "00": "blocked",
    "01": "restore_20",
    "10": "restore_02",
    "11": "restore_both",
}
SELECTED = {
    "00": "3012",
    "01": "3201",
    "10": "2031",
    "11": "2031",
}
UNDIRECTED = (("00", "01"), ("00", "10"), ("01", "11"), ("10", "11"))
ROUTE_ORDER = (
    "physical_exclusion",
    "terminal_or_improving_output",
    "bounded_strict_potential",
    "finite_unrestorable_capacity",
    "decorated_outer_reset",
)

CONTRACTS = (
    {
        "path": "docs/alternating-core-builder-state-boundary-gates.md",
        "blob_sha": "33ee792692a52d232dd71e3cde48ea8573ba78df",
        "checker_path": "scripts/verify_ac_builder_state_boundary_gates.py",
        "checker_blob_sha": "acebfb7fa66e6fdf7a390cde5aec42b2ecd47f0b",
        "contract": "exact normalized false-to-true gate plus exclusion, terminal output, bounded potential, finite unrestorable capacity, or higher outer reset",
        "first_host_values_populated": 0,
        "checker_uses_synthetic_parameter_families": 1,
    },
    {
        "path": "docs/alternating-core-physical-source-capacity-overload.md",
        "blob_sha": "022c24a9004d330cf84a149540eaf86a28390342",
        "checker_path": "scripts/verify_ac_physical_source_capacity_overload.py",
        "checker_blob_sha": "b88c477aafb01c089ac3fb72920f5edf09154563",
        "contract": "finite occurrence-faithful atom capacities and exact overload tickets",
        "first_host_values_populated": 0,
        "checker_uses_synthetic_parameter_families": 1,
    },
    {
        "path": "docs/alternating-core-source-capacity-recreation-ledger.md",
        "blob_sha": "20890501500cb1212a5cd0cdd8a32a48fdf609a9",
        "checker_path": "scripts/verify_ac_source_capacity_recreation.py",
        "checker_blob_sha": "d0fe04a9752f1cd523fcf27d28948de0a41a5e5e",
        "contract": "capacity recreation charged to finite nonreplenishing exact source stock",
        "first_host_values_populated": 0,
        "checker_uses_synthetic_parameter_families": 1,
    },
    {
        "path": "docs/alternating-core-outer-reset-quotient.md",
        "blob_sha": "4ef671f294392b3ff31a48dd516f9e7759535b3c",
        "checker_path": "scripts/verify_ac_outer_reset_quotient.py",
        "checker_blob_sha": "852601f0e0309660d8bf8e8c506872eaf50cf432",
        "contract": "first decorated outer edge is finite progress; repetition requires ticket, payment, bounded descent, or terminal output",
        "first_host_values_populated": 0,
        "checker_uses_synthetic_parameter_families": 1,
    },
)

ROUTE_CONTRACTS = {
    "physical_exclusion": {
        "base_physical_fields": (
            "physical_source_ref",
            "legal_operations",
            "realization_status",
        ),
        "route_specific_fields": (
            "exact_edge_ref",
            "exclusion_proof_ref",
        ),
        "acceptance": "exact directed edge is source-proved impossible for the physical occurrence",
    },
    "terminal_or_improving_output": {
        "base_physical_fields": (
            "physical_source_ref",
            "provenance.owner",
            "legal_operations",
            "intermediate_states",
            "child_row",
            "positive_weights",
            "parent_budget",
            "realization_status",
        ),
        "route_specific_fields": (
            "outcome_kind",
            "outcome_proof_ref",
        ),
        "acceptance": "exact legal edge has a source-backed terminal or improving output",
    },
    "bounded_strict_potential": {
        "base_physical_fields": (
            "physical_source_ref",
            "provenance.owner",
            "legal_operations",
            "intermediate_states",
            "positive_weights",
            "parent_budget",
            "realization_status",
        ),
        "route_specific_fields": (
            "potential_ref",
            "source_value",
            "target_value",
            "bounded_range_ref",
        ),
        "acceptance": "source value is strictly greater than target value in one proved bounded potential",
    },
    "finite_unrestorable_capacity": {
        "base_physical_fields": (
            "physical_source_ref",
            "provenance.owner",
            "legal_operations",
            "intermediate_states",
            "realization_status",
        ),
        "route_specific_fields": (
            "capacity_address",
            "initial_capacity",
            "debit_rule_ref",
            "nonrestoration_ref",
        ),
        "acceptance": "every traversal debits one exact finite capacity unit which cannot be restored in the closure epoch",
    },
    "decorated_outer_reset": {
        "base_physical_fields": (
            "physical_source_ref",
            "legal_operations",
            "intermediate_states",
            "realization_status",
        ),
        "route_specific_fields": (
            "source_outer_profile_ref",
            "target_outer_profile_ref",
            "decoration_ref",
            "repetition_route_ref",
        ),
        "acceptance": "edge changes a reconstructed outer profile and every repetition is separately ticketed, paid, descending, or terminal",
    },
}


class ClosureRouteError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ClosureRouteError(message)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ClosureRouteError("unable to locate repository root")


def hamming(first: str, second: str) -> int:
    return sum(a != b for a, b in zip(first, second))


def bit_flipped(source: str, target: str) -> str:
    require(hamming(source, target) == 1, "single-bit edge")
    return "r02" if source[0] != target[0] else "r20"


def action(source: str, target: str) -> str:
    index = 0 if bit_flipped(source, target) == "r02" else 1
    return "restore" if source[index] == "0" and target[index] == "1" else "delete"


def directed_edges() -> list[tuple[str, str]]:
    return sorted(
        [(a, b) for a, b in UNDIRECTED] + [(b, a) for a, b in UNDIRECTED]
    )


def is_acyclic(vertices: tuple[str, ...], edges: set[tuple[str, str]]) -> bool:
    incoming = {vertex: 0 for vertex in vertices}
    outgoing = {vertex: [] for vertex in vertices}
    for source, target in edges:
        incoming[target] += 1
        outgoing[source].append(target)
    queue = [vertex for vertex in vertices if incoming[vertex] == 0]
    seen = 0
    while queue:
        source = queue.pop()
        seen += 1
        for target in outgoing[source]:
            incoming[target] -= 1
            if incoming[target] == 0:
                queue.append(target)
    return seen == len(vertices)


def menu_route_covers() -> list[frozenset[tuple[str, str]]]:
    covers: set[frozenset[tuple[str, str]]] = set()
    for order in itertools.permutations(STATES):
        rank = {state: index for index, state in enumerate(order)}
        paid = {
            (a, b) if rank[a] > rank[b] else (b, a)
            for a, b in UNDIRECTED
        }
        require(is_acyclic(STATES, paid), "paid menu orientation")
        residual = frozenset((target, source) for source, target in paid)
        covers.add(residual)
    require(len(covers) == 14, "menu route-cover census")
    return sorted(covers, key=lambda rows: sorted(f"{a}->{b}" for a, b in rows))


def label_route_covers() -> list[frozenset[tuple[str, str]]]:
    changing = {
        edge for edge in directed_edges()
        if SELECTED[edge[0]] != SELECTED[edge[1]]
    }
    covers: set[frozenset[tuple[str, str]]] = set()
    labels = tuple(sorted(set(SELECTED.values())))
    for order in itertools.permutations(labels):
        rank = {label: index for index, label in enumerate(order)}
        paid = {
            edge for edge in changing
            if rank[SELECTED[edge[0]]] > rank[SELECTED[edge[1]]]
        }
        residual = frozenset(changing - paid)
        require(len(paid) == len(residual) == 3, "label route split")
        covers.add(residual)
    require(len(covers) == 6, "label route-cover census")
    return sorted(covers, key=lambda rows: sorted(f"{a}->{b}" for a, b in rows))


def build_manifest(root: Path) -> dict[str, Any]:
    coverage = load_json(
        root / "data/exact_recurrent_first_host_physical_source_coverage.json"
    )
    route_cover = load_json(
        root / "data/exact_recurrent_first_host_scalar_route_cover.json"
    )

    require(coverage["aggregate"]["required_physical_fields"] == 16, "physical field count")
    require(coverage["aggregate"]["source_backed_physical_fields"] == 0, "physical coverage")
    physical_status = {
        row["field"]: int(row["physical_populated"])
        for row in coverage["field_coverage"]
    }
    require(len(physical_status) == 16, "physical field status map")
    require(set(physical_status.values()) == {0}, "all physical fields unpopulated")

    aggregate = route_cover["aggregate"]
    require(aggregate["selected_label_scalar_compatible_route_covers"] == 6, "label covers")
    require(aggregate["menu_scalar_compatible_route_covers"] == 14, "menu covers")
    require(aggregate["selected_label_minimum_external_routes"] == 3, "label residual count")
    require(aggregate["menu_minimum_external_routes"] == 4, "menu residual count")

    edges = []
    for source, target in directed_edges():
        changing = SELECTED[source] != SELECTED[target]
        route_rows = []
        for route in ROUTE_ORDER:
            contract = ROUTE_CONTRACTS[route]
            base = list(contract["base_physical_fields"])
            missing_base = [field for field in base if physical_status.get(field, 0) == 0]
            route_specific = list(contract["route_specific_fields"])
            route_rows.append(
                {
                    "route": route,
                    "base_physical_fields": base,
                    "missing_base_physical_fields": missing_base,
                    "route_specific_fields": route_specific,
                    "route_specific_fields_populated": 0,
                    "source_admissible": 0,
                    "acceptance": contract["acceptance"],
                }
            )
        edges.append(
            {
                "edge": f"{source}->{target}",
                "source_state": source,
                "target_state": target,
                "source_menu": MENUS[source],
                "target_menu": MENUS[target],
                "source_selected_response": SELECTED[source],
                "target_selected_response": SELECTED[target],
                "selector_changing": int(changing),
                "selector_neutral": int(not changing),
                "bit_flipped": bit_flipped(source, target),
                "action": action(source, target),
                "candidate_normalized_gate_address": 1,
                "physical_legal_edge_proved": 0,
                "persistent_owner_token_populated": 0,
                "source_admissible_route_count": 0,
                "routes": route_rows,
            }
        )

    label_covers = label_route_covers()
    menu_covers = menu_route_covers()
    edge_frequency_label = Counter(edge for cover in label_covers for edge in cover)
    edge_frequency_menu = Counter(edge for cover in menu_covers for edge in cover)
    changing_edges = {
        edge for edge in directed_edges()
        if SELECTED[edge[0]] != SELECTED[edge[1]]
    }
    require(set(edge_frequency_label) == changing_edges, "label cover edge support")
    require(set(edge_frequency_menu) == set(directed_edges()), "menu cover edge support")
    require(set(edge_frequency_label.values()) == {3}, "label edge frequency")
    require(set(edge_frequency_menu.values()) == {7}, "menu edge frequency")

    base_field_union = sorted(
        set().union(
            *(set(contract["base_physical_fields"]) for contract in ROUTE_CONTRACTS.values())
        )
    )
    route_specific_union = sorted(
        set().union(
            *(set(contract["route_specific_fields"]) for contract in ROUTE_CONTRACTS.values())
        )
    )

    return {
        "schema": "exact-recurrent-first-host-closure-route-source-gate/v1",
        "scope": {
            "host_id": HOST_ID,
            "states": [
                {
                    "state": state,
                    "menu": MENUS[state],
                    "selected_response": SELECTED[state],
                }
                for state in STATES
            ],
            "route_classes": list(ROUTE_ORDER),
        },
        "alternating_core_contracts": list(CONTRACTS),
        "route_contracts": [
            {
                "route": route,
                **{
                    key: list(value) if isinstance(value, tuple) else value
                    for key, value in ROUTE_CONTRACTS[route].items()
                },
            }
            for route in ROUTE_ORDER
        ],
        "edges": edges,
        "cover_obligations": {
            "label_scalar": {
                "compatible_covers": 6,
                "paid_selector_edges_per_cover": 3,
                "residual_selector_edges_per_cover": 3,
                "distinct_exact_capacity_addresses_if_capacity_only": 3,
                "shared_capacity_reduction_requires_separate_theorem": 1,
                "edge_residual_frequency_across_covers": {
                    f"{a}->{b}": edge_frequency_label[(a, b)]
                    for a, b in sorted(edge_frequency_label)
                },
            },
            "menu_scalar": {
                "compatible_covers": 14,
                "paid_menu_edges_per_cover": 4,
                "residual_menu_edges_per_cover": 4,
                "residual_selector_changing_edges_per_cover": 3,
                "residual_selector_neutral_edges_per_cover": 1,
                "distinct_exact_capacity_addresses_if_capacity_only": 4,
                "shared_capacity_reduction_requires_separate_theorem": 1,
                "edge_residual_frequency_across_covers": {
                    f"{a}->{b}": edge_frequency_menu[(a, b)]
                    for a, b in sorted(edge_frequency_menu)
                },
            },
        },
        "conditional_budget_formulas": {
            "capacity_only_residual_traversals": "sum_{e in residual cover} initial_capacity(e)",
            "source_paid_capacity_recreation": "sum_a rho_a * source_stock_a(0)",
            "decorated_outer_reset_first_traversals": "number of distinct decorated outer edges",
            "decorated_outer_reset_repetitions": "sum of macro-ticket capacities plus separately bounded descent/payment events",
        },
        "aggregate": {
            "directed_menu_edges": 8,
            "selector_changing_edges": 6,
            "selector_neutral_edges": 2,
            "route_classes": 5,
            "edge_route_pairs": 40,
            "candidate_normalized_gate_addresses": 8,
            "physical_legal_edges_proved": 0,
            "persistent_owner_tokens_populated": 0,
            "source_admissible_edge_route_pairs": 0,
            "edges_with_at_least_one_source_admissible_route": 0,
            "base_physical_route_fields": len(base_field_union),
            "source_backed_base_physical_route_fields": sum(
                physical_status.get(field, 0) for field in base_field_union
            ),
            "route_specific_fields": len(route_specific_union),
            "source_backed_route_specific_fields": 0,
            "alternating_contracts_audited": len(CONTRACTS),
            "alternating_contracts_with_first_host_values": 0,
            "synthetic_contract_checkers": len(CONTRACTS),
        },
        "conclusion": {
            "finite_route_classification_complete": 1,
            "symbolic_menu_edges_have_normalized_candidate_addresses": 1,
            "alternating_contracts_supply_acceptance_rules": 1,
            "alternating_contracts_supply_first_host_route_values": 0,
            "one_capacity_address_can_pay_multiple_distinct_edges_without_shared_capacity_theorem": 0,
            "first_outer_reset_traversal_alone_closes_repeated_edge": 0,
            "physical_route_assignment_complete": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_chart_confinement_proved": 0,
            "physical_occurrence_coverage_proved": 0,
            "physical_transition_legality_proved": 0,
            "persistent_owner_identity_proved": 0,
            "boundary_capacities_populated": 0,
            "outer_profile_mapping_populated": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate_manifest(manifest: dict[str, Any]) -> None:
    require(manifest.get("schema") == "exact-recurrent-first-host-closure-route-source-gate/v1", "schema")
    aggregate = manifest["aggregate"]
    expected = {
        "directed_menu_edges": 8,
        "selector_changing_edges": 6,
        "selector_neutral_edges": 2,
        "route_classes": 5,
        "edge_route_pairs": 40,
        "candidate_normalized_gate_addresses": 8,
        "physical_legal_edges_proved": 0,
        "persistent_owner_tokens_populated": 0,
        "source_admissible_edge_route_pairs": 0,
        "edges_with_at_least_one_source_admissible_route": 0,
        "alternating_contracts_audited": 4,
        "alternating_contracts_with_first_host_values": 0,
        "synthetic_contract_checkers": 4,
    }
    for key, value in expected.items():
        require(aggregate.get(key) == value, f"aggregate {key}")
    require(aggregate["base_physical_route_fields"] >= 8, "base route fields")
    require(aggregate["source_backed_base_physical_route_fields"] == 0, "base source coverage")
    require(aggregate["route_specific_fields"] >= 12, "route-specific fields")
    require(aggregate["source_backed_route_specific_fields"] == 0, "route-specific coverage")

    require(len(manifest["edges"]) == 8, "edge rows")
    for edge in manifest["edges"]:
        require(edge["candidate_normalized_gate_address"] == 1, "candidate gate")
        require(edge["physical_legal_edge_proved"] == 0, "physical edge")
        require(edge["persistent_owner_token_populated"] == 0, "owner token")
        require(edge["source_admissible_route_count"] == 0, "admissible routes")
        require(len(edge["routes"]) == 5, "route row count")
        for route in edge["routes"]:
            require(route["source_admissible"] == 0, "route admitted")
            require(route["route_specific_fields_populated"] == 0, "route-specific population")
            require(bool(route["missing_base_physical_fields"]), "missing base fields")

    label = manifest["cover_obligations"]["label_scalar"]
    require(label["compatible_covers"] == 6, "label cover count")
    require(label["residual_selector_edges_per_cover"] == 3, "label residual")
    require(label["distinct_exact_capacity_addresses_if_capacity_only"] == 3, "label capacity addresses")
    require(set(label["edge_residual_frequency_across_covers"].values()) == {3}, "label frequency")

    menu = manifest["cover_obligations"]["menu_scalar"]
    require(menu["compatible_covers"] == 14, "menu cover count")
    require(menu["residual_menu_edges_per_cover"] == 4, "menu residual")
    require(menu["residual_selector_changing_edges_per_cover"] == 3, "menu changing residual")
    require(menu["residual_selector_neutral_edges_per_cover"] == 1, "menu neutral residual")
    require(menu["distinct_exact_capacity_addresses_if_capacity_only"] == 4, "menu capacity addresses")
    require(set(menu["edge_residual_frequency_across_covers"].values()) == {7}, "menu frequency")

    for contract in manifest["alternating_core_contracts"]:
        require(len(contract["blob_sha"]) == 40, "contract sha")
        require(contract["first_host_values_populated"] == 0, "contract first-host values")
        require(contract["checker_uses_synthetic_parameter_families"] == 1, "synthetic checker")

    conclusion = manifest["conclusion"]
    require(conclusion["finite_route_classification_complete"] == 1, "route classification")
    require(conclusion["symbolic_menu_edges_have_normalized_candidate_addresses"] == 1, "candidate addresses")
    require(conclusion["alternating_contracts_supply_acceptance_rules"] == 1, "acceptance rules")
    for key in (
        "alternating_contracts_supply_first_host_route_values",
        "one_capacity_address_can_pay_multiple_distinct_edges_without_shared_capacity_theorem",
        "first_outer_reset_traversal_alone_closes_repeated_edge",
        "physical_route_assignment_complete",
        "promotion_to_recurrent_closure_allowed",
    ):
        require(conclusion[key] == 0, f"conclusion {key}")

    for key, value in manifest["honesty"].items():
        require(value == 0, f"honesty {key}")


def mutation_audit(manifest: dict[str, Any]) -> int:
    mutations = [
        lambda x: x["aggregate"].update(directed_menu_edges=7),
        lambda x: x["aggregate"].update(edge_route_pairs=39),
        lambda x: x["aggregate"].update(physical_legal_edges_proved=1),
        lambda x: x["aggregate"].update(source_admissible_edge_route_pairs=1),
        lambda x: x["aggregate"].update(alternating_contracts_with_first_host_values=1),
        lambda x: x["edges"][0].update(source_admissible_route_count=1),
        lambda x: x["edges"][0]["routes"][0].update(source_admissible=1),
        lambda x: x["edges"][0]["routes"][0].update(route_specific_fields_populated=1),
        lambda x: x["cover_obligations"]["label_scalar"].update(distinct_exact_capacity_addresses_if_capacity_only=2),
        lambda x: x["cover_obligations"]["menu_scalar"].update(residual_selector_neutral_edges_per_cover=0),
        lambda x: x["cover_obligations"]["menu_scalar"]["edge_residual_frequency_across_covers"].update({"00->01": 6}),
        lambda x: x["conclusion"].update(alternating_contracts_supply_first_host_route_values=1),
        lambda x: x["conclusion"].update(one_capacity_address_can_pay_multiple_distinct_edges_without_shared_capacity_theorem=1),
        lambda x: x["conclusion"].update(first_outer_reset_traversal_alone_closes_repeated_edge=1),
        lambda x: x["conclusion"].update(promotion_to_recurrent_closure_allowed=1),
        lambda x: x["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate_manifest(candidate)
        except ClosureRouteError:
            rejected += 1
    require(rejected == len(mutations), "mutation accepted")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()

    root = repository_root()
    manifest = build_manifest(root)
    validate_manifest(manifest)

    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if args.check:
        require(load_json(args.check) == manifest, "manifest mismatch")

    print(
        json.dumps(
            {
                "checker": "exact-recurrent-first-host-closure-route-source-gate",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(manifest),
                **manifest["conclusion"],
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

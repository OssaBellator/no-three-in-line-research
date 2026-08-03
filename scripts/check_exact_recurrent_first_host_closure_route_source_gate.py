#!/usr/bin/env python3
"""Audit source-backed closure routes for the first residual host."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from collections import Counter
from pathlib import Path

HOST = "s4-75b04c45c1c8eac2"
STATES = ("00", "01", "10", "11")
MENUS = {"00": "blocked", "01": "restore_20", "10": "restore_02", "11": "restore_both"}
SELECTED = {"00": "3012", "01": "3201", "10": "2031", "11": "2031"}
UNDIRECTED = (("00", "01"), ("00", "10"), ("01", "11"), ("10", "11"))
ROUTES = {
    "physical_exclusion": {
        "base": ["physical_source_ref", "legal_operations", "realization_status"],
        "specific": ["exact_edge_ref", "exclusion_proof_ref"],
    },
    "terminal_or_improving_output": {
        "base": ["physical_source_ref", "provenance.owner", "legal_operations",
                 "intermediate_states", "child_row", "positive_weights",
                 "parent_budget", "realization_status"],
        "specific": ["outcome_kind", "outcome_proof_ref"],
    },
    "bounded_strict_potential": {
        "base": ["physical_source_ref", "provenance.owner", "legal_operations",
                 "intermediate_states", "positive_weights", "parent_budget",
                 "realization_status"],
        "specific": ["potential_ref", "source_value", "target_value", "bounded_range_ref"],
    },
    "finite_unrestorable_capacity": {
        "base": ["physical_source_ref", "provenance.owner", "legal_operations",
                 "intermediate_states", "realization_status"],
        "specific": ["capacity_address", "initial_capacity", "debit_rule_ref", "nonrestoration_ref"],
    },
    "decorated_outer_reset": {
        "base": ["physical_source_ref", "legal_operations", "intermediate_states",
                 "realization_status"],
        "specific": ["source_outer_profile_ref", "target_outer_profile_ref",
                     "decoration_ref", "repetition_route_ref"],
    },
}
CONTRACTS = [
    ["docs/alternating-core-builder-state-boundary-gates.md",
     "33ee792692a52d232dd71e3cde48ea8573ba78df",
     "scripts/verify_ac_builder_state_boundary_gates.py",
     "acebfb7fa66e6fdf7a390cde5aec42b2ecd47f0b"],
    ["docs/alternating-core-physical-source-capacity-overload.md",
     "022c24a9004d330cf84a149540eaf86a28390342",
     "scripts/verify_ac_physical_source_capacity_overload.py",
     "b88c477aafb01c089ac3fb72920f5edf09154563"],
    ["docs/alternating-core-source-capacity-recreation-ledger.md",
     "20890501500cb1212a5cd0cdd8a32a48fdf609a9",
     "scripts/verify_ac_source_capacity_recreation.py",
     "d0fe04a9752f1cd523fcf27d28948de0a41a5e5e"],
    ["docs/alternating-core-outer-reset-quotient.md",
     "4ef671f294392b3ff31a48dd516f9e7759535b3c",
     "scripts/verify_ac_outer_reset_quotient.py",
     "852601f0e0309660d8bf8e8c506872eaf50cf432"],
]


class GateError(RuntimeError):
    pass


def need(ok: bool, message: str) -> None:
    if not ok:
        raise GateError(message)


def root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here.parent, *here.parents):
        if (candidate / "STATUS.md").is_file():
            return candidate
    raise GateError("repository root not found")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def edges() -> list[tuple[str, str]]:
    return sorted([(a, b) for a, b in UNDIRECTED] + [(b, a) for a, b in UNDIRECTED])


def bit(edge: tuple[str, str]) -> str:
    source, target = edge
    return "r02" if source[0] != target[0] else "r20"


def action(edge: tuple[str, str]) -> str:
    source, target = edge
    index = 0 if bit(edge) == "r02" else 1
    return "restore" if source[index] == "0" else "delete"


def label_covers() -> list[frozenset[tuple[str, str]]]:
    changing = {edge for edge in edges() if SELECTED[edge[0]] != SELECTED[edge[1]]}
    out = set()
    for order in itertools.permutations(sorted(set(SELECTED.values()))):
        rank = {label: index for index, label in enumerate(order)}
        paid = {edge for edge in changing
                if rank[SELECTED[edge[0]]] > rank[SELECTED[edge[1]]]}
        out.add(frozenset(changing - paid))
    need(len(out) == 6, "label cover count")
    return sorted(out, key=lambda cover: sorted(cover))


def menu_covers() -> list[frozenset[tuple[str, str]]]:
    out = set()
    for order in itertools.permutations(STATES):
        rank = {state: index for index, state in enumerate(order)}
        paid = {(a, b) if rank[a] > rank[b] else (b, a) for a, b in UNDIRECTED}
        out.add(frozenset((b, a) for a, b in paid))
    need(len(out) == 14, "menu cover count")
    return sorted(out, key=lambda cover: sorted(cover))


def compile_manifest(repo: Path) -> dict:
    coverage = load(repo / "data/exact_recurrent_first_host_physical_source_coverage.json")
    scalar = load(repo / "data/exact_recurrent_first_host_scalar_route_cover.json")
    need(coverage["aggregate"]["source_backed_physical_fields"] == 0, "coverage changed")
    populated = {row["field"]: row["physical_populated"] for row in coverage["field_coverage"]}
    need(len(populated) == 16 and not any(populated.values()), "physical fields changed")
    need(scalar["aggregate"]["selected_label_scalar_compatible_route_covers"] == 6, "label scalar")
    need(scalar["aggregate"]["menu_scalar_compatible_route_covers"] == 14, "menu scalar")

    directed = edges()
    label = label_covers()
    menu = menu_covers()
    label_frequency = Counter(edge for cover in label for edge in cover)
    menu_frequency = Counter(edge for cover in menu for edge in cover)
    need(set(label_frequency.values()) == {3}, "label edge frequency")
    need(set(menu_frequency.values()) == {7}, "menu edge frequency")

    base_union = sorted({field for route in ROUTES.values() for field in route["base"]})
    specific_union = sorted({field for route in ROUTES.values() for field in route["specific"]})
    edge_rows = []
    for source, target in directed:
        edge_rows.append({
            "edge": f"{source}->{target}",
            "source_menu": MENUS[source],
            "target_menu": MENUS[target],
            "source_selected": SELECTED[source],
            "target_selected": SELECTED[target],
            "selector_changing": int(SELECTED[source] != SELECTED[target]),
            "bit": bit((source, target)),
            "action": action((source, target)),
            "candidate_normalized_gate": 1,
            "physical_legal_edge": 0,
            "persistent_owner_token": 0,
            "route_admissibility": {route: 0 for route in ROUTES},
        })

    return {
        "schema": "exact-recurrent-first-host-closure-route-source-gate/v1",
        "scope": {
            "host_id": HOST,
            "states": [{"state": state, "menu": MENUS[state], "selected": SELECTED[state]}
                       for state in STATES],
        },
        "alternating_core_contracts": [
            {"document": doc, "document_blob_sha": dsha, "checker": checker,
             "checker_blob_sha": csha, "synthetic_parameter_check": 1,
             "first_host_values_populated": 0}
            for doc, dsha, checker, csha in CONTRACTS
        ],
        "route_contracts": [
            {"route": name, "base_physical_fields": row["base"],
             "route_specific_fields": row["specific"],
             "base_fields_populated": 0, "route_specific_fields_populated": 0}
            for name, row in ROUTES.items()
        ],
        "edges": edge_rows,
        "cover_obligations": {
            "label_scalar": {
                "compatible_covers": 6,
                "residual_edges_per_cover": 3,
                "distinct_capacity_addresses_if_capacity_only": 3,
                "residual_frequency": {f"{a}->{b}": label_frequency[(a, b)]
                                       for a, b in sorted(label_frequency)},
            },
            "menu_scalar": {
                "compatible_covers": 14,
                "residual_edges_per_cover": 4,
                "residual_selector_changing": 3,
                "residual_selector_neutral": 1,
                "distinct_capacity_addresses_if_capacity_only": 4,
                "residual_frequency": {f"{a}->{b}": menu_frequency[(a, b)]
                                       for a, b in sorted(menu_frequency)},
            },
        },
        "conditional_budgets": {
            "capacity_only": "sum_{e in residual cover} initial_capacity(e)",
            "source_paid_recreation": "sum_a rho_a*source_stock_a(0)",
            "outer_first_traversals": "number of distinct decorated outer edges",
            "outer_repetitions": "macro-ticket stock plus separately bounded descent/payment events",
        },
        "aggregate": {
            "directed_edges": 8,
            "selector_changing_edges": 6,
            "selector_neutral_edges": 2,
            "route_classes": 5,
            "edge_route_pairs": 40,
            "candidate_normalized_gates": 8,
            "physical_legal_edges": 0,
            "persistent_owner_tokens": 0,
            "source_admissible_edge_route_pairs": 0,
            "edges_with_route": 0,
            "base_route_fields": len(base_union),
            "source_backed_base_route_fields": sum(populated.get(field, 0) for field in base_union),
            "route_specific_fields": len(specific_union),
            "source_backed_route_specific_fields": 0,
            "contracts_audited": 4,
            "contracts_with_first_host_values": 0,
        },
        "conclusion": {
            "finite_route_classification_complete": 1,
            "alternating_contracts_supply_acceptance_rules": 1,
            "alternating_contracts_supply_first_host_values": 0,
            "shared_capacity_reduction_without_theorem": 0,
            "first_outer_reset_alone_closes_repetition": 0,
            "physical_route_assignment_complete": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
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


def mutation_audit(manifest: dict) -> int:
    mutations = [
        lambda x: x["aggregate"].update(directed_edges=7),
        lambda x: x["aggregate"].update(edge_route_pairs=39),
        lambda x: x["aggregate"].update(physical_legal_edges=1),
        lambda x: x["aggregate"].update(source_admissible_edge_route_pairs=1),
        lambda x: x["edges"][0].update(physical_legal_edge=1),
        lambda x: x["edges"][0]["route_admissibility"].update(physical_exclusion=1),
        lambda x: x["cover_obligations"]["label_scalar"].update(
            distinct_capacity_addresses_if_capacity_only=2),
        lambda x: x["cover_obligations"]["menu_scalar"].update(residual_selector_neutral=0),
        lambda x: x["conclusion"].update(alternating_contracts_supply_first_host_values=1),
        lambda x: x["conclusion"].update(first_outer_reset_alone_closes_repetition=1),
        lambda x: x["conclusion"].update(promotion_to_recurrent_closure_allowed=1),
        lambda x: x["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            need(candidate == compile_manifest(root()), "corruption")
        except GateError:
            rejected += 1
    need(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    manifest = compile_manifest(root())
    if args.write:
        args.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                             encoding="utf-8")
    if args.check:
        need(load(args.check) == manifest, "checked manifest mismatch")
    print(json.dumps({"checker": "closure-route-source-gate",
                      **manifest["aggregate"],
                      "mutation_corruptions_rejected": mutation_audit(manifest),
                      **manifest["conclusion"],
                      **manifest["honesty"]}, sort_keys=True))


if __name__ == "__main__":
    main()

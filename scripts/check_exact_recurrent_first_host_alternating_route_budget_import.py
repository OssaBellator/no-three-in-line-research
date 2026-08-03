#!/usr/bin/env python3
"""Compile the exact alternating-core route-budget import for the first residual host."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path

State = tuple[int, int]
Edge = tuple[State, State]

HOST_ID = "s4-75b04c45c1c8eac2"
STATES: tuple[State, ...] = ((0, 0), (0, 1), (1, 0), (1, 1))
SELECTED = {(0, 0): "3012", (0, 1): "3201", (1, 0): "2031", (1, 1): "2031"}
MENUS = {(0, 0): "blocked", (0, 1): "restore_20", (1, 0): "restore_02", (1, 1): "restore_both"}

UPSTREAM = (
    {
        "role": "normalized_builder_boundary_capacity",
        "doc_path": "docs/alternating-core-builder-state-boundary-gates.md",
        "doc_blob_sha": "33ee792692a52d232dd71e3cde48ea8573ba78df",
        "script_path": "scripts/verify_ac_builder_state_boundary_gates.py",
        "script_blob_sha": "acebfb7fa66e6fdf7a390cde5aec42b2ecd47f0b",
        "contract": "exact gate address plus finite unrestorable capacity, or another registered route",
        "validator_kind": "synthetic finite state/predicate/graph/ticket enumeration",
    },
    {
        "role": "source_paid_capacity_recreation",
        "doc_path": "docs/alternating-core-source-capacity-recreation-ledger.md",
        "doc_blob_sha": "20890501500cb1212a5cd0cdd8a32a48fdf609a9",
        "script_path": "scripts/verify_ac_source_capacity_recreation.py",
        "script_blob_sha": "d0fe04a9752f1cd523fcf27d28948de0a41a5e5e",
        "contract": "fixed atom universe, finite source addresses/rates/counters, and occurrence-faithful assignment of every positive capacity increment",
        "validator_kind": "synthetic exhaustive vectors plus seeded random histories",
    },
    {
        "role": "physical_capacity_overload",
        "doc_path": "docs/alternating-core-physical-source-capacity-overload.md",
        "doc_blob_sha": "022c24a9004d330cf84a149540eaf86a28390342",
        "script_path": "scripts/verify_ac_physical_source_capacity_overload.py",
        "script_blob_sha": "b88c477aafb01c089ac3fb72920f5edf09154563",
        "contract": "fixed occurrence-faithful atom capacities and finite crossing/loss/conservative ticket stocks",
        "validator_kind": "generic finite capacity and occupancy audit",
    },
    {
        "role": "outer_reset_repetition",
        "doc_path": "docs/alternating-core-outer-reset-quotient.md",
        "doc_blob_sha": "4ef671f294392b3ff31a48dd516f9e7759535b3c",
        "script_path": "scripts/verify_ac_outer_reset_quotient.py",
        "script_blob_sha": "852601f0e0309660d8bf8e8c506872eaf50cf432",
        "contract": "finite outer profiles/decorations; first decorated edge is progress and every repeat needs a macro ticket, another strict potential, payment, or terminal output",
        "validator_kind": "synthetic profile/edge/ticket parameter sweep",
    },
)


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def state_code(state: State) -> str:
    return f"{state[0]}{state[1]}"


def edge_code(edge: Edge) -> str:
    return f"{state_code(edge[0])}->{state_code(edge[1])}"


def reverse(edge: Edge) -> Edge:
    return edge[1], edge[0]


def hamming(first: State, second: State) -> int:
    return sum(a != b for a, b in zip(first, second))


def changed_bit(edge: Edge) -> str:
    require(hamming(*edge) == 1, "single-bit edge required")
    return "r02" if edge[0][0] != edge[1][0] else "r20"


def operation_direction(edge: Edge) -> str:
    index = 0 if changed_bit(edge) == "r02" else 1
    return "restore" if edge[0][index] == 0 else "delete"


def paid_from_order(order: tuple[State, ...], undirected: tuple[Edge, ...]) -> frozenset[Edge]:
    rank = {state: index for index, state in enumerate(order)}
    return frozenset(
        (first, second) if rank[first] > rank[second] else (second, first)
        for first, second in undirected
    )


def parallel_reversal_profile(paid: frozenset[Edge]) -> dict[str, bool]:
    pairs = {
        "r02": (((0, 0), (1, 0)), ((0, 1), (1, 1))),
        "r20": (((0, 0), (0, 1)), ((1, 0), (1, 1))),
    }
    result: dict[str, bool] = {}
    for bit, bit_pairs in pairs.items():
        directions = []
        for first, second in bit_pairs:
            if (first, second) in paid:
                directions.append("restore")
            elif (second, first) in paid:
                directions.append("delete")
            else:
                raise AuditError("missing paid orientation")
        result[bit] = directions[0] != directions[1]
    return result


def compile_manifest() -> dict[str, object]:
    undirected = tuple(
        (first, second)
        for index, first in enumerate(STATES)
        for second in STATES[index + 1 :]
        if hamming(first, second) == 1
    )
    directed = {orientation for edge in undirected for orientation in (edge, reverse(edge))}
    require((len(undirected), len(directed)) == (4, 8), "restoration square census")

    orientation_orders: dict[frozenset[Edge], list[tuple[State, ...]]] = defaultdict(list)
    for order in itertools.permutations(STATES):
        orientation_orders[paid_from_order(order, undirected)].append(order)
    require(len(orientation_orders) == 14, "acyclic orientation census")

    route_rows = []
    restore_distribution: Counter[int] = Counter()
    interaction_restore_cross: Counter[tuple[str, int]] = Counter()
    constant_profiles = set()

    for paid, orders in sorted(
        orientation_orders.items(),
        key=lambda item: sorted(edge_code(edge) for edge in item[0]),
    ):
        residual = frozenset(reverse(edge) for edge in paid)
        reversal = parallel_reversal_profile(paid)
        interaction_required = any(reversal.values())
        residual_restore = sum(operation_direction(edge) == "restore" for edge in residual)
        residual_delete = 4 - residual_restore
        residual_changing = sum(SELECTED[edge[0]] != SELECTED[edge[1]] for edge in residual)
        residual_neutral = 4 - residual_changing
        residual_r02 = sum(changed_bit(edge) == "r02" for edge in residual)
        residual_r20 = 4 - residual_r02
        target_counts = Counter(
            SELECTED[edge[1]]
            for edge in residual
            if SELECTED[edge[0]] != SELECTED[edge[1]]
        )

        require((residual_changing, residual_neutral) == (3, 1), "changing-neutral invariant")
        require((residual_r02, residual_r20) == (2, 2), "bit-family invariant")
        constant_profiles.add((residual_changing, residual_neutral, residual_r02, residual_r20))
        restore_distribution[residual_restore] += 1
        interaction_restore_cross[
            ("interaction" if interaction_required else "additive", residual_restore)
        ] += 1

        route_rows.append(
            {
                "paid_edges": sorted(edge_code(edge) for edge in paid),
                "residual_route_edges": sorted(edge_code(edge) for edge in residual),
                "strict_menu_orders_low_to_high": [
                    [state_code(state) for state in order]
                    for order in sorted(orders)
                ],
                "residual_profile": {
                    "restore": residual_restore,
                    "delete": residual_delete,
                    "r02": residual_r02,
                    "r20": residual_r20,
                    "selector_changing": residual_changing,
                    "selector_neutral": residual_neutral,
                    "selected_target_counts": dict(sorted(target_counts.items())),
                },
                "parallel_reversal_profile": reversal,
                "interaction_required": int(interaction_required),
                "minimum_integer_abs_gamma": 2 if interaction_required else 0,
            }
        )

    require(len(constant_profiles) == 1, "constant coarse route profile")
    require(
        restore_distribution == Counter({0: 1, 1: 4, 2: 4, 3: 4, 4: 1}),
        "operation-direction distribution",
    )
    require(
        interaction_restore_cross
        == Counter(
            {
                ("additive", 0): 1,
                ("additive", 2): 2,
                ("additive", 4): 1,
                ("interaction", 1): 4,
                ("interaction", 2): 2,
                ("interaction", 3): 4,
            }
        ),
        "interaction-direction cross table",
    )

    for restore_cost in range(8):
        for delete_cost in range(8):
            for interaction_penalty in range(8):
                costs = []
                for row in route_rows:
                    profile = row["residual_profile"]
                    cost = (
                        restore_cost * profile["restore"]
                        + delete_cost * profile["delete"]
                        + interaction_penalty * row["interaction_required"]
                    )
                    costs.append((cost, row["interaction_required"]))
                minimum = min(cost for cost, _ in costs)
                require(
                    any(cost == minimum and interaction == 0 for cost, interaction in costs),
                    "additive optimum for aggregate direction cost",
                )

    all_directed = sorted(directed, key=edge_code)
    for row in route_rows:
        residual_codes = set(row["residual_route_edges"])
        costs = {edge_code(edge): (0 if edge_code(edge) in residual_codes else 1) for edge in all_directed}
        row_costs = [
            (
                sum(costs[code] for code in candidate["residual_route_edges"]),
                candidate["residual_route_edges"],
            )
            for candidate in route_rows
        ]
        minimum = min(cost for cost, _ in row_costs)
        minimizers = [codes for cost, codes in row_costs if cost == minimum]
        require(minimum == 0 and minimizers == [row["residual_route_edges"]], "edge-sensitive unique optimum")

    missing_fields = [
        "persistent_owner_token",
        "legal_normalized_transition_edges",
        "direct_gate_capacities",
        "capacity_atom_universe",
        "capacity_source_addresses",
        "capacity_conversion_rates",
        "capacity_source_initial_counters",
        "capacity_increment_assignments",
        "physical_occurrence_capacities",
        "overload_crossing_tickets",
        "outer_profile_dictionary",
        "outer_edge_decorations",
        "internal_epoch_bound",
        "macro_ticket_stock",
        "source_backed_menu_potential_values",
        "registered_residual_route_assignment",
    ]

    return {
        "schema": "exact-recurrent-first-host-alternating-route-budget-import/v1",
        "scope": {
            "host_id": HOST_ID,
            "states": [
                {
                    "state": state_code(state),
                    "menu": MENUS[state],
                    "selected_response": SELECTED[state],
                }
                for state in STATES
            ],
            "upstream_branch": "research/alternating-core-chain",
            "audit_branch": "research/exact-recurrent-lyapunov-audit",
        },
        "upstream_contracts": list(UPSTREAM),
        "source_nonpromotion": {
            "upstream_validators_with_first_host_records": 0,
            "upstream_validators_with_first_host_owner_tokens": 0,
            "upstream_validators_with_first_host_capacity_values": 0,
            "upstream_validators_with_first_host_macro_tickets": 0,
            "validator_inputs_are_generic_or_synthetic": 1,
        },
        "menu_scalar_route_covers": route_rows,
        "aggregate": {
            "directed_menu_edges": len(directed),
            "distinct_scalar_compatible_menu_covers": len(route_rows),
            "residual_edges_per_cover": 4,
            "residual_selector_changing_per_cover": 3,
            "residual_selector_neutral_per_cover": 1,
            "residual_r02_per_cover": 2,
            "residual_r20_per_cover": 2,
            "residual_restore_distribution": {
                str(key): restore_distribution[key] for key in range(5)
            },
            "additive_covers": sum(not row["interaction_required"] for row in route_rows),
            "interaction_required_covers": sum(row["interaction_required"] for row in route_rows),
            "interaction_restore_cross_table": {
                f"{kind}:restore_{restore}": interaction_restore_cross[(kind, restore)]
                for kind in ("additive", "interaction")
                for restore in range(5)
                if interaction_restore_cross[(kind, restore)]
            },
            "required_physical_import_fields": len(missing_fields),
            "populated_physical_import_fields": 0,
            "complete_route_contracts": 0,
        },
        "conditional_budget_formulae": {
            "finite_gate_capacity": {
                "formula": "N_cap <= C0 + H_cap",
                "definitions": {
                    "C0": "sum of initial exact residual-gate capacities",
                    "H_cap": "sum_a rho_a*s_a(0), the source-faithful capacity-recreation budget",
                    "N_cap": "total charged episodes routed through those exact capacities",
                },
                "hypotheses": [
                    "every charged episode consumes one unit at its exact normalized gate address",
                    "every positive capacity increment is occurrence-faithfully source assigned",
                    "no unregistered atom, rate, source address, or payment decoration enters the epoch",
                ],
            },
            "outer_reset_ticket": {
                "formula": "N_out <= E_first + Q",
                "definitions": {
                    "E_first": "number of distinct decorated residual outer edges traversed",
                    "Q": "finite capacity-one macro-ticket stock consumed by repeated decorated edges",
                    "N_out": "total residual episodes routed as outer resets",
                },
                "hypotheses": [
                    "every symbolic residual edge has a source-backed decorated outer-edge address",
                    "each first decorated traversal is counted once",
                    "every repeated decorated traversal consumes a new macro ticket or closes by another registered route",
                ],
            },
        },
        "missing_physical_import_fields": missing_fields,
        "conclusion": {
            "alternating_core_capacity_and_reset_contracts_exact": 1,
            "contracts_supply_first_host_values": 0,
            "coarse_bit_or_selector_profile_distinguishes_menu_covers": 0,
            "operation_direction_profile_distinguishes_menu_covers": 1,
            "direction_only_nonnegative_cost_has_additive_optimum": 1,
            "interaction_can_be_forced_by_exact_edge_sensitive_costs": 1,
            "finite_gate_budget_formula_installed_conditionally": 1,
            "outer_reset_ticket_formula_installed_conditionally": 1,
            "physical_route_contract_installed": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_chart_confinement_proved": 0,
            "physical_occurrence_coverage_proved": 0,
            "physical_transition_legality_proved": 0,
            "persistent_owner_identity_proved": 0,
            "boundary_capacities_populated": 0,
            "outer_macro_tickets_populated": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from exact compiler")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(distinct_scalar_compatible_menu_covers=13),
        lambda item: item["aggregate"].update(residual_selector_neutral_per_cover=0),
        lambda item: item["aggregate"].update(residual_r02_per_cover=1),
        lambda item: item["aggregate"]["residual_restore_distribution"].update({"2": 5}),
        lambda item: item["aggregate"].update(additive_covers=5),
        lambda item: item["aggregate"].update(interaction_required_covers=9),
        lambda item: item["aggregate"].update(populated_physical_import_fields=1),
        lambda item: item["source_nonpromotion"].update(upstream_validators_with_first_host_records=1),
        lambda item: item["menu_scalar_route_covers"].pop(),
        lambda item: item["missing_physical_import_fields"].pop(),
        lambda item: item["conditional_budget_formulae"]["finite_gate_capacity"].update(formula="N_cap <= C0"),
        lambda item: item["conditional_budget_formulae"]["outer_reset_ticket"].update(formula="N_out <= Q"),
        lambda item: item["conclusion"].update(direction_only_nonnegative_cost_has_additive_optimum=0),
        lambda item: item["conclusion"].update(physical_route_contract_installed=1),
        lambda item: item["conclusion"].update(promotion_to_recurrent_closure_allowed=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate)
        except (AuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    manifest = compile_manifest()
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.check:
        validate(json.loads(args.check.read_text(encoding="utf-8")))
    print(json.dumps({
        "checker": "exact-recurrent-first-host-alternating-route-budget-import",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()

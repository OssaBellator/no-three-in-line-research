#!/usr/bin/env python3
"""Compile symbolic selected-response boundary gates on the two-bit restoration cube."""
from __future__ import annotations

import argparse
import copy
import json
from itertools import combinations, product
from pathlib import Path

State = tuple[int, int]

HOST_ID = "s4-75b04c45c1c8eac2"
STATE_NAMES: dict[State, str] = {
    (0, 0): "blocked",
    (1, 0): "restore_02",
    (0, 1): "restore_20",
    (1, 1): "restore_both",
}
SELECTED: dict[State, str] = {
    (0, 0): "3012",
    (1, 0): "2031",
    (0, 1): "3201",
    (1, 1): "2031",
}
RESPONSES = ("3012", "2031", "3201")


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def code(state: State) -> str:
    return f"{state[0]}{state[1]}"


def hamming(first: State, second: State) -> int:
    return sum(a != b for a, b in zip(first, second))


def changed_bit(first: State, second: State) -> str:
    require(hamming(first, second) == 1, "single-bit transition required")
    return "r02" if first[0] != second[0] else "r20"


def predicate(response: str, state: State) -> bool:
    return SELECTED[state] == response


def compile_manifest() -> dict[str, object]:
    states = tuple(sorted(STATE_NAMES))
    directed_single_bit = tuple(
        (source, target)
        for source, target in product(states, repeat=2)
        if hamming(source, target) == 1
    )
    require(len(directed_single_bit) == 8, "two-cube directed edge census")

    arbitrary_gates: dict[str, list[tuple[State, State]]] = {}
    single_bit_gates: dict[str, list[tuple[State, State]]] = {}
    for response in RESPONSES:
        arbitrary = [
            (source, target)
            for source, target in product(states, repeat=2)
            if source != target
            and not predicate(response, source)
            and predicate(response, target)
        ]
        local = [pair for pair in arbitrary if hamming(*pair) == 1]
        arbitrary_gates[response] = sorted(arbitrary)
        single_bit_gates[response] = sorted(local)

    require(
        {response: len(rows) for response, rows in arbitrary_gates.items()}
        == {"3012": 3, "2031": 4, "3201": 3},
        "arbitrary boundary stock",
    )
    require(
        {response: len(rows) for response, rows in single_bit_gates.items()}
        == {"3012": 2, "2031": 2, "3201": 2},
        "single-bit boundary stock",
    )

    changing = [
        (source, target)
        for source, target in directed_single_bit
        if SELECTED[source] != SELECTED[target]
    ]
    neutral = [
        (source, target)
        for source, target in directed_single_bit
        if SELECTED[source] == SELECTED[target]
    ]
    require(len(changing) == 6, "changing edge census")
    require(len(neutral) == 2, "neutral edge census")
    require(
        set(changing)
        == {
            pair
            for rows in single_bit_gates.values()
            for pair in rows
        },
        "changing edges equal target-label recreation gates",
    )
    require(
        neutral == [((1, 0), (1, 1)), ((1, 1), (1, 0))],
        "neutral edge identity",
    )

    changing_by_bit = {
        bit: sum(changed_bit(source, target) == bit for source, target in changing)
        for bit in ("r02", "r20")
    }
    require(changing_by_bit == {"r02": 4, "r20": 2}, "changing-bit census")

    label_edges = {
        (SELECTED[source], SELECTED[target])
        for source, target in changing
    }
    complete_bidirected = {
        (source, target)
        for source, target in product(RESPONSES, repeat=2)
        if source != target
    }
    require(label_edges == complete_bidirected, "complete bidirected label graph")
    bidirected_pairs = tuple(sorted(tuple(sorted(pair)) for pair in combinations(RESPONSES, 2)))
    require(len(bidirected_pairs) == 3, "label two-cycle census")

    maximum_label_descent_edges = len(bidirected_pairs)
    minimum_label_other_route_edges = len(label_edges) - maximum_label_descent_edges
    context_bidirected_pairs = len(directed_single_bit) // 2
    maximum_context_descent_edges = context_bidirected_pairs
    minimum_context_other_route_edges = len(directed_single_bit) - maximum_context_descent_edges
    require(maximum_label_descent_edges == 3, "maximum label descent edge count")
    require(minimum_label_other_route_edges == 3, "minimum label other-route count")
    require(context_bidirected_pairs == 4, "context two-cycle count")
    require(maximum_context_descent_edges == 4, "maximum context descent edge count")
    require(minimum_context_other_route_edges == 4, "minimum context other-route count")

    gate_rows = []
    for response in RESPONSES:
        for source, target in single_bit_gates[response]:
            gate_rows.append(
                {
                    "response": response,
                    "source": code(source),
                    "source_menu": STATE_NAMES[source],
                    "target": code(target),
                    "target_menu": STATE_NAMES[target],
                    "changed_bit": changed_bit(source, target),
                    "bit_direction": "0->1" if sum(target) > sum(source) else "1->0",
                }
            )

    return {
        "schema": "exact-recurrent-first-host-selector-boolean-boundary/v3",
        "scope": {
            "host_id": HOST_ID,
            "context_bits": [
                "r02=1 iff deletion edge 02 is restored",
                "r20=1 iff deletion edge 20 is restored",
            ],
            "selector_rule": "lexicographically least complete-score minimizer on the chart-safe class",
            "symbolic_selected_responses": list(RESPONSES),
        },
        "menu_states": [
            {
                "state": code(state),
                "menu": STATE_NAMES[state],
                "selected_response": SELECTED[state],
            }
            for state in states
        ],
        "predicates": {
            "3012": "not r02 and not r20",
            "2031": "r02",
            "3201": "not r02 and r20",
        },
        "single_bit_recreation_gates": gate_rows,
        "selector_neutral_single_bit_edges": [
            {
                "source": code(source),
                "source_menu": STATE_NAMES[source],
                "target": code(target),
                "target_menu": STATE_NAMES[target],
                "selected_response": SELECTED[source],
                "changed_bit": changed_bit(source, target),
            }
            for source, target in neutral
        ],
        "selected_label_transition_graph": {
            "vertices": list(RESPONSES),
            "directed_edges": [
                {"source": source, "target": target}
                for source, target in sorted(label_edges)
            ],
            "bidirected_pairs": [list(pair) for pair in bidirected_pairs],
            "strongly_connected_components": [list(RESPONSES)],
            "maximum_edges_payable_by_strict_label_descent": maximum_label_descent_edges,
            "minimum_edges_requiring_non_label_descent_route": minimum_label_other_route_edges,
        },
        "menu_transition_graph": {
            "directed_edges": len(directed_single_bit),
            "bidirected_pairs": context_bidirected_pairs,
            "maximum_edges_payable_by_strict_menu_descent": maximum_context_descent_edges,
            "minimum_edges_requiring_non_menu_descent_route": minimum_context_other_route_edges,
        },
        "aggregate": {
            "context_bits": 2,
            "menu_states": len(states),
            "symbolic_selected_response_labels": len(RESPONSES),
            "directed_single_bit_context_edges": len(directed_single_bit),
            "context_bidirected_pairs": context_bidirected_pairs,
            "selector_changing_single_bit_edges": len(changing),
            "selector_neutral_single_bit_edges": len(neutral),
            "exact_single_bit_recreation_gates": sum(map(len, single_bit_gates.values())),
            "exact_arbitrary_transition_recreation_gates": sum(map(len, arbitrary_gates.values())),
            "generic_single_bit_gate_bound_three_labels": len(RESPONSES) * 2 * 2,
            "generic_arbitrary_gate_bound_three_labels": len(RESPONSES) * 4,
            "changing_edges_flipping_r02": changing_by_bit["r02"],
            "changing_edges_flipping_r20": changing_by_bit["r20"],
            "selected_label_transition_edges": len(label_edges),
            "selected_label_bidirected_pairs": len(bidirected_pairs),
            "selected_label_strongly_connected_components": 1,
            "largest_selected_label_scc": len(RESPONSES),
            "maximum_selected_label_edges_payable_by_strict_descent": maximum_label_descent_edges,
            "minimum_selector_edges_requiring_other_route": minimum_label_other_route_edges,
            "maximum_menu_edges_payable_by_strict_descent": maximum_context_descent_edges,
            "minimum_menu_edges_requiring_other_route": minimum_context_other_route_edges,
        },
        "conclusion": {
            "selected_response_predicates_exact_on_safe_class": 1,
            "single_bit_selector_recreation_stock_exact": 1,
            "exact_single_bit_stock_improves_generic_bound": 1,
            "two_selector_neutral_menu_edges_identified": 1,
            "selected_label_transition_graph_complete_bidirected": 1,
            "strict_selected_label_potential_exists_on_all_six_edges": 0,
            "strict_menu_state_potential_exists_on_all_eight_edges": 0,
            "at_least_three_selector_edges_need_non_label_descent_route": 1,
            "at_least_four_menu_edges_need_non_menu_descent_route": 1,
            "alternating_core_boolean_boundary_interface_applicable_symbolically": 1,
            "physical_owner_token_identification_proved": 0,
            "physical_transition_legality_proved": 0,
            "boundary_capacities_populated": 0,
            "promotion_to_recurrent_closure_allowed": 0,
        },
        "honesty": {
            "physical_chart_confinement_proved": 0,
            "physical_occurrence_coverage_proved": 0,
            "legal_operations_populated": 0,
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
        lambda item: item["aggregate"].update(menu_states=3),
        lambda item: item["aggregate"].update(selector_changing_single_bit_edges=5),
        lambda item: item["aggregate"].update(selector_neutral_single_bit_edges=3),
        lambda item: item["aggregate"].update(exact_single_bit_recreation_gates=5),
        lambda item: item["aggregate"].update(exact_arbitrary_transition_recreation_gates=9),
        lambda item: item["aggregate"].update(changing_edges_flipping_r02=3),
        lambda item: item["aggregate"].update(selected_label_transition_edges=5),
        lambda item: item["aggregate"].update(selected_label_bidirected_pairs=2),
        lambda item: item["aggregate"].update(minimum_selector_edges_requiring_other_route=2),
        lambda item: item["aggregate"].update(minimum_menu_edges_requiring_other_route=3),
        lambda item: item["predicates"].update({"2031": "r20"}),
        lambda item: item["single_bit_recreation_gates"].pop(),
        lambda item: item["selector_neutral_single_bit_edges"].pop(),
        lambda item: item["selected_label_transition_graph"]["directed_edges"].pop(),
        lambda item: item["conclusion"].update(strict_selected_label_potential_exists_on_all_six_edges=1),
        lambda item: item["conclusion"].update(strict_menu_state_potential_exists_on_all_eight_edges=1),
        lambda item: item["conclusion"].update(physical_owner_token_identification_proved=1),
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
    arguments = parser.parse_args()
    manifest = compile_manifest()

    if arguments.write:
        arguments.write.parent.mkdir(parents=True, exist_ok=True)
        arguments.write.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if arguments.check:
        validate(json.loads(arguments.check.read_text(encoding="utf-8")))

    print(
        json.dumps(
            {
                "checker": "exact-recurrent-first-host-selector-boolean-boundary",
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

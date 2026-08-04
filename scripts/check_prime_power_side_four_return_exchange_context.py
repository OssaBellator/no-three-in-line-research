#!/usr/bin/env python3
"""Compile and validate exact side-four returned-edge exchange and rank-three return context."""
from __future__ import annotations
import copy, hashlib, json
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any

class ReturnExchangeContextError(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ReturnExchangeContextError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
CONTRACT_PATH = "data/prime_power_side_four_return_exchange_context_contract.json"
EXPECTED_SELECTED_SHA256 = "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_CONTRACT_SHA256 = "0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b"
EXPECTED_COMPILED_CONTEXT_ROW_SHA256 = "fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea"

def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ReturnExchangeContextError("unable to locate repository root")

def collinear(first: tuple[int, int], second: tuple[int, int], third: tuple[int, int]) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )

def source_cycle_lengths(selector: str) -> dict[int, int]:
    require(len(selector) == 4 and set(selector) == set("0123"), f"{selector}: response permutation")
    permutation = [int(value) for value in selector]
    seen: set[int] = set()
    lengths: dict[int, int] = {}
    for start in range(4):
        if start in seen:
            continue
        cycle: list[int] = []
        current = start
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current = permutation[current]
        require(len(cycle) in {2, 4}, f"{selector}: derangement cycle length")
        for source in cycle:
            lengths[source] = len(cycle)
    require(set(lengths) == set(range(4)), f"{selector}: cycle coverage")
    return lengths

def compile_rows(selected: dict[str, Any]) -> list[dict[str, Any]]:
    require(digest(selected) == EXPECTED_SELECTED_SHA256, "selected-response manifest digest")
    rows: list[dict[str, Any]] = []
    for host in selected.get("hosts", []):
        require(isinstance(host, list) and len(host) == 8, "selected host row")
        host_id, selector, _face, minimum, _gap, fate, _blockers, collision = host
        cycle_lengths = source_cycle_lengths(selector)
        exchanges = []
        for source in range(4):
            alternating_cycle_length = 2 * cycle_lengths[source]
            returned_edge = f"{source}{source}"
            entering_edge = f"{source}{selector[source]}"
            exchange_class = f"src{source}:ret{returned_edge}:ent{entering_edge}:alt{alternating_cycle_length}"
            exchanges.append([source, returned_edge, entering_edge, alternating_cycle_length, exchange_class])

        selected_edges = tuple((source, int(selector[source])) for source in range(4))
        charges: Counter[tuple[tuple[int, int], int, int]] = Counter()
        owned_credits = []
        for triple in combinations(sorted(selected_edges), 3):
            if not collinear(*triple):
                continue
            owner = max(triple)
            predecessor = (owner[0], owner[0])
            matching_cycle_length = cycle_lengths[owner[0]]
            charges[(predecessor, 0, matching_cycle_length)] += 1
            owned_credits.append([
                ",".join(f"{source}{target}" for source, target in triple),
                f"{owner[0]}{owner[1]}",
                f"{predecessor[0]}{predecessor[1]}",
                matching_cycle_length,
            ])

        charge_rows = [
            [f"{predecessor[0]}{predecessor[1]}", old_overlap, cycle_length, count]
            for (predecessor, old_overlap, cycle_length), count in sorted(charges.items())
        ]
        require(sum(entry[3] for entry in charge_rows) == minimum, f"{host_id}: rank-three credit count")
        rows.append({
            "host_id": host_id,
            "selected_response": selector,
            "fate": "zero-response" if fate == "Z" else "blocker-alternative",
            "collision_key": collision,
            "exchanges": exchanges,
            "rank_three_kernel": {
                "recreated_credit_count": minimum,
                "charges": charge_rows,
                "owned_credits": owned_credits,
            },
        })
    return rows

def expected_contract() -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-return-exchange-context-contract/v2",
        "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
        "compiled_return_context_row_sha256": EXPECTED_COMPILED_CONTEXT_ROW_SHA256,
        "old_matching": "identity:00,11,22,33",
        "pairing_rule": "same-source returned predecessor to selected entering edge",
        "owner_rule": "lexicographically maximal entering edge in each recreated collinear triple",
        "credit_system": "collinear triples in the selected response",
        "exchange_entry_encoding": "[source,returned_edge,entering_edge,alternating_cycle_length,exchange_class]",
        "rank_three_charge_encoding": "[returned_edge,old_edge_overlap,matching_cycle_length,count]",
        "aggregate": {
            "rows": 86,
            "exchange_entries": 344,
            "alternating_cycle_length_census": {"4": 68, "8": 276},
            "host_cycle_type_census": {"two-alt4-cycles": 17, "one-alt8-cycle": 69},
            "returned_edge_census": {"00": 86, "11": 86, "22": 86, "33": 86},
            "selector_census": {"2031": 34, "2301": 15, "2310": 13, "3012": 9, "3201": 13, "3210": 2},
            "zero_response_rows": 75,
            "blocker_alternative_rows": 11,
            "rank_three_recreated_credits": 17,
            "rank_three_nonzero_kernel_entries": 13,
            "rank_three_charge_by_returned_edge": {"22": 2, "33": 15},
            "rank_three_coarse_class_census": {"old0-cycle2": 8, "old0-cycle4": 9},
            "rank_three_nonzero_rows": 11,
        },
        "honesty": {
            "return_exchange_context_complete_for_normalized_block": 1,
            "rank_three_return_kernel_complete_for_normalized_block": 1,
            "complete_return_coefficient_rule_complete": 0,
            "residual_return_credit_classes_complete": 0,
            "return_child_keys_complete": 0,
            "return_child_weights_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
    }

def validate(selected: dict[str, Any], contract: dict[str, Any]) -> list[dict[str, Any]]:
    require(contract == expected_contract(), "return-exchange contract differs from canonical schema")
    require(digest(contract) == EXPECTED_CONTRACT_SHA256, "return-exchange contract digest mismatch")
    rows = compile_rows(selected)
    require(len(rows) == 86, "return-context row count")
    require(digest(rows) == EXPECTED_COMPILED_CONTEXT_ROW_SHA256, "return-context row digest mismatch")

    alternating = Counter()
    returned = Counter()
    host_types = Counter()
    charge_edges = Counter()
    charge_classes = Counter()
    kernel_entries = 0
    recreated_credits = 0
    nonzero_rows = 0

    for row in rows:
        exchanges = row["exchanges"]
        require(len(exchanges) == 4, f"{row['host_id']}: four source exchanges")
        require({entry[0] for entry in exchanges} == set(range(4)), f"{row['host_id']}: source coverage")
        lengths = {entry[3] for entry in exchanges}
        require(lengths in ({4}, {8}), f"{row['host_id']}: uniform host cycle type")
        host_types["two-alt4-cycles" if lengths == {4} else "one-alt8-cycle"] += 1
        for source, returned_edge, entering_edge, cycle_length, exchange_class in exchanges:
            require(returned_edge == f"{source}{source}", f"{row['host_id']}: returned edge")
            require(entering_edge == f"{source}{row['selected_response'][source]}", f"{row['host_id']}: entering edge")
            require(cycle_length in {4, 8}, f"{row['host_id']}: alternating cycle length")
            require(exchange_class == f"src{source}:ret{returned_edge}:ent{entering_edge}:alt{cycle_length}", f"{row['host_id']}: exchange class")
            alternating[cycle_length] += 1
            returned[returned_edge] += 1

        kernel = row["rank_three_kernel"]
        recreated_credits += kernel["recreated_credit_count"]
        kernel_entries += len(kernel["charges"])
        nonzero_rows += bool(kernel["charges"])
        require(len(kernel["owned_credits"]) == kernel["recreated_credit_count"], f"{row['host_id']}: owned credit count")
        for returned_edge, old_overlap, matching_cycle_length, count in kernel["charges"]:
            require(returned_edge in {"00", "11", "22", "33"}, f"{row['host_id']}: rank-three returned edge")
            require(old_overlap == 0, f"{row['host_id']}: old overlap")
            require(matching_cycle_length in {2, 4}, f"{row['host_id']}: matching cycle length")
            require(isinstance(count, int) and count > 0, f"{row['host_id']}: kernel count")
            charge_edges[returned_edge] += count
            charge_classes[(old_overlap, matching_cycle_length)] += count

    require(alternating == Counter({8: 276, 4: 68}), "alternating cycle census")
    require(returned == Counter({"00": 86, "11": 86, "22": 86, "33": 86}), "returned edge census")
    require(host_types == Counter({"one-alt8-cycle": 69, "two-alt4-cycles": 17}), "host cycle type census")
    require(recreated_credits == 17, "rank-three recreated credit census")
    require(kernel_entries == 13, "rank-three kernel entry census")
    require(nonzero_rows == 11, "rank-three nonzero row census")
    require(charge_edges == Counter({"33": 15, "22": 2}), "rank-three returned-edge charge census")
    require(charge_classes == Counter({(0, 4): 9, (0, 2): 8}), "rank-three coarse class census")
    return rows

def mutation_audit(selected: dict[str, Any], contract: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(rows=85),
        lambda item: item["aggregate"].update(exchange_entries=343),
        lambda item: item.update(compiled_return_context_row_sha256="0" * 64),
        lambda item: item.update(old_matching="unknown"),
        lambda item: item.update(owner_rule="arbitrary"),
        lambda item: item.update(credit_system="all triples"),
        lambda item: item["aggregate"]["alternating_cycle_length_census"].update({"4": 67}),
        lambda item: item["aggregate"].update(rank_three_recreated_credits=16),
        lambda item: item["aggregate"]["rank_three_charge_by_returned_edge"].update({"33": 14}),
        lambda item: item["honesty"].update(complete_return_coefficient_rule_complete=1),
        lambda item: item["honesty"].update(residual_return_credit_classes_complete=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(contract)
        mutate(bad)
        try:
            validate(selected, bad)
        except ReturnExchangeContextError:
            rejected += 1
    require(rejected == len(mutations), "return-context corruption accepted")
    return rejected

def main() -> None:
    root = repository_root()
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    contract = json.loads((root / CONTRACT_PATH).read_text(encoding="utf-8"))
    rows = validate(selected, contract)
    print(json.dumps({
        "checker": "prime-power-side-four-return-exchange-context",
        "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
        "return_exchange_contract_sha256": EXPECTED_CONTRACT_SHA256,
        "compiled_return_context_row_sha256": EXPECTED_COMPILED_CONTEXT_ROW_SHA256,
        "row_count": len(rows),
        "exchange_entry_count": 344,
        "rank_three_recreated_credit_count": 17,
        "rank_three_nonzero_kernel_entry_count": 13,
        "rank_three_charge_to_returned_22": 2,
        "rank_three_charge_to_returned_33": 15,
        "rejected_corruptions": mutation_audit(selected, contract),
        "side_four_return_exchange_context_complete": 1,
        "return_exchange_context_complete_for_normalized_block": 1,
        "rank_three_return_kernel_complete_for_normalized_block": 1,
        "complete_return_coefficient_rule_complete": 0,
        "residual_return_credit_classes_complete": 0,
        "return_child_keys_complete": 0,
        "return_child_weights_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))

if __name__ == "__main__":
    main()

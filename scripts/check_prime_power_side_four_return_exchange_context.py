#!/usr/bin/env python3
"""Compile and validate exact side-four returned-edge exchange context."""
from __future__ import annotations
import copy, hashlib, json
from collections import Counter
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
EXPECTED_CONTRACT_SHA256 = "d13c5357bd54433c01148f12f2b683add5945b30e41ddf420746c2268f77033f"
EXPECTED_COMPILED_ROW_SHA256 = "0d70e367357021770cb79c30c7bfdd2322f10392356c85efd938d96349da800b"

def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ReturnExchangeContextError("unable to locate repository root")

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
        host_id, selector, _face, _minimum, _gap, fate, _blockers, collision = host
        cycle_lengths = source_cycle_lengths(selector)
        exchanges = []
        for source in range(4):
            alternating_cycle_length = 2 * cycle_lengths[source]
            returned_edge = f"{source}{source}"
            entering_edge = f"{source}{selector[source]}"
            exchange_class = f"src{source}:ret{returned_edge}:ent{entering_edge}:alt{alternating_cycle_length}"
            exchanges.append([source, returned_edge, entering_edge, alternating_cycle_length, exchange_class])
        rows.append({
            "host_id": host_id,
            "selected_response": selector,
            "fate": "zero-response" if fate == "Z" else "blocker-alternative",
            "collision_key": collision,
            "exchanges": exchanges,
        })
    return rows

def expected_contract() -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-return-exchange-context-contract/v1",
        "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
        "compiled_return_exchange_row_sha256": EXPECTED_COMPILED_ROW_SHA256,
        "old_matching": "identity:00,11,22,33",
        "pairing_rule": "same-source returned predecessor to selected entering edge",
        "exchange_entry_encoding": "[source,returned_edge,entering_edge,alternating_cycle_length,exchange_class]",
        "aggregate": {
            "rows": 86,
            "exchange_entries": 344,
            "alternating_cycle_length_census": {"4": 68, "8": 276},
            "host_cycle_type_census": {"two-alt4-cycles": 17, "one-alt8-cycle": 69},
            "returned_edge_census": {"00": 86, "11": 86, "22": 86, "33": 86},
            "selector_census": {"2031": 34, "2301": 15, "2310": 13, "3012": 9, "3201": 13, "3210": 2},
            "zero_response_rows": 75,
            "blocker_alternative_rows": 11,
        },
        "honesty": {
            "return_exchange_context_complete_for_normalized_block": 1,
            "return_coefficient_rule_complete": 0,
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
    require(len(rows) == 86, "return-exchange row count")
    require(digest(rows) == EXPECTED_COMPILED_ROW_SHA256, "return-exchange row digest mismatch")
    alternating = Counter()
    returned = Counter()
    host_types = Counter()
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
    require(alternating == Counter({8: 276, 4: 68}), "alternating cycle census")
    require(returned == Counter({"00": 86, "11": 86, "22": 86, "33": 86}), "returned edge census")
    require(host_types == Counter({"one-alt8-cycle": 69, "two-alt4-cycles": 17}), "host cycle type census")
    return rows

def mutation_audit(selected: dict[str, Any], contract: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(rows=85),
        lambda item: item["aggregate"].update(exchange_entries=343),
        lambda item: item.update(compiled_return_exchange_row_sha256="0" * 64),
        lambda item: item.update(old_matching="unknown"),
        lambda item: item.update(pairing_rule="target-only"),
        lambda item: item["aggregate"]["alternating_cycle_length_census"].update({"4": 67}),
        lambda item: item["aggregate"]["host_cycle_type_census"].update({"two-alt4-cycles": 16}),
        lambda item: item["aggregate"]["returned_edge_census"].update({"00": 85}),
        lambda item: item["aggregate"]["selector_census"].update({"2031": 33}),
        lambda item: item["honesty"].update(return_coefficient_rule_complete=1),
        lambda item: item["honesty"].update(return_child_keys_complete=1),
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
    require(rejected == len(mutations), "return-exchange corruption accepted")
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
        "compiled_return_exchange_row_sha256": EXPECTED_COMPILED_ROW_SHA256,
        "row_count": len(rows),
        "exchange_entry_count": 344,
        "alternating_cycle_length_four_count": 68,
        "alternating_cycle_length_eight_count": 276,
        "two_cycle_host_count": 17,
        "one_cycle_host_count": 69,
        "rejected_corruptions": mutation_audit(selected, contract),
        "side_four_return_exchange_context_complete": 1,
        "return_exchange_context_complete_for_normalized_block": 1,
        "return_coefficient_rule_complete": 0,
        "return_child_keys_complete": 0,
        "return_child_weights_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Compile and validate every within-host side-four response exchange."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


class ReturnExchangeManifestError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ReturnExchangeManifestError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


RAW_PATH = "data/prime_power_side_four_raw_fibre_lineage_manifest.json"
SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
CONTRACT_PATH = "data/prime_power_side_four_return_exchange_manifest_contract.json"
RAW_CHECKER_PATH = "scripts/check_prime_power_side_four_raw_fibre_lineage_manifest.py"
SELECTED_CHECKER_PATH = "scripts/check_prime_power_side_four_selected_response_provenance_manifest.py"
EXPECTED_RAW_SHA256 = "84ad1c92a9e0bcfb4d1f613e05edec20c4300022d96269ed561b45d32bf7432f"
EXPECTED_SELECTED_SHA256 = "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_CONTRACT_SHA256 = "b6f768bae19061ffe35e1b0b437a402e4d49c7ce4ac8fa5bc5ea005518c565f9"
EXPECTED_RECORD_SHA256 = "1151a0d65b228612217b484e97256d36a1a809d95338f18a28b2eb58ab2a3274"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ReturnExchangeManifestError("unable to locate repository root")


def load_module(path: Path, name: str) -> Any:
    require(path.is_file(), f"{path}: missing checker")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{path}: import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def response_edges(code: str) -> tuple[tuple[int, int], ...]:
    require(len(code) == 4 and set(code) == set("0123"), f"{code}: response permutation")
    return tuple((row, int(code[row])) for row in range(4))


def alternating_components(
    old: tuple[tuple[int, int], ...], new: tuple[tuple[int, int], ...]
) -> list[tuple[list[int], int]]:
    old_map = dict(old)
    new_map = dict(new)
    changed = [row for row in sorted(old_map) if old_map[row] != new_map[row]]
    adjacency: dict[tuple[str, int], list[tuple[str, int]]] = defaultdict(list)
    for row in changed:
        row_vertex = ("r", row)
        for column in (old_map[row], new_map[row]):
            column_vertex = ("c", column)
            adjacency[row_vertex].append(column_vertex)
            adjacency[column_vertex].append(row_vertex)
    seen: set[tuple[str, int]] = set()
    components: list[tuple[list[int], int]] = []
    for start in sorted(adjacency):
        if start in seen:
            continue
        stack = [start]
        vertices: set[tuple[str, int]] = set()
        rows: set[int] = set()
        while stack:
            vertex = stack.pop()
            if vertex in seen:
                continue
            seen.add(vertex)
            vertices.add(vertex)
            if vertex[0] == "r":
                rows.add(vertex[1])
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    stack.append(neighbor)
        require(len(vertices) == 2 * len(rows), "alternating component balance")
        require(len(vertices) >= 4 and len(vertices) % 2 == 0, "even alternating cycle")
        components.append((sorted(rows), len(vertices)))
    return sorted(components, key=lambda item: (item[1], item[0]))


def compile_records(raw: dict[str, Any], selected: dict[str, Any]) -> list[dict[str, Any]]:
    selected_by_host = {
        host[0]: {
            "selector": host[1],
            "face": set(host[2].split(",")),
        }
        for host in selected["hosts"]
    }
    raw_by_host = {host[0]: host for host in raw["hosts"]}
    require(set(raw_by_host) == set(selected_by_host), "raw/selected host identifiers")
    records: list[dict[str, Any]] = []
    for host_id in sorted(raw_by_host):
        raw_host = raw_by_host[host_id]
        response_energy: dict[str, int] = {}
        for encoded in raw_host[2]:
            code, energy_text = encoded.split(":", 1)
            response_energy[code] = int(energy_text)
        responses = sorted(response_energy)
        selector = selected_by_host[host_id]["selector"]
        face = selected_by_host[host_id]["face"]
        require(selector in face and face <= set(responses), f"{host_id}: selector face")
        for old_code in responses:
            for new_code in responses:
                if old_code == new_code:
                    continue
                old = response_edges(old_code)
                new = response_edges(new_code)
                old_map = dict(old)
                new_map = dict(new)
                changed_rows = [row for row in range(4) if old_map[row] != new_map[row]]
                components = alternating_components(old, new)
                row_cycle_length: dict[int, int] = {}
                for rows, cycle_length in components:
                    for row in rows:
                        row_cycle_length[row] = cycle_length
                require(set(row_cycle_length) == set(changed_rows), f"{host_id}: cycle row coverage")
                returned_edge_states = [
                    [f"{row}{old_map[row]}", f"{row}{new_map[row]}", row_cycle_length[row]]
                    for row in changed_rows
                ]
                old_inverse = {column: row for row, column in old}
                new_inverse = {column: row for row, column in new}
                changed_targets = [
                    column
                    for column in range(4)
                    if old_inverse[column] != new_inverse[column]
                ]
                target_exchange_pairs = [
                    [
                        f"{old_inverse[column]}{column}",
                        f"{new_inverse[column]}{column}",
                        row_cycle_length[old_inverse[column]],
                    ]
                    for column in changed_targets
                ]
                require(len(returned_edge_states) == len(target_exchange_pairs), f"{host_id}: source/target exchange cardinality")
                records.append(
                    {
                        "host_id": host_id,
                        "old_response": old_code,
                        "new_response": new_code,
                        "old_energy": response_energy[old_code],
                        "new_energy": response_energy[new_code],
                        "returned_edge_states": returned_edge_states,
                        "target_exchange_pairs": target_exchange_pairs,
                        "cycle_lengths": [length for _, length in components],
                        "churn": len(changed_rows),
                        "old_is_selector": int(old_code == selector),
                        "new_is_selector": int(new_code == selector),
                        "old_in_minimizer_face": int(old_code in face),
                        "new_in_minimizer_face": int(new_code in face),
                        "recreated_credit_classes": None,
                        "return_kernel_entries": None,
                    }
                )
    return records


def expected_contract() -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-return-exchange-manifest-contract/v1",
        "raw_lineage_manifest_sha256": EXPECTED_RAW_SHA256,
        "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
        "compiled_transition_record_sha256": EXPECTED_RECORD_SHA256,
        "record_fields": [
            "host_id",
            "old_response",
            "new_response",
            "old_energy",
            "new_energy",
            "returned_edge_states",
            "target_exchange_pairs",
            "cycle_lengths",
            "churn",
            "old_is_selector",
            "new_is_selector",
            "old_in_minimizer_face",
            "new_in_minimizer_face",
            "recreated_credit_classes",
            "return_kernel_entries",
        ],
        "rules": {
            "transition_universe": "all ordered pairs of distinct allowed responses within one normalized host",
            "returned_edge_state": "[old selected edge,new selected same-source entering edge,alternating-cycle length]",
            "target_exchange_pair": "[old selected edge,new selected same-target entering edge,alternating-cycle length]",
            "cycle_decomposition": "vertex-disjoint even cycles of the old/new symmetric difference",
            "selector_binding": "canonical selector and complete minimizer face from the sealed selected-response manifest",
            "credit_boundary": "recreated credit classes and exact return-kernel entries remain null until physical credit provenance is attached",
        },
        "aggregate": {
            "hosts": 86,
            "response_occurrences": 206,
            "ordered_distinct_transitions": 378,
            "returned_edge_state_occurrences": 998,
            "churn_census": {"2": 200, "3": 114, "4": 64},
            "cycle_signature_census": {"4": 200, "6": 114, "4+4": 32, "8": 32},
            "energy_transition_census": {
                "0->0": 164,
                "0->1": 41,
                "0->4": 46,
                "1->0": 41,
                "1->4": 20,
                "4->0": 46,
                "4->1": 20,
            },
            "selector_source_transitions": 120,
            "selector_destination_transitions": 120,
            "minimizer_face_source_transitions": 260,
            "minimizer_face_destination_transitions": 260,
            "within_minimizer_face_transitions": 164,
        },
        "honesty": {
            "side_four_return_exchange_manifest_complete": 1,
            "return_exchange_state_complete": 1,
            "recreated_credit_classes_complete": 0,
            "return_kernel_entries_complete": 0,
            "return_coefficients_complete": 0,
            "global_child_provenance_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(
    raw: dict[str, Any], selected: dict[str, Any], contract: dict[str, Any]
) -> list[dict[str, Any]]:
    require(digest(raw) == EXPECTED_RAW_SHA256, "raw lineage digest")
    require(digest(selected) == EXPECTED_SELECTED_SHA256, "selected-response digest")
    require(contract == expected_contract(), "return exchange contract differs from canonical schema")
    require(digest(contract) == EXPECTED_CONTRACT_SHA256, "return exchange contract digest")
    records = compile_records(raw, selected)
    require(len(records) == 378, "ordered transition count")
    require(digest(records) == EXPECTED_RECORD_SHA256, "compiled transition digest")
    require(sum(len(record["returned_edge_states"]) for record in records) == 998, "returned-edge occurrence count")
    require(Counter(record["churn"] for record in records) == Counter({2: 200, 3: 114, 4: 64}), "churn census")
    cycle_census = Counter(
        "+".join(str(length) for length in record["cycle_lengths"])
        for record in records
    )
    require(cycle_census == Counter({"4": 200, "6": 114, "4+4": 32, "8": 32}), "cycle signature census")
    energy_census = Counter(
        f"{record['old_energy']}->{record['new_energy']}" for record in records
    )
    require(
        energy_census
        == Counter(
            {
                "0->0": 164,
                "0->1": 41,
                "0->4": 46,
                "1->0": 41,
                "1->4": 20,
                "4->0": 46,
                "4->1": 20,
            }
        ),
        "energy transition census",
    )
    require(sum(record["old_is_selector"] for record in records) == 120, "selector source count")
    require(sum(record["new_is_selector"] for record in records) == 120, "selector destination count")
    require(sum(record["old_in_minimizer_face"] for record in records) == 260, "minimizer source count")
    require(sum(record["new_in_minimizer_face"] for record in records) == 260, "minimizer destination count")
    require(
        sum(
            record["old_in_minimizer_face"]
            and record["new_in_minimizer_face"]
            for record in records
        )
        == 164,
        "within-face transition count",
    )
    for record in records:
        require(record["old_response"] != record["new_response"], "distinct transition responses")
        require(record["churn"] == len(record["returned_edge_states"]), "churn/source state count")
        require(record["churn"] == len(record["target_exchange_pairs"]), "churn/target pair count")
        require(record["recreated_credit_classes"] is None, "credit class honesty")
        require(record["return_kernel_entries"] is None, "kernel entry honesty")
        for old_edge, new_edge, cycle_length in record["returned_edge_states"]:
            require(old_edge[0] == new_edge[0], "same-source exchange")
            require(old_edge != new_edge, "changed source edge")
            require(cycle_length in {4, 6, 8}, "source cycle length")
        for old_edge, new_edge, cycle_length in record["target_exchange_pairs"]:
            require(old_edge[1] == new_edge[1], "same-target exchange")
            require(old_edge != new_edge, "changed target edge")
            require(cycle_length in {4, 6, 8}, "target cycle length")
    return records


def mutation_audit(
    raw: dict[str, Any], selected: dict[str, Any], contract: dict[str, Any]
) -> int:
    mutations = [
        lambda item: item["aggregate"].update(ordered_distinct_transitions=377),
        lambda item: item["aggregate"].update(returned_edge_state_occurrences=997),
        lambda item: item["aggregate"]["churn_census"].update({"2": 199}),
        lambda item: item["aggregate"]["cycle_signature_census"].pop("8"),
        lambda item: item["aggregate"]["energy_transition_census"].update({"0->0": 163}),
        lambda item: item.update(compiled_transition_record_sha256="0" * 64),
        lambda item: item["record_fields"].remove("returned_edge_states"),
        lambda item: item["rules"].update(transition_universe="selector transitions only"),
        lambda item: item["rules"].update(credit_boundary="assume no recreated credits"),
        lambda item: item["honesty"].update(recreated_credit_classes_complete=1),
        lambda item: item["honesty"].update(return_coefficients_complete=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(contract)
        mutate(bad)
        try:
            validate(raw, selected, bad)
        except ReturnExchangeManifestError:
            rejected += 1
    require(rejected == len(mutations), "return exchange corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    raw = json.loads((root / RAW_PATH).read_text(encoding="utf-8"))
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    contract = json.loads((root / CONTRACT_PATH).read_text(encoding="utf-8"))
    raw_checker = load_module(root / RAW_CHECKER_PATH, "side_four_raw_checker")
    selected_checker = load_module(root / SELECTED_CHECKER_PATH, "side_four_selected_checker")
    raw_checker.validate(raw)
    selected_checker.validate(raw, selected)
    records = validate(raw, selected, contract)
    print(
        json.dumps(
            {
                "checker": "prime-power-side-four-return-exchange-manifest",
                "return_exchange_contract_sha256": EXPECTED_CONTRACT_SHA256,
                "compiled_transition_record_sha256": EXPECTED_RECORD_SHA256,
                "ordered_transition_count": len(records),
                "returned_edge_state_occurrence_count": 998,
                "selector_destination_transition_count": 120,
                "within_minimizer_face_transition_count": 164,
                "rejected_corruptions": mutation_audit(raw, selected, contract),
                "side_four_return_exchange_manifest_complete": 1,
                "return_exchange_state_complete": 1,
                "recreated_credit_classes_complete": 0,
                "return_kernel_entries_complete": 0,
                "return_coefficients_complete": 0,
                "global_child_provenance_complete": 0,
                "complete_weighted_rows_strict": 0,
                "all_n_proved_by_checker": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

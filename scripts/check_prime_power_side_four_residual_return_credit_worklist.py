#!/usr/bin/env python3
"""Compile rank-one and rank-two residual return-credit dependency rows."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path
from typing import Any


class ResidualReturnCreditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ResidualReturnCreditError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
RETURN_CONTRACT_PATH = "data/prime_power_side_four_return_exchange_context_contract.json"
WORKLIST_CONTRACT_PATH = "data/prime_power_side_four_residual_return_credit_worklist_contract.json"
RETURN_CHECKER_PATH = "scripts/check_prime_power_side_four_return_exchange_context.py"
EXPECTED_SELECTED_SHA256 = "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_RETURN_CONTRACT_SHA256 = "0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b"
EXPECTED_RETURN_CONTEXT_ROW_SHA256 = "fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea"
EXPECTED_WORKLIST_CONTRACT_SHA256 = "606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808"
EXPECTED_RESIDUAL_ROW_SHA256 = "72efb06f92a1af90addde21b06146cdfc5b73f31134953583effae188f8713d2"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ResidualReturnCreditError("unable to locate repository root")


def load_module(path: Path) -> Any:
    require(path.is_file(), "return context checker missing")
    spec = importlib.util.spec_from_file_location("side_four_return_context", path)
    require(spec is not None and spec.loader is not None, "return checker import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_line(
    first: tuple[int, int], second: tuple[int, int]
) -> tuple[int, int, int]:
    x1, y1 = first
    x2, y2 = second
    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
    common = 0
    for value in (a, b, c):
        common = gcd(common, abs(value))
    if common:
        a, b, c = a // common, b // common, c // common
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def line_occupancy(
    points: tuple[tuple[int, int], ...], line: tuple[int, int, int]
) -> int:
    a, b, c = line
    return sum(a * x + b * y + c == 0 for x, y in points)


def compile_rows(
    selected: dict[str, Any], return_rows: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    require(digest(selected) == EXPECTED_SELECTED_SHA256, "selected manifest digest")
    return_by_host = {row["host_id"]: row for row in return_rows}
    require(len(return_by_host) == 86, "return host coverage")
    rows: list[dict[str, Any]] = []
    for host in selected["hosts"]:
        host_id, selector = host[0], host[1]
        require(host_id in return_by_host, f"{host_id}: return context missing")
        return_row = return_by_host[host_id]
        require(return_row["selected_response"] == selector, f"{host_id}: selector mismatch")
        exchange_by_source = {entry[0]: entry for entry in return_row["exchanges"]}
        require(set(exchange_by_source) == set(range(4)), f"{host_id}: source exchanges")
        points = tuple((source, int(selector[source])) for source in range(4))

        rank_one_entries: list[dict[str, Any]] = []
        for source, target in points:
            exchange = exchange_by_source[source]
            require(exchange[1] == f"{source}{source}", f"{host_id}: rank-one predecessor")
            require(exchange[2] == f"{source}{target}", f"{host_id}: rank-one entering edge")
            rank_one_entries.append(
                {
                    "host_id": host_id,
                    "entering_edge": exchange[2],
                    "returned_predecessor": exchange[1],
                    "matching_cycle_length": exchange[3] // 2,
                    "background_pair_incidence": None,
                    "rank_one_child_key": None,
                    "rank_one_child_weight": None,
                }
            )

        rank_two_entries: list[dict[str, Any]] = []
        for first, second in combinations(points, 2):
            line = canonical_line(first, second)
            owner = max(first, second)
            exchange = exchange_by_source[owner[0]]
            require(exchange[2] == f"{owner[0]}{owner[1]}", f"{host_id}: rank-two owner")
            rank_two_entries.append(
                {
                    "host_id": host_id,
                    "response_pair": [
                        f"{first[0]}{first[1]}",
                        f"{second[0]}{second[1]}",
                    ],
                    "line_equation": list(line),
                    "response_line_occupancy": line_occupancy(points, line),
                    "entering_owner": exchange[2],
                    "returned_predecessor": exchange[1],
                    "matching_cycle_length": exchange[3] // 2,
                    "background_point_incidence": None,
                    "rank_two_child_key": None,
                    "rank_two_child_weight": None,
                }
            )

        rows.append(
            {
                "host_id": host_id,
                "selected_response": selector,
                "rank_one_entries": rank_one_entries,
                "rank_two_entries": rank_two_entries,
            }
        )
    return rows


def expected_contract() -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-residual-return-credit-worklist-contract/v1",
        "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
        "return_exchange_contract_sha256": EXPECTED_RETURN_CONTRACT_SHA256,
        "compiled_return_context_row_sha256": EXPECTED_RETURN_CONTEXT_ROW_SHA256,
        "compiled_residual_return_row_sha256": EXPECTED_RESIDUAL_ROW_SHA256,
        "rank_one_entry_encoding": "[host,entering_edge,returned_predecessor,matching_cycle_length,background_pair_incidence,child_key,child_weight]",
        "rank_two_entry_encoding": "[host,response_pair,line_equation,response_line_occupancy,entering_owner,returned_predecessor,matching_cycle_length,background_point_incidence,child_key,child_weight]",
        "rules": {
            "rank_one": "one selected entering edge with an unresolved collinear background pair; owner is the entering edge and charge uses its same-source identity predecessor",
            "rank_two": "one selected response pair with an unresolved collinear background point; owner is the lexicographically maximal entering edge and charge uses its same-source identity predecessor",
            "line_geometry": "rank-two response-pair line equation and response occupancy are exact on the normalized selected response",
            "background_boundary": "background pair and point incidences remain null until the actual background-height and incidence profile is attached",
            "binding_boundary": "every rank-one and rank-two child key and positive weight remains unresolved",
        },
        "aggregate": {
            "rows": 86,
            "rank_one_dependency_entries": 344,
            "rank_two_dependency_entries": 516,
            "unresolved_background_pair_incidences": 344,
            "unresolved_background_point_incidences": 516,
            "unresolved_child_keys": 860,
            "unresolved_child_weights": 860,
            "rank_one_returned_edge_census": {"00": 86, "11": 86, "22": 86, "33": 86},
            "rank_one_matching_cycle_census": {"2": 68, "4": 276},
            "rank_two_returned_edge_census": {"11": 86, "22": 172, "33": 258},
            "rank_two_matching_cycle_census": {"2": 102, "4": 414},
            "rank_two_response_line_occupancy_census": {"2": 477, "3": 27, "4": 12},
            "distinct_rank_two_line_equations": 23,
            "rank_two_line_equation_multiplicity_distribution": {
                "9": 2,
                "13": 8,
                "15": 3,
                "27": 1,
                "28": 2,
                "34": 5,
                "47": 1,
                "49": 1,
            },
        },
        "honesty": {
            "side_four_residual_return_credit_worklist_complete": 1,
            "rank_one_return_structure_complete_for_normalized_block": 1,
            "rank_two_return_structure_complete_for_normalized_block": 1,
            "actual_background_profiles_complete": 0,
            "rank_one_return_coefficients_complete": 0,
            "rank_two_return_coefficients_complete": 0,
            "residual_return_credit_classes_complete": 0,
            "return_child_keys_complete": 0,
            "return_child_weights_complete": 0,
            "complete_return_coefficient_rule_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(
    selected: dict[str, Any], return_rows: list[dict[str, Any]], contract: dict[str, Any]
) -> list[dict[str, Any]]:
    require(contract == expected_contract(), "residual return contract differs from canonical schema")
    require(digest(contract) == EXPECTED_WORKLIST_CONTRACT_SHA256, "residual return contract digest")
    rows = compile_rows(selected, return_rows)
    require(len(rows) == 86, "residual row count")
    require(digest(rows) == EXPECTED_RESIDUAL_ROW_SHA256, "residual row digest")

    rank_one = [entry for row in rows for entry in row["rank_one_entries"]]
    rank_two = [entry for row in rows for entry in row["rank_two_entries"]]
    require(len(rank_one) == 344, "rank-one entry count")
    require(len(rank_two) == 516, "rank-two entry count")
    require(Counter(entry["returned_predecessor"] for entry in rank_one) == Counter({"00": 86, "11": 86, "22": 86, "33": 86}), "rank-one returned-edge census")
    require(Counter(entry["matching_cycle_length"] for entry in rank_one) == Counter({4: 276, 2: 68}), "rank-one cycle census")
    require(Counter(entry["returned_predecessor"] for entry in rank_two) == Counter({"33": 258, "22": 172, "11": 86}), "rank-two returned-edge census")
    require(Counter(entry["matching_cycle_length"] for entry in rank_two) == Counter({4: 414, 2: 102}), "rank-two cycle census")
    require(Counter(entry["response_line_occupancy"] for entry in rank_two) == Counter({2: 477, 3: 27, 4: 12}), "rank-two occupancy census")
    line_counts = Counter(tuple(entry["line_equation"]) for entry in rank_two)
    require(len(line_counts) == 23, "rank-two line-equation count")
    require(Counter(line_counts.values()) == Counter({13: 8, 34: 5, 15: 3, 28: 2, 9: 2, 49: 1, 47: 1, 27: 1}), "rank-two line multiplicity distribution")

    for entry in rank_one:
        require(entry["background_pair_incidence"] is None, "rank-one background honesty")
        require(entry["rank_one_child_key"] is None and entry["rank_one_child_weight"] is None, "rank-one binding honesty")
        require(entry["entering_edge"][0] == entry["returned_predecessor"][0], "rank-one source pairing")
    for entry in rank_two:
        require(entry["background_point_incidence"] is None, "rank-two background honesty")
        require(entry["rank_two_child_key"] is None and entry["rank_two_child_weight"] is None, "rank-two binding honesty")
        require(entry["entering_owner"][0] == entry["returned_predecessor"][0], "rank-two source pairing")
        require(entry["response_line_occupancy"] in {2, 3, 4}, "rank-two response occupancy")
    return rows


def mutation_audit(
    selected: dict[str, Any], return_rows: list[dict[str, Any]], contract: dict[str, Any]
) -> int:
    mutations = [
        lambda item: item["aggregate"].update(rank_one_dependency_entries=343),
        lambda item: item["aggregate"].update(rank_two_dependency_entries=515),
        lambda item: item.update(compiled_residual_return_row_sha256="0" * 64),
        lambda item: item["aggregate"]["rank_one_returned_edge_census"].update({"00": 85}),
        lambda item: item["aggregate"]["rank_two_returned_edge_census"].update({"33": 257}),
        lambda item: item["aggregate"]["rank_two_response_line_occupancy_census"].update({"2": 476}),
        lambda item: item["rules"].update(background_boundary="assume empty background"),
        lambda item: item["rules"].update(binding_boundary="default weight one"),
        lambda item: item["honesty"].update(actual_background_profiles_complete=1),
        lambda item: item["honesty"].update(rank_one_return_coefficients_complete=1),
        lambda item: item["honesty"].update(residual_return_credit_classes_complete=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(contract)
        mutate(bad)
        try:
            validate(selected, return_rows, bad)
        except ResidualReturnCreditError:
            rejected += 1
    require(rejected == len(mutations), "residual return corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    return_contract = json.loads((root / RETURN_CONTRACT_PATH).read_text(encoding="utf-8"))
    contract = json.loads((root / WORKLIST_CONTRACT_PATH).read_text(encoding="utf-8"))
    return_checker = load_module(root / RETURN_CHECKER_PATH)
    require(return_checker.EXPECTED_CONTRACT_SHA256 == EXPECTED_RETURN_CONTRACT_SHA256, "return contract binding")
    require(return_checker.EXPECTED_COMPILED_CONTEXT_ROW_SHA256 == EXPECTED_RETURN_CONTEXT_ROW_SHA256, "return row binding")
    return_rows = return_checker.validate(selected, return_contract)
    rows = validate(selected, return_rows, contract)
    print(
        json.dumps(
            {
                "checker": "prime-power-side-four-residual-return-credit-worklist",
                "residual_return_contract_sha256": EXPECTED_WORKLIST_CONTRACT_SHA256,
                "compiled_residual_return_row_sha256": EXPECTED_RESIDUAL_ROW_SHA256,
                "row_count": len(rows),
                "rank_one_dependency_entry_count": 344,
                "rank_two_dependency_entry_count": 516,
                "unresolved_background_incidence_count": 860,
                "unresolved_child_key_count": 860,
                "unresolved_child_weight_count": 860,
                "rejected_corruptions": mutation_audit(selected, return_rows, contract),
                "side_four_residual_return_credit_worklist_complete": 1,
                "rank_one_return_structure_complete_for_normalized_block": 1,
                "rank_two_return_structure_complete_for_normalized_block": 1,
                "actual_background_profiles_complete": 0,
                "rank_one_return_coefficients_complete": 0,
                "rank_two_return_coefficients_complete": 0,
                "residual_return_credit_classes_complete": 0,
                "return_child_keys_complete": 0,
                "return_child_weights_complete": 0,
                "complete_return_coefficient_rule_complete": 0,
                "complete_weighted_rows_strict": 0,
                "all_n_proved_by_checker": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

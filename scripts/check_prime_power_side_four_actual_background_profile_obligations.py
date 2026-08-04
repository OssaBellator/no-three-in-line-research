#!/usr/bin/env python3
"""Compile exact actual-background profile obligations for the side-four block."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from collections import Counter, defaultdict
from math import comb
from pathlib import Path
from typing import Any


class ActualBackgroundProfileObligationError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ActualBackgroundProfileObligationError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
RETURN_CONTRACT_PATH = "data/prime_power_side_four_return_exchange_context_contract.json"
RESIDUAL_CONTRACT_PATH = "data/prime_power_side_four_residual_return_credit_worklist_contract.json"
PROFILE_CONTRACT_PATH = "data/prime_power_side_four_actual_background_profile_obligation_contract.json"
RETURN_CHECKER_PATH = "scripts/check_prime_power_side_four_return_exchange_context.py"
RESIDUAL_CHECKER_PATH = "scripts/check_prime_power_side_four_residual_return_credit_worklist.py"

EXPECTED_SELECTED_SHA256 = "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_RETURN_CONTRACT_SHA256 = "0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b"
EXPECTED_RETURN_CONTEXT_ROW_SHA256 = "fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea"
EXPECTED_RESIDUAL_CONTRACT_SHA256 = "606627526d45ca38c216ad036439046b0da8d9f90f12041fa25019fbb2a82808"
EXPECTED_RESIDUAL_ROW_SHA256 = "72efb06f92a1af90addde21b06146cdfc5b73f31134953583effae188f8713d2"
EXPECTED_PROFILE_CONTRACT_SHA256 = "090adf1124d186d0eb8c16a4f7ae286d167583540386832c642b4eac2d24922f"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ActualBackgroundProfileObligationError("unable to locate repository root")


def load_module(path: Path, name: str) -> Any:
    require(path.is_file(), f"{path}: missing checker")
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"{name}: import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expected_contract() -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-actual-background-profile-obligation-contract/v1",
        "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
        "return_exchange_contract_sha256": EXPECTED_RETURN_CONTRACT_SHA256,
        "residual_return_contract_sha256": EXPECTED_RESIDUAL_CONTRACT_SHA256,
        "compiled_residual_return_row_sha256": EXPECTED_RESIDUAL_ROW_SHA256,
        "profile_fields": [
            "host_id",
            "background_id",
            "background_points",
            "background_point_provenance",
            "rank_one_incidence_witnesses",
            "rank_two_line_loads",
            "line_owner_labels",
            "interface_provenance",
            "crt_provenance",
        ],
        "rules": {
            "background_identity": "each profile identifies one exact background point set and complete provenance refinement for one normalized host row",
            "rank_one_witness": "for each selected entering edge, list every nonaxis background line through it and certify the exact sum of binomial(line_load,2)",
            "rank_two_line_class": "all response pairs on one exact host-line share one background line-load variable; a response line of occupancy k expands to binomial(k,2) pair slots",
            "complete_line_kernel": "for background load h and response occupancy k use k*binomial(h,2)+binomial(k,2)*h+binomial(k,3)",
            "provenance_boundary": "line owner, interface and CRT labels remain explicit and are never inferred from the normalized host",
            "unresolved_boundary": "null profile fields are obligations, not zero values",
        },
        "aggregate": {
            "host_profile_records": 86,
            "rank_one_incidence_slots": 344,
            "rank_two_pair_slots": 516,
            "rank_two_host_line_classes": 488,
            "host_line_classes_by_response_occupancy": {"2": 477, "3": 9, "4": 2},
            "pair_slots_by_response_occupancy": {"2": 477, "3": 27, "4": 12},
            "unresolved_background_ids": 86,
            "unresolved_background_point_sets": 86,
            "unresolved_background_point_provenance_records": 86,
            "unresolved_rank_one_incidence_witnesses": 344,
            "unresolved_rank_two_line_loads": 488,
            "unresolved_line_owner_labels": 488,
            "unresolved_interface_provenance_records": 86,
            "unresolved_crt_provenance_records": 86,
        },
        "honesty": {
            "actual_background_profile_obligation_compiler_complete": 1,
            "actual_background_profiles_complete": 0,
            "rank_one_return_coefficients_complete": 0,
            "rank_two_return_coefficients_complete": 0,
            "line_coefficients_complete": 0,
            "global_child_provenance_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def compile_requirements(residual_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    requirements: list[dict[str, Any]] = []
    for row in residual_rows:
        host_id = row["host_id"]
        rank_one = []
        for entry in row["rank_one_entries"]:
            require(entry["background_pair_incidence"] is None, f"{host_id}: rank-one incidence unexpectedly populated")
            rank_one.append(
                {
                    "entering_edge": entry["entering_edge"],
                    "returned_predecessor": entry["returned_predecessor"],
                    "matching_cycle_length": entry["matching_cycle_length"],
                    "incident_background_lines": None,
                    "background_pair_incidence": None,
                }
            )

        grouped: dict[tuple[int, int, int], list[dict[str, Any]]] = defaultdict(list)
        for entry in row["rank_two_entries"]:
            require(entry["background_point_incidence"] is None, f"{host_id}: rank-two incidence unexpectedly populated")
            grouped[tuple(entry["line_equation"])].append(entry)

        rank_two_lines = []
        for line, entries in sorted(grouped.items()):
            occupancies = {entry["response_line_occupancy"] for entry in entries}
            require(len(occupancies) == 1, f"{host_id}:{line}: occupancy consistency")
            occupancy = occupancies.pop()
            require(len(entries) == comb(occupancy, 2), f"{host_id}:{line}: pair expansion")
            rank_two_lines.append(
                {
                    "line_equation": list(line),
                    "response_line_occupancy": occupancy,
                    "response_pairs": [entry["response_pair"] for entry in entries],
                    "entering_owners": [entry["entering_owner"] for entry in entries],
                    "returned_predecessors": [entry["returned_predecessor"] for entry in entries],
                    "background_line_load": None,
                    "line_owner_label": None,
                }
            )

        requirements.append(
            {
                "host_id": host_id,
                "selected_response": row["selected_response"],
                "background_id": None,
                "background_points": None,
                "background_point_provenance": None,
                "rank_one_incidence_witnesses": rank_one,
                "rank_two_line_loads": rank_two_lines,
                "interface_provenance": None,
                "crt_provenance": None,
            }
        )
    return requirements


def validate(
    selected: dict[str, Any],
    return_rows: list[dict[str, Any]],
    residual_rows: list[dict[str, Any]],
    contract: dict[str, Any],
) -> list[dict[str, Any]]:
    require(digest(selected) == EXPECTED_SELECTED_SHA256, "selected manifest digest")
    require(len(return_rows) == 86 and len(residual_rows) == 86, "host row coverage")
    require(contract == expected_contract(), "profile obligation contract differs from canonical schema")
    require(digest(contract) == EXPECTED_PROFILE_CONTRACT_SHA256, "profile obligation contract digest")

    requirements = compile_requirements(residual_rows)
    require(len(requirements) == 86, "profile requirement count")
    require(sum(len(row["rank_one_incidence_witnesses"]) for row in requirements) == 344, "rank-one slot count")
    require(sum(sum(len(line["response_pairs"]) for line in row["rank_two_line_loads"]) for row in requirements) == 516, "rank-two pair slot count")
    require(sum(len(row["rank_two_line_loads"]) for row in requirements) == 488, "host-line class count")

    line_class_occupancies = Counter(
        line["response_line_occupancy"]
        for row in requirements
        for line in row["rank_two_line_loads"]
    )
    require(line_class_occupancies == Counter({2: 477, 3: 9, 4: 2}), "host-line occupancy census")
    pair_slot_occupancies = Counter()
    for row in requirements:
        require(row["background_id"] is None, f"{row['host_id']}: background id honesty")
        require(row["background_points"] is None, f"{row['host_id']}: background points honesty")
        require(row["background_point_provenance"] is None, f"{row['host_id']}: background provenance honesty")
        require(row["interface_provenance"] is None, f"{row['host_id']}: interface provenance honesty")
        require(row["crt_provenance"] is None, f"{row['host_id']}: CRT provenance honesty")
        for witness in row["rank_one_incidence_witnesses"]:
            require(witness["incident_background_lines"] is None, f"{row['host_id']}: rank-one witness honesty")
            require(witness["background_pair_incidence"] is None, f"{row['host_id']}: rank-one coefficient honesty")
        for line in row["rank_two_line_loads"]:
            require(line["background_line_load"] is None, f"{row['host_id']}: line-load honesty")
            require(line["line_owner_label"] is None, f"{row['host_id']}: line-owner honesty")
            pair_slot_occupancies[line["response_line_occupancy"]] += len(line["response_pairs"])
    require(pair_slot_occupancies == Counter({2: 477, 3: 27, 4: 12}), "pair-slot occupancy census")
    return requirements


def mutation_audit(
    selected: dict[str, Any],
    return_rows: list[dict[str, Any]],
    residual_rows: list[dict[str, Any]],
    contract: dict[str, Any],
) -> int:
    mutations = [
        lambda item: item["aggregate"].update(host_profile_records=85),
        lambda item: item["aggregate"].update(rank_two_host_line_classes=487),
        lambda item: item["aggregate"]["host_line_classes_by_response_occupancy"].update({"2": 476}),
        lambda item: item["aggregate"]["pair_slots_by_response_occupancy"].update({"3": 26}),
        lambda item: item["profile_fields"].remove("background_points"),
        lambda item: item["rules"].update(rank_two_line_class="one variable per response pair"),
        lambda item: item["rules"].update(unresolved_boundary="null means zero"),
        lambda item: item["rules"].update(complete_line_kernel="rank three only"),
        lambda item: item["honesty"].update(actual_background_profiles_complete=1),
        lambda item: item["honesty"].update(rank_one_return_coefficients_complete=1),
        lambda item: item["honesty"].update(line_coefficients_complete=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(contract)
        mutate(bad)
        try:
            validate(selected, return_rows, residual_rows, bad)
        except ActualBackgroundProfileObligationError:
            rejected += 1
    require(rejected == len(mutations), "background profile corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    return_contract = json.loads((root / RETURN_CONTRACT_PATH).read_text(encoding="utf-8"))
    residual_contract = json.loads((root / RESIDUAL_CONTRACT_PATH).read_text(encoding="utf-8"))
    contract = json.loads((root / PROFILE_CONTRACT_PATH).read_text(encoding="utf-8"))

    return_checker = load_module(root / RETURN_CHECKER_PATH, "side_four_return_checker")
    residual_checker = load_module(root / RESIDUAL_CHECKER_PATH, "side_four_residual_checker")
    require(return_checker.EXPECTED_CONTRACT_SHA256 == EXPECTED_RETURN_CONTRACT_SHA256, "return contract binding")
    require(return_checker.EXPECTED_COMPILED_CONTEXT_ROW_SHA256 == EXPECTED_RETURN_CONTEXT_ROW_SHA256, "return row binding")
    require(residual_checker.EXPECTED_WORKLIST_CONTRACT_SHA256 == EXPECTED_RESIDUAL_CONTRACT_SHA256, "residual contract binding")
    require(residual_checker.EXPECTED_RESIDUAL_ROW_SHA256 == EXPECTED_RESIDUAL_ROW_SHA256, "residual row binding")

    return_rows = return_checker.validate(selected, return_contract)
    residual_rows = residual_checker.validate(selected, return_rows, residual_contract)
    requirements = validate(selected, return_rows, residual_rows, contract)
    print(
        json.dumps(
            {
                "checker": "prime-power-side-four-actual-background-profile-obligations",
                "profile_obligation_contract_sha256": EXPECTED_PROFILE_CONTRACT_SHA256,
                "compiled_profile_requirement_sha256": digest(requirements),
                "profile_record_count": 86,
                "rank_one_incidence_slot_count": 344,
                "rank_two_pair_slot_count": 516,
                "rank_two_host_line_class_count": 488,
                "rejected_corruptions": mutation_audit(selected, return_rows, residual_rows, contract),
                "actual_background_profile_obligation_compiler_complete": 1,
                "actual_background_profiles_complete": 0,
                "rank_one_return_coefficients_complete": 0,
                "rank_two_return_coefficients_complete": 0,
                "line_coefficients_complete": 0,
                "global_child_provenance_complete": 0,
                "complete_weighted_rows_strict": 0,
                "all_n_proved_by_checker": 0,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

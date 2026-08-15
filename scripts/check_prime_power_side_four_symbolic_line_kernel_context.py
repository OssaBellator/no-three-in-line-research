#!/usr/bin/env python3
"""Compile and validate the exact symbolic side-four line-energy kernel context."""
from __future__ import annotations
import copy, hashlib, importlib.util, json
from collections import Counter
from itertools import combinations
from math import comb, gcd
from pathlib import Path
from typing import Any

class SymbolicLineKernelError(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise SymbolicLineKernelError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
RETURN_CHECKER_PATH = "scripts/check_prime_power_side_four_return_exchange_context.py"
RETURN_CONTRACT_PATH = "data/prime_power_side_four_return_exchange_context_contract.json"
CONTRACT_PATH = "data/prime_power_side_four_symbolic_line_kernel_context_contract.json"
EXPECTED_SELECTED_SHA256 = "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_RETURN_CONTRACT_SHA256 = "0ef63d739e0d82c80105387cffaa4e81ff8834fc0d389f2597f4968cd1084e1b"
EXPECTED_RETURN_CONTEXT_ROW_SHA256 = "fdb2ff3287ce607727740130754230cd9c55a415985f393ea166bb3f7ef626ea"
EXPECTED_CONTRACT_SHA256 = "0232bda658189acdb880681ce19192698e049d603a2e779d5f9e287d43fe481e"

def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise SymbolicLineKernelError("unable to locate repository root")

def load_return_checker(path: Path) -> Any:
    require(path.is_file(), "return checker missing")
    spec = importlib.util.spec_from_file_location("side_four_return_checker", path)
    require(spec is not None and spec.loader is not None, "return checker import spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def canonical_line(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int, int]:
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

def selector_catalogue(selector: str) -> list[list[Any]]:
    require(len(selector) == 4 and set(selector) == set("0123"), f"{selector}: response permutation")
    points = [(source, int(selector[source])) for source in range(4)]
    lines: dict[tuple[int, int, int], int] = {}
    for first, second in combinations(points, 2):
        line = canonical_line(first, second)
        lines[line] = sum(line[0] * x + line[1] * y + line[2] == 0 for x, y in points)
    return [
        [f"{a},{b},{c}", occupancy, occupancy, comb(occupancy, 2), comb(occupancy, 3)]
        for (a, b, c), occupancy in sorted(lines.items())
    ]

def compiled_catalogue(selected: dict[str, Any]) -> tuple[dict[str, list[list[Any]]], Counter[str]]:
    require(digest(selected) == EXPECTED_SELECTED_SHA256, "selected-response manifest digest")
    selectors = Counter(host[1] for host in selected.get("hosts", []))
    require(sum(selectors.values()) == 86, "selected host count")
    return {selector: selector_catalogue(selector) for selector in sorted(selectors)}, selectors

def expected_contract() -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-symbolic-line-kernel-context-contract/v1",
        "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
        "return_exchange_contract_sha256": EXPECTED_RETURN_CONTRACT_SHA256,
        "compiled_return_context_row_sha256": EXPECTED_RETURN_CONTEXT_ROW_SHA256,
        "kernel_formula": "K(h,k)=k*C(h,2)+C(k,2)*h+C(k,3)",
        "entry_encoding": "[canonical_line,response_occupancy,rank_one_multiplier,rank_two_multiplier,rank_three_constant]",
        "selector_kernel_catalogue": {
            "2031": [["1,-2,-1",2,2,1,0],["1,-2,4",2,2,1,0],["1,3,-6",2,2,1,0],["2,1,-7",2,2,1,0],["2,1,-2",2,2,1,0],["3,-1,-3",2,2,1,0]],
            "2301": [["1,-1,-2",2,2,1,0],["1,-1,2",2,2,1,0],["1,1,-4",2,2,1,0],["1,1,-2",2,2,1,0],["1,3,-6",2,2,1,0],["3,1,-6",2,2,1,0]],
            "2310": [["1,-1,2",2,2,1,0],["1,1,-3",2,2,1,0],["1,2,-4",2,2,1,0],["2,1,-5",2,2,1,0],["2,3,-6",2,2,1,0],["3,2,-9",2,2,1,0]],
            "3012": [["1,-1,-1",3,3,3,1],["1,1,-3",2,2,1,0],["1,3,-9",2,2,1,0],["3,1,-3",2,2,1,0]],
            "3201": [["1,-1,-2",2,2,1,0],["1,1,-3",2,2,1,0],["1,2,-5",2,2,1,0],["2,1,-4",2,2,1,0],["2,3,-9",2,2,1,0],["3,2,-6",2,2,1,0]],
            "3210": [["1,1,-3",4,4,6,4]],
        },
        "aggregate": {
            "rows": 86,
            "selector_kernel_patterns": 6,
            "line_occurrence_entries": 488,
            "response_occupancy_census": {"2": 477, "3": 9, "4": 2},
            "rank_one_multiplier_total": 989,
            "rank_two_multiplier_total": 516,
            "rank_three_constant_total": 17,
            "unresolved_background_height_occurrences": 488,
            "unresolved_line_owner_occurrences": 488,
        },
        "honesty": {
            "symbolic_line_coefficient_rule_complete_for_normalized_block": 1,
            "rank_three_line_constants_match_return_kernel": 1,
            "actual_background_height_profiles_complete": 0,
            "line_owner_labels_complete": 0,
            "numeric_rank_one_rank_two_line_coefficients_complete": 0,
            "line_child_keys_complete": 0,
            "line_child_weights_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
    }

def validate(root: Path, contract: dict[str, Any]) -> dict[str, list[list[Any]]]:
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    return_checker = load_return_checker(root / RETURN_CHECKER_PATH)
    require(return_checker.EXPECTED_CONTRACT_SHA256 == EXPECTED_RETURN_CONTRACT_SHA256, "return contract binding")
    require(return_checker.EXPECTED_COMPILED_CONTEXT_ROW_SHA256 == EXPECTED_RETURN_CONTEXT_ROW_SHA256, "return row binding")
    return_contract = json.loads((root / RETURN_CONTRACT_PATH).read_text(encoding="utf-8"))
    return_rows = return_checker.validate(selected, return_contract)
    require(contract == expected_contract(), "symbolic line contract differs from canonical schema")
    require(digest(contract) == EXPECTED_CONTRACT_SHA256, "symbolic line contract digest mismatch")
    catalogue, selectors = compiled_catalogue(selected)
    require(catalogue == contract["selector_kernel_catalogue"], "selector kernel catalogue")
    occurrence = Counter()
    rank_one = rank_two = rank_three = entries = 0
    return_rank_three = 0
    return_by_host = {row["host_id"]: row for row in return_rows}
    for host in selected["hosts"]:
        host_id, selector = host[0], host[1]
        require(host_id in return_by_host, f"{host_id}: return row missing")
        require(return_by_host[host_id]["selected_response"] == selector, f"{host_id}: selector mismatch")
        row_rank_three = 0
        for _line, occupancy, r1, r2, r3 in catalogue[selector]:
            occurrence[occupancy] += 1
            rank_one += r1
            rank_two += r2
            rank_three += r3
            row_rank_three += r3
            entries += 1
        return_count = return_by_host[host_id]["rank_three_kernel"]["recreated_credit_count"]
        require(row_rank_three == return_count, f"{host_id}: line/return rank-three mismatch")
        return_rank_three += return_count
    require(selectors == Counter({"2031":34,"2301":15,"2310":13,"3012":9,"3201":13,"3210":2}), "selector census")
    require(entries == 488, "line occurrence entry count")
    require(occurrence == Counter({2:477,3:9,4:2}), "response occupancy census")
    require((rank_one, rank_two, rank_three, return_rank_three) == (989,516,17,17), "kernel multiplier census")
    return catalogue

def mutation_audit(root: Path, contract: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(rows=85),
        lambda item: item["aggregate"].update(line_occurrence_entries=487),
        lambda item: item["aggregate"].update(rank_one_multiplier_total=988),
        lambda item: item["aggregate"].update(rank_three_constant_total=16),
        lambda item: item.update(kernel_formula="rank three only"),
        lambda item: item["selector_kernel_catalogue"]["2031"].pop(),
        lambda item: item["selector_kernel_catalogue"]["3012"][0].__setitem__(1,2),
        lambda item: item["selector_kernel_catalogue"]["3210"][0].__setitem__(4,3),
        lambda item: item["honesty"].update(actual_background_height_profiles_complete=1),
        lambda item: item["honesty"].update(numeric_rank_one_rank_two_line_coefficients_complete=1),
        lambda item: item["honesty"].update(line_child_keys_complete=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(contract)
        mutate(bad)
        try:
            validate(root, bad)
        except SymbolicLineKernelError:
            rejected += 1
    require(rejected == len(mutations), "symbolic line corruption accepted")
    return rejected

def main() -> None:
    root = repository_root()
    contract = json.loads((root / CONTRACT_PATH).read_text(encoding="utf-8"))
    catalogue = validate(root, contract)
    print(json.dumps({
        "checker": "prime-power-side-four-symbolic-line-kernel-context",
        "symbolic_line_contract_sha256": EXPECTED_CONTRACT_SHA256,
        "return_exchange_contract_sha256": EXPECTED_RETURN_CONTRACT_SHA256,
        "selector_kernel_pattern_count": len(catalogue),
        "line_occurrence_entry_count": 488,
        "rank_one_multiplier_total": 989,
        "rank_two_multiplier_total": 516,
        "rank_three_constant_total": 17,
        "unresolved_background_height_occurrence_count": 488,
        "unresolved_line_owner_occurrence_count": 488,
        "rejected_corruptions": mutation_audit(root, contract),
        "side_four_symbolic_line_kernel_context_complete": 1,
        "symbolic_line_coefficient_rule_complete_for_normalized_block": 1,
        "rank_three_line_constants_match_return_kernel": 1,
        "actual_background_height_profiles_complete": 0,
        "line_owner_labels_complete": 0,
        "numeric_rank_one_rank_two_line_coefficients_complete": 0,
        "line_child_keys_complete": 0,
        "line_child_weights_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))

if __name__ == "__main__":
    main()

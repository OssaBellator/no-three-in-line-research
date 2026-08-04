#!/usr/bin/env python3
"""Compile and validate the complete side-four compulsory-row obligation worklist."""
from __future__ import annotations
import copy, hashlib, json
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path
from typing import Any

class CompulsoryRowObligationError(RuntimeError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise CompulsoryRowObligationError(message)

def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
CONTRACT_PATH = "data/prime_power_side_four_compulsory_row_obligation_worklist.json"
EXPECTED_SELECTED_SHA256 = "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_CONTRACT_SHA256 = "62c6c448b40a8b0294a35673aac997eac73c3380b1cceedffe9616c2326f3211"
EXPECTED_COMPILED_ROW_SHA256 = "b33e4fa3e442349edacbb14a65b088a92b823c67b6a4f810958076a65e3e797b"
CATEGORIES = ("return", "selector", "collision", "line", "interface", "geometric")

def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise CompulsoryRowObligationError("unable to locate repository root")

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

def response_line_signature(selector: str) -> str:
    require(len(selector) == 4 and set(selector) == set("0123"), f"{selector}: response permutation")
    points = [(index, int(selector[index])) for index in range(4)]
    lines: dict[tuple[int, int, int], int] = {}
    for first, second in combinations(points, 2):
        line = canonical_line(first, second)
        lines[line] = sum(line[0] * x + line[1] * y + line[2] == 0 for x, y in points)
    return ";".join(f"{a},{b},{c}:{occupancy}" for (a, b, c), occupancy in sorted(lines.items()))

def compile_rows(selected: dict[str, Any]) -> list[dict[str, Any]]:
    require(digest(selected) == EXPECTED_SELECTED_SHA256, "selected-response manifest digest")
    rows: list[dict[str, Any]] = []
    for host in selected.get("hosts", []):
        require(isinstance(host, list) and len(host) == 8, "selected host row")
        host_id, selector, face, minimum, gap, fate, blockers, collision = host
        require(fate in {"Z", "B"}, f"{host_id}: fate")
        context = {
            "host_id": host_id,
            "normalized_owner_scope": "side-four-raw-host",
            "fate": "zero-response" if fate == "Z" else "blocker-alternative",
            "collision_key": collision,
            "selected_response": selector,
            "minimizer_face": face,
            "minimum_energy": minimum,
            "next_energy_gap": gap,
            "local_line_signature": response_line_signature(selector),
            "interface_label": "side4-target01",
            "prime_power_label": "p2-k2",
            "crt_scope": "not-applied",
            "blockers": blockers,
        }
        obligations: list[list[Any]] = []
        for category in CATEGORIES:
            if category == "geometric":
                obligations.append([category, "known", minimum, None, None, "child-key-and-weight-unresolved"])
            else:
                obligations.append([category, "unresolved", None, None, None, "coefficient-child-key-and-weight-unresolved"])
        rows.append({"context": context, "obligations": obligations})
    return rows

def expected_contract() -> dict[str, Any]:
    return {
        "schema": "prime-power-side-four-compulsory-row-obligation-worklist-contract/v1",
        "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
        "compiled_row_digest": EXPECTED_COMPILED_ROW_SHA256,
        "categories": list(CATEGORIES),
        "context_fields": [
            "host_id",
            "normalized_owner_scope",
            "fate",
            "collision_key",
            "selected_response",
            "minimizer_face",
            "minimum_energy",
            "next_energy_gap",
            "local_line_signature",
            "interface_label",
            "prime_power_label",
            "crt_scope",
            "blockers",
        ],
        "context_rules": {
            "normalized_owner_scope": "side-four-raw-host",
            "fate": "Z->zero-response;B->blocker-alternative",
            "collision_key": "selected-response deletion trace",
            "local_line_signature": "canonical exact secant-line equations and occupancies of selected response",
            "interface_label": "side4-target01",
            "prime_power_label": "p2-k2",
            "crt_scope": "not-applied",
        },
        "coefficient_rules": {
            "return": "unresolved",
            "selector": "unresolved",
            "collision": "unresolved",
            "line": "unresolved",
            "interface": "unresolved",
            "geometric": "selected minimum_energy",
        },
        "child_binding_rule": "all child keys and positive weights remain unresolved",
        "aggregate": {
            "rows": 86,
            "obligations": 516,
            "known_coefficients": 86,
            "unresolved_coefficients": 430,
            "unresolved_child_keys": 516,
            "unresolved_child_weights": 516,
            "zero_geometric_coefficients": 75,
            "positive_geometric_coefficients": 11,
            "zero_response_rows": 75,
            "blocker_alternative_rows": 11,
            "distinct_local_line_signatures": 6,
            "local_line_signature_multiplicities": {"2": 1, "9": 1, "13": 2, "15": 1, "34": 1},
        },
        "honesty": {
            "compiled_normalized_row_context_complete": 1,
            "global_child_provenance_complete": 0,
            "compulsory_coefficients_complete": 0,
            "child_weights_complete": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
    }

def validate(selected: dict[str, Any], contract: dict[str, Any]) -> list[dict[str, Any]]:
    require(contract == expected_contract(), "obligation contract differs from canonical schema")
    require(digest(contract) == EXPECTED_CONTRACT_SHA256, "obligation contract digest mismatch")
    rows = compile_rows(selected)
    require(len(rows) == 86, "compiled row count")
    require(digest(rows) == EXPECTED_COMPILED_ROW_SHA256, "compiled row digest mismatch")
    complete_contexts = set()
    coefficient_status: Counter[str] = Counter()
    signature_counts: Counter[str] = Counter()
    for row in rows:
        context = row["context"]
        signature_counts[context["local_line_signature"]] += 1
        complete_context = tuple(context[field] if field != "blockers" else tuple(context[field]) for field in contract["context_fields"])
        require(complete_context not in complete_contexts, f"{context['host_id']}: duplicate normalized context")
        complete_contexts.add(complete_context)
        obligations = row["obligations"]
        require([item[0] for item in obligations] == list(CATEGORIES), f"{context['host_id']}: compulsory categories")
        for category, status, coefficient, child_key, child_weight, resolution in obligations:
            coefficient_status[status] += 1
            require(child_key is None and child_weight is None, f"{context['host_id']}:{category}: unresolved child binding")
            if category == "geometric":
                require(status == "known" and coefficient == context["minimum_energy"], f"{context['host_id']}: geometric coefficient")
                require(resolution == "child-key-and-weight-unresolved", f"{context['host_id']}: geometric resolution")
            else:
                require(status == "unresolved" and coefficient is None, f"{context['host_id']}:{category}: unresolved coefficient")
                require(resolution == "coefficient-child-key-and-weight-unresolved", f"{context['host_id']}:{category}: resolution")
    require(coefficient_status == Counter({"unresolved": 430, "known": 86}), "coefficient status census")
    require(len(signature_counts) == 6, "local line signature count")
    require(Counter(signature_counts.values()) == Counter({13: 2, 34: 1, 15: 1, 9: 1, 2: 1}), "line signature multiplicities")
    return rows

def mutation_audit(selected: dict[str, Any], contract: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(rows=85),
        lambda item: item["aggregate"].update(unresolved_coefficients=429),
        lambda item: item.update(compiled_row_digest="0" * 64),
        lambda item: item["categories"].pop(),
        lambda item: item["context_fields"].remove("collision_key"),
        lambda item: item["context_rules"].update(crt_scope="applied"),
        lambda item: item["coefficient_rules"].update({"return": "zero"}),
        lambda item: item["coefficient_rules"].update(geometric="unresolved"),
        lambda item: item.update(child_binding_rule="default weight one"),
        lambda item: item["honesty"].update(global_child_provenance_complete=1),
        lambda item: item["honesty"].update(compulsory_coefficients_complete=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(contract)
        mutate(bad)
        try:
            validate(selected, bad)
        except CompulsoryRowObligationError:
            rejected += 1
    require(rejected == len(mutations), "obligation contract corruption accepted")
    return rejected

def main() -> None:
    root = repository_root()
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    contract = json.loads((root / CONTRACT_PATH).read_text(encoding="utf-8"))
    rows = validate(selected, contract)
    print(json.dumps({
        "checker": "prime-power-side-four-compulsory-row-obligation-worklist",
        "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
        "obligation_contract_sha256": EXPECTED_CONTRACT_SHA256,
        "compiled_row_sha256": EXPECTED_COMPILED_ROW_SHA256,
        "row_count": len(rows),
        "obligation_count": 516,
        "known_coefficient_count": 86,
        "unresolved_coefficient_count": 430,
        "unresolved_child_key_count": 516,
        "unresolved_child_weight_count": 516,
        "distinct_local_line_signature_count": 6,
        "rejected_corruptions": mutation_audit(selected, contract),
        "side_four_compulsory_row_obligation_worklist_complete": 1,
        "compiled_normalized_row_context_complete": 1,
        "global_child_provenance_complete": 0,
        "compulsory_coefficients_complete": 0,
        "child_weights_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))

if __name__ == "__main__":
    main()

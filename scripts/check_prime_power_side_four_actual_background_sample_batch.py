#!/usr/bin/env python3
"""Validate one explicit side-four actual-background sample profile."""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations
from math import comb, gcd
from pathlib import Path
from typing import Any


class ActualBackgroundSampleError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ActualBackgroundSampleError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
OBLIGATION_PATH = "data/prime_power_side_four_actual_background_profile_obligation_contract.json"
SAMPLE_PATH = "data/prime_power_side_four_actual_background_sample_batch.json"
EXPECTED_SELECTED_SHA256 = "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_OBLIGATION_SHA256 = "e605c9da6e45bc4253129cea8e40e744dece8426aae0f0e7efbd2c849e1a08cd"
EXPECTED_RESIDUAL_ROW_SHA256 = "72efb06f92a1af90addde21b06146cdfc5b73f31134953583effae188f8713d2"
EXPECTED_SAMPLE_SHA256 = "71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise ActualBackgroundSampleError("unable to locate repository root")


def canonical_line(
    first: tuple[int, int], second: tuple[int, int]
) -> tuple[int, int, int]:
    require(first != second, "distinct points required")
    x1, y1 = first
    x2, y2 = second
    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
    common = 0
    for value in (a, b, c):
        common = gcd(common, abs(value))
    require(common > 0, "nonzero line")
    a, b, c = a // common, b // common, c // common
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def on_line(line: tuple[int, int, int], point: tuple[int, int]) -> bool:
    a, b, c = line
    x, y = point
    return a * x + b * y + c == 0


def edge(point: tuple[int, int]) -> str:
    return f"{point[0]}{point[1]}"


def compile_profile(
    selected: dict[str, Any], sample: dict[str, Any]
) -> dict[str, Any]:
    require(digest(selected) == EXPECTED_SELECTED_SHA256, "selected manifest digest")
    profile = sample["profile"]
    host_rows = [row for row in selected["hosts"] if row[0] == profile["host_id"]]
    require(len(host_rows) == 1, "sample host coverage")
    host = host_rows[0]
    require(host[1] == profile["selected_response"], "selected response binding")
    selector = profile["selected_response"]
    require(len(selector) == 4 and set(selector) == set("0123"), "response permutation")
    response = tuple((source, int(selector[source])) for source in range(4))

    raw_background = profile["background_points"]
    require(
        isinstance(raw_background, list)
        and len(raw_background) == 2
        and all(
            isinstance(point, list)
            and len(point) == 2
            and all(isinstance(value, int) for value in point)
            for point in raw_background
        ),
        "two integer background points",
    )
    background = tuple(tuple(point) for point in raw_background)
    require(len(set(background)) == len(background), "distinct background points")
    require(not set(background) & set(response), "background-response collision")
    require(
        profile["coordinate_scope"] == "integer-lattice-sample-not-global-board-claim",
        "sample coordinate scope",
    )
    require(sample["scope"] == {
        "kind": "explicit-integer-coordinate-sample",
        "global_recurrent_state_claim": 0,
        "normalized_host_inference": 0,
        "identity_matching_inference": 0,
    }, "sample scope honesty")

    provenance = profile["background_point_provenance"]
    require(
        provenance == [
            {"point": [4, 4], "label": "declared-sample-background-point-0"},
            {"point": [6, 5], "label": "declared-sample-background-point-1"},
        ],
        "background provenance",
    )

    rank_one: dict[str, int] = {}
    for point in response:
        incidence = 0
        for first, second in combinations(background, 2):
            line = canonical_line(first, second)
            if line[0] != 0 and line[1] != 0 and on_line(line, point):
                incidence += 1
        rank_one[edge(point)] = incidence

    rank_two: dict[str, int] = {}
    line_profiles: dict[tuple[int, int, int], dict[str, int]] = {}
    for first, second in combinations(response, 2):
        line = canonical_line(first, second)
        key = "|".join(sorted((edge(first), edge(second))))
        load = sum(on_line(line, point) for point in background)
        rank_two[key] = load
        occupancy = sum(on_line(line, point) for point in response)
        require(occupancy >= 2, f"{key}: response occupancy")
        if line in line_profiles:
            require(
                line_profiles[line]["response_occupancy"] == occupancy
                and line_profiles[line]["background_load"] == load,
                f"{key}: line profile consistency",
            )
        else:
            rank_one_line = occupancy * comb(load, 2)
            rank_two_line = comb(occupancy, 2) * load
            rank_three_line = comb(occupancy, 3)
            line_profiles[line] = {
                "background_load": load,
                "response_occupancy": occupancy,
                "rank_one": rank_one_line,
                "rank_two": rank_two_line,
                "rank_three": rank_three_line,
                "total": rank_one_line + rank_two_line + rank_three_line,
            }

    rank_one_return = {f"{source}{source}": 0 for source in range(4)}
    for point in response:
        rank_one_return[f"{point[0]}{point[0]}"] += rank_one[edge(point)]

    rank_two_return = {f"{source}{source}": 0 for source in range(4)}
    for first, second in combinations(response, 2):
        owner = max(first, second)
        key = "|".join(sorted((edge(first), edge(second))))
        rank_two_return[f"{owner[0]}{owner[0]}"] += rank_two[key]

    total_return = {
        predecessor: rank_one_return[predecessor] + rank_two_return[predecessor]
        for predecessor in rank_one_return
    }
    encoded_lines = {
        ",".join(str(value) for value in line): values
        for line, values in sorted(line_profiles.items())
    }
    return {
        "rank_one_by_entering_edge": rank_one,
        "rank_one_total": sum(rank_one.values()),
        "rank_two_by_response_pair": rank_two,
        "rank_two_total": sum(rank_two.values()),
        "rank_three_total": sum(item["rank_three"] for item in line_profiles.values()),
        "complete_line_kernel_by_line": encoded_lines,
        "complete_line_kernel_total": sum(item["total"] for item in line_profiles.values()),
        "return_rank_one_charge_by_predecessor": rank_one_return,
        "return_rank_two_charge_by_predecessor": rank_two_return,
        "return_total_charge_by_predecessor": total_return,
    }


def validate(
    selected: dict[str, Any],
    obligation: dict[str, Any],
    sample: dict[str, Any],
) -> dict[str, Any]:
    require(digest(obligation) == EXPECTED_OBLIGATION_SHA256, "profile obligation digest")
    require(
        sample["actual_background_profile_obligation_contract_sha256"]
        == EXPECTED_OBLIGATION_SHA256,
        "profile obligation binding",
    )
    require(
        sample["compiled_residual_return_row_sha256"]
        == EXPECTED_RESIDUAL_ROW_SHA256,
        "residual return binding",
    )
    require(
        sample["selected_response_manifest_sha256"] == EXPECTED_SELECTED_SHA256,
        "selected manifest binding",
    )
    require(digest(sample) == EXPECTED_SAMPLE_SHA256, "sample contract digest")
    compiled = compile_profile(selected, sample)
    require(sample["expected"] == compiled, "sample numeric profile")
    require(sample["aggregate"] == {
        "profile_records": 1,
        "background_points": 2,
        "populated_rank_one_entries": 4,
        "positive_rank_one_entries": 2,
        "populated_rank_two_entries": 6,
        "positive_rank_two_entries": 1,
        "populated_line_classes": 6,
        "positive_line_classes": 1,
        "numeric_non_geometric_categories": ["line", "return"],
    }, "sample aggregate")
    require(sample["honesty"] == {
        "side_four_actual_background_sample_batch_complete": 1,
        "sample_line_coefficients_complete": 1,
        "sample_rank_one_rank_two_return_coefficients_complete": 1,
        "actual_background_profiles_complete": 0,
        "global_child_provenance_complete": 0,
        "child_keys_complete": 0,
        "child_weights_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, "sample honesty")
    require(
        sample["profile"]["line_owner_labels"]
        == {"1,-2,4": "sample-line-owner:1,-2,4"},
        "line owner label",
    )
    require(
        sample["profile"]["interface_provenance"]
        == "side4-target01/sample-local-interface/v1",
        "interface provenance",
    )
    require(
        sample["profile"]["crt_provenance"] == "not-applied/sample-profile/v1",
        "CRT provenance",
    )
    return compiled


def mutation_audit(
    selected: dict[str, Any],
    obligation: dict[str, Any],
    sample: dict[str, Any],
) -> int:
    mutations = [
        lambda item: item["profile"].update(host_id="missing-host"),
        lambda item: item["profile"].update(selected_response="2301"),
        lambda item: item["profile"]["background_points"][0].__setitem__(0, 5),
        lambda item: item["profile"]["background_point_provenance"][0].update(label="inferred"),
        lambda item: item["scope"].update(global_recurrent_state_claim=1),
        lambda item: item["scope"].update(identity_matching_inference=1),
        lambda item: item["expected"].update(rank_one_total=1),
        lambda item: item["expected"].update(rank_two_total=1),
        lambda item: item["expected"].update(complete_line_kernel_total=3),
        lambda item: item["expected"]["return_total_charge_by_predecessor"].update({"22": 2}),
        lambda item: item["profile"]["line_owner_labels"].clear(),
        lambda item: item["honesty"].update(actual_background_profiles_complete=1),
        lambda item: item["honesty"].update(child_weights_complete=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(sample)
        mutate(bad)
        try:
            validate(selected, obligation, bad)
        except ActualBackgroundSampleError:
            rejected += 1
    require(rejected == len(mutations), "sample corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    obligation = json.loads((root / OBLIGATION_PATH).read_text(encoding="utf-8"))
    sample = json.loads((root / SAMPLE_PATH).read_text(encoding="utf-8"))
    compiled = validate(selected, obligation, sample)
    print(json.dumps({
        "checker": "prime-power-side-four-actual-background-sample-batch",
        "sample_contract_sha256": EXPECTED_SAMPLE_SHA256,
        "host_id": sample["profile"]["host_id"],
        "background_point_count": len(sample["profile"]["background_points"]),
        "rank_one_total": compiled["rank_one_total"],
        "rank_two_total": compiled["rank_two_total"],
        "complete_line_kernel_total": compiled["complete_line_kernel_total"],
        "return_total_charge_by_predecessor": compiled["return_total_charge_by_predecessor"],
        "rejected_corruptions": mutation_audit(selected, obligation, sample),
        "side_four_actual_background_sample_batch_complete": 1,
        "sample_line_coefficients_complete": 1,
        "sample_rank_one_rank_two_return_coefficients_complete": 1,
        "actual_background_profiles_complete": 0,
        "global_child_provenance_complete": 0,
        "child_keys_complete": 0,
        "child_weights_complete": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()

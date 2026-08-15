#!/usr/bin/env python3
"""Validate complete line/geometric selector scores for the two side-four samples."""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, permutations
from math import comb, gcd
from pathlib import Path
from typing import Any


class JointSampleSelectorScoreError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise JointSampleSelectorScoreError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
ZERO_SAMPLE_PATH = "data/prime_power_side_four_actual_background_sample_batch.json"
BLOCKER_SAMPLE_PATH = "data/prime_power_side_four_blocker_actual_background_sample_batch.json"
SCORES_PATH = "data/prime_power_side_four_joint_sample_complete_line_selector_scores.json"

EXPECTED_SELECTED_SHA256 = "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
EXPECTED_ZERO_SAMPLE_SHA256 = "71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0"
EXPECTED_BLOCKER_SAMPLE_SHA256 = "39677a7e68826f9bf9702d3af8f3b4218138fa0bb1d885c6801d220dddcabeaf"
EXPECTED_SCORES_SHA256 = "c5a7f78ddef889aacdffc152b40945ed4b798f850c9aecbd20d4428f9ea63d0e"


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "data").is_dir():
            return candidate
    raise JointSampleSelectorScoreError("unable to locate repository root")


def canonical_line(
    first: tuple[int, int], second: tuple[int, int]
) -> tuple[int, int, int]:
    require(first != second, "distinct points")
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


def parse_deletions(value: str) -> set[tuple[int, int]]:
    if value == "-":
        return set()
    output = set()
    for code in value.split(","):
        require(len(code) == 2 and code.isdigit(), "deletion code")
        output.add((int(code[0]), int(code[1])))
    return output


def allowed_responses(collision_key: str) -> list[str]:
    base = {
        (left, right)
        for left in range(4)
        for right in range(4)
        if left != right and (left, right) != (0, 1)
    }
    allowed = base - parse_deletions(collision_key)
    return [
        "".join(str(value) for value in permutation)
        for permutation in permutations(range(4))
        if all((left, permutation[left]) in allowed for left in range(4))
    ]


def score_response(response: str, background: list[list[int]]) -> dict[str, Any]:
    require(len(response) == 4 and set(response) == set("0123"), "response permutation")
    points = [(source, int(response[source])) for source in range(4)]
    background_points = [tuple(point) for point in background]
    lines: dict[tuple[int, int, int], int] = {}
    for first, second in combinations(points, 2):
        line = canonical_line(first, second)
        lines[line] = sum(on_line(line, point) for point in points)

    rank_one = rank_two = rank_three = 0
    for line, occupancy in lines.items():
        height = sum(on_line(line, point) for point in background_points)
        rank_one += occupancy * comb(height, 2)
        rank_two += comb(occupancy, 2) * height
        rank_three += comb(occupancy, 3)
    return {
        "response": response,
        "rank_one": rank_one,
        "rank_two": rank_two,
        "rank_three": rank_three,
        "total": rank_one + rank_two + rank_three,
    }


def selected_row(selected: dict[str, Any], host_id: str) -> list[Any]:
    rows = [row for row in selected["hosts"] if row[0] == host_id]
    require(len(rows) == 1, f"{host_id}: selected row")
    return rows[0]


def compile_scope(
    selected: dict[str, Any],
    sample: dict[str, Any],
) -> dict[str, Any]:
    profile = sample["profile"]
    host = selected_row(selected, profile["host_id"])
    collision_key = host[7]
    responses = allowed_responses(collision_key)
    scores = [score_response(response, profile["background_points"]) for response in responses]
    scores.sort(key=lambda item: item["response"])
    minimum = min(item["total"] for item in scores)
    face = [item["response"] for item in scores if item["total"] == minimum]
    canonical = host[1]
    canonical_score = next(item["total"] for item in scores if item["response"] == canonical)
    return {
        "host_id": profile["host_id"],
        "collision_key": collision_key,
        "background_points": profile["background_points"],
        "canonical_response_only_selector": canonical,
        "canonical_response_only_minimizer_face": host[2].split(","),
        "response_scores": scores,
        "complete_line_minimum": minimum,
        "complete_line_minimizer_face": face,
        "canonical_selector_complete_line_score": canonical_score,
        "canonical_selector_disadvantage": canonical_score - minimum,
        "canonical_selector_stable": int(canonical in face),
    }


def validate(
    selected: dict[str, Any],
    zero_sample: dict[str, Any],
    blocker_sample: dict[str, Any],
    scores: dict[str, Any],
) -> None:
    require(digest(selected) == EXPECTED_SELECTED_SHA256, "selected digest")
    require(digest(zero_sample) == EXPECTED_ZERO_SAMPLE_SHA256, "zero sample digest")
    require(digest(blocker_sample) == EXPECTED_BLOCKER_SAMPLE_SHA256, "blocker sample digest")
    require(digest(scores) == EXPECTED_SCORES_SHA256, "selector score digest")
    require(
        scores["inputs"]
        == {
            "selected_response_manifest_sha256": EXPECTED_SELECTED_SHA256,
            "zero_sample_sha256": EXPECTED_ZERO_SAMPLE_SHA256,
            "blocker_sample_sha256": EXPECTED_BLOCKER_SAMPLE_SHA256,
        },
        "score input bindings",
    )

    compiled = {
        "zero": compile_scope(selected, zero_sample),
        "blocker": compile_scope(selected, blocker_sample),
    }
    require(scores["rows"] == compiled, "compiled selector score rows")
    require(len(compiled["zero"]["response_scores"]) == 6, "zero response count")
    require(len(compiled["blocker"]["response_scores"]) == 2, "blocker response count")
    require(compiled["zero"]["complete_line_minimizer_face"] == ["2301", "2310", "3201"], "zero minimizer face")
    require(compiled["blocker"]["complete_line_minimizer_face"] == ["3210"], "blocker minimizer face")
    require(compiled["zero"]["canonical_selector_disadvantage"] == 4, "zero selector disadvantage")
    require(compiled["blocker"]["canonical_selector_disadvantage"] == 1, "blocker selector disadvantage")
    require(compiled["zero"]["canonical_selector_stable"] == 0, "zero selector instability")
    require(compiled["blocker"]["canonical_selector_stable"] == 0, "blocker selector instability")

    require(
        scores["aggregate"]
        == {
            "sample_rows": 2,
            "response_scores": 8,
            "canonical_selectors_stable": 0,
            "canonical_selectors_unstable": 2,
            "zero_complete_line_minimizer_count": 3,
            "blocker_complete_line_minimizer_count": 1,
        },
        "score aggregate",
    )
    require(
        scores["conclusion"]
        == {
            "complete_line_scores_require_selector_reoptimization": 1,
            "complete_coupled_selector_resolved": 0,
            "reason": "return collision interface and global child-weight terms are not included in the line/geometric score table",
        },
        "selector conclusion",
    )
    require(
        scores["honesty"]
        == {
            "joint_sample_complete_line_selector_score_tables_complete": 1,
            "joint_sample_canonical_selectors_stable_under_complete_line_score": 0,
            "joint_sample_complete_coupled_selector_terms_complete": 0,
            "joint_sample_full_compulsory_rows_complete": 0,
            "global_binding_constructed": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
        "selector honesty",
    )


def mutation_audit(
    selected: dict[str, Any],
    zero_sample: dict[str, Any],
    blocker_sample: dict[str, Any],
    scores: dict[str, Any],
) -> int:
    mutations = [
        lambda item: item["rows"]["zero"]["response_scores"].pop(),
        lambda item: item["rows"]["zero"]["response_scores"][0].update(total=3),
        lambda item: item["rows"]["zero"].update(complete_line_minimizer_face=["2031"]),
        lambda item: item["rows"]["zero"].update(canonical_selector_stable=1),
        lambda item: item["rows"]["zero"].update(canonical_selector_disadvantage=0),
        lambda item: item["rows"]["blocker"]["response_scores"][0].update(rank_three=0),
        lambda item: item["rows"]["blocker"].update(complete_line_minimum=5),
        lambda item: item["rows"]["blocker"].update(complete_line_minimizer_face=["3012"]),
        lambda item: item["rows"]["blocker"].update(canonical_selector_stable=1),
        lambda item: item["aggregate"].update(response_scores=7),
        lambda item: item["aggregate"].update(canonical_selectors_stable=1),
        lambda item: item["conclusion"].update(complete_coupled_selector_resolved=1),
        lambda item: item["honesty"].update(joint_sample_complete_coupled_selector_terms_complete=1),
        lambda item: item["honesty"].update(joint_sample_full_compulsory_rows_complete=1),
        lambda item: item["honesty"].update(complete_weighted_rows_strict=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(scores)
        mutate(bad)
        try:
            validate(selected, zero_sample, blocker_sample, bad)
        except JointSampleSelectorScoreError:
            rejected += 1
    require(rejected == len(mutations), "selector-score corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    selected = json.loads((root / SELECTED_PATH).read_text(encoding="utf-8"))
    zero_sample = json.loads((root / ZERO_SAMPLE_PATH).read_text(encoding="utf-8"))
    blocker_sample = json.loads((root / BLOCKER_SAMPLE_PATH).read_text(encoding="utf-8"))
    scores = json.loads((root / SCORES_PATH).read_text(encoding="utf-8"))
    validate(selected, zero_sample, blocker_sample, scores)
    print(json.dumps({
        "checker": "prime-power-side-four-joint-sample-complete-line-selector-scores",
        "contract_sha256": EXPECTED_SCORES_SHA256,
        "sample_row_count": 2,
        "response_score_count": 8,
        "canonical_selector_stable_count": 0,
        "canonical_selector_unstable_count": 2,
        "rejected_corruptions": mutation_audit(selected, zero_sample, blocker_sample, scores),
        "joint_sample_complete_line_selector_score_tables_complete": 1,
        "joint_sample_canonical_selectors_stable_under_complete_line_score": 0,
        "joint_sample_complete_coupled_selector_terms_complete": 0,
        "joint_sample_full_compulsory_rows_complete": 0,
        "global_binding_constructed": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()

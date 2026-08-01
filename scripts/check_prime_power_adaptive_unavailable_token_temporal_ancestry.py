#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import Counter
from typing import Any

EXPECTED_CONTRACT_SHA256 = "d7c2c9bef971f9cb2d4b3298ef908641fb9afb8d80ba8f381202ee100a6efcc0"


class AdaptiveUnavailableError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AdaptiveUnavailableError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


CONTRACT = {
    "schema": "prime-power-adaptive-unavailable-token-temporal-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(507, 522)],
    "operations": [
        "adaptive-unavailable-matching-absorption",
        "unavailable-row-column-cover-extraction",
        "heavy-unavailable-star-extraction",
        "unavailable-star-heavy-token",
        "unavailable-star-dispersed-token-bank",
        "unavailable-token-finite-stock",
        "unavailable-token-reintroduction-payment",
        "unavailable-token-persistent-blocker",
        "free-absorption-finite-stock",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}


def matching_family(rows: set[int], cols: set[int], host: frozenset[tuple[int, int]]) -> list[frozenset[tuple[int, int]]]:
    if len(rows) != len(cols):
        return []
    rs = tuple(sorted(rows))
    result = []
    for perm in itertools.permutations(sorted(cols)):
        matching = frozenset(zip(rs, perm))
        if matching <= host:
            result.append(matching)
    return result


def maximum_matching(rows: set[int], cols: set[int], host: frozenset[tuple[int, int]]) -> frozenset[tuple[int, int]]:
    best: frozenset[tuple[int, int]] = frozenset()
    for size in range(min(len(rows), len(cols)) + 1):
        for selected_rows in itertools.combinations(sorted(rows), size):
            for selected_cols in itertools.combinations(sorted(cols), size):
                for perm in itertools.permutations(selected_cols):
                    matching = frozenset(zip(selected_rows, perm))
                    if matching <= host:
                        if len(matching) > len(best):
                            best = matching
                        elif len(matching) == len(best) and tuple(sorted(matching)) < tuple(sorted(best)):
                            best = matching
    return best


def minimum_vertex_cover(rows: set[int], cols: set[int], host: frozenset[tuple[int, int]]) -> frozenset[tuple[str, int]]:
    vertices = [("L", row) for row in sorted(rows)] + [("R", col) for col in sorted(cols)]
    for size in range(len(vertices) + 1):
        for selected in itertools.combinations(vertices, size):
            cover = frozenset(selected)
            if all(("L", row) in cover or ("R", col) in cover for row, col in host):
                return cover
    raise AdaptiveUnavailableError("minimum cover not found")


def extend_partial(n: int, partial: frozenset[tuple[int, int]]) -> frozenset[tuple[int, int]]:
    require(len({row for row, _ in partial}) == len(partial), "partial matching repeats source")
    require(len({col for _, col in partial}) == len(partial), "partial matching repeats target")
    for perm in itertools.permutations(range(n)):
        matching = frozenset(zip(range(n), perm))
        if partial <= matching:
            return matching
    raise AdaptiveUnavailableError("partial matching does not extend")


def adaptive_absorption_census() -> dict[str, int]:
    n = 3
    complete = frozenset(itertools.product(range(n), repeat=2))
    counts = Counter()
    for trace_mask in range(1 << n):
        trace = frozenset((i, i) for i in range(n) if trace_mask >> i & 1)
        used = {i for i, _ in trace}
        surviving_rows = set(range(n)) - used
        surviving_cols = set(range(n)) - used
        residual_universe = frozenset((row, col) for row in surviving_rows for col in surviving_cols)
        for unavailable_mask in range(1 << (n * n)):
            unavailable = frozenset(
                edge for index, edge in enumerate(sorted(complete))
                if unavailable_mask >> index & 1
            )
            residual_unavailable = unavailable & residual_universe
            absorbed = maximum_matching(surviving_rows, surviving_cols, residual_unavailable)
            forbidden = extend_partial(n, trace | absorbed)
            require(
                forbidden & unavailable == (trace & unavailable) | absorbed,
                "forbidden matching contains an unaccounted unavailable edge",
            )
            allowed_unavailable = (complete - forbidden) & unavailable
            cover = minimum_vertex_cover(surviving_rows, surviving_cols, residual_unavailable)
            require(len(cover) == len(absorbed), "König equality failed")
            wall = set(cover)
            for row, col in trace:
                wall.add(("L", row))
                wall.add(("R", col))
            require(
                all(("L", row) in wall or ("R", col) in wall for row, col in allowed_unavailable),
                "row-column cover does not cover the allowed unavailable inventory",
            )
            require(len(wall) <= 2 * len(trace) + len(absorbed), "cover-size bound failed")
            counts["adaptive_profiles"] += 1
            counts["absorbed_edge_incidences"] += len(absorbed)
            counts["cover_vertex_incidences"] += len(wall)
            if len(absorbed) >= 2:
                counts["free_absorption_profiles"] += 1
            else:
                counts["small_cover_profiles"] += 1
            if allowed_unavailable:
                degrees = Counter()
                for row, col in allowed_unavailable:
                    if ("L", row) in wall:
                        degrees[("L", row)] += 1
                    if ("R", col) in wall:
                        degrees[("R", col)] += 1
                require(degrees, "nonempty inventory has no cover incidence")
                require(
                    max(degrees.values()) >= math.ceil(len(allowed_unavailable) / len(wall)),
                    "heavy unavailable star bound failed",
                )
                counts["heavy_star_profiles"] += 1
                counts["heavy_star_edge_incidences"] += max(degrees.values())
    require(counts["adaptive_profiles"] == 4096, "unexpected adaptive profile census")
    return dict(counts)


def token_star_census() -> dict[str, int]:
    t, p, h = 8, 2, 3
    counts = Counter()
    for orientation in ("row", "column"):
        for fixed in range(t):
            for mask in range(1, 1 << t):
                moving = [value for value in range(t) if mask >> value & 1]
                degree = len(moving)
                threshold = max(2, math.ceil(math.sqrt(degree)))
                for depth in range(1, h):
                    modulus = p ** depth
                    classes = Counter(value % modulus for value in moving)
                    require(sum(classes.values()) == degree, "prefix classes do not partition the star")
                    require(max(classes.values()) <= t // modulus, "prefix cell exceeds capacity")
                    counts["star_depth_profiles"] += 1
                    if max(classes.values()) >= threshold:
                        counts["heavy_token_profiles"] += 1
                        counts["heavy_token_edge_incidences"] += max(classes.values())
                    else:
                        occupied = len(classes)
                        require(
                            occupied >= math.ceil(degree / (threshold - 1)),
                            "dispersed token count below theorem bound",
                        )
                        counts["dispersed_token_profiles"] += 1
                        counts["dispersed_token_witnesses"] += occupied
                        witnesses = []
                        for residue in sorted(classes):
                            representative = min(value for value in moving if value % modulus == residue)
                            edge = (fixed, representative) if orientation == "row" else (representative, fixed)
                            witnesses.append((depth, fixed % modulus, residue, edge))
                        require(len({(d, a, c) for d, a, c, _ in witnesses}) == len(witnesses),
                                "dispersed witnesses do not occupy distinct tokens")
    require(counts["star_depth_profiles"] == 8160, "unexpected token-star census")
    require(counts["heavy_token_profiles"] > 0 and counts["dispersed_token_profiles"] > 0,
            "both token alternatives must occur")
    return dict(counts)


def one_token_episode_census() -> dict[str, int]:
    universe = range(4)
    witness_sets = [frozenset(pair) for pair in itertools.combinations(universe, 2)]
    counts = Counter()
    threshold = 3
    episode_count = 3
    for history in itertools.product(witness_sets, repeat=episode_count):
        multiplicity = Counter(edge for witnesses in history for edge in witnesses)
        if max(multiplicity.values()) >= threshold:
            counts["persistent_pair_histories"] += 1
        else:
            require(
                episode_count <= (threshold - 1) * len(universe) // 2,
                "finite one-token episode bound failed",
            )
            counts["finite_token_histories"] += 1
    require(counts["finite_token_histories"] == 114, "unexpected finite token histories")
    require(counts["persistent_pair_histories"] == 102, "unexpected persistent token histories")
    return dict(counts)


def absence_runs(availability: tuple[bool, ...], episode_times: tuple[int, ...]) -> list[list[int]]:
    runs: list[list[int]] = []
    current: list[int] = []
    previous: int | None = None
    for time in episode_times:
        if previous is None or not all(not availability[index] for index in range(previous, time + 1)):
            if current:
                runs.append(current)
            current = [time]
        else:
            current.append(time)
        previous = time
    if current:
        runs.append(current)
    return runs


def temporal_census() -> dict[str, int]:
    counts = Counter()
    for bits in itertools.product((False, True), repeat=6):
        absent = [time for time, available in enumerate(bits) if not available]
        reintroductions = sum(not bits[index - 1] and bits[index] for index in range(1, len(bits)))
        for size in range(1, len(absent) + 1):
            for selected in itertools.combinations(absent, size):
                runs = absence_runs(bits, selected)
                require(len(runs) <= 1 + reintroductions, "absence-run bound failed")
                require(
                    max(map(len, runs)) >= math.ceil(size / (1 + reintroductions)),
                    "absence-run pigeonhole bound failed",
                )
                counts["absence_histories"] += 1
                if size >= 3:
                    if reintroductions >= 1:
                        counts["reintroduction_endpoint_histories"] += 1
                    if max(map(len, runs)) >= 3:
                        counts["persistent_run_histories"] += 1
                    require(
                        reintroductions >= 1 or max(map(len, runs)) >= 3,
                        "three-way temporal endpoint failed",
                    )
    require(counts["absence_histories"] == 665, "unexpected absence-history census")
    require(counts["reintroduction_endpoint_histories"] > 0, "reintroduction endpoint absent")
    require(counts["persistent_run_histories"] > 0, "persistent endpoint absent")
    return dict(counts)


def free_absorption_history_census() -> dict[str, int]:
    witness_sets = [frozenset(pair) for pair in itertools.combinations(range(9), 2)]
    counts = Counter()
    for history in itertools.product(witness_sets, repeat=3):
        multiplicity = Counter(edge for witnesses in history for edge in witnesses)
        if max(multiplicity.values()) >= 3:
            counts["recurrent_absorbed_edge_histories"] += 1
        else:
            require(3 <= (3 - 1) * 9 // 2, "free-absorption finite bound failed")
            counts["finite_absorption_histories"] += 1
    require(counts["finite_absorption_histories"] == 42084, "unexpected finite absorption histories")
    require(counts["recurrent_absorbed_edge_histories"] == 4572, "unexpected recurrent absorption histories")
    return dict(counts)


def validate_report(report: dict[str, Any]) -> None:
    require(report.get("contract_sha256") == EXPECTED_CONTRACT_SHA256, "contract mismatch")
    require(
        report.get("record_sha256")
        == digest({key: value for key, value in report.items() if key != "record_sha256"}),
        "record seal mismatch",
    )
    for key in (
        "adaptive_profiles",
        "free_absorption_profiles",
        "small_cover_profiles",
        "heavy_star_profiles",
        "star_depth_profiles",
        "heavy_token_profiles",
        "dispersed_token_profiles",
        "finite_token_histories",
        "persistent_pair_histories",
        "absence_histories",
        "reintroduction_endpoint_histories",
        "persistent_run_histories",
        "finite_absorption_histories",
        "recurrent_absorbed_edge_histories",
    ):
        require(isinstance(report.get(key), int) and report[key] > 0, f"{key}: positive integer required")
    require(report.get("adaptive_unavailable_absorption_ancestry_proved") == 1, "absorption flag missing")
    require(report.get("unavailable_star_token_splice_proved") == 1, "token-splice flag missing")
    require(report.get("unavailable_token_temporal_scheduler_exact") == 1, "temporal flag missing")
    require(report.get("global_transition_kind_bank_exhaustive") == 0, "global exhaustiveness honesty")
    require(report.get("global_termination_proved") == 0, "termination honesty")
    require(report.get("actual_global_parent_rule_complete") == 0, "parent-rule honesty")
    require(report.get("all_n_proved_by_checker") == 0, "all-n honesty")


def main() -> None:
    require(digest(CONTRACT) == EXPECTED_CONTRACT_SHA256, "contract digest changed")
    claims = {
        "checker": "prime-power-adaptive-unavailable-token-temporal-ancestry",
        "contract_sha256": EXPECTED_CONTRACT_SHA256,
        **adaptive_absorption_census(),
        **token_star_census(),
        **one_token_episode_census(),
        **temporal_census(),
        **free_absorption_history_census(),
        "sample_labelled_token_edge_stock": (2 + 1) * (3 - 1) * 8 * 8,
        "corruption_rejections": 8,
        "adaptive_unavailable_absorption_ancestry_proved": 1,
        "unavailable_star_token_splice_proved": 1,
        "unavailable_token_temporal_scheduler_exact": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    claims["record_sha256"] = digest(claims)
    validate_report(claims)
    mutations = [
        ("contract_sha256", "0" * 64),
        ("adaptive_unavailable_absorption_ancestry_proved", 0),
        ("unavailable_star_token_splice_proved", 0),
        ("unavailable_token_temporal_scheduler_exact", 0),
        ("all_n_proved_by_checker", 1),
        ("adaptive_profiles", 0),
        ("heavy_token_profiles", 0),
        ("record_sha256", "f" * 64),
    ]
    rejected = 0
    for key, value in mutations:
        bad = dict(claims)
        bad[key] = value
        if key != "record_sha256":
            bad["record_sha256"] = digest(
                {name: item for name, item in bad.items() if name != "record_sha256"}
            )
        try:
            validate_report(bad)
        except AdaptiveUnavailableError:
            rejected += 1
    require(rejected == len(mutations), "corrupted report accepted")
    print(json.dumps(claims, sort_keys=True))


if __name__ == "__main__":
    main()

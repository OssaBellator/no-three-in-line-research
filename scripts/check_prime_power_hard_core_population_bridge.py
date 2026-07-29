#!/usr/bin/env python3
"""Bridge literal T03 hard-core populations to the exact T21 scalar selector.

The checker consumes a T03 slot/candidate-population certificate, identifies slots
whose independently expected host is one of the eleven side-four hard-core hosts,
validates literal survivor backgrounds and response families, recomputes the exact
pivot-line energy, and requires a canonical selector-data projection.

This is a population/selector consistency bridge only. It does not supply the
actual parent rule or any genuine population data, does not prove the T03 payloads
mathematically correct, and permanently reports all_n_proved_by_checker=0.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
from typing import Any, Iterable

Edge = tuple[int, int]
Point = tuple[int, int]
Line = tuple[int, int, int]
Permutation = tuple[int, ...]

GRID = {(x, y) for x in range(4) for y in range(4)}
Q_ONE: Permutation = (3, 0, 1, 2)
Q_FOUR: Permutation = (3, 2, 1, 0)
K_MINUS: Line = (1, -1, -1)
K_PLUS: Line = (1, 1, -3)
K_30: Line = (3, 1, -3)
K_03: Line = (1, 3, -9)
RELEVANT_LINES = (K_MINUS, K_PLUS, K_30, K_03)
LINE_WEIGHTS = {K_MINUS: 3, K_PLUS: -5, K_30: 1, K_03: 1}
POSITIVE_PIVOTS: tuple[Point, Point] = ((3, 2), (1, 0))
NEGATIVE_PIVOTS: tuple[Point, Point] = ((3, 0), (1, 2))
EXPECTED_CONTRACT_SHA256 = "c7773e0f18779f6fa89db7d31e802c281e4e2618e60096a9a3d86471d08d528c"


class HardCorePopulationBridgeError(ValueError):
    """Raised when a T03-to-T21 hard-core bridge is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HardCorePopulationBridgeError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def partial_matchings(edges: Iterable[Edge]) -> list[tuple[Edge, ...]]:
    edge_list = sorted(edges)
    output: list[tuple[Edge, ...]] = []

    def recurse(index: int, chosen: list[Edge], left_used: set[int], right_used: set[int]) -> None:
        if index == len(edge_list):
            output.append(tuple(chosen))
            return
        recurse(index + 1, chosen, left_used, right_used)
        left, right = edge_list[index]
        if left not in left_used and right not in right_used:
            chosen.append((left, right))
            left_used.add(left)
            right_used.add(right)
            recurse(index + 1, chosen, left_used, right_used)
            right_used.remove(right)
            left_used.remove(left)
            chosen.pop()

    recurse(0, [], set(), set())
    return output


def perfect_matchings(side: int, forbidden: set[Edge]) -> list[Permutation]:
    return [
        permutation
        for permutation in permutations(range(side))
        if all((left, permutation[left]) not in forbidden for left in range(side))
    ]


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def response_triples(permutation: Permutation) -> int:
    points = [(left, permutation[left]) for left in range(len(permutation))]
    return sum(collinear(*triple) for triple in combinations(points, 3))


def host_identity(deletion: tuple[Edge, ...]) -> str:
    core = {"side": 4, "deletion_edges": [list(edge) for edge in deletion]}
    return f"s4-{canonical_digest(core)[:16]}"


def hard_core_hosts() -> list[dict[str, Any]]:
    side = 4
    diagonal = {(index, index) for index in range(side)}
    target = {(0, 1)}
    admissible = {
        (left, right)
        for left in range(side)
        for right in range(side)
    } - diagonal - target
    output: list[dict[str, Any]] = []
    for deletion in partial_matchings(admissible):
        responses = perfect_matchings(side, diagonal | target | set(deletion))
        if not responses:
            continue
        if min(response_triples(response) for response in responses) == 0:
            continue
        require(
            responses in ([Q_ONE, Q_FOUR], [Q_FOUR]),
            f"unexpected hard-core response family: {responses}",
        )
        output.append(
            {
                "host_id": host_identity(deletion),
                "deletion_edges": [list(edge) for edge in deletion],
                "response_family": [list(response) for response in responses],
            }
        )
    require(len(output) == 11, "hard-core host census drift")
    require(sum(len(host["response_family"]) == 2 for host in output) == 9, "two-response host census drift")
    require(sum(len(host["response_family"]) == 1 for host in output) == 2, "singleton host census drift")
    return output


def normalized_line(first: Point, second: Point) -> Line:
    require(first != second, "line requires distinct points")
    x1, y1 = first
    x2, y2 = second
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "degenerate line")
    a //= divisor
    b //= divisor
    c //= divisor
    for value in (a, b, c):
        if value < 0:
            a, b, c = -a, -b, -c
            break
        if value > 0:
            break
    return a, b, c


def on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def point_weight(point: Point) -> int:
    return sum(LINE_WEIGHTS[line] * int(on_line(point, line)) for line in RELEVANT_LINES)


def pivot_energy(pivot: Point, background: tuple[Point, ...]) -> int:
    counts = Counter(normalized_line(pivot, point) for point in background)
    return sum(count * (count - 1) // 2 for count in counts.values())


def energy_terms(background: tuple[Point, ...]) -> dict[str, int]:
    positive = sum(pivot_energy(pivot, background) for pivot in POSITIVE_PIVOTS)
    negative = sum(pivot_energy(pivot, background) for pivot in NEGATIVE_PIVOTS)
    weight = sum(point_weight(point) for point in background)
    return {
        "positive_pivot_energy": positive,
        "negative_pivot_energy": negative,
        "point_weight_sum": weight,
        "delta_q1_minus_q4": positive - negative + weight - 3,
    }


def exact_background(raw: Any, path: str) -> tuple[Point, ...]:
    require(isinstance(raw, list), f"{path}: list required")
    points: list[Point] = []
    for index, item in enumerate(raw):
        require(isinstance(item, list) and len(item) == 2, f"{path}[{index}]: integer pair required")
        x, y = item
        require(
            isinstance(x, int) and not isinstance(x, bool)
            and isinstance(y, int) and not isinstance(y, bool),
            f"{path}[{index}]: integer coordinates required",
        )
        point = (x, y)
        require(point not in GRID, f"{path}[{index}]: response-grid point forbidden")
        points.append(point)
    require(len(points) == len(set(points)), f"{path}: duplicate point")
    return tuple(sorted(points))


def exact_selector_data(host: dict[str, Any], background: tuple[Point, ...]) -> dict[str, Any]:
    terms = energy_terms(background)
    family = [tuple(response) for response in host["response_family"]]
    if family == [Q_ONE, Q_FOUR]:
        selected = Q_ONE if terms["delta_q1_minus_q4"] <= 0 else Q_FOUR
        condition = "delta_le_zero" if selected == Q_ONE else "delta_gt_zero"
    elif family == [Q_FOUR]:
        selected = Q_FOUR
        condition = "all_signatures"
    else:
        raise HardCorePopulationBridgeError("unsupported hard-core response family")
    output = {
        "selector_kind": "side-four-hard-core-exchange-v1",
        "hard_core_host_id": host["host_id"],
        "survivor_background_sha256": canonical_digest([list(point) for point in background]),
        "survivor_background_points": len(background),
        **terms,
        "selected_response": list(selected),
        "selector_condition": condition,
    }
    output["hard_core_selector_sha256"] = canonical_digest(output)
    return output


def exact_bridge_record(
    slot: dict[str, Any],
    status_record: dict[str, Any],
    payload: dict[str, Any] | None,
    host: dict[str, Any],
) -> dict[str, Any]:
    slot_id = slot.get("slot_id")
    require(isinstance(slot_id, str) and slot_id, "slot_id required")
    require(slot.get("expected_host_id") == host["host_id"], f"{slot_id}: hard-core host mismatch")
    require(status_record.get("slot_id") == slot_id, f"{slot_id}: status record mismatch")
    status = status_record.get("status")
    require(status in {"open", "populated", "proved"}, f"{slot_id}: bad status")

    output: dict[str, Any] = {
        "slot_id": slot_id,
        "slot_sha256": slot.get("slot_sha256"),
        "hard_core_host_id": host["host_id"],
        "status": status,
    }
    if status == "open":
        require(payload is None, f"{slot_id}: open hard-core slot cannot have payload")
        output.update(
            {
                "bridge_status": "awaiting_population",
                "fibre_id": None,
                "slot_population_payload_sha256": None,
                "selector_data": None,
            }
        )
    else:
        require(isinstance(payload, dict), f"{slot_id}: non-open hard-core slot requires payload")
        require(payload.get("slot_id") == slot_id, f"{slot_id}: payload slot mismatch")
        require(payload.get("host_id") == host["host_id"], f"{slot_id}: payload host mismatch")
        population_data = payload.get("population_data")
        require(isinstance(population_data, dict), f"{slot_id}: population_data required")
        require(
            population_data.get("response_family") == host["response_family"],
            f"{slot_id}: exact hard-core response family required",
        )
        background = exact_background(
            population_data.get("survivor_background"),
            f"{slot_id}.survivor_background",
        )
        selector = exact_selector_data(host, background)
        require(
            population_data.get("selector_data") == selector,
            f"{slot_id}: selector_data does not match exact hard-core projection",
        )
        output.update(
            {
                "bridge_status": "scalar_projection_ready",
                "fibre_id": payload.get("fibre_id"),
                "slot_population_payload_sha256": payload.get("slot_population_payload_sha256"),
                "selector_data": selector,
            }
        )
    output["hard_core_population_bridge_record_sha256"] = canonical_digest(output)
    return output


def exact_bridge_manifest(
    slots: list[dict[str, Any]],
    records: list[dict[str, Any]],
    payloads: list[dict[str, Any]],
) -> dict[str, Any]:
    require(isinstance(slots, list), "slots must be a list")
    require(isinstance(records, list), "records must be a list")
    require(isinstance(payloads, list), "payloads must be a list")
    host_map = {host["host_id"]: host for host in hard_core_hosts()}
    record_by_slot = {record.get("slot_id"): record for record in records}
    require(len(record_by_slot) == len(records), "duplicate status-record slot")
    payload_groups: dict[str, list[dict[str, Any]]] = {}
    for payload in payloads:
        payload_groups.setdefault(payload.get("slot_id"), []).append(payload)
    require(all(len(group) == 1 for group in payload_groups.values()), "duplicate population payload for slot")

    bridge_records: list[dict[str, Any]] = []
    for slot in slots:
        host = host_map.get(slot.get("expected_host_id"))
        if host is None:
            continue
        slot_id = slot.get("slot_id")
        require(slot_id in record_by_slot, f"{slot_id}: missing population status record")
        group = payload_groups.get(slot_id, [])
        require(len(group) <= 1, f"{slot_id}: duplicate payload")
        payload = group[0] if group else None
        bridge_records.append(exact_bridge_record(slot, record_by_slot[slot_id], payload, host))

    status_counts = Counter(record["status"] for record in bridge_records)
    selected_counts = Counter(
        tuple(record["selector_data"]["selected_response"])
        for record in bridge_records
        if record["selector_data"] is not None
    )
    claims = {
        "hard_core_hosts": len(host_map),
        "hard_core_slots": len(bridge_records),
        "open_hard_core_slots": status_counts["open"],
        "data_populated_hard_core_slots": status_counts["populated"],
        "t03_proved_hard_core_slots": status_counts["proved"],
        "scalar_projection_ready_slots": sum(record["bridge_status"] == "scalar_projection_ready" for record in bridge_records),
        "Q1_selected_slots": selected_counts[Q_ONE],
        "Q4_selected_slots": selected_counts[Q_FOUR],
        "all_hard_core_slots_scalar_ready": int(bool(bridge_records) and status_counts["open"] == 0),
        "all_hard_core_slots_t03_proved": int(bool(bridge_records) and status_counts["proved"] == len(bridge_records)),
        "t21_semantic_chambers_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    output: dict[str, Any] = {
        "version": 1,
        "hard_core_host_ids": sorted(host_map),
        "hard_core_population_bridge_records": bridge_records,
        "claims": claims,
    }
    output["manifest_sha256"] = canonical_digest(output)
    return output


def validate_bridge_manifest(
    manifest: Any,
    slots: list[dict[str, Any]],
    records: list[dict[str, Any]],
    payloads: list[dict[str, Any]],
) -> dict[str, int]:
    require(isinstance(manifest, dict), "bridge manifest must be an object")
    expected = exact_bridge_manifest(slots, records, payloads)
    require(manifest == expected, "canonical hard-core population bridge mismatch")
    return copy.deepcopy(expected["claims"])


def bridge_contract_manifest() -> dict[str, Any]:
    hosts = hard_core_hosts()
    output: dict[str, Any] = {
        "version": 1,
        "bridge_kind": "t03-hard-core-population-to-t21-scalar-v1",
        "hard_core_host_ids": sorted(host["host_id"] for host in hosts),
        "two_response_hosts": sum(len(host["response_family"]) == 2 for host in hosts),
        "singleton_response_hosts": sum(len(host["response_family"]) == 1 for host in hosts),
        "required_population_fields": [
            "survivor_background",
            "response_family",
            "selector_data",
        ],
        "selector_data_fields": [
            "selector_kind",
            "hard_core_host_id",
            "survivor_background_sha256",
            "survivor_background_points",
            "positive_pivot_energy",
            "negative_pivot_energy",
            "point_weight_sum",
            "delta_q1_minus_q4",
            "selected_response",
            "selector_condition",
            "hard_core_selector_sha256",
        ],
        "claims": {
            "hard_core_hosts": 11,
            "hard_core_chambers": 20,
            "actual_parent_rule_present": 0,
            "actual_t03_population_supplied_by_bridge": 0,
            "t21_semantic_chambers_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    output["contract_sha256"] = canonical_digest(output)
    return output


def validate_contract() -> dict[str, int]:
    contract = bridge_contract_manifest()
    require(contract["claims"]["hard_core_hosts"] == 11, "contract hard-core host census drift")
    require(contract["claims"]["hard_core_chambers"] == 20, "contract chamber census drift")
    if EXPECTED_CONTRACT_SHA256 != "TO_BE_FILLED":
        require(contract["contract_sha256"] == EXPECTED_CONTRACT_SHA256, "built-in contract digest drift")
    return copy.deepcopy(contract["claims"])


def fixture_inputs(all_proved: bool = False) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    slots: list[dict[str, Any]] = []
    records: list[dict[str, Any]] = []
    payloads: list[dict[str, Any]] = []
    hosts = hard_core_hosts()
    for index, host in enumerate(hosts):
        slot_core = {
            "parent_state_id": f"fixture-parent-{index:02d}",
            "operation_kind": "fixture-hard-core-population",
            "operation_key": {"ordinal": index},
            "expected_host_id": host["host_id"],
            "state_labels": {"fixture": f"host-{index:02d}"},
        }
        slot_id = f"fixture-slot-{index:02d}"
        slot = {**slot_core, "slot_id": slot_id}
        slot["slot_sha256"] = canonical_digest(slot)
        slots.append(slot)
        status = "proved" if all_proved else ("open" if index < 3 else "populated" if index < 7 else "proved")
        record = {
            "slot_id": slot_id,
            "slot_sha256": slot["slot_sha256"],
            "status": status,
        }
        records.append(record)
        if status == "open":
            continue
        if index % 2 == 0:
            background: tuple[Point, ...] = ()
        else:
            background = ((-1, -2), (4, 3))
        selector = exact_selector_data(host, background)
        population_data = {
            "points": [],
            "removals": [],
            "survivor_background": [list(point) for point in background],
            "owner_fate_witnesses": [],
            "response_family": copy.deepcopy(host["response_family"]),
            "feasibility_signatures": [],
            "selector_data": selector,
            "labelled_vectors": [],
            "routed_credits": [],
            "row_loads": [],
            "transitions": [],
        }
        source_sha256 = canonical_digest(population_data)
        payload = {
            "slot_id": slot_id,
            "host_id": host["host_id"],
            "fibre_id": f"{host['host_id']}:{source_sha256[:16]}",
            "population_data": population_data,
            "source_sha256": source_sha256,
        }
        payload["slot_population_payload_sha256"] = canonical_digest(payload)
        payloads.append(payload)
    return slots, records, payloads


def self_test() -> dict[str, Any]:
    contract_claims = validate_contract()
    mixed = fixture_inputs(all_proved=False)
    mixed_manifest = exact_bridge_manifest(*mixed)
    mixed_claims = validate_bridge_manifest(mixed_manifest, *mixed)
    require(
        (
            mixed_claims["hard_core_slots"],
            mixed_claims["open_hard_core_slots"],
            mixed_claims["data_populated_hard_core_slots"],
            mixed_claims["t03_proved_hard_core_slots"],
            mixed_claims["scalar_projection_ready_slots"],
        )
        == (11, 3, 4, 4, 8),
        "mixed fixture census drift",
    )

    complete = fixture_inputs(all_proved=True)
    complete_manifest = exact_bridge_manifest(*complete)
    complete_claims = validate_bridge_manifest(complete_manifest, *complete)
    require(complete_claims["all_hard_core_slots_scalar_ready"] == 1, "complete scalar readiness drift")
    require(complete_claims["all_hard_core_slots_t03_proved"] == 1, "complete T03 readiness drift")
    require(complete_claims["t21_semantic_chambers_proved"] == 0, "semantic honesty drift")

    mutations: list[tuple[str, Any]] = []

    def input_mutation(name: str, mutator: Any) -> None:
        slots, records, payloads = copy.deepcopy(complete)
        mutator(slots, records, payloads)
        mutations.append((name, ("input", slots, records, payloads)))

    input_mutation(
        "duplicate-background-point",
        lambda s, r, p: p[0]["population_data"]["survivor_background"].extend([[-1, -2], [-1, -2]]),
    )
    input_mutation(
        "response-grid-background-point",
        lambda s, r, p: p[0]["population_data"].update(survivor_background=[[0, 0]]),
    )
    input_mutation(
        "response-family-corruption",
        lambda s, r, p: p[0]["population_data"].update(response_family=[list(Q_FOUR)]),
    )
    input_mutation(
        "selector-delta-corruption",
        lambda s, r, p: p[0]["population_data"]["selector_data"].update(delta_q1_minus_q4=99),
    )
    input_mutation(
        "selector-response-corruption",
        lambda s, r, p: p[1]["population_data"]["selector_data"].update(selected_response=list(Q_ONE)),
    )
    input_mutation(
        "payload-host-corruption",
        lambda s, r, p: p[0].update(host_id="s4-corrupt"),
    )
    input_mutation(
        "open-payload-corruption",
        lambda s, r, p: r[0].update(status="open"),
    )
    input_mutation(
        "missing-status-record",
        lambda s, r, p: r.pop(),
    )

    corrupt_manifest = copy.deepcopy(complete_manifest)
    corrupt_manifest["claims"]["all_n_proved_by_checker"] = 1
    mutations.append(("honesty-claim-corruption", ("manifest", corrupt_manifest)))
    corrupt_manifest = copy.deepcopy(complete_manifest)
    corrupt_manifest["manifest_sha256"] = "0" * 64
    mutations.append(("manifest-seal-corruption", ("manifest", corrupt_manifest)))

    rejected = 0
    for name, mutation in mutations:
        try:
            if mutation[0] == "input":
                _, slots, records, payloads = mutation
                exact_bridge_manifest(slots, records, payloads)
            else:
                validate_bridge_manifest(mutation[1], *complete)
        except HardCorePopulationBridgeError:
            rejected += 1
        else:
            raise HardCorePopulationBridgeError(f"mutation accepted: {name}")
    require(rejected == 10, "mutation rejection census drift")

    return {
        **contract_claims,
        "mixed_hard_core_slots": mixed_claims["hard_core_slots"],
        "mixed_open_slots": mixed_claims["open_hard_core_slots"],
        "mixed_scalar_ready_slots": mixed_claims["scalar_projection_ready_slots"],
        "complete_scalar_ready_slots": complete_claims["scalar_projection_ready_slots"],
        "rejected_mutations": rejected,
        "contract_sha256": bridge_contract_manifest()["contract_sha256"],
    }


def certificate_slots(certificate: dict[str, Any]) -> list[dict[str, Any]]:
    try:
        return certificate[
            "rule_exhaustiveness_frontier_certificate"
        ][
            "source_truth_frontier_execution_certificate"
        ][
            "source_statement_truth_registry_certificate"
        ][
            "rule_source_provenance_certificate"
        ][
            "clause_manifest"
        ][
            "expected_slot_registry"
        ][
            "slots"
        ]
    except (KeyError, TypeError) as error:
        raise HardCorePopulationBridgeError("unable to locate exact expected-slot registry in T03 certificate") from error


def bridge_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    try:
        import check_prime_power_slot_candidate_population_frontier as t03
    except ImportError as error:
        raise HardCorePopulationBridgeError("T03 checker import failed") from error
    t03.validate_certificate(certificate)
    exact = t03.exact_certificate(certificate)
    return exact_bridge_manifest(
        certificate_slots(certificate),
        exact["slot_population_records"],
        exact["slot_population_payloads"],
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", help="T03 slot/candidate-population certificate JSON")
    parser.add_argument("--self-test", action="store_true", help="run canonical bridge fixtures and mutations")
    parser.add_argument("--write", type=Path, help="write the derived bridge manifest")
    args = parser.parse_args()

    if args.self_test:
        require(args.certificate is None, "--self-test does not accept a certificate")
        require(args.write is None, "--self-test does not write a certificate-derived manifest")
        print(json.dumps(self_test(), sort_keys=True))
        return

    require(args.certificate is not None, "certificate path required unless --self-test is used")
    certificate = json.loads(Path(args.certificate).read_text(encoding="utf-8"))
    manifest = bridge_certificate(certificate)
    if args.write is not None:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest["claims"], sort_keys=True))


if __name__ == "__main__":
    main()

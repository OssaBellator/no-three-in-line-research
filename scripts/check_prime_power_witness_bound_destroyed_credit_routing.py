#!/usr/bin/env python3
"""Bind response-local destroyed credits to literal triples and child-bearing witnesses.

CMR2142--CMR2149 permit a response-local child credit vector whose total does not exceed
the literal destroyed-current-triple count. This checker replaces each positive unit by
an explicit injective assignment

    literal destroyed triple -> nondeleted witness occurring in the response -> child.

Within one response neither a destroyed triple nor a target witness may be reused. The
child counts must equal the linked recurrent-row credit vector exactly. The same unit
may appear in different responses because responses are alternative operations.

Passing this checker proves literal witness-bound accounting relative to the accepted
owner/fate manifest. It does not prove that the manifest's child labels have their
intended external semantics or that credits may be reused across simultaneous rows.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_direct_response_triple_delta as direct
import check_geometric_owner_fate_manifest as owner_fate
import check_prime_power_background_signature as signature
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_labelled_recurrent_row_margin as row_margin
import check_prime_power_labelled_weight_exposure as exposure
import check_prime_power_linked_operation_selector as linked


class WitnessRoutingError(ValueError):
    """Raised when literal destroyed-credit routing is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise WitnessRoutingError(message)


def response_key(response: list[list[int]]) -> tuple[tuple[int, int], ...]:
    return row_margin.response_key(response)


def prescription_from_fate(rank: int, record: dict[str, Any]) -> tuple[tuple[int, int], ...]:
    if rank == 1:
        return (tuple(record["response"]),)
    return tuple(sorted(tuple(edge) for edge in record["response"]))


def witness_payload(rank: int, record: dict[str, Any]) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "rank": rank,
        "prescription": [list(edge) for edge in prescription_from_fate(rank, record)],
        "owner": record["owner"],
        "kind": record["kind"],
        "child": record.get("child"),
    }
    if rank == 1:
        payload["background_pair"] = record["background_pair"]
    elif rank == 2:
        payload["background_point"] = record["background_point"]
    if record.get("multiplicity") is not None:
        payload["multiplicity"] = record["multiplicity"]
    payload["witness_id"] = f"witness-{catalogue.canonical_digest(payload)[:24]}"
    return payload


def exact_destroyed_records(linked_certificate: dict[str, Any]) -> list[dict[str, Any]]:
    pool_manifest = linked_certificate["direct_delta_certificate"]["pool_certificate"]["pool_manifest"]
    points = [tuple(point) for point in pool_manifest["pre_response_points"]]
    removed = set(pool_manifest["removed_point_indices"])
    destroyed_indices = sorted(
        triple for triple in direct.collinear_triples(points) if any(index in removed for index in triple)
    )
    records = []
    for triple in destroyed_indices:
        core = {
            "point_indices": list(triple),
            "points": [list(points[index]) for index in triple],
            "removed_point_indices": [index for index in triple if index in removed],
        }
        record = copy.deepcopy(core)
        record["destroyed_id"] = f"destroyed-{catalogue.canonical_digest(core)[:24]}"
        record["destroyed_record_sha256"] = catalogue.canonical_digest(record)
        records.append(record)
    claims = linked.exact_composition(linked_certificate)["claims"]
    require(len(records) == claims["destroyed_current_triples"], "literal destroyed record count mismatch")
    require(len({record["destroyed_id"] for record in records}) == len(records), "destroyed ID collision")
    return records


def exact_witness_records(source_manifest: dict[str, Any]) -> list[dict[str, Any]]:
    owner_fate.validate_manifest(source_manifest)
    records = []
    for rank, name in ((1, "rank1"), (2, "rank2"), (3, "rank3")):
        for fate in source_manifest["fates"][name]:
            if fate["kind"] == "deleted":
                continue
            payload = witness_payload(rank, fate)
            payload["witness_record_sha256"] = catalogue.canonical_digest(payload)
            records.append(payload)
    records.sort(key=lambda record: record["witness_id"])
    require(len({record["witness_id"] for record in records}) == len(records), "witness ID collision")
    return records


def exact_route_assignment(raw: dict[str, Any], destroyed_by_id: dict[str, dict[str, Any]],
                           witness_by_id: dict[str, dict[str, Any]],
                           response: tuple[tuple[int, int], ...]) -> dict[str, Any]:
    destroyed_id = raw.get("destroyed_id")
    witness_id = raw.get("witness_id")
    child = raw.get("child")
    evidence = raw.get("evidence")
    require(isinstance(destroyed_id, str) and destroyed_id in destroyed_by_id, "route: unknown destroyed triple")
    require(isinstance(witness_id, str) and witness_id in witness_by_id, "route: unknown witness")
    require(isinstance(child, str) and child, "route: child required")
    require(isinstance(evidence, str) and evidence, "route: evidence required")
    witness = witness_by_id[witness_id]
    require(witness["child"] == child, "route: child differs from witness target")
    require(set(tuple(edge) for edge in witness["prescription"]).issubset(response),
            "route: witness does not occur in response")
    output = {"destroyed_id": destroyed_id, "witness_id": witness_id, "child": child, "evidence": evidence}
    output["route_assignment_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    row_certificate = certificate.get("row_margin_certificate")
    raw_routes = certificate.get("response_routes")
    require(isinstance(row_certificate, dict), "row_margin_certificate: expected object")
    require(isinstance(raw_routes, list), "response_routes: expected list")
    row_margin.validate_certificate(row_certificate)
    row_exact = row_margin.exact_certificate(row_certificate)
    linked_certificate = row_certificate["linked_operation_certificate"]
    source = linked_certificate["linkage_certificate"]["source_manifest"]
    destroyed_records = exact_destroyed_records(linked_certificate)
    witness_records = exact_witness_records(source)
    destroyed_by_id = {record["destroyed_id"]: record for record in destroyed_records}
    witness_by_id = {record["witness_id"]: record for record in witness_records}
    expected_credit_records = {
        response_key(record["response"]): record for record in row_exact["response_credit_records"]
    }

    route_records = []
    route_by_response: dict[tuple[tuple[int, int], ...], dict[str, Any]] = {}
    for index, raw_record in enumerate(raw_routes):
        require(isinstance(raw_record, dict), f"response_routes[{index}]: expected object")
        response = raw_record.get("response")
        assignments_raw = raw_record.get("assignments")
        require(isinstance(response, list), f"response_routes[{index}].response: expected list")
        require(isinstance(assignments_raw, list), f"response_routes[{index}].assignments: expected list")
        key = response_key(response)
        require(key in expected_credit_records, f"response_routes[{index}]: unknown response")
        require(key not in route_by_response, f"response_routes[{index}]: duplicate response")
        assignments = [exact_route_assignment(raw, destroyed_by_id, witness_by_id, key) for raw in assignments_raw]
        assignments.sort(key=lambda record: (record["destroyed_id"], record["witness_id"], record["child"]))
        require(assignments_raw == assignments,
                f"response_routes[{index}].assignments: canonical order or digest mismatch")
        require(len({assignment["destroyed_id"] for assignment in assignments}) == len(assignments),
                f"response_routes[{index}]: destroyed triple reused")
        require(len({assignment["witness_id"] for assignment in assignments}) == len(assignments),
                f"response_routes[{index}]: witness reused")
        child_counts = Counter(assignment["child"] for assignment in assignments)
        expected_counts = expected_credit_records[key]["credit_routes"]
        require({child: child_counts.get(child, 0) for child in expected_counts} == expected_counts,
                f"response_routes[{index}]: child counts differ from row credit vector")
        output = {
            "response": [list(edge) for edge in key],
            "assignments": assignments,
            "routed_units": len(assignments),
            "child_route_counts": [[child, child_counts[child]] for child in sorted(child_counts)],
        }
        output["response_route_sha256"] = catalogue.canonical_digest(output)
        route_records.append(output)
        route_by_response[key] = output
    route_records.sort(key=lambda record: record["response"])
    require(raw_routes == route_records, "response_routes: canonical response order or digest mismatch")
    require(set(route_by_response) == set(expected_credit_records), "response_routes: must cover every response exactly")

    total_routes = sum(record["routed_units"] for record in route_records)
    child_totals = Counter(assignment["child"] for record in route_records for assignment in record["assignments"])
    claims = {
        "host_id": row_exact["claims"]["host_id"],
        "fibre_id": row_exact["claims"]["fibre_id"],
        "responses": len(route_records),
        "literal_destroyed_triples": len(destroyed_records),
        "nondeleted_child_witnesses": len(witness_records),
        "routed_units_across_alternative_responses": total_routes,
        "maximum_response_routed_units": max([0] + [record["routed_units"] for record in route_records]),
        "responses_with_routes": sum(record["routed_units"] > 0 for record in route_records),
        "distinct_children_routed": len(child_totals),
        "child_route_totals": [[child, child_totals[child]] for child in sorted(child_totals)],
        "destroyed_records_sha256": catalogue.canonical_digest(destroyed_records),
        "witness_records_sha256": catalogue.canonical_digest(witness_records),
        "route_records_sha256": catalogue.canonical_digest(route_records),
        "row_margin_sha256": row_certificate["certificate_sha256"],
    }
    return {"destroyed_triple_records": destroyed_records, "child_witness_records": witness_records,
            "response_routes": route_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("destroyed_triple_records", "child_witness_records", "response_routes", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"responses": claims["responses"], "destroyed": claims["literal_destroyed_triples"],
            "witnesses": claims["nondeleted_child_witnesses"],
            "routes": claims["routed_units_across_alternative_responses"],
            "routed_responses": claims["responses_with_routes"], "children": claims["distinct_children_routed"]}


def build_certificate(row_certificate: dict[str, Any],
                      response_assignments: dict[tuple[tuple[int, int], ...], list[dict[str, Any]]]) -> dict[str, Any]:
    row_margin.validate_certificate(row_certificate)
    routes = []
    for credit_record in row_margin.exact_certificate(row_certificate)["response_credit_records"]:
        key = response_key(credit_record["response"])
        assignments = []
        for raw in response_assignments.get(key, []):
            core = {name: raw[name] for name in ("destroyed_id", "witness_id", "child", "evidence")}
            core["route_assignment_sha256"] = catalogue.canonical_digest(core)
            assignments.append(core)
        assignments.sort(key=lambda record: (record["destroyed_id"], record["witness_id"], record["child"]))
        counts = Counter(assignment["child"] for assignment in assignments)
        record = {"response": credit_record["response"], "assignments": assignments,
                  "routed_units": len(assignments),
                  "child_route_counts": [[child, count] for child, count in sorted(counts.items())]}
        record["response_route_sha256"] = catalogue.canonical_digest(record)
        routes.append(record)
    routes.sort(key=lambda record: record["response"])
    certificate: dict[str, Any] = {"version": 1, "row_margin_certificate": row_certificate,
                                   "response_routes": routes}
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def synthetic_certificate(random: Random) -> dict[str, Any]:
    host = random.choice(catalogue.build_catalogue()["hosts"])
    background = signature.random_background(host["side"], random)
    linked_certificate = linked.build_certificate(host, background, random, "canonical-rank3-selector")
    bundle = linked_certificate["direct_delta_certificate"]["pool_certificate"]["geometric_bundle"]
    exposure_certificate = exposure.build_certificate(bundle)
    weights = row_margin.first_supported_weights(exposure_certificate)
    destroyed_records = exact_destroyed_records(linked_certificate)
    witnesses = exact_witness_records(linked_certificate["linkage_certificate"]["source_manifest"])
    children = exposure_certificate["children"]
    assignments_by_response = {}
    route_counts = {}
    for response_record in exposure_certificate["response_vectors"]:
        key = response_key(response_record["response"])
        eligible = [witness for witness in witnesses if set(tuple(edge) for edge in witness["prescription"]).issubset(key)]
        random.shuffle(eligible)
        available_destroyed = list(destroyed_records); random.shuffle(available_destroyed)
        assignments = []
        limit = min(len(eligible), len(available_destroyed), random.randrange(0, 3))
        for destroyed_record, witness in zip(available_destroyed[:limit], eligible[:limit]):
            assignments.append({"destroyed_id": destroyed_record["destroyed_id"],
                                "witness_id": witness["witness_id"], "child": witness["child"],
                                "evidence": "synthetic literal witness-bound route"})
        assignments_by_response[key] = assignments
        counts = Counter(assignment["child"] for assignment in assignments)
        route_counts[key] = {child: counts.get(child, 0) for child in children}
    row_certificate = row_margin.build_certificate(linked_certificate, exposure_certificate, weights,
                                                    random.randrange(0, 3), random.randrange(1, 12), route_counts)
    return build_certificate(row_certificate, assignments_by_response)


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(2166); totals: Counter[str] = Counter()
    for _ in range(80): totals.update(validate_certificate(synthetic_certificate(random)))
    return 80, totals


def run_mutation_tests() -> int:
    random = Random(167); certificate = synthetic_certificate(random); validate_certificate(certificate)
    mutations = []
    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate); mutator(candidate); mutations.append(candidate)
    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data["destroyed_triple_records"].reverse())
    add(lambda data: data["child_witness_records"].reverse())
    add(lambda data: data["response_routes"].reverse())
    add(lambda data: data["claims"].update(responses=999))
    add(lambda data: data["row_margin_certificate"].update(certificate_sha256="0" * 64))
    routed = next((record for record in certificate["response_routes"] if record["assignments"]), None)
    if routed is not None:
        index = certificate["response_routes"].index(routed)
        add(lambda data, i=index: data["response_routes"][i]["assignments"].append(copy.deepcopy(data["response_routes"][i]["assignments"][0])))
        add(lambda data, i=index: data["response_routes"][i]["assignments"][0].update(child="missing-child"))
        add(lambda data, i=index: data["response_routes"][i]["assignments"][0].update(destroyed_id="destroyed-missing"))
        add(lambda data, i=index: data["response_routes"][i]["assignments"][0].update(witness_id="witness-missing"))
    else:
        add(lambda data: data["response_routes"][0].update(routed_units=1))
        add(lambda data: data["response_routes"][0].update(child_route_counts=[["missing", 1]]))
        add(lambda data: data["claims"].update(routed_units_across_alternative_responses=1))
        add(lambda data: data["claims"].update(distinct_children_routed=1))
    add(lambda data: data["response_routes"][0].update(response_route_sha256="f" * 64))
    rejected = 0
    for candidate in mutations:
        try: validate_certificate(candidate)
        except (WitnessRoutingError, row_margin.RowMarginError, linked.LinkedOperationError,
                exposure.ExposureError, owner_fate.FateError, catalogue.CatalogueError): rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted routing accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 2:
        print(validate_certificate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))); return
    require(len(sys.argv) == 1,
            "usage: check_prime_power_witness_bound_destroyed_credit_routing.py [certificate.json]")
    systems, totals = run_random_tests(); rejected = run_mutation_tests()
    print("verified witness-bound destroyed-credit routing: "
          f"{systems} systems, {totals['responses']} alternative responses, {totals['destroyed']} literal destroyed triples, "
          f"{totals['witnesses']} nondeleted child witnesses, {totals['routes']} routed assignments across "
          f"{totals['routed_responses']} response records, and {rejected} corruptions rejected")


if __name__ == "__main__": main()

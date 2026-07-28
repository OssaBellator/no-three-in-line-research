#!/usr/bin/env python3
"""Validate one common positive state-weight vector across recurrent row certificates.

Each input row is a witness-bound destroyed-credit routing certificate and therefore
contains one exact labelled recurrent-row margin certificate. This checker requires a
single positive integer weight for every state appearing in the block, requires every
row's child weights to be the corresponding restriction, and requires the row's parent
budget to equal the global weight of its parent state.

The checker reconstructs recurrent support edges from positive child-vector coordinates,
checks exact parent-row coverage, reports recurrent exits, tests strong connectivity of
the declared block and verifies every row margin. A complete strict SCC certificate is
recognized only when the block is closed, strongly connected and every row is strict.

Passing an open block still proves common-weight consistency and exact row margins, but
not closure. Passing a complete strict SCC certificate remains relative to the supplied
row sources and does not prove that the genuine parent-rule population is complete.
"""
from __future__ import annotations

import copy
import json
import math
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_labelled_recurrent_row_margin as row_margin
import check_prime_power_labelled_weight_exposure as exposure
import check_prime_power_linked_operation_selector as linked
import check_prime_power_witness_bound_destroyed_credit_routing as routing


class CommonWeightError(ValueError):
    """Raised when common recurrent-block weights are inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CommonWeightError(message)


def state_core(record: dict[str, Any]) -> dict[str, Any]:
    state_id = record.get("id")
    role = record.get("role")
    stratum = record.get("stratum")
    owner = record.get("owner")
    require(isinstance(state_id, str) and state_id, "state.id: nonempty string required")
    require(role in {"recurrent", "offdiagonal", "auxiliary", "sink"}, f"state {state_id}: bad role")
    require(type(stratum) is int and stratum >= 0, f"state {state_id}: bad stratum")
    require(owner is None or (isinstance(owner, list) and len(owner) == 2), f"state {state_id}: bad owner")
    return {"id": state_id, "role": role, "stratum": stratum, "owner": owner}


def strongly_connected(nodes: list[str], edges: set[tuple[str, str]]) -> bool:
    if not nodes:
        return False
    adjacency: dict[str, set[str]] = defaultdict(set)
    reverse: dict[str, set[str]] = defaultdict(set)
    for left, right in edges:
        adjacency[left].add(right)
        reverse[right].add(left)

    def reachable(start: str, graph: dict[str, set[str]]) -> set[str]:
        seen = {start}
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for nxt in graph.get(current, set()):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return seen

    return reachable(nodes[0], adjacency) >= set(nodes) and reachable(nodes[0], reverse) >= set(nodes)


def exact_weight_record(record: dict[str, Any]) -> dict[str, Any]:
    state_id = record.get("state_id")
    weight = record.get("weight")
    require(isinstance(state_id, str) and state_id, "state_weights: state_id required")
    require(type(weight) is int and weight > 0, f"state_weights.{state_id}: positive integer required")
    output = {"state_id": state_id, "weight": weight}
    output["weight_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    raw_rows = certificate.get("routed_row_certificates")
    raw_weights = certificate.get("state_weights")
    scc_state_ids = certificate.get("scc_state_ids")
    require(isinstance(raw_rows, list) and raw_rows, "routed_row_certificates: nonempty list required")
    require(isinstance(raw_weights, list) and raw_weights, "state_weights: nonempty list required")
    require(isinstance(scc_state_ids, list) and scc_state_ids, "scc_state_ids: nonempty list required")
    require(scc_state_ids == sorted(scc_state_ids), "scc_state_ids: sorted order required")
    require(len(scc_state_ids) == len(set(scc_state_ids)), "scc_state_ids: duplicates")

    weight_records = [exact_weight_record(record) for record in raw_weights]
    require(raw_weights == weight_records, "state_weights: canonical records and digests required")
    require(weight_records == sorted(weight_records, key=lambda record: record["state_id"]),
            "state_weights: canonical order required")
    weights = {record["state_id"]: record["weight"] for record in weight_records}
    require(len(weights) == len(weight_records), "state_weights: duplicate state")
    require(math.gcd(*weights.values()) == 1, "state_weights: common gcd must be one")

    rows = []
    states: dict[str, dict[str, Any]] = {}
    parent_counts: Counter[str] = Counter()
    recurrent_edges: set[tuple[str, str]] = set()
    external_recurrent_edges: set[tuple[str, str]] = set()
    exit_edges: set[tuple[str, str]] = set()
    margins = []
    for index, route_certificate in enumerate(raw_rows):
        require(isinstance(route_certificate, dict), f"routed_row_certificates[{index}]: expected object")
        routing.validate_certificate(route_certificate)
        route_exact = routing.exact_certificate(route_certificate)
        row_certificate = route_certificate["row_margin_certificate"]
        row_exact = row_margin.exact_certificate(row_certificate)
        source = row_certificate["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]
        parent = source["parent"]
        parent_counts[parent] += 1
        for raw_state in source["states"]:
            core = state_core(raw_state)
            if core["id"] in states:
                require(states[core["id"]] == core, f"state {core['id']}: definition drift across rows")
            else:
                states[core["id"]] = core
        require(parent in states and states[parent]["role"] == "recurrent", f"row {index}: parent not recurrent")
        require(parent in weights, f"row {index}: parent missing global weight")
        require(row_certificate["parent_budget"] == weights[parent],
                f"row {index}: parent budget/global weight mismatch")
        children = row_certificate["weight_exposure_certificate"]["children"]
        require(set(children) <= set(weights), f"row {index}: child missing global weight")
        require(row_certificate["child_weights"] == {child: weights[child] for child in children},
                f"row {index}: child weights are not the global restriction")
        child_index = {child: position for position, child in enumerate(children)}
        positive_children = {
            child for child in children
            if any(record["child_vector"][child_index[child]] > 0
                   for record in row_certificate["weight_exposure_certificate"]["response_vectors"])
        }
        for child in positive_children:
            require(child in states, f"row {index}: positive child missing state definition")
            role = states[child]["role"]
            if role == "recurrent" and child in scc_state_ids:
                recurrent_edges.add((parent, child))
            elif role == "recurrent":
                external_recurrent_edges.add((parent, child))
            else:
                exit_edges.add((parent, child))
        claims = row_exact["claims"]
        margins.append(claims["maximum_margin"])
        rows.append({
            "parent_state_id": parent, "fibre_id": claims["fibre_id"], "host_id": claims["host_id"],
            "responses": claims["responses"], "children": claims["children"],
            "parent_weight": weights[parent], "minimum_row_load": claims["minimum_row_load"],
            "maximum_margin": claims["maximum_margin"], "strict_row": claims["strict_row"],
            "positive_child_states": sorted(positive_children),
            "routing_certificate_sha256": route_certificate["certificate_sha256"],
            "row_margin_sha256": row_certificate["certificate_sha256"],
            "route_records_sha256": route_exact["claims"]["route_records_sha256"],
        })
    rows.sort(key=lambda record: (record["parent_state_id"], record["fibre_id"]))
    require(raw_rows == sorted(raw_rows, key=lambda cert: (
        cert["row_margin_certificate"]["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]["parent"],
        cert["row_margin_certificate"]["claims"]["fibre_id"])),
        "routed_row_certificates: canonical parent/fibre order required")
    require(all(count == 1 for count in parent_counts.values()), "routed_row_certificates: duplicate parent row")
    require(set(parent_counts) == set(scc_state_ids), "scc_state_ids: every SCC parent must have exactly one row")
    require(set(states) == set(weights), "state_weights: must cover exactly the shared row-state registry")
    require(all(states[state_id]["role"] == "recurrent" for state_id in scc_state_ids),
            "scc_state_ids: nonrecurrent state")

    strong = int(strongly_connected(scc_state_ids, recurrent_edges))
    closed = int(not external_recurrent_edges)
    all_strict = int(all(margin > 0 for margin in margins))
    complete_strict_scc = int(strong and closed and all_strict)
    claims = {
        "states": len(states), "scc_states": len(scc_state_ids), "rows": len(rows),
        "recurrent_internal_edges": len(recurrent_edges),
        "external_recurrent_edges": len(external_recurrent_edges),
        "nonrecurrent_exit_edges": len(exit_edges),
        "strongly_connected": strong, "closed_recurrent_block": closed,
        "strict_rows": sum(record["strict_row"] for record in rows),
        "critical_rows": sum(record["maximum_margin"] == 0 for record in rows),
        "excess_rows": sum(record["maximum_margin"] < 0 for record in rows),
        "all_rows_strict": all_strict, "minimum_margin": min(margins), "total_margin": sum(margins),
        "maximum_state_weight": max(weights.values()), "complete_strict_scc": complete_strict_scc,
        "recurrent_edges": [list(edge) for edge in sorted(recurrent_edges)],
        "external_recurrent_edge_records": [list(edge) for edge in sorted(external_recurrent_edges)],
        "exit_edge_records": [list(edge) for edge in sorted(exit_edges)],
        "states_sha256": catalogue.canonical_digest([states[key] for key in sorted(states)]),
        "weights_sha256": catalogue.canonical_digest(weight_records),
        "rows_sha256": catalogue.canonical_digest(rows),
    }
    return {"state_weights": weight_records, "row_records": rows, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("state_weights", "row_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"states": claims["states"], "scc_states": claims["scc_states"], "rows": claims["rows"],
            "internal_edges": claims["recurrent_internal_edges"],
            "external_edges": claims["external_recurrent_edges"], "strict": claims["strict_rows"],
            "minimum_margin": claims["minimum_margin"], "strong": claims["strongly_connected"],
            "closed": claims["closed_recurrent_block"], "complete": claims["complete_strict_scc"]}


def build_certificate(route_certificates: list[dict[str, Any]], scc_state_ids: list[str],
                      weights: dict[str, int]) -> dict[str, Any]:
    ordered_routes = sorted(route_certificates, key=lambda cert: (
        cert["row_margin_certificate"]["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]["parent"],
        cert["row_margin_certificate"]["claims"]["fibre_id"]))
    require(weights and math.gcd(*weights.values()) == 1,
            "weights: supplied vector must already be primitive")
    weight_records = []
    for state_id in sorted(weights):
        record = {"state_id": state_id, "weight": weights[state_id]}
        record["weight_record_sha256"] = catalogue.canonical_digest(record)
        weight_records.append(record)
    certificate: dict[str, Any] = {"version": 1, "scc_state_ids": sorted(scc_state_ids),
                                   "state_weights": weight_records,
                                   "routed_row_certificates": ordered_routes}
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def synthetic_open_block(random: Random) -> dict[str, Any]:
    for _attempt in range(200):
        temporary = routing.synthetic_certificate(random)
        old_row = temporary["row_margin_certificate"]
        linked_certificate = old_row["linked_operation_certificate"]
        exposure_certificate = old_row["weight_exposure_certificate"]
        child_weights = old_row["child_weights"]
        source = linked_certificate["linkage_certificate"]["source_manifest"]
        parent = source["parent"]
        route_counts = {row_margin.response_key(record["response"]): record["credit_routes"]
                        for record in old_row["response_credit_records"]}
        minimum_load = old_row["claims"]["minimum_row_load"]
        global_weights = {state["id"]: 1 for state in source["states"]}
        global_weights.update(child_weights)
        if parent in child_weights:
            parent_budget = child_weights[parent]
            if parent_budget <= minimum_load:
                continue
        else:
            parent_budget = max(1, minimum_load + 1)
            global_weights[parent] = parent_budget
        if math.gcd(*global_weights.values()) != 1:
            continue
        new_row = row_margin.build_certificate(linked_certificate, exposure_certificate, child_weights,
                                               old_row["fixed_load"], parent_budget, route_counts)
        assignments = {
            row_margin.response_key(record["response"]): [
                {key: assignment[key] for key in ("destroyed_id", "witness_id", "child", "evidence")}
                for assignment in record["assignments"]]
            for record in temporary["response_routes"]}
        routed = routing.build_certificate(new_row, assignments)
        if routed["row_margin_certificate"]["claims"]["strict_row"] == 1:
            return build_certificate([routed], [parent], global_weights)
    raise CommonWeightError("unable to construct deterministic strict open-block regression")


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(2174)
    totals: Counter[str] = Counter()
    for _ in range(30):
        totals.update(validate_certificate(synthetic_open_block(random)))
    return 30, totals


def run_graph_regressions() -> None:
    require(strongly_connected(["a"], set()), "singleton SCC regression failed")
    require(strongly_connected(["a", "b"], {("a", "b"), ("b", "a")}), "two-cycle regression failed")
    require(not strongly_connected(["a", "b"], {("a", "b")}), "one-way regression failed")


def run_mutation_tests() -> int:
    random = Random(173)
    certificate = synthetic_open_block(random)
    validate_certificate(certificate)
    mutations = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data["state_weights"].reverse())
    add(lambda data: data["state_weights"][0].update(weight=0))
    add(lambda data: data["scc_state_ids"].append(data["scc_state_ids"][0]))
    add(lambda data: data["routed_row_certificates"].append(copy.deepcopy(data["routed_row_certificates"][0])))
    add(lambda data: data["row_records"].reverse())
    add(lambda data: data["claims"].update(minimum_margin=999))
    add(lambda data: data["routed_row_certificates"][0]["row_margin_certificate"].update(parent_budget=999))
    first_child = next(iter(certificate["routed_row_certificates"][0]["row_margin_certificate"]["child_weights"]))
    add(lambda data: data["routed_row_certificates"][0]["row_margin_certificate"]["child_weights"].update({first_child: 999}))
    add(lambda data: data["state_weights"][0].update(weight_record_sha256="f" * 64))
    add(lambda data: data["routed_row_certificates"][0].update(certificate_sha256="0" * 64))
    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (CommonWeightError, routing.WitnessRoutingError, row_margin.RowMarginError,
                linked.LinkedOperationError, exposure.ExposureError, catalogue.CatalogueError):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted common-weight certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 2:
        print(validate_certificate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))))
        return
    require(len(sys.argv) == 1,
            "usage: check_prime_power_common_recurrent_block_weights.py [certificate.json]")
    run_graph_regressions()
    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print("verified common recurrent-block weights: "
          f"{systems} deterministic strict row blocks, {totals['states']} state records, {totals['rows']} rows, "
          f"{totals['internal_edges']} internal recurrent edges, {totals['external_edges']} recurrent exits, "
          f"{totals['strict']} strict rows, {totals['complete']} complete strict SCCs, three graph regressions, "
          f"and {rejected} corruptions rejected")


if __name__ == "__main__":
    main()

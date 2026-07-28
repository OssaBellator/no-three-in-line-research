#!/usr/bin/env python3
"""Validate declarative finite parent-rule clauses and enumerate operation slots.

The actual parent rule is not yet present in the repository. This checker fixes the
finite proof surface that such a rule must populate. A rule source supplies a complete
parent-case registry, finitely many clauses, explicit finite parameter axes and explicit
excluded parameter rows. The checker expands every admitted Cartesian-product row,
constructs the source-independent operation slots of CMR2118--CMR2125, and verifies
parent/clause incidence, exclusion coverage, duplicate freedom and exact reloadability.

Passing this checker proves exhaustive enumeration relative to the supplied parent-case
and clause data. It does not prove that those data are the genuine or exhaustive parent
operation rule.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from itertools import product
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_operation_slot_registry as slots


class ClauseEnumeratorError(ValueError):
    """Raised when a declarative parent-rule enumerator is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ClauseEnumeratorError(message)


def canonical_json_value(value: Any, path: str) -> Any:
    require(value is None or isinstance(value, (bool, int, str, list, dict)), f"{path}: non-JSON value")
    if isinstance(value, list):
        return [canonical_json_value(item, f"{path}[]") for item in value]
    if isinstance(value, dict):
        require(all(isinstance(key, str) for key in value), f"{path}: non-string key")
        return {key: canonical_json_value(value[key], f"{path}.{key}") for key in value}
    return value


def exact_parent_case(record: dict[str, Any]) -> dict[str, Any]:
    case_id = record.get("case_id")
    parent_state_id = record.get("parent_state_id")
    expected_host_id = record.get("expected_host_id")
    labels = record.get("state_labels")
    applicable = record.get("applicable_clause_ids")
    require(isinstance(case_id, str) and case_id, "parent case: nonempty case_id required")
    require(isinstance(parent_state_id, str) and parent_state_id, f"{case_id}: nonempty parent_state_id required")
    require(isinstance(expected_host_id, str) and expected_host_id, f"{case_id}: expected_host_id required")
    require(isinstance(labels, dict) and tuple(labels) == slots.LABEL_KEYS, f"{case_id}: exact ordered labels required")
    require(all(isinstance(labels[key], str) and labels[key] for key in slots.LABEL_KEYS), f"{case_id}: empty label")
    require(isinstance(applicable, list) and applicable, f"{case_id}: applicable_clause_ids required")
    require(all(isinstance(value, str) and value for value in applicable), f"{case_id}: bad applicable clause")
    require(len(applicable) == len(set(applicable)), f"{case_id}: duplicate applicable clause")
    return {
        "case_id": case_id,
        "parent_state_id": parent_state_id,
        "expected_host_id": expected_host_id,
        "state_labels": copy.deepcopy(labels),
        "applicable_clause_ids": list(applicable),
    }


def exact_axis(record: dict[str, Any], path: str) -> dict[str, Any]:
    name = record.get("name")
    values = record.get("values")
    require(isinstance(name, str) and name, f"{path}.name: nonempty string required")
    require(isinstance(values, list) and values, f"{path}.values: nonempty list required")
    canonical = [canonical_json_value(value, f"{path}.values") for value in values]
    digests = [catalogue.canonical_digest(value) for value in canonical]
    require(len(digests) == len(set(digests)), f"{path}.values: duplicate canonical value")
    return {"name": name, "values": canonical}


def row_key(row: dict[str, Any], axis_names: list[str]) -> str:
    require(tuple(row) == tuple(axis_names), "parameter row: exact axis order required")
    return catalogue.canonical_digest(row)


def exact_clause(record: dict[str, Any]) -> dict[str, Any]:
    clause_id = record.get("clause_id")
    operation_kind = record.get("operation_kind")
    case_ids = record.get("case_ids")
    axes_raw = record.get("parameter_axes")
    exclusions_raw = record.get("excluded_parameter_rows")
    require(isinstance(clause_id, str) and clause_id, "clause_id: nonempty string required")
    require(isinstance(operation_kind, str) and operation_kind, f"{clause_id}: operation_kind required")
    require(isinstance(case_ids, list) and case_ids, f"{clause_id}: case_ids required")
    require(all(isinstance(value, str) and value for value in case_ids), f"{clause_id}: bad case_id")
    require(len(case_ids) == len(set(case_ids)), f"{clause_id}: duplicate case_id")
    require(isinstance(axes_raw, list), f"{clause_id}: parameter_axes expected list")
    axes = [exact_axis(axis, f"{clause_id}.parameter_axes[{index}]") for index, axis in enumerate(axes_raw)]
    axis_names = [axis["name"] for axis in axes]
    require(len(axis_names) == len(set(axis_names)), f"{clause_id}: duplicate axis name")
    require(isinstance(exclusions_raw, list), f"{clause_id}: excluded_parameter_rows expected list")
    exclusions = []
    excluded_keys = set()
    for index, raw in enumerate(exclusions_raw):
        require(isinstance(raw, dict), f"{clause_id}.excluded_parameter_rows[{index}]: expected object")
        row = raw.get("row")
        reason = raw.get("reason")
        require(isinstance(row, dict), f"{clause_id}.excluded_parameter_rows[{index}].row: expected object")
        require(isinstance(reason, str) and reason, f"{clause_id}.excluded_parameter_rows[{index}].reason required")
        canonical_row = {name: canonical_json_value(row.get(name), f"{clause_id}.excluded row.{name}") for name in axis_names}
        require(tuple(row) == tuple(axis_names), f"{clause_id}: exclusion axis order mismatch")
        key = row_key(canonical_row, axis_names)
        require(key not in excluded_keys, f"{clause_id}: duplicate excluded row")
        excluded_keys.add(key)
        exclusions.append({"row": canonical_row, "reason": reason})
    return {
        "clause_id": clause_id,
        "operation_kind": operation_kind,
        "case_ids": list(case_ids),
        "parameter_axes": axes,
        "excluded_parameter_rows": exclusions,
    }


def clause_rows(clause: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    axes = clause["parameter_axes"]
    axis_names = [axis["name"] for axis in axes]
    excluded = {row_key(record["row"], axis_names) for record in clause["excluded_parameter_rows"]}
    rows = []
    all_rows = []
    for values in product(*(axis["values"] for axis in axes)) if axes else [()]:
        row = {name: copy.deepcopy(value) for name, value in zip(axis_names, values)}
        all_rows.append(row)
        if row_key(row, axis_names) not in excluded:
            rows.append(row)
    require(len(excluded) <= len(all_rows), f"{clause['clause_id']}: too many exclusions")
    require(excluded <= {row_key(row, axis_names) for row in all_rows}, f"{clause['clause_id']}: exclusion outside domain")
    require(rows, f"{clause['clause_id']}: clause has no admitted parameter row")
    return rows, all_rows


def exact_enumerator(manifest: dict[str, Any]) -> dict[str, Any]:
    require(manifest.get("version") == 1, "version: expected 1")
    rule_id = manifest.get("rule_id")
    rule_source = manifest.get("rule_source")
    raw_cases = manifest.get("parent_cases")
    raw_clauses = manifest.get("clauses")
    require(isinstance(rule_id, str) and rule_id, "rule_id: nonempty string required")
    require(isinstance(rule_source, dict), "rule_source: expected object")
    require(isinstance(raw_cases, list) and raw_cases, "parent_cases: nonempty list required")
    require(isinstance(raw_clauses, list) and raw_clauses, "clauses: nonempty list required")
    cases = [exact_parent_case(record) for record in raw_cases]
    clauses = [exact_clause(record) for record in raw_clauses]
    require(cases == sorted(cases, key=lambda record: record["case_id"]), "parent_cases: canonical case_id order required")
    require(clauses == sorted(clauses, key=lambda record: record["clause_id"]), "clauses: canonical clause_id order required")
    case_ids = [record["case_id"] for record in cases]
    clause_ids = [record["clause_id"] for record in clauses]
    require(len(case_ids) == len(set(case_ids)), "parent_cases: duplicate case_id")
    require(len(clause_ids) == len(set(clause_ids)), "clauses: duplicate clause_id")
    case_map = {record["case_id"]: record for record in cases}
    clause_map = {record["clause_id"]: record for record in clauses}
    catalogue_hosts = {host["host_id"] for host in catalogue.build_catalogue()["hosts"]}
    require(all(record["expected_host_id"] in catalogue_hosts for record in cases), "parent_cases: unknown host")
    for case in cases:
        require(set(case["applicable_clause_ids"]) <= set(clause_map), f"{case['case_id']}: unknown applicable clause")
    for clause in clauses:
        require(set(clause["case_ids"]) <= set(case_map), f"{clause['clause_id']}: unknown case")
    for case in cases:
        reverse = sorted(clause["clause_id"] for clause in clauses if case["case_id"] in clause["case_ids"])
        require(reverse == sorted(case["applicable_clause_ids"]), f"{case['case_id']}: case/clause incidence mismatch")

    slot_cores = []
    clause_claims = []
    total_domain_rows = total_excluded_rows = 0
    for clause in clauses:
        admitted, all_rows = clause_rows(clause)
        total_domain_rows += len(all_rows) * len(clause["case_ids"])
        total_excluded_rows += (len(all_rows) - len(admitted)) * len(clause["case_ids"])
        for case_id in clause["case_ids"]:
            case = case_map[case_id]
            for ordinal, row in enumerate(admitted):
                operation_key = {
                    "clause_id": clause["clause_id"],
                    "case_id": case_id,
                    "parameter_ordinal": ordinal,
                    "parameters": row,
                }
                slot_cores.append({
                    "parent_state_id": case["parent_state_id"],
                    "operation_kind": clause["operation_kind"],
                    "operation_key": operation_key,
                    "expected_host_id": case["expected_host_id"],
                    "state_labels": case["state_labels"],
                })
        clause_claims.append({
            "clause_id": clause["clause_id"],
            "cases": len(clause["case_ids"]),
            "domain_rows_per_case": len(all_rows),
            "excluded_rows_per_case": len(all_rows) - len(admitted),
            "admitted_rows_per_case": len(admitted),
            "generated_slots": len(clause["case_ids"]) * len(admitted),
        })
    registry = slots.build_registry(rule_id, rule_source, slot_cores)
    slots.validate_registry(registry)
    host_counts = Counter(slot["expected_host_id"] for slot in registry["slots"])
    parent_counts = Counter(slot["parent_state_id"] for slot in registry["slots"])
    kind_counts = Counter(slot["operation_kind"] for slot in registry["slots"])
    claims = {
        "parent_cases": len(cases),
        "clauses": len(clauses),
        "domain_case_rows": total_domain_rows,
        "excluded_case_rows": total_excluded_rows,
        "admitted_case_rows": total_domain_rows - total_excluded_rows,
        "generated_slots": len(registry["slots"]),
        "unique_parents": len(parent_counts),
        "unique_hosts": len(host_counts),
        "unique_operation_kinds": len(kind_counts),
        "clause_claims": clause_claims,
        "operation_kind_distribution": [[key, kind_counts[key]] for key in sorted(kind_counts)],
        "registry_sha256": registry["registry_sha256"],
        "cases_sha256": catalogue.canonical_digest(cases),
        "clauses_sha256": catalogue.canonical_digest(clauses),
    }
    return {"parent_cases": cases, "clauses": clauses, "expected_slot_registry": registry, "claims": claims}


def validate_manifest(manifest: Any) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest: expected object")
    exact = exact_enumerator(manifest)
    for key in ("parent_cases", "clauses", "expected_slot_registry", "claims"):
        require(manifest.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in manifest.items() if key != "manifest_sha256"}
    require(manifest.get("manifest_sha256") == catalogue.canonical_digest(payload), "manifest_sha256: incorrect")
    claims = exact["claims"]
    return {
        "cases": claims["parent_cases"], "clauses": claims["clauses"],
        "domain_rows": claims["domain_case_rows"], "excluded": claims["excluded_case_rows"],
        "slots": claims["generated_slots"], "parents": claims["unique_parents"],
        "hosts": claims["unique_hosts"], "kinds": claims["unique_operation_kinds"],
    }


def build_manifest(rule_id: str, rule_source: dict[str, Any], parent_cases: list[dict[str, Any]], clauses: list[dict[str, Any]]) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "version": 1, "rule_id": rule_id, "rule_source": copy.deepcopy(rule_source),
        "parent_cases": sorted((exact_parent_case(record) for record in parent_cases), key=lambda record: record["case_id"]),
        "clauses": sorted((exact_clause(record) for record in clauses), key=lambda record: record["clause_id"]),
    }
    manifest.update(exact_enumerator(manifest))
    manifest["manifest_sha256"] = catalogue.canonical_digest(manifest)
    return manifest


def synthetic_manifest() -> dict[str, Any]:
    random = Random(2158)
    hosts = catalogue.build_catalogue()["hosts"]
    clause_ids = ["delete", "rollback", "weighted"]
    cases = []
    for index in range(24):
        applicable = [clause_ids[index % 3], clause_ids[(index + 1) % 3]]
        labels = {
            "provenance": f"prov-{index % 7}", "collision": f"collision-{index % 5}",
            "local_line": f"line-{index % 11}", "interface": f"interface-{index % 4}",
            "root": f"root-{index % 3}", "thin": f"thin-{index % 2}", "crt": f"crt-{index % 6}",
        }
        cases.append({
            "case_id": f"case-{index:02d}", "parent_state_id": f"parent-{index:02d}",
            "expected_host_id": hosts[(index * 41 + 13) % len(hosts)]["host_id"],
            "state_labels": labels, "applicable_clause_ids": sorted(applicable),
        })
    clauses = []
    for clause_index, clause_id in enumerate(clause_ids):
        case_ids = [case["case_id"] for case in cases if clause_id in case["applicable_clause_ids"]]
        excluded = []
        if clause_index == 1:
            excluded.append({"row": {"channel": 2, "phase": 1}, "reason": "synthetic rollback exclusion"})
        clauses.append({
            "clause_id": clause_id, "operation_kind": f"{clause_id}-and-match", "case_ids": case_ids,
            "parameter_axes": [{"name": "channel", "values": list(range(3))}, {"name": "phase", "values": [0, 1]}],
            "excluded_parameter_rows": excluded,
        })
    return build_manifest("synthetic-parent-rule-clauses-v1",
        {"enumerator": "deterministic-clause-regression", "seed": 2158, "nonce": random.randrange(10**6)}, cases, clauses)


def run_mutation_tests() -> int:
    manifest = synthetic_manifest()
    validate_manifest(manifest)
    mutations = []
    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest); mutator(candidate); mutations.append(candidate)
    add(lambda data: data.update(manifest_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data["parent_cases"].reverse())
    add(lambda data: data["clauses"].reverse())
    add(lambda data: data["parent_cases"][0]["applicable_clause_ids"].append("missing"))
    add(lambda data: data["clauses"][0]["case_ids"].append("missing"))
    add(lambda data: data["clauses"][0]["parameter_axes"][0]["values"].append(0))
    add(lambda data: data["clauses"][0]["excluded_parameter_rows"].append({"row": {"channel": 99, "phase": 0}, "reason": "bad"}))
    add(lambda data: data["expected_slot_registry"]["slots"].pop())
    add(lambda data: data["claims"].update(generated_slots=999))
    add(lambda data: data["parent_cases"][0]["state_labels"].pop("crt"))
    add(lambda data: data["clauses"][0].update(operation_kind=""))
    rejected = 0
    for candidate in mutations:
        try: validate_manifest(candidate)
        except (ClauseEnumeratorError, slots.SlotRegistryError, catalogue.CatalogueError): rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted enumerator accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 2:
        print(validate_manifest(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))); return
    require(len(sys.argv) == 1, "usage: check_prime_power_parent_rule_clause_enumerator.py [manifest.json]")
    summary = validate_manifest(synthetic_manifest()); rejected = run_mutation_tests()
    print("verified parent-rule clause enumeration: "
          f"{summary['cases']} cases, {summary['clauses']} clauses, {summary['domain_rows']} domain case-rows, "
          f"{summary['excluded']} exclusions, {summary['slots']} slots, {summary['parents']} parents, "
          f"{summary['hosts']} hosts, {summary['kinds']} operation kinds, and {rejected} corruptions rejected")


if __name__ == "__main__": main()

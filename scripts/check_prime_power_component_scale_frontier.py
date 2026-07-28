#!/usr/bin/env python3
"""Validate and synchronize the exact T14 cross-block component-scale proof bank.

T13 supplies the exact local-to-global state classes and proof artifacts. T11 supplies the exact
primitive positive common weights and closed recurrent-block artifacts. This checker derives every
shared-state scale equation, rejects inconsistent ratio cycles, clears denominators componentwise and
requires one semantic proof package for each connected block component.

Disconnected components remain independently normalized. The checker validates documentary identity,
support and exact rational arithmetic only; it does not prove external scale semantics and permanently
reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import json
import math
import sys
from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_recurrent_block_closure_frontier as t11_frontier
import check_prime_power_state_equivalence_frontier as t13_frontier


class ComponentScaleFrontierError(ValueError):
    """Raised when the exact T14 component-scale bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ComponentScaleFrontierError(message)


COMPONENT_ARTIFACT_KIND = "component-scale-synchronization-proof"
OBLIGATION_LOCATOR = "component-scale-frontier://COMPONENT_SCALE_SEMANTIC"
T14_TARGET_LOCATOR = "component-scale-frontier://T14_COMPONENT_SCALES"


def lcm(left: int, right: int) -> int:
    return abs(left * right) // math.gcd(left, right)


def exact_status_record(
    raw: dict[str, Any],
    *,
    arithmetic: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    component_id = arithmetic["component_id"]
    require(raw.get("component_id") == component_id, f"{path}.component_id: mismatch")
    require(
        raw.get("scale_component_arithmetic_sha256")
        == arithmetic["scale_component_arithmetic_sha256"],
        f"{path}.scale_component_arithmetic_sha256: mismatch",
    )
    status = raw.get("status")
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    note = raw.get("note")
    require(status in {"open", "proved"}, f"{path}.status: expected open/proved")
    require(isinstance(note, str) and note, f"{path}.note: required")
    if status == "open":
        require(locator is None, f"{path}.verification_locator: open requires null")
        require(digest is None, f"{path}.verification_digest: open requires null")
    else:
        require(
            locator == f"component-scale-registry://{component_id}",
            f"{path}.verification_locator: canonical component URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    core = {
        "component_id": component_id,
        "scale_component_arithmetic_sha256": arithmetic[
            "scale_component_arithmetic_sha256"
        ],
        "status": status,
        "verification_locator": locator,
        "note": note,
    }
    output = {
        **core,
        "verification_digest": digest,
        "component_scale_record_core_sha256": catalogue.canonical_digest(core),
    }
    output["component_scale_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_equation_semantic(
    raw: dict[str, Any],
    *,
    equation: dict[str, Any],
    expected_t13_support: list[str],
    expected_t11_common_support: list[str],
    path: str,
) -> dict[str, Any]:
    require(
        raw.get("scale_equation_sha256") == equation["scale_equation_sha256"],
        f"{path}.scale_equation_sha256: mismatch",
    )
    require(
        raw.get("global_state_id") == equation["global_state_id"],
        f"{path}.global_state_id: mismatch",
    )
    statement = raw.get("scale_statement")
    evidence = raw.get("evidence")
    require(isinstance(statement, str) and statement, f"{path}.scale_statement: required")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    require(
        raw.get("support_t13_class_artifact_ids") == expected_t13_support,
        f"{path}.support_t13_class_artifact_ids: exact support required",
    )
    require(
        raw.get("support_t11_common_weight_artifact_ids") == expected_t11_common_support,
        f"{path}.support_t11_common_weight_artifact_ids: exact support required",
    )
    output = {
        "scale_equation_sha256": equation["scale_equation_sha256"],
        "global_state_id": equation["global_state_id"],
        "support_t13_class_artifact_ids": list(expected_t13_support),
        "support_t11_common_weight_artifact_ids": list(expected_t11_common_support),
        "scale_statement": statement,
        "evidence": evidence,
    }
    output["scale_equation_semantic_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_semantic_certificate(
    raw: dict[str, Any],
    *,
    arithmetic: dict[str, Any],
    class_artifact_by_global: dict[str, str],
    common_artifact_by_block: dict[str, str],
    closure_artifact_by_block: dict[str, str],
    path: str,
) -> dict[str, Any]:
    component_id = arithmetic["component_id"]
    require(raw.get("component_id") == component_id, f"{path}.component_id: mismatch")
    require(
        raw.get("scale_component_arithmetic_sha256")
        == arithmetic["scale_component_arithmetic_sha256"],
        f"{path}.scale_component_arithmetic_sha256: mismatch",
    )
    normalization_statement = raw.get("normalization_statement")
    evidence = raw.get("evidence")
    require(
        isinstance(normalization_statement, str) and normalization_statement,
        f"{path}.normalization_statement: required",
    )
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")

    expected_classes = arithmetic["global_state_ids"]
    expected_t13_all = sorted(
        class_artifact_by_global[global_state_id]
        for global_state_id in expected_classes
    )
    expected_common_all = sorted(
        common_artifact_by_block[block_id] for block_id in arithmetic["block_ids"]
    )
    expected_closure_all = sorted(
        closure_artifact_by_block[block_id] for block_id in arithmetic["block_ids"]
    )
    require(
        raw.get("component_t13_class_artifact_ids") == expected_t13_all,
        f"{path}.component_t13_class_artifact_ids: exact support required",
    )
    require(
        raw.get("component_t11_common_weight_artifact_ids") == expected_common_all,
        f"{path}.component_t11_common_weight_artifact_ids: exact support required",
    )
    require(
        raw.get("component_t11_block_closure_artifact_ids") == expected_closure_all,
        f"{path}.component_t11_block_closure_artifact_ids: exact support required",
    )

    raw_semantics = raw.get("equation_semantics")
    require(isinstance(raw_semantics, list), f"{path}.equation_semantics: expected list")
    equations = arithmetic["scale_equation_records"]
    require(
        len(raw_semantics) == len(equations),
        f"{path}.equation_semantics: exact equation cardinality required",
    )
    equation_semantics = []
    for index, (raw_semantic, equation) in enumerate(zip(raw_semantics, equations)):
        global_state_id = equation["global_state_id"]
        left_block = equation["left_block_id"]
        right_block = equation["right_block_id"]
        semantic = exact_equation_semantic(
            raw_semantic,
            equation=equation,
            expected_t13_support=[class_artifact_by_global[global_state_id]],
            expected_t11_common_support=sorted(
                {
                    common_artifact_by_block[left_block],
                    common_artifact_by_block[right_block],
                }
            ),
            path=f"{path}.equation_semantics[{index}]",
        )
        equation_semantics.append(semantic)
    require(
        raw_semantics == equation_semantics,
        f"{path}.equation_semantics: canonical records/digests required",
    )
    output = {
        "component_id": component_id,
        "scale_component_arithmetic_sha256": arithmetic[
            "scale_component_arithmetic_sha256"
        ],
        "component_t13_class_artifact_ids": expected_t13_all,
        "component_t11_common_weight_artifact_ids": expected_common_all,
        "component_t11_block_closure_artifact_ids": expected_closure_all,
        "equation_semantics": equation_semantics,
        "normalization_statement": normalization_statement,
        "evidence": evidence,
    }
    output["component_scale_semantic_certificate_sha256"] = catalogue.canonical_digest(
        output
    )
    return output


def exact_component_artifact(
    raw: dict[str, Any],
    *,
    arithmetic: dict[str, Any],
    semantic: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    values = {
        key: raw.get(key)
        for key in (
            "artifact_id",
            "artifact_kind",
            "proof_locator",
            "proof_digest",
            "proof_statement",
            "evidence",
        )
    }
    for name, value in values.items():
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    component_id = arithmetic["component_id"]
    require(raw.get("component_id") == component_id, f"{path}.component_id: mismatch")
    require(
        raw.get("scale_component_arithmetic_sha256")
        == arithmetic["scale_component_arithmetic_sha256"],
        f"{path}.scale_component_arithmetic_sha256: mismatch",
    )
    require(
        raw.get("component_scale_semantic_certificate_sha256")
        == semantic["component_scale_semantic_certificate_sha256"],
        f"{path}.component_scale_semantic_certificate_sha256: mismatch",
    )
    require(
        values["artifact_kind"] == COMPONENT_ARTIFACT_KIND,
        f"{path}.artifact_kind: wrong kind",
    )
    support_fields = {
        "support_t13_class_artifact_ids": semantic[
            "component_t13_class_artifact_ids"
        ],
        "support_t11_common_weight_artifact_ids": semantic[
            "component_t11_common_weight_artifact_ids"
        ],
        "support_t11_block_closure_artifact_ids": semantic[
            "component_t11_block_closure_artifact_ids"
        ],
    }
    output = {
        "component_id": component_id,
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        "scale_component_arithmetic_sha256": arithmetic[
            "scale_component_arithmetic_sha256"
        ],
        "component_scale_semantic_certificate_sha256": semantic[
            "component_scale_semantic_certificate_sha256"
        ],
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
    }
    for field, expected in support_fields.items():
        support = raw.get(field)
        require(support == expected, f"{path}.{field}: exact support required")
        require(isinstance(support, list), f"{path}.{field}: list required")
        require(support == sorted(support), f"{path}.{field}: sorted")
        require(len(support) == len(set(support)), f"{path}.{field}: duplicates")
        require(values["artifact_id"] not in support, f"{path}: self support")
        output[field] = list(support)
    output["evidence"] = values["evidence"]
    output["component_scale_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t11_certificate = certificate.get("recurrent_block_closure_frontier_certificate")
    t13_certificate = certificate.get("state_equivalence_frontier_certificate")
    raw_statuses = certificate.get("component_scale_records")
    raw_semantics = certificate.get("component_scale_semantic_certificates")
    raw_artifacts = certificate.get("component_scale_artifacts")
    require(isinstance(t11_certificate, dict),
            "recurrent_block_closure_frontier_certificate: expected object")
    require(isinstance(t13_certificate, dict),
            "state_equivalence_frontier_certificate: expected object")
    for name, value in (
        ("component_scale_records", raw_statuses),
        ("component_scale_semantic_certificates", raw_semantics),
        ("component_scale_artifacts", raw_artifacts),
    ):
        require(isinstance(value, list), f"{name}: expected list")

    t11_frontier.validate_certificate(t11_certificate)
    t11_exact = t11_frontier.exact_certificate(t11_certificate)
    t13_frontier.validate_certificate(t13_certificate)
    t13_exact = t13_frontier.exact_certificate(t13_certificate)

    t10_certificate = t11_certificate["transition_resource_frontier_certificate"]
    t06_certificate = t10_certificate["candidate_policy_frontier_certificate"]
    t07_from_t11 = t06_certificate["fate_transition_state_frontier_certificate"]
    require(
        t13_certificate["fate_transition_state_frontier_certificate"]["certificate_sha256"]
        == t07_from_t11["certificate_sha256"],
        "T13 and T11 use different T07 semantic roots",
    )

    t04_certificate = t07_from_t11["block_interface_population_frontier_certificate"]
    target_registry = t04_certificate["atomic_target_artifact_registry_certificate"]
    target_artifacts.validate_certificate(target_registry)
    target_exact = target_artifacts.exact_certificate(target_registry)
    current = target_registry["current_frontier_execution_certificate"]
    atomic_certificate = current["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    t03_certificate = t04_certificate["slot_candidate_population_frontier_certificate"]
    rule_certificate = t03_certificate["rule_exhaustiveness_frontier_certificate"]
    source_registry = rule_certificate["source_truth_frontier_execution_certificate"][
        "source_statement_truth_registry_certificate"
    ]
    obligation_certificate = source_registry["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    closure_exact = closure.exact_certificate(closure_certificate)

    common_records = t11_exact["recurrent_block_common_weight_records"]
    require(common_records, "T14 requires exact T11 common-weight records")
    common_by_block = {record["block_id"]: record for record in common_records}
    require(
        len(common_by_block) == len(common_records),
        "T11 common-weight records: duplicate block_id",
    )
    common_artifact_by_block = {
        item["block_id"]: item["artifact_id"]
        for item in t11_exact["recurrent_block_common_weight_artifacts"]
    }
    closure_artifact_by_block = {
        item["block_id"]: item["artifact_id"]
        for item in t11_exact["recurrent_block_closure_artifacts"]
    }
    block_ids = sorted(common_by_block)

    global_records = t13_exact["global_state_records"]
    require(global_records, "T14 requires exact T13 global-state records")
    class_artifact_by_global = {
        item["global_state_id"]: item["artifact_id"]
        for item in t13_exact["state_equivalence_class_artifacts"]
    }
    member_blocks = {
        member["block_id"]
        for global_record in global_records
        for member in global_record["members"]
    }
    require(
        member_blocks == set(block_ids),
        "T13 local-state blocks differ from exact T11 block bank",
    )

    weights_by_block = {
        block_id: {
            item["state_id"]: item["weight"]
            for item in common_by_block[block_id]["state_weights"]
        }
        for block_id in block_ids
    }
    for global_record in global_records:
        for member in global_record["members"]:
            require(
                member["local_state_id"] in weights_by_block[member["block_id"]],
                f"global state {global_record['global_state_id']}: local state lacks T11 weight",
            )

    adjacency: dict[str, set[str]] = {block_id: set() for block_id in block_ids}
    for global_record in global_records:
        blocks = global_record["member_blocks"]
        for index, left in enumerate(blocks):
            for right in blocks[index + 1:]:
                adjacency[left].add(right)
                adjacency[right].add(left)

    components: list[list[str]] = []
    unseen = set(block_ids)
    while unseen:
        root = min(unseen)
        queue = deque([root])
        seen = {root}
        while queue:
            current_block = queue.popleft()
            for nxt in sorted(adjacency[current_block]):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        unseen -= seen
        components.append(sorted(seen))

    arithmetic_records: list[dict[str, Any]] = []
    multiplier_by_block: dict[str, int] = {}
    global_weight_records: list[dict[str, Any]] = []

    global_by_component_blocks: dict[tuple[str, ...], list[dict[str, Any]]] = {}
    for component_blocks in components:
        key = tuple(component_blocks)
        global_by_component_blocks[key] = [
            global_record
            for global_record in global_records
            if any(block_id in component_blocks for block_id in global_record["member_blocks"])
        ]

    for component_blocks in components:
        key = tuple(component_blocks)
        component_globals = sorted(
            global_by_component_blocks[key],
            key=lambda item: item["global_state_id"],
        )
        shared_globals = [
            item for item in component_globals if item["member_count"] > 1
        ]
        component_core = {
            "block_ids": component_blocks,
            "shared_global_state_ids": [
                item["global_state_id"] for item in shared_globals
            ],
        }
        component_id = f"component::{catalogue.canonical_digest(component_core)[:24]}"

        constraints: dict[str, list[tuple[str, Fraction, str]]] = defaultdict(list)
        raw_equation_pairs: list[
            tuple[dict[str, Any], dict[str, Any], dict[str, Any]]
        ] = []
        for global_record in shared_globals:
            members = global_record["members"]
            left = members[0]
            left_weight = weights_by_block[left["block_id"]][left["local_state_id"]]
            for right in members[1:]:
                right_weight = weights_by_block[right["block_id"]][
                    right["local_state_id"]
                ]
                ratio = Fraction(left_weight, right_weight)
                constraints[left["block_id"]].append(
                    (right["block_id"], ratio, global_record["global_state_id"])
                )
                constraints[right["block_id"]].append(
                    (left["block_id"], Fraction(1, 1) / ratio, global_record["global_state_id"])
                )
                raw_equation_pairs.append((global_record, left, right))

        root = component_blocks[0]
        scales: dict[str, Fraction] = {root: Fraction(1, 1)}
        queue = deque([root])
        while queue:
            block_id = queue.popleft()
            for neighbor, ratio, global_state_id in sorted(
                constraints.get(block_id, []),
                key=lambda item: (item[0], item[2], item[1].numerator, item[1].denominator),
            ):
                proposed = scales[block_id] * ratio
                if neighbor in scales:
                    require(
                        scales[neighbor] == proposed,
                        f"component {component_id}: scale conflict through {global_state_id}",
                    )
                else:
                    scales[neighbor] = proposed
                    queue.append(neighbor)
        require(
            set(scales) == set(component_blocks),
            f"component {component_id}: ratio graph does not reach every block",
        )

        denominator = 1
        for scale in scales.values():
            denominator = lcm(denominator, scale.denominator)
        raw_multipliers = {
            block_id: int(scales[block_id] * denominator)
            for block_id in component_blocks
        }
        common_gcd = math.gcd(*raw_multipliers.values())
        multipliers = {
            block_id: raw_multipliers[block_id] // common_gcd
            for block_id in component_blocks
        }
        require(
            math.gcd(*multipliers.values()) == 1,
            f"component {component_id}: multipliers are not primitive",
        )
        for block_id in component_blocks:
            multiplier_by_block[block_id] = multipliers[block_id]

        multiplier_records = []
        for block_id in component_blocks:
            item = {
                "block_id": block_id,
                "rational_scale_numerator": scales[block_id].numerator,
                "rational_scale_denominator": scales[block_id].denominator,
                "primitive_integer_multiplier": multipliers[block_id],
                "t11_state_weights_sha256": common_by_block[block_id][
                    "state_weights_sha256"
                ],
            }
            item["block_scale_multiplier_sha256"] = catalogue.canonical_digest(item)
            multiplier_records.append(item)

        equation_records = []
        for global_record, left, right in raw_equation_pairs:
            left_weight = weights_by_block[left["block_id"]][left["local_state_id"]]
            right_weight = weights_by_block[right["block_id"]][right["local_state_id"]]
            left_scaled = multipliers[left["block_id"]] * left_weight
            right_scaled = multipliers[right["block_id"]] * right_weight
            require(
                left_scaled == right_scaled,
                f"global state {global_record['global_state_id']}: scaled weights disagree",
            )
            equation = {
                "component_id": component_id,
                "global_state_id": global_record["global_state_id"],
                "global_state_record_sha256": global_record[
                    "global_state_record_sha256"
                ],
                "left_block_id": left["block_id"],
                "left_local_state_id": left["local_state_id"],
                "left_local_weight": left_weight,
                "left_block_multiplier": multipliers[left["block_id"]],
                "left_scaled_weight": left_scaled,
                "right_block_id": right["block_id"],
                "right_local_state_id": right["local_state_id"],
                "right_local_weight": right_weight,
                "right_block_multiplier": multipliers[right["block_id"]],
                "right_scaled_weight": right_scaled,
            }
            equation["scale_equation_sha256"] = catalogue.canonical_digest(equation)
            equation_records.append(equation)
        equation_records.sort(
            key=lambda item: (
                item["global_state_id"],
                item["left_block_id"],
                item["left_local_state_id"],
                item["right_block_id"],
                item["right_local_state_id"],
            )
        )

        component_global_records = []
        for global_record in component_globals:
            values = [
                multipliers[member["block_id"]]
                * weights_by_block[member["block_id"]][member["local_state_id"]]
                for member in global_record["members"]
            ]
            require(
                len(set(values)) == 1,
                f"global state {global_record['global_state_id']}: component weight differs",
            )
            item = {
                "component_id": component_id,
                "global_state_id": global_record["global_state_id"],
                "global_state_record_sha256": global_record[
                    "global_state_record_sha256"
                ],
                "role": global_record["role"],
                "stratum": global_record["stratum"],
                "owner": copy.deepcopy(global_record["owner"]),
                "component_weight": values[0],
                "member_count": global_record["member_count"],
            }
            item["global_component_weight_sha256"] = catalogue.canonical_digest(item)
            component_global_records.append(item)
            global_weight_records.append(item)

        scaled_block_margins = []
        for block_id in component_blocks:
            common_record = common_by_block[block_id]
            item = {
                "component_id": component_id,
                "block_id": block_id,
                "block_multiplier": multipliers[block_id],
                "t11_minimum_margin": common_record["minimum_margin"],
                "scaled_minimum_margin": (
                    multipliers[block_id] * common_record["minimum_margin"]
                ),
                "recurrent_block_common_weight_record_sha256": common_record[
                    "recurrent_block_common_weight_record_sha256"
                ],
            }
            require(item["scaled_minimum_margin"] > 0,
                    f"block {block_id}: scaled margin is not positive")
            item["scaled_block_margin_sha256"] = catalogue.canonical_digest(item)
            scaled_block_margins.append(item)

        arithmetic = {
            "component_id": component_id,
            "block_ids": component_blocks,
            "global_state_ids": [
                item["global_state_id"] for item in component_globals
            ],
            "shared_global_state_ids": [
                item["global_state_id"] for item in shared_globals
            ],
            "block_scale_multipliers": multiplier_records,
            "scale_equation_records": equation_records,
            "global_component_weight_records": component_global_records,
            "scaled_block_margin_records": scaled_block_margins,
            "multiplier_gcd": math.gcd(*multipliers.values()),
            "minimum_scaled_margin": min(
                item["scaled_minimum_margin"] for item in scaled_block_margins
            ),
        }
        arithmetic["scale_component_arithmetic_sha256"] = catalogue.canonical_digest(
            arithmetic
        )
        arithmetic_records.append(arithmetic)

    arithmetic_records.sort(key=lambda item: item["component_id"])
    global_weight_records.sort(
        key=lambda item: (item["component_id"], item["global_state_id"])
    )

    require(
        len(raw_statuses) == len(arithmetic_records),
        "component_scale_records: exact component cardinality required",
    )
    require(
        [item.get("component_id") for item in raw_statuses]
        == [item["component_id"] for item in arithmetic_records],
        "component_scale_records: canonical component order required",
    )
    statuses = [
        exact_status_record(
            raw,
            arithmetic=arithmetic,
            path=f"component_scale_records[{index}]",
        )
        for index, (raw, arithmetic) in enumerate(
            zip(raw_statuses, arithmetic_records)
        )
    ]
    require(raw_statuses == statuses,
            "component_scale_records: canonical records/digests required")
    status_by_component = {item["component_id"]: item for item in statuses}

    semantic_groups = {item["component_id"]: [] for item in arithmetic_records}
    for raw in raw_semantics:
        require(isinstance(raw, dict),
                "component_scale_semantic_certificates: expected objects")
        component_id = raw.get("component_id")
        require(component_id in semantic_groups,
                f"component_scale_semantic_certificates: unknown component {component_id}")
        semantic_groups[component_id].append(raw)

    semantics: list[dict[str, Any]] = []
    semantic_by_component: dict[str, dict[str, Any]] = {}
    for arithmetic in arithmetic_records:
        component_id = arithmetic["component_id"]
        group = semantic_groups[component_id]
        if status_by_component[component_id]["status"] == "open":
            require(not group, f"component {component_id}: open record cannot contain semantics")
            continue
        require(len(group) == 1,
                f"component {component_id}: exactly one semantic certificate required")
        require(
            all(global_state_id in class_artifact_by_global
                for global_state_id in arithmetic["global_state_ids"]),
            f"component {component_id}: every T13 class must be proved",
        )
        require(
            all(block_id in common_artifact_by_block
                and block_id in closure_artifact_by_block
                for block_id in arithmetic["block_ids"]),
            f"component {component_id}: every T11 block artifact must be present",
        )
        semantic = exact_semantic_certificate(
            group[0],
            arithmetic=arithmetic,
            class_artifact_by_global=class_artifact_by_global,
            common_artifact_by_block=common_artifact_by_block,
            closure_artifact_by_block=closure_artifact_by_block,
            path=f"component_scale_semantic_certificate[{component_id}]",
        )
        semantics.append(semantic)
        semantic_by_component[component_id] = semantic
    require(raw_semantics == semantics,
            "component_scale_semantic_certificates: canonical order/content required")

    artifact_groups = {item["component_id"]: [] for item in arithmetic_records}
    for raw in raw_artifacts:
        require(isinstance(raw, dict), "component_scale_artifacts: expected objects")
        component_id = raw.get("component_id")
        require(component_id in artifact_groups,
                f"component_scale_artifacts: unknown component {component_id}")
        artifact_groups[component_id].append(raw)

    artifacts: list[dict[str, Any]] = []
    proof_bundles: list[dict[str, Any]] = []
    for arithmetic in arithmetic_records:
        component_id = arithmetic["component_id"]
        status = status_by_component[component_id]
        group = artifact_groups[component_id]
        if status["status"] == "open":
            require(not group, f"component {component_id}: open record cannot contain artifact")
            continue
        require(len(group) == 1,
                f"component {component_id}: exactly one scale artifact required")
        semantic = semantic_by_component[component_id]
        artifact = exact_component_artifact(
            group[0],
            arithmetic=arithmetic,
            semantic=semantic,
            path=f"component_scale_artifact[{component_id}]",
        )
        artifacts.append(artifact)
        proof_bundle = {
            "component_id": component_id,
            "component_scale_record_core_sha256": status[
                "component_scale_record_core_sha256"
            ],
            "scale_component_arithmetic_sha256": arithmetic[
                "scale_component_arithmetic_sha256"
            ],
            "component_scale_semantic_certificate_sha256": semantic[
                "component_scale_semantic_certificate_sha256"
            ],
            "component_scale_artifact_sha256": artifact[
                "component_scale_artifact_sha256"
            ],
            "support_t13_class_artifact_ids": artifact[
                "support_t13_class_artifact_ids"
            ],
            "support_t11_common_weight_artifact_ids": artifact[
                "support_t11_common_weight_artifact_ids"
            ],
            "support_t11_block_closure_artifact_ids": artifact[
                "support_t11_block_closure_artifact_ids"
            ],
        }
        proof_bundle["component_scale_proof_bundle_sha256"] = catalogue.canonical_digest(
            proof_bundle
        )
        require(
            status["verification_digest"]
            == proof_bundle["component_scale_proof_bundle_sha256"],
            f"component {component_id}: verification digest does not bind exact bundle",
        )
        proof_bundles.append(proof_bundle)
    require(raw_artifacts == artifacts,
            "component_scale_artifacts: canonical order/content required")
    artifact_ids = [item["artifact_id"] for item in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)),
            "component_scale_artifacts: duplicate artifact_id")

    counts = Counter(item["status"] for item in statuses)
    t11_ready = int(t11_exact["claims"]["t11_recurrent_block_closure_ready"])
    t13_ready = int(t13_exact["claims"]["t13_state_equivalence_ready"])
    t14_ready = int(
        t11_ready
        and t13_ready
        and counts["proved"] == len(statuses)
        and len(semantics) == len(statuses)
        and len(artifacts) == len(statuses)
    )
    proof_bank = {
        "t11_recurrent_block_closure_proof_bank_sha256": t11_exact["claims"][
            "t11_recurrent_block_closure_proof_bank_sha256"
        ],
        "t13_state_equivalence_proof_bank_sha256": t13_exact["claims"][
            "state_equivalence_frontier_proof_bank_sha256"
        ],
        "component_scale_arithmetic_records_sha256": catalogue.canonical_digest(
            arithmetic_records
        ),
        "global_component_weight_records_sha256": catalogue.canonical_digest(
            global_weight_records
        ),
        "component_scale_records_sha256": catalogue.canonical_digest(statuses),
        "component_scale_semantic_certificates_sha256": catalogue.canonical_digest(
            semantics
        ),
        "component_scale_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "component_scale_proof_bundles_sha256": catalogue.canonical_digest(
            proof_bundles
        ),
    }
    proof_bank["component_scale_frontier_proof_bank_sha256"] = catalogue.canonical_digest(
        proof_bank
    )

    closure_by_id = {
        item["obligation_id"]: item
        for item in closure_exact["obligation_closure_records"]
    }
    require(
        int(closure_by_id["COMPONENT_SCALE_SEMANTIC"]["closed"]) == t14_ready,
        "COMPONENT_SCALE_SEMANTIC closure disagrees with exact T14 bank",
    )
    obligation_records = [
        artifact for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "COMPONENT_SCALE_SEMANTIC"
    ]
    require(
        len(obligation_records) == (1 if t14_ready else 0),
        "COMPONENT_SCALE_SEMANTIC artifact presence disagrees with readiness",
    )
    if t14_ready:
        artifact = obligation_records[0]
        require(artifact["artifact_kind"] == "component-scale-proof",
                "COMPONENT_SCALE_SEMANTIC: wrong artifact kind")
        require(artifact["locator"] == OBLIGATION_LOCATOR,
                "COMPONENT_SCALE_SEMANTIC: locator mismatch")
        require(
            artifact["digest"] == proof_bank["component_scale_frontier_proof_bank_sha256"],
            "COMPONENT_SCALE_SEMANTIC: digest mismatch",
        )
        expected_support = sorted(
            item["artifact_id"]
            for item in obligation_exact["proof_artifacts"]
            if item["obligation_id"]
            in {"CROSS_BLOCK_STATE_IDENTITY_SEMANTIC", "CLOSED_STRICT_RECURRENT_BLOCKS"}
        )
        require(
            artifact["support_artifact_ids"] == expected_support,
            "COMPONENT_SCALE_SEMANTIC: exact T11/T13 obligation support required",
        )

    target_results = {
        item["target_id"]: item for item in atomic_exact["target_result_records"]
    }
    require(
        int(target_results["T14_COMPONENT_SCALES"]["effective_target_complete"])
        == t14_ready,
        "T14_COMPONENT_SCALES completion disagrees with exact T14 bank",
    )
    target_artifact_by_id = {
        artifact["target_id"]: artifact
        for artifact in target_exact["atomic_target_artifacts"]
    }
    target_artifact = target_artifact_by_id.get("T14_COMPONENT_SCALES")
    if t14_ready:
        require(target_artifact is not None, "completed T14 target missing artifact")
        require(target_artifact["artifact_kind"] == "component-scale-proof",
                "T14 target requires component-scale-proof")
        require(target_artifact["proof_locator"] == T14_TARGET_LOCATOR,
                "T14 target proof locator mismatch")
        require(
            target_artifact["proof_digest"]
            == proof_bank["component_scale_frontier_proof_bank_sha256"],
            "T14 target proof digest mismatch",
        )
    else:
        require(target_artifact is None, "open T14 target cannot contain target artifact")

    claims = {
        "recurrent_blocks": len(block_ids),
        "global_state_classes": len(global_records),
        "scale_components": len(arithmetic_records),
        "shared_global_state_classes": sum(
            item["member_count"] > 1 for item in global_records
        ),
        "scale_equations": sum(
            len(item["scale_equation_records"]) for item in arithmetic_records
        ),
        "global_component_weights": len(global_weight_records),
        "open_scale_components": counts["open"],
        "proved_scale_components": counts["proved"],
        "component_scale_artifacts": len(artifacts),
        "maximum_block_multiplier": max(multiplier_by_block.values()),
        "minimum_scaled_margin": min(
            item["minimum_scaled_margin"] for item in arithmetic_records
        ),
        "t11_recurrent_block_closure_ready": t11_ready,
        "t13_state_equivalence_ready": t13_ready,
        "t14_component_scales_ready": t14_ready,
        "exact_t11_t13_shared_root_identity": 1,
        "exact_shared_state_scale_equations": 1,
        "exact_ratio_cycle_consistency": 1,
        "primitive_componentwise_integer_multipliers": 1,
        "exact_global_component_weights": 1,
        "disconnected_components_independently_normalized": 1,
        "noncircular_t14_bank_binding": 1,
        "all_n_proved_by_checker": 0,
        "open_component_ids": [
            item["component_id"] for item in statuses if item["status"] == "open"
        ],
        "component_scale_arithmetic_records_sha256": catalogue.canonical_digest(
            arithmetic_records
        ),
        "global_component_weight_records_sha256": catalogue.canonical_digest(
            global_weight_records
        ),
        "component_scale_records_sha256": catalogue.canonical_digest(statuses),
        "component_scale_semantic_certificates_sha256": catalogue.canonical_digest(
            semantics
        ),
        "component_scale_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "component_scale_frontier_proof_bank_sha256": proof_bank[
            "component_scale_frontier_proof_bank_sha256"
        ],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "atomic_target_artifact_registry_sha256": target_registry["certificate_sha256"],
    }
    return {
        "component_scale_arithmetic_records": arithmetic_records,
        "global_component_weight_records": global_weight_records,
        "component_scale_records": statuses,
        "component_scale_semantic_certificates": semantics,
        "component_scale_artifacts": artifacts,
        "component_scale_proof_bundles": proof_bundles,
        "component_scale_frontier_proof_bank": proof_bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "component_scale_arithmetic_records",
        "global_component_weight_records",
        "component_scale_records",
        "component_scale_semantic_certificates",
        "component_scale_artifacts",
        "component_scale_proof_bundles",
        "component_scale_frontier_proof_bank",
        "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {
        key: value for key, value in certificate.items() if key != "certificate_sha256"
    }
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "blocks": claims["recurrent_blocks"],
        "components": claims["scale_components"],
        "equations": claims["scale_equations"],
        "proved": claims["proved_scale_components"],
        "minimum_margin": claims["minimum_scaled_margin"],
        "ready": claims["t14_component_scales_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    t11_certificate: dict[str, Any],
    t13_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    semantic_certificates: list[dict[str, Any]],
    artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "recurrent_block_closure_frontier_certificate": t11_certificate,
        "state_equivalence_frontier_certificate": t13_certificate,
        "component_scale_records": records,
        "component_scale_semantic_certificates": semantic_certificates,
        "component_scale_artifacts": artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_component_scale_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()

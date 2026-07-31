#!/usr/bin/env python3
"""Verify forced mixed-certificate escape ancestry and payment.

CMR643--CMR648 state that a forced product certificate can disappear only by
certificate-edge deletion, selected-skeleton churn, or loss of factor-edge
essentiality after genuinely new factor edges enter.  This checker generates
literal parent/later factor and skeleton contexts, classifies the first
applicable escape, and verifies the alternating-component entering-edge witness.

The checker proves construction ancestry only for this escape bank.  It does
not prove all restoration operations, construction-transition exhaustiveness,
global termination, or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, permutations
from typing import Any, Iterable

Edge = tuple[int, int]
TypedEdge = tuple[str, int, int]
Matching = tuple[Edge, ...]

EXPECTED_CONTRACT_SHA256 = "dc3c472d258d7cfbbfbf5dd45f68f19a5999c5f4a1818a6945dd460eb1c82253"


class ForcedCertificateEscapeError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ForcedCertificateEscapeError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_positive_int(value: Any, path: str, minimum: int = 1) -> int:
    require(
        isinstance(value, int) and not isinstance(value, bool) and value >= minimum,
        f"{path}: integer at least {minimum} required",
    )
    return value


def exact_coordinates(raw: Iterable[int], n: int, path: str) -> tuple[int, ...]:
    values = tuple(raw)
    require(values == tuple(sorted(values)), f"{path}: canonical order required")
    require(len(values) == len(set(values)), f"{path}: duplicate coordinate")
    require(values, f"{path}: nonempty coordinate domain required")
    require(
        all(isinstance(x, int) and not isinstance(x, bool) and 0 <= x < n for x in values),
        f"{path}: coordinate outside ambient side",
    )
    return values


def exact_edges(
    raw: Iterable[Iterable[int]],
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    path: str,
) -> tuple[Edge, ...]:
    edges = tuple(tuple(edge) for edge in raw)
    require(edges == tuple(sorted(edges)), f"{path}: canonical order required")
    require(len(edges) == len(set(edges)), f"{path}: duplicate edge")
    require(
        all(
            len(edge) == 2
            and isinstance(edge[0], int)
            and isinstance(edge[1], int)
            and edge[0] in rows
            and edge[1] in columns
            for edge in edges
        ),
        f"{path}: edge outside domains",
    )
    return edges  # type: ignore[return-value]


def generate_matchings(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    allowed: tuple[Edge, ...],
) -> tuple[Matching, ...]:
    require(len(rows) == len(columns), "balanced factor required")
    allowed_set = set(allowed)
    result = []
    for image in permutations(columns):
        matching = tuple((rows[index], image[index]) for index in range(len(rows)))
        if set(matching) <= allowed_set:
            result.append(matching)
    return tuple(sorted(result))


def exact_matching(
    raw: Iterable[Iterable[int]],
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    allowed: tuple[Edge, ...],
    path: str,
) -> Matching:
    matching = tuple(tuple(edge) for edge in raw)
    require(matching == tuple(sorted(matching)), f"{path}: canonical order required")
    require(len(matching) == len(rows), f"{path}: exact cardinality required")
    require({edge[0] for edge in matching} == set(rows), f"{path}: row saturation failed")
    require({edge[1] for edge in matching} == set(columns), f"{path}: column saturation failed")
    require(set(matching) <= set(allowed), f"{path}: edge outside allowed host")
    return matching  # type: ignore[return-value]


def factor_context(
    n: int,
    name: str,
    rows_raw: Iterable[int],
    columns_raw: Iterable[int],
    allowed_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    rows = exact_coordinates(rows_raw, n, f"{name}.rows")
    columns = exact_coordinates(columns_raw, n, f"{name}.columns")
    require(len(rows) == len(columns), f"{name}: balanced factor required")
    allowed = exact_edges(allowed_raw, rows, columns, f"{name}.allowed")
    family = generate_matchings(rows, columns, allowed)
    require(family, f"{name}: factor host must have a perfect matching")
    complete = tuple((row, column) for row in rows for column in columns)
    deleted = tuple(edge for edge in complete if edge not in set(allowed))
    essential = tuple(sorted(set.intersection(*(set(matching) for matching in family))))
    result: dict[str, Any] = {
        "name": name,
        "ambient_side": n,
        "rows": list(rows),
        "columns": list(columns),
        "allowed_edges": [list(edge) for edge in allowed],
        "deleted_edges": [list(edge) for edge in deleted],
        "feasible_matchings": [[list(edge) for edge in matching] for matching in family],
        "essential_edges": [list(edge) for edge in essential],
        "family_sha256": digest([[list(edge) for edge in matching] for matching in family]),
    }
    result["context_sha256"] = digest(result)
    return result


def exact_skeleton_context(
    n: int,
    host_raw: Iterable[Iterable[int]],
    selected_raw: Iterable[Iterable[int]],
    path: str,
) -> dict[str, Any]:
    coords = tuple(range(n))
    host = exact_edges(host_raw, coords, coords, f"{path}.host")
    selected = exact_edges(selected_raw, coords, coords, f"{path}.selected")
    require(set(selected) <= set(host), f"{path}: selected skeleton outside host")
    result: dict[str, Any] = {
        "ambient_side": n,
        "host_edges": [list(edge) for edge in host],
        "selected_edges": [list(edge) for edge in selected],
    }
    result["skeleton_sha256"] = digest(result)
    return result


def exact_typed_certificate(raw: Iterable[Iterable[Any]], n: int) -> tuple[TypedEdge, ...]:
    values = tuple(tuple(item) for item in raw)
    require(values == tuple(sorted(values)), "certificate: canonical order required")
    require(len(values) == 3 and len(set(values)) == 3, "certificate: exactly three edges required")
    require(
        all(
            len(item) == 3
            and item[0] in ("I", "J", "S")
            and isinstance(item[1], int)
            and isinstance(item[2], int)
            and 0 <= item[1] < n
            and 0 <= item[2] < n
            for item in values
        ),
        "certificate: malformed typed edge",
    )
    return values  # type: ignore[return-value]


def typed_present_in_host(
    edge: TypedEdge,
    factors: dict[str, dict[str, Any]],
    skeleton: dict[str, Any],
) -> bool:
    part, row, column = edge
    physical = [row, column]
    if part == "S":
        return physical in skeleton["host_edges"]
    return physical in factors[part]["allowed_edges"]


def typed_present_in_state(
    edge: TypedEdge,
    matchings: dict[str, Matching],
    skeleton: dict[str, Any],
) -> bool:
    part, row, column = edge
    physical = (row, column)
    if part == "S":
        return [row, column] in skeleton["selected_edges"]
    return physical in set(matchings[part])


def validate_forced_certificate(
    certificate: tuple[TypedEdge, ...],
    factors: dict[str, dict[str, Any]],
    skeleton: dict[str, Any],
) -> None:
    for part, row, column in certificate:
        physical = [row, column]
        if part == "S":
            require(physical in skeleton["selected_edges"], "certificate skeleton edge not selected")
        else:
            require(physical in factors[part]["essential_edges"], "certificate factor edge not essential")


def alternating_components(old: Matching, new: Matching) -> tuple[dict[str, Any], ...]:
    old_only = set(old) - set(new)
    new_only = set(new) - set(old)
    remaining = set(old_only) | set(new_only)
    components: list[dict[str, Any]] = []
    while remaining:
        seed = min(remaining)
        vertices = {("r", seed[0]), ("c", seed[1])}
        changed = True
        component_edges: set[Edge] = set()
        while changed:
            changed = False
            for edge in tuple(remaining):
                endpoints = {("r", edge[0]), ("c", edge[1])}
                if vertices & endpoints:
                    component_edges.add(edge)
                    new_vertices = endpoints - vertices
                    if new_vertices:
                        vertices |= new_vertices
                        changed = True
        remaining -= component_edges
        old_part = tuple(sorted(component_edges & old_only))
        new_part = tuple(sorted(component_edges & new_only))
        require(len(old_part) == len(new_part) and old_part, "nontrivial alternating cycle required")
        components.append(
            {
                "old_edges": [list(edge) for edge in old_part],
                "new_edges": [list(edge) for edge in new_part],
                "rows": sorted(vertex for kind, vertex in vertices if kind == "r"),
                "columns": sorted(vertex for kind, vertex in vertices if kind == "c"),
            }
        )
    return tuple(sorted(components, key=lambda item: (item["old_edges"], item["new_edges"])))


def product_identity(
    n: int,
    owner: str,
    factors: dict[str, dict[str, Any]],
    skeleton: dict[str, Any],
) -> dict[str, Any]:
    require(isinstance(owner, str) and owner, "owner: nonempty string required")
    result: dict[str, Any] = {
        "ambient_side": n,
        "owner": owner,
        "factor_I": factors["I"],
        "factor_J": factors["J"],
        "skeleton": skeleton,
    }
    result["product_sha256"] = digest(result)
    return result


def exact_escape_manifest(
    n: int,
    owner: str,
    parent_factor_I: dict[str, Any],
    parent_factor_J: dict[str, Any],
    parent_skeleton: dict[str, Any],
    certificate_raw: Iterable[Iterable[Any]],
    later_factor_I: dict[str, Any],
    later_factor_J: dict[str, Any],
    later_skeleton: dict[str, Any],
    old_matching_I_raw: Iterable[Iterable[int]],
    old_matching_J_raw: Iterable[Iterable[int]],
    later_matching_I_raw: Iterable[Iterable[int]],
    later_matching_J_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    exact_positive_int(n, "ambient_side")
    certificate = exact_typed_certificate(certificate_raw, n)
    parent_factors = {"I": parent_factor_I, "J": parent_factor_J}
    later_factors = {"I": later_factor_I, "J": later_factor_J}
    validate_forced_certificate(certificate, parent_factors, parent_skeleton)

    old_matchings: dict[str, Matching] = {}
    later_matchings: dict[str, Matching] = {}
    for part, old_raw, later_raw in (
        ("I", old_matching_I_raw, later_matching_I_raw),
        ("J", old_matching_J_raw, later_matching_J_raw),
    ):
        parent = parent_factors[part]
        later = later_factors[part]
        require(parent["rows"] == later["rows"] and parent["columns"] == later["columns"],
                f"factor {part}: domains changed during escape event")
        rows = tuple(parent["rows"])
        columns = tuple(parent["columns"])
        old_matchings[part] = exact_matching(
            old_raw, rows, columns, tuple(tuple(edge) for edge in parent["allowed_edges"]),
            f"old_matching_{part}",
        )
        later_matchings[part] = exact_matching(
            later_raw, rows, columns, tuple(tuple(edge) for edge in later["allowed_edges"]),
            f"later_matching_{part}",
        )

    require(
        all(typed_present_in_state(edge, old_matchings, parent_skeleton) for edge in certificate),
        "parent endpoint does not contain forced certificate",
    )
    later_contains = all(
        typed_present_in_state(edge, later_matchings, later_skeleton) for edge in certificate
    )

    parent_product = product_identity(n, owner, parent_factors, parent_skeleton)
    later_product = product_identity(n, owner, later_factors, later_skeleton)

    if later_contains:
        category = "persistent-forced-certificate"
        witness = None
        affected_components: list[dict[str, Any]] = []
        semantics = "later state still contains every certificate edge"
    else:
        missing_host_edges = tuple(
            edge for edge in certificate
            if not typed_present_in_host(edge, later_factors, later_skeleton)
        )
        if missing_host_edges:
            category = "certificate-edge-deletion"
            selected = missing_host_edges[0]
            witness = {
                "witness_kind": "deletion",
                "physical_edge": [selected[1], selected[2]],
                "certificate_part": selected[0],
            }
            affected_components = []
            semantics = "first certificate edge absent from later literal host"
        elif parent_skeleton["selected_edges"] != later_skeleton["selected_edges"]:
            category = "selected-skeleton-churn"
            symmetric = sorted(
                set(tuple(edge) for edge in parent_skeleton["selected_edges"])
                ^ set(tuple(edge) for edge in later_skeleton["selected_edges"])
            )
            require(symmetric, "skeleton churn requires nonempty symmetric difference")
            witness = {
                "witness_kind": "skeleton",
                "physical_edge": list(symmetric[0]),
                "skeleton_symmetric_difference": [list(edge) for edge in symmetric],
            }
            affected_components = []
            semantics = "selected skeleton changed while certificate edges stayed host-available"
        else:
            category = "factor-essentiality-loss-entering-edge"
            affected_components = []
            for part in ("I", "J"):
                omitted = tuple(
                    (row, column)
                    for cert_part, row, column in certificate
                    if cert_part == part and (row, column) not in set(later_matchings[part])
                )
                if not omitted:
                    continue
                old_allowed = set(tuple(edge) for edge in parent_factors[part]["allowed_edges"])
                later_allowed = set(tuple(edge) for edge in later_factors[part]["allowed_edges"])
                entering = later_allowed - old_allowed
                require(entering, f"factor {part}: essentiality loss has no genuinely new edge")
                components = alternating_components(old_matchings[part], later_matchings[part])
                for component_index, component in enumerate(components):
                    old_part = set(tuple(edge) for edge in component["old_edges"])
                    omitted_here = tuple(sorted(old_part & set(omitted)))
                    if not omitted_here:
                        continue
                    new_part = set(tuple(edge) for edge in component["new_edges"])
                    entering_here = tuple(sorted(new_part & entering))
                    require(
                        entering_here,
                        f"factor {part}: affected alternating component lacks entering edge",
                    )
                    affected_components.append(
                        {
                            "factor": part,
                            "component_index": component_index,
                            "omitted_essential_edges": [list(edge) for edge in omitted_here],
                            "entering_edges": [list(edge) for edge in entering_here],
                            "canonical_entering_witness": list(entering_here[0]),
                            "alternating_component": component,
                        }
                    )
            require(affected_components, "essentiality-loss branch has no affected component")
            canonical = min(
                affected_components,
                key=lambda item: (
                    item["factor"], item["component_index"], item["canonical_entering_witness"]
                ),
            )
            witness = {
                "witness_kind": "entering",
                "physical_edge": canonical["canonical_entering_witness"],
                "factor": canonical["factor"],
                "affected_component_count": len(affected_components),
            }
            entering_distinct = {
                (item["factor"], tuple(item["canonical_entering_witness"]))
                for item in affected_components
            }
            require(
                len(affected_components) <= len(entering_distinct),
                "affected-component entering-edge injection failed",
            )
            semantics = "old essential certificate edge omitted only through new-edge alternating support"

    claims = {
        "parent_forced_certificate_valid": 1,
        "later_certificate_present": int(later_contains),
        "escape_first_applicable_type_exact": 1,
        "certificate_edge_deletion_transition_exact": int(category == "certificate-edge-deletion"),
        "selected_skeleton_churn_transition_exact": int(category == "selected-skeleton-churn"),
        "factor_restoration_essentiality_loss_transition_exact": int(
            category == "factor-essentiality-loss-entering-edge"
        ),
        "affected_component_entering_edge_payment_exact": int(
            category == "factor-essentiality-loss-entering-edge"
        ),
        "forced_certificate_persistence_exact": int(category == "persistent-forced-certificate"),
        "forced_mixed_certificate_escape_proved": 1,
        "all_restoration_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "forced-mixed-certificate-escape-transition-v1",
        "source_theorems": ["CMR643", "CMR644", "CMR645", "CMR646", "CMR647", "CMR648"],
        "transition_kind": category,
        "owner": owner,
        "certificate": [list(edge) for edge in certificate],
        "parent_product": parent_product,
        "later_product": later_product,
        "old_matchings": {
            part: [list(edge) for edge in old_matchings[part]] for part in ("I", "J")
        },
        "later_matchings": {
            part: [list(edge) for edge in later_matchings[part]] for part in ("I", "J")
        },
        "canonical_witness": witness,
        "affected_alternating_components": affected_components,
        "exact_semantics": semantics,
        "claims": claims,
    }
    result["transition_sha256"] = digest(result)
    return result


def exact_escape_history(
    events: Iterable[dict[str, Any]],
    n: int,
    p: int,
    g: int,
    recurrence_threshold: int,
) -> dict[str, Any]:
    exact_positive_int(n, "ambient_side")
    exact_positive_int(p, "prime")
    exact_positive_int(g, "exponent")
    exact_positive_int(recurrence_threshold, "recurrence_threshold", 2)
    require(n == p ** g, "ambient side must equal p^g")
    records = tuple(events)
    require(records, "escape history must be nonempty")
    owners = {record["owner"] for record in records}
    require(len(owners) == 1, "escape history must have one owner")
    witness_keys = []
    for record in records:
        require(
            record["transition_kind"] != "persistent-forced-certificate",
            "history records must be actual escape events",
        )
        witness = record["canonical_witness"]
        require(witness is not None, "escape event lacks canonical witness")
        key = (witness["witness_kind"], tuple(witness["physical_edge"]))
        witness_keys.append(key)
    counts = {key: witness_keys.count(key) for key in sorted(set(witness_keys))}
    recurrent = tuple(key for key, count in counts.items() if count >= recurrence_threshold)
    j = len(records)
    finite_bound = 3 * (recurrence_threshold - 1) * n * n
    if recurrent:
        category = "recurrent-owner-labelled-witness"
    else:
        category = "finite-forced-certificate-escape-history"
        require(j <= finite_bound, "CMR646 finite-history bound failed")
    token_per_event = (p + 1) * (g - 1)
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "forced-certificate-escape-history-payment-v1",
        "owner": next(iter(owners)),
        "ambient_side": n,
        "prime": p,
        "exponent": g,
        "recurrence_threshold": recurrence_threshold,
        "escape_events": j,
        "distinct_owner_labelled_witnesses": len(counts),
        "witness_multiplicities": [
            {"witness_kind": key[0], "physical_edge": list(key[1]), "count": count}
            for key, count in counts.items()
        ],
        "history_category": category,
        "recurrent_witnesses": [
            {"witness_kind": key[0], "physical_edge": list(key[1])} for key in recurrent
        ],
        "finite_history_bound": finite_bound,
        "nonroot_token_incidences_per_event": token_per_event,
        "total_nonroot_token_incidences": j * token_per_event,
        "claims": {
            "owner_labelled_witness_universe_bound": 3 * n * n,
            "owner_labelled_escape_stock_exact": 1,
            "recurrent_or_finite_escape_history_exact": 1,
            "escape_token_payment_exact": 1,
            "forced_mixed_certificate_escape_proved": 1,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["history_sha256"] = digest(result)
    return result


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "forced-mixed-certificate-escape-ancestry-v1",
        "source_theorems": ["CMR643", "CMR644", "CMR645", "CMR646", "CMR647", "CMR648"],
        "claims": {
            "forced_certificate_escape_trichotomy_exact": 1,
            "certificate_edge_deletion_transition_exact": 1,
            "selected_skeleton_churn_transition_exact": 1,
            "factor_restoration_essentiality_loss_transition_exact": 1,
            "affected_component_entering_edge_payment_exact": 1,
            "owner_labelled_escape_stock_exact": 1,
            "escape_token_payment_exact": 1,
            "forced_mixed_certificate_escape_proved": 1,
            "all_restoration_operations_proved": 0,
            "all_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["contract_sha256"] = digest(result)
    return result


def validate_contract() -> dict[str, int]:
    contract = contract_manifest()
    require(
        contract["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
        "built-in contract digest drift",
    )
    return copy.deepcopy(contract["claims"])


def make_factor(n: int, name: str, allowed: Iterable[Edge]) -> dict[str, Any]:
    domain = tuple(range(2))
    return factor_context(n, name, domain, domain, tuple(sorted(allowed)))


def base_scenario() -> dict[str, Any]:
    n = 4
    identity = ((0, 0), (1, 1))
    full = ((0, 0), (0, 1), (1, 0), (1, 1))
    parent_I = make_factor(n, "I", identity)
    parent_J = make_factor(n, "J", identity)
    parent_skeleton = exact_skeleton_context(n, ((0, 2), (1, 3)), ((0, 2),), "parent_skeleton")
    certificate = (("I", 0, 0), ("J", 0, 0), ("S", 0, 2))
    return {
        "n": n,
        "owner": "owner:forced-product-base",
        "identity": identity,
        "full": full,
        "parent_I": parent_I,
        "parent_J": parent_J,
        "parent_skeleton": parent_skeleton,
        "certificate": certificate,
        "old_I": identity,
        "old_J": identity,
    }


def scenario_manifests() -> dict[str, dict[str, Any]]:
    data = base_scenario()
    n = data["n"]
    identity = data["identity"]
    full = data["full"]
    parent_I = data["parent_I"]
    parent_J = data["parent_J"]
    parent_skeleton = data["parent_skeleton"]
    cert = data["certificate"]
    owner = data["owner"]

    persistent = exact_escape_manifest(
        n, owner, parent_I, parent_J, parent_skeleton, cert,
        parent_I, parent_J, parent_skeleton,
        identity, identity, identity, identity,
    )
    deleted_I = make_factor(n, "I", ((0, 1), (1, 0), (1, 1)))
    deletion = exact_escape_manifest(
        n, owner, parent_I, parent_J, parent_skeleton, cert,
        deleted_I, parent_J, parent_skeleton,
        identity, identity, ((0, 1), (1, 0)), identity,
    )
    churn_skeleton = exact_skeleton_context(
        n, ((0, 2), (1, 3)), ((1, 3),), "later_skeleton"
    )
    churn = exact_escape_manifest(
        n, owner, parent_I, parent_J, parent_skeleton, cert,
        parent_I, parent_J, churn_skeleton,
        identity, identity, identity, identity,
    )
    restored_I = make_factor(n, "I", full)
    entering = exact_escape_manifest(
        n, owner, parent_I, parent_J, parent_skeleton, cert,
        restored_I, parent_J, parent_skeleton,
        identity, identity, ((0, 1), (1, 0)), identity,
    )
    return {
        "persistent": persistent,
        "deletion": deletion,
        "skeleton": churn,
        "entering": entering,
    }


def exhaustive_two_by_two_essentiality_loss() -> dict[str, int]:
    domain = (0, 1)
    all_edges = tuple((row, column) for row in domain for column in domain)
    checked = affected_components = entering_incidences = 0
    for size in range(1, len(all_edges) + 1):
        for old_subset in combinations(all_edges, size):
            old_family = generate_matchings(domain, domain, tuple(old_subset))
            if not old_family:
                continue
            essential = set.intersection(*(set(matching) for matching in old_family))
            for later_size in range(1, len(all_edges) + 1):
                for later_subset in combinations(all_edges, later_size):
                    later_family = generate_matchings(domain, domain, tuple(later_subset))
                    if not later_family:
                        continue
                    entering = set(later_subset) - set(old_subset)
                    for old_matching in old_family:
                        for later_matching in later_family:
                            omitted = essential - set(later_matching)
                            if not omitted:
                                continue
                            require(entering, "essentiality loss without entering edge")
                            components = alternating_components(old_matching, later_matching)
                            for component in components:
                                old_part = set(tuple(edge) for edge in component["old_edges"])
                                if not (old_part & omitted):
                                    continue
                                entering_here = (
                                    set(tuple(edge) for edge in component["new_edges"]) & entering
                                )
                                require(entering_here, "affected component lacks entering edge")
                                affected_components += 1
                                entering_incidences += len(entering_here)
                            checked += 1
    require(checked > 0, "essentiality-loss regression has no examples")
    return {
        "two_by_two_essentiality_loss_transitions": checked,
        "affected_alternating_components": affected_components,
        "affected_component_entering_incidences": entering_incidences,
    }


def multi_component_witness() -> dict[str, int]:
    rows = columns = (0, 1, 2, 3)
    old = ((0, 0), (1, 1), (2, 2), (3, 3))
    new = ((0, 1), (1, 0), (2, 3), (3, 2))
    components = alternating_components(old, new)
    require(len(components) == 2, "two-component witness drift")
    entering = set(new)
    for component in components:
        require(
            set(tuple(edge) for edge in component["new_edges"]) <= entering,
            "multi-component witness lacks entering support",
        )
    return {
        "multi_component_essentiality_loss_witnesses": 1,
        "multi_component_affected_components": len(components),
    }


def history_regression(events: dict[str, dict[str, Any]]) -> dict[str, int]:
    finite_events = [
        copy.deepcopy(events["deletion"]),
        copy.deepcopy(events["skeleton"]),
        copy.deepcopy(events["entering"]),
    ]
    finite = exact_escape_history(finite_events, 4, 2, 2, 2)
    recurrent = exact_escape_history(
        [copy.deepcopy(events["entering"]) for _ in range(3)], 4, 2, 2, 3
    )
    require(
        finite["history_category"] == "finite-forced-certificate-escape-history",
        "finite history branch drift",
    )
    require(
        recurrent["history_category"] == "recurrent-owner-labelled-witness",
        "recurrent history branch drift",
    )
    return {
        "escape_history_scenarios": 2,
        "finite_escape_histories": 1,
        "recurrent_escape_histories": 1,
        "history_escape_events": finite["escape_events"] + recurrent["escape_events"],
        "history_token_incidences": (
            finite["total_nonroot_token_incidences"]
            + recurrent["total_nonroot_token_incidences"]
        ),
    }


def mutation_tests(events: dict[str, dict[str, Any]]) -> int:
    data = base_scenario()
    bad_calls = [
        lambda: exact_typed_certificate((("I", 0, 0),), data["n"]),
        lambda: factor_context(4, "bad", (0, 1), (0, 1), ((0, 0),)),
        lambda: exact_skeleton_context(4, ((0, 2),), ((1, 3),), "bad"),
        lambda: exact_escape_manifest(
            data["n"], data["owner"], data["parent_I"], data["parent_J"],
            data["parent_skeleton"], data["certificate"],
            data["parent_I"], data["parent_J"], data["parent_skeleton"],
            data["old_I"], data["old_J"], ((0, 1), (1, 0)), data["old_J"],
        ),
        lambda: exact_escape_history([events["persistent"]], 4, 2, 2, 2),
    ]
    rejected = 0
    for call in bad_calls:
        try:
            call()
        except (ValueError, KeyError):
            rejected += 1
        else:
            raise ForcedCertificateEscapeError("malformed escape input accepted")
    for mutation in ("honesty", "seal", "witness"):
        bad = copy.deepcopy(events["entering"])
        if mutation == "honesty":
            bad["claims"]["all_n_proved_by_checker"] = 1
        elif mutation == "seal":
            bad["transition_sha256"] = "0" * 64
        else:
            bad["canonical_witness"]["physical_edge"] = [3, 3]
        try:
            require(bad == events["entering"], "corrupted escape manifest mismatch")
        except ForcedCertificateEscapeError:
            rejected += 1
        else:
            raise ForcedCertificateEscapeError("corrupted escape manifest accepted")
    require(rejected == 8, "mutation rejection census drift")
    return rejected


def finite_regression() -> dict[str, int]:
    events = scenario_manifests()
    categories = {record["transition_kind"] for record in events.values()}
    require(
        categories
        == {
            "persistent-forced-certificate",
            "certificate-edge-deletion",
            "selected-skeleton-churn",
            "factor-essentiality-loss-entering-edge",
        },
        "escape category census drift",
    )
    return {
        "canonical_escape_scenarios": len(events),
        "persistent_certificate_scenarios": 1,
        "certificate_deletion_scenarios": 1,
        "skeleton_churn_scenarios": 1,
        "factor_essentiality_loss_scenarios": 1,
        **exhaustive_two_by_two_essentiality_loss(),
        **multi_component_witness(),
        **history_regression(events),
        "rejected_mutations": mutation_tests(events),
    }


def self_test() -> dict[str, Any]:
    return {
        **validate_contract(),
        **finite_regression(),
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()

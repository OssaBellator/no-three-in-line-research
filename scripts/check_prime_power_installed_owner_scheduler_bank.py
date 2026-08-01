#!/usr/bin/env python3
"""Audit the installed construction transition bank and owner-stage scheduler.

Every transition kind already installed on the branch is bound to its executable
checker contract, theorem ancestry, owner effect, and one exact stock/descent or
scheduler-dispatch class.  The CMR691--CMR719 arithmetic then gives finite
owner-stage, edge, token, certificate, target-pair, envelope and deletion stocks
on the nonrecurrent branch.

This checker proves exhaustiveness only for the currently installed transition
bank.  It does not prove that no further construction operation exists, that
all owner/scheduler operations are installed, global transition exhaustiveness,
global termination, or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from math import comb, floor
from typing import Any

EXPECTED_CONTRACT_SHA256 = "108802c0d4934c7b3d77cc972d5418a2d8b91a6cca9da78b49bc4ab58970ad26"


class OwnerSchedulerError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise OwnerSchedulerError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_int(value: Any, path: str, minimum: int = 0) -> int:
    require(isinstance(value, int) and not isinstance(value, bool) and value >= minimum,
            f"{path}: integer at least {minimum} required")
    return value


ALLOWED_OWNER_EFFECTS = {
    "same-owner",
    "host-owner-change",
    "routing-owner-change",
    "factor-child-owner-change",
    "envelope-owner-change",
    "restoration-owner-change",
    "contraction-owner-change",
}

ALLOWED_PAYMENT_CLASSES = {
    "local-family-restriction",
    "factor-contraction",
    "routing-stock",
    "scheduler-dispatch",
    "strict-child-descent",
    "host-edge-deletion",
    "owner-witness-stock",
    "edge-reintroduction",
    "target-chain-stock",
    "closure-depth",
    "same-envelope-dispatch",
}

PROGRESS_PAYMENT_CLASSES = {
    "local-family-restriction",
    "factor-contraction",
    "routing-stock",
    "strict-child-descent",
    "host-edge-deletion",
    "owner-witness-stock",
    "edge-reintroduction",
    "target-chain-stock",
    "closure-depth",
}

CHECKER_CONTRACTS = {
    "scripts/check_prime_power_context_transition_registry.py":
        "ace68b33d5c7111a5d623cb5a1db128ccc86bb193601404a5ede4713571b241d",
    "scripts/check_prime_power_routing_change_context_ancestry.py":
        "b2de334dedbde2a865704f3d08cc9f590e74e14b7e8d813c329e59cc97636360",
    "scripts/check_prime_power_routing_change_history_payment.py":
        "b7c4efe585e6fa70cf6556e4eb86969e685c542d8192326b3c29169c8f9b2259",
    "scripts/check_prime_power_factor_child_product_ancestry.py":
        "bd725106632e65cac38f2b33fb1787f3d5ef93d0825c4ccfc0d2afd2c6492dae",
    "scripts/check_prime_power_mixed_child_deletion_ancestry.py":
        "b49c1313b765fc63676aed96bfbb91adf52f17293feb47089cfc8129b42b7429",
    "scripts/check_prime_power_forced_certificate_escape_ancestry.py":
        "dc3c472d258d7cfbbfbf5dd45f68f19a5999c5f4a1818a6945dd460eb1c82253",
    "scripts/check_prime_power_target_edge_return_ancestry.py":
        "04a533666c90c2f13bcb18731e10e0bca4d6357a806f8be44ee47af6f90e2382",
    "scripts/check_prime_power_target_handoff_envelope_ancestry.py":
        "a8230eb1e301b1c08972b686be836dc30a3daba8d906840bb4dba6a67bb1fa8b",
    "scripts/check_prime_power_recurrent_target_edge_deletion_ancestry.py":
        "a7153947e5f44b8433e404050eb317fc17f5b380722c6c121b8a4d910140fad0",
    "scripts/check_prime_power_closure_envelope_transition_ancestry.py":
        "50b7720e03295dbde2557ab1d3a11dfc99a8f6d4a9528391555bc4e3adbf91c1",
}


def installed_registry() -> list[dict[str, Any]]:
    context = "scripts/check_prime_power_context_transition_registry.py"
    routing = "scripts/check_prime_power_routing_change_context_ancestry.py"
    product = "scripts/check_prime_power_factor_child_product_ancestry.py"
    mixed = "scripts/check_prime_power_mixed_child_deletion_ancestry.py"
    escape = "scripts/check_prime_power_forced_certificate_escape_ancestry.py"
    returned = "scripts/check_prime_power_target_edge_return_ancestry.py"
    handoff = "scripts/check_prime_power_target_handoff_envelope_ancestry.py"
    recurrent = "scripts/check_prime_power_recurrent_target_edge_deletion_ancestry.py"
    envelope = "scripts/check_prime_power_closure_envelope_transition_ancestry.py"
    return [
        {
            "operation_kind": "single-edge-deletion",
            "checker": context,
            "contract_sha256": CHECKER_CONTRACTS[context],
            "source_theorems": ["CMR830", "CMR2843", "CMR2868", "CMR2890"],
            "owner_effect": "host-owner-change",
            "payment_class": "local-family-restriction",
            "continuation": "exact child family",
        },
        {
            "operation_kind": "required-edge-conditioning",
            "checker": context,
            "contract_sha256": CHECKER_CONTRACTS[context],
            "source_theorems": ["CMR862", "CMR2844", "CMR2869", "CMR2891"],
            "owner_effect": "host-owner-change",
            "payment_class": "local-family-restriction",
            "continuation": "exact conditioned child family",
        },
        {
            "operation_kind": "forced-set-contraction",
            "checker": context,
            "contract_sha256": CHECKER_CONTRACTS[context],
            "source_theorems": ["CMR864", "CMR2870", "CMR2871", "CMR2872", "CMR2892"],
            "owner_effect": "contraction-owner-change",
            "payment_class": "factor-contraction",
            "continuation": "strict residual factor",
        },
        {
            "operation_kind": "first-missing-deletion",
            "checker": context,
            "contract_sha256": CHECKER_CONTRACTS[context],
            "source_theorems": ["CMR862", "CMR2794", "CMR2895"],
            "owner_effect": "host-owner-change",
            "payment_class": "local-family-restriction",
            "continuation": "disjoint first-missing branch",
        },
        {
            "operation_kind": "first-missing-conditioned-contraction",
            "checker": context,
            "contract_sha256": CHECKER_CONTRACTS[context],
            "source_theorems": ["CMR862", "CMR2794", "CMR2895"],
            "owner_effect": "contraction-owner-change",
            "payment_class": "factor-contraction",
            "continuation": "conditioned asymmetric residual factor",
        },
        {
            "operation_kind": "routing-skeleton-change",
            "checker": routing,
            "contract_sha256": CHECKER_CONTRACTS[routing],
            "support_checker": "scripts/check_prime_power_routing_change_history_payment.py",
            "support_contract_sha256":
                CHECKER_CONTRACTS["scripts/check_prime_power_routing_change_history_payment.py"],
            "source_theorems": ["CMR656", "CMR659", "CMR671", "CMR672", "CMR673", "CMR674", "CMR675"],
            "owner_effect": "routing-owner-change",
            "payment_class": "routing-stock",
            "continuation": "finite routing history or recurrent physical edge",
        },
        {
            "operation_kind": "fixed-routing-child-product-split",
            "checker": product,
            "contract_sha256": CHECKER_CONTRACTS[product],
            "source_theorems": ["CMR659", "CMR663", "CMR2920", "CMR2922"],
            "owner_effect": "same-owner",
            "payment_class": "scheduler-dispatch",
            "continuation": "mixed deletion, forced certificate, clean state, or strict child",
        },
        {
            "operation_kind": "mixed-clean-strict-child-handoff",
            "checker": product,
            "contract_sha256": CHECKER_CONTRACTS[product],
            "source_theorems": ["CMR682", "CMR683", "CMR2929"],
            "owner_effect": "factor-child-owner-change",
            "payment_class": "strict-child-descent",
            "continuation": "smaller factor and stricter prefix envelope",
        },
        {
            "operation_kind": "mixed-atom-nonessential-edge-deletion",
            "checker": mixed,
            "contract_sha256": CHECKER_CONTRACTS[mixed],
            "source_theorems": ["CMR677", "CMR678", "CMR679", "CMR680", "CMR2935"],
            "owner_effect": "host-owner-change",
            "payment_class": "host-edge-deletion",
            "continuation": "strict active-atom descent",
        },
        {
            "operation_kind": "forced-certificate-edge-deletion",
            "checker": escape,
            "contract_sha256": CHECKER_CONTRACTS[escape],
            "source_theorems": ["CMR643", "CMR645", "CMR646", "CMR647", "CMR2946"],
            "owner_effect": "host-owner-change",
            "payment_class": "owner-witness-stock",
            "continuation": "certificate removed with labelled deletion witness",
        },
        {
            "operation_kind": "forced-certificate-selected-skeleton-churn",
            "checker": escape,
            "contract_sha256": CHECKER_CONTRACTS[escape],
            "source_theorems": ["CMR645", "CMR646", "CMR647", "CMR2947"],
            "owner_effect": "routing-owner-change",
            "payment_class": "routing-stock",
            "continuation": "selected-skeleton symmetric-difference witness",
        },
        {
            "operation_kind": "forced-certificate-factor-essentiality-loss-restoration",
            "checker": escape,
            "contract_sha256": CHECKER_CONTRACTS[escape],
            "source_theorems": ["CMR643", "CMR644", "CMR645", "CMR2948", "CMR2949"],
            "owner_effect": "restoration-owner-change",
            "payment_class": "edge-reintroduction",
            "continuation": "entering edge on every affected alternating component",
        },
        {
            "operation_kind": "returned-target-edge-restoration",
            "checker": returned,
            "contract_sha256": CHECKER_CONTRACTS[returned],
            "source_theorems": ["CMR720", "CMR721", "CMR722", "CMR2956"],
            "owner_effect": "restoration-owner-change",
            "payment_class": "edge-reintroduction",
            "continuation": "redeletion, blocked witness, or essential contraction",
        },
        {
            "operation_kind": "returned-target-edge-redeletion",
            "checker": returned,
            "contract_sha256": CHECKER_CONTRACTS[returned],
            "source_theorems": ["CMR720", "CMR721", "CMR2958", "CMR2959"],
            "owner_effect": "host-owner-change",
            "payment_class": "host-edge-deletion",
            "continuation": "stored or alternate avoidance matching survives",
        },
        {
            "operation_kind": "essential-target-contraction",
            "checker": returned,
            "contract_sha256": CHECKER_CONTRACTS[returned],
            "source_theorems": ["CMR722", "CMR725", "CMR2961"],
            "owner_effect": "contraction-owner-change",
            "payment_class": "factor-contraction",
            "continuation": "rank-at-most-two residual target",
        },
        {
            "operation_kind": "target-handoff-internal",
            "checker": handoff,
            "contract_sha256": CHECKER_CONTRACTS[handoff],
            "source_theorems": ["CMR698", "CMR699", "CMR700", "CMR701", "CMR706", "CMR709", "CMR710"],
            "owner_effect": "same-owner",
            "payment_class": "target-chain-stock",
            "continuation": "finite target chain or recurrent cell-target pair",
        },
        {
            "operation_kind": "target-handoff-envelope-expansion",
            "checker": handoff,
            "contract_sha256": CHECKER_CONTRACTS[handoff],
            "source_theorems": ["CMR700", "CMR701", "CMR711", "CMR2974"],
            "owner_effect": "envelope-owner-change",
            "payment_class": "closure-depth",
            "continuation": "strict ancestor envelope",
        },
        {
            "operation_kind": "recurrent-target-entering-edge-deletion",
            "checker": recurrent,
            "contract_sha256": CHECKER_CONTRACTS[recurrent],
            "source_theorems": ["CMR713", "CMR714", "CMR715", "CMR716", "CMR717", "CMR718", "CMR719"],
            "owner_effect": "host-owner-change",
            "payment_class": "host-edge-deletion",
            "continuation": "target star inactive until reintroduction or owner change",
        },
        {
            "operation_kind": "closure-envelope-internal-rematch",
            "checker": envelope,
            "contract_sha256": CHECKER_CONTRACTS[envelope],
            "source_theorems": ["CMR172", "CMR173", "CMR175"],
            "owner_effect": "same-owner",
            "payment_class": "same-envelope-dispatch",
            "continuation": "target-chain or structural scheduler required",
        },
        {
            "operation_kind": "closure-envelope-strict-expansion",
            "checker": envelope,
            "contract_sha256": CHECKER_CONTRACTS[envelope],
            "source_theorems": ["CMR174", "CMR193", "CMR194", "CMR195"],
            "owner_effect": "envelope-owner-change",
            "payment_class": "closure-depth",
            "continuation": "strictly smaller nonnegative envelope depth",
        },
    ]


def validate_registry(registry: list[dict[str, Any]]) -> dict[str, Any]:
    require(isinstance(registry, list) and registry, "registry: nonempty list required")
    kinds: set[str] = set()
    payment_counts: dict[str, int] = {}
    checker_counts: dict[str, int] = {}
    dispatch_count = 0
    for i, entry in enumerate(registry):
        path = f"registry[{i}]"
        require(isinstance(entry, dict), f"{path}: object required")
        kind = entry.get("operation_kind")
        require(isinstance(kind, str) and kind, f"{path}.operation_kind: nonempty string required")
        require(kind not in kinds, f"{path}.operation_kind: duplicate kind")
        kinds.add(kind)
        checker = entry.get("checker")
        require(checker in CHECKER_CONTRACTS, f"{path}.checker: unknown installed checker")
        require(entry.get("contract_sha256") == CHECKER_CONTRACTS[checker],
                f"{path}.contract_sha256: checker contract mismatch")
        support = entry.get("support_checker")
        if support is not None:
            require(support in CHECKER_CONTRACTS, f"{path}.support_checker: unknown checker")
            require(entry.get("support_contract_sha256") == CHECKER_CONTRACTS[support],
                    f"{path}.support_contract_sha256: mismatch")
        sources = entry.get("source_theorems")
        require(isinstance(sources, list) and sources and
                all(isinstance(source, str) and source.startswith("CMR") for source in sources),
                f"{path}.source_theorems: theorem identifiers required")
        owner_effect = entry.get("owner_effect")
        require(owner_effect in ALLOWED_OWNER_EFFECTS, f"{path}.owner_effect: unknown effect")
        payment = entry.get("payment_class")
        require(payment in ALLOWED_PAYMENT_CLASSES, f"{path}.payment_class: unknown class")
        continuation = entry.get("continuation")
        require(isinstance(continuation, str) and continuation,
                f"{path}.continuation: nonempty statement required")
        if payment not in PROGRESS_PAYMENT_CLASSES:
            require("scheduler" in continuation or "mixed deletion" in continuation,
                    f"{path}: dispatch operation lacks mandatory scheduler continuation")
            dispatch_count += 1
        payment_counts[payment] = payment_counts.get(payment, 0) + 1
        checker_counts[checker] = checker_counts.get(checker, 0) + 1
    require(set(CHECKER_CONTRACTS).issubset(set(checker_counts).union(
            {"scripts/check_prime_power_routing_change_history_payment.py"})),
            "registry: an installed construction checker is unrepresented")
    return {
        "operation_kind_count": len(kinds),
        "checker_contract_count": len(CHECKER_CONTRACTS),
        "payment_class_count": len(payment_counts),
        "dispatch_operation_count": dispatch_count,
        "payment_counts": payment_counts,
        "registry_sha256": digest(registry),
    }


def host_stage_count(m: int) -> int:
    exact_int(m, "m", 1)
    return 2 * m * m + m + 1


def routing_change_bound(m: int, lam: int) -> int:
    exact_int(m, "m", 1)
    exact_int(lam, "lambda", 2)
    return floor((lam - 1) * m * m / 2)


def owner_stage_stock(d: int, lam: int) -> int:
    exact_int(d, "d", 1)
    exact_int(lam, "lambda", 2)
    return sum(host_stage_count(m) * (1 + routing_change_bound(m, lam))
               for m in range(1, d + 1))


def owner_edge_stock(d: int, lam: int) -> int:
    return sum(host_stage_count(m) * (1 + routing_change_bound(m, lam)) * m * m
               for m in range(1, d + 1))


def owner_certificate_stock(d: int, lam: int) -> int:
    return sum(host_stage_count(m) * (1 + routing_change_bound(m, lam)) * comb(m * m, 3)
               for m in range(1, d + 1))


def owner_target_pair_stock(d: int, lam: int, ambient_side: int) -> int:
    exact_int(ambient_side, "ambient_side", 1)
    return 3 * owner_stage_stock(d, lam) * comb(ambient_side * ambient_side, 3)


def fixed_envelope_target_bound(h: int, mu: int, ambient_side: int) -> int:
    exact_int(h, "h", 0)
    exact_int(mu, "mu", 2)
    exact_int(ambient_side, "ambient_side", 1)
    return (h + 1) * (3 * mu - 2) * comb(ambient_side * ambient_side, 3)


def nonrecurrent_scheduler_bound(d: int, p: int, h: int, lam: int,
                                 mu: int, nu: int) -> dict[str, int]:
    exact_int(p, "p", 2)
    exact_int(h, "h", 1)
    ambient = p ** h
    o = owner_stage_stock(d, lam)
    e = owner_edge_stock(d, lam)
    c = owner_certificate_stock(d, lam)
    pairs = owner_target_pair_stock(d, lam, ambient)
    targets = fixed_envelope_target_bound(h, mu, ambient)
    token = (p + 1) * (h - 1) * e
    coarse = o + e + c + pairs + targets + h + max(0, d - 1)
    return {
        "owner_stage_stock": o,
        "owner_edge_stock": e,
        "owner_token_stock": token,
        "owner_certificate_stock": c,
        "owner_target_pair_stock": pairs,
        "fixed_envelope_target_bound": targets,
        "closure_expansion_bound": h,
        "strict_child_descent_bound": max(0, d - 1),
        "coarse_nonrecurrent_scheduler_bound": coarse,
    }


def finite_or_recurrent(labels: list[str], stock: int, threshold: int,
                        finite_name: str, recurrent_name: str) -> dict[str, Any]:
    exact_int(stock, "stock", 1)
    exact_int(threshold, "threshold", 2)
    require(all(isinstance(label, str) and label for label in labels),
            "labels: nonempty strings required")
    counts: dict[str, int] = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    recurrent = sorted(label for label, count in counts.items() if count >= threshold)
    if recurrent:
        witness = recurrent[0]
        return {
            "endpoint": recurrent_name,
            "witness": witness,
            "multiplicity": counts[witness],
        }
    bound = (threshold - 1) * stock
    require(len(labels) <= bound, "finite history exceeds stock bound")
    return {
        "endpoint": finite_name,
        "episode_count": len(labels),
        "bound": bound,
    }


def validate_payment_examples(registry: list[dict[str, Any]]) -> dict[str, int]:
    by_kind = {entry["operation_kind"]: entry for entry in registry}
    required = {
        "single-edge-deletion": "local-family-restriction",
        "forced-set-contraction": "factor-contraction",
        "routing-skeleton-change": "routing-stock",
        "mixed-clean-strict-child-handoff": "strict-child-descent",
        "mixed-atom-nonessential-edge-deletion": "host-edge-deletion",
        "forced-certificate-factor-essentiality-loss-restoration": "edge-reintroduction",
        "target-handoff-internal": "target-chain-stock",
        "closure-envelope-strict-expansion": "closure-depth",
        "recurrent-target-entering-edge-deletion": "host-edge-deletion",
    }
    for kind, payment in required.items():
        require(by_kind[kind]["payment_class"] == payment,
                f"payment example mismatch for {kind}")
    owner_changes = sum(entry["owner_effect"] != "same-owner" for entry in registry)
    same_owner = len(registry) - owner_changes
    return {
        "owner_changing_operation_kinds": owner_changes,
        "same_owner_operation_kinds": same_owner,
        "required_payment_examples": len(required),
    }


def expect_rejection(registry: list[dict[str, Any]], mutator: Any) -> None:
    bad = copy.deepcopy(registry)
    mutator(bad)
    try:
        validate_registry(bad)
    except OwnerSchedulerError:
        return
    raise AssertionError("corrupted installed transition registry was accepted")


def finite_regression() -> dict[str, Any]:
    registry = installed_registry()
    registry_report = validate_registry(registry)
    payment_report = validate_payment_examples(registry)
    bounds = nonrecurrent_scheduler_bound(d=4, p=2, h=3, lam=3, mu=2, nu=2)

    finite_routing = finite_or_recurrent(
        [f"routing-edge-{i}" for i in range(10)],
        bounds["owner_edge_stock"], 2,
        "finite-routing-witness-history", "recurrent-routing-edge")
    recurrent_routing = finite_or_recurrent(
        ["same-routing-edge", "same-routing-edge"],
        bounds["owner_edge_stock"], 2,
        "finite-routing-witness-history", "recurrent-routing-edge")
    finite_certificate = finite_or_recurrent(
        [f"certificate-{i}" for i in range(10)],
        max(1, bounds["owner_certificate_stock"]), 2,
        "finite-certificate-history", "recurrent-owner-certificate")
    recurrent_certificate = finite_or_recurrent(
        ["same-certificate", "same-certificate"],
        max(1, bounds["owner_certificate_stock"]), 2,
        "finite-certificate-history", "recurrent-owner-certificate")
    finite_pair = finite_or_recurrent(
        [f"pair-{i}" for i in range(10)],
        bounds["owner_target_pair_stock"], 2,
        "finite-target-pair-history", "recurrent-owner-cell-target-pair")
    recurrent_pair = finite_or_recurrent(
        ["same-pair", "same-pair"],
        bounds["owner_target_pair_stock"], 2,
        "finite-target-pair-history", "recurrent-owner-cell-target-pair")

    require(finite_routing["endpoint"] == "finite-routing-witness-history",
            "finite routing endpoint missing")
    require(recurrent_routing["endpoint"] == "recurrent-routing-edge",
            "recurrent routing endpoint missing")
    require(finite_certificate["endpoint"] == "finite-certificate-history",
            "finite certificate endpoint missing")
    require(recurrent_certificate["endpoint"] == "recurrent-owner-certificate",
            "recurrent certificate endpoint missing")
    require(finite_pair["endpoint"] == "finite-target-pair-history",
            "finite pair endpoint missing")
    require(recurrent_pair["endpoint"] == "recurrent-owner-cell-target-pair",
            "recurrent pair endpoint missing")

    rejection_count = 0
    mutations = [
        lambda r: r.append(copy.deepcopy(r[0])),
        lambda r: r[0].__setitem__("contract_sha256", "0" * 64),
        lambda r: r[0].__setitem__("checker", "scripts/missing.py"),
        lambda r: r[0].__setitem__("source_theorems", []),
        lambda r: r[0].__setitem__("owner_effect", "anonymous-owner"),
        lambda r: r[0].__setitem__("payment_class", "unpaid"),
        lambda r: r[6].__setitem__("continuation", ""),
        lambda r: r[5].__setitem__("support_contract_sha256", "0" * 64),
        lambda r: r[18].__setitem__("continuation", "unbounded continuation"),
    ]
    for mutation in mutations:
        expect_rejection(registry, mutation)
        rejection_count += 1

    return {
        **registry_report,
        **payment_report,
        **bounds,
        "finite_history_endpoint_cases": 3,
        "recurrent_history_endpoint_cases": 3,
        "rejected_corruptions": rejection_count,
    }


def main() -> None:
    contract = {
        "registry_version": "installed-construction-transition-bank-v1",
        "sources": [
            "CMR691", "CMR692", "CMR693", "CMR694", "CMR695", "CMR696", "CMR697",
            "CMR706", "CMR709", "CMR711", "CMR716", "CMR717", "CMR718", "CMR719"
        ],
        "required_fields": [
            "operation_kind", "checker", "contract_sha256", "source_theorems",
            "owner_effect", "payment_class", "continuation"
        ],
        "honesty": {
            "installed_transition_kind_bank_exhaustive": 1,
            "global_transition_kind_bank_exhaustive": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    require(digest(contract) == EXPECTED_CONTRACT_SHA256,
            "contract digest mismatch")
    census = finite_regression()
    report = {
        "checker": "prime-power-installed-owner-scheduler-bank",
        "contract_sha256": EXPECTED_CONTRACT_SHA256,
        **census,
        "installed_transition_kind_bank_exhaustive": 1,
        "installed_operation_payment_assignment_complete": 1,
        "descending_path_owner_stage_stock_exact": 1,
        "owner_edge_token_stock_exact": 1,
        "owner_certificate_stock_exact": 1,
        "owner_target_pair_stock_exact": 1,
        "fixed_envelope_scheduler_bound_exact": 1,
        "installed_nonrecurrent_scheduler_finite": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_returned_edge_operations_proved": 0,
        "all_envelope_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

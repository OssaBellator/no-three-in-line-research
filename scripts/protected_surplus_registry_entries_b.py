#!/usr/bin/env python3
"""Immutable CMR1006--CMR1093 registry entries."""
from __future__ import annotations
from typing import Any

CONTRACT_SHA256 = "5e90f91f2c8a8679bdeb3fc78ab7b0ed71c2f8d3e09de41b8ad9fc18865bddd8"

def e(kind: str, sources: list[str], owner: str, payment: str, continuation: str) -> dict[str, Any]:
    return {"operation_kind": kind, "source_theorems": sources, "owner_effect": owner,
            "payment_class": payment, "continuation": continuation,
            "contract_sha256": CONTRACT_SHA256}

ENTRIES = [
    e('loaded-old-line-majority-absorption', ['CMR1046', 'CMR1047', 'CMR1048'], 'host-owner-change', 'protected-core-growth', 'absorb all free majority-layer cells of the recorded old line'),
    e('loaded-old-line-profile-destruction', ['CMR1049'], 'same-owner', 'target-destruction-stock', 'charge the exact old line-profile triples destroyed by absorbed cells'),
    e('loaded-old-line-large-core-dispatch', ['CMR1050', 'CMR1052', 'CMR1053'], 'same-owner', 'scheduler-dispatch', 'scheduler routes zero loaded-line growth to large-core product descent'),
    e('loaded-old-line-capacity', ['CMR1051'], 'same-owner', 'history-budget', 'sum loaded-line protected absorption across both layers'),
    e('simultaneous-common-star-direct-absorption', ['CMR1054', 'CMR1055', 'CMR1056'], 'host-owner-change', 'protected-core-growth', 'absorb the complete free simultaneous outside-pair union directly'),
    e('simultaneous-common-star-large-core', ['CMR1057', 'CMR1058'], 'same-owner', 'scheduler-dispatch', 'scheduler routes zero direct-star growth to a linear protected core'),
    e('simultaneous-common-star-capacity', ['CMR1059', 'CMR1060', 'CMR1061'], 'same-owner', 'history-budget', 'direct-star growth consumes the shared two-layer protected capacity'),
    e('simultaneous-cross-star-endpoint-matching', ['CMR1062', 'CMR1063'], 'same-owner', 'support-packing', 'both endpoint sides of a simultaneous cross-star are partial matchings'),
    e('simultaneous-cross-star-hall-rematch', ['CMR1064', 'CMR1065'], 'same-owner', 'scheduler-dispatch', 'scheduler rematches the better endpoint layer against two forbidden matchings'),
    e('simultaneous-cross-star-protected-growth', ['CMR1065', 'CMR1068'], 'host-owner-change', 'protected-core-growth', 'protect one free endpoint per destroyed cross-layer arm'),
    e('simultaneous-cross-star-large-cores', ['CMR1066', 'CMR1069'], 'same-owner', 'scheduler-dispatch', 'scheduler routes zero endpoint growth to large protected cores in both layers'),
    e('simultaneous-cross-star-host-normalization', ['CMR1067'], 'same-owner', 'scheduler-dispatch', 'scheduler normalizes missing Hall edges by rollback contraction loss ancestry or improvement'),
    e('minimum-target-disjoint-packing', ['CMR1070'], 'same-owner', 'support-packing', 'extract a disjoint target bank or a small selected-cell cover'),
    e('minimum-target-small-cover-concentration', ['CMR1070', 'CMR1072', 'CMR1073'], 'same-owner', 'owner-witness-stock', 'concentrate the target cover at one rooted cell and line/star decomposition'),
    e('disjoint-target-conditioned-contraction', ['CMR1071', 'CMR1076'], 'factor-child-owner-change', 'strict-factor-contraction', 'condition on a physically disjoint target bank and contract all labelled target edges'),
    e('minimum-rooted-star-execution', ['CMR1073', 'CMR1074'], 'same-owner', 'scheduler-dispatch', 'scheduler sends a simultaneous rooted star to direct common or cross-layer absorption'),
    e('minimum-loaded-line-execution', ['CMR1075', 'CMR1077'], 'same-owner', 'scheduler-dispatch', 'scheduler sends a loaded minimum target line to absorption or product descent'),
    e('disjoint-target-majority-layer-representatives', ['CMR1078', 'CMR1079'], 'same-owner', 'owner-witness-stock', 'choose a compatible representative matching from one majority layer'),
    e('disjoint-target-degree-two-hall-escape', ['CMR1080', 'CMR1081'], 'same-owner', 'scheduler-dispatch', 'scheduler rematches one layer and destroys at least half the disjoint targets'),
    e('disjoint-target-minimum-response', ['CMR1082', 'CMR1083', 'CMR1084', 'CMR1085'], 'same-owner', 'scheduler-dispatch', 'scheduler chooses improvement same-value handoff robust surplus or normalized structural exit'),
    e('owner-stage-protected-capacity', ['CMR1086'], 'same-owner', 'protected-core-growth', 'each owner-routing stage has at most two factor sides of fresh protected edges'),
    e('strict-path-protected-capacity', ['CMR1087'], 'same-owner', 'history-budget', 'aggregate protected growth over host stages and routing epochs on one descent path'),
    e('unit-wall-tree-protected-capacity', ['CMR1088'], 'same-owner', 'history-budget', 'aggregate protected growth over every node of one unit-wall factor tree'),
    e('closure-branch-protected-capacity', ['CMR1089'], 'same-owner', 'history-budget', 'aggregate protected growth over all envelope epochs'),
    e('global-large-growth-episode-bound', ['CMR1090', 'CMR1091'], 'same-owner', 'history-budget', 'bound all positive protected-growth episodes by the global owner-labelled capacity'),
    e('global-zero-growth-protected-dispatch', ['CMR1092', 'CMR1093'], 'same-owner', 'scheduler-dispatch', 'scheduler routes post-capacity episodes to core line recurrence loss routing or envelope progress'),
]

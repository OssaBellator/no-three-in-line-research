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
    e('robust-new-triple-entry-rank-partition', ['CMR1006', 'CMR1007'], 'same-owner', 'owner-witness-stock', 'partition every new triple by physical entry rank and select the rank-one or higher-rank branch'),
    e('rank-one-entering-cell-concentration', ['CMR1008'], 'same-owner', 'owner-witness-stock', 'one entering physical cell carries the averaged rank-one new-triple load'),
    e('rank-one-old-line-load-certificate', ['CMR1009', 'CMR1010'], 'same-owner', 'scheduler-dispatch', 'scheduler routes a loaded old line to target-line absorption'),
    e('rank-one-secant-star-extraction', ['CMR1009', 'CMR1010'], 'same-owner', 'support-packing', 'extract a cell-disjoint simultaneous secant-star bank through one entering cell'),
    e('higher-rank-entering-pair-concentration', ['CMR1011', 'CMR1012'], 'same-owner', 'owner-witness-stock', 'one entering physical pair carries many new triples on one nonaxis line'),
    e('higher-rank-loaded-line-certificate', ['CMR1011', 'CMR1012', 'CMR1013'], 'same-owner', 'scheduler-dispatch', 'scheduler routes the cubic loaded-line certificate to majority-layer absorption'),
    e('secant-star-layer-pattern-partition', ['CMR1014', 'CMR1015'], 'same-owner', 'branch-cover-dispatch', 'partition simultaneous star arms into common-layer or cross-layer subbanks'),
    e('common-layer-outside-pair-bank', ['CMR1016'], 'same-owner', 'support-packing', 'the simultaneous common-layer outside union is one compatible partial matching'),
    e('common-layer-protected-star-execution', ['CMR1017', 'CMR1031'], 'same-owner', 'protected-core-growth', 'absorb free outside pairs or certify a large protected core'),
    e('cross-layer-rooted-pair-bank', ['CMR1018'], 'same-owner', 'support-packing', 'select one rooted compatible paid pair from every cross-layer arm'),
    e('cross-layer-rooted-line-clean-cylinder', ['CMR1019', 'CMR1020'], 'same-owner', 'scheduler-dispatch', 'scheduler combines the rooted cylinder with an explicit opposite-layer response'),
    e('loaded-line-majority-layer-selection', ['CMR1022', 'CMR1023'], 'same-owner', 'owner-witness-stock', 'select a majority permutation layer whose loaded-line cells form a partial matching'),
    e('loaded-line-free-cell-extraction', ['CMR1024'], 'same-owner', 'protected-core-growth', 'remove protected-touching cells and retain a large free majority-line matching'),
    e('entering-pair-majority-line-absorption', ['CMR1025', 'CMR1026'], 'host-owner-change', 'protected-core-growth', 'extend the protected matching and restrict to a cylinder avoiding all free loaded-line cells'),
    e('entering-pair-large-core-certificate', ['CMR1027', 'CMR1029'], 'same-owner', 'scheduler-dispatch', 'scheduler sends zero line growth to the large protected-core descent'),
    e('protected-line-absorption-capacity', ['CMR1028'], 'same-owner', 'history-budget', 'monotone majority-line absorption consumes finite protected matching capacity'),
    e('robust-episode-rank-one-scale', ['CMR1030', 'CMR1031'], 'same-owner', 'owner-witness-stock', 'compute the old-line or polarized secant-star execution scale'),
    e('robust-episode-higher-rank-scale', ['CMR1032', 'CMR1033'], 'same-owner', 'owner-witness-stock', 'compute the entering-pair line load growth or large-core scale'),
    e('two-layer-protected-growth-capacity', ['CMR1034', 'CMR1035'], 'same-owner', 'history-budget', 'sum fresh protected growth across both layer matchings'),
    e('zero-growth-robust-episode-dispatch', ['CMR1036', 'CMR1037'], 'same-owner', 'scheduler-dispatch', 'scheduler routes zero growth to loaded line wall large core or cross-layer payment'),
    e('protected-minimum-skeleton-class-selection', ['CMR1038'], 'same-owner', 'local-family-restriction', 'restrict to the unique cross-skeleton class containing the selected minimum'),
    e('protected-skeleton-exact-product', ['CMR1039'], 'factor-child-owner-change', 'factor-product-dispatch', 'factor the selected skeleton class into fixed skeleton and protected/free matching factors'),
    e('protected-skeleton-coupling-normalization', ['CMR1040'], 'same-owner', 'history-budget', 'delete or contract low-rank coupling atoms on the selected minimum face'),
    e('large-core-coordinate-factor-descent', ['CMR1041'], 'factor-child-owner-change', 'strict-child-descent', 'freeze all but one product coordinate and descend the selected minimum'),
    e('large-core-sparse-interface-stock', ['CMR1042'], 'same-owner', 'owner-witness-stock', 'bound selected skeleton and mixed-atom stocks by the free codimension'),
    e('large-core-pure-factor-recursion', ['CMR1043', 'CMR1044', 'CMR1045'], 'factor-child-owner-change', 'strict-child-descent', 'continue through essential-core contraction and strict prefix routing'),
]

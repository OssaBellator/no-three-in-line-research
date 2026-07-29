#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter, defaultdict
from itertools import combinations
import random

SEED = 41
SYSTEMS = 2500
KINDS = ("anchor", "quotient", "carry", "bda")
REQUIRED = {
    "anchor": {"endpoint_disjoint_star", "an_seed_fields"},
    "quotient": {"ratio_set", "small_quotient_bound", "paid_weight"},
    "carry": {"signature", "new_or_repeated", "owner_route"},
    "bda": {"denominator", "determinant_occurrence", "chamber"},
}


def falling(t, r):
    out = 1
    for i in range(r):
        out *= t - i
    return out


def unique_certificates(rng, rank, count, side=20):
    seen = set()
    while len(seen) < count:
        rows = tuple(sorted(rng.sample(range(side), rank)))
        cols = tuple(rng.sample(range(side), rank))
        seen.add(tuple(zip(rows, cols)))
    certs = []
    for occurrence, anchors in enumerate(sorted(seen)):
        label = (
            rng.randrange(2), rng.randrange(3), rng.randrange(4),
            rng.randrange(3), rng.randrange(5),
        )
        certs.append({
            "occurrence": occurrence,
            "anchors": anchors,
            "line": ("L", occurrence % 7),
            "label": label,
            "weight": rng.randint(1, 5),
        })
    return certs


def incidence_identities(certs, rank):
    degree = Counter()
    pair_degree = Counter()
    for cert in certs:
        for anchor in cert["anchors"]:
            degree[anchor] += 1
        for pair in combinations(cert["anchors"], 2):
            pair_degree[tuple(sorted(pair))] += 1
    assert sum(degree.values()) == rank * len(certs)
    assert sum(pair_degree.values()) == (rank * (rank - 1) // 2) * len(certs)
    return degree, pair_degree


def anchor_extract(certs, delta):
    degree, _ = incidence_identities(certs, 3)
    anchor = max(degree, key=lambda value: (degree[value], value))
    family = [cert for cert in certs if anchor in cert["anchors"]]
    codegree = Counter()
    edges = []
    for cert in family:
        other = tuple(value for value in cert["anchors"] if value != anchor)
        assert len(other) == 2
        edges.append((other, cert))
        codegree.update(other)
    heavy = [value for value, count in codegree.items() if count > delta]
    if heavy:
        return "pair", anchor, min(heavy), len(family)
    chosen = []
    used = set()
    for edge, cert in edges:
        if edge[0] not in used and edge[1] not in used:
            chosen.append(cert)
            used.update(edge)
    assert len(chosen) * (2 * delta - 1) >= len(family)
    return "star", anchor, tuple(cert["occurrence"] for cert in chosen), len(family)


def compile_continuation(kind, record):
    missing = sorted(REQUIRED[kind] - set(record))
    if missing:
        return "missing", kind, missing[0]
    if kind == "anchor":
        return "install-seed", len(record["endpoint_disjoint_star"])
    if kind == "quotient":
        return "paid-ratio-bank", record["small_quotient_bound"]
    if kind == "carry":
        route = "new-signature" if record["new_or_repeated"] == "new" else "repeated-signature"
        return route, record["signature"]
    return "bda-chamber", record["denominator"]


def run():
    rng = random.Random(SEED)
    stats = {
        "systems": SYSTEMS,
        "certificate_occurrences": 0,
        "heavy_rank_checks": 0,
        "heavy_label_checks": 0,
        "incidence_identity_checks": 0,
        "pair_concentrations": 0,
        "endpoint_disjoint_stars": 0,
        "certified_continuations": 0,
        "missing_semantic_certificates": 0,
        "anchor_continuations": 0,
        "quotient_continuations": 0,
        "carry_continuations": 0,
        "bda_continuations": 0,
        "rich_line_multiplicity_occurrences": 0,
    }

    for system in range(SYSTEMS):
        t = rng.randint(7, 12)
        desired = 1 + system % 3
        norms = [0, 0.04, 0.04, 0.04]
        norms[desired] = 0.35
        counts = [0] + [max(1, int(norms[r] * falling(t, r))) for r in (1, 2, 3)]
        normalized = [0] + [counts[r] / falling(t, r) for r in (1, 2, 3)]
        total = 128 * sum(normalized[1:])
        gap = rng.uniform(0.2, 0.95) * total
        rank = max((1, 2, 3), key=lambda r: normalized[r])
        assert normalized[rank] >= gap / 384 - 1e-12
        stats["heavy_rank_checks"] += 1

        certs = unique_certificates(rng, rank, counts[rank])
        stats["certificate_occurrences"] += len(certs)
        by_label = defaultdict(list)
        for cert in certs:
            by_label[cert["label"]].append(cert)
        label, family = max(by_label.items(), key=lambda item: (len(item[1]), item[0]))
        label_count = len(by_label)
        assert len(family) / falling(t, rank) >= gap / (384 * label_count) - 1e-12
        stats["heavy_label_checks"] += 1

        incidence_identities(certs, rank)
        stats["incidence_identity_checks"] += 1
        line_counts = Counter(cert["line"] for cert in certs)
        stats["rich_line_multiplicity_occurrences"] += sum(
            count for count in line_counts.values() if count > 1
        )

        if rank == 3:
            route = anchor_extract(certs, 1 if system % 2 == 0 else 20)
            if route[0] == "pair":
                stats["pair_concentrations"] += 1
            else:
                stats["endpoint_disjoint_stars"] += 1

        kind = KINDS[system % 4]
        record = {
            "family_occurrences": [cert["occurrence"] for cert in family],
            "rank": rank,
            "label": label,
            "normalized_weight": len(family) / falling(t, rank),
        }
        if system < 1000:
            if kind == "anchor":
                record.update(
                    endpoint_disjoint_star=record["family_occurrences"][:max(1, min(5, len(family)))],
                    an_seed_fields={"t": t, "label": label},
                )
            elif kind == "quotient":
                record.update(
                    ratio_set=list(range(max(2, min(6, len(family))))),
                    small_quotient_bound=2 * len(family),
                    paid_weight=sum(cert["weight"] for cert in family),
                )
            elif kind == "carry":
                record.update(
                    signature=("carry",) + label,
                    new_or_repeated="new" if system % 8 < 4 else "repeated",
                    owner_route="PAID",
                )
            else:
                record.update(
                    denominator=rng.randint(2, 2 * (t - 1) ** 2),
                    determinant_occurrence=("det", system),
                    chamber=("perfect", label),
                )
            result = compile_continuation(kind, record)
            assert result[0] != "missing"
            stats["certified_continuations"] += 1
            stats[kind + "_continuations"] += 1
        else:
            required = sorted(REQUIRED[kind])
            omitted = required[(system - 1000) % len(required)]
            for field in required:
                if field == omitted:
                    continue
                values = {
                    "endpoint_disjoint_star": [0],
                    "an_seed_fields": {"t": t},
                    "ratio_set": [1, 2],
                    "small_quotient_bound": 4,
                    "paid_weight": 1,
                    "signature": ("carry", system),
                    "new_or_repeated": "new",
                    "owner_route": "PAID",
                    "denominator": 2,
                    "determinant_occurrence": ("det", system),
                    "chamber": ("perfect", system),
                }
                record[field] = values[field]
            result = compile_continuation(kind, record)
            assert result == ("missing", kind, omitted)
            stats["missing_semantic_certificates"] += 1

    return stats


if __name__ == "__main__":
    output = run()
    print("AC AC1 physical certificate compiler audit")
    for key, value in output.items():
        print(f"{key}: {value}")

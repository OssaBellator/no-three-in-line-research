#!/usr/bin/env python3
"""Finite diagnostic for fixed-centre source degree savings.

Enumerates anchored compatible pairs and collinear partial-permutation triples.
This is a finite regression check, not an asymptotic proof.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Sequence


def collinear(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def divisor_count(n: int) -> int:
    if n <= 0:
        return 0
    total = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            total += 1 if d * d == n else 2
        d += 1
    return total


def divisor_max(limit: int) -> int:
    return max((divisor_count(n) for n in range(1, max(1, limit) + 1)), default=1)


def has_directed_cycle(arcs: Sequence[tuple[int, int]]) -> bool:
    nxt = {u: v for u, v in arcs}
    for start in nxt:
        seen: set[int] = set()
        cur = start
        while cur in nxt and cur not in seen:
            seen.add(cur)
            cur = nxt[cur]
        if cur in seen:
            return True
    return False


def enumerate_anchored_pairs(
    n: int,
    centre: int,
    xs: Sequence[int],
    ys: Sequence[int],
    anchors: Sequence[tuple[int, int]],
) -> int:
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    count = 0
    for (i, j), (k, l) in itertools.combinations(arcs, 2):
        if i == k or j == l:
            continue
        support = {i, j, k, l}
        if len(support) != 4 or centre not in support:
            continue
        p = (xs[i], ys[j])
        q = (xs[k], ys[l])
        if any(collinear(z, p, q) for z in anchors):
            count += 1
    return count


def enumerate_inserted_triples(
    n: int,
    centre: int,
    xs: Sequence[int],
    ys: Sequence[int],
) -> Counter[int]:
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    counts: Counter[int] = Counter()
    for triple in itertools.combinations(arcs, 3):
        tails = {u for u, _ in triple}
        heads = {v for _, v in triple}
        if len(tails) != 3 or len(heads) != 3:
            continue
        support = set(tails) | set(heads)
        h = len(support)
        if h not in (4, 5, 6) or centre not in support:
            continue
        if has_directed_cycle(triple):
            continue
        points = [(xs[u], ys[v]) for u, v in triple]
        if collinear(points[0], points[1], points[2]):
            counts[h] += 1
    return counts


def unary_degrees(n: int, arcs: Sequence[Sequence[int]]) -> tuple[int, list[int], list[int]]:
    out_deg = [0] * n
    in_deg = [0] * n
    seen: set[tuple[int, int]] = set()
    for raw in arcs:
        if len(raw) != 2:
            raise ValueError(f"invalid unary arc: {raw}")
        u, v = map(int, raw)
        if not (0 <= u < n and 0 <= v < n and u != v):
            raise ValueError(f"invalid unary arc: {raw}")
        if (u, v) in seen:
            continue
        seen.add((u, v))
        out_deg[u] += 1
        in_deg[v] += 1
    return len(seen), out_deg, in_deg


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()

    data = json.loads(args.instance.read_text())
    n = int(data["n"])
    centre = int(data["centre"])
    b = int(data["block_size"])
    delta = float(data["clean_density"])
    target = int(data["target_bank"])
    xs = list(map(int, data["x_coordinates"]))
    ys = list(map(int, data["y_coordinates"]))
    anchors = [tuple(map(int, z)) for z in data.get("anchors", [])]
    unary_arcs = data.get("unary_forbidden_arcs", [])
    constant = float(data.get("diagnostic_bound_constant", 100.0))
    rho_constant = float(data.get("rho_constant", 0.25))
    k = float(data.get("cylinder_constant", 1.0))

    if len(xs) != n or len(ys) != n:
        raise ValueError("coordinate arrays must have length n")
    if len(set(xs)) != n or len(set(ys)) != n:
        raise ValueError("old columns and rows must be distinct")
    if not (0 <= centre < n):
        raise ValueError("centre out of range")
    if not (5 <= b <= n):
        raise ValueError("require 5 <= block_size <= n")
    if not (0 < delta <= 1):
        raise ValueError("clean_density must lie in (0,1]")

    dp = enumerate_anchored_pairs(n, centre, xs, ys, anchors)
    triple = enumerate_inserted_triples(n, centre, xs, ys)
    d4, d5, d6 = triple[4], triple[5], triple[6]

    m_coord = max(max(map(abs, xs), default=0), max(map(abs, ys), default=0), 1) + 1
    dm = divisor_max(m_coord * m_coord)
    scale_p = len(anchors) * dm * n + n * n
    scales = {4: n**2, 5: n**3, 6: n**4}

    if dp > constant * max(1, scale_p):
        raise AssertionError("anchored-pair diagnostic bound failed")
    for h, value in ((4, d4), (5, d5), (6, d6)):
        if value > constant * scales[h]:
            raise AssertionError(f"rank-{h} triple diagnostic bound failed")

    high_load = (
        (k**2) * dp * b / (n**3)
        + (k**3) * (
            d4 / (n**3)
            + d5 * b / (n**4)
            + d6 * (b**2) / (n**5)
        )
    )

    u2, out_deg, in_deg = unary_degrees(n, unary_arcs)
    marked_degree = out_deg[centre] + in_deg[centre]
    marked_threshold = rho_constant * delta * n
    global_threshold = rho_constant * delta * (n**2) / b

    if marked_degree >= marked_threshold:
        orientation = "outgoing" if out_deg[centre] >= in_deg[centre] else "incoming"
        star_size = max(out_deg[centre], in_deg[centre])
        outcome = "marked_centre_unary_star"
    elif u2 >= global_threshold:
        best_out = max(range(n), key=out_deg.__getitem__)
        best_in = max(range(n), key=in_deg.__getitem__)
        if out_deg[best_out] >= in_deg[best_in]:
            orientation = "outgoing"
            star_size = out_deg[best_out]
            star_vertex = best_out
        else:
            orientation = "incoming"
            star_size = in_deg[best_in]
            star_vertex = best_in
        outcome = "global_unary_resource_star"
    else:
        orientation = None
        star_size = 0
        star_vertex = None
        outcome = "residual_source_light"

    result = {
        "n": n,
        "centre": centre,
        "block_size": b,
        "clean_density": delta,
        "anchored_pair_degree": dp,
        "anchored_pair_scale": scale_p,
        "rank4_triple_degree": d4,
        "rank5_triple_degree": d5,
        "rank6_triple_degree": d6,
        "rank4_scale": scales[4],
        "rank5_scale": scales[5],
        "rank6_scale": scales[6],
        "normalised_high_support_load": high_load,
        "unary_total": u2,
        "marked_unary_degree": marked_degree,
        "marked_threshold": marked_threshold,
        "global_threshold": global_threshold,
        "target_bank": target,
        "outcome": outcome,
        "orientation": orientation,
        "star_size": star_size,
    }
    if outcome == "global_unary_resource_star":
        result["star_vertex"] = star_vertex

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

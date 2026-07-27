#!/usr/bin/env python3
"""Finite audit for GC2el--GC2ep."""

from collections import defaultdict
import random

SEED = 20260727


def greedy_edge_coloring(edges, endpoint_degree):
    colours = {}
    by_vertex = defaultdict(list)
    for edge in edges:
        by_vertex[edge[0]].append(edge[3])
        by_vertex[edge[1]].append(edge[3])

    edge_by_id = {edge[3]: edge for edge in edges}
    order = sorted(
        edges,
        key=lambda edge: endpoint_degree[edge[0]] + endpoint_degree[edge[1]],
        reverse=True,
    )
    for edge in order:
        used = set()
        for vertex in edge[:2]:
            for other_id in by_vertex[vertex]:
                if other_id in colours:
                    used.add(colours[other_id])
        colour = 0
        while colour in used:
            colour += 1
        colours[edge[3]] = colour
    return colours, edge_by_id


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(15000):
        n = rng.randint(3, 25)
        cells = list(range(n * n))
        certificate_count = rng.randint(
            1,
            min(100, len(cells) * (len(cells) - 1) // 2),
        )
        certificates = []
        for certificate_id in range(certificate_count):
            triple = tuple(sorted(rng.sample(cells, 3)))
            weight = rng.randint(1, 10000)
            certificates.append((triple, weight, certificate_id))

        birth_weight = sum(weight for _, weight, _ in certificates)
        survivors = []
        paid_weight = 0
        for triple, weight, certificate_id in certificates:
            if rng.random() < 0.5:
                survivors.append((triple, float(weight), certificate_id))
            else:
                paid_weight += weight

        surviving_weight = sum(weight for _, weight, _ in survivors)
        assert surviving_weight + paid_weight == birth_weight

        if paid_weight * 2 >= birth_weight:
            counts["payment_branches"] += 1
            continue

        incidence = defaultdict(float)
        for triple, weight, _ in survivors:
            for cell in triple:
                incidence[cell] += weight

        anchor = max(incidence, key=incidence.get)
        anchor_weight = incidence[anchor]
        assert anchor_weight * (n * n) + 1e-7 >= 3 * surviving_weight
        assert anchor_weight + 1e-7 >= 3 * birth_weight / (2 * n * n)

        link_edges = []
        degree = defaultdict(int)
        edge_id = 0
        for triple, weight, _ in survivors:
            if anchor not in triple:
                continue
            others = [cell for cell in triple if cell != anchor]
            assert len(others) == 2
            first, second = others
            link_edges.append((first, second, weight, edge_id))
            degree[first] += 1
            degree[second] += 1
            edge_id += 1

        link_weight = sum(edge[2] for edge in link_edges)
        assert abs(link_weight - anchor_weight) <= max(
            1e-7,
            1e-12 * anchor_weight,
        )

        delta = rng.randint(1, max(1, max(degree.values(), default=1)))
        if max(degree.values(), default=0) > delta:
            counts["pair_multiplicity_branches"] += 1
            assert any(value > delta for value in degree.values())
        else:
            colours, edge_by_id = greedy_edge_coloring(link_edges, degree)
            used_count = max(colours.values(), default=-1) + 1
            assert used_count <= 2 * delta - 1

            totals = defaultdict(float)
            for edge in link_edges:
                totals[colours[edge[3]]] += edge[2]
            best = max(totals, key=totals.get)
            selected = [
                edge_by_id[current_id]
                for current_id, colour in colours.items()
                if colour == best
            ]
            selected_weight = totals[best]
            assert selected_weight * (2 * delta - 1) + 1e-7 >= anchor_weight

            used_endpoints = set()
            for first, second, _, _ in selected:
                assert first not in used_endpoints
                assert second not in used_endpoints
                used_endpoints.add(first)
                used_endpoints.add(second)

            target = 3 * birth_weight / (
                2 * n * n * (2 * delta - 1)
            )
            assert selected_weight + 1e-7 >= target
            counts["star_branches"] += 1
            counts["selected_star_edges"] += len(selected)

        counts["survival_systems"] += 1
        counts["surviving_certificates"] += len(survivors)

    print("GC surviving exact-certificate anchor-star audit passed")
    keys = [
        "payment_branches",
        "survival_systems",
        "surviving_certificates",
        "pair_multiplicity_branches",
        "star_branches",
        "selected_star_edges",
    ]
    for key in keys:
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()

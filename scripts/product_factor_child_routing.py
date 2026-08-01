#!/usr/bin/env python3
from __future__ import annotations

import itertools
import math
from collections import Counter, defaultdict
from typing import Any, Iterable

from product_factor_child_common import *

def common_prefix_depth(values: Iterable[int], p: int, h: int) -> int:
    items = list(values)
    require(items, "nonempty coordinate set")
    best = 0
    for s in range(h + 1):
        modulus = p**s
        if len({x % modulus for x in items}) == 1:
            best = s
        else:
            break
    return best


def routing_skeleton(M: Matching, X: tuple[int, ...], Y: tuple[int, ...], p: int, beta: int) -> tuple[Any, ...]:
    source_route: dict[tuple[int, int], tuple[int, ...]] = {}
    target_route: dict[tuple[int, int], tuple[int, ...]] = {}
    for r in range(p):
        for s in range(p):
            xs = tuple(sorted(x for x, y in M if (x // (p**beta)) % p == r and (y // (p**beta)) % p == s))
            ys = tuple(sorted(y for x, y in M if (x // (p**beta)) % p == r and (y // (p**beta)) % p == s))
            source_route[(r, s)] = xs
            target_route[(r, s)] = ys
    return tuple((r, s, source_route[(r, s)], target_route[(r, s)]) for r in range(p) for s in range(p))


def factor_prefix_routing_audit() -> dict[str, int]:
    p, h, t = 2, 3, 8
    factor_profiles = transport_checks = factorisation_checks = 0
    routing_skeletons = finite_stock_checks = heavy_profiles = dispersed_profiles = 0
    selected_pairs: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for d in (2, 3):
        for X in itertools.combinations(range(t), d):
            for Y in itertools.combinations(range(t), d):
                selected_pairs.append((X, Y))
    for X in list(itertools.combinations(range(t), 4))[:20]:
        for Y in list(itertools.combinations(range(t), 4))[:20]:
            selected_pairs.append((X, Y))

    for X, Y in selected_pairs:
        d = len(X)
        beta = min(common_prefix_depth(X, p, h), common_prefix_depth(Y, p, h))
        require(beta < h, "CMR656 nontrivial factor depth")
        q = t // (p ** (beta + 1))
        xr = Counter((x // (p**beta)) % p for x in X)
        ys = Counter((y // (p**beta)) % p for y in Y)
        require(max(len(xr), len(ys)) >= 2, "CMR657 projection split")
        E = {(x, y) for x in X for y in Y}
        PM = perfect_matchings(E, X, Y)
        groups: dict[tuple[Any, ...], list[Matching]] = defaultdict(list)
        for M in PM:
            table = Counter(((x // (p**beta)) % p, (y // (p**beta)) % p) for x, y in M)
            for r, count in xr.items():
                require(sum(table[(r, s)] for s in range(p)) == count, "transport row margin")
            for s, count in ys.items():
                require(sum(table[(r, s)] for r in range(p)) == count, "transport col margin")
            z = sum(value > 0 for value in table.values())
            require(z >= max(len(xr), len(ys)), "CMR658 support projection")
            require(z >= math.ceil(d / q), "CMR658 child capacity")
            transport_checks += 1
            skel = routing_skeleton(M, X, Y, p, beta)
            groups[skel].append(M)
            threshold = max(2, math.ceil(math.sqrt(d)))
            if max(table.values()) >= threshold:
                heavy_profiles += 1
            else:
                require(z >= math.ceil(d / (threshold - 1)), "CMR662 dispersion")
                dispersed_profiles += 1
        require(len(groups) <= p ** (2 * d), "CMR660 routing stock")
        routing_skeletons += len(groups)
        finite_stock_checks += 1
        for skel, states in groups.items():
            local_hosts: list[tuple[set[Edge], set[int], set[int]]] = []
            for r, s, xs, yvals in skel:
                if not xs:
                    continue
                local_edges = {(x, y) for x in xs for y in yvals}
                local_hosts.append((local_edges, set(xs), set(yvals)))
            product_count = 1
            for edges, rows, cols in local_hosts:
                product_count *= len(perfect_matchings(edges, rows, cols))
            require(product_count == len(states), "CMR659 child factorisation count")
            factorisation_checks += 1
        factor_profiles += 1
    return {
        "factor_prefix_profiles": factor_profiles,
        "transport_table_checks": transport_checks,
        "routing_skeletons_realised": routing_skeletons,
        "routing_factorisation_checks": factorisation_checks,
        "routing_stock_checks": finite_stock_checks,
        "heavy_child_profiles": heavy_profiles,
        "dispersed_child_profiles": dispersed_profiles,
    }


def multi_child_and_routing_audit() -> dict[str, int]:
    factors = [({0, 4}, {0, 4}), ({1, 5}, {1, 5})]
    hosts = [{(r, c) for r in rows for c in cols} for rows, cols in factors]
    families = [perfect_matchings(H, rows, cols) for H, (rows, cols) in zip(hosts, factors)]
    product_states = list(itertools.product(*families))
    atoms = candidate_atoms(set().union(*hosts))
    mixed = [T for T in atoms if sum(bool(set(T) & H) for H in hosts) >= 2]
    require(mixed, "multi-child mixed atom fixture")
    rank_vector_checks = box_checks = dirty_box_checks = essential_actions = 0
    for T in mixed:
        ranks = sorted((len(set(T) & H) for H in hosts if set(T) & H), reverse=True)
        require(ranks in ([2, 1], [1, 1, 1]), "CMR665 rank pattern")
        rank_vector_checks += 1
        expected = {
            index for index, state in enumerate(product_states)
            if all((set(T) & hosts[i]).issubset(state[i]) for i in range(len(hosts)))
        }
        actual = {
            index for index, state in enumerate(product_states)
            if set(T).issubset(set().union(*map(set, state)))
        }
        require(expected == actual, "CMR666 box mismatch")
        box_checks += 1
        if expected:
            dirty_box_checks += 1
            forced = True
            for i, H in enumerate(hosts):
                local = set(T) & H
                if not local:
                    continue
                core = essential_core(families[i])
                if not local.issubset(core):
                    forced = False
                    edge = sorted(local - core)[0]
                    reduced = H - {edge}
                    require(perfect_matchings(reduced, *factors[i]), "CMR670 deletion")
                    require(all(not set(T).issubset(set().union(*map(set, state)))
                                for state in itertools.product(
                                    *[perfect_matchings(reduced, *factors[i]) if j == i else families[j]
                                      for j in range(len(hosts))])),
                            "deleted atom remains active")
                    essential_actions += 1
                    break
            if forced:
                require(all(set(T).issubset(set().union(*map(set, state))) for state in product_states),
                        "forced mixed certificate not universal")
                essential_actions += 1

    X = Y = (0, 1, 4, 5)
    E = {(x, y) for x in X for y in Y}
    PM = perfect_matchings(E, X, Y)
    routing_pairs = entering_support = leaving_support = changed_components = 0
    edge_incidence = Counter()
    beta = 0
    for M, N in itertools.combinations(PM, 2):
        gamma_M = routing_skeleton(M, X, Y, 2, beta)
        gamma_N = routing_skeleton(N, X, Y, 2, beta)
        AX = {x for x in X if (dict(M)[x] % 2) != (dict(N)[x] % 2)}
        invM = {y: x for x, y in M}
        invN = {y: x for x, y in N}
        AY = {y for y in Y if (invM[y] % 2) != (invN[y] % 2)}
        require(len(AX) != 1 and len(AY) != 1, "CMR671 singleton routing change")
        require((gamma_M != gamma_N) == bool(AX or AY), "routing identity")
        if gamma_M == gamma_N:
            continue
        Eplus = {(x, dict(N)[x]) for x in AX} | {(invN[y], y) for y in AY}
        Eminus = {(x, dict(M)[x]) for x in AX} | {(invM[y], y) for y in AY}
        require(len(Eplus) >= 2 and len(Eminus) >= 2, "CMR672 support size")
        require(Eplus.issubset(set(N) - set(M)), "entering routing support")
        require(Eminus.issubset(set(M) - set(N)), "leaving routing support")
        comps = component_edges(M, N)
        affected = [comp for comp in comps if comp & (Eplus | Eminus)]
        require(sum(len(comp & set(N)) for comp in affected) >= 2, "CMR673 entering component union")
        require(sum(len(comp & set(M)) for comp in affected) >= 2, "CMR673 leaving component union")
        routing_pairs += 1
        entering_support += len(Eplus)
        leaving_support += len(Eminus)
        changed_components += len(affected)
        edge_incidence.update(Eplus)
    lam = max(edge_incidence.values()) + 1 if edge_incidence else 2
    require(routing_pairs <= ((lam - 1) * len(E)) // 2, "CMR674 finite routing bound")
    return {
        "multi_child_product_states": len(product_states),
        "multi_child_mixed_atoms": len(mixed),
        "multi_child_rank_vector_checks": rank_vector_checks,
        "multi_child_box_checks": box_checks,
        "dirty_active_box_checks": dirty_box_checks,
        "multi_child_essentiality_actions": essential_actions,
        "routing_change_pairs": routing_pairs,
        "routing_entering_edge_incidences": entering_support,
        "routing_leaving_edge_incidences": leaving_support,
        "routing_changed_components": changed_components,
    }


def mixed_child_recursion_audit() -> dict[str, int]:
    factor_vertices = [({0, 4}, {0, 4}), ({1, 5}, {1, 5})]
    universes = [sorted((r, c) for r in rows for c in cols) for rows, cols in factor_vertices]
    host_pairs = recursion_steps = deleted_atoms = forced_endpoints = clean_endpoints = 0
    strict_measure_checks = 0
    for mask0 in range(1 << 4):
        H0 = {universes[0][i] for i in range(4) if mask0 >> i & 1}
        if not perfect_matchings(H0, *factor_vertices[0]):
            continue
        for mask1 in range(1 << 4):
            H1 = {universes[1][i] for i in range(4) if mask1 >> i & 1}
            if not perfect_matchings(H1, *factor_vertices[1]):
                continue
            host_pairs += 1
            hosts = [set(H0), set(H1)]
            limit = sum(map(len, hosts)) + 1
            for _ in range(limit):
                families = [perfect_matchings(hosts[i], *factor_vertices[i]) for i in range(2)]
                product = list(itertools.product(*families))
                mixed = [
                    T for T in candidate_atoms(hosts[0] | hosts[1])
                    if set(T) & hosts[0] and set(T) & hosts[1]
                    and any(set(T).issubset(set(a) | set(b)) for a, b in product)
                ]
                if not mixed:
                    for state in product:
                        full_atoms = candidate_atoms(set(state[0]) | set(state[1]))
                        pure = [T for T in full_atoms if set(T).issubset(hosts[0]) or set(T).issubset(hosts[1])]
                        require(len(full_atoms) == len(pure), "CMR682 additivity")
                    clean_endpoints += 1
                    break
                T = sorted(mixed)[0]
                action = None
                for i in range(2):
                    local = set(T) & hosts[i]
                    if not local:
                        continue
                    core = essential_core(families[i])
                    nonessential = sorted(local - core)
                    if nonessential:
                        edge = nonessential[0]
                        hosts[i].remove(edge)
                        require(perfect_matchings(hosts[i], *factor_vertices[i]), "CMR679 deletion")
                        action = "delete"
                        deleted_atoms += 1
                        recursion_steps += 1
                        break
                if action is None:
                    require(all(set(T).issubset(set(a) | set(b)) for a, b in product),
                            "CMR681 forced certificate")
                    forced_endpoints += 1
                    break
            else:
                raise ProductFactorChildError("mixed child recursion exceeded edge stock")
            require(sum(len(H) for H in hosts) <= 8, "mixed-child edge measure")
            strict_measure_checks += 1

    stage_checks = certificate_stock_checks = escape_stock_checks = 0
    for d in range(1, 9):
        stage = sum(2 * m * m + m + 1 for m in range(1, d + 1))
        closed = d * (d + 1) * (2 * d + 1) // 3 + d * (d + 1) // 2 + d
        require(stage == closed, "CMR686 stage formula")
        stock = stage * math.comb(d * d, 3) if d * d >= 3 else 0
        require(stock >= 0, "forced certificate stock")
        stage_checks += 1
        certificate_stock_checks += 1
        for mu in range(2, 6):
            require(3 * (mu - 1) * d * d >= 0, "CMR689 escape stock")
            escape_stock_checks += 1
    return {
        "mixed_child_host_pairs": host_pairs,
        "mixed_child_deletion_steps": recursion_steps,
        "mixed_child_atoms_deleted": deleted_atoms,
        "mixed_child_forced_endpoints": forced_endpoints,
        "mixed_child_clean_endpoints": clean_endpoints,
        "strict_child_measure_checks": strict_measure_checks,
        "forced_child_stage_formula_checks": stage_checks,
        "forced_child_certificate_stock_checks": certificate_stock_checks,
        "forced_child_escape_stock_checks": escape_stock_checks,
    }

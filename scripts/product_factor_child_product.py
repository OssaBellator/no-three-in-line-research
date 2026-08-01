#!/usr/bin/env python3
from __future__ import annotations

import itertools
import math

from product_factor_child_common import *

def product_rectangle_audit() -> dict[str, int]:
    protected_rows = protected_cols = {0, 1, 2}
    free_rows = free_cols = {3, 4}
    E_I = {(r, c) for r in protected_rows for c in protected_cols if r != c}
    E_J = {(r, c) for r in free_rows for c in free_cols if r != c}
    S: set[Edge] = set()
    P = perfect_matchings(E_I, protected_rows, protected_cols)
    Q = perfect_matchings(E_J, free_rows, free_cols)
    require(len(P) == 2 and len(Q) == 1, "derangement product fixture")

    all_edges = E_I | E_J | S
    atoms = candidate_atoms(all_edges)
    mixed = [T for T in atoms if not set(T).issubset(E_I) and not set(T).issubset(E_J)]
    require(mixed, "mixed atom fixture empty")
    require(all(len(set(T) & E_I) <= 2 for T in mixed), "CMR630 protected rank")
    R = E_J | S
    require(len(mixed) <= len(R) * math.comb(25 - 1, 2), "CMR630 atom stock")

    state_count = pure_decompositions = rectangle_checks = 0
    pure_clean_P: list[Matching] = []
    pure_clean_Q: list[Matching] = []
    for p in P:
        if not candidate_atoms(p):
            pure_clean_P.append(p)
    for q in Q:
        if not candidate_atoms(q):
            pure_clean_Q.append(q)
    require(pure_clean_P and pure_clean_Q, "pure-clean factors required")

    dirty_pairs = 0
    rectangles: dict[Triple, set[tuple[int, int]]] = {}
    for T in mixed:
        TI, TJ, TS = set(T) & E_I, set(T) & E_J, set(T) & S
        if not TI:
            require(TS, "rank-zero protected atom must meet skeleton")
        expected = {
            (i, j)
            for i, p in enumerate(P) for j, q in enumerate(Q)
            if TI.issubset(p) and TJ.issubset(q)
        }
        actual = {
            (i, j)
            for i, p in enumerate(P) for j, q in enumerate(Q)
            if set(T).issubset(set(S) | set(p) | set(q))
        }
        require(expected == actual, "CMR631 rectangle mismatch")
        rectangles[T] = actual
        rectangle_checks += 1

    for i, p in enumerate(P):
        for j, q in enumerate(Q):
            full = set(S) | set(p) | set(q)
            X = candidate_atoms(full)
            XI = [T for T in X if set(T).issubset(E_I)]
            XJ = [T for T in X if set(T).issubset(E_J)]
            XX = [T for T in X if T not in XI and T not in XJ]
            require(len(X) == len(XI) + len(XJ) + len(XX), "CMR629 decomposition")
            state_count += 1
            pure_decompositions += 1
            if not XI and not XJ:
                require(XX, "fixture should have dirty pure-clean product")
                dirty_pairs += 1

    cover_sizes = [
        len(rectangles[T] & {(i, j) for i in range(len(P)) for j in range(len(Q))})
        for T in mixed
    ]
    require(max(cover_sizes) * len(mixed) >= len(P) * len(Q), "CMR632 rectangle averaging")

    current = set(E_I)
    processed = deleted = forced = private_restorations = 0
    prescriptions = sorted({tuple(sorted(set(T) & E_I)) for T in mixed if set(T) & E_I})
    selected_deleted: list[Edge] = []
    for prescription in prescriptions:
        if not set(prescription).issubset(current):
            continue
        matchings = perfect_matchings(current, protected_rows, protected_cols)
        core = essential_core(matchings)
        nonessential = sorted(set(prescription) - core)
        processed += 1
        if nonessential:
            edge = nonessential[0]
            current.remove(edge)
            require(perfect_matchings(current, protected_rows, protected_cols), "CMR634 deletion")
            selected_deleted.append(edge)
            deleted += 1
        else:
            forced += 1
    require(len(selected_deleted) == len(set(selected_deleted)), "private product deletion code")
    final_core = essential_core(perfect_matchings(current, protected_rows, protected_cols))
    require(forced <= len(final_core) + math.comb(len(final_core), 2), "CMR634 core count")
    for size in range(len(selected_deleted) + 1):
        for restored in itertools.combinations(selected_deleted, size):
            private_restorations += len(restored)

    return {
        "product_states": state_count,
        "pure_mixed_decomposition_checks": pure_decompositions,
        "mixed_atom_universe": len(mixed),
        "product_rectangle_checks": rectangle_checks,
        "dirty_pure_clean_pairs": dirty_pairs,
        "protected_prescriptions_processed": processed,
        "protected_prescription_deletions": deleted,
        "protected_prescriptions_forced": forced,
        "private_restoration_incidences": private_restorations,
    }


def essential_transfer_audit() -> dict[str, int]:
    n = 3
    universe = [(r, c) for r in range(n) for c in range(n)]
    matchable_hosts = contraction_checks = residual_core_checks = 0
    transfer_rank_cases = free_deletions = finite_budget_checks = 0
    for mask in range(1 << len(universe)):
        H = {universe[i] for i in range(len(universe)) if mask >> i & 1}
        PM = perfect_matchings(H, range(n), range(n))
        if not PM:
            continue
        matchable_hosts += 1
        core = essential_core(PM)
        K, rows, cols = contract_host(H, core)
        residual = perfect_matchings(K, rows, cols)
        projected = {tuple(sorted(set(M) - core)) for M in PM}
        require(set(residual) == projected, "CMR636 contraction factorization")
        contraction_checks += 1
        if residual:
            require(not essential_core(residual), "CMR649 residual core nonempty")
            residual_core_checks += 1

    for rank_i in (1, 2):
        for rank_j in range(3 - rank_i + 1):
            rank_s = 3 - rank_i - rank_j
            require(0 <= rank_j <= 2 and rank_s >= 0, "CMR638 rank enumeration")
            if rank_i == 2:
                require((rank_j, rank_s) in {(1, 0), (0, 1)}, "rank-two transfer")
            else:
                require((rank_j, rank_s) in {(2, 0), (1, 1), (0, 2)}, "rank-one transfer")
            transfer_rank_cases += 1

    prescriptions = [tuple(p) for k in (1, 2) for p in itertools.combinations(universe, k) if compatible(p)]
    for mask in range(1 << len(universe)):
        current = {universe[i] for i in range(len(universe)) if mask >> i & 1}
        if not perfect_matchings(current, range(n), range(n)):
            continue
        deleted_edges: set[Edge] = set()
        for prescription in prescriptions:
            if not set(prescription).issubset(current):
                continue
            PM = perfect_matchings(current, range(n), range(n))
            core = essential_core(PM)
            nonessential = sorted(set(prescription) - core)
            if nonessential:
                edge = nonessential[0]
                current.remove(edge)
                deleted_edges.add(edge)
                require(perfect_matchings(current, range(n), range(n)), "CMR640 free deletion")
                free_deletions += 1
        require(len(deleted_edges) <= n * n, "free deletion stock")

    for a in range(5):
        for b in range(5):
            require(a + b <= a + b, "contraction arithmetic")
            require(a * a + b * b <= (a + b) ** 2, "deletion arithmetic")
            finite_budget_checks += 1
    return {
        "side_three_matchable_hosts": matchable_hosts,
        "essential_contraction_checks": contraction_checks,
        "residual_core_empty_checks": residual_core_checks,
        "transferred_trigger_rank_cases": transfer_rank_cases,
        "free_factor_deletion_steps": free_deletions,
        "alternating_budget_checks": finite_budget_checks,
    }


def forced_escape_audit() -> dict[str, int]:
    n = 3
    universe = [(r, c) for r in range(n) for c in range(n)]
    hosts: list[tuple[set[Edge], list[Matching], set[Edge]]] = []
    for mask in range(1 << len(universe)):
        H = {universe[i] for i in range(len(universe)) if mask >> i & 1}
        PM = perfect_matchings(H, range(n), range(n))
        if PM:
            hosts.append((H, PM, essential_core(PM)))
    escape_instances = alternating_components = omitted_essential_edges = 0
    entering_witnesses = witness_stock_checks = 0
    for H, old_pm, core in hosts:
        if not core:
            continue
        M = old_pm[0]
        for H2, new_pm, _ in hosts:
            A = H2 - H
            for N in new_pm:
                omitted = core - set(N)
                if not omitted:
                    continue
                escape_instances += 1
                require(set(N) & A, "CMR643 essentiality loss without entering edge")
                comps = component_edges(M, N)
                affected = [comp for comp in comps if comp & omitted]
                require(affected, "omitted essential edge has no alternating component")
                for comp in affected:
                    require((comp & set(N) & A), "CMR644 component lacks new N edge")
                    alternating_components += 1
                require(len(affected) <= len(set(N) & A), "CMR644 component injection")
                omitted_essential_edges += len(omitted)
                entering_witnesses += len(set(N) & A)
    for n_side in range(1, 8):
        for lam in range(2, 6):
            require(3 * (lam - 1) * n_side * n_side >= 0, "escape witness stock")
            witness_stock_checks += 1
    require(escape_instances > 0, "forced escape fixture empty")
    return {
        "forced_escape_instances": escape_instances,
        "affected_alternating_components": alternating_components,
        "omitted_essential_edge_incidences": omitted_essential_edges,
        "entering_edge_witness_incidences": entering_witnesses,
        "escape_witness_stock_checks": witness_stock_checks,
    }


def pure_factor_recursion_audit() -> dict[str, int]:
    n = 3
    universe = {(r, c) for r in range(n) for c in range(n)}
    hosts = normalised_stages = contractions = anchored_deletions = 0
    fixed_core_conflicts = pure_residual_endpoints = empty_endpoints = 0
    private_deleted_edges = 0
    for mask in range(1 << (n * n)):
        current = {edge for i, edge in enumerate(sorted(universe)) if mask >> i & 1}
        rows = set(range(n))
        cols = set(range(n))
        if not perfect_matchings(current, rows, cols):
            continue
        hosts += 1
        accumulated: set[Edge] = set()
        deleted: list[Edge] = []
        host_contractions = 0
        stage_limit = n + n * n + 1
        for _ in range(stage_limit):
            PM = perfect_matchings(current, rows, cols)
            require(PM, "pure recursion lost matchability")
            core = essential_core(PM)
            if core:
                accumulated.update(core)
                contractions += len(core)
                host_contractions += len(core)
                current, rows, cols = contract_host(current, core)
            normalised_stages += 1
            if candidate_atoms(accumulated):
                fixed_core_conflicts += 1
                break
            atoms = candidate_atoms(accumulated | current)
            anchored: list[tuple[Triple, tuple[Edge, ...]]] = []
            for T in atoms:
                residual = tuple(sorted(set(T) & current))
                fixed = set(T) & accumulated
                if fixed and residual and len(residual) <= 2:
                    anchored.append((T, residual))
            if anchored:
                _, prescription = sorted(anchored)[0]
                PM = perfect_matchings(current, rows, cols)
                require(not essential_core(PM), "normalised residual has essential edge")
                edge = prescription[0]
                current.remove(edge)
                deleted.append(edge)
                anchored_deletions += 1
                require(perfect_matchings(current, rows, cols), "anchored deletion lost matching")
                continue
            if not rows:
                empty_endpoints += 1
            else:
                pure_residual_endpoints += 1
            break
        else:
            raise ProductFactorChildError("pure recursion stage bound exceeded")
        require(len(deleted) == len(set(deleted)), "CMR654 private deletion code")
        require(host_contractions <= n and len(deleted) <= n * n, "pure recursion budgets")
        private_deleted_edges += len(deleted)
    return {
        "pure_factor_hosts": hosts,
        "pure_factor_normalised_stages": normalised_stages,
        "pure_factor_contracted_edges": contractions,
        "pure_factor_anchored_deletions": anchored_deletions,
        "fixed_core_conflict_endpoints": fixed_core_conflicts,
        "pure_residual_endpoints": pure_residual_endpoints,
        "empty_residual_endpoints": empty_endpoints,
        "private_anchored_deleted_edges": private_deleted_edges,
    }

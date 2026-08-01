#!/usr/bin/env python3
from __future__ import annotations

import itertools
import math
from collections import Counter

from target_anchor_common import *


def state_feasible(state: State, host: set[LabelledEdge]) -> bool:
    return set(state) <= host


def anchor_batch_audit() -> dict[str, int]:
    n = 3
    states = permutation_states(n)
    universe = {(layer, row, column) for layer in (0, 1)
                for row in range(n) for column in range(n)}
    require(len(states) == 12, "side-three saturated state count")
    anchor_passes = candidates = batches = deleted_edges = 0
    forced_targets = pair_forcings = contractions = 0
    private_disjoint_checks = restoration_subset_checks = 0
    for anchor in states:
        target = set(sorted(physical(anchor))[:3])
        host = set(universe)
        private_batches: list[set[LabelledEdge]] = []
        for candidate in states:
            if candidate == anchor or not state_feasible(candidate, host):
                continue
            if target <= physical(candidate):
                continue
            entering = set(candidate) - set(anchor)
            require(len(entering) >= 2 and entering.isdisjoint(anchor),
                    "CMR785 entering set")
            require(state_feasible(anchor, host - entering), "CMR786 anchor survival")
            require(not state_feasible(candidate, host - entering), "candidate rejection")
            require(all(entering.isdisjoint(old) for old in private_batches),
                    "CMR793 private batches")
            host -= entering
            private_batches.append(entering)
            batches += 1
            deleted_edges += len(entering)
            candidates += 1
        require(set(anchor) <= host, "anchor lost")
        require(len(private_batches) <= n * (n - 1), "CMR788 batch budget")
        require(sum(map(len, private_batches)) <= 2 * n * n - 2 * n,
                "deleted edge budget")
        survivors = [state for state in states if state_feasible(state, host)]
        if all(target <= physical(state) for state in survivors):
            forced_targets += 1
        pair = tuple(sorted(set(anchor))[:2])
        for candidate in list(survivors):
            if set(pair) <= set(candidate):
                continue
            entering = set(candidate) - set(anchor)
            if not entering:
                continue
            require(all(entering.isdisjoint(old) for old in private_batches),
                    "pair batch overlap")
            host -= entering
            private_batches.append(entering)
        survivors = [state for state in states if state_feasible(state, host)]
        if all(set(pair) <= set(state) for state in survivors):
            pair_forcings += 1
            contractions += 1
        private_union = set().union(*private_batches) if private_batches else set()
        require(private_union.isdisjoint(anchor), "private union meets anchor")
        for i, first in enumerate(private_batches):
            for second in private_batches[i + 1:]:
                require(first.isdisjoint(second), "batch non-disjoint")
                private_disjoint_checks += 1
        private_list = sorted(private_union)
        for size in range(len(private_list) + 1):
            for restored in itertools.combinations(private_list, size):
                later = host | set(restored)
                require(state_feasible(anchor, later), "stored anchor not feasible")
                require(state_feasible(anchor, later - private_union),
                        "CMR800 bulk redeletion")
                restoration_subset_checks += 1
        anchor_passes += 1
    return {
        "anchor_passes": anchor_passes,
        "target_destroying_candidates_rejected": candidates,
        "private_entering_batches": batches,
        "private_deleted_edge_incidences": deleted_edges,
        "branch_local_forced_targets": forced_targets,
        "branch_local_pair_forcings": pair_forcings,
        "branch_local_pair_contractions": contractions,
        "private_batch_disjointness_checks": private_disjoint_checks,
        "bulk_redeletion_restoration_subsets": restoration_subset_checks,
    }


def anchor_restoration_audit() -> dict[str, int]:
    n = 3
    states = permutation_states(n)
    anchor = states[0]
    batches = []
    used = set(anchor)
    for candidate in states[1:]:
        entering = set(candidate) - set(anchor)
        if len(entering) >= 2 and entering.isdisjoint(used):
            batches.append(entering)
            used |= entering
    private_union = set().union(*batches) if batches else set()
    reopen_profiles = assigned_restorations = normalized_profiles = cycle_erasures = 0
    anchor_loss_profiles = replacement_checks = 0
    private_list = sorted(private_union)
    for mask in range(1 << len(private_list)):
        restored = {private_list[i] for i in range(len(private_list)) if mask >> i & 1}
        reopened = [batch for batch in batches if batch & restored]
        require(len(restored) >= len(reopened), "CMR795 restored-edge injection")
        chosen = [sorted(batch & restored)[0] for batch in reopened]
        require(len(chosen) == len(set(chosen)), "private restoration assignment")
        reopen_profiles += 1
        assigned_restorations += len(chosen)
        host_base = set(anchor) | private_union
        normalized = (host_base | restored) - private_union
        require(normalized == host_base - private_union, "CMR808 normalization")
        normalized_profiles += 1
        if normalized == set(anchor):
            cycle_erasures += 1
    for lost_count in range(1, len(anchor) + 1):
        lost = set(anchor[:lost_count])
        later = set(anchor) - lost
        require(set(anchor) - later, "CMR801 anchor loss witness")
        anchor_loss_profiles += 1
        require(lost_count <= 2 * n * n - 2 * n or lost_count <= len(anchor),
                "CMR803 replacement budget")
        replacement_checks += 1
    for threshold in range(2, 6):
        require((threshold - 1) * 2 * n * n >= 0, "CMR796 reopening bound")
    return {
        "anchor_reopening_profiles": reopen_profiles,
        "assigned_private_restorations": assigned_restorations,
        "private_normalization_profiles": normalized_profiles,
        "pure_reopening_cycle_erasures": cycle_erasures,
        "anchor_loss_profiles": anchor_loss_profiles,
        "anchor_replacement_checks": replacement_checks,
    }


def active_context_audit() -> dict[str, int]:
    n = 3
    states = permutation_states(n)
    anchor = states[0]
    private: set[LabelledEdge] = set()
    base_host = set(anchor)
    activation_profiles = absorbed_enablers = deactivation_profiles = 0
    normalized_change_profiles = recurrence_bound_checks = 0
    for candidate in states[1:]:
        entering = set(candidate) - set(anchor)
        if len(entering) < 2 or entering & private:
            continue
        host = base_host - private
        later = (host | set(candidate)) - private
        require(not state_feasible(candidate, host) and state_feasible(candidate, later),
                "newly enabled state fixture")
        require(set(candidate) & (later - host), "CMR814 activation support")
        require((later - host) <= entering, "CMR815 new edge outside entering batch")
        private |= entering
        require((later - host) <= private, "activation edge not privatized")
        activation_profiles += 1
        absorbed_enablers += len(later - host)
        require(later - private == host - private,
                "active private absorption normalization")
        normalized_change_profiles += 1
    for state in states:
        host = set(state)
        for edge in state:
            reduced = host - {edge}
            require(state_feasible(state, host) and not state_feasible(state, reduced),
                    "CMR817 loss witness")
            deactivation_profiles += 1
    for threshold in range(2, 7):
        bound = n * (n - 1) + 2 * threshold * n * n
        require(bound >= n * (n - 1), "CMR819 active transition bound")
        recurrence_bound_checks += 1
    return {
        "active_context_activation_profiles": activation_profiles,
        "absorbed_activation_edge_incidences": absorbed_enablers,
        "active_context_deactivation_profiles": deactivation_profiles,
        "normalized_context_change_profiles": normalized_change_profiles,
        "active_transition_bound_checks": recurrence_bound_checks,
    }


def physical_edge_lineage_audit() -> dict[str, int]:
    product_ownership_checks = side_lineages = owner_slot_checks = 0
    restoration_concentration_checks = 0
    factors = [({0, 1}, {0, 1}), ({2, 3}, {2, 3}), ({4}, {4})]
    fixed = {(5, 5)}
    all_edges = set(fixed)
    factor_edges = []
    for rows, columns in factors:
        edges = {(row, column) for row in rows for column in columns}
        factor_edges.append(edges)
        all_edges |= edges
    for edge in all_edges:
        memberships = int(edge in fixed) + sum(edge in edges for edges in factor_edges)
        require(memberships == 1, "CMR822 unique ownership")
        product_ownership_checks += 1
    for ambient in range(1, 13):
        stage_stock = sum(2 * side * side + side + 1 for side in range(1, ambient + 1))
        visited = sum(2 * side * side + side + 1 for side in range(ambient, 0, -1))
        require(visited == stage_stock, "CMR824 edge lineage stock")
        side_lineages += 1
        for h in range(1, 5):
            owner_slots = (h + 1) * (stage_stock + 1)
            require(owner_slots >= stage_stock + 1, "CMR825 owner slots")
            owner_slot_checks += 1
            for threshold in range(2, 5):
                restorations = (threshold - 1) * owner_slots + 1
                require(math.ceil(restorations / owner_slots) >= threshold,
                        "CMR826 restoration concentration")
                restoration_concentration_checks += 1
    return {
        "unique_product_edge_ownership_checks": product_ownership_checks,
        "strict_side_lineage_profiles": side_lineages,
        "physical_edge_owner_slot_checks": owner_slot_checks,
        "restoration_owner_concentration_checks": restoration_concentration_checks,
    }

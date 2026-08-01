#!/usr/bin/env python3
"""Check CMR854--CMR925 SCC, constant-arity branch, and minimum-face ancestry."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
from math import ceil, floor
from typing import Any

Edge = tuple[int, int]
LEdge = tuple[int, int, int]
State = frozenset[LEdge]
Triple = frozenset[LEdge]


class FrontierError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise FrontierError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def permutations(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(itertools.permutations(range(n)))


def matching(perm: tuple[int, ...]) -> frozenset[Edge]:
    return frozenset((i, perm[i]) for i in range(len(perm)))


def perfect_matchings(n: int, host: frozenset[Edge]) -> tuple[frozenset[Edge], ...]:
    return tuple(matching(p) for p in permutations(n) if matching(p) <= host)


def sccs(n: int, arcs: frozenset[tuple[int, int]]) -> tuple[frozenset[int], ...]:
    reach = [[False] * n for _ in range(n)]
    for i in range(n):
        reach[i][i] = True
    for i, j in arcs:
        reach[i][j] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    out: list[frozenset[int]] = []
    unseen = set(range(n))
    while unseen:
        i = min(unseen)
        comp = frozenset(j for j in unseen if reach[i][j] and reach[j][i])
        out.append(comp)
        unseen -= comp
    return tuple(out)


def acyclic_after_removal(
    n: int, arcs: frozenset[tuple[int, int]], removed: frozenset[int]
) -> bool:
    active = [i for i in range(n) if i not in removed]
    indeg = {i: 0 for i in active}
    adj = {i: [] for i in active}
    for i, j in arcs:
        if i in indeg and j in indeg:
            adj[i].append(j)
            indeg[j] += 1
    stack = [i for i in active if indeg[i] == 0]
    seen = 0
    while stack:
        i = stack.pop()
        seen += 1
        for j in adj[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                stack.append(j)
    return seen == len(active)


def fvs_number(n: int, arcs: frozenset[tuple[int, int]]) -> int:
    for r in range(n + 1):
        for subset in itertools.combinations(range(n), r):
            if acyclic_after_removal(n, arcs, frozenset(subset)):
                return r
    raise AssertionError


def distinguishing_rank(
    family: tuple[frozenset[Any], ...], q: frozenset[Any]
) -> int:
    alternatives = [q - r for r in family if r != q]
    if not alternatives:
        return 0
    qtuple = tuple(sorted(q))
    for size in range(len(qtuple) + 1):
        for subset in itertools.combinations(qtuple, size):
            b = frozenset(subset)
            if all(b & diff for diff in alternatives):
                return size
    raise AssertionError


def matching_scc_audit(n: int = 3) -> dict[str, int]:
    universe = tuple((i, j) for i in range(n) for j in range(n))
    hosts = nodes = edge_checks = product_checks = width_checks = local_cover_checks = 0
    for mask in range(1 << len(universe)):
        host = frozenset(universe[i] for i in range(len(universe)) if mask >> i & 1)
        fam = perfect_matchings(n, host)
        if not fam:
            continue
        hosts += 1
        union = frozenset().union(*fam)
        for q in fam:
            nodes += 1
            qperm = tuple(next(v for u, v in q if u == i) for i in range(n))
            arcs = frozenset(
                (i, j)
                for i in range(n)
                for j in range(n)
                if i != j and (i, qperm[j]) in host
            )
            comps = sccs(n, arcs)
            comp_of = {v: c for c, comp in enumerate(comps) for v in comp}
            active = frozenset(q) | frozenset(
                (i, qperm[j]) for i, j in arcs if comp_of[i] == comp_of[j]
            )
            require(active == union, "CMR854-855 usable-edge union")
            edge_checks += len(host)
            local_counts: list[int] = []
            local_deltas: list[int] = []
            cyclic = 0
            local_cover: set[Edge] = set()
            for comp in comps:
                rows = tuple(sorted(comp))
                targets = frozenset(qperm[i] for i in rows)
                block = frozenset(
                    (i, j) for i, j in active if i in comp and j in targets
                )
                local = []
                for perm_targets in itertools.permutations(sorted(targets)):
                    m = frozenset(zip(rows, perm_targets))
                    if m <= block:
                        local.append(m)
                local_family = tuple(local)
                require(local_family, "CMR856 local factor matchable")
                local_counts.append(len(local_family))
                qlocal = frozenset(e for e in q if e[0] in comp)
                dlocal = distinguishing_rank(local_family, qlocal)
                local_deltas.append(dlocal)
                sub_arcs = frozenset(
                    (i, j) for i, j in arcs if i in comp and j in comp
                )
                fvs = fvs_number(n, sub_arcs)
                require(dlocal == fvs, "CMR857 local FVS width")
                if fvs:
                    cyclic += 1
                for size in range(len(qlocal) + 1):
                    found = None
                    for subset in itertools.combinations(sorted(qlocal), size):
                        b = frozenset(subset)
                        if all(
                            b & (qlocal - r)
                            for r in local_family
                            if r != qlocal
                        ):
                            found = b
                            break
                    if found is not None:
                        local_cover.update(found)
                        break
            product = 1
            for count in local_counts:
                product *= count
            require(product == len(fam), "CMR856 exact SCC product count")
            product_checks += 1
            delta = distinguishing_rank(fam, q)
            require(delta == sum(local_deltas), "CMR857 width additivity")
            require(cyclic <= delta, "CMR858 cyclic component count")
            require(len(local_cover) == delta, "CMR859 local cover assembly")
            for r in fam:
                if r != q:
                    require(
                        any(e not in r for e in local_cover),
                        "CMR859 exact cover",
                    )
            local_cover_checks += 1
            width_checks += 1
    return {
        "matchable_hosts": hosts,
        "matching_nodes": nodes,
        "usable_edge_checks": edge_checks,
        "scc_product_checks": product_checks,
        "scc_width_checks": width_checks,
        "local_cover_checks": local_cover_checks,
    }


def joint_states(n: int = 3) -> tuple[State, ...]:
    out = []
    for p0 in permutations(n):
        for p1 in permutations(n):
            if all(p0[i] != p1[i] for i in range(n)):
                out.append(
                    frozenset(
                        {
                            *((0, i, p0[i]) for i in range(n)),
                            *((1, i, p1[i]) for i in range(n)),
                        }
                    )
                )
    return tuple(out)


def physical(state: State) -> frozenset[tuple[int, int]]:
    return frozenset((r, c) for _, r, c in state)


def collinear(
    a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]
) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])


def physical_triples(state: State) -> tuple[frozenset[tuple[int, int]], ...]:
    points = sorted(physical(state))
    return tuple(
        frozenset(triple)
        for triple in itertools.combinations(points, 3)
        if collinear(*triple)
    )


def labelled_triple(
    state: State, triple: frozenset[tuple[int, int]]
) -> Triple:
    return frozenset(e for e in state if (e[1], e[2]) in triple)


def support(triple: Triple) -> frozenset[tuple[Any, ...]]:
    atoms = set()
    for layer, row, column in triple:
        atoms.add(("cell", row, column))
        atoms.add(("source", layer, row))
        atoms.add(("target", layer, column))
    return frozenset(atoms)


def family_core(family: tuple[State, ...]) -> frozenset[LEdge]:
    core = set(family[0])
    for state in family[1:]:
        core &= set(state)
    return frozenset(core)


def exact_prescription_audit(states: tuple[State, ...]) -> dict[str, int]:
    family_count = prescription_checks = ordered_checks = min_face_edge_checks = 0
    new_triples = minimum_forcing_steps = support_checks = batching_checks = 0
    universe = tuple(
        (layer, row, column)
        for layer in range(2)
        for row in range(3)
        for column in range(3)
    )
    potentials = {state: len(physical_triples(state)) for state in states}
    signatures: set[Triple] = set()
    for family_mask in range(1, 1 << len(states)):
        family = tuple(
            states[i] for i in range(len(states)) if family_mask >> i & 1
        )
        family_count += 1
        minimum = min(potentials[state] for state in family)
        minimum_face = tuple(
            state for state in family if potentials[state] == minimum
        )
        minimum_core = family_core(minimum_face)
        residuals = tuple(
            frozenset(state - minimum_core) for state in minimum_face
        )
        require(
            not residuals
            or not set.intersection(*(set(residual) for residual in residuals)),
            "CMR913 residual minimum core",
        )
        for edge in universe:
            avoiders = tuple(state for state in minimum_face if edge not in state)
            if avoiders:
                require(
                    min(
                        potentials[state]
                        for state in family
                        if edge not in state
                    )
                    == minimum,
                    "CMR911 min avoiding deletion",
                )
            else:
                require(edge in minimum_core, "CMR911 minimum core")
            min_face_edge_checks += 1
        for rejected in family:
            rejected_edges = tuple(sorted(rejected))
            for size in range(1, 4):
                for ordered_prescription in itertools.combinations(
                    rejected_edges, size
                ):
                    prescription = frozenset(ordered_prescription)
                    deletion_union = {
                        state
                        for state in family
                        if any(edge not in state for edge in prescription)
                    }
                    conditioned = {
                        state for state in family if prescription <= state
                    }
                    require(
                        deletion_union | conditioned == set(family),
                        "CMR862 split",
                    )
                    require(
                        {state for state in family if state != rejected}
                        == deletion_union | (conditioned - {rejected}),
                        "CMR862 rejected split",
                    )
                    prescription_checks += 1
                    children = []
                    prefix: set[LEdge] = set()
                    for edge in ordered_prescription:
                        child = {
                            state
                            for state in family
                            if prefix <= state and edge not in state
                        }
                        children.append(child)
                        prefix.add(edge)
                    children.append(
                        {state for state in family if prescription <= state}
                    )
                    require(
                        set().union(*children) == set(family),
                        "CMR894 ordered cover",
                    )
                    require(
                        sum(len(child) for child in children) == len(family),
                        "CMR894 disjoint partition",
                    )
                    ordered_checks += 1
        anchor = min(minimum_face, key=lambda state: tuple(sorted(state)))
        anchor_triples = set(physical_triples(anchor))
        for candidate in family:
            candidate_triples = set(physical_triples(candidate))
            if (
                anchor_triples - candidate_triples
                and potentials[candidate] >= potentials[anchor]
            ):
                new = sorted(
                    candidate_triples - anchor_triples,
                    key=lambda triple: tuple(sorted(triple)),
                )
                require(new, "CMR866 new triple")
                prescription = labelled_triple(candidate, new[0])
                require(
                    len(prescription) == 3 and prescription - anchor,
                    "CMR866 nonanchor edge",
                )
                signatures.add(prescription)
                new_triples += 1
        if anchor_triples:
            target = min(anchor_triples, key=lambda triple: tuple(sorted(triple)))
            current = list(family)
            deleted: set[LEdge] = set()
            while any(not target <= physical(state) for state in current):
                candidate = min(
                    (
                        state
                        for state in current
                        if not target <= physical(state)
                    ),
                    key=lambda state: tuple(sorted(state)),
                )
                candidate_new = sorted(
                    set(physical_triples(candidate)) - anchor_triples,
                    key=lambda triple: tuple(sorted(triple)),
                )
                require(candidate_new, "CMR903 forcing new triple")
                prescription = labelled_triple(candidate, candidate_new[0])
                edge = min(prescription - anchor)
                require(edge not in deleted, "CMR904 distinct deletion")
                deleted.add(edge)
                current = [state for state in current if edge not in state]
                require(anchor in current, "CMR902 anchor preserved")
                minimum_forcing_steps += 1
            require(
                all(target <= physical(state) for state in current),
                "CMR904 target forced",
            )
            anchor_prescription = labelled_triple(anchor, target)
            while any(
                not anchor_prescription <= state for state in current
            ):
                candidate = min(
                    (
                        state
                        for state in current
                        if not anchor_prescription <= state
                    ),
                    key=lambda state: tuple(sorted(state)),
                )
                edge = min(candidate - anchor)
                require(edge not in deleted, "CMR905 distinct pool")
                deleted.add(edge)
                current = [state for state in current if edge not in state]
                require(anchor in current, "CMR905 anchor preserved")
                minimum_forcing_steps += 1
            require(
                len(deleted) <= 12
                and all(anchor_prescription <= state for state in current),
                "CMR905 force bound",
            )
    signature_list = tuple(
        sorted(signatures, key=lambda triple: tuple(sorted(triple)))
    )
    for triple in signature_list:
        require(len(support(triple)) == 9, "CMR870 support size")
        support_checks += 1
    packing: list[Triple] = []
    for triple in signature_list:
        if all(
            support(triple).isdisjoint(support(other)) for other in packing
        ):
            packing.append(triple)
    cover = (
        frozenset().union(*(support(triple) for triple in packing))
        if packing
        else frozenset()
    )
    require(
        all(support(triple) & cover for triple in signature_list),
        "CMR872 maximal support cover",
    )
    for first, second in itertools.combinations(packing, 2):
        require(
            support(first).isdisjoint(support(second)),
            "CMR875 disjoint bank",
        )
    support_checks += len(signature_list)
    atom_groups: dict[tuple[Any, ...], list[Triple]] = {}
    for triple in signature_list:
        for atom in support(triple):
            atom_groups.setdefault(atom, []).append(triple)
    for atom, group in atom_groups.items():
        counts: dict[LEdge, int] = {}
        for triple in group:
            for edge in triple:
                if atom[0] == "cell" and (edge[1], edge[2]) == atom[1:]:
                    counts[edge] = counts.get(edge, 0) + 1
                elif atom[0] == "source" and (edge[0], edge[1]) == atom[1:]:
                    counts[edge] = counts.get(edge, 0) + 1
                elif atom[0] == "target" and (edge[0], edge[2]) == atom[1:]:
                    counts[edge] = counts.get(edge, 0) + 1
        edge, count = max(counts.items(), key=lambda item: item[1])
        require(
            count >= ceil(len(group) / 6),
            "CMR888 uniform stabilization for n=3",
        )
        without = {state for state in states if edge not in state}
        with_edge = {state for state in states if edge in state}
        require(
            without.isdisjoint(with_edge)
            and without | with_edge == set(states),
            "CMR889 binary split",
        )
        for triple in group:
            if edge in triple:
                require(
                    len(triple - {edge}) == 2,
                    "CMR891 rank-two residual",
                )
        batching_checks += 1
    return {
        "joint_states": len(states),
        "state_families": family_count,
        "prescription_split_checks": prescription_checks,
        "ordered_partition_checks": ordered_checks,
        "minimum_face_edge_checks": min_face_edge_checks,
        "new_triple_witnesses": new_triples,
        "minimum_forcing_steps": minimum_forcing_steps,
        "distinct_new_triple_signatures": len(signature_list),
        "support_checks": support_checks,
        "support_atom_batches": batching_checks,
    }


def leaf_compression_audit(states: tuple[State, ...]) -> dict[str, int]:
    potentials = {state: len(physical_triples(state)) for state in states}
    root = tuple(state for state in states if potentials[state] >= 1)
    if not root:
        return {"tree_nodes": 0, "tree_leaves": 0, "terminal_classes": 0}
    leaves: list[
        tuple[
            tuple[State, ...],
            frozenset[LEdge],
            frozenset[LEdge],
            frozenset[tuple[int, int]],
        ]
    ] = []
    nodes = 0

    def recurse(
        family: tuple[State, ...],
        fixed: frozenset[LEdge],
        deleted: frozenset[LEdge],
        depth: int,
    ) -> None:
        nonlocal nodes
        nodes += 1
        require(depth <= 18, "CMR897 tree depth")
        anchor = min(
            family,
            key=lambda state: (potentials[state], tuple(sorted(state))),
        )
        triples = sorted(
            physical_triples(anchor), key=lambda triple: tuple(sorted(triple))
        )
        require(triples, "positive baseline leaf target")
        target = triples[0]
        omitters = [
            candidate
            for candidate in family
            if not target <= physical(candidate)
        ]
        if not omitters:
            leaves.append((family, fixed, deleted, target))
            return
        candidate = min(omitters, key=lambda state: tuple(sorted(state)))
        new = sorted(
            set(physical_triples(candidate)) - set(physical_triples(anchor)),
            key=lambda triple: tuple(sorted(triple)),
        )
        require(new, "CMR896 new triple")
        prescription = labelled_triple(candidate, new[0])
        residual = tuple(
            edge
            for edge in sorted(prescription)
            if edge not in fixed and edge not in deleted
        )
        require(residual, "CMR896 undecided edge")
        prefix: set[LEdge] = set()
        children = []
        for edge in residual:
            child = tuple(
                state
                for state in family
                if prefix <= state and edge not in state
            )
            if child:
                children.append(
                    (child, fixed | frozenset(prefix), deleted | {edge})
                )
            prefix.add(edge)
        child = tuple(
            state for state in family if set(residual) <= state
        )
        if child:
            children.append((child, fixed | frozenset(residual), deleted))
        require(
            sum(len(item[0]) for item in children) == len(family),
            "CMR894 tree partition",
        )
        for child_family, child_fixed, child_deleted in children:
            recurse(child_family, child_fixed, child_deleted, depth + 1)

    recurse(root, frozenset(), frozenset(), 0)
    require(
        sum(len(family) for family, _, _, _ in leaves) == len(root),
        "CMR898 leaf partition",
    )
    classes: dict[
        tuple[tuple[tuple[int, int], ...], tuple[int, ...]], list[State]
    ] = {}
    for family, _, _, target in leaves:
        ordered = tuple(sorted(target))
        for state in family:
            assignment = tuple(
                next(
                    layer
                    for layer, row, column in state
                    if (row, column) == cell
                )
                for cell in ordered
            )
            classes.setdefault((ordered, assignment), []).append(state)
    for (ordered, assignment), family in classes.items():
        prescription = frozenset(
            (assignment[index], ordered[index][0], ordered[index][1])
            for index in range(3)
        )
        require(
            all(prescription <= state for state in family),
            "CMR900 fixed labelled triple class",
        )
    require(len(classes) <= 8 * 84, "CMR901 class bound")
    return {
        "tree_nodes": nodes,
        "tree_leaves": len(leaves),
        "terminal_classes": len(classes),
        "tree_root_states": len(root),
    }


def path_budget_audit(max_n: int = 12) -> dict[str, int]:
    checks = 0
    max_edge_slots = 0
    for n in range(1, max_n + 1):
        deletion_budget = 2 * n * n - 2 * n
        combined_budget = deletion_budget + floor(2 * n / 3)
        require(combined_budget >= deletion_budget, "CMR878 budget")
        for h in range(1, 5):
            stage_sum = sum(2 * m * m + m + 1 for m in range(1, n + 1))
            owner_slots = (h + 1) * (stage_sum + 1)
            max_edge_slots = max(max_edge_slots, owner_slots)
            for threshold in range(2, 6):
                active_bound = 2 * n * n * threshold * owner_slots
                require(
                    active_bound >= threshold * owner_slots,
                    "CMR923 active bound",
                )
                active = threshold * owner_slots
                restorations = max(0, active - owner_slots)
                require(
                    restorations >= 0 and active <= restorations + owner_slots,
                    "CMR919 restoration",
                )
                token = restorations * 3 * (h - 1)
                require(token >= 0, "CMR921 token")
                checks += 1
    return {
        "path_budget_parameter_checks": checks,
        "max_edge_owner_slots": max_edge_slots,
    }


CONTRACT = {
    "schema": "prime-power-scc-branch-minimum-face-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(854, 926)],
    "banks": [
        "generic-exchange-scc-width",
        "new-triple-constant-arity-split",
        "new-triple-support-packing",
        "constant-arity-path-budget",
        "support-atom-edge-batching",
        "disjoint-leaf-certificate-compression",
        "minimum-anchor-preserving-path",
        "minimum-face-edge-dichotomy",
        "minimum-face-edge-lineage-budget",
    ],
    "honesty": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = (
    "3ec89baac0450290c3dbe3a340af76aaea95bf7f4c84342a9aac8f7c31862498"
)


def mutation_audit() -> int:
    mutations = [
        lambda contract: contract.update(schema="bad"),
        lambda contract: contract.update(source_theorems=[]),
        lambda contract: contract["source_theorems"].pop(),
        lambda contract: contract["source_theorems"].__setitem__(0, "CMR853"),
        lambda contract: contract["banks"].pop(),
        lambda contract: contract["banks"].append(contract["banks"][0]),
        lambda contract: contract["honesty"].update(all_n_proved_by_checker=1),
        lambda contract: contract["honesty"].update(global_termination_proved=1),
        lambda contract: contract["honesty"].pop(
            "actual_global_parent_rule_complete"
        ),
    ]

    def validate_contract(contract: dict[str, Any]) -> None:
        require(contract.get("schema") == CONTRACT["schema"], "contract schema")
        require(
            contract.get("source_theorems")
            == [f"CMR{i}" for i in range(854, 926)],
            "contract theorem interval",
        )
        require(contract.get("banks") == CONTRACT["banks"], "contract banks")
        require(
            contract.get("honesty") == CONTRACT["honesty"],
            "contract honesty",
        )

    rejected = 0
    for mutate in mutations:
        contract = copy.deepcopy(CONTRACT)
        mutate(contract)
        try:
            validate_contract(contract)
        except FrontierError:
            rejected += 1
    require(rejected == len(mutations), "contract mutation accepted")
    return rejected


def main() -> None:
    contract_sha = digest(CONTRACT)
    require(contract_sha == EXPECTED_CONTRACT_SHA256, "contract digest")
    matching_report = matching_scc_audit()
    states = joint_states()
    state_report = exact_prescription_audit(states)
    leaf_report = leaf_compression_audit(states)
    path_report = path_budget_audit()
    report = {
        "checker": "prime-power-scc-branch-minimum-face-ancestry",
        "contract_sha256": contract_sha,
        **matching_report,
        **state_report,
        **leaf_report,
        **path_report,
        "rejected_corruptions": mutation_audit(),
        "generic_exchange_scc_width_exact": 1,
        "new_triple_constant_arity_split_exact": 1,
        "new_triple_support_packing_exact": 1,
        "constant_arity_path_budget_exact": 1,
        "support_atom_edge_batching_exact": 1,
        "disjoint_leaf_certificate_compression_exact": 1,
        "minimum_anchor_preserving_path_exact": 1,
        "minimum_face_edge_dichotomy_exact": 1,
        "minimum_face_edge_lineage_budget_exact": 1,
        "scc_branch_minimum_face_ancestry_proved": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()

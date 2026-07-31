#!/usr/bin/env python3
"""Verify genuine routing-change ancestry inside an asymmetric context.

CMR656--CMR663 define the canonical factor-prefix envelope and routing skeleton.
CMR671--CMR676 define changed routing vertices, entering/leaving edge support,
alternating-component support and finite routing-change stock. This checker
embeds one balanced factor host as layer zero of a canonical asymmetric context
(layer one is empty), reconstructs all theorem data, and emits a typed state
transition with theorem-derived factor, routing and envelope labels.

This proves ancestry only for the routing-skeleton-change operation kind. It
does not prove that all construction operations are represented, termination,
or the all-n conjecture.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations, permutations
from typing import Any, Iterable

Edge = tuple[int, int, int]
Matching = tuple[tuple[int, int], ...]
State = tuple[Edge, ...]
EXPECTED_CONTRACT_SHA256 = "b2de334dedbde2a865704f3d08cc9f590e74e14b7e8d813c329e59cc97636360"


class RoutingChangeContextAncestryError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RoutingChangeContextAncestryError(message)


def digest(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_int(value: Any, path: str, minimum: int = 0) -> int:
    require(isinstance(value, int) and not isinstance(value, bool) and value >= minimum,
            f"{path}: integer at least {minimum} required")
    return value


def exact_coordinates(raw: Iterable[int], t: int, path: str) -> tuple[int, ...]:
    values = tuple(raw)
    require(values == tuple(sorted(values)), f"{path}: canonical order required")
    require(len(values) == len(set(values)), f"{path}: duplicate coordinate")
    require(values, f"{path}: nonempty coordinate set required")
    require(all(isinstance(x, int) and not isinstance(x, bool) and 0 <= x < t
                for x in values), f"{path}: coordinate outside ambient side")
    return values


def exact_deleted(raw: Iterable[Iterable[int]], x: tuple[int, ...],
                  y: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    edges = tuple(tuple(edge) for edge in raw)
    require(edges == tuple(sorted(edges)), "deleted_edges: canonical order required")
    require(len(edges) == len(set(edges)), "deleted_edges: duplicate edge")
    require(all(len(edge) == 2 and edge[0] in x and edge[1] in y for edge in edges),
            "deleted_edges: edge outside factor host")
    return edges  # type: ignore[return-value]


def exact_matching(raw: Iterable[Iterable[int]], x: tuple[int, ...],
                   y: tuple[int, ...], deleted: tuple[tuple[int, int], ...],
                   path: str) -> Matching:
    matching = tuple(tuple(edge) for edge in raw)
    require(matching == tuple(sorted(matching)), f"{path}: canonical order required")
    require(len(matching) == len(x), f"{path}: exact factor size required")
    require(len(set(matching)) == len(matching), f"{path}: duplicate edge")
    require({edge[0] for edge in matching} == set(x), f"{path}: source saturation failed")
    require({edge[1] for edge in matching} == set(y), f"{path}: target saturation failed")
    require(set(matching).isdisjoint(deleted), f"{path}: contains deleted edge")
    return matching  # type: ignore[return-value]


def generate_factor_family(x: tuple[int, ...], y: tuple[int, ...],
                           deleted: tuple[tuple[int, int], ...]) -> tuple[Matching, ...]:
    deleted_set = set(deleted)
    family = []
    for image in permutations(y):
        matching = tuple((x[index], image[index]) for index in range(len(x)))
        if deleted_set.isdisjoint(matching):
            family.append(matching)
    return tuple(sorted(family))


def delta(values: tuple[int, ...], p: int, h: int) -> int:
    for s in range(h, -1, -1):
        modulus = p ** s
        residues = {value % modulus for value in values}
        if len(residues) == 1:
            return s
    raise AssertionError("depth zero must be common")


def child_label(value: int, p: int, beta: int) -> int:
    return (value // (p ** beta)) % p


def matching_map(matching: Matching) -> dict[int, int]:
    return dict(matching)


def inverse_map(matching: Matching) -> dict[int, int]:
    return {target: source for source, target in matching}


def routing_skeleton(matching: Matching, x: tuple[int, ...], y: tuple[int, ...],
                     p: int, beta: int) -> dict[str, Any]:
    forward = matching_map(matching)
    inverse = inverse_map(matching)
    source_map = [[source, child_label(forward[source], p, beta)] for source in x]
    target_map = [[target, child_label(inverse[target], p, beta)] for target in y]
    cells = []
    for r in range(p):
        for s in range(p):
            xs = [source for source in x
                  if child_label(source, p, beta) == r
                  and child_label(forward[source], p, beta) == s]
            ys = [target for target in y
                  if child_label(target, p, beta) == s
                  and child_label(inverse[target], p, beta) == r]
            require(len(xs) == len(ys), "routing cell source/target sizes differ")
            if xs or ys:
                cells.append({"source_child": r, "target_child": s,
                              "sources": xs, "targets": ys, "load": len(xs)})
    result: dict[str, Any] = {
        "source_routing_map": source_map,
        "target_routing_map": target_map,
        "routing_cells": cells,
    }
    result["routing_sha256"] = digest(result)
    return result


def changed_vertices(m: Matching, n: Matching, x: tuple[int, ...],
                     y: tuple[int, ...], p: int, beta: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    fm, fn = matching_map(m), matching_map(n)
    im, inn = inverse_map(m), inverse_map(n)
    ax = tuple(source for source in x
               if child_label(fm[source], p, beta) != child_label(fn[source], p, beta))
    ay = tuple(target for target in y
               if child_label(im[target], p, beta) != child_label(inn[target], p, beta))
    return ax, ay


def support_edges(m: Matching, n: Matching, ax: tuple[int, ...],
                  ay: tuple[int, ...]) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
    fm, fn = matching_map(m), matching_map(n)
    im, inn = inverse_map(m), inverse_map(n)
    entering = tuple(sorted({(source, fn[source]) for source in ax}
                            | {(inn[target], target) for target in ay}))
    leaving = tuple(sorted({(source, fm[source]) for source in ax}
                           | {(im[target], target) for target in ay}))
    return entering, leaving


def alternating_components(m: Matching, n: Matching, ax: tuple[int, ...],
                           ay: tuple[int, ...]) -> tuple[dict[str, Any], ...]:
    adjacency: dict[tuple[str, int], set[tuple[str, int]]] = {}
    edge_labels: dict[frozenset[tuple[str, int]], list[str]] = {}
    for label, matching in (("old", m), ("new", n)):
        for source, target in matching:
            left, right = ("x", source), ("y", target)
            adjacency.setdefault(left, set()).add(right)
            adjacency.setdefault(right, set()).add(left)
            edge_labels.setdefault(frozenset((left, right)), []).append(label)
    seen: set[tuple[str, int]] = set()
    components = []
    for root in sorted(adjacency):
        if root in seen:
            continue
        stack = [root]
        vertices = set()
        while stack:
            vertex = stack.pop()
            if vertex in vertices:
                continue
            vertices.add(vertex)
            seen.add(vertex)
            stack.extend(adjacency[vertex] - vertices)
        old_edges, new_edges = [], []
        for key, labels in edge_labels.items():
            u, v = tuple(key)
            if u in vertices and v in vertices:
                edge = (u[1], v[1]) if u[0] == "x" else (v[1], u[1])
                if "old" in labels:
                    old_edges.append(edge)
                if "new" in labels:
                    new_edges.append(edge)
        changed_sources = sorted(value for kind, value in vertices if kind == "x" and value in ax)
        changed_targets = sorted(value for kind, value in vertices if kind == "y" and value in ay)
        component = {
            "source_vertices": sorted(value for kind, value in vertices if kind == "x"),
            "target_vertices": sorted(value for kind, value in vertices if kind == "y"),
            "old_edges": [list(edge) for edge in sorted(old_edges)],
            "new_edges": [list(edge) for edge in sorted(new_edges)],
            "changed_sources": changed_sources,
            "changed_targets": changed_targets,
            "routing_changes": int(bool(changed_sources or changed_targets)),
        }
        component["component_sha256"] = digest(component)
        components.append(component)
    return tuple(components)


def context_identity(t: int, x: tuple[int, ...], y: tuple[int, ...],
                     deleted: tuple[tuple[int, int], ...]) -> dict[str, Any]:
    family = generate_factor_family(x, y, deleted)
    labelled_family = [
        [[0, source, target] for source, target in matching]
        for matching in family
    ]
    result: dict[str, Any] = {
        "ambient_side": t,
        "row_domains": [list(x), []],
        "column_domains": [list(y), []],
        "deleted_edges": [[0, source, target] for source, target in deleted],
        "required_edges": [],
        "feasible_states": len(family),
        "feasible_family_sha256": digest(labelled_family),
    }
    result["context_sha256"] = digest(result)
    return result


def exact_routing_change_manifest(
    p_raw: Any,
    h_raw: Any,
    x_raw: Iterable[int],
    y_raw: Iterable[int],
    deleted_raw: Iterable[Iterable[int]],
    old_raw: Iterable[Iterable[int]],
    new_raw: Iterable[Iterable[int]],
) -> dict[str, Any]:
    p = exact_int(p_raw, "prime", 2)
    h = exact_int(h_raw, "height", 1)
    require(all(p % divisor for divisor in range(2, int(p ** 0.5) + 1)),
            "prime: prime value required")
    t = p ** h
    x = exact_coordinates(x_raw, t, "sources")
    y = exact_coordinates(y_raw, t, "targets")
    require(len(x) == len(y), "factor must be balanced")
    d = len(x)
    require(d >= 2, "routing-change factor must be nontrivial")
    deleted = exact_deleted(deleted_raw, x, y)
    old = exact_matching(old_raw, x, y, deleted, "old_matching")
    new = exact_matching(new_raw, x, y, deleted, "new_matching")
    require(old != new, "routing-change transition requires distinct matchings")

    beta = min(delta(x, p, h), delta(y, p, h))
    require(beta < h, "nontrivial factor envelope must have beta < h")
    source_classes = {child_label(value, p, beta) for value in x}
    target_classes = {child_label(value, p, beta) for value in y}
    require(max(len(source_classes), len(target_classes)) >= 2,
            "canonical first child split missing")

    old_routing = routing_skeleton(old, x, y, p, beta)
    new_routing = routing_skeleton(new, x, y, p, beta)
    require(old_routing["routing_sha256"] != new_routing["routing_sha256"],
            "matchings do not change the routing skeleton")
    ax, ay = changed_vertices(old, new, x, y, p, beta)
    require(len(ax) == 0 or len(ax) >= 2,
            "changed source set has forbidden size one")
    require(len(ay) == 0 or len(ay) >= 2,
            "changed target set has forbidden size one")
    require(bool(ax or ay), "routing changed but no changed vertex recorded")

    entering, leaving = support_edges(old, new, ax, ay)
    require(len(entering) >= 2 and len(leaving) >= 2,
            "routing support must contain at least two edges each way")
    require(set(entering) <= set(new) - set(old),
            "entering routing support is not contained in new minus old")
    require(set(leaving) <= set(old) - set(new),
            "leaving routing support is not contained in old minus new")

    components = alternating_components(old, new, ax, ay)
    changed_components = tuple(component for component in components
                               if component["routing_changes"])
    changed_old = {tuple(edge) for component in changed_components
                   for edge in component["old_edges"]}
    changed_new = {tuple(edge) for component in changed_components
                   for edge in component["new_edges"]}
    require(set(entering) <= changed_new and set(leaving) <= changed_old,
            "routing support escapes routing-changing component union")

    context = context_identity(t, x, y, deleted)
    factor_label = digest({"ambient_side": t, "sources": x, "targets": y,
                           "deleted": deleted})
    envelope = {
        "prime": p,
        "height": h,
        "depth": beta,
        "side": t // (p ** beta),
        "source_residue": x[0] % (p ** beta) if beta else 0,
        "target_residue": y[0] % (p ** beta) if beta else 0,
        "source_child_labels": sorted(source_classes),
        "target_child_labels": sorted(target_classes),
    }
    envelope["envelope_sha256"] = digest(envelope)
    labels = {
        "operation_slot": "CMR671-CMR676-routing-skeleton-change",
        "owner": f"factor-owner:{factor_label}",
        "routing": f"{old_routing['routing_sha256']}->{new_routing['routing_sha256']}",
        "factor": f"factor:{factor_label}",
        "envelope": f"prefix-envelope:{envelope['envelope_sha256']}",
    }
    old_state: State = tuple((0, source, target) for source, target in old)
    new_state: State = tuple((0, source, target) for source, target in new)
    transition: dict[str, Any] = {
        "transition_kind": "routing-skeleton-change",
        "source_theorems": [
            "CMR656", "CMR657", "CMR659", "CMR671", "CMR672",
            "CMR673", "CMR674", "CMR675", "CMR676", "CMR2888", "CMR2889",
        ],
        "construction_labels": labels,
        "parent_context": context,
        "child_context": copy.deepcopy(context),
        "parent_state": [list(edge) for edge in old_state],
        "child_state": [list(edge) for edge in new_state],
        "factor_envelope": envelope,
        "old_routing_skeleton": old_routing,
        "new_routing_skeleton": new_routing,
        "changed_source_vertices": list(ax),
        "changed_target_vertices": list(ay),
        "entering_routing_support": [[0, source, target] for source, target in entering],
        "leaving_routing_support": [[0, source, target] for source, target in leaving],
        "alternating_components": list(components),
        "routing_changing_component_count": len(changed_components),
        "claims": {
            "factor_embedded_as_asymmetric_context": 1,
            "canonical_factor_envelope_recomputed": 1,
            "routing_skeletons_recomputed": 1,
            "routing_skeleton_changed": 1,
            "changed_vertex_conservation_exact": 1,
            "entering_leaving_support_exact": 1,
            "alternating_component_union_support_exact": 1,
            "parent_child_context_equal": 1,
            "parent_child_states_feasible": 1,
            "construction_labels_theorem_derived": 1,
            "routing_change_construction_ancestry_proved": 1,
            "all_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    transition["transition_sha256"] = digest(transition)
    return transition


def validate_manifest(manifest: Any, *args: Any) -> dict[str, int]:
    expected = exact_routing_change_manifest(*args)
    require(isinstance(manifest, dict) and manifest == expected,
            "routing-change ancestry manifest mismatch")
    return copy.deepcopy(expected["claims"])


def contract_manifest() -> dict[str, Any]:
    result: dict[str, Any] = {
        "version": 1,
        "rule_kind": "prime-power-routing-change-context-ancestry-v1",
        "source_theorems": [
            "CMR656", "CMR657", "CMR659", "CMR671", "CMR672",
            "CMR673", "CMR674", "CMR675", "CMR676", "CMR2888", "CMR2889",
        ],
        "claims": {
            "factor_embedded_as_asymmetric_context": 1,
            "canonical_factor_envelope_recomputed": 1,
            "routing_skeletons_recomputed": 1,
            "changed_vertex_conservation_exact": 1,
            "entering_leaving_support_exact": 1,
            "alternating_component_union_support_exact": 1,
            "construction_labels_theorem_derived": 1,
            "routing_change_construction_ancestry_proved": 1,
            "all_construction_ancestry_proved": 0,
            "global_transition_kind_bank_exhaustive": 0,
            "global_termination_proved": 0,
            "actual_global_parent_rule_complete": 0,
            "all_n_proved_by_checker": 0,
        },
    }
    result["contract_sha256"] = digest(result)
    return result


def validate_contract() -> dict[str, int]:
    manifest = contract_manifest()
    require(manifest["contract_sha256"] == EXPECTED_CONTRACT_SHA256,
            "built-in contract digest drift")
    return copy.deepcopy(manifest["claims"])


def finite_regression() -> dict[str, int]:
    transitions = factors = entering = leaving = multi_component = 0
    skeleton_pairs: set[tuple[str, str]] = set()
    for p, h in ((2, 2), (3, 1)):
        t = p ** h
        coordinates = tuple(range(t))
        for d in range(2, min(t, 3) + 1):
            for x in combinations(coordinates, d):
                for y in combinations(coordinates, d):
                    beta = min(delta(x, p, h), delta(y, p, h))
                    if beta >= h:
                        continue
                    if max(len({child_label(v, p, beta) for v in x}),
                           len({child_label(v, p, beta) for v in y})) < 2:
                        continue
                    family = generate_factor_family(x, y, ())
                    factor_had_change = False
                    for old in family:
                        for new in family:
                            if old >= new:
                                continue
                            old_r = routing_skeleton(old, x, y, p, beta)
                            new_r = routing_skeleton(new, x, y, p, beta)
                            if old_r["routing_sha256"] == new_r["routing_sha256"]:
                                continue
                            manifest = exact_routing_change_manifest(
                                p, h, x, y, (), old, new
                            )
                            factor_had_change = True
                            transitions += 1
                            entering += len(manifest["entering_routing_support"])
                            leaving += len(manifest["leaving_routing_support"])
                            multi_component += int(
                                manifest["routing_changing_component_count"] > 1
                            )
                            skeleton_pairs.add((
                                manifest["old_routing_skeleton"]["routing_sha256"],
                                manifest["new_routing_skeleton"]["routing_sha256"],
                            ))
                    factors += int(factor_had_change)
    witness = exact_routing_change_manifest(
        2, 2, (0, 1, 2, 3), (0, 1, 2, 3), (),
        ((0, 0), (1, 1), (2, 2), (3, 3)),
        ((0, 1), (1, 0), (2, 3), (3, 2)),
    )
    require(witness["routing_changing_component_count"] == 2,
            "two-component routing witness drift")
    multi_component += 1
    require(transitions > 0 and factors > 0, "routing regression produced no transitions")
    require(entering >= 2 * transitions and leaving >= 2 * transitions,
            "routing support incidence lower bound failed")
    return {
        "factor_hosts_with_routing_changes": factors,
        "routing_change_transitions": transitions,
        "entering_support_incidences": entering,
        "leaving_support_incidences": leaving,
        "distinct_ordered_skeleton_pairs": len(skeleton_pairs),
        "multi_component_routing_changes": multi_component,
    }


def mutation_tests() -> int:
    p, h = 2, 2
    x = y = (0, 1, 2, 3)
    old = ((0, 0), (1, 1), (2, 2), (3, 3))
    new = ((0, 1), (1, 0), (2, 3), (3, 2))
    good = exact_routing_change_manifest(p, h, x, y, (), old, new)
    bad_calls = [
        lambda: exact_routing_change_manifest(4, 1, x, y, (), old, new),
        lambda: exact_routing_change_manifest(p, h, (0, 0), y, (), old, new),
        lambda: exact_routing_change_manifest(p, h, x, y, ((0, 0),), old, new),
        lambda: exact_routing_change_manifest(p, h, x, y, (), old, old),
        lambda: exact_routing_change_manifest(
            p, h, x, y, (), old,
            ((0, 2), (1, 1), (2, 0), (3, 3)),
        ),
    ]
    rejected = 0
    for call in bad_calls:
        try:
            call()
        except (ValueError, RoutingChangeContextAncestryError):
            rejected += 1
        else:
            raise RoutingChangeContextAncestryError("malformed routing input accepted")
    corruptions = []
    bad_honesty = copy.deepcopy(good)
    bad_honesty["claims"]["all_construction_ancestry_proved"] = 1
    corruptions.append(bad_honesty)
    bad_support = copy.deepcopy(good)
    bad_support["entering_routing_support"].pop()
    corruptions.append(bad_support)
    bad_label = copy.deepcopy(good)
    bad_label["construction_labels"]["owner"] = "invented-owner"
    corruptions.append(bad_label)
    bad_seal = copy.deepcopy(good)
    bad_seal["transition_sha256"] = "0" * 64
    corruptions.append(bad_seal)
    for bad in corruptions:
        try:
            validate_manifest(bad, p, h, x, y, (), old, new)
        except RoutingChangeContextAncestryError:
            rejected += 1
        else:
            raise RoutingChangeContextAncestryError("corrupted routing manifest accepted")
    require(rejected == 9, "mutation rejection census drift")
    return rejected


def self_test() -> dict[str, Any]:
    return {
        **validate_contract(),
        **finite_regression(),
        "rejected_mutations": mutation_tests(),
        "contract_sha256": contract_manifest()["contract_sha256"],
    }


def main() -> None:
    print(json.dumps(self_test(), sort_keys=True))


if __name__ == "__main__":
    main()

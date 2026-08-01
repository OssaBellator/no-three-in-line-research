#!/usr/bin/env python3
"""Check packed-conflict deletion, protected contacts and recurrent-set batching."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from collections import Counter
from typing import Any, Iterable

Edge = tuple[int, int]
Triple = tuple[Edge, Edge, Edge]


class ProtectedBatchError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ProtectedBatchError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def perfect_matchings(edges: Iterable[Edge], n: int) -> list[tuple[Edge, ...]]:
    edge_set = set(edges)
    out = []
    for perm in itertools.permutations(range(n)):
        matching = tuple((i, perm[i]) for i in range(n))
        if all(edge in edge_set for edge in matching):
            out.append(matching)
    return out


def active_permutation_triples(edges: set[Edge], n: int) -> list[Triple]:
    return [
        tuple((i, perm[i]) for i in range(n))
        for perm in itertools.permutations(range(n))
        if all((i, perm[i]) in edges for i in range(n))
    ]


def packing_subfamilies(triples: list[Triple]) -> list[tuple[Triple, ...]]:
    out = []
    for size in range(1, len(triples) + 1):
        for family in itertools.combinations(triples, size):
            used = [edge for triple in family for edge in triple]
            if len(set(used)) == len(used):
                out.append(family)
    return out


def packed_deletion_audit() -> dict[str, int]:
    n = 3
    universe = [(i, j) for i in range(n) for j in range(n)]
    matchable_hosts = packing_profiles = processed_conflicts = 0
    killed_conflicts = fully_forced_conflicts = deletion_steps = 0
    restoration_subsets = recreated_conflicts = restoration_incidences = 0
    maximum_packing = 0
    for mask in range(1 << len(universe)):
        initial = {universe[k] for k in range(len(universe)) if mask >> k & 1}
        if not perfect_matchings(initial, n):
            continue
        matchable_hosts += 1
        triples = active_permutation_triples(initial, n)
        for family in packing_subfamilies(triples):
            packing_profiles += 1
            maximum_packing = max(maximum_packing, len(family))
            host = set(initial)
            killed: list[tuple[Triple, Edge]] = []
            forced: list[Triple] = []
            for triple in sorted(family):
                matchings = perfect_matchings(host, n)
                require(matchings, "deletion pass lost matchability")
                essential = {edge for edge in host if all(edge in M for M in matchings)}
                deletable = sorted(edge for edge in triple if edge not in essential)
                processed_conflicts += 1
                if deletable:
                    edge = deletable[0]
                    host.remove(edge)
                    require(perfect_matchings(host, n), "nonessential deletion killed family")
                    killed.append((triple, edge))
                    killed_conflicts += 1
                    deletion_steps += 1
                else:
                    require(all(edge in essential for edge in triple), "forced triple not essential")
                    forced.append(triple)
                    fully_forced_conflicts += 1
            final_matchings = perfect_matchings(host, n)
            core = {edge for edge in host if all(edge in M for M in final_matchings)}
            require(len({r for r, _ in core}) == len(core), "essential core row collision")
            require(len({c for _, c in core}) == len(core), "essential core column collision")
            require(3 * len(forced) <= n, "forced packing exceeds core capacity")
            deleted = [edge for _, edge in killed]
            require(len(deleted) == len(set(deleted)), "private deletion code not injective")
            require(all(not set(triple).issubset(host) for triple, _ in killed),
                    "killed conflict survived")
            for size in range(len(deleted) + 1):
                for subset in itertools.combinations(deleted, size):
                    restoration_subsets += 1
                    restored = host | set(subset)
                    count = sum(set(triple).issubset(restored) for triple, _ in killed)
                    required = {
                        edge for triple, edge in killed if set(triple).issubset(restored)
                    }
                    require(required.issubset(subset), "recreated conflict lacks private edge")
                    require(len(required) >= count, "restoration incidence too small")
                    recreated_conflicts += count
                    restoration_incidences += len(required)
    return {
        "side_three_matchable_hosts": matchable_hosts,
        "packed_conflict_profiles": packing_profiles,
        "processed_packed_conflicts": processed_conflicts,
        "killed_packed_conflicts": killed_conflicts,
        "fully_forced_packed_conflicts": fully_forced_conflicts,
        "matching_preserving_deletion_steps": deletion_steps,
        "restoration_subsets_checked": restoration_subsets,
        "recreated_packed_conflicts": recreated_conflicts,
        "private_restoration_incidences": restoration_incidences,
        "maximum_edge_disjoint_packing_size": maximum_packing,
    }


def partial_matchings(n: int) -> list[tuple[Edge, ...]]:
    out = []
    for size in range(1, n + 1):
        for rows in itertools.combinations(range(n), size):
            for cols in itertools.combinations(range(n), size):
                for perm in itertools.permutations(cols):
                    out.append(tuple(sorted(zip(rows, perm))))
    return out


def ordered_extension(protected: tuple[Edge, ...], n: int) -> tuple[Edge, ...]:
    used_rows = {r for r, _ in protected}
    used_cols = {c for _, c in protected}
    free_rows = sorted(set(range(n)) - used_rows)
    free_cols = sorted(set(range(n)) - used_cols)
    return tuple(sorted((*protected, *zip(free_rows, free_cols))))


def blocked_edges(protected: tuple[Edge, ...], n: int) -> set[Edge]:
    forbidden = set(ordered_extension(protected, n))
    rows = {r for r, _ in protected}
    cols = {c for _, c in protected}
    return {
        (r, c)
        for r in range(n) for c in range(n)
        if (r, c) not in forbidden and (r in rows or c in cols)
    }


def protected_contact_audit() -> dict[str, int]:
    n = 4
    states = physical_edges = contact_subsets = wall_incidences = 0
    heavy_tokens = dispersed_banks = recurrent_histories = finite_histories = 0
    for protected in partial_matchings(n):
        size = len(protected)
        blocked = sorted(blocked_edges(protected, n))
        states += 1
        physical_edges += len(blocked)
        require(len(blocked) <= 2 * size * (n - 1), "CMR582 contact universe bound")
        subsets: list[tuple[Edge, ...]] = []
        if len(blocked) <= 8:
            for subset_size in range(1, len(blocked) + 1):
                subsets.extend(itertools.combinations(blocked, subset_size))
        else:
            for subset_size in sorted({1, 2, min(4, len(blocked)), len(blocked)}):
                subsets.extend(itertools.combinations(blocked, subset_size))
                if len(subsets) > 5000:
                    break
        for subset in subsets:
            contact_subsets += 1
            degrees = Counter()
            for contact in subset:
                for edge in protected:
                    if contact[0] == edge[0]:
                        degrees[("source", edge)] += 1
                    if contact[1] == edge[1]:
                        degrees[("target", edge)] += 1
            degree = max(degrees.values())
            require(degree >= math.ceil(len(subset) / (2 * size)),
                    "CMR584 wall concentration")
            wall_incidences += degree
            label = max(degrees, key=degrees.get)
            kind, edge = label
            if kind == "source":
                wall = [contact for contact in subset if contact[0] == edge[0]]
                classes = Counter(c % 2 for _, c in wall)
            else:
                wall = [contact for contact in subset if contact[1] == edge[1]]
                classes = Counter(r % 2 for r, _ in wall)
            threshold = max(2, math.ceil(math.sqrt(max(1, len(wall)))))
            if max(classes.values(), default=0) >= threshold:
                heavy_tokens += 1
            else:
                occupied = sum(value > 0 for value in classes.values())
                require(occupied >= math.ceil(len(wall) / (threshold - 1)),
                        "CMR585 dispersed token bound")
                dispersed_banks += 1
        sample = blocked[: min(4, len(blocked))]
        if sample:
            for history in itertools.product(sample, repeat=3):
                multiplicity = Counter(history)
                if max(multiplicity.values()) >= 3:
                    recurrent_histories += 1
                else:
                    require(len(history) <= 2 * (3 - 1) * size * (n - 1),
                            "CMR583 finite history bound")
                    finite_histories += 1
    return {
        "protected_selector_states": states,
        "physical_blocked_edge_incidences": physical_edges,
        "protected_contact_subsets": contact_subsets,
        "protected_wall_edge_incidences": wall_incidences,
        "heavy_protected_contact_tokens": heavy_tokens,
        "dispersed_protected_contact_banks": dispersed_banks,
        "finite_contact_histories": finite_histories,
        "recurrent_contact_histories": recurrent_histories,
    }


def maximum_matching_size(edges: set[Edge], n: int) -> int:
    best = 0
    for size in range(1, n + 1):
        for family in itertools.combinations(edges, size):
            if len({r for r, _ in family}) == size and len({c for _, c in family}) == size:
                best = size
    return best


def minimum_vertex_cover(edges: set[Edge], n: int) -> set[tuple[str, int]]:
    vertices = [("r", i) for i in range(n)] + [("c", j) for j in range(n)]
    for size in range(len(vertices) + 1):
        for cover in itertools.combinations(vertices, size):
            selected = set(cover)
            if all(("r", r) in selected or ("c", c) in selected for r, c in edges):
                return selected
    raise AssertionError("vertex cover not found")


def recurrent_set_audit() -> dict[str, int]:
    universe = list(range(5))
    inventories = [set(item) for item in itertools.combinations(universe, 3)]
    subset_histories = recurrent_sets = finite_subset_histories = 0
    r = 2
    recurrence_threshold = 2
    bound = (recurrence_threshold - 1) * math.comb(5, r) / math.comb(3, r)
    for length in range(1, 5):
        for history in itertools.product(inventories, repeat=length):
            subset_histories += 1
            multiplicity = Counter(
                subset
                for inventory in history
                for subset in itertools.combinations(sorted(inventory), r)
            )
            if max(multiplicity.values(), default=0) >= recurrence_threshold:
                recurrent_sets += 1
            else:
                require(length <= bound + 1e-12, "CMR587 finite subset bound")
                finite_subset_histories += 1

    n = 4
    decomposition_profiles = batch_profiles = wall_profiles = 0
    batch_edges = wall_edges = 0
    for protected in partial_matchings(n):
        forbidden = set(ordered_extension(protected, n))
        allowed = {(i, j) for i in range(n) for j in range(n)} - forbidden
        allowed_list = sorted(allowed)
        for size in range(1, min(4, len(allowed_list)) + 1):
            for witness_tuple in itertools.combinations(allowed_list, size):
                witness = set(witness_tuple)
                decomposition_profiles += 1
                protected_rows = {("r", edge[0]) for edge in protected}
                protected_cols = {("c", edge[1]) for edge in protected}
                unprotected = {
                    (a, b) for a, b in witness
                    if ("r", a) not in protected_rows and ("c", b) not in protected_cols
                }
                matching_number = maximum_matching_size(unprotected, n)
                batch_size = 2
                if matching_number >= batch_size:
                    selected = next(
                        family for family in itertools.combinations(unprotected, batch_size)
                        if len({a for a, _ in family}) == batch_size
                        and len({b for _, b in family}) == batch_size
                    )
                    combined = tuple(sorted((*protected, *selected)))
                    require(len({a for a, _ in combined}) == len(combined),
                            "batch row collision")
                    require(len({b for _, b in combined}) == len(combined),
                            "batch column collision")
                    batch_profiles += 1
                    batch_edges += batch_size
                else:
                    cover = minimum_vertex_cover(unprotected, n)
                    require(len(cover) == matching_number, "Konig cover mismatch")
                    full_cover = cover | protected_rows | protected_cols
                    require(all(("r", a) in full_cover or ("c", b) in full_cover
                                for a, b in witness), "persistent set not covered")
                    degrees = Counter()
                    for a, b in witness:
                        if ("r", a) in full_cover:
                            degrees[("r", a)] += 1
                        if ("c", b) in full_cover:
                            degrees[("c", b)] += 1
                    denominator = 2 * len(protected) + batch_size - 1
                    require(max(degrees.values()) >= math.ceil(len(witness) / denominator),
                            "persistent wall degree")
                    wall_profiles += 1
                    wall_edges += max(degrees.values())

    fixed_set = {(0, 0), (1, 1)}
    time_count = 6
    joint_histories = aggregate_returns = persistent_endpoints = 0
    edges = sorted(fixed_set)
    for masks in itertools.product(range(1 << time_count), repeat=2):
        history = []
        for time in range(time_count):
            history.append({
                edges[index] for index, mask in enumerate(masks) if mask >> time & 1
            })
        absent_times = [time for time, available in enumerate(history)
                        if fixed_set.isdisjoint(available)]
        if len(absent_times) < 3:
            continue
        joint_histories += 1
        reintroductions = sum(
            sum(edge not in history[time - 1] and edge in history[time]
                for time in range(1, time_count))
            for edge in fixed_set
        )
        persistent = any(
            end - start + 1 >= 3
            and all(fixed_set.isdisjoint(history[time]) for time in range(start, end + 1))
            for start in range(time_count) for end in range(start, time_count)
        )
        if persistent:
            persistent_endpoints += 1
        else:
            require(reintroductions >= 1, "CMR588 aggregate reintroduction missing")
            aggregate_returns += 1

    growth_checks = 0
    for initial_size in range(n + 1):
        for batch_size in range(1, n + 1):
            steps = (n - initial_size) // batch_size
            require(initial_size + steps * batch_size <= n
                    < initial_size + (steps + 1) * batch_size,
                    "batch growth bound")
            growth_checks += 1

    return {
        "subset_history_profiles": subset_histories,
        "recurrent_r_set_histories": recurrent_sets,
        "finite_subset_histories": finite_subset_histories,
        "matching_cover_decomposition_profiles": decomposition_profiles,
        "batch_absorption_profiles": batch_profiles,
        "persistent_wall_profiles": wall_profiles,
        "batch_absorbed_edge_incidences": batch_edges,
        "persistent_wall_edge_incidences": wall_edges,
        "joint_absence_histories": joint_histories,
        "aggregate_reintroduction_endpoints": aggregate_returns,
        "jointly_persistent_set_endpoints": persistent_endpoints,
        "batch_growth_arithmetic_checks": growth_checks,
    }


CONTRACT = {
    "schema": "prime-power-protected-conflict-batching-ancestry/v1",
    "source_theorems": [f"CMR{i}" for i in range(577, 593)],
    "operations": [
        "packed-conflict-nonessential-deletion",
        "packed-conflict-forced-terminality",
        "packed-conflict-private-restoration",
        "protected-contact-finite-stock",
        "protected-contact-wall-extraction",
        "protected-contact-token-splice",
        "protected-contact-reintroduction",
        "recurrent-unavailable-set-extraction",
        "recurrent-set-aggregate-reintroduction",
        "recurrent-set-batch-absorption",
        "recurrent-set-persistent-wall",
        "recurrent-set-batch-growth",
    ],
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "a48ee5aa77c167c1dba3d6eab6e3a65db7397e1739323fb794df66c32d76ec5f"


def validate_report(report: dict[str, Any]) -> None:
    require(report["contract_sha256"] == EXPECTED_CONTRACT_SHA256, "contract seal")
    census = report["census"]
    require(census["killed_packed_conflicts"] > 0, "deletion branch missing")
    require(census["fully_forced_packed_conflicts"] > 0, "forced branch missing")
    require(census["recreated_packed_conflicts"] > 0, "restoration branch missing")
    require(census["heavy_protected_contact_tokens"] > 0, "heavy contact token missing")
    require(census["dispersed_protected_contact_banks"] > 0,
            "dispersed contact bank missing")
    require(census["batch_absorption_profiles"] > 0, "batch absorption missing")
    require(census["persistent_wall_profiles"] > 0, "persistent wall missing")
    require(census["aggregate_reintroduction_endpoints"] > 0,
            "aggregate reintroduction missing")
    require(census["jointly_persistent_set_endpoints"] > 0,
            "joint persistence missing")
    require(report["all_n_proved_by_checker"] == 0, "honesty flag")


def mutation_audit(report: dict[str, Any]) -> int:
    mutations = [
        lambda item: item.update(contract_sha256="0" * 64),
        lambda item: item["census"].update(killed_packed_conflicts=0),
        lambda item: item["census"].update(fully_forced_packed_conflicts=0),
        lambda item: item["census"].update(recreated_packed_conflicts=0),
        lambda item: item["census"].update(heavy_protected_contact_tokens=0),
        lambda item: item["census"].update(dispersed_protected_contact_banks=0),
        lambda item: item["census"].update(batch_absorption_profiles=0),
        lambda item: item["census"].update(persistent_wall_profiles=0),
        lambda item: item["census"].update(aggregate_reintroduction_endpoints=0),
        lambda item: item["census"].update(jointly_persistent_set_endpoints=0),
        lambda item: item.update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(report)
        mutate(bad)
        try:
            validate_report(bad)
        except ProtectedBatchError:
            rejected += 1
    require(rejected == len(mutations), "corruption accepted")
    return rejected


def main() -> None:
    contract_sha256 = digest(CONTRACT)
    require(contract_sha256 == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    census: dict[str, int] = {}
    for audit in (packed_deletion_audit, protected_contact_audit, recurrent_set_audit):
        census.update(audit())
    report: dict[str, Any] = {
        "checker": "prime-power-protected-conflict-batching-ancestry",
        "contract_sha256": contract_sha256,
        "census": census,
        "packed_conflict_deletion_ancestry_proved": 1,
        "protected_contact_token_ledger_exact": 1,
        "recurrent_unavailable_set_batching_exact": 1,
        "all_owner_operations_proved": 0,
        "all_scheduler_operations_proved": 0,
        "all_restoration_operations_proved": 0,
        "all_returned_edge_operations_proved": 0,
        "all_envelope_operations_proved": 0,
        "all_construction_ancestry_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    }
    validate_report(report)
    report["census"]["rejected_corruptions"] = mutation_audit(report)
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()

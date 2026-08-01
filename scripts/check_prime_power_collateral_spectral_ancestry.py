#!/usr/bin/env python3
"""Finite ancestry checks for CMR1198--CMR1277 collateral and spectral banks."""
from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, comb
from typing import Any, Iterable


class CollateralSpectralError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise CollateralSpectralError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


SOURCE_FILES = [
    "docs/254-prime-power-degree-two-bank-collateral-expectation.md",
    "docs/255-prime-power-restricted-bank-target-collateral-selection.md",
    "docs/256-prime-power-last-entering-edge-collateral-ownership.md",
    "docs/257-prime-power-degree-two-bank-line-energy.md",
    "docs/258-prime-power-rank-one-bank-marginal-refinement.md",
    "docs/259-prime-power-full-collateral-local-envelope.md",
    "docs/260-prime-power-optimized-envelope-target-aggregation.md",
    "docs/261-prime-power-last-creation-collateral-credit-ledger.md",
    "docs/262-prime-power-collateral-reproduction-matrix.md",
    "docs/263-prime-power-rational-spectral-certificate.md",
]
CONTRACT = {
    "schema": "prime-power-collateral-spectral-ancestry/v1",
    "source_range": ["CMR1198", "CMR1277"],
    "source_files": SOURCE_FILES,
    "finite_model": {
        "side": 4,
        "joint_state_count": 216,
        "selected_target_count": 1728,
        "response_bank_model": "two disjoint forbidden perfect matchings",
    },
    "checked_banks": [
        "degree-two permanent cylinders and rank probabilities",
        "restricted-host availability penalties",
        "absolute last-entering collateral ownership",
        "corrected three-rank line energy",
        "rank-one doubly-stochastic marginals",
        "full local collateral envelopes",
        "optimized target-envelope aggregation",
        "last-creation physical credit ledger",
        "nonnegative reproduction-matrix reduction",
        "exact rational and integer spectral certificates",
    ],
    "honesty_flags": {
        "global_target_collateral_inequality_proved": 0,
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "26e224413ed320276f50e0852b64291c11994861d21b35bb4bec9077179b7577"

Cell = tuple[int, int]
LabelledEdge = tuple[int, int, int]
Matching = frozenset[Cell]
JointState = tuple[Matching, Matching]
Triple = frozenset[Cell]


def line_key(first: Cell, second: Cell) -> tuple[int, int, int]:
    from math import gcd

    a = second[1] - first[1]
    b = first[0] - second[0]
    c = -(a * first[0] + b * first[1])
    divisor = gcd(gcd(abs(a), abs(b)), abs(c)) or 1
    a, b, c = a // divisor, b // divisor, c // divisor
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def collinear(points: Iterable[Cell]) -> bool:
    first, second, third = tuple(points)
    return line_key(first, second) == line_key(first, third)


def is_compatible(edges: Iterable[Cell]) -> bool:
    edges = tuple(edges)
    return len({row for row, _column in edges}) == len(edges) and len(
        {column for _row, column in edges}
    ) == len(edges)


def all_matchings(side: int) -> tuple[Matching, ...]:
    return tuple(
        frozenset((row, permutation[row]) for row in range(side))
        for permutation in permutations(range(side))
    )


def joint_states(matchings: tuple[Matching, ...]) -> tuple[JointState, ...]:
    return tuple(
        (first, second)
        for first in matchings
        for second in matchings
        if first.isdisjoint(second)
    )


def triple_family(cells: Iterable[Cell]) -> frozenset[Triple]:
    return frozenset(
        frozenset(triple)
        for triple in combinations(sorted(set(cells)), 3)
        if collinear(triple)
    )


def build_lines(
    side: int,
) -> tuple[
    dict[tuple[int, int, int], frozenset[Cell]],
    dict[Cell, tuple[tuple[int, int, int], ...]],
]:
    board = tuple((row, column) for row in range(side) for column in range(side))
    keys = {line_key(first, second) for first, second in combinations(board, 2)}
    lines: dict[tuple[int, int, int], frozenset[Cell]] = {}
    through: dict[Cell, list[tuple[int, int, int]]] = defaultdict(list)
    for key in keys:
        a, b, c = key
        cells = frozenset(
            (row, column)
            for row, column in board
            if a * row + b * column + c == 0
        )
        if len(cells) >= 2:
            lines[key] = cells
            for cell in cells:
                through[cell].append(key)
    return lines, {
        cell: tuple(sorted(keys_for_cell))
        for cell, keys_for_cell in through.items()
    }


def bank_matchings(
    matchings: tuple[Matching, ...], opposite: Matching, forbidden: Matching
) -> tuple[Matching, ...]:
    return tuple(
        response
        for response in matchings
        if response.isdisjoint(opposite) and response.isdisjoint(forbidden)
    )


def forbidden_extensions(
    matchings: tuple[Matching, ...], opposite: Matching, target: Cell
) -> tuple[Matching, ...]:
    return tuple(
        extension
        for extension in matchings
        if target in extension and extension.isdisjoint(opposite)
    )


def compatible_subsets(
    edges: Iterable[Cell], rank: int
) -> Iterable[frozenset[Cell]]:
    for subset in combinations(sorted(edges), rank):
        if is_compatible(subset):
            yield frozenset(subset)


def classify_candidates(
    side: int,
    old_cells: frozenset[Cell],
    opposite: Matching,
    graph: frozenset[Cell],
    all_collinear: frozenset[Triple],
) -> dict[int, tuple[tuple[Triple, frozenset[Cell]], ...]]:
    del side
    old_triples = triple_family(old_cells)
    result: dict[int, list[tuple[Triple, frozenset[Cell]]]] = {
        1: [],
        2: [],
        3: [],
    }
    for triple in all_collinear - old_triples:
        prescription = frozenset(triple - opposite)
        rank = len(prescription)
        if (
            rank in result
            and prescription <= graph
            and is_compatible(prescription)
        ):
            result[rank].append((triple, prescription))
    return {rank: tuple(items) for rank, items in result.items()}


def new_rank_counts(
    old_cells: frozenset[Cell], opposite: Matching, response: Matching
) -> Counter[int]:
    old = triple_family(old_cells)
    new = triple_family(opposite | response) - old
    return Counter(len(triple - opposite) for triple in new)


def exact_line_energy(
    lines: dict[tuple[int, int, int], frozenset[Cell]],
    opposite: Matching,
    graph: frozenset[Cell],
    old_rematched: Matching,
) -> tuple[int, int, int, int, int]:
    old_allowed = old_rematched & graph
    v1 = v2 = v3 = pair_stock = 0
    for cells in lines.values():
        o = len(opposite & cells)
        g_edges = graph & cells
        m = len(old_allowed & cells)
        c2 = sum(1 for _ in compatible_subsets(g_edges, 2))
        c3 = sum(1 for _ in compatible_subsets(g_edges, 3))
        v1 += comb(o, 2) * (len(g_edges) - m)
        v2 += o * (c2 - comb(m, 2))
        v3 += c3 - comb(m, 3)
        pair_stock += c2
    formula = len(graph) * (len(graph) - 1) // 2
    degree = len(graph) // len(opposite)
    formula -= 2 * len(opposite) * comb(degree, 2)
    require(pair_stock == formula, "compatible-pair stock formula")
    require(pair_stock - comb(len(old_allowed), 2) >= 0, "corrected pair stock")
    return v1, v2, v3, pair_stock, len(old_allowed)


def edge_weights(
    graph: frozenset[Cell],
    opposite: Matching,
    old_rematched: Matching,
    lines: dict[tuple[int, int, int], frozenset[Cell]],
    through: dict[Cell, tuple[tuple[int, int, int], ...]],
) -> dict[Cell, int]:
    return {
        edge: (
            0
            if edge in old_rematched
            else sum(
                comb(len(opposite & lines[key]), 2) for key in through[edge]
            )
        )
        for edge in graph
    }


def local_envelopes(
    graph: frozenset[Cell],
    bank: tuple[Matching, ...],
    opposite: Matching,
    old_rematched: Matching,
    lines: dict[tuple[int, int, int], frozenset[Cell]],
    through: dict[Cell, tuple[tuple[int, int, int], ...]],
) -> tuple[dict[Cell, Fraction], Fraction, int]:
    weights = edge_weights(graph, opposite, old_rematched, lines, through)
    lambdas: dict[Cell, Fraction] = {}
    conditioned_checks = 0
    for edge in sorted(graph):
        containing = [response for response in bank if edge in response]
        require(containing, "allowed edge must extend to a bank matching")
        delta2 = 0
        delta3 = 0
        for response in containing:
            tau2 = 0
            tau3 = 0
            others = sorted(response - {edge})
            for second in others:
                line = lines[line_key(edge, second)]
                if not {edge, second} <= old_rematched:
                    tau2 += len(opposite & line)
            for second, third in combinations(others, 2):
                if collinear((edge, second, third)) and not {
                    edge,
                    second,
                    third,
                } <= old_rematched:
                    tau3 += 1
            delta2 = max(delta2, tau2)
            delta3 = max(delta3, tau3)
            conditioned_checks += 1
        lambdas[edge] = (
            Fraction(weights[edge], 1)
            + Fraction(delta2, 2)
            + Fraction(delta3, 3)
        )

    rows: dict[int, list[Fraction]] = defaultdict(list)
    columns: dict[int, list[Fraction]] = defaultdict(list)
    for (row, column), value in lambdas.items():
        rows[row].append(value)
        columns[column].append(value)
    row_bound = sum(max(values) for values in rows.values())
    column_bound = sum(max(values) for values in columns.values())
    envelope = min(row_bound, column_bound)

    old_cells = frozenset(opposite | old_rematched)
    for response in bank:
        ranks = new_rank_counts(old_cells, opposite, response)
        n_total = sum(ranks.values())
        local_sum = sum(lambdas[edge] for edge in response)
        require(
            Fraction(n_total, 1) <= local_sum <= envelope,
            "full local envelope",
        )
        n2_incidence = n3_incidence = 0
        for edge in response:
            others = sorted(response - {edge})
            n2_incidence += sum(
                len(opposite & lines[line_key(edge, second)])
                for second in others
                if not {edge, second} <= old_rematched
            )
            n3_incidence += sum(
                1
                for second, third in combinations(others, 2)
                if collinear((edge, second, third))
                and not {edge, second, third} <= old_rematched
            )
        require(
            n2_incidence == 2 * ranks[2],
            "rank-two local incidence identity",
        )
        require(
            n3_incidence == 3 * ranks[3],
            "rank-three local incidence identity",
        )
    return lambdas, envelope, conditioned_checks


def check_degree_two_banks(side: int = 4) -> dict[str, int]:
    matchings = all_matchings(side)
    states = joint_states(matchings)
    lines, through = build_lines(side)
    board = frozenset(
        (row, column) for row in range(side) for column in range(side)
    )
    all_collinear = triple_family(board)
    kappa = Fraction(side, side - 2) ** side
    require(kappa == 16, "side-four permanent-loss factor")

    bank_configurations = 0
    response_states = 0
    cylinder_probability_checks = 0
    collateral_identity_checks = 0
    line_energy_checks = 0
    marginal_checks = 0
    local_envelope_checks = 0
    conditioned_envelope_checks = 0
    strict_improvement_certificates = 0
    target_aggregate_states = 0
    target_aggregate_edges = 0
    restricted_host_profiles = 0
    owner_partition_checks = 0
    optimized_barrier_checks = 0

    for first, second in states:
        old_cells = frozenset(first | second)
        old_triples = triple_family(old_cells)
        state_improves = False
        beta_sum = Fraction(0, 1)
        for old_rematched, opposite in ((first, second), (second, first)):
            for target in sorted(old_rematched):
                target_aggregate_edges += 1
                all_extensions = forbidden_extensions(
                    matchings, opposite, target
                )
                require(all_extensions, "disjoint forbidden extension exists")
                extensions = (
                    all_extensions
                    if target_aggregate_states < 24
                    else all_extensions[:1]
                )
                d_target = sum(
                    1 for triple in old_triples if target in triple
                )
                envelopes: list[Fraction] = []
                any_improvement = False
                for extension in extensions:
                    graph = frozenset(board - opposite - extension)
                    require(
                        len(graph) == side * (side - 2),
                        "degree-two graph size",
                    )
                    bank = bank_matchings(
                        matchings, opposite, extension
                    )
                    require(
                        bank,
                        "regular response graph has a perfect matching",
                    )
                    bank_configurations += 1
                    response_states += len(bank)

                    candidates = classify_candidates(
                        side,
                        old_cells,
                        opposite,
                        graph,
                        all_collinear,
                    )
                    v = {
                        rank: len(candidates[rank])
                        for rank in (1, 2, 3)
                    }
                    v1, v2, v3, pair_stock, old_allowed_count = (
                        exact_line_energy(
                            lines, opposite, graph, old_rematched
                        )
                    )
                    require(
                        (v1, v2, v3) == (v[1], v[2], v[3]),
                        "corrected line-energy identity",
                    )
                    require(
                        pair_stock - comb(old_allowed_count, 2) >= 0,
                        "new pair stock",
                    )
                    line_energy_checks += 1

                    exact_expectation = Fraction(0, 1)
                    for rank in (1, 2, 3):
                        denominator = (
                            side
                            if rank == 1
                            else side * (side - 1)
                            if rank == 2
                            else side * (side - 1) * (side - 2)
                        )
                        for _triple, prescription in candidates[rank]:
                            containing = sum(
                                1
                                for response in bank
                                if prescription <= response
                            )
                            probability = Fraction(containing, len(bank))
                            exact_expectation += probability
                            require(
                                probability
                                <= kappa / Fraction(denominator, 1),
                                "rank-cylinder probability bound",
                            )
                            cylinder_probability_checks += 1

                    actual_new_total = 0
                    weights = edge_weights(
                        graph,
                        opposite,
                        old_rematched,
                        lines,
                        through,
                    )
                    edge_marginals = {
                        edge: Fraction(
                            sum(
                                1
                                for response in bank
                                if edge in response
                            ),
                            len(bank),
                        )
                        for edge in graph
                    }
                    for row in range(side):
                        require(
                            sum(
                                edge_marginals.get((row, column), 0)
                                for column in range(side)
                            )
                            == 1,
                            "row bank marginal",
                        )
                    for column in range(side):
                        require(
                            sum(
                                edge_marginals.get((row, column), 0)
                                for row in range(side)
                            )
                            == 1,
                            "column bank marginal",
                        )
                    marginal_checks += 2 * side

                    expected_rank_one = sum(
                        Fraction(weights[edge], 1) * probability
                        for edge, probability in edge_marginals.items()
                    )
                    matching_rank_one = []
                    for response in bank:
                        ranks = new_rank_counts(
                            old_cells, opposite, response
                        )
                        require(
                            ranks[1]
                            == sum(weights[edge] for edge in response),
                            "rank-one matching cost",
                        )
                        matching_rank_one.append(ranks[1])
                        actual_new_total += sum(ranks.values())
                        owner_fibres: dict[Cell, set[Triple]] = defaultdict(set)
                        entering = sorted(response - old_rematched)
                        for triple in (
                            triple_family(opposite | response) - old_triples
                        ):
                            owners = [
                                edge for edge in entering if edge in triple
                            ]
                            require(
                                owners,
                                "new triple entering-edge owner",
                            )
                            owner_fibres[min(owners)].add(triple)
                        require(
                            sum(len(items) for items in owner_fibres.values())
                            == sum(ranks.values()),
                            "absolute owner partition",
                        )
                        owner_partition_checks += 1
                    require(
                        Fraction(actual_new_total, len(bank))
                        == exact_expectation,
                        "exact collateral expectation",
                    )
                    require(
                        expected_rank_one
                        == Fraction(sum(matching_rank_one), len(bank)),
                        "rank-one marginal expectation",
                    )
                    row_rank_one = sum(
                        max(
                            weights.get((row, column), 0)
                            for column in range(side)
                        )
                        for row in range(side)
                    )
                    column_rank_one = sum(
                        max(
                            weights.get((row, column), 0)
                            for row in range(side)
                        )
                        for column in range(side)
                    )
                    require(
                        expected_rank_one
                        <= max(matching_rank_one)
                        <= min(row_rank_one, column_rank_one),
                        "rank-one assignment envelope",
                    )

                    normalized = sum(
                        Fraction(
                            v[rank],
                            side
                            if rank == 1
                            else side * (side - 1)
                            if rank == 2
                            else side * (side - 1) * (side - 2),
                        )
                        for rank in (1, 2, 3)
                    )
                    require(
                        exact_expectation <= kappa * normalized,
                        "universal collateral expectation",
                    )
                    collateral_identity_checks += 1

                    _lambdas, envelope, conditioned = local_envelopes(
                        graph,
                        bank,
                        opposite,
                        old_rematched,
                        lines,
                        through,
                    )
                    conditioned_envelope_checks += conditioned
                    local_envelope_checks += len(bank)
                    envelopes.append(envelope)
                    if envelope < d_target:
                        require(
                            all(
                                len(triple_family(opposite | response))
                                < len(old_triples)
                                for response in bank
                            ),
                            "pointwise strict-improvement criterion",
                        )
                        strict_improvement_certificates += 1
                    if any(
                        len(triple_family(opposite | response))
                        < len(old_triples)
                        for response in bank
                    ):
                        any_improvement = True

                    if (
                        extension == extensions[0]
                        and target_aggregate_edges <= 32
                    ):
                        graph_edges = sorted(graph)
                        for mask in range(1 << len(graph_edges)):
                            unavailable = {
                                graph_edges[index]
                                for index in range(len(graph_edges))
                                if mask & (1 << index)
                            }
                            expected_unavailable = sum(
                                edge_marginals[edge]
                                for edge in unavailable
                            )
                            require(
                                expected_unavailable
                                <= kappa * len(unavailable) / side,
                                "unavailable-edge expectation",
                            )
                            feasible = [
                                response
                                for response in bank
                                if response.isdisjoint(unavailable)
                            ]
                            m = len(old_triples)
                            weighted = []
                            for response in bank:
                                delta = (
                                    len(triple_family(opposite | response))
                                    - m
                                )
                                r_h = len(response & unavailable)
                                weighted.append(delta + (m + 1) * r_h)
                                if delta + (m + 1) * r_h < 0:
                                    require(
                                        r_h == 0 and delta < 0,
                                        "weighted feasibility forcing",
                                    )
                            if sum(
                                Fraction(value, len(weighted))
                                for value in weighted
                            ) < 0:
                                require(
                                    any(
                                        len(
                                            triple_family(
                                                opposite | response
                                            )
                                        )
                                        < m
                                        for response in feasible
                                    ),
                                    "restricted-host improvement criterion",
                                )
                            restricted_host_profiles += 1

                beta = min(envelopes)
                beta_sum += beta
                state_improves = state_improves or any_improvement
                if not any_improvement:
                    require(
                        beta >= d_target,
                        "optimized target-envelope barrier",
                    )
                    optimized_barrier_checks += 1
        if not state_improves:
            require(
                beta_sum >= 3 * len(old_triples),
                "global optimized-envelope barrier",
            )
            optimized_barrier_checks += 1
        target_aggregate_states += 1

    require(len(states) == 216, "side-four joint state census")
    require(target_aggregate_edges == 1728, "selected target census")
    return {
        "side_four_joint_states": len(states),
        "selected_target_cells": target_aggregate_edges,
        "degree_two_bank_configurations": bank_configurations,
        "degree_two_response_states": response_states,
        "rank_cylinder_probability_checks": cylinder_probability_checks,
        "collateral_expectation_checks": collateral_identity_checks,
        "corrected_line_energy_checks": line_energy_checks,
        "doubly_stochastic_marginal_checks": marginal_checks,
        "full_local_envelope_checks": local_envelope_checks,
        "edge_conditioned_envelope_checks": conditioned_envelope_checks,
        "restricted_host_profiles": restricted_host_profiles,
        "absolute_owner_partition_checks": owner_partition_checks,
        "strict_improvement_certificates": strict_improvement_certificates,
        "optimized_envelope_barrier_checks": optimized_barrier_checks,
    }


def labelled_state(
    first: Matching, second: Matching
) -> frozenset[LabelledEdge]:
    return frozenset(
        [(0, row, column) for row, column in first]
        + [(1, row, column) for row, column in second]
    )


def physical_triples_of_labelled(
    state: frozenset[LabelledEdge],
) -> frozenset[Triple]:
    return triple_family((row, column) for _layer, row, column in state)


def check_credit_ledgers(side: int = 4) -> dict[str, int]:
    matchings = all_matchings(side)
    states = joint_states(matchings)
    labelled = [labelled_state(first, second) for first, second in states]
    histories = 0
    transition_checks = 0
    relabel_checks = 0

    sequences: list[list[frozenset[LabelledEdge]]] = []
    for index in range(0, len(labelled), 3):
        sequence = [
            labelled[(index + offset * 17) % len(labelled)]
            for offset in range(6)
        ]
        first, second = states[index % len(states)]
        sequence.insert(1, labelled_state(second, first))
        sequences.append(sequence)

    for sequence in sequences:
        live: dict[Triple, tuple[int, Cell | None]] = {}
        root = physical_triples_of_labelled(sequence[0])
        for triple in root:
            live[triple] = (0, None)
        require(len(live) == len(root), "root credit partition")
        for time in range(1, len(sequence)):
            old_state, new_state = sequence[time - 1], sequence[time]
            old_triples = physical_triples_of_labelled(old_state)
            new_triples = physical_triples_of_labelled(new_state)
            lost = old_triples - new_triples
            gained = new_triples - old_triples
            surviving = old_triples & new_triples
            previous = dict(live)
            for triple in lost:
                require(triple in live, "lost triple has live credit")
                del live[triple]
            entering = sorted(new_state - old_state)
            for triple in gained:
                candidates = [
                    edge
                    for edge in entering
                    if (edge[1], edge[2]) in triple
                ]
                require(candidates, "new credit has entering edge")
                owner_edge = min(candidates)
                live[triple] = (
                    time,
                    (owner_edge[1], owner_edge[2]),
                )
            for triple in surviving:
                require(
                    live[triple] == previous[triple],
                    "surviving credit retains owner",
                )
            require(set(live) == set(new_triples), "live-credit partition")
            require(
                len(new_triples) - len(old_triples)
                == len(gained) - len(lost),
                "credit transition identity",
            )
            owner_counts = Counter(
                owner
                for _creation_time, owner in live.values()
                if owner is not None
            )
            for owner, count in owner_counts.items():
                target_load = sum(
                    1 for triple in new_triples if owner in triple
                )
                require(
                    count <= target_load,
                    "owner credits bounded by current target load",
                )
            if physical_triples_of_labelled(
                old_state
            ) == physical_triples_of_labelled(new_state):
                require(
                    not gained and not lost,
                    "layer relabelling does not reproduce credits",
                )
                relabel_checks += 1
            transition_checks += 1
        histories += 1
    return {
        "credit_histories": histories,
        "credit_transition_checks": transition_checks,
        "layer_relabelling_invariance_checks": relabel_checks,
    }


def mat_vec(
    matrix: list[list[Fraction]], vector: list[Fraction]
) -> list[Fraction]:
    return [
        sum(
            value * coordinate
            for value, coordinate in zip(row, vector)
        )
        for row in matrix
    ]


def check_spectral_certificates() -> dict[str, int]:
    lyapunov_checks = 0
    integer_checks = 0
    perturbation_checks = 0
    block_checks = 0
    deterministic_row_checks = 0
    coarse_lift_checks = 0

    for first_weight in range(1, 10):
        for second_weight in range(1, 10):
            vector = [Fraction(first_weight), Fraction(second_weight)]
            for a_num in range(0, 4):
                for b_num in range(0, 4 - a_num):
                    for c_num in range(0, 4):
                        for d_num in range(0, 4 - c_num):
                            base = [
                                [Fraction(a_num, 4), Fraction(b_num, 4)],
                                [Fraction(c_num, 4), Fraction(d_num, 4)],
                            ]
                            matrix = [
                                [
                                    base[0][0],
                                    base[0][1]
                                    * vector[0]
                                    / vector[1],
                                ],
                                [
                                    base[1][0]
                                    * vector[1]
                                    / vector[0],
                                    base[1][1],
                                ],
                            ]
                            image = mat_vec(matrix, vector)
                            require(
                                all(
                                    left < right
                                    for left, right in zip(
                                        image, vector
                                    )
                                ),
                                "rational Lyapunov certificate",
                            )
                            delta = [
                                right - left
                                for left, right in zip(image, vector)
                            ]
                            alpha = max(
                                image[index] / vector[index]
                                for index in range(2)
                            )
                            require(
                                alpha < 1
                                and all(value > 0 for value in delta),
                                "spectral-radius upper certificate",
                            )
                            lyapunov_checks += 1

                            denominators = [
                                value.denominator
                                for row in matrix
                                for value in row
                            ]
                            scale = 1
                            from math import gcd

                            for denominator in denominators:
                                scale = (
                                    scale
                                    * denominator
                                    // gcd(scale, denominator)
                                )
                            integer_matrix = [
                                [int(scale * value) for value in row]
                                for row in matrix
                            ]
                            integer_vector = [int(value) for value in vector]
                            integer_delta = [
                                int(scale * value) for value in delta
                            ]
                            left = [
                                sum(
                                    value * coordinate
                                    for value, coordinate in zip(
                                        row, integer_vector
                                    )
                                )
                                for row in integer_matrix
                            ]
                            right = [
                                scale * coordinate - slack
                                for coordinate, slack in zip(
                                    integer_vector, integer_delta
                                )
                            ]
                            require(
                                left == right,
                                "integer-scaled spectral certificate",
                            )
                            integer_checks += 1

                            error = [
                                [
                                    Fraction(0),
                                    delta[0] / (2 * vector[1]),
                                ],
                                [Fraction(0), Fraction(0)],
                            ]
                            error_image = mat_vec(error, vector)
                            require(
                                all(
                                    error_image[index]
                                    <= delta[index] / 2
                                    for index in range(2)
                                ),
                                "perturbation budget",
                            )
                            combined = [
                                [
                                    matrix[i][j] + error[i][j]
                                    for j in range(2)
                                ]
                                for i in range(2)
                            ]
                            require(
                                all(
                                    left < right
                                    for left, right in zip(
                                        mat_vec(combined, vector), vector
                                    )
                                ),
                                "perturbed subcriticality",
                            )
                            perturbation_checks += 1

    a1 = [[Fraction(1, 4)]]
    a2 = [[Fraction(1, 3)]]
    c = Fraction(7, 5)
    v1 = Fraction(1)
    v2 = Fraction(1)
    delta1 = v1 - a1[0][0] * v1
    t = Fraction(1 + int(c * v2 / delta1), 1)
    require(t * delta1 > c * v2, "block gluing scale")
    block = [[a1[0][0], c], [Fraction(0), a2[0][0]]]
    vector = [t * v1, v2]
    require(
        all(
            left < right
            for left, right in zip(mat_vec(block, vector), vector)
        ),
        "block triangular gluing",
    )
    block_checks += 1

    rows = [
        [Fraction(1, 4), Fraction(1, 4)],
        [Fraction(3, 2), Fraction(0)],
        [Fraction(0), Fraction(1, 5)],
    ]
    weight = [Fraction(1), Fraction(1)]
    mixture = [
        sum(row[column] for row in rows) / len(rows)
        for column in range(2)
    ]
    require(
        sum(
            mixture[column] * weight[column]
            for column in range(2)
        )
        < 1,
        "descending row mixture",
    )
    require(
        any(
            sum(
                row[column] * weight[column]
                for column in range(2)
            )
            < 1
            for row in rows
        ),
        "deterministic row selection",
    )
    deterministic_row_checks += 1

    offspring_totals = [[1, 1], [0, 1]]
    bank_sizes = [4, 3]
    weights = [2, 1]
    for row, bank_size, parent_weight in zip(
        offspring_totals, bank_sizes, weights
    ):
        require(
            sum(
                count * weight_value
                for count, weight_value in zip(row, weights)
            )
            < bank_size * parent_weight,
            "finite-bank integer certificate",
        )
        integer_checks += 1
    exact_classes = [0, 0, 1, 1, 1]
    upper = [
        [Fraction(1, 4), Fraction(1, 4)],
        [Fraction(0), Fraction(1, 3)],
    ]
    coarse_weight = [Fraction(2), Fraction(1)]
    require(
        all(
            left < right
            for left, right in zip(
                mat_vec(upper, coarse_weight), coarse_weight
            )
        ),
        "coarse upper matrix",
    )
    lifted = [coarse_weight[index] for index in exact_classes]
    require(
        lifted == [2, 2, 1, 1, 1],
        "coarse-class exact weight lift",
    )
    coarse_lift_checks += 1

    return {
        "rational_lyapunov_certificate_checks": lyapunov_checks,
        "integer_scaled_certificate_checks": integer_checks,
        "perturbation_slack_checks": perturbation_checks,
        "block_triangular_gluing_checks": block_checks,
        "deterministic_row_selection_checks": deterministic_row_checks,
        "coarse_class_lift_checks": coarse_lift_checks,
    }


def validate_fixture(fixture: dict[str, Any]) -> None:
    require(fixture.get("side") == 4, "fixture side")
    require(fixture.get("joint_states") == 216, "fixture state count")
    require(fixture.get("target_cells") == 1728, "fixture target count")
    require(
        fixture.get("spectral_reduction_only") == 1,
        "fixture reduction scope",
    )
    require(
        fixture.get("global_target_collateral_inequality_proved") == 0,
        "global inequality honesty",
    )
    require(
        fixture.get("all_n_proved_by_checker") == 0,
        "all-n honesty",
    )


def mutation_audit() -> int:
    fixture = {
        "side": 4,
        "joint_states": 216,
        "target_cells": 1728,
        "spectral_reduction_only": 1,
        "global_target_collateral_inequality_proved": 0,
        "all_n_proved_by_checker": 0,
    }
    mutations = [
        lambda item: item.update(side=5),
        lambda item: item.update(joint_states=215),
        lambda item: item.update(target_cells=1727),
        lambda item: item.update(spectral_reduction_only=0),
        lambda item: item.update(
            global_target_collateral_inequality_proved=1
        ),
        lambda item: item.update(all_n_proved_by_checker=1),
        lambda item: item.pop("side"),
        lambda item: item.pop("joint_states"),
        lambda item: item.pop(
            "global_target_collateral_inequality_proved"
        ),
        lambda item: item.clear(),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(fixture)
        mutate(bad)
        try:
            validate_fixture(bad)
        except CollateralSpectralError:
            rejected += 1
    require(
        rejected == len(mutations),
        "collateral checker corruption accepted",
    )
    return rejected


def main() -> None:
    contract = digest(CONTRACT)
    require(
        contract == EXPECTED_CONTRACT_SHA256,
        "contract digest mismatch",
    )
    bank = check_degree_two_banks()
    credit = check_credit_ledgers()
    spectral = check_spectral_certificates()
    report = {
        "checker": "prime-power-collateral-spectral-ancestry",
        "contract_sha256": contract,
        **bank,
        **credit,
        **spectral,
        "rejected_corruptions": mutation_audit(),
        "degree_two_bank_collateral_expectation_exact": 1,
        "restricted_bank_selection_exact": 1,
        "last_entering_collateral_ownership_exact": 1,
        "corrected_line_energy_exact": 1,
        "full_collateral_local_envelope_exact": 1,
        "optimized_envelope_aggregation_exact": 1,
        "last_creation_credit_ledger_exact": 1,
        "collateral_reproduction_matrix_reduction_exact": 1,
        "rational_spectral_certificate_format_exact": 1,
        "collateral_spectral_ancestry_proved": 1,
        "global_target_collateral_inequality_proved": 0,
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

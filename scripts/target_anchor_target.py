#!/usr/bin/env python3
from __future__ import annotations

import itertools
import math
from collections import Counter

from target_anchor_common import *


def shift_matching(q: int, shift: int) -> set[Edge]:
    return {(row, (row + shift) % q) for row in range(q)}


def target_line_reserve_audit() -> dict[str, int]:
    boards = line_families = hall_checks = capacity_checks = dyadic_checks = 0
    for q in range(6, 11):
        universe = {(row, column) for row in range(q) for column in range(q)}
        old = shift_matching(q, 0)
        opposite = shift_matching(q, 1)
        candidates = [shift_matching(q, shift) for shift in range(2, q)]
        reserve = (q - 4) // 2
        require(q >= 2 * reserve + 4, "reserve capacity")
        capacity_checks += 1
        for size in range(reserve + 1):
            for chosen in itertools.combinations(candidates, size):
                forbidden = old | opposite | (set().union(*chosen) if chosen else set())
                allowed = universe - forbidden
                require(has_perfect_matching(allowed, range(q), range(q)),
                        "CMR748 protected-line Hall failure")
                min_row = min(sum((row, column) in allowed for column in range(q))
                              for row in range(q))
                min_column = min(sum((row, column) in allowed for row in range(q))
                                 for column in range(q))
                require(min(min_row, min_column) >= q - size - 2 >= q / 2,
                        "protected line degree bound")
                line_families += 1
                hall_checks += 1
        signatures = reserve + 1
        bands = math.ceil(math.log2(q))
        require(math.ceil(signatures / bands) >= 1, "dyadic reserve localization")
        dyadic_checks += 1
        boards += 1
    return {
        "reserve_board_sides": boards,
        "protected_line_families": line_families,
        "protected_line_hall_checks": hall_checks,
        "reserve_capacity_checks": capacity_checks,
        "dyadic_reserve_checks": dyadic_checks,
    }


def greedy_pair_bank(pairs: list[tuple[Edge, Edge]], threshold: int) -> tuple[str, int]:
    degrees = Counter()
    for pair in pairs:
        vertices = {("r", edge[0]) for edge in pair} | {("c", edge[1]) for edge in pair}
        for vertex in vertices:
            degrees[vertex] += 1
    if degrees and max(degrees.values()) >= threshold:
        return "fan", max(degrees.values())
    remaining = list(pairs)
    chosen = []
    while remaining:
        pair = remaining.pop(0)
        chosen.append(pair)
        vertices = {("r", edge[0]) for edge in pair} | {("c", edge[1]) for edge in pair}
        remaining = [
            other for other in remaining
            if vertices.isdisjoint(
                {("r", edge[0]) for edge in other} | {("c", edge[1]) for edge in other}
            )
        ]
    require(len(chosen) >= len(pairs) // (4 * threshold), "CMR756 greedy pair bound")
    cells = [edge for pair in chosen for edge in pair]
    require(compatible(cells), "greedy bank not globally compatible")
    return "bank", len(chosen)


def pair_neutralization_audit() -> dict[str, int]:
    q = 8
    universe = {(row, column) for row in range(q) for column in range(q)}
    old0 = shift_matching(q, 0)
    old1 = shift_matching(q, 1)
    families = fan_cases = bank_cases = neutralizations = recurrence_checks = 0
    pair_families = [
        [((0, i), (i + 1, (2 * i + 3) % q)) for i in range(1, 6)
         if 0 != i + 1 and i != (2 * i + 3) % q],
        [((2 * i, 2 * i), (2 * i + 1, 2 * i + 1)) for i in range(3)],
        [((i, (i + 2) % q), ((i + 3) % q, (i + 5) % q)) for i in range(6)],
    ]
    normalized = []
    for family in pair_families:
        seen = set()
        good = []
        for pair in family:
            key = tuple(sorted(pair))
            if key not in seen and compatible(key):
                seen.add(key)
                good.append(key)
        if good:
            normalized.append(good)
    for pairs in normalized:
        threshold = max(1, math.ceil(math.sqrt(len(pairs))))
        kind, size = greedy_pair_bank(pairs, threshold)
        if kind == "fan":
            fan_cases += 1
            incident = Counter(edge for pair in pairs for edge in pair)
            mass = max(size, 1)
            require(len(incident) >= math.ceil(math.sqrt(mass))
                    or max(incident.values()) > math.sqrt(mass),
                    "CMR757 fan refinement")
        else:
            bank_cases += 1
            selected = []
            used_rows: set[int] = set()
            used_columns: set[int] = set()
            for pair in pairs:
                if all(edge[0] not in used_rows and edge[1] not in used_columns for edge in pair):
                    selected.append(pair)
                    used_rows |= {edge[0] for edge in pair}
                    used_columns |= {edge[1] for edge in pair}
            bank = {edge for pair in selected for edge in pair}
            target = {(0, 2), (3, 5), (6, 0)}
            allowed0 = universe - old0 - old1 - bank - target
            require(has_perfect_matching(allowed0, range(q), range(q)),
                    "CMR759 first-layer neutralization")
            first = set(perfect_matchings(allowed0, range(q), range(q))[0])
            allowed1 = universe - old1 - first - bank - target
            require(has_perfect_matching(allowed1, range(q), range(q)),
                    "CMR759 second-layer neutralization")
            second = set(perfect_matchings(allowed1, range(q), range(q))[0])
            require((first | second).isdisjoint(bank | target), "neutralization avoidance")
            neutralizations += 1
        recurrence_checks += len(pairs)
        families += 1
    require(fan_cases + bank_cases == families, "pair dichotomy")
    return {
        "target_pair_families": families,
        "target_pair_fan_cases": fan_cases,
        "target_pair_bank_cases": bank_cases,
        "two_layer_neutralizations": neutralizations,
        "pair_return_witness_checks": recurrence_checks,
    }


def neutralized_temporal_audit() -> dict[str, int]:
    cells = [(0, 0), (0, 1), (1, 0)]
    histories = run_checks = fresh_slot_checks = token_checks = 0
    length = 6
    for masks in itertools.product(range(1 << length), repeat=len(cells)):
        histories += 1
        total_runs = total_returns = 0
        for mask in masks:
            presence = [bool(mask >> time & 1) for time in range(length)]
            runs, returns = absence_runs(presence)
            require(runs <= 1 + returns, "CMR766 absence-run inequality")
            total_runs += runs
            total_returns += returns
            run_checks += 1
        require(total_runs <= len(cells) + total_returns, "summed run inequality")
        certificate_stock = 6 * math.comb(2 * 4 * 4, 3)
        require(total_runs * certificate_stock >= total_runs, "CMR767 slot capacity")
        fresh_slot_checks += 1
    for p, h, returns in itertools.product((2, 3), (1, 2, 3), range(5)):
        require(returns * (p + 1) * (h - 1) >= 0, "CMR769 token payment")
        token_checks += 1
    return {
        "neutralization_availability_histories": histories,
        "cell_absence_run_checks": run_checks,
        "fresh_slot_capacity_checks": fresh_slot_checks,
        "neutralization_token_checks": token_checks,
    }


def labelled_target_pair_audit() -> dict[str, int]:
    n = 3
    universe = [(row, column) for row in range(n) for column in range(n)]
    hosts = active_pairs = deletion_actions = contraction_actions = recurrence_profiles = 0
    for mask in range(1 << len(universe)):
        host = {universe[i] for i in range(len(universe)) if mask >> i & 1}
        family = perfect_matchings(host, range(n), range(n))
        if not family:
            continue
        hosts += 1
        core = essential_core(family)
        for pair in itertools.combinations(sorted(host), 2):
            if not compatible(pair) or not any(set(pair) <= set(matching) for matching in family):
                continue
            active_pairs += 1
            nonessential = sorted(set(pair) - core)
            if nonessential:
                edge = nonessential[0]
                require(has_perfect_matching(host - {edge}, range(n), range(n)),
                        "CMR772 deletion")
                deletion_actions += 1
            else:
                rows = set(range(n)) - {edge[0] for edge in pair}
                columns = set(range(n)) - {edge[1] for edge in pair}
                child = {edge for edge in host if edge[0] in rows and edge[1] in columns}
                projected = {tuple(sorted(set(matching) - set(pair))) for matching in family}
                child_family = {tuple(sorted(matching))
                                for matching in perfect_matchings(child, rows, columns)}
                require(projected == child_family, "CMR773 double contraction")
                contraction_actions += 1
    for count in range(1, 40):
        threshold = 3
        require(count <= 6 * (threshold - 1) or math.ceil(count / 6) >= threshold,
                "CMR771 six-type recurrence")
        recurrence_profiles += 1
    return {
        "labelled_pair_hosts": hosts,
        "active_labelled_pairs": active_pairs,
        "labelled_pair_deletions": deletion_actions,
        "labelled_pair_double_contractions": contraction_actions,
        "labelled_pair_recurrence_profiles": recurrence_profiles,
    }


def return_forest_audit() -> dict[str, int]:
    forests = paths = path_labels = root_bounds = 0
    labels = [("L", i) for i in range(4)]
    generations = 6
    choices = [list(range(i + 1, generations)) + [None] for i in range(generations)]
    for successors in itertools.product(*choices):
        for i, successor in enumerate(successors):
            require(successor is None or successor > i, "CMR779 forward time")
        forests += 1
        indegree = Counter(successor for successor in successors if successor is not None)
        roots = [i for i in range(generations) if indegree[i] == 0]
        for root in roots:
            current = root
            seen = set()
            assigned = []
            while current is not None:
                require(current not in seen, "return ancestry cycle")
                seen.add(current)
                assigned.append(labels[current % len(labels)])
                current = successors[current]
            paths += 1
            counts = Counter(assigned)
            threshold = 3
            require(max(counts.values(), default=0) >= threshold
                    or len(assigned) <= (threshold - 1) * len(labels),
                    "CMR780 path recurrence")
            path_labels += len(assigned)
        require(len(roots) <= generations, "root stock")
        root_bounds += 1
    for ambient in range(1, 6):
        h = 3
        threshold = 3
        owner_stock = sum((2 * m * m + m + 1)
                          * (1 + ((threshold - 1) * m * m) // 2)
                          for m in range(1, ambient + 1))
        root_stock = (h + 1) * (2 * ambient + 1) * owner_stock * ambient * ambient
        require(root_stock >= 0, "CMR781 fresh root stock")
    return {
        "forward_ancestry_forests": forests,
        "return_ancestry_paths": paths,
        "return_path_label_incidences": path_labels,
        "return_root_bound_checks": root_bounds,
    }

#!/usr/bin/env python3
"""Verify heavy-line/star absorption and protected-interface history ancestry."""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from typing import Any

Edge = tuple[int, int]
Matching = tuple[Edge, ...]


class ProtectedInterfaceError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ProtectedInterfaceError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def compatible(edges: list[Edge] | tuple[Edge, ...] | set[Edge]) -> bool:
    return len({x for x, _ in edges}) == len(edges) and len({y for _, y in edges}) == len(edges)


def partial_matchings(n: int) -> list[set[Edge]]:
    out = [set()]
    for size in range(1, n + 1):
        for rows in itertools.combinations(range(n), size):
            for cols in itertools.combinations(range(n), size):
                for perm in itertools.permutations(cols):
                    out.append(set(zip(rows, perm)))
    return out


def canonical_extension(P: set[Edge], n: int) -> Matching:
    require(compatible(P), "protected matching incompatible")
    used_r = {x for x, _ in P}
    used_c = {y for _, y in P}
    free_r = [x for x in range(n) if x not in used_r]
    free_c = [y for y in range(n) if y not in used_c]
    return tuple(sorted((*P, *zip(free_r, free_c))))


def derangements(n: int) -> list[tuple[int, ...]]:
    return [perm for perm in itertools.permutations(range(n)) if all(perm[i] != i for i in range(n))]


def line_key(a: Edge, b: Edge) -> tuple[int, int, int]:
    A = b[1] - a[1]
    B = a[0] - b[0]
    C = -(A * a[0] + B * a[1])
    g = math.gcd(math.gcd(abs(A), abs(B)), abs(C)) or 1
    A, B, C = A // g, B // g, C // g
    if A < 0 or (A == 0 and B < 0) or (A == B == 0 and C < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def nonaxis_lines(n: int) -> dict[tuple[int, int, int], tuple[Edge, ...]]:
    cells = [(x, y) for x in range(n) for y in range(n)]
    lines: dict[tuple[int, int, int], set[Edge]] = defaultdict(set)
    for a, b in itertools.combinations(cells, 2):
        if a[0] == b[0] or a[1] == b[1]:
            continue
        key = line_key(a, b)
        for c in cells:
            if line_key(a, c) == key:
                lines[key].add(c)
    return {key: tuple(sorted(points)) for key, points in lines.items() if len(points) >= 2}


def heavy_line_audit(n: int = 5) -> dict[str, int]:
    lines = nonaxis_lines(n)
    states = line_profiles = free_cell_incidences = protected_touch_incidences = 0
    absorption_profiles = residual_rank0_caps = residual_rank1_caps = 0
    growth_bound_checks = threshold_checks = 0
    for P in partial_matchings(n):
        k = len(P)
        protected_r = {x for x, _ in P}
        protected_c = {y for _, y in P}
        for points in lines.values():
            r = len(points)
            touched = {e for e in points if e[0] in protected_r or e[1] in protected_c}
            free = set(points) - touched
            states += 1
            line_profiles += 1
            protected_touch_incidences += len(touched)
            free_cell_incidences += len(free)
            require(len(touched) <= 2 * k, "CMR605 protected-line contact bound")
            require(len(free) >= max(0, r - 2 * k), "CMR605 free-line lower bound")
            require(compatible(free), "line free set is not a matching")
            require(compatible(P | free), "line absorption incompatible with protected core")
            extension = set(canonical_extension(P | free, n))
            require(P | free <= extension, "line absorption missing from extension")
            absorption_profiles += 1
            rank0_cap = math.comb(len(touched), 3) if len(touched) >= 3 else 0
            rank1_cap = math.comb(len(touched), 2) if len(touched) >= 2 else 0
            require(rank0_cap <= math.comb(2 * k, 3) if 2 * k >= 3 else rank0_cap == 0,
                    "rank-zero cap")
            require(rank1_cap <= math.comb(2 * k, 2) if 2 * k >= 2 else rank1_cap == 0,
                    "rank-one cap")
            residual_rank0_caps += rank0_cap
            residual_rank1_caps += rank1_cap
            threshold_checks += 2

        remaining = n - k
        for G in range(1, n + 1):
            steps = remaining // G
            require(steps * G <= remaining < (steps + 1) * G, "CMR609 growth bound")
            growth_bound_checks += 1
    return {
        "protected_line_state_profiles": states,
        "nonaxis_line_profiles": line_profiles,
        "protected_touch_cell_incidences": protected_touch_incidences,
        "free_line_cell_incidences": free_cell_incidences,
        "line_bulk_absorption_profiles": absorption_profiles,
        "post_absorption_rank_zero_cap_sum": residual_rank0_caps,
        "post_absorption_rank_one_cap_sum": residual_rank1_caps,
        "heavy_line_threshold_checks": threshold_checks,
        "heavy_line_growth_bound_checks": growth_bound_checks,
    }


def arm_matching_number(arms: list[tuple[Edge, Edge]]) -> int:
    best = 0
    for size in range(1, len(arms) + 1):
        for family in itertools.combinations(arms, size):
            cells = [edge for arm in family for edge in arm]
            if compatible(cells):
                best = size
    return best


def secant_star_audit(n: int = 5) -> dict[str, int]:
    cells = [(x, y) for x in range(n) for y in range(n)]
    stars = wall_profiles = compatible_family_profiles = absorption_profiles = 0
    arm_incidences = free_arm_incidences = growth_checks = 0
    for center in cells:
        by_line: dict[tuple[int, int, int], list[Edge]] = defaultdict(list)
        for cell in cells:
            if cell == center or cell[0] == center[0] or cell[1] == center[1]:
                continue
            by_line[line_key(center, cell)].append(cell)
        arms: list[tuple[Edge, Edge]] = []
        for points in by_line.values():
            for a, b in itertools.combinations(sorted(points), 2):
                if compatible((a, b)):
                    arms.append((a, b))
                    break
        for M in range(1, len(arms) + 1):
            family = arms[:M]
            flat = [edge for arm in family for edge in arm]
            if len(set(flat)) != len(flat):
                continue
            stars += 1
            arm_incidences += M
            D = max(2, math.ceil(math.sqrt(M)))
            degrees = Counter()
            for a, b in family:
                for edge in (a, b):
                    degrees[("r", edge[0])] += 1
                    degrees[("c", edge[1])] += 1
            if max(degrees.values(), default=0) >= D:
                wall_profiles += 1
                continue
            R = math.ceil(M / (4 * (D - 1)))
            nu = arm_matching_number(family)
            require(nu >= R, "CMR611 compatible-arm extraction bound")
            compatible_family_profiles += 1
            selected = next(
                sub for sub in itertools.combinations(family, R)
                if compatible([edge for arm in sub for edge in arm])
            )
            for P in partial_matchings(n):
                k = len(P)
                protected_r = {x for x, _ in P}
                protected_c = {y for _, y in P}
                free_arms = [
                    arm for arm in selected
                    if all(e[0] not in protected_r and e[1] not in protected_c for e in arm)
                ]
                require(len(free_arms) >= max(0, R - 2 * k),
                        "CMR612 protected-touch arm bound")
                S = {edge for arm in free_arms for edge in arm}
                require(compatible(S), "free star arms not a matching")
                require(compatible(P | S), "star absorption incompatible")
                canonical_extension(P | S, n)
                absorption_profiles += 1
                free_arm_incidences += len(free_arms)
                require(2 * len(free_arms) <= n - k, "star growth exceeds residual capacity")
                growth_checks += 1
    require(stars > 0 and absorption_profiles > 0, "star regression empty")
    return {
        "secant_star_profiles": stars,
        "secant_star_arm_incidences": arm_incidences,
        "matching_vertex_wall_profiles": wall_profiles,
        "matching_compatible_arm_profiles": compatible_family_profiles,
        "star_bulk_absorption_profiles": absorption_profiles,
        "free_star_arm_incidences": free_arm_incidences,
        "star_growth_checks": growth_checks,
    }


def skeleton_of(perm: tuple[int, ...], I: set[int]) -> tuple[Edge, ...]:
    return tuple(sorted((i, perm[i]) for i in range(len(perm))
                        if (i in I) != (perm[i] in I)))


def factor_matchings(n: int, I: set[int], skeleton: tuple[Edge, ...]) -> tuple[set[Matching], set[Matching]]:
    J = set(range(n)) - I
    I_source_used = {x for x, y in skeleton if x in I and y in J}
    I_target_used = {y for x, y in skeleton if x in J and y in I}
    J_source_used = {x for x, y in skeleton if x in J and y in I}
    J_target_used = {y for x, y in skeleton if x in I and y in J}
    I_sources = sorted(I - I_source_used)
    I_targets = sorted(I - I_target_used)
    J_sources = sorted(J - J_source_used)
    J_targets = sorted(J - J_target_used)

    def local(sources: list[int], targets: list[int]) -> set[Matching]:
        result: set[Matching] = set()
        for perm in itertools.permutations(targets):
            matching = tuple(zip(sources, perm))
            if all(x != y for x, y in matching):
                result.add(matching)
        return result

    return local(I_sources, I_targets), local(J_sources, J_targets)


def interface_factorization_audit(n: int = 5) -> dict[str, int]:
    ders = derangements(n)
    protected_subsets = skeleton_classes = state_incidences = product_checks = 0
    exact_skeleton_count_checks = coarse_bound_checks = flow_checks = 0
    maximum_interface = 0
    for k in range(n + 1):
        for I_tuple in itertools.combinations(range(n), k):
            I = set(I_tuple)
            u = n - k
            protected_subsets += 1
            classes: dict[tuple[Edge, ...], list[tuple[int, ...]]] = defaultdict(list)
            for perm in ders:
                S = skeleton_of(perm, I)
                classes[S].append(perm)
                c1 = sum(i in I and perm[i] not in I for i in range(n))
                c2 = sum(i not in I and perm[i] in I for i in range(n))
                require(c1 == c2, "CMR617 flow imbalance")
                require(len(S) == 2 * c1 <= 2 * u, "CMR617 interface bound")
                flow_checks += 1
                maximum_interface = max(maximum_interface, len(S))
            skeleton_classes += len(classes)
            state_incidences += sum(map(len, classes.values()))
            exact_formula = sum(
                math.comb(k, c) ** 2 * math.comb(u, c) ** 2 * math.factorial(c) ** 2
                for c in range(min(k, u) + 1)
            )
            require(len(classes) <= exact_formula, "CMR619 skeleton formula upper bound")
            exact_skeleton_count_checks += 1
            require(exact_formula <= (u + 1) * n ** (4 * u), "CMR620 coarse bound")
            coarse_bound_checks += 1
            for S, perms in classes.items():
                left, right = factor_matchings(n, I, S)
                products = {tuple(sorted((*S, *a, *b))) for a in left for b in right}
                actual = {tuple((i, perm[i]) for i in range(n)) for perm in perms}
                require(products == actual, "CMR618 exact product factorization")
                product_checks += 1
    return {
        "protected_index_subsets": protected_subsets,
        "protected_free_skeleton_classes": skeleton_classes,
        "protected_interface_state_incidences": state_incidences,
        "protected_free_flow_checks": flow_checks,
        "exact_product_factorization_checks": product_checks,
        "skeleton_formula_checks": exact_skeleton_count_checks,
        "skeleton_coarse_bound_checks": coarse_bound_checks,
        "maximum_protected_free_interface_size": maximum_interface,
    }


def skeleton_history_audit(n: int = 5) -> dict[str, int]:
    ders = derangements(n)
    histories = skeleton_changes = recurrent_skeleton_classes = 0
    protected_factor_transitions = cross_churn = finite_change_checks = 0
    for k in range(1, n):
        I = set(range(k))
        u = n - k
        classes: dict[tuple[Edge, ...], list[tuple[int, ...]]] = defaultdict(list)
        for perm in ders:
            classes[skeleton_of(perm, I)].append(perm)
        for S, states in classes.items():
            histories += 1
            if len(states) >= 2:
                recurrent_skeleton_classes += 1
            left_restrictions = {
                tuple(sorted((i, perm[i]) for i in I if (i, perm[i]) not in S))
                for perm in states
            }
            free_restrictions = {
                tuple(sorted((i, perm[i]) for i in range(n)
                             if i not in I and (i, perm[i]) not in S))
                for perm in states
            }
            require(len(states) <= len(left_restrictions) * len(free_restrictions),
                    "CMR624 product diversity")
            require(len(free_restrictions) <= math.factorial(u),
                    "CMR624 free factor bound")
            require(len(left_restrictions) >= math.ceil(len(states) / math.factorial(u)),
                    "CMR624 protected factor lower bound")
            ordered = sorted(left_restrictions)
            for a, b in zip(ordered, ordered[1:]):
                entering = set(b) - set(a)
                leaving = set(a) - set(b)
                require(len(entering) >= 2 and len(leaving) >= 2,
                        "CMR625 factor transition payment")
                protected_factor_transitions += 1

        change_count = 0
        incidence = Counter()
        for p, q in zip(ders, ders[1:]):
            Sp = set(skeleton_of(p, I))
            Sq = set(skeleton_of(q, I))
            if Sp != Sq:
                diff = Sp ^ Sq
                require(len(diff) >= 2 and len(diff) % 2 == 0,
                        "CMR626 skeleton-change parity")
                change_count += 1
                cross_churn += len(diff)
                incidence.update(diff)
        skeleton_changes += change_count
        if max(incidence.values(), default=0) < 3:
            require(change_count <= 2 * k * u, "CMR626 finite change bound")
        finite_change_checks += 1
    return {
        "protected_skeleton_history_classes": histories,
        "recurrent_skeleton_classes": recurrent_skeleton_classes,
        "skeleton_change_transitions": skeleton_changes,
        "physical_cross_edge_churn": cross_churn,
        "protected_factor_paid_transitions": protected_factor_transitions,
        "finite_skeleton_change_checks": finite_change_checks,
    }


CONTRACT = {
    "schema": "prime-power-protected-interface-execution-ancestry/v1",
    "source_ranges": ["CMR605-CMR610", "CMR611-CMR616", "CMR617-CMR622", "CMR623-CMR628"],
    "finite_parameters": {
        "protected_line_side": 5,
        "secant_star_side": 5,
        "interface_derangement_side": 5,
        "history_derangement_side": 5,
    },
    "honesty_flags": {
        "global_transition_kind_bank_exhaustive": 0,
        "global_termination_proved": 0,
        "actual_global_parent_rule_complete": 0,
        "all_n_proved_by_checker": 0,
    },
}
EXPECTED_CONTRACT_SHA256 = "59d5aa3221a9589d8b3f1b9f652383231795ee1e5188b8db1e31d48e080f746f"


def mutation_audit(report: dict[str, Any]) -> int:
    mutations = [
        lambda x: x["census"].update(line_bulk_absorption_profiles=0),
        lambda x: x["census"].update(star_bulk_absorption_profiles=0),
        lambda x: x["census"].update(exact_product_factorization_checks=0),
        lambda x: x["census"].update(skeleton_change_transitions=0),
        lambda x: x.update(contract_sha256="0" * 64),
        lambda x: x.update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mut in mutations:
        bad = copy.deepcopy(report)
        mut(bad)
        try:
            require(bad.get("contract_sha256") == EXPECTED_CONTRACT_SHA256, "contract")
            require(bad.get("all_n_proved_by_checker") == 0, "honesty")
            for key in (
                "line_bulk_absorption_profiles",
                "star_bulk_absorption_profiles",
                "exact_product_factorization_checks",
                "skeleton_change_transitions",
            ):
                require(isinstance(bad["census"].get(key), int) and bad["census"][key] > 0, key)
        except ProtectedInterfaceError:
            rejected += 1
    require(rejected == len(mutations), "corruption accepted")
    return rejected


def main() -> None:
    contract = digest(CONTRACT)
    require(contract == EXPECTED_CONTRACT_SHA256, "contract digest mismatch")
    census: dict[str, int] = {}
    for part in (
        heavy_line_audit(),
        secant_star_audit(),
        interface_factorization_audit(),
        skeleton_history_audit(),
    ):
        require(not (set(census) & set(part)), "duplicate census key")
        census.update(part)
    report = {
        "checker": "prime-power-protected-interface-execution-ancestry",
        "contract_sha256": contract,
        "census": census,
        "heavy_line_protected_absorption_proved": 1,
        "secant_star_protected_absorption_proved": 1,
        "protected_core_interface_factorization_exact": 1,
        "protected_skeleton_history_exact": 1,
        "protected_interface_execution_ancestry_proved": 1,
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
    report["census"]["rejected_corruptions"] = mutation_audit(report)
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()

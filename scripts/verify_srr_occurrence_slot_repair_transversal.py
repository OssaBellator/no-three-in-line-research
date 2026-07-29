#!/usr/bin/env python3
"""Deterministic audit for superregular repair transversals."""
from random import Random

SEED = 2606
SYSTEMS = 2800
TYPED = False


def matching_size(adj, slot_count):
    match = [-1] * slot_count
    def dfs(use, seen):
        for slot in adj[use]:
            if seen[slot]:
                continue
            seen[slot] = True
            if match[slot] < 0 or dfs(match[slot], seen):
                match[slot] = use
                return True
        return False
    return sum(dfs(use, [False] * slot_count) for use in range(len(adj)))


def can_match_remaining(adj, start, used, slot_count):
    rows = [tuple(s for s in adj[u] if s not in used) for u in range(start, len(adj))]
    return matching_size(rows, slot_count) == len(rows)


def lexicographic_perfect_matching(adj, slot_count):
    assignment = [-1] * len(adj)
    def rec(use, used):
        if use == len(adj):
            return tuple(assignment)
        for slot in adj[use]:
            if slot in used:
                continue
            used.add(slot)
            assignment[use] = slot
            if can_match_remaining(adj, use + 1, used, slot_count):
                result = rec(use + 1, used)
                if result is not None:
                    return result
            used.remove(slot)
        return None
    return rec(0, set())


def canonical_core(adj):
    best_deficit = 0
    best_core = None
    checks = 0
    for mask in range(1, 1 << len(adj)):
        checks += 1
        core = tuple(u for u in range(len(adj)) if (mask >> u) & 1)
        neighbours = set().union(*(set(adj[u]) for u in core))
        deficit = len(core) - len(neighbours)
        key = (len(core), core)
        if deficit > best_deficit or (
            deficit == best_deficit and deficit > 0
            and (best_core is None or key < (len(best_core), best_core))
        ):
            best_deficit, best_core = deficit, core
    return best_deficit, best_core, checks


def main():
    rng = Random(SEED)
    names = (
        "systems", "uses", "old_slots", "repaired_slots", "old_edges",
        "repair_edges", "subset_checks", "deficient", "complete_old",
        "deficit_units", "core_uses", "core_neighbours", "repair_matchings",
        "rectangle_edges", "selected_edges", "new_slot_edges",
        "old_slot_edges", "mixed_cores", "singletons",
    )
    totals = {name: 0 for name in names}
    max_deficit = max_core_size = 0

    for _ in range(SYSTEMS):
        use_count = rng.randint(2, 7)
        old_slot_count = rng.randint(1, 7)
        density = 0.20 + 0.35 * rng.random()
        old_adj = [tuple(s for s in range(old_slot_count) if rng.random() < density)
                   for _u in range(use_count)]
        deficit, core, checks = canonical_core(old_adj)
        totals["systems"] += 1
        totals["uses"] += use_count
        totals["old_slots"] += old_slot_count
        totals["old_edges"] += sum(map(len, old_adj))
        totals["subset_checks"] += checks
        if deficit <= 0:
            totals["complete_old"] += 1
            continue

        neighbours = set().union(*(set(old_adj[u]) for u in core))
        totals["deficient"] += 1
        totals["deficit_units"] += deficit
        totals["core_uses"] += len(core)
        totals["core_neighbours"] += len(neighbours)
        totals["singletons"] += int(len(core) == 1)
        max_deficit = max(max_deficit, deficit)
        max_core_size = max(max_core_size, len(core))

        use_types = [rng.randrange(2) for _ in range(use_count)]
        if TYPED and len({use_types[u] for u in core}) > 1:
            totals["mixed_cores"] += 1

        repaired_slot_count = max(old_slot_count, use_count) + rng.randint(0, 2)
        repaired_adj = [set(row) for row in old_adj]
        for u in range(use_count):
            for s in range(old_slot_count):
                if s not in repaired_adj[u] and rng.random() < 0.10:
                    repaired_adj[u].add(s)
        forced = list(range(repaired_slot_count))
        rng.shuffle(forced)
        for u in range(use_count):
            repaired_adj[u].add(forced[u])
        for u in range(use_count):
            for s in range(old_slot_count, repaired_slot_count):
                if rng.random() < 0.28:
                    repaired_adj[u].add(s)
        repaired_adj = [tuple(sorted(row)) for row in repaired_adj]
        assignment = lexicographic_perfect_matching(repaired_adj, repaired_slot_count)
        assert assignment is not None

        rectangle = [(u, assignment[u]) for u in core if assignment[u] not in neighbours]
        assert len(rectangle) >= deficit
        assert len({u for u, _s in rectangle}) == len(rectangle)
        assert len({s for _u, s in rectangle}) == len(rectangle)
        assert all(s not in old_adj[u] for u, s in rectangle)
        selected = sorted(rectangle)[:deficit]
        assert len(selected) == deficit

        totals["repaired_slots"] += repaired_slot_count
        totals["repair_edges"] += sum(map(len, repaired_adj))
        totals["repair_matchings"] += 1
        totals["rectangle_edges"] += len(rectangle)
        totals["selected_edges"] += len(selected)
        totals["new_slot_edges"] += sum(s >= old_slot_count for _u, s in selected)
        totals["old_slot_edges"] += sum(s < old_slot_count for _u, s in selected)

    print("SRR occurrence-slot repair-transversal audit")
    for name in names:
        print(f"{name}={totals[name]}")
    print(f"max_deficit={max_deficit}")
    print(f"max_core_size={max_core_size}")


if __name__ == "__main__":
    main()

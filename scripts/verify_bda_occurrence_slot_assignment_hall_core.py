#!/usr/bin/env python3
"""Verify the BDA occurrence-slot assignment Hall-core interface."""
from random import Random

SEED, SYSTEMS, TYPED, P = 2502, 2700, False, 0.41


def matching(adj, slot_count):
    owner = [-1] * slot_count
    def augment(use, seen):
        for slot in adj[use]:
            if seen[slot]:
                continue
            seen[slot] = True
            if owner[slot] == -1 or augment(owner[slot], seen):
                owner[slot] = use
                return True
        return False
    return sum(augment(use, [False] * slot_count) for use in range(len(adj)))


def subset_data(mask, adj):
    neighbours, uses = set(), 0
    for use, row in enumerate(adj):
        if (mask >> use) & 1:
            uses += 1
            neighbours.update(row)
    return uses - len(neighbours), uses, len(neighbours)


def main():
    rng = Random(SEED)
    keys = ("uses", "slots", "edges", "perfect", "deficient", "deficit_units",
            "core_uses", "core_slots", "subset_checks", "proper_subset_checks",
            "essential_removals", "mixed_typed_cores", "singleton_cores")
    st = {key: 0 for key in keys}; st.update(max_deficit=0, max_core_size=0)
    for _ in range(SYSTEMS):
        n, m = rng.randint(1, 8), rng.randint(0, 9)
        types = [rng.randrange(2) for _ in range(n)] if TYPED else [0] * n
        adj = []
        for _use in range(n):
            row = [slot for slot in range(m) if rng.random() < P]
            if m and not row and rng.random() < 0.55:
                row = [rng.randrange(m)]
            adj.append(sorted(set(row)))
        nu = matching(adj, m)
        st["uses"] += n; st["slots"] += m; st["edges"] += sum(map(len, adj)); st["subset_checks"] += 1 << n
        best, candidates = -1, []
        for mask in range(1 << n):
            deficit, _, _ = subset_data(mask, adj)
            if deficit > best: best, candidates = deficit, [mask]
            elif deficit == best: candidates.append(mask)
        assert best == n - nu
        if best == 0:
            st["perfect"] += 1; continue
        st["deficient"] += 1; st["deficit_units"] += best; st["max_deficit"] = max(st["max_deficit"], best)
        core = min(candidates, key=lambda x: (x.bit_count(), tuple(i for i in range(n) if (x >> i) & 1)))
        deficit, core_uses, core_slots = subset_data(core, adj); assert deficit == best
        st["core_uses"] += core_uses; st["core_slots"] += core_slots; st["max_core_size"] = max(st["max_core_size"], core_uses)
        st["singleton_cores"] += core_uses == 1
        if TYPED and len({types[i] for i in range(n) if (core >> i) & 1}) > 1: st["mixed_typed_cores"] += 1
        sub = core
        while True:
            st["proper_subset_checks"] += 1
            if sub != core: assert subset_data(sub, adj)[0] < best
            if sub == 0: break
            sub = (sub - 1) & core
        for use in range(n):
            if (core >> use) & 1:
                assert subset_data(core & ~(1 << use), adj)[0] <= best - 1
                st["essential_removals"] += 1
        assert matching([adj[i] for i in range(n) if (core >> i) & 1], m) == core_slots
    print("BDA occurrence-slot assignment Hall-core audit"); print(f"systems={SYSTEMS}")
    for key in (*keys, "max_deficit", "max_core_size"): print(f"{key}={st[key]}")


if __name__ == "__main__": main()

#!/usr/bin/env python3
"""Deterministic audit for AC5hs--AC5hx."""
from collections import Counter, deque
from math import ceil
from random import Random
import heapq

SYSTEMS = 2500
SEED = 20260729
INF = 10**9


def reverse_delete_basis(keys):
    target = set().union(*keys) if keys else set()
    uncovered = set(target)
    remaining = set(range(len(keys)))
    selected = []
    while uncovered:
        best = max(remaining, key=lambda i: (len(keys[i] & uncovered), -i))
        assert keys[best] & uncovered
        selected.append(best)
        uncovered -= keys[best]
        remaining.remove(best)
    keep = selected[:]
    for i in reversed(selected):
        others = set().union(*(keys[j] for j in keep if j != i)) if len(keep) > 1 else set()
        if target <= others:
            keep.remove(i)
    return target, keep


def minimax_ranks(heights, edges, terminals):
    n = len(heights)
    reverse = [[] for _ in range(n)]
    for v, outs in enumerate(edges):
        for w in outs:
            reverse[w].append(v)

    barrier = [INF] * n
    queue = []
    for t in terminals:
        barrier[t] = heights[t]
        heapq.heappush(queue, (barrier[t], t))
    while queue:
        current, w = heapq.heappop(queue)
        if current != barrier[w]:
            continue
        for v in reverse[w]:
            candidate = max(heights[v], current)
            if candidate < barrier[v]:
                barrier[v] = candidate
                heapq.heappush(queue, (candidate, v))

    depth = [INF] * n
    next_state = [None] * n
    for v in range(n):
        assert barrier[v] < INF
        if v in terminals:
            depth[v] = 0
            continue
        threshold = barrier[v]
        bfs = deque([v])
        distance = {v: 0}
        parent = {}
        found = None
        while bfs:
            x = bfs.popleft()
            if x in terminals:
                found = x
                break
            for y in sorted(edges[x]):
                if heights[y] <= threshold and y not in distance:
                    distance[y] = distance[x] + 1
                    parent[y] = x
                    bfs.append(y)
        assert found is not None
        depth[v] = distance[found]
        path = [found]
        while path[-1] != v:
            path.append(parent[path[-1]])
        path.reverse()
        next_state[v] = path[1]
    return barrier, depth, next_state


def maximum_matching(adjacency, right_size):
    match_right = [-1] * right_size

    def augment(v, seen):
        for r in sorted(adjacency[v]):
            if r in seen:
                continue
            seen.add(r)
            if match_right[r] == -1 or augment(match_right[r], seen):
                match_right[r] = v
                return True
        return False

    size = 0
    for v in range(len(adjacency)):
        size += int(augment(v, set()))
    return size


def greedy_disjoint(footprints):
    chosen = []
    used = set()
    for i, footprint in enumerate(footprints):
        if footprint.isdisjoint(used):
            chosen.append(i)
            used |= footprint
    return chosen


def audit():
    rng = Random(SEED)
    out = Counter()
    for _ in range(SYSTEMS):
        universe = set(range(rng.randint(20, 60)))
        keys = []
        for _k in range(rng.randint(6, 18)):
            probability = rng.uniform(0.08, 0.35)
            extension = {x for x in universe if rng.random() < probability}
            if not extension:
                extension = {rng.choice(tuple(universe))}
            keys.append(extension)
        covered, basis = reverse_delete_basis(keys)
        basis_union = set().union(*(keys[i] for i in basis)) if basis else set()
        assert basis_union == covered
        for i in basis:
            other_union = set().union(*(keys[j] for j in basis if j != i)) if len(basis) > 1 else set()
            assert keys[i] - other_union
        out.update(
            semantic_pairs=len(universe),
            covered_pairs=len(covered),
            uncovered_pairs=len(universe - covered),
            semantic_keys=len(keys),
            basis_keys=len(basis),
            private_witnesses=len(basis),
        )

        state_count = rng.randint(8, 25)
        heights = [rng.randint(0, 8) for _ in range(state_count)]
        edges = [set() for _ in range(state_count)]
        for i in range(1, state_count):
            edges[i].add(rng.randrange(i))
            for _j in range(rng.randint(0, 4)):
                edges[i].add(rng.randrange(state_count))
        edges[0] = set()
        barrier, depth, next_state = minimax_ranks(heights, edges, {0})
        depth_max = max(depth)
        for v in range(1, state_count):
            w = next_state[v]
            assert w is not None and barrier[w] <= barrier[v]
            if barrier[w] == barrier[v]:
                assert depth[w] < depth[v]
            rank_v = barrier[v] * (depth_max + 1) + depth[v]
            rank_w = barrier[w] * (depth_max + 1) + depth[w]
            assert rank_w < rank_v
            out["minimax_moves"] += 1
        out["repair_states"] += state_count

        fibre_count = rng.randint(3, 10)
        token_count = fibre_count + rng.randint(0, 4)
        adjacency = []
        for _f in range(fibre_count):
            neighbours = {j for j in range(token_count) if rng.random() < 0.45}
            if rng.random() < 0.75 and not neighbours:
                neighbours.add(rng.randrange(token_count))
            adjacency.append(neighbours)
        matching_size = maximum_matching(adjacency, token_count)
        if matching_size == fibre_count:
            out["full_move_matchings"] += 1
            primitive_count = rng.randint(8, 20)
            footprints = [
                set(rng.sample(range(primitive_count), rng.randint(1, 4)))
                for _f in range(fibre_count)
            ]
            h = max(map(len, footprints))
            beta = max(sum(x in footprint for footprint in footprints) for x in range(primitive_count))
            chosen = greedy_disjoint(footprints)
            assert len(chosen) >= ceil(fibre_count / (h * (beta - 1) + 1))
            for a in range(len(chosen)):
                for b in range(a):
                    assert footprints[chosen[a]].isdisjoint(footprints[chosen[b]])
            out["matched_moves"] += fibre_count
            out["commuting_moves"] += len(chosen)
        else:
            out["hall_shortages"] += 1

        fixed_old = [rng.randint(0, 5) for _ in range(rng.randint(8, 25))]
        fixed_new = fixed_old[:]
        fixed_credit = 0
        for i in rng.sample(range(len(fixed_new)), rng.randint(1, min(5, len(fixed_new)))):
            decrease = rng.randint(0, fixed_new[i])
            fixed_new[i] -= decrease
            fixed_credit += decrease
        dynamic_old = [rng.randint(0, 4) for _ in range(rng.randint(5, 15))]
        keep_count = rng.randint(0, len(dynamic_old))
        dynamic_credit = sum(dynamic_old[keep_count:])
        dynamic_new = [rng.randint(0, x) for x in dynamic_old[:keep_count]]
        dynamic_new += [0] * rng.randint(0, 6)
        theta_old = sum(fixed_old) + sum(dynamic_old)
        theta_new = sum(fixed_new) + sum(dynamic_new)
        assert theta_new <= theta_old - fixed_credit - dynamic_credit
        out["restart_credit"] += fixed_credit + dynamic_credit
        out["restart_checks"] += 1

        delta_star = rng.randint(2, 10)
        theta_star = rng.randint(4, 20)
        rank_star = rng.randint(5, 30)
        delta_weight = (theta_star + 1) * (rank_star + 1)

        def potential(delta, theta, rank):
            return delta * delta_weight + theta * (rank_star + 1) + rank

        delta = rng.randint(1, delta_star)
        theta = rng.randint(0, theta_star)
        rank = rng.randint(0, rank_star)
        before = potential(delta, theta, rank)
        kind = rng.choice(("supply", "paid", "minimax"))
        if kind == "supply":
            after = potential(delta - 1, rng.randint(0, theta_star), rng.randint(0, rank_star))
        elif kind == "paid" and theta > 0:
            after = potential(delta, theta - 1, rng.randint(0, rank_star))
        else:
            if rank == 0:
                rank = 1
                before = potential(delta, theta, rank)
            after = potential(delta, theta, rank - 1)
        assert after < before
        out["scalar_descents"] += 1
    return out


def main():
    got = audit()
    expected = {
        "semantic_pairs": 99979,
        "covered_pairs": 91818,
        "uncovered_pairs": 8161,
        "semantic_keys": 29744,
        "basis_keys": 17831,
        "private_witnesses": 17831,
        "repair_states": 41485,
        "minimax_moves": 38985,
        "full_move_matchings": 2307,
        "hall_shortages": 193,
        "matched_moves": 15268,
        "commuting_moves": 7100,
        "restart_credit": 34096,
        "restart_checks": 2500,
        "scalar_descents": 2500,
    }
    assert dict(got) == expected
    print(
        f"systems={SYSTEMS} semantic_pairs={got['semantic_pairs']} "
        f"covered={got['covered_pairs']} uncovered={got['uncovered_pairs']} "
        f"basis_keys={got['basis_keys']} private={got['private_witnesses']}"
    )
    print(
        f"repair_states={got['repair_states']} minimax_moves={got['minimax_moves']} "
        f"full_matchings={got['full_move_matchings']} hall_shortages={got['hall_shortages']} "
        f"commuting_moves={got['commuting_moves']}"
    )
    print(
        f"restart_credit={got['restart_credit']} restart_checks={got['restart_checks']} "
        f"scalar_descents={got['scalar_descents']}"
    )


if __name__ == "__main__":
    main()

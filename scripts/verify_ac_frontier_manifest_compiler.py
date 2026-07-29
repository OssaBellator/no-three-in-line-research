#!/usr/bin/env python3
"""Deterministic audit for AC5hy--AC5ic."""
from collections import Counter, deque
from dataclasses import dataclass
from heapq import heappop, heappush
from random import Random

SYSTEMS = 2500
SEED = 20260730
TRACKS = ("AC", "RI", "BDA", "GC", "OP", "SRR", "SAS")
INF = 10**9


@dataclass(frozen=True)
class Key:
    version: int
    cover: frozenset
    values: tuple
    fields_complete: bool = True
    sound: bool = True
    shared_ok: bool = True

    def value_map(self):
        return dict(self.values)


def reverse_delete_basis(keys):
    target = set().union(*(set(k.cover) for k in keys)) if keys else set()
    uncovered = set(target)
    remaining = set(range(len(keys)))
    selected = []
    while uncovered:
        best = max(remaining, key=lambda i: (len(set(keys[i].cover) & uncovered), -i))
        assert set(keys[best].cover) & uncovered
        selected.append(best)
        uncovered -= set(keys[best].cover)
        remaining.remove(best)
    keep = selected[:]
    for i in reversed(selected):
        others = set().union(*(set(keys[j].cover) for j in keep if j != i)) if len(keep) > 1 else set()
        if target <= others:
            keep.remove(i)
    private = {}
    for i in keep:
        others = set().union(*(set(keys[j].cover) for j in keep if j != i)) if len(keep) > 1 else set()
        witness = min(set(keys[i].cover) - others)
        private[i] = witness
    return target, keep, private


def compile_track(universe, keys, version):
    for i, key in enumerate(keys):
        if key.version != version:
            return ("stale_key", i)
        if not key.fields_complete:
            return ("omitted_field", i)
        if not key.shared_ok:
            return ("shared_disagreement", i)
    values = {}
    for i, key in enumerate(keys):
        for pair, value in key.value_map().items():
            if pair not in key.cover:
                return ("unsound_key", i)
            if pair in values and values[pair] != value:
                return ("semantic_conflict", pair)
            values[pair] = value
    target, basis, private = reverse_delete_basis(keys)
    for i in basis:
        if not keys[i].sound:
            return ("unsound_key", private[i])
    uncovered = sorted(set(universe) - target)
    if uncovered:
        return ("semantic_uncovered", uncovered[0])
    return ("ok", values, basis, private)


def minimax_ranks(heights, edges, terminals):
    n = len(heights)
    reverse = [[] for _ in range(n)]
    for v, outs in enumerate(edges):
        for w in outs:
            if not (0 <= w < n):
                return None
            reverse[w].append(v)
    barrier = [INF] * n
    queue = []
    for t in terminals:
        if not (0 <= t < n):
            return None
        barrier[t] = heights[t]
        heappush(queue, (barrier[t], t))
    while queue:
        b, w = heappop(queue)
        if b != barrier[w]:
            continue
        for v in reverse[w]:
            candidate = max(heights[v], b)
            if candidate < barrier[v]:
                barrier[v] = candidate
                heappush(queue, (candidate, v))
    if any(b == INF for b in barrier):
        return None

    depth = [INF] * n
    next_state = [None] * n
    terminal_set = set(terminals)
    for v in range(n):
        if v in terminal_set:
            depth[v] = 0
            continue
        threshold = barrier[v]
        queue = deque([v])
        dist = {v: 0}
        parent = {}
        found = None
        while queue:
            x = queue.popleft()
            if x in terminal_set:
                found = x
                break
            for y in sorted(edges[x]):
                if heights[y] <= threshold and y not in dist:
                    dist[y] = dist[x] + 1
                    parent[y] = x
                    queue.append(y)
        assert found is not None
        depth[v] = dist[found]
        path = [found]
        while path[-1] != v:
            path.append(parent[path[-1]])
        path.reverse()
        next_state[v] = path[1]
    d_star = max(depth)
    rank = [barrier[v] * (d_star + 1) + depth[v] for v in range(n)]
    for v in range(n):
        if v in terminal_set:
            continue
        w = next_state[v]
        assert w is not None and rank[w] < rank[v]
    return barrier, depth, next_state, rank


def make_complete_keys(rng, universe, version):
    key_count = rng.randint(5, 12)
    truth = {x: rng.randrange(2) for x in universe}
    keys = []
    remaining = set(universe)
    for i in range(key_count):
        cover = {x for x in universe if rng.random() < 0.30}
        if i == key_count - 1:
            cover |= remaining
        if not cover:
            cover = {rng.choice(tuple(universe))}
        remaining -= cover
        values = tuple(sorted((x, truth[x]) for x in cover))
        keys.append(Key(version, frozenset(cover), values))
    return truth, keys


def make_repair_graph(rng):
    n = rng.randint(8, 22)
    heights = [rng.randint(0, 8) for _ in range(n)]
    edges = [set() for _ in range(n)]
    edges[0] = set()
    for v in range(1, n):
        edges[v].add(rng.randrange(v))
        for _ in range(rng.randint(0, 3)):
            edges[v].add(rng.randrange(n))
    result = minimax_ranks(heights, edges, {0})
    assert result is not None
    return heights, edges, {0}, result


def make_restart(rng, positive_activation=False):
    fixed_old = [rng.randint(0, 6) for _ in range(rng.randint(6, 18))]
    fixed_new = fixed_old[:]
    fixed_credit = 0
    for i in rng.sample(range(len(fixed_new)), rng.randint(1, min(4, len(fixed_new)))):
        drop = rng.randint(0, fixed_new[i])
        fixed_new[i] -= drop
        fixed_credit += drop
    active_old = [rng.randint(0, 5) for _ in range(rng.randint(4, 12))]
    keep = rng.randint(0, len(active_old))
    active_new = [rng.randint(0, x) for x in active_old[:keep]]
    new_count = rng.randint(1, 5)
    added = [0] * new_count
    if positive_activation:
        added[rng.randrange(new_count)] = rng.randint(1, 4)
    active_new += added
    active_credit = sum(active_old[keep:])
    return {
        "fixed_old": fixed_old,
        "fixed_new": fixed_new,
        "active_old": active_old,
        "active_new": active_new,
        "keep": keep,
        "fixed_credit": fixed_credit,
        "active_credit": active_credit,
    }


def audit_restart(restart):
    keep = restart["keep"]
    added = restart["active_new"][keep:]
    for i, value in enumerate(added):
        if value > 0:
            return ("positive_activation", i)
    theta_old = sum(restart["fixed_old"]) + sum(restart["active_old"])
    theta_new = sum(restart["fixed_new"]) + sum(restart["active_new"])
    expected = theta_old - restart["fixed_credit"] - restart["active_credit"]
    if theta_new > expected:
        return ("restart_increase", theta_new - expected)
    return ("ok", theta_old, theta_new)


def make_manifest(rng, mode):
    tracks = {}
    for s in TRACKS:
        version = 1
        universe = tuple(range(rng.randint(8, 20)))
        truth, keys = make_complete_keys(rng, universe, version)
        tracks[s] = {"version": version, "universe": universe, "truth": truth, "keys": keys}
    heights, edges, terminals, rank_data = make_repair_graph(rng)
    restart = make_restart(rng, positive_activation=(mode == "positive_activation"))
    capacities = {
        "payment": [(f"p{i}", rng.randint(1, 4)) for i in range(rng.randint(2, 8))],
        "ticket": [(f"t{i}", 1) for i in range(rng.randint(2, 8))],
        "reset": [(f"r{i}", 1) for i in range(rng.randint(1, 5))],
    }
    manifest = {
        "tracks": tracks,
        "heights": heights,
        "edges": edges,
        "terminals": terminals,
        "rank_data": rank_data,
        "restart": restart,
        "capacities": capacities,
        "disturbance": rng.randint(0, 8),
        "disturbance_weight": rng.randint(1, 5),
        "delta_star": rng.randint(2, 10),
    }

    if mode == "missing_track":
        del tracks["SAS"]
    elif mode == "semantic_uncovered":
        t = tracks["GC"]
        last = max(t["universe"])
        new_keys = []
        for k in t["keys"]:
            cover = set(k.cover)
            cover.discard(last)
            values = tuple((x, v) for x, v in k.values if x != last)
            if cover:
                new_keys.append(Key(k.version, frozenset(cover), values))
        t["keys"] = new_keys
    elif mode == "semantic_conflict":
        t = tracks["RI"]
        pair = min(t["universe"])
        base = t["truth"][pair]
        t["keys"].append(Key(1, frozenset({pair}), ((pair, 1 - base),)))
    elif mode == "stale_key":
        t = tracks["BDA"]
        k = t["keys"][0]
        t["keys"][0] = Key(0, k.cover, k.values)
    elif mode == "omitted_field":
        t = tracks["OP"]
        k = t["keys"][0]
        t["keys"][0] = Key(k.version, k.cover, k.values, fields_complete=False)
    elif mode == "shared_disagreement":
        t = tracks["SRR"]
        k = t["keys"][0]
        t["keys"][0] = Key(k.version, k.cover, k.values, shared_ok=False)
    elif mode == "unsound_key":
        t = tracks["AC"]
        pair = min(t["universe"])
        cleaned = []
        for k in t["keys"]:
            cover = set(k.cover)
            cover.discard(pair)
            values = tuple((x, v) for x, v in k.values if x != pair)
            if cover:
                cleaned.append(Key(k.version, frozenset(cover), values))
        cleaned.append(Key(1, frozenset({pair}), ((pair, t["truth"][pair]),), sound=False))
        t["keys"] = cleaned
    elif mode == "illegal_edge":
        manifest["edges"][-1].add(len(manifest["heights"]) + 3)
    elif mode == "unreachable_state":
        n = len(manifest["heights"])
        manifest["edges"][-1] = {n - 1}
    elif mode == "duplicate_capacity":
        manifest["capacities"]["ticket"].append(manifest["capacities"]["ticket"][0])
    return manifest


def compile_manifest(manifest):
    if tuple(manifest["tracks"].keys()) != TRACKS:
        missing = [s for s in TRACKS if s not in manifest["tracks"]]
        return ("missing_track", missing[0] if missing else "order")

    basis_total = 0
    private_total = 0
    pair_total = 0
    for s in TRACKS:
        t = manifest["tracks"][s]
        pair_total += len(t["universe"])
        result = compile_track(t["universe"], t["keys"], t["version"])
        if result[0] != "ok":
            return result
        _status, values, basis, private = result
        for pair in t["universe"]:
            if values[pair] != t["truth"][pair]:
                return ("unsound_key", (s, pair))
        basis_total += len(basis)
        private_total += len(private)

    rank_data = minimax_ranks(manifest["heights"], manifest["edges"], manifest["terminals"])
    if rank_data is None:
        n = len(manifest["heights"])
        for v, outs in enumerate(manifest["edges"]):
            bad = [w for w in outs if not (0 <= w < n)]
            if bad:
                return ("illegal_edge", (v, min(bad)))
        return ("unreachable_state", None)
    barrier, depth, next_state, rank = rank_data

    restart_result = audit_restart(manifest["restart"])
    if restart_result[0] != "ok":
        return restart_result
    _, theta_old, theta_new = restart_result

    capacity_total = {}
    for kind, entries in manifest["capacities"].items():
        seen = set()
        total = 0
        for address, amount in entries:
            if address in seen:
                return ("duplicate_capacity", (kind, address))
            if amount < 0:
                return ("negative_capacity", (kind, address))
            seen.add(address)
            total += amount
        capacity_total[kind] = total

    delta_star = manifest["delta_star"]
    theta_star = max(theta_old, theta_new)
    rank_star = max(rank)
    w_delta = (theta_star + 1) * (rank_star + 1)
    psi_star = delta_star * w_delta + theta_star * (rank_star + 1) + rank_star
    episode_bound = (
        (capacity_total["reset"] + 1) * psi_star
        + manifest["disturbance"] * manifest["disturbance_weight"]
        + capacity_total["payment"]
        + capacity_total["ticket"]
    )

    delta = delta_star
    theta = theta_star
    repair = rank_star
    before = delta * w_delta + theta * (rank_star + 1) + repair
    after_supply = (delta - 1) * w_delta + theta_star * (rank_star + 1) + rank_star
    assert after_supply < before
    if theta > 0:
        after_restart = delta * w_delta + (theta - 1) * (rank_star + 1) + rank_star
        assert after_restart < before
    nonterm = [v for v in range(len(rank)) if v not in manifest["terminals"]]
    for v in nonterm:
        w = next_state[v]
        assert rank[w] < rank[v]

    return (
        "valid",
        {
            "pairs": pair_total,
            "basis": basis_total,
            "private": private_total,
            "states": len(rank),
            "moves": len(nonterm),
            "theta_credit": theta_old - theta_new,
            "psi_star": psi_star,
            "episode_bound": episode_bound,
            "payment_capacity": capacity_total["payment"],
            "ticket_capacity": capacity_total["ticket"],
            "reset_capacity": capacity_total["reset"],
        },
    )


def audit():
    rng = Random(SEED)
    modes = (
        "valid",
        "missing_track",
        "semantic_uncovered",
        "semantic_conflict",
        "stale_key",
        "omitted_field",
        "shared_disagreement",
        "unsound_key",
        "illegal_edge",
        "unreachable_state",
        "positive_activation",
        "duplicate_capacity",
    )
    out = Counter()
    for i in range(SYSTEMS):
        mode = modes[i % len(modes)]
        result = compile_manifest(make_manifest(rng, mode))
        outcome = result[0]
        expected = {
            "valid": "valid",
            "missing_track": "missing_track",
            "semantic_uncovered": "semantic_uncovered",
            "semantic_conflict": "semantic_conflict",
            "stale_key": "stale_key",
            "omitted_field": "omitted_field",
            "shared_disagreement": "shared_disagreement",
            "unsound_key": "unsound_key",
            "illegal_edge": "illegal_edge",
            "unreachable_state": "unreachable_state",
            "positive_activation": "positive_activation",
            "duplicate_capacity": "duplicate_capacity",
        }[mode]
        assert outcome == expected, (mode, result)
        out[outcome] += 1
        if outcome == "valid":
            cert = result[1]
            for key, value in cert.items():
                out[key] += value
    return out


def main():
    got = audit()
    expected = {
        "valid": 209,
        "missing_track": 209,
        "semantic_uncovered": 209,
        "semantic_conflict": 209,
        "stale_key": 208,
        "omitted_field": 208,
        "shared_disagreement": 208,
        "unsound_key": 208,
        "illegal_edge": 208,
        "unreachable_state": 208,
        "positive_activation": 208,
        "duplicate_capacity": 208,
        "pairs": 20303,
        "basis": 5957,
        "private": 5957,
        "states": 3244,
        "moves": 3035,
        "theta_credit": 3830,
        "psi_star": 3285903,
        "episode_bound": 13314334,
        "payment_capacity": 2494,
        "ticket_capacity": 1043,
        "reset_capacity": 642,
    }
    assert dict(got) == expected, (dict(got), expected)
    print(
        f"systems={SYSTEMS} valid={got['valid']} routed_failures={SYSTEMS-got['valid']} "
        f"pairs={got['pairs']} basis={got['basis']} private={got['private']}"
    )
    print(
        f"states={got['states']} strict_moves={got['moves']} "
        f"restart_credit={got['theta_credit']} psi_star_sum={got['psi_star']}"
    )
    print(
        f"episode_bound_sum={got['episode_bound']} payment={got['payment_capacity']} "
        f"tickets={got['ticket_capacity']} resets={got['reset_capacity']}"
    )


if __name__ == "__main__":
    main()

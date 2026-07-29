#!/usr/bin/env python3
"""Deterministic audit for AC5ii--AC5im."""

from collections import Counter, deque
from random import Random
import heapq

SYSTEMS = 2500
SEED = 20260730
INF = 10**9
CATEGORIES = (
    "valid",
    "stale",
    "state_conflict",
    "pair_conflict",
    "uncovered_pair",
    "uncovered_state",
    "uncovered_edge",
    "switch_violation",
    "capacity_conflict",
    "unreachable",
)


def reachable_states(n, edges, terminals):
    reverse = [[] for _ in range(n)]
    for v, w in edges:
        reverse[w].append(v)
    seen = set(terminals)
    queue = deque(terminals)
    while queue:
        w = queue.popleft()
        for v in reverse[w]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return seen


def minimax_ranks(states, edges, terminals):
    n = len(states)
    reverse = [[] for _ in range(n)]
    for v, w in edges:
        reverse[w].append(v)

    heights = [states[i]["height"] for i in range(n)]
    barrier = [INF] * n
    queue = []
    for terminal in terminals:
        barrier[terminal] = heights[terminal]
        heapq.heappush(queue, (barrier[terminal], terminal))

    while queue:
        current, w = heapq.heappop(queue)
        if current != barrier[w]:
            continue
        for v in reverse[w]:
            candidate = max(heights[v], current)
            if candidate < barrier[v]:
                barrier[v] = candidate
                heapq.heappush(queue, (candidate, v))

    if any(value >= INF for value in barrier):
        return None

    terminals = set(terminals)
    depth = [INF] * n
    next_state = [None] * n
    for v in range(n):
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
            outgoing = sorted(w for u, w in edges if u == x and heights[w] <= threshold)
            for y in outgoing:
                if y not in distance:
                    distance[y] = distance[x] + 1
                    parent[y] = x
                    bfs.append(y)
        if found is None:
            return None
        depth[v] = distance[found]
        path = [found]
        while path[-1] != v:
            path.append(parent[path[-1]])
        path.reverse()
        next_state[v] = path[1]

    depth_star = max(depth)
    rank = [barrier[v] * (depth_star + 1) + depth[v] for v in range(n)]
    for v in range(n):
        if v not in terminals:
            assert rank[next_state[v]] < rank[v]
    return barrier, depth, rank, next_state


def generate_base(rng):
    state_count = rng.randint(7, 18)
    template_count = rng.randint(3, 6)
    version = rng.randint(1, 4)

    states = {}
    for state in range(state_count):
        states[state] = {
            "version": version,
            "terminal": state == 0,
            "height": rng.randint(0, 8),
            "delta": rng.randint(0, 5),
            "theta": rng.randint(0, 8),
            "zone": state % template_count,
        }
    states[0]["height"] = 0

    edge_keys = {}
    for state in range(1, state_count):
        edge_keys[(state, rng.randrange(state))] = None
    for state in range(2, state_count):
        for _ in range(rng.randint(0, 2)):
            edge_keys.setdefault((state, rng.randrange(state)), None)

    capacity_kinds = ("pay", "ticket", "reset", "disturbance")
    capacity_count = rng.randint(8, 16)
    capacities = {}
    for index in range(capacity_count):
        kind = capacity_kinds[index % len(capacity_kinds)]
        amount = rng.randint(1, 5)
        weight = rng.randint(1, 4) if kind == "disturbance" else 0
        capacities[f"{kind}:{index}"] = (kind, amount, weight)
    reset_addresses = [address for address, record in capacities.items() if record[0] == "reset"]

    edges = {}
    for v, w in sorted(edge_keys):
        cross = states[v]["zone"] != states[w]["zone"]
        if cross and rng.random() < 0.35:
            record = {
                "v": v,
                "w": w,
                "cross": True,
                "inserted_mass": rng.randint(0, 2),
                "reset_addr": rng.choice(reset_addresses),
            }
        else:
            record = {
                "v": v,
                "w": w,
                "cross": cross,
                "inserted_mass": 0,
                "reset_addr": None,
            }
        edges[(v, w)] = record

    pair_count = rng.randint(15, 45)
    pairs = {pair: rng.randint(0, 1) for pair in range(pair_count)}
    templates = [
        {"version": version, "states": {}, "edges": {}, "pairs": {}, "caps": {}}
        for _ in range(template_count)
    ]

    for state, record in states.items():
        templates[record["zone"]]["states"][state] = record.copy()
    for template in templates:
        template["states"][0] = states[0].copy()

    for index, (edge, record) in enumerate(sorted(edges.items())):
        template_index = index % template_count
        template = templates[template_index]
        template["edges"][edge] = record.copy()
        v, w = edge
        template["states"][v] = states[v].copy()
        template["states"][w] = states[w].copy()
        if index % 5 == 0:
            duplicate = templates[(template_index + 1) % template_count]
            duplicate["edges"][edge] = record.copy()
            duplicate["states"][v] = states[v].copy()
            duplicate["states"][w] = states[w].copy()

    for pair, value in pairs.items():
        if pair == 0:
            indices = range(template_count)
        else:
            first = pair % template_count
            indices = [first]
            if pair % 3 == 0:
                indices.append((first + 1) % template_count)
        for index in indices:
            templates[index]["pairs"][pair] = value

    addresses = list(capacities)
    for index, address in enumerate(addresses):
        if index == 0:
            indices = range(template_count)
        else:
            indices = [index % template_count]
            if index % 3 == 0:
                indices.append((index + 1) % template_count)
        for template_index in indices:
            templates[template_index]["caps"][address] = capacities[address]

    return {
        "version": version,
        "states": states,
        "edges": edges,
        "terminals": {0},
        "pairs": pairs,
        "caps": capacities,
        "templates": templates,
    }


def mutate_case(manifest, category):
    templates = manifest["templates"]
    if category == "valid":
        return
    if category == "stale":
        templates[0]["version"] = manifest["version"] + 1
    elif category == "state_conflict":
        templates[1]["states"][0] = templates[1]["states"][0].copy()
        templates[1]["states"][0]["height"] += 1
    elif category == "pair_conflict":
        templates[1]["pairs"][0] = 1 - templates[1]["pairs"][0]
    elif category == "uncovered_pair":
        pair = max(manifest["pairs"])
        for template in templates:
            template["pairs"].pop(pair, None)
    elif category == "uncovered_state":
        state = max(manifest["states"])
        for template in templates:
            template["states"].pop(state, None)
    elif category == "uncovered_edge":
        edge = sorted(manifest["edges"])[0]
        for template in templates:
            template["edges"].pop(edge, None)
    elif category == "switch_violation":
        edge = (1, 0)
        if edge not in manifest["edges"]:
            edge = next(key for key, record in manifest["edges"].items() if record["cross"])
        bad = manifest["edges"][edge].copy()
        bad["inserted_mass"] = 1
        bad["reset_addr"] = None
        manifest["edges"][edge] = bad
        for template in templates:
            if edge in template["edges"]:
                template["edges"][edge] = bad.copy()
    elif category == "capacity_conflict":
        address = next(iter(manifest["caps"]))
        kind, amount, weight = templates[1]["caps"][address]
        templates[1]["caps"][address] = (kind, amount + 1, weight)
    elif category == "unreachable":
        state = max(manifest["states"])
        outgoing = [edge for edge in manifest["edges"] if edge[0] == state]
        for edge in outgoing:
            manifest["edges"].pop(edge)
            for template in templates:
                template["edges"].pop(edge, None)
    else:
        raise ValueError(category)


def compile_atlas(manifest):
    version = manifest["version"]
    states = manifest["states"]
    edges = manifest["edges"]
    pairs = manifest["pairs"]
    capacities = manifest["caps"]
    templates = manifest["templates"]

    for index, template in enumerate(templates):
        if template["version"] != version:
            return "stale", index

    seen_states = {}
    for index, template in enumerate(templates):
        for state, record in sorted(template["states"].items()):
            if state not in states:
                return "unknown_state", (index, state)
            if record != states[state]:
                return "state_conflict", (index, state)
            if state in seen_states and seen_states[state] != record:
                return "state_conflict", (index, state)
            seen_states[state] = record

    seen_pairs = {}
    for index, template in enumerate(templates):
        for pair, value in sorted(template["pairs"].items()):
            if pair not in pairs:
                return "unknown_pair", (index, pair)
            if value != pairs[pair]:
                return "pair_conflict", (index, pair)
            if pair in seen_pairs and seen_pairs[pair] != value:
                return "pair_conflict", (index, pair)
            seen_pairs[pair] = value

    for pair in sorted(pairs):
        if pair not in seen_pairs:
            return "uncovered_pair", pair
    for state in sorted(states):
        if state not in seen_states:
            return "uncovered_state", state

    seen_edges = {}
    for index, template in enumerate(templates):
        for edge, record in sorted(template["edges"].items()):
            if edge not in edges:
                return "unknown_edge", (index, edge)
            if record != edges[edge]:
                return "edge_conflict", (index, edge)
            if edge in seen_edges and seen_edges[edge] != record:
                return "edge_conflict", (index, edge)
            seen_edges[edge] = record
    for edge in sorted(edges):
        if edge not in seen_edges:
            return "uncovered_edge", edge

    for edge, record in sorted(edges.items()):
        if record["cross"] and record["inserted_mass"] > 0:
            reset_address = record["reset_addr"]
            if (
                reset_address is None
                or reset_address not in capacities
                or capacities[reset_address][0] != "reset"
            ):
                return "switch_violation", edge

    seen_capacities = {}
    raw_references = 0
    for index, template in enumerate(templates):
        for address, record in sorted(template["caps"].items()):
            raw_references += 1
            if address not in capacities:
                return "unknown_capacity", (index, address)
            if record != capacities[address]:
                return "capacity_conflict", (index, address)
            if address in seen_capacities and seen_capacities[address] != record:
                return "capacity_conflict", (index, address)
            seen_capacities[address] = record
    for address in sorted(capacities):
        if address not in seen_capacities:
            return "uncovered_capacity", address

    reachable = reachable_states(len(states), set(edges), manifest["terminals"])
    if len(reachable) < len(states):
        return "unreachable", min(set(states) - reachable)

    ranks = minimax_ranks(states, edges, manifest["terminals"])
    assert ranks is not None
    _, _, rank, _ = ranks
    theta_star = max(record["theta"] for record in states.values())
    rank_star = max(rank)
    delta_weight = (theta_star + 1) * (rank_star + 1)
    psi = {
        state: record["delta"] * delta_weight
        + record["theta"] * (rank_star + 1)
        + rank[state]
        for state, record in states.items()
    }
    psi_star = max(psi.values())

    pay = sum(amount for kind, amount, _ in capacities.values() if kind == "pay")
    ticket = sum(amount for kind, amount, _ in capacities.values() if kind == "ticket")
    reset = sum(amount for kind, amount, _ in capacities.values() if kind == "reset")
    disturbance = sum(amount for kind, amount, _ in capacities.values() if kind == "disturbance")
    disturbance_weight = max(
        [weight for kind, _, weight in capacities.values() if kind == "disturbance"] or [0]
    )
    episode_bound = (
        (reset + 1) * psi_star
        + disturbance * disturbance_weight
        + pay
        + ticket
    )

    bridges = sum(record["cross"] for record in edges.values())
    rescues = 0
    for state, record in states.items():
        if state in manifest["terminals"]:
            continue
        owner = record["zone"]
        local_edges = set(templates[owner]["edges"])
        local_reachable = reachable_states(len(states), local_edges, manifest["terminals"])
        if state not in local_reachable:
            rescues += 1

    return "valid", {
        "templates": len(templates),
        "pairs": len(pairs),
        "states": len(states),
        "edges": len(edges),
        "raw_cap_refs": raw_references,
        "unique_caps": len(capacities),
        "dedup_saved": raw_references - len(capacities),
        "bridges": bridges,
        "rescues": rescues,
        "psi_star": psi_star,
        "episode": episode_bound,
        "rank_star": rank_star,
    }


def audit():
    rng = Random(SEED)
    output = Counter()
    for index in range(SYSTEMS):
        manifest = generate_base(rng)
        category = CATEGORIES[index % len(CATEGORIES)]
        mutate_case(manifest, category)
        result, payload = compile_atlas(manifest)
        assert result == category, (index, category, result, payload)
        output[result] += 1
        if result == "valid":
            output.update(payload)
    return output


def main():
    got = audit()
    expected = {
        "valid": 250,
        "stale": 250,
        "state_conflict": 250,
        "pair_conflict": 250,
        "uncovered_pair": 250,
        "uncovered_state": 250,
        "uncovered_edge": 250,
        "switch_violation": 250,
        "capacity_conflict": 250,
        "unreachable": 250,
        "templates": 1115,
        "pairs": 7283,
        "states": 3080,
        "edges": 4774,
        "raw_cap_refs": 4672,
        "unique_caps": 2982,
        "dedup_saved": 1690,
        "bridges": 4051,
        "rescues": 2069,
        "psi_star": 417436,
        "episode": 3905521,
        "rank_star": 8318,
    }
    assert dict(got) == expected
    print(
        f"systems={SYSTEMS} valid={got['valid']} intended_failures={SYSTEMS-got['valid']} "
        f"templates={got['templates']} pairs={got['pairs']} states={got['states']} edges={got['edges']}"
    )
    print(
        f"bridges={got['bridges']} cross_kernel_rescues={got['rescues']} "
        f"raw_capacity_refs={got['raw_cap_refs']} unique_capacities={got['unique_caps']} "
        f"deduplicated_aliases={got['dedup_saved']}"
    )
    print(
        f"aggregate_rank_star={got['rank_star']} aggregate_psi_star={got['psi_star']} "
        f"aggregate_episode_bound={got['episode']}"
    )


if __name__ == "__main__":
    main()

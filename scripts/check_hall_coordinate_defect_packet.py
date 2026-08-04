#!/usr/bin/env python3
from collections import Counter
from itertools import combinations

MOTIFS = tuple(tuple(range(3 * index, 3 * index + 3)) for index in range(10))
RESOURCE_LISTS = tuple(
    frozenset((1000 + 3 * index + local, 2000 + index) for local in range(3))
    for index in range(10)
)

DEFECT_EDGES = [
    ("s0", "h0"),
    ("s0", "h1"),
    ("s1", "h2"),
    ("s2", "h2"),
]
DEFECT_EDGES.extend((f"s{centre - 1}", f"h{centre - 1}") for centre in range(4, 30))
DEFECT_EDGES = tuple(DEFECT_EDGES)
LEFT_PORT = 29
RIGHT_PORT = 28


def conflict_adjacency(defect_edges):
    adjacency = [set() for _ in defect_edges]
    for first, second in combinations(range(len(defect_edges)), 2):
        if (
            defect_edges[first][0] == defect_edges[second][0]
            or defect_edges[first][1] == defect_edges[second][1]
        ):
            adjacency[first].add(second)
            adjacency[second].add(first)
    return tuple(frozenset(neighbours) for neighbours in adjacency)


def component_sizes(adjacency):
    seen = set()
    result = []
    for start in range(len(adjacency)):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        vertices = []
        while stack:
            vertex = stack.pop()
            vertices.append(vertex)
            for neighbour in adjacency[vertex]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        result.append((len(vertices), sum(len(adjacency[v]) for v in vertices) // 2))
    return tuple(sorted(result))


def maximum_independent_set_size(adjacency):
    closed = []
    for vertex, neighbours in enumerate(adjacency):
        mask = 1 << vertex
        for neighbour in neighbours:
            mask |= 1 << neighbour
        closed.append(mask)
    memo = {}

    def solve(remaining):
        if not remaining:
            return 0
        if remaining in memo:
            return memo[remaining]
        vertex = (remaining & -remaining).bit_length() - 1
        answer = max(
            solve(remaining & ~(1 << vertex)),
            1 + solve(remaining & ~closed[vertex]),
        )
        memo[remaining] = answer
        return answer

    return solve((1 << len(adjacency)) - 1)


def cross(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        - (second[1] - first[1]) * (third[0] - first[0])
    )


def coordinate_realization(defect_edges, ordered=False):
    if ordered:
        source_labels = tuple(dict.fromkeys(source for source, _ in defect_edges))
        host_labels = tuple(dict.fromkeys(host for _, host in defect_edges))
    else:
        source_labels = sorted(
            {source for source, _ in defect_edges}, key=lambda label: int(label[1:])
        )
        host_labels = sorted(
            {host for _, host in defect_edges}, key=lambda label: int(label[1:])
        )
    source_x = {label: 2 ** (index + 1) for index, label in enumerate(source_labels)}
    host_y = {label: 3 ** (index + 1) for index, label in enumerate(host_labels)}
    return tuple((source_x[source], host_y[host]) for source, host in defect_edges)


def chain_defect_edges(copies):
    result = []
    for packet in range(copies):
        result.extend((
            (f"s{packet}_0", f"h{packet}_0"),
            (f"s{packet}_0", f"h{packet}_1"),
            (f"s{packet}_1", f"h{packet}_2"),
            (f"s{packet}_2", f"h{packet}_2"),
        ))
        for centre in range(4, 28):
            result.append((f"s{packet}_{centre - 1}", f"h{packet}_{centre - 1}"))
        right_host = f"interface_{packet}" if packet < copies - 1 else f"right_end_{packet}"
        left_host = f"interface_{packet - 1}" if packet > 0 else f"left_end_{packet}"
        result.append((f"s{packet}_right", right_host))
        result.append((f"s{packet}_left", left_host))
    return tuple(result)


def exact_boundary_table(adjacency):
    boundary = {LEFT_PORT, RIGHT_PORT}
    table = {}
    for left_selected in (0, 1):
        for right_selected in (0, 1):
            selected = {
                vertex
                for vertex, flag in ((LEFT_PORT, left_selected), (RIGHT_PORT, right_selected))
                if flag
            }
            allowed = [vertex for vertex in range(len(adjacency)) if vertex not in boundary]
            local_index = {vertex: index for index, vertex in enumerate(allowed)}
            local_adjacency = tuple(
                frozenset(
                    local_index[neighbour]
                    for neighbour in adjacency[vertex]
                    if neighbour in local_index
                )
                for vertex in allowed
            )
            table[(left_selected, right_selected)] = (
                len(selected) + maximum_independent_set_size(local_adjacency)
            )
    return table


def transfer_chain_values(table, copies):
    previous = {
        right: max(table[(left, right)] for left in (0, 1))
        for right in (0, 1)
    }
    values = [max(previous.values())]
    for _ in range(1, copies):
        current = {}
        for right in (0, 1):
            current[right] = max(
                previous[old_right] + table[(left, right)]
                for old_right in (0, 1)
                for left in (0, 1)
                if not (old_right and left)
            )
        previous = current
        values.append(max(previous.values()))
    return tuple(values)


assert sorted(vertex for motif in MOTIFS for vertex in motif) == list(range(30))
assert all(
    not (RESOURCE_LISTS[first] & RESOURCE_LISTS[second])
    for first, second in combinations(range(10), 2)
)
source_loads = Counter(source for source, _ in DEFECT_EDGES)
host_loads = Counter(host for _, host in DEFECT_EDGES)
assert Counter(source_loads.values()) == Counter({1: 28, 2: 1})
assert Counter(host_loads.values()) == Counter({1: 28, 2: 1})

ADJACENCY = conflict_adjacency(DEFECT_EDGES)
assert component_sizes(ADJACENCY) == ((1, 0),) * 26 + ((2, 1),) * 2
assert maximum_independent_set_size(ADJACENCY) == 28

POINTS = coordinate_realization(DEFECT_EDGES)
assert len(set(POINTS)) == 30
assert all(cross(*triple) != 0 for triple in combinations(POINTS, 3))
for first, second in combinations(range(30), 2):
    coordinate_conflict = (
        POINTS[first][0] == POINTS[second][0]
        or POINTS[first][1] == POINTS[second][1]
    )
    assert coordinate_conflict == (second in ADJACENCY[first])

TABLE = exact_boundary_table(ADJACENCY)
assert TABLE == {(0, 0): 26, (0, 1): 27, (1, 0): 27, (1, 1): 28}
CHAIN_VALUES = transfer_chain_values(TABLE, 12)
assert CHAIN_VALUES == tuple(27 * copies + 1 for copies in range(1, 13))

chain_coordinate_bit_lengths = []
for copies in range(1, 13):
    vertices = 30 * copies
    conflict_edges = 3 * copies - 1
    assert vertices - conflict_edges == CHAIN_VALUES[copies - 1]
    chain_edges = chain_defect_edges(copies)
    chain_adjacency = conflict_adjacency(chain_edges)
    assert sum(len(neighbours) for neighbours in chain_adjacency) // 2 == conflict_edges
    assert max(len(neighbours) for neighbours in chain_adjacency) == 1
    if copies <= 6:
        chain_points = coordinate_realization(chain_edges, ordered=True)
        assert len(set(chain_points)) == vertices
        assert all(cross(*triple) != 0 for triple in combinations(chain_points, 3))
        for first, second in combinations(range(vertices), 2):
            coordinate_conflict = (
                chain_points[first][0] == chain_points[second][0]
                or chain_points[first][1] == chain_points[second][1]
            )
            assert coordinate_conflict == (second in chain_adjacency[first])
        chain_coordinate_bit_lengths.append(
            max(max(abs(x), abs(y)) for x, y in chain_points).bit_length()
        )

print({
    "motifs": 10,
    "centres": 30,
    "pairwise_resource_disjoint_motifs": 10,
    "source_load_histogram": dict(sorted(Counter(source_loads.values()).items())),
    "host_load_histogram": dict(sorted(Counter(host_loads.values()).items())),
    "centre_conflict_components": {"isolates": 26, "edges": 2},
    "single_packet_retention": 28,
    "coordinate_no_three": True,
    "maximum_coordinate_bit_length": max(max(abs(x), abs(y)) for x, y in POINTS).bit_length(),
    "boundary_table": TABLE,
    "chain_values_1_through_12": CHAIN_VALUES,
    "explicit_coordinate_chain_checks": 6,
    "chain_coordinate_bit_lengths": tuple(chain_coordinate_bit_lengths),
    "exact_chain_formula": "27*K+1",
    "asymptotic_transfer_rate": 27,
    "evidence_level": "synthetic_coordinate_defect_packet",
    "status": "passed",
})

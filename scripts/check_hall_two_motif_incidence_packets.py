#!/usr/bin/env python3
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations

CENTRES = 6
LEFT = (0, 1)
RIGHT = (2, 3)
INTERNAL = (4, 5)
NEGATIVE_INFINITY = -10**9
STATES = range(4)


def pair_partitions(size):
    result = []

    def recurse(remaining, blocks):
        if not remaining:
            result.append(tuple(blocks))
            return
        first = min(remaining)
        rest = set(remaining)
        rest.remove(first)
        recurse(rest, blocks + ((first,),))
        for second in sorted(rest):
            next_remaining = set(rest)
            next_remaining.remove(second)
            recurse(next_remaining, blocks + ((first, second),))

    recurse(set(range(size)), tuple())
    return tuple(result)


def conflict_graph(source_partition, host_partition):
    edges = set()
    for partition in (source_partition, host_partition):
        for block in partition:
            if len(block) == 2:
                first, second = block
                edges.add((min(first, second), max(first, second)))
    return tuple(sorted(edges))


def independent(mask, edges):
    return all(not (mask & (1 << first) and mask & (1 << second)) for first, second in edges)


def transfer_table(edges):
    table = [[NEGATIVE_INFINITY] * 4 for _ in STATES]
    for mask in range(1 << CENTRES):
        if not independent(mask, edges):
            continue
        left_state = ((mask >> LEFT[0]) & 1) | (((mask >> LEFT[1]) & 1) << 1)
        right_state = ((mask >> RIGHT[0]) & 1) | (((mask >> RIGHT[1]) & 1) << 1)
        table[left_state][right_state] = max(
            table[left_state][right_state], mask.bit_count()
        )
    initial = [max(table[left_state][right_state] for left_state in STATES) for right_state in STATES]
    transition = [[NEGATIVE_INFINITY] * 4 for _ in STATES]
    for previous_right in STATES:
        for current_right in STATES:
            transition[previous_right][current_right] = max(
                table[current_left][current_right]
                for current_left in STATES
                if previous_right & current_left == 0
            )
    return table, initial, transition


def transfer_value(edges, packet_count):
    _, initial, transition = transfer_table(edges)
    values = list(initial)
    for _ in range(packet_count - 1):
        values = [
            max(
                values[previous_right] + transition[previous_right][current_right]
                for previous_right in STATES
            )
            for current_right in STATES
        ]
    return max(values)


def reachable_states(initial, transition):
    reached = {
        state for state, value in enumerate(initial)
        if value > NEGATIVE_INFINITY // 2
    }
    changed = True
    while changed:
        changed = False
        for first in tuple(reached):
            for second, weight in enumerate(transition[first]):
                if weight > NEGATIVE_INFINITY // 2 and second not in reached:
                    reached.add(second)
                    changed = True
    return tuple(sorted(reached))


def maximum_cycle_mean(edges):
    _, initial, transition = transfer_table(edges)
    reached = reachable_states(initial, transition)
    best = None
    for length in range(1, len(reached) + 1):
        for cycle in permutations(reached, length):
            total = 0
            valid = True
            for index in range(length):
                weight = transition[cycle[index]][cycle[(index + 1) % length]]
                if weight <= NEGATIVE_INFINITY // 2:
                    valid = False
                    break
                total += weight
            if valid:
                mean = Fraction(total, length)
                if best is None or mean > best:
                    best = mean
    assert best is not None
    return best


def chain_graph(packet_edges, packet_count):
    edges = set()
    for packet in range(packet_count):
        offset = packet * CENTRES
        for first, second in packet_edges:
            edges.add((offset + first, offset + second))
    for packet in range(packet_count - 1):
        previous = packet * CENTRES
        current = (packet + 1) * CENTRES
        edges.add((previous + RIGHT[0], current + LEFT[0]))
        edges.add((previous + RIGHT[1], current + LEFT[1]))
    return packet_count * CENTRES, tuple(sorted(edges))


def independence_number(vertex_count, edges):
    adjacency = [0] * vertex_count
    for first, second in edges:
        adjacency[first] |= 1 << second
        adjacency[second] |= 1 << first

    @lru_cache(None)
    def solve(mask):
        if mask == 0:
            return 0
        isolated = 0
        scan = mask
        while scan:
            bit = scan & -scan
            vertex = bit.bit_length() - 1
            scan -= bit
            if adjacency[vertex] & mask == 0:
                isolated += 1
                mask -= bit
        if mask == 0:
            return isolated
        vertex = max(
            (candidate for candidate in range(vertex_count) if mask & (1 << candidate)),
            key=lambda candidate: (adjacency[candidate] & mask).bit_count(),
        )
        skip = solve(mask & ~(1 << vertex))
        take = 1 + solve(mask & ~(1 << vertex) & ~adjacency[vertex])
        return isolated + max(skip, take)

    return solve((1 << vertex_count) - 1)


partitions = pair_partitions(CENTRES)
assert len(partitions) == 76
incidence_multiplicity = defaultdict(int)
for source_partition in partitions:
    for host_partition in partitions:
        incidence_multiplicity[conflict_graph(source_partition, host_partition)] += 1

assert sum(incidence_multiplicity.values()) == 76**2 == 5776
assert len(incidence_multiplicity) == 1636
assert Counter(map(len, incidence_multiplicity)) == {
    0: 1,
    1: 15,
    2: 105,
    3: 375,
    4: 675,
    5: 405,
    6: 60,
}

cycle_mean_histogram = Counter()
packet_threshold_histogram = Counter()
one_packet_histogram = Counter()
strict_additive_improvements = 0
maximum_additive_improvement = 0
direct_checks = 0

for edges in sorted(incidence_multiplicity):
    one_packet = transfer_value(edges, 1)
    one_packet_histogram[one_packet] += 1
    cycle_mean_histogram[maximum_cycle_mean(edges)] += 1
    threshold = next(
        packet_count
        for packet_count in range(1, 15)
        if transfer_value(edges, packet_count) >= 28
    )
    packet_threshold_histogram[threshold] += 1
    for packet_count in range(1, 5):
        exact = transfer_value(edges, packet_count)
        vertex_count, chain_edges = chain_graph(edges, packet_count)
        direct = independence_number(vertex_count, chain_edges)
        assert exact == direct
        additive = packet_count * one_packet - 2 * (packet_count - 1)
        assert exact >= additive
        improvement = exact - additive
        strict_additive_improvements += int(improvement > 0)
        maximum_additive_improvement = max(maximum_additive_improvement, improvement)
        direct_checks += 1

assert direct_checks == 1636 * 4 == 6544
assert one_packet_histogram == {3: 660, 4: 900, 5: 75, 6: 1}
assert cycle_mean_histogram == {
    Fraction(3, 1): 1059,
    Fraction(4, 1): 441,
    Fraction(7, 2): 120,
    Fraction(10, 3): 16,
}
assert packet_threshold_histogram == {7: 441, 8: 120, 9: 415, 10: 660}
assert strict_additive_improvements == 4866
assert maximum_additive_improvement == 6

example_edges = ((0, 1),)
assert example_edges in incidence_multiplicity
assert [transfer_value(example_edges, count) for count in range(1, 8)] == [
    5, 9, 13, 17, 21, 25, 29,
]
assert next(
    count for count in range(1, 15)
    if count * 5 - 2 * (count - 1) >= 28
) == 9

print({
    "centres_per_packet": CENTRES,
    "motifs_per_packet": 2,
    "source_partitions": len(partitions),
    "host_partitions": len(partitions),
    "incidence_tables": 5776,
    "distinct_realisable_conflict_graphs": len(incidence_multiplicity),
    "all_simple_graphs": 1 << (CENTRES * (CENTRES - 1) // 2),
    "realisable_characterisation": "union of one source matching and one host matching; equivalently path/even-cycle components",
    "edge_count_histogram": dict(sorted(Counter(map(len, incidence_multiplicity)).items())),
    "one_packet_independence_histogram": dict(sorted(one_packet_histogram.items())),
    "cycle_mean_histogram": {str(value): count for value, count in sorted(cycle_mean_histogram.items())},
    "packet_count_for_28_histogram": dict(sorted(packet_threshold_histogram.items())),
    "direct_chain_checks": direct_checks,
    "strict_improvements_over_two_edge_charge": strict_additive_improvements,
    "maximum_four_packet_improvement": maximum_additive_improvement,
    "strict_example": {
        "internal_conflicts": example_edges,
        "exact_counts_1_through_7": [5, 9, 13, 17, 21, 25, 29],
        "exact_packets_for_28": 7,
        "additive_packets_for_28": 9,
    },
    "remaining_gap": "realise one audited incidence packet by explicit coordinate motifs and repeat its labelled boundary without additional conflicts",
    "evidence_level": "exact_two_motif_defect_incidence_packet_classification",
    "status": "passed",
})

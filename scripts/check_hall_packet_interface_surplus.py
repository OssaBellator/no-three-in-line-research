#!/usr/bin/env python3


def independence_number(vertex_count, edges):
    edges = tuple(tuple(sorted(edge)) for edge in edges)
    best = 0
    for mask in range(1 << vertex_count):
        if all(not ((mask >> first) & 1 and (mask >> second) & 1)
               for first, second in edges):
            best = max(best, mask.bit_count())
    return best


def maximum_matching(edges):
    edges = tuple(edges)
    best = 0

    def search(index, used, count):
        nonlocal best
        if index == len(edges):
            best = max(best, count)
            return
        search(index + 1, used, count)
        first, second = edges[index]
        if first not in used and second not in used:
            search(index + 1, used | {first, second}, count + 1)

    search(0, set(), 0)
    return best


def packet_graphs():
    graphs = []
    for left_size in range(1, 3):
        for right_size in range(1, 3):
            possible = tuple(
                (left, left_size + right)
                for left in range(left_size)
                for right in range(right_size)
            )
            for mask in range(1 << len(possible)):
                edges = tuple(
                    edge for index, edge in enumerate(possible)
                    if mask & (1 << index)
                )
                degree = [0] * (left_size + right_size)
                for first, second in edges:
                    degree[first] += 1
                    degree[second] += 1
                assert max(degree, default=0) <= 2
                graphs.append((
                    left_size + right_size,
                    edges,
                    maximum_matching(edges),
                ))
    return tuple(graphs)


def cross_matchings(first_size, second_size):
    possible = tuple(
        (first, first_size + second)
        for first in range(first_size)
        for second in range(second_size)
    )
    answer = []

    def search(index, used_first, used_second, chosen):
        if index == len(possible):
            answer.append(tuple(chosen))
            return
        first, shifted_second = possible[index]
        second = shifted_second - first_size
        search(index + 1, used_first, used_second, chosen)
        if first not in used_first and second not in used_second:
            chosen.append((first, shifted_second))
            search(
                index + 1,
                used_first | {first},
                used_second | {second},
                chosen,
            )
            chosen.pop()

    search(0, set(), set(), [])
    return tuple(answer)


PACKETS = packet_graphs()
assert len(PACKETS) == 26

cases = 0
exact = 0
strict = 0
maximum_slack = 0
for first_size, first_edges, first_loss in PACKETS:
    for second_size, second_edges, second_loss in PACKETS:
        shifted_second_edges = tuple(
            (first + first_size, second + first_size)
            for first, second in second_edges
        )
        for interface in cross_matchings(first_size, second_size):
            edges = first_edges + shifted_second_edges + interface
            retained = independence_number(first_size + second_size, edges)
            certified = (
                first_size + second_size
                - first_loss
                - second_loss
                - len(interface)
            )
            assert retained >= certified
            cases += 1
            exact += retained == certified
            strict += retained > certified
            maximum_slack = max(maximum_slack, retained - certified)

assert cases == 76156
assert exact == 3766
assert strict == 72390
assert maximum_slack == 4


def packets_needed(local_retained, interface_loss, target=28):
    assert local_retained > interface_loss
    numerator = target - interface_loss
    denominator = local_retained - interface_loss
    return max(1, (numerator + denominator - 1) // denominator)

assert packets_needed(9, 1) == 4
assert packets_needed(10, 2) == 4
assert packets_needed(12, 2) == 3

print({
    "packet_graphs": len(PACKETS),
    "two_packet_interface_cases": cases,
    "exact_lower_bound_cases": exact,
    "strict_lower_bound_cases": strict,
    "maximum_observed_slack": maximum_slack,
    "concatenation_bound": "sum_j r_j - sum_i c_i",
    "identical_packet_bound": "K*r-(K-1)*c = K*(r-c)+c",
    "packets_needed": "max(1,ceil((28-c)/(r-c))) for r>c",
    "remaining_gap": "a coordinate host must supply packet resource lists, internal degree-two centre graphs, and certified interface matchings",
    "evidence_level": "exact_packet_interface_hall_surplus",
    "status": "passed",
})

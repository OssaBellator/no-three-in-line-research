#!/usr/bin/env python3
"""Finite audit for GC2gt--GC2gx.

The script checks small donor graphs and synthetic least-cause partitions. The
Markdown note contains the arbitrary-size proof.
"""


def maximum_matching(edges, left_size, right_size):
    best = []

    def search(left, used_right, pairs):
        nonlocal best
        if left == left_size:
            if len(pairs) > len(best) or (
                len(pairs) == len(best) and tuple(pairs) < tuple(best)
            ):
                best = pairs.copy()
            return

        search(left + 1, used_right, pairs)
        for right in range(right_size):
            if right not in used_right and (left, right) in edges:
                used_right.add(right)
                pairs.append((left, right))
                search(left + 1, used_right, pairs)
                pairs.pop()
                used_right.remove(right)

    search(0, set(), [])
    return best


def alternating_core(edges, left_size, right_size, matching):
    matched_left = {left: right for left, right in matching}
    matched_right = {right: left for left, right in matching}

    X = {left for left in range(left_size) if left not in matched_left}
    Y = set()
    queue = sorted(X)
    cursor = 0

    while cursor < len(queue):
        left = queue[cursor]
        cursor += 1
        for right in range(right_size):
            if (
                (left, right) in edges
                and matched_left.get(left) != right
                and right not in Y
            ):
                Y.add(right)
                if right in matched_right and matched_right[right] not in X:
                    X.add(matched_right[right])
                    queue.append(matched_right[right])

    return X, Y


def main():
    graphs = cores = global_shortages = rectangle_pairs = weighted_checks = 0

    for left_size in range(1, 5):
        for right_size in range(1, 5):
            all_edges = [
                (left, right)
                for left in range(left_size)
                for right in range(right_size)
            ]

            for mask in range(1 << len(all_edges)):
                edges = {
                    all_edges[index]
                    for index in range(len(all_edges))
                    if (mask >> index) & 1
                }
                matching = maximum_matching(edges, left_size, right_size)
                graphs += 1
                if len(matching) == left_size:
                    continue

                X, Y = alternating_core(
                    edges, left_size, right_size, matching
                )
                neighbourhood = {
                    right
                    for left in X
                    for right in range(right_size)
                    if (left, right) in edges
                }
                assert neighbourhood == Y
                assert len(X) - len(Y) == left_size - len(matching)
                cores += 1

                if len(Y) == right_size:
                    assert len(X) - right_size > 0
                    global_shortages += 1
                    continue

                rectangle = [
                    (left, right)
                    for left in sorted(X)
                    for right in range(right_size)
                    if right not in Y
                ]
                assert rectangle
                assert all(pair not in edges for pair in rectangle)

                cause_count = 1 + ((left_size + right_size + mask) % 5)
                target_weight = {
                    left: 1 + ((3 * left + mask) % 4)
                    for left in X
                }
                weighted_load = [0] * cause_count
                unweighted_load = [0] * cause_count

                for index, (left, right) in enumerate(rectangle):
                    cause = (index + left + 2 * right + mask) % cause_count
                    weighted_load[cause] += target_weight[left]
                    unweighted_load[cause] += 1

                total_weight = (right_size - len(Y)) * sum(target_weight.values())
                assert sum(weighted_load) == total_weight
                assert max(weighted_load) * cause_count >= total_weight

                maximum_cause_load = max(unweighted_load)
                active_causes = sum(load > 0 for load in unweighted_load)
                assert active_causes * maximum_cause_load >= len(rectangle)

                rectangle_pairs += len(rectangle)
                weighted_checks += 1

    print(f"{graphs:,} donor graphs")
    print(f"{cores:,} canonical Hall cores")
    print(f"{global_shortages:,} global donor-count overloads")
    print(f"{rectangle_pairs:,} missing target/donor incidences")
    print(f"{weighted_checks:,} weighted cause partitions")


if __name__ == "__main__":
    main()

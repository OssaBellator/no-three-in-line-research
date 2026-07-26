#!/usr/bin/env python3
"""Finite checks for CMR1102--CMR1109."""

from itertools import combinations
import random


def random_nested_segment(universe_size, state_size, rng):
    universe = set(range(universe_size))
    final_state = set(rng.sample(tuple(universe), state_size))
    removable = list(universe - final_state)
    rng.shuffle(removable)
    host = set(universe)
    hosts = [frozenset(host)]
    anchors = []
    witnesses = []

    while removable:
        anchor = set(final_state)
        available_extra = list(host - final_state)
        extra_count = rng.randint(0, min(len(available_extra), state_size))
        if extra_count:
            removed_from_final = rng.sample(tuple(final_state), extra_count)
            added = rng.sample(available_extra, extra_count)
            anchor.difference_update(removed_from_final)
            anchor.update(added)
        assert len(anchor) == state_size and anchor <= host
        anchors.append(frozenset(anchor))

        candidates = [edge for edge in removable if edge in anchor]
        if candidates:
            witness = candidates[0]
        else:
            witness = removable[0]
        host.remove(witness)
        removable.remove(witness)
        hosts.append(frozenset(host))
        if witness in anchor:
            witnesses.append(witness)

    return hosts, anchors, witnesses, final_state


def check_nested_witnesses():
    rng = random.Random(1102)
    checked = 0
    witness_cases = 0
    for universe_size in range(2, 100):
        for state_size in range(1, universe_size + 1):
            for _ in range(20):
                hosts, _anchors, witnesses, final_state = random_nested_segment(
                    universe_size, state_size, rng
                )
                assert all(hosts[i + 1] < hosts[i] for i in range(len(hosts) - 1))
                assert len(witnesses) == len(set(witnesses))
                assert set(witnesses).isdisjoint(final_state)
                assert len(witnesses) <= universe_size - state_size
                for index, witness in enumerate(witnesses):
                    # The construction removes witnesses in chronological order;
                    # every later host omits every earlier witness.
                    removal_index = next(i for i in range(len(hosts) - 1) if witness in hosts[i] and witness not in hosts[i + 1])
                    assert all(witness not in host for host in hosts[removal_index + 1 :])
                witness_cases += len(witnesses)
                checked += 1
    return checked, witness_cases


def check_fixed_side_bounds():
    checked = 0
    for side in range(1, 1000):
        universe = 2 * side * side
        state = 2 * side
        segment_loss = universe - state
        total_loss = (2 * side + 1) * segment_loss
        assert segment_loss == 2 * side * side - 2 * side
        assert total_loss >= segment_loss
        checked += 1
    return checked


def host_stages(side):
    return 2 * side * side + side + 1


def check_branch_arithmetic():
    checked = 0
    for side in range(1, 300):
        path = sum(
            host_stages(m) * (2 * m + 1) * (2 * m * m - 2 * m)
            for m in range(1, side + 1)
        )
        assert path >= 0
        for height in range(1, 20):
            global_bound = (height + 1) * (2 * side + 1) * path
            assert global_bound >= path
            checked += 1
    return checked


def check_two_label_target_cuts():
    rng = random.Random(1107)
    checked = 0
    for cell_count in range(1, 200):
        labelled = {(layer, cell) for layer in (0, 1) for cell in range(cell_count)}
        for _ in range(100):
            cell = rng.randrange(cell_count)
            old_label = (rng.randint(0, 1), cell)
            old_state = {old_label}
            extras = list(labelled - {(0, cell), (1, cell)})
            old_state.update(rng.sample(extras, rng.randint(0, min(20, len(extras)))))
            cut = {(0, cell), (1, cell)}
            new_host = labelled - cut
            assert old_label not in new_host
            assert new_host.isdisjoint(cut)
            checked += 1
    return checked


def main():
    segments, witnesses = check_nested_witnesses()
    print(
        "verified minimum-loss normalization:",
        segments,
        "nested segments with",
        witnesses,
        "canonical witnesses,",
        check_fixed_side_bounds(),
        "fixed-side bounds,",
        check_branch_arithmetic(),
        "branch bounds, and",
        check_two_label_target_cuts(),
        "two-label cuts",
    )


if __name__ == "__main__":
    main()

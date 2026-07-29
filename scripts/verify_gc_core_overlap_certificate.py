#!/usr/bin/env python3
"""Exhaustive finite audit for GC2ka--GC2ke."""

SYSTEMS = 3200
FOUR_TERMINAL_SYSTEMS = 600
PAIR_CORE_SYSTEMS = 1850
SINGLETON_CORE_SYSTEMS = 320


def maximum_payment(neighborhoods, enabled):
    match = {}
    def augment(terminal, seen):
        for source in neighborhoods[terminal]:
            if source in seen:
                continue
            seen.add(source)
            if source not in match or augment(match[source], seen):
                match[source] = terminal
                return True
        return False
    return sum(augment(terminal, set()) for terminal in enabled)


def main():
    subset_checks = deficient = paid = singleton = nontrivial = 0
    addresses = deficit_units = marginal_checks = partitions = overlap_units = 0
    for system in range(SYSTEMS):
        n = 4 if system < FOUR_TERMINAL_SYSTEMS else 5
        if system < PAIR_CORE_SYSTEMS:
            kind = "pair"
            neighborhoods = [[0], [0]] + [[i] for i in range(1, n - 1)]
        elif system < PAIR_CORE_SYSTEMS + SINGLETON_CORE_SYSTEMS:
            kind = "singleton"
            neighborhoods = [[]] + [[i] for i in range(1, n)]
        else:
            kind = "paid"
            neighborhoods = [[i] for i in range(n)]
        values = {}
        for mask in range(1 << n):
            enabled = [i for i in range(n) if mask & (1 << i)]
            flow = maximum_payment(neighborhoods, enabled)
            values[mask] = (len(enabled), flow, len(enabled) - flow)
            subset_checks += 1
        bad = [mask for mask, value in values.items() if value[2] > 0]
        if not bad:
            assert kind == "paid"
            paid += 1
            continue
        core = min(bad, key=lambda mask: (mask.bit_count(), tuple(i for i in range(n) if mask & (1 << i))))
        demand, flow, delta = values[core]
        deficient += 1
        addresses += core.bit_count()
        deficit_units += delta
        for mask in range(1 << n):
            if mask != core and not (mask & ~core):
                assert values[mask][2] == 0
        for i in range(n):
            if core & (1 << i):
                without = core & ~(1 << i)
                assert 1 - (flow - values[without][1]) == delta
                marginal_checks += 1
        if core.bit_count() == 1:
            singleton += 1
            continue
        nontrivial += 1
        least = core & -core
        for left in range(1 << n):
            if left == 0 or left == core or left & ~core or not left & least:
                continue
            right = core ^ left
            overlap = values[left][1] + values[right][1] - flow
            assert overlap == delta
            partitions += 1
            overlap_units += overlap
    assert subset_checks == 92800
    assert deficient == 2170 and paid == 1030
    assert singleton == 320 and nontrivial == 1850
    assert addresses == marginal_checks == 4020
    assert deficit_units == 2170
    assert partitions == overlap_units == 1850
    print("GC2ka--GC2ke core-overlap audit passed")
    print(f"systems: {SYSTEMS}")
    print(f"terminal-subset checks: {subset_checks}")
    print(f"deficient systems: {deficient}")
    print(f"singleton cores: {singleton}")
    print(f"nontrivial core bipartitions: {partitions}")
    print(f"core addresses: {addresses}")
    print(f"competition-overlap units: {overlap_units}")


if __name__ == "__main__":
    main()

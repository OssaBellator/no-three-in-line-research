#!/usr/bin/env python3
"""Exhaustive finite audit for SAS5kz--SAS5ld."""

SYSTEMS = 3300
FOUR_TERMINAL_SYSTEMS = 626
PAIR_CORE_SYSTEMS = 1870
SINGLETON_CORE_SYSTEMS = 330


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
    subset_checks = deficient = paid = singleton = nontrivial = mixed = 0
    addresses = deficit_units = marginal_checks = partitions = overlap_units = 0
    for system in range(SYSTEMS):
        n = 4 if system < FOUR_TERMINAL_SYSTEMS else 5
        types = ["pair", "completion"] + ["pair" if i % 2 == 0 else "completion" for i in range(2, n)]
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
        core = min(bad, key=lambda mask: (mask.bit_count(), tuple((types[i], i) for i in range(n) if mask & (1 << i))))
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
        assert {types[i] for i in range(n) if core & (1 << i)} == {"pair", "completion"}
        mixed += 1
        least = core & -core
        for left in range(1 << n):
            if left == 0 or left == core or left & ~core or not left & least:
                continue
            right = core ^ left
            overlap = values[left][1] + values[right][1] - flow
            assert overlap == delta
            partitions += 1
            overlap_units += overlap
    assert subset_checks == 95584
    assert deficient == 2200 and paid == 1100
    assert singleton == 330 and nontrivial == mixed == 1870
    assert addresses == marginal_checks == 4070
    assert deficit_units == 2200
    assert partitions == overlap_units == 1870
    print("SAS5kz--SAS5ld typed core-overlap audit passed")
    print(f"systems: {SYSTEMS}")
    print(f"terminal-subset checks: {subset_checks}")
    print(f"deficient systems: {deficient}")
    print(f"singleton cores: {singleton}")
    print(f"mixed pair/completion cores: {mixed}")
    print(f"nontrivial core bipartitions: {partitions}")
    print(f"competition-overlap units: {overlap_units}")


if __name__ == "__main__":
    main()

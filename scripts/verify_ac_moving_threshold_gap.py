#!/usr/bin/env python3
"""Finite audit for AC3wk--AC3wo: co-moving threshold phase cycles."""

from math import floor

systems = phase_cycles = positive = negative = zero = budget_checks = 0

for qn in range(1, 4):
    for mod in range(2, 6):
        phases = [(q, r) for q in range(qn) for r in range(mod)]
        for seed in range(60):
            systems += 1
            nxt = {}
            inc = {}
            for q, r in phases:
                g = ((seed + 3 * q + 5 * r) % 7) - 3
                q2 = (q + 1 + ((seed + q * r) % qn)) % qn
                r2 = (r + g) % mod
                nxt[(q, r)] = (q2, r2)
                inc[(q, r)] = g

            seen_global = set()
            for start in phases:
                if start in seen_global:
                    continue
                order = []
                pos = {}
                cur = start
                while cur not in pos:
                    pos[cur] = len(order)
                    order.append(cur)
                    seen_global.add(cur)
                    cur = nxt[cur]
                cyc = order[pos[cur] :]
                if not cyc:
                    continue
                phase_cycles += 1
                drift = sum(inc[z] for z in cyc)
                assert drift % mod == 0

                pref = [0]
                for z in cyc:
                    pref.append(pref[-1] + inc[z])
                min_pref = min(pref)

                if drift > 0:
                    positive += 1
                    y = max(0, -min_pref) + mod
                    assert y + min_pref >= 0
                    assert y + drift > y
                elif drift < 0:
                    negative += 1
                    y = max(0, -min_pref) + 3 * (-drift) + mod
                    exact = floor((y + min_pref) / (-drift)) + 1
                    count = 0
                    gap = y
                    while gap + min_pref >= 0:
                        count += 1
                        gap += drift
                    assert count == exact
                    budget_checks += 1
                else:
                    zero += 1
                    y = max(0, -min_pref) + mod
                    gap = y
                    for z in cyc:
                        gap += inc[z]
                    assert gap == y

print(f"{systems=}")
print(f"{phase_cycles=}")
print(f"{positive=}")
print(f"{negative=}")
print(f"{zero=}")
print(f"{budget_checks=}")

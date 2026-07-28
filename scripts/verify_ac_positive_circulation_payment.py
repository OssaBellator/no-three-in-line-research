#!/usr/bin/env python3
"""Finite audit for AC3ur--AC3uv."""

from collections import defaultdict
import random

SEED = 20260728


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(40000):
        q = rng.randint(1, 6)
        m = [rng.randint(0, 20) for _ in range(q)]

        pcount = rng.randint(1, 8)
        h0 = [rng.randint(0, 20) for _ in range(pcount)]
        h = h0[:]

        r = rng.randint(1, 6)
        rho = [rng.randint(1, 5) for _ in range(r)]
        s0 = [rng.randint(0, 12) for _ in range(r)]
        s = s0[:]

        qdim = rng.randint(1, 5)
        D_q = rng.randint(1, 12)
        L_macro = rng.randint(1, 10)
        L_gate = rng.randint(1, 8)
        L_circ = (qdim + 1) * D_q * L_macro

        cap_words = 0
        cap_output = 0
        source_words = 0
        gross_created = 0
        gates = 0
        edges = 0

        for _step in range(200):
            can_cap = any(x > 0 for x in h)
            can_source = any(x > 0 for x in s)
            if not can_cap and not can_source:
                break

            use_cap = can_cap and (not can_source or rng.random() < 0.5)
            if use_cap:
                available = [p for p, value in enumerate(h) if value > 0]
                p = rng.choice(available)
                net = rng.randint(1, h[p])
                h[p] -= net
                cap_output += net
                cap_words += 1
            else:
                available = [u for u, value in enumerate(s) if value > 0]
                u = rng.choice(available)
                debit = rng.randint(1, s[u])
                source_credit = rho[u] * debit
                R = rng.randint(1, source_credit)
                C = rng.randint(0, R - 1)
                net = R - C
                s[u] -= debit
                gross_created += R
                source_words += 1

            z = [0] * q
            for _unit in range(net):
                z[rng.randrange(q)] += 1
            old_total = sum(m)
            m = [m[j] + z[j] for j in range(q)]
            assert sum(m) - old_total == sum(z) == net >= 1

            word_gates = rng.randint(1, L_circ)
            word_edges = word_gates * rng.randint(1, L_gate)
            gates += word_gates
            edges += word_edges
            counts["positive_words"] += 1

        H_cap = sum(h0)
        S_src = sum(s0)
        assert cap_words <= H_cap
        assert cap_output <= H_cap
        assert source_words <= S_src
        assert gross_created <= sum(rho[i] * s0[i] for i in range(r))
        assert cap_words + source_words <= H_cap + S_src
        assert gates <= (cap_words + source_words) * L_circ
        assert edges <= (cap_words + source_words) * L_circ * L_gate

        counts["systems"] += 1
        counts["cap_words"] += cap_words
        counts["cap_output_units"] += cap_output
        counts["source_words"] += source_words
        counts["gross_created_units"] += gross_created
        counts["completed_gates"] += gates
        counts["control_edges"] += edges

    print("AC positive-circulation payment audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()

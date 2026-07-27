#!/usr/bin/env python3
"""Finite audit for AC3tx--AC3ub."""

from collections import defaultdict
import random

SEED = 20260727


def distribute(total, size, rng):
    out = [0] * size
    for _ in range(total):
        out[rng.randrange(size)] += 1
    return out


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(30000):
        q = rng.randint(1, 6)
        r = rng.randint(1, 5)
        rho = [rng.randint(1, 5) for _ in range(r)]
        m0 = [rng.randint(0, 8) for _ in range(q)]
        s0 = [rng.randint(0, 6) for _ in range(r)]
        m = m0[:]
        s = s0[:]

        a = rng.randint(1, 9)
        l_cyc = rng.randint(1, a)
        l_gate = rng.randint(1, 20)

        creation_cap = sum(x * y for x, y in zip(rho, s0))
        cycle_cap = sum(m0) + sum((x + 1) * y for x, y in zip(rho, s0))

        total_r = 0
        total_c = 0
        total_d = [0] * r
        positive_creation_steps = 0
        cycles = 0
        used_gates = 0
        used_edges = 0

        while sum(m) + sum(s) > 0 and rng.random() < 0.92:
            # Choose a nonstuttering accepted macro: consume a resource unit,
            # debit a source, or both.
            c_vec = [0] * q
            d_vec = [0] * r

            can_consume = sum(m) > 0
            can_debit = sum(s) > 0
            choose_consume = can_consume and (not can_debit or rng.random() < 0.7)
            choose_debit = can_debit and (not choose_consume or rng.random() < 0.65)

            if choose_consume:
                available = [i for i, value in enumerate(m) if value > 0]
                for _ in range(rng.randint(1, min(3, sum(m)))):
                    available = [i for i, value in enumerate(m) if value - c_vec[i] > 0]
                    if not available:
                        break
                    i = rng.choice(available)
                    c_vec[i] += 1

            if choose_debit:
                available = [u for u, value in enumerate(s) if value > 0]
                for _ in range(rng.randint(1, min(2, sum(s)))):
                    available = [u for u, value in enumerate(s) if value - d_vec[u] > 0]
                    if not available:
                        break
                    u = rng.choice(available)
                    d_vec[u] += 1

            if sum(c_vec) == 0 and sum(d_vec) == 0:
                break

            source_credit = sum(rho[u] * d_vec[u] for u in range(r))
            r_total = rng.randint(0, source_credit)
            r_vec = distribute(r_total, q, rng)

            old_m = m[:]
            old_s = s[:]
            phi_old = sum(old_m) + sum(rho[u] * old_s[u] for u in range(r))
            stock_old = sum(old_s)

            m = [old_m[i] - c_vec[i] + r_vec[i] for i in range(q)]
            s = [old_s[u] - d_vec[u] for u in range(r)]
            assert all(value >= 0 for value in m)
            assert all(value >= 0 for value in s)

            gross_created = sum(r_vec)
            gross_consumed = sum(c_vec)
            assert sum(m) - sum(old_m) == gross_created - gross_consumed
            assert gross_created <= source_credit

            phi_new = sum(m) + sum(rho[u] * s[u] for u in range(r))
            stock_new = sum(s)
            assert phi_new - phi_old <= -gross_consumed
            if gross_consumed >= 1:
                assert phi_new < phi_old
            else:
                assert stock_new < stock_old

            total_r += gross_created
            total_c += gross_consumed
            for u in range(r):
                total_d[u] += d_vec[u]
            if gross_created > 0:
                positive_creation_steps += 1

            gate_len = rng.randint(1, l_cyc)
            edge_len = sum(rng.randint(1, l_gate) for _ in range(gate_len))
            used_gates += gate_len
            used_edges += edge_len
            cycles += 1

            assert cycles <= cycle_cap
            counts["accepted_cycles"] += 1
            counts["created_units"] += gross_created
            counts["consumed_units"] += gross_consumed
            counts["completed_gates"] += gate_len
            counts["control_edges"] += edge_len

        assert total_r <= creation_cap
        assert positive_creation_steps <= sum(s0)
        assert cycles <= cycle_cap
        assert all(total_d[u] <= s0[u] for u in range(r))
        assert total_c <= sum(m0) + total_r

        # Add one final cycle-free auxiliary tail.
        tail = rng.randint(0, a - 1)
        tail_edges = sum(rng.randint(1, l_gate) for _ in range(tail))
        assert used_gates + tail <= cycle_cap * l_cyc + (a - 1)
        assert used_edges + tail_edges <= (cycle_cap * l_cyc + (a - 1)) * l_gate

        counts["systems"] += 1
        counts["positive_creation_steps"] += positive_creation_steps
        counts["final_tail_gates"] += tail

    print("AC macro resource-payment audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()

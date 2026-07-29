#!/usr/bin/env python3
"""Verify exact structural legality for two swaps sharing one row."""

from itertools import permutations, combinations


def swap(p, i, j):
    q = list(p)
    q[i], q[j] = q[j], q[i]
    return tuple(q)


def host_valid(p, host):
    return all((r, p[r]) in host for r in range(len(p)))


def disjoint(p, q):
    return all(p[r] != q[r] for r in range(len(p)))


def main():
    checked_identity = 0
    checked_hosts = 0
    checked_layers = 0
    for n in range(3, 7):
        rows = range(n)
        for pi in permutations(rows):
            for i, j, k in permutations(rows, 3):
                final = swap(swap(pi, i, j), j, k)
                assert final[i] == pi[j]
                assert final[j] == pi[k]
                assert final[k] == pi[i]
                checked_identity += 1

                relevant = [(i, pi[j]), (j, pi[k]), (k, pi[i])]
                original = {(r, pi[r]) for r in rows}
                for mask in range(1 << 3):
                    host = set(original)
                    for bit, edge in enumerate(relevant):
                        if mask & (1 << bit):
                            host.add(edge)
                    criterion = all(edge in host for edge in relevant)
                    assert host_valid(final, host) == criterion
                    checked_hosts += 1

            if n <= 5:
                for rho in permutations(rows):
                    if not disjoint(pi, rho):
                        continue
                    for i, j, k in permutations(rows, 3):
                        final = swap(swap(pi, i, j), j, k)
                        host = {(r, pi[r]) for r in rows} | {
                            (i, pi[j]), (j, pi[k]), (k, pi[i])
                        }
                        criterion = (
                            pi[j] != rho[i]
                            and pi[k] != rho[j]
                            and pi[i] != rho[k]
                        )
                        assert (host_valid(final, host) and disjoint(final, rho)) == criterion
                        checked_layers += 1

    print(
        f"verified {checked_identity} compositions, "
        f"{checked_hosts} host tests, and {checked_layers} two-layer tests"
    )


if __name__ == "__main__":
    main()

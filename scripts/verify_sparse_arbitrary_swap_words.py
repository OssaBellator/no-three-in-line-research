#!/usr/bin/env python3
"""Finite checks for SAS5hq--SAS5ht."""

from itertools import permutations, combinations


def compose_transposition(alpha, i, j):
    alpha = list(alpha)
    alpha[i], alpha[j] = alpha[j], alpha[i]
    return tuple(alpha)


def final_images(pi, alpha):
    return tuple(pi[alpha[i]] for i in range(len(pi)))


def pi_samples(rows):
    n = len(rows)
    if n <= 5:
        return list(permutations(rows))
    return [
        tuple(rows),
        tuple(reversed(rows)),
        tuple((i + 1) % n for i in rows),
        tuple((2 * i) % n for i in rows) if n % 2 else tuple((3 * i) % n for i in rows),
    ]


def main():
    checks = 0
    for n in range(2, 8):
        rows = tuple(range(n))
        for pi in pi_samples(rows):
            # Rotate the current image list to obtain a rowwise-disjoint second layer.
            rho = tuple(pi[(i + 1) % n] for i in rows)
            assert all(rho[i] != pi[i] for i in rows)

            for alpha in permutations(rows):
                moved = [i for i in rows if alpha[i] != i]
                p2 = final_images(pi, alpha)
                assert sorted(p2) == sorted(pi)

                final_edges = {(i, p2[i]) for i in rows}
                original_edges = {(i, pi[i]) for i in rows}
                hosts = [original_edges | final_edges]
                if moved:
                    hosts.append((original_edges | final_edges) - {(moved[0], p2[moved[0]])})
                for host in hosts:
                    criterion = all((i, p2[i]) in host for i in moved)
                    actual = all((i, p2[i]) in host for i in rows)
                    assert criterion == actual

                    criterion2 = criterion and all(p2[i] != rho[i] for i in moved)
                    actual2 = actual and all(p2[i] != rho[i] for i in rows)
                    assert criterion2 == actual2
                    failed = sum((i, p2[i]) not in host for i in moved) + sum(p2[i] == rho[i] for i in moved)
                    assert failed <= 2 * len(moved)
                checks += 1

            alpha = tuple(rows)
            for i, j in combinations(rows, 2):
                alpha = compose_transposition(alpha, i, j)
                assert sorted(alpha) == list(rows)

    print(f"verified {checks} arbitrary image permutations")


if __name__ == "__main__":
    main()

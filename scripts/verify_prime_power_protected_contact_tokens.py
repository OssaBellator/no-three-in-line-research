#!/usr/bin/env python3
"""Verify CMR582--CMR586 protected-contact stock and token arithmetic."""

from math import ceil, sqrt


Edge = tuple[int, int]


def blocked_edges(n: int, k: int) -> set[Edge]:
    """Use the identity matching with its first k edges protected."""
    forbidden = {(i, i) for i in range(n)}
    return {
        (u, v)
        for u in range(n)
        for v in range(n)
        if (u, v) not in forbidden and (u < k or v < k)
    }


def check_contact_universe_and_wall() -> None:
    for n in range(2, 40):
        for k in range(1, n + 1):
            contacts = blocked_edges(n, k)
            assert len(contacts) <= 2 * k * (n - 1)
            if not contacts:
                continue

            degrees = [
                sum(u == vertex for u, _ in contacts)
                for vertex in range(k)
            ] + [
                sum(v == vertex for _, v in contacts)
                for vertex in range(k)
            ]
            assert max(degrees) >= ceil(len(contacts) / (2 * k))


def check_multiplicity_bounds() -> None:
    for n in range(2, 30):
        for k in range(1, n + 1):
            stock = 2 * k * (n - 1)
            for lam in range(2, 12):
                maximum_without_recurrence = (lam - 1) * stock
                assert maximum_without_recurrence == 2 * (lam - 1) * k * (n - 1)
                for episodes in range(maximum_without_recurrence + 1):
                    support_lower = ceil(episodes / (lam - 1)) if episodes else 0
                    assert support_lower <= stock


def check_token_partition() -> None:
    for d in range(1, 1000):
        root = ceil(sqrt(d))
        if root >= 2:
            assert ceil(d / (root - 1)) >= root
        for threshold in range(2, min(d + 2, 50)):
            # If every occupied class has size at most threshold-1, this many
            # classes are necessary.
            classes = ceil(d / (threshold - 1))
            assert classes * (threshold - 1) >= d


def check_absence_run_bound() -> None:
    for occurrences in range(1, 100):
        for sigma in range(2, 20):
            required_returns = ceil(occurrences / (sigma - 1)) - 1
            if required_returns < 0:
                required_returns = 0
            runs = required_returns + 1
            assert runs * (sigma - 1) >= occurrences


def main() -> None:
    check_contact_universe_and_wall()
    check_multiplicity_bounds()
    check_token_partition()
    check_absence_run_bound()
    print("verified protected contact token ledger through configured ranges")


if __name__ == "__main__":
    main()

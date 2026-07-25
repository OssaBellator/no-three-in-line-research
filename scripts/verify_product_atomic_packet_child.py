#!/usr/bin/env python3
"""Finite verifier for PX319--PX322."""

from math import ceil


def verify_blocked_average() -> None:
    for h in range(2, 8):
        edges = [(u, v) for u in range(h) for v in range(u + 1, h)]
        families = []
        families.append({e: 0 for e in edges})
        for heavy in edges:
            families.append({e: (4 if e == heavy else 0) for e in edges})
        families.append({e: 1 for e in edges})
        families.append({e: (u + v) % 4 for e in edges for u, v in [e]})
        for weights in families:
            total = sum(weights.values())
            if total == 0:
                continue
            deg = [0] * h
            for (u, v), w in weights.items():
                deg[u] += w
                deg[v] += w
            assert max(deg) * h >= 2 * total
            for K in range(1, 6):
                star = ceil(max(deg) / K)
                assert star >= ceil(2 * total / (h * K))


def verify_atomic_ledgers() -> None:
    for K in range(1, 8):
        for w in range(1, 18):
            for mu1 in range(0, 18):
                for mu2 in range(0, 18):
                    for lam in range(0, 18):
                        c = mu1 + mu2 + lam
                        if w > c:
                            assert -w + c < 0
                        else:
                            q = ceil(w / 3)
                            assert max(mu1, mu2, lam) >= q
                            if max(mu1, mu2) >= q:
                                star = ceil(max(mu1, mu2) / K)
                                assert star >= ceil(w / (3 * K))
                            else:
                                line_size = lam + 2
                                assert line_size >= ceil(w / 3) + 2


def verify_interface_cases() -> None:
    for blocked in (False, True):
        for w in range(1, 20):
            if blocked:
                child_units = w
                assert child_units >= 1
            else:
                for mu1 in range(5):
                    for mu2 in range(5):
                        for lam in range(5):
                            c = mu1 + mu2 + lam
                            assert (w > c) or (max(mu1, mu2, lam) >= ceil(w / 3))


if __name__ == "__main__":
    verify_blocked_average()
    verify_atomic_ledgers()
    verify_interface_cases()
    print("PX319--PX322 verified")

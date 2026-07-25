#!/usr/bin/env python3
"""Arithmetic checks for PX319--PX323."""


def main() -> None:
    for mu1 in range(21):
        for mu2 in range(21):
            for lam in range(21):
                c = mu1 + mu2 + lam
                for w in range(1, 31):
                    if w <= c:
                        assert 3 * max(mu1, mu2, lam) >= w
                        blockers = c - w + 1
                        assert 1 <= blockers <= c
                        assert c - blockers < w
                    else:
                        assert -w + c < 0

    for k in range(1, 8):
        for t in range(1, 8):
            for ell in range(1, 8):
                for mu1 in range(k * t):
                    for mu2 in range(k * t):
                        for lam in range(ell):
                            c = mu1 + mu2 + lam
                            for w in range(1, 2 * k * t + ell + 3):
                                if w <= c:
                                    assert w < 2 * k * t + ell
    print("PX319--PX323 packet blocker-budget verifier: PASS")


if __name__ == "__main__":
    main()

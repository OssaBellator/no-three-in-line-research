#!/usr/bin/env python3
"""Finite audit for SAS5hd--SAS5hh."""


def toggle(x, bit):
    return x ^ (1 << bit)


def eval_table(table, x):
    # Invariant legality predicates depend only on the two untouched bits.
    key = (x >> 2) & 0b11
    return bool(table >> key & 1)


def main():
    checked = 0
    legal_squares = 0
    for sigma_table in range(16):
        for tau_table in range(16):
            for x in range(16):
                sx = toggle(x, 0)
                tx = toggle(x, 1)
                stx = toggle(sx, 1)
                # Commutation.
                assert stx == toggle(tx, 0)
                Ls = lambda y: eval_table(sigma_table, y)
                Lt = lambda y: eval_table(tau_table, y)
                # Transport and reversal invariance.
                assert Ls(x) == Ls(tx)
                assert Ls(x) == Ls(sx)
                assert Lt(x) == Lt(sx)
                assert Lt(x) == Lt(tx)
                if Ls(x) and Lt(x):
                    assert Ls(tx) and Ls(stx)
                    assert Lt(sx) and Lt(stx)
                    legal_squares += 1
                checked += 1
    print("SAS mixed-orientation legality audit passed")
    print(f"  base predicate states checked: {checked}")
    print(f"  fully legal operation squares: {legal_squares}")


if __name__ == "__main__":
    main()

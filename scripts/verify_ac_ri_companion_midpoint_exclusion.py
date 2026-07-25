#!/usr/bin/env python3
"""Finite checks for AC3ez."""

PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)


def main():
    fibres = physical_midpoint_checks = 0

    for p in PRIMES:
        for r in range(1, p):
            for g in range(1, p):
                if g == 1:
                    continue

                roots = [
                    c
                    for c in range(1, p)
                    if c * (1 + g - c) % p == r * g % p
                ]
                if len(roots) != 2 or roots[0] == roots[1]:
                    continue

                c, companion = roots
                assert (c + companion) % p == (1 + g) % p
                assert c * companion % p == r * g % p
                assert (c + companion) % p != 2 % p
                assert (c + companion) % p != 2 * g % p
                fibres += 1

                for x in range(1, p):
                    first_anchor_col = c * x % p
                    second_anchor_col = companion * x % p
                    partner_col = g * x % p
                    assert first_anchor_col and second_anchor_col and partner_col

                    # Exact physical midpoint equality implies the corresponding
                    # modular equality, so neither integer equality can occur.
                    assert 2 * x != first_anchor_col + second_anchor_col
                    assert 2 * partner_col != first_anchor_col + second_anchor_col
                    physical_midpoint_checks += 2

    print(
        "AC RI companion midpoint exclusion: verified "
        f"{fibres} nonfixed fibres and "
        f"{physical_midpoint_checks} physical midpoint checks"
    )


if __name__ == "__main__":
    main()

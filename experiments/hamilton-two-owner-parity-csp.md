# Two-owner Hamilton flaws as a parity CSP

Run:

```bash
python scripts/check_hamilton_two_owner_parity_csp.py \
  experiments/hamilton-two-owner-parity-csp-audit.json
```

For a fixed Hamilton pair cycle, each owner pair is tested under all four
orientation assignments. Horizontal board reflection complements both
orientations simultaneously, so the two-owner flaw predicate depends only on
the XOR of the two sign bits.

Thus every constrained owner pair either:

```text
requires e_i xor e_j = 0,
requires e_i xor e_j = 1,
forbids both values, or
imposes no constraint.
```

The resulting signed graph is solved by parity propagation. The complete finite
census is:

| `m` | Hamilton cycles | parity edges | satisfiable cycles | unsatisfiable cycles | clean sign vectors |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 2 | 6 | 0 | 80 |
| 5 | 24 | 32 | 22 | 2 | 376 |
| 6 | 120 | 180 | 112 | 8 | 3,576 |
| 7 | 720 | 1,296 | 664 | 56 | 36,736 |

No owner pair forbids both XOR values through `m=7`. The parity-edge splits are:

| `m` | require XOR 0 | require XOR 1 |
|---:|---:|---:|
| 4 | 0 | 2 |
| 5 | 12 | 20 |
| 6 | 84 | 96 |
| 7 | 624 | 672 |

For every satisfiable cycle, the number of two-owner-clean orientation vectors
is a power of two, exactly `2^c`, where `c` is the number of connected components
of the signed constraint graph.

This eliminates all two-owner flaws for most finite Hamilton cycles before any
successor rotation is used. It does not control the remaining three-owner flaws
or prove asymptotic existence.

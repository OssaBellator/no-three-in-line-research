# Swapped edge-disjoint first-moment diagnostic

Run:

```bash
python scripts/check_swapped_edge_disjoint_first_moment.py \
  experiments/swapped-edge-disjoint-first-moment-example.json
```

The checker exhausts every ordered edge-disjoint signed permutation through six
pair vertices.  It constructs the first permutation graph and tests every
selected triple by an exact integer determinant.

The exact output totals are:

```text
states tested:       39,222
determinant checks: 8,271,144
```

The mean numbers of first-layer collinear triples are:

```text
 m   n   edge-disjoint states   exact mean       decimal
 2   4                      6   4/3              1.333333
 3   6                     36   20/9             2.222222
 4   8                    300   74/25            2.960000
 5  10                  3,000   1354/375         3.610667
 6  12                 35,880   21131/4485       4.711483
```

For each `m`, the enumerated state count is also checked against the exact
coefficient of

```text
exp(-z^2)/(1-2z).
```

The finite means are a diagnostic only.  The asymptotic theorem in `docs/291`
uses generic triple cylinders to prove an `Omega(n log n)` first-layer defect
under the uniform edge-disjoint swapped measure.

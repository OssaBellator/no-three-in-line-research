# Exact p=37 support-thirteen swapped-orbit certificate

Run:

```bash
python scripts/check_p37_swapped_orbit_support13_certificate.py \
  experiments/p37-swapped-orbit-support13-certificate.json \
  experiments/p37-swapped-quarter-turn-near-example.json
```

The checker verifies three equivalent representations of the same configuration:

1. a signed pair cycle cover on eighteen reversal-pair vertices;
2. two edge-disjoint permutation layers on `[36]^2`; and
3. a compact standard row-pair code.

It also compares the signed pair cover with the audited four-line near-state and
checks that the canonical changed-source support is exactly

```text
{1,2,3,4,6,7,10,12,13,15,16,17,18},
```

of size thirteen.

The resulting pair-cycle data are

```text
cycle lengths:        [14,3,1]
orientation parities: [0,1,1]
relative cycles:      [14,14,6,2].
```

The selected set has `72` points, exactly two in every row and column.  The
checker performs all

```text
binom(72,3)=59640
```

integer determinant tests, finds no zero determinant, and finds minimum
nonzero absolute determinant one.

The standard code is

```text
oEMEFRU6MBR27CWNU24GHAPKV7T03YZBYIQGQ9J9H1O01WZ6S4FAPIJVX5C3NSX8ODT58KLDL
```

The Hall-propagated branch-and-bound in `docs/290` already excludes supports one
through twelve.  Therefore this positive support-thirteen certificate proves
that the audited near-state has exact canonical signed-orbit repair radius
thirteen.

This is a finite `p=37` seed certificate.  It does not prove the asymptotic
prime-minus-one seed theorem.
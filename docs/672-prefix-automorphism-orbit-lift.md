# Prefix automorphism orbit lift

The canonical thirteen-pair source has 104 minimum-crossing anchor matchings.
`docs/666` lifts every optimal rerouting for one matching. This chapter classifies
all 104 matchings under source automorphisms and gives a bounded coordinate lift
for every orbit representative.

## PP3dca — Exact automorphism orbit decomposition

The source incidence permutation has cycle type

```text
2,2,4,5.
```

Its colour-preserving automorphism group consists of independent cycle rotations,
together with interchange of the two two-cycles. The group has order

```text
2^2 * 2! * 4 * 5 = 160.
```

It acts on anchor matchings by conjugation. The 104 minimum-crossing matchings
split into exactly twenty orbits, with size distribution

```text
2:12, 10:8.
```

Thus twenty representatives suffice for every purely combinatorial statement
invariant under source relabelling.

## PP3dcb — Radius four for every representative and deletion

For each of the twenty lexicographically least orbit representatives, delete each
of the two two-pair components in turn. In all forty representative/deletion cases,
the exact minimum rerouting distance is four.

Select the lexicographically first optimal route in each case. This produces forty
canonical radius-four routes spanning every matching orbit and both deletion types.

## PP3dcc — All-unit coordinate lift for all forty routes

Apply the established greedy primitive-direction insertion rule with one inserted
point on each of the eleven surviving anchors. Every one of the forty canonical
routes embeds without a mixed-run collinear triple.

The maximum-coordinate distributions are

```text
deletion {0,2}: 50:4, 52:4, 66:2, 84:10,
deletion {3,5}: 44:10, 48:10.
```

This proves an orbit-wide coordinate lift for the all-unit composition. It does not
extend the full 1,024-composition audit from the canonical matching to every orbit.

## Verification

`scripts/check_prefix_automorphism_orbit_unit_lifts.py` reconstructs all 104
minimum-crossing matchings, generates the full 160-element source automorphism
group, verifies the twenty orbits, computes all forty first optimal routes, and
checks the all-unit coordinate embedding in every case.

## Evidence boundary

The automorphism reduction is combinatorially complete, but the greedy coordinate
rule is not equivariant under arbitrary row and column relabelling. Arbitrary
compositions for the nineteen new representatives, all 104 physical labelings,
and an all-size recurrence remain open.

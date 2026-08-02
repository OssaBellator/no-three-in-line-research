# Prefix matching orbit reduction

`docs/666` gives a complete coordinate audit for all 288 optimal reroutings of one
minimum-crossing matching. This chapter classifies all 104 minimum-crossing
matchings at the incidence level and determines whether that classification alone
reduces the remaining coordinate work.

## PP3dca — Exact forbidden-incidence automorphism group

The forbidden `P`-to-`Q` incidence graph has component pair-sizes

```text
2,2,4,5.
```

Its full bipartition-preserving automorphism group has order

```text
2,560.
```

The factor includes independent cycle automorphisms and the exchange of the two
equal two-pair components.

## PP3dcb — Four matching and deletion-case orbits

The 104 minimum-four-cross-component anchor matchings split into exactly four
orbits under this group, with sizes

```text
8,16,40,40.
```

The 208 pairs consisting of a minimum-crossing matching and one of the two
two-pair component deletions also split into exactly four orbits, with sizes

```text
16,32,80,80.
```

Thus the combinatorial anchor-permutation layer has only four essential case
types.

## PP3dcc — No coordinate symmetry transfer

The actual twenty-six-cell source is preserved by only the identity among the
eight dihedral symmetries of the `13 x 13` grid.

Consequently the 2,560 incidence automorphisms do not automatically transport a
greedy integer-insertion certificate from one orbit member to another. The orbit
reduction is exact for matching and rerouting combinatorics, but not for coordinate
legality or coordinate bounds.

A future exhaustive coordinate audit may use the four orbit representatives as a
classification guide, but geometric success must still be checked separately
unless a larger coordinate automorphism group or equivariant insertion theorem is
proved.

## Supplemental diagonal-subgroup unit lifts

A separate finite audit uses the 160-element subgroup that applies the same
component rotation or exchange to `P` and `Q` row labels. Under that subgroup the
104 matchings split into twenty orbits: twelve of size two and eight of size ten.

For each of the twenty representatives and each two-pair deletion, the audit
chooses the lexicographically first optimal distance-four rerouting and tests the
all-unit composition. All forty coordinate lifts pass. Their maximum-coordinate
histograms are

```text
first deletion:  50:4, 52:4, 66:2, 84:10
second deletion: 44:10, 48:10.
```

This is useful finite evidence across more matching types, but it checks only one
composition and one optimal rerouting per representative. It does not imply the
same result for every physical labeling in an orbit.

## Verification

- `scripts/check_prefix_matching_orbits.py` constructs the forbidden graph,
  enumerates its complete bipartition-preserving automorphism group, regenerates
  all 104 minimum-crossing matchings, computes both full orbit decompositions, and
  checks all eight grid-dihedral transformations of the source.
- `scripts/check_prefix_automorphism_orbit_unit_lifts.py` performs the supplemental
  160-subgroup classification and forty all-unit coordinate audits.

## Evidence boundary

The result reduces the abstract combinatorial classification from 104 matchings to
four full-incidence types and supplies forty supplemental unit-composition lifts.
It does not reduce the full coordinate audit to four cases and does not supply an
all-size recurrence.

# Orbit-representative composition lifts

`docs/672` proves that incidence automorphisms do not transfer physical coordinate
certificates. Its supplemental diagonal-subgroup audit nevertheless supplies twenty
selected matching representatives and one canonical radius-four route for each of
the two two-pair deletions. This chapter exhausts every ordered composition for
those forty fixed routes.

## PP3dcs — All compositions pass for forty selected routes

For each of the twenty selected representatives and each two-pair deletion, choose
the lexicographically first optimal radius-four rerouting. Apply the established
greedy primitive-direction insertion rule to every ordered composition of eleven.

There are `2^10=1,024` compositions per route, so the audit contains

```text
20 * 2 * 1,024 = 40,960
```

route/composition pairs. Every pair embeds successfully, and every collinear triple
lies entirely inside one labelled run.

## PP3dct — Exact coordinate-bound collapse

For deletion `{0,2}`, the maximum coordinate over all 1,024 compositions has
representative distribution

```text
120:10, 132:10.
```

For deletion `{3,5}`, the distribution is

```text
84:10, 132:10.
```

Thus every selected representative has a uniform all-composition coordinate bound
at most 132, substantially sharper than treating each composition independently.

## PP3dcu — A deterministic finite route selector

On this twenty-representative family, the rule

```text
choose the lexicographically first optimal radius-four rerouting
```

is coordinate-safe for both deletions and every ordered composition of eleven.
This is the first deterministic selector verified beyond a single canonical
matching.

The selector is finite rather than equivariant: the twenty representatives come
from the supplemental 160-element diagonal subgroup, not the full 2,560-element
incidence automorphism group, and coordinate safety is checked directly rather
than transported by symmetry.

## Verification

- `scripts/check_prefix_automorphism_orbit_unit_lifts.py` reconstructs the twenty
  selected representatives and their forty first optimal routes.
- `scripts/check_prefix_orbit_representative_compositions.cpp` checks all 40,960
  route/composition pairs and the exact maximum-coordinate distributions.

## Evidence boundary

The result does not cover every physical one of the 104 minimum-crossing matchings,
all optimal routes, a coordinate-equivariant automorphism action, or an all-size
reservoir recurrence. It is a substantial finite selector audit, not a uniform
prefix theorem.

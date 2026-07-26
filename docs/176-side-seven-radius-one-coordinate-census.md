# Exact coordinate census for the full radius-one selector layer

PX512--PX514 turn simple alternating-cycle flips into a complete local move
language and show that the four certified centre selectors have exactly

\[
1092,\quad364,\quad180,\quad112
\]

radius-one neighbours.  This chapter applies the exact 21-variable coordinate
CSP from PX504--PX507 to every one of those neighbours.

## 1. Monotone dangerous-line certificate

For a fixed abstract selector and radix orientation, the scalar embedding is
controlled by three permutations of `[7]`:

\[
A_0,\qquad A_1,\qquad R.
\]

The first fourteen CSP variables assign `A_0,A_1`; the final seven assign the
bottom-row ordering `R`.  At a partial assignment, keep the set of completed
selected scalar points and the grid mask

\[
\mathcal D
=
\bigcup_{x\ne y\text{ completed}}
\bigl(\overline{xy}\cap[14]^2\bigr).
\]

### Theorem PX515 -- PROVED

A trial coordinate value is extendible exactly when every newly completed point
lies outside `D`, and, when two points complete simultaneously, their joining
line contains no previously completed point.

Consequently the dangerous-line backtracking algorithm rejects a branch if and
only if the current partial embedding already contains a collinear triple.

### Proof

Any new bad triple first appears when its last unresolved coordinate variable is
assigned.  If exactly one point of the triple completes at that step, it lies on
a line through two old completed points and hence in `D`.  If two points complete
at once, either one lies in `D`, or their joining line contains the third old
point.  These are precisely the two rejection tests.  Conversely each rejection
displays the corresponding completed triple.  The all-different masks on the
three variable groups enumerate permutations and no other assignments. \(\square\)

## 2. Complete radius-one census

The selectors are ordered lexicographically and split into deterministic shards.
Every selector is tested in all four radix orientations.  The exact results are:

| Relative class | Selectors | Shards | CSP nodes | Feasible embeddings |
|---|---:|---:|---:|---:|
| `(7)` | 1,092 | 12 | 749,452,110 | 0 |
| `(5,2)` | 364 | 8 | 237,531,638 | 0 |
| `(4,3)` | 180 | 4 | 155,634,538 | 0 |
| `(3,2,2)` | 112 | 1 | 59,379,166 | 0 |
| **Total** | **1,748** | **25** | **1,201,997,452** | **0** |

### Theorem PX516 -- PROVED FINITE

The displayed selector, shard, and node counts are exact.

The raw coordinate space represented by this census is

\[
1748\cdot4\cdot(7!)^3
=
\boxed{895{,}144{,}255{,}488{,}000}
\]

ordered selector-orientation-coordinate assignments.

### Theorem PX517 -- PROVED FINITE

No radius-one neighbour of any of the four certified side-seven centre selectors
has a no-three scalar embedding in any radix orientation.

### Corollary PX518 -- PROVED REDUCTION

Within each canonical side-seven relative class, any successful abstract
selector has alternating-cycle distance at least two from the corresponding
certified centre.

This is a complete radius-one obstruction, not a proof that the full canonical
host problem is unsatisfiable.

## 3. Verification

Compile the verifier and run its deterministic shards:

```bash
g++ -O3 -std=c++17 scripts/verify_product_side_seven_radius_one_coordinate_census.cpp -o /tmp/side7_r1
/tmp/side7_r1 cycle7 0
# cycle7 shards 0..11; cycle52 shards 0..7;
# cycle43 shards 0..3; cycle322 shard 0.
```

Each shard regenerates the simple-cycle neighbours, checks its exact index range,
runs all four coordinate CSPs, and verifies the recorded node total using exact
integer collinearity tests.
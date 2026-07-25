# Union-safe repair for RI companion rectangles

**Branch:** `research/alternating-core-chain`

AC3et proves the companion rectangle geometry. The original AC3eu full-blocker case used a phase flip, moving the old anchors from the active layer to the blocker layer. That preserves the rectangle union and therefore does not destroy the no-three-in-line certificates on the four-point companion line. This note replaces the blocker menu by repairs which keep both old anchors out of the final two-layer union.

## Setup

Use the AC3et notation

$$
A=(a_0,b_0),
\qquad
Z=(a_1,b_1),
$$

$$
C=(a_0,b_1),
\qquad
D=(a_1,b_0).
$$

The active layer contains the four distinct collinear matching cells

$$
P_x,\ P_{gx},\ A,\ Z.
$$

Hence the grid has at least four rows and columns, and there are at least two active/blocker columns outside `{a_0,a_1}`.

Switch the active diagonal `{A,Z}` to `{C,D}`.

## AC3fw -- union-safe companion blocker repair -- PROVED

Let `t` be the blocker occupancy of `{C,D}`. There is a blocker repair preserving all blocker rows and columns, disjoint from the switched active layer, and containing neither `A` nor `Z`.

### `t=0`

Leave the blocker layer unchanged.

### `t=1`

Suppose `C=(a_0,b_1)` is blocked; the case of `D` is symmetric. The blocker row `b_0` occurs at one outside column because `D` is not blocked and blocker disjointness excludes `A`. Choose a different outside blocker cell

$$
E=(a_2,s_2),
\qquad s_2\ne b_0.
$$

Replace `C,E` by

$$
(a_0,s_2),
\qquad
(a_2,b_1).
$$

Neither old anchor is restored. The symmetric rule for blocked `D` avoids row `b_1`.

### `t=2`

Choose blocker cells

$$
E_2=(a_2,s_2),
\qquad
E_3=(a_3,s_3)
$$

in two distinct outside columns. Replace

$$
C,D,E_2,E_3
$$

by

$$
\boxed{
(a_0,s_2),
\quad(a_1,s_3),
\quad(a_2,b_0),
\quad(a_3,b_1).
}
$$

The final blocker layer contains neither `A` nor `Z`.

### Proof

The selected blocker rows and columns are preserved. In the singleton case, the auxiliary row is chosen to avoid the other old anchor row, while the blocked cross row is moved to an outside column. In the full case, `s_2,s_3` differ from `b_0,b_1` because those rows are already used by `D,C`. Thus the first two replacements are neither old anchors nor active cross cells. The rows `b_0,b_1` moved to outside columns differ from the switched active rows there because they were the original active rows in the distinct columns `a_0,a_1`. QED.

## AC3fx -- union destruction and paid companion decoding -- PROVED

After the active rectangle switch and any AC3fw repair, both old anchors `A,Z` are absent from the final union. Therefore all four current three-subsets of

$$
L_x=\{P_x,P_{gx},A,Z\}
$$

are destroyed, including the private paid original factor

$$
T_x^c=\{P_x,P_{gx},A\}.
$$

The fixed edge `{P_x,P_{gx}}` is unchanged. The active replacement support `{P_x,P_{gx},C,D}` remains internally triple-free by AC3ez.

### Proof

Every old companion-line triple contains `A` or `Z`; the private factor contains `A`. AC3fw excludes both anchors from both layers. AC3ez supplies the replacement-support assertion. QED.

## AC3fy -- corrected direct and absent-anchor products -- PROVED

Replace every use of the AC3eu blocker menu in AC3ev and AC3ew--AC3ex by AC3fw.

1. Direct off-family companion banks remain scope-complete executable paid products after enlarging each envelope by at most two auxiliary blocker cells and four blocker replacements.
2. Absent-anchor composites still install `Z`, repair the first stage, apply the companion rectangle, and repair the final stage; the final AC3fw repair removes both `A,Z` from the union.
3. The private payment, `1/31` extraction, AC2c loss, created-cell-rank router, and constants
   $$
   V/(93K),
   \qquad
   U/(279K),
   \qquad
   U/(153K)
   $$
   remain unchanged.
4. Every product and collateral calculation must use the enlarged union-safe envelope.

### Proof

AC3fw is a finite legal local menu on the same rectangle rows and columns plus at most two explicitly scoped auxiliary blocker cells. AC3v product legality and AC3w payment additivity apply after those cells and all affected scopes are included. AC3fx gives union-level destruction. The weight constants depend only on the prior `1/31`, `1/K`, three-way source split and AC3fa rank split, none of which changes. QED.

## Correction notice

The AC3eu phase flip remains a legal exchange of two permutation diagonals, but the sentence claiming that it destroys the companion-line triples in the two-layer union is false. AC3fw--AC3fy supersede AC3eu for every union-potential use. The same issue is corrected on the source BDA branch by BDA5ai--BDA5ak.

## Finite check

`scripts/verify_ac_ri_companion_union_safe_repair.py` normalizes the active matching, exhausts disjoint blocker permutations and anchor rectangles on grids of size four through seven, verifies every union-safe repair and fixed-edge preservation, and records the full-block phase-flip counterexample.

# Union-safe radial rectangle repairs

**Branch:** `research/bounded-denominator-absorbers`

BDA5a correctly proves the rectangle determinant and the legality of exchanging the two layer matchings on a fully blocked rectangle. That phase flip is not, by itself, a paid decoder for the no-three-in-line potential on the union of the two layers: it moves the old active endpoints to the blocker layer and leaves the same union triples present. This note supplies union-safe repairs for all blocker occupancies. The clean five-cell support provides enough outside columns to reroute blocker rows without restoring either old radial endpoint.

## Setup

For one radial role write

$$
A=(c_0,r_0),
\qquad
B=(c_1,r_1)
$$

for the two active endpoints and

$$
C=(c_0,r_1),
\qquad
D=(c_1,r_0)
$$

for the desired opposite diagonal. The clean BDA support uses five distinct active rows and columns, so the grid has size at least five and there are at least three columns outside `{c_0,c_1}`.

Switch the active layer from `{A,B}` to `{C,D}`. Let the blocker layer occupy `b` of `{C,D}`.

## BDA5ai -- union-safe blocker repair for one role -- PROVED

There is a blocker repair which preserves the blocker row and column sets, remains disjoint from the switched active layer, and contains neither `A` nor `B`.

### Empty diagonal: `b=0`

Leave the blocker layer unchanged.

### Single blocker: `b=1`

Suppose `C=(c_0,r_1)` is blocked; the case of `D` is symmetric. The blocker row `r_0` then occurs in one column outside `{c_0,c_1}`, because `D` is not blocked and blocker disjointness excludes `A`. Choose a different outside blocker cell

$$
E=(c_2,s_2)
$$

with `s_2!=r_0`. Replace `C,E` by

$$
(c_0,s_2),
\qquad
(c_2,r_1).
$$

Neither old endpoint is restored. The symmetric rule for blocked `D` chooses an outside cell whose row is not `r_1`.

### Full blocker diagonal: `b=2`

Choose two blocker cells

$$
E_2=(c_2,s_2),
\qquad
E_3=(c_3,s_3)
$$

in distinct columns outside `{c_0,c_1}`. Replace

$$
C,D,E_2,E_3
$$

by

$$
\boxed{
(c_0,s_2),
\quad(c_1,s_3),
\quad(c_2,r_0),
\quad(c_3,r_1).
}
$$

This four-row permutation contains neither `A` nor `B`.

### Proof

Every replacement uses the same selected blocker rows and columns, so the blocker layer remains a permutation matching. In the single-blocker case, the chosen auxiliary row differs from both the switched active row in the blocked column and the old endpoint row which would restore the paid cell. The row moved to the outside column was an old active row in a different column, so it differs from the switched active row there.

In the full case, `s_2,s_3` are distinct from `r_0,r_1` because the blocker permutation already uses `r_1,r_0` at `c_0,c_1`. Thus the first two replacements avoid `C,D` and `A,B`. At outside columns `c_2,c_3`, the rows `r_0,r_1` differ from the active rows because those were the original active rows in the distinct columns `c_0,c_1`. Hence the layers remain disjoint. QED.

## BDA5aj -- union-safe clean-pair decoder -- PROVED

Apply BDA5ai to either radial role `w` after switching its active endpoints to the opposite diagonal. The final two-layer union contains neither `A_w` nor `B_w`. Therefore both paid radial triples

$$
T_h(P),
\qquad
T_H(P)
$$

are absent from the final union.

Every clean co-anchored adjacent radial pair consequently has a local union-safe decoder for blocker counts zero, one and two. The coupled single-blocker derangement of BDA5c remains a valid alternative when several singly blocked rectangles are processed together, but it is no longer needed for local existence.

### Proof

Each paid radial triple contains one endpoint from each role. Switching either role and applying BDA5ai removes both endpoints of that role from the entire union. The anchor `P` and the other role are irrelevant to destruction once those endpoints are absent. Legality is BDA5ai. QED.

## BDA5ak -- correction to the phase-flip payment interpretation -- PROVED

The fully blocked phase flip in BDA5a preserves both permutation layers and their disjointness, but it preserves the four-cell rectangle union:

$$
\{A,B\}\cup\{C,D\}
$$

before and after the flip. It therefore destroys an active-colour triple only in a colour-sensitive ledger; it does not destroy a no-three-in-line certificate defined on the union.

All union-potential uses of BDA5a--BDA5g must use the BDA5ai union-safe repair in the full-blocker case. The determinant, clean-support and cylinder calculations remain unchanged. Product legality remains valid after enlarging each decoder envelope by the one or two auxiliary blocker cells.

### Proof

A phase flip exchanges which layer contains each diagonal and leaves the set of occupied cells unchanged. BDA5ai instead removes `A,B` from both layers. The other cited calculations depend only on row-column preservation, finite local menus and exact scopes, all of which persist under the auxiliary repairs. QED.

## Consequence

The bounded-denominator decoder now certifies destruction for the actual union potential in all three blocker occupancies. The cost is only a bounded enlargement of the local blocker envelope:

- no auxiliary blocker for `b=0`;
- one for `b=1`;
- two for `b=2`.

No denominator, scale or grid-size loss is introduced.

## Finite check

`scripts/verify_bda_union_safe_rectangle_repair.py` normalizes the active matching, exhausts disjoint blocker permutations and all rectangle orientations on grids of size five through seven, verifies all three repair cases, checks that both old endpoints are absent from the final union, and records the phase-flip counterexample in every full-blocker case.

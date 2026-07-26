# Partner-pool and pair-shadow stability

**Branch:** `research/geometric-cleaning`

GC1a gives the initial admissible partner density and GC3a bounds permanent pool
consumption.  The exact way those two statements compose is a sharp density-loss
formula, not only the special half-pool corollary.  Pair-shadow also has a useful
one-sided stability law: deleting targets or partners cannot create a new
exceptional anchor.  Any threshold crossing must therefore be charged to genuinely
new possible cells, and the crossing margin is bounded by the new cell-pair
incidence.

These are abstract accounting statements.  The remaining geometric work is to
bound the initial blocker sets, the number of genuinely introduced cells and the
reuse of paid current incidence.

## GC1b -- sharp partner-density stability under pool restriction -- PROVED

Let `P_0` be a common initial partner pool.  For every target `b`, let
`I_b subseteq P_0` be its initial inadmissible set and assume

\[
|I_b|\le\delta|P_0|.
\]

Let `P subseteq P_0` be any surviving pool with

\[
|P|\ge\rho|P_0|,
\qquad 0<\rho\le1.
\]

Assume restriction does not create a new blocker on a retained partner: a partner
in `P` is admissible for `b` whenever it was admissible in `P_0`.  Then every target
has at least

\[
\boxed{
|P\setminus I_b|
\ge
|P|-\delta|P_0|
\ge
\left(1-\frac\delta\rho\right)|P|.
}
\]

In particular, positive density survives whenever `delta<rho`.  The earlier
half-pool estimate is the case `rho=1/2`.

### Proof

At most the initially inadmissible elements `I_b` can be bad among the retained
pool.  Therefore

\[
|P\setminus I_b|
=|P|-|P\cap I_b|
\ge|P|-|I_b|
\ge|P|-\delta|P_0|.
\]

Since `|P_0|<=|P|/rho`, the last quantity is at least
`(1-delta/rho)|P|`. QED.

The no-new-blocker hypothesis is essential.  An intermediate switch may create a
new high line or active-core conflict even when the partner itself was retained;
that change belongs to the event inventory below rather than pure pool depletion.

## Possible-cell pair-shadow

For each target `b` and current partner pool `P_b`, let `Z_b(P_b)` be the set of
possible cells inserted by its individually admissible switches, and put

\[
Z(\mathcal P)=\bigcup_b Z_b(P_b),
\qquad
\mathcal P=(P_b)_b.
\]

For an unchanged anchor `a`, let

\[
\lambda_H(a;Z)
\]

be the number of compatible unordered pairs `{z,z'} subseteq Z` such that
`a,z,z'` lie on a line of height at least `H`.

## GC2a -- pair-shadow is monotone under target and pool restriction -- PROVED

Suppose a new target/pool system satisfies

\[
B'\subseteq B,
\qquad
P_b'\subseteq P_b\quad(b\in B'),
\]

and the possible-cell map is restriction-monotone:

\[
Z_b(P_b')\subseteq Z_b(P_b).
\]

Then

\[
\boxed{
Z(\mathcal P')\subseteq Z(\mathcal P)
}
\]

and every unchanged anchor obeys

\[
\boxed{
\lambda_H(a;Z(\mathcal P'))
\le
\lambda_H(a;Z(\mathcal P)).
}
\]

Consequently pure deletion of targets or partners cannot create a new
pair-shadow-exceptional anchor.

### Proof

Every surviving possible cell already belonged to the old possible-cell union, so
the first inclusion holds.  Every compatible unordered pair in the smaller set is
also a compatible unordered pair in the larger set, proving the second display.
QED.

This statement concerns the possible-cell inventory.  If an intermediate switch
changes line heights, protected status or the rule defining admissibility, the
resulting newly possible cells must be recorded explicitly.

## GC3c -- exact new-pair increment identity -- PROVED

Let `Z` be an old possible-cell set and let `Y` be a disjoint set of genuinely new
possible cells.  For an anchor `a`, define

\[
e_H(a;Z,Y)
=
|\{(z,y)\in Z\times Y:a,z,y\text{ are compatible and collinear on a height-}\ge H\text{ line}\}|.
\]

Then

\[
\boxed{
\lambda_H(a;Z\cup Y)-\lambda_H(a;Z)
=
e_H(a;Z,Y)+\lambda_H(a;Y).
}
\]

If `a` had old load at most `Theta-eta` and new load greater than `Theta`, where
`eta>=0`, then

\[
\boxed{
e_H(a;Z,Y)+\lambda_H(a;Y)>\eta.}
\]

For integer loads, the right side is at least `floor(eta)+1`.

### Proof

Partition the compatible unordered pairs in `Z union Y` into pairs contained in
`Z`, pairs with one endpoint in each set, and pairs contained in `Y`.  The three
classes are disjoint and have sizes `lambda_H(a;Z)`, `e_H(a;Z,Y)` and
`lambda_H(a;Y)`.  Subtraction gives the identity.  A threshold crossing from at
most `Theta-eta` to more than `Theta` requires increment greater than `eta`. QED.

Thus a new exceptional anchor is never caused by retained old pairs alone.  It
carries a positive incidence with the new-cell inventory, and a crossing with
margin `eta` carries at least `eta` such incidence.

## GC3d -- paid new-pair charging bounds exceptional-anchor creation -- PROVED

Consider a sequence of possible-cell inventories.  At step `i`, first restrict the
old target/pool system and then add a disjoint genuinely new cell set `Y_i`.  Let
`A_i` be a set of anchors whose pre-addition load is at most `Theta-eta` and whose
post-addition load is greater than `Theta`, for one fixed `eta>0`.

Assume every new cross-pair or new--new pair incidence counted in GC3c is assigned
to paid current syndrome incidence, with:

1. total original paid incidence weight `W`;
2. each paid incidence used with total multiplicity at most `R` across all steps and
   anchors;
3. one unit of pair-shadow increment requiring one unit of charge.

Then

\[
\boxed{
\sum_i|A_i|
<
\frac{RW}{\eta}.
}
\]

For integer loads one may replace `eta` in the denominator by
`floor(eta)+1` and use a weak inequality.

### Proof

By GC3c, every anchor in `A_i` receives more than `eta` units of new-pair
increment.  Therefore all threshold crossings require more than
`eta sum_i|A_i|` charged units.  The reuse hypothesis permits at most `RW` charged
units in total.  Comparing the two quantities proves the display. QED.

The theorem is intentionally margin-sensitive.  Without a positive margin, one new
pair can create an exceptional anchor, so only a raw count of newly introduced
pairs is available.

## Combined GC1--GC3 interface

Suppose one scale epoch supplies:

- GC1a initial blocker density `delta`;
- GC3a depletion leaving a pool fraction at least `rho`;
- no new blocker on retained partners except through an explicitly inventoried
  state change;
- a pre-addition pair-shadow margin `eta` for nonexceptional anchors;
- a paid new-pair charge with reuse at most `R`.

Then:

1. every unchanged target retains relative partner density at least
   `1-delta/rho` by GC1b;
2. pure restriction creates no new pair-shadow exception by GC2a;
3. every actual new exception is witnessed by the exact GC3c new-pair inventory;
4. the total number of margin-`eta` exceptions is below `RW/eta` by GC3d.

The unresolved geometric obligations are now explicit: prove `delta<rho`, bound the
new cell-pair inventory by current paid syndrome incidence, and keep the reuse
constant and crossing margin compatible with the L4 drift constants.

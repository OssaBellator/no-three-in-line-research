# GC1--GC3 partner-pool and pair-shadow event import

**Branch:** `research/alternating-core-chain`

AC5q--AC5t inventory newly possible assignments, while the geometric-cleaning track separately proves
sharp partner-pool restriction and pair-shadow threshold accounting. This note imports those results
into one AC5 menu interface. It closes the deterministic inventory question: pure deletion cannot
create a pair-shadow exception, and every actual new exception is charged to a genuinely new possible
cell pair.

The result does not by itself prove the quantitative AC5 drift inequality. The final comparison still
requires either the per-cylinder reverse-load bound of AC5y--AC5ab or the aggregate min-cost Hall-flow
bound of AC5ac--AC5af for the complete inventory identified here.

## Menu and possible-cell model

Fix one AC5 menu epoch. Let `P_0` be an initial common partner pool. For each target `b`, let
`I_b subseteq P_0` be the initially blocked partners and assume

`|I_b|<=delta |P_0|`.

After paid depletion and restriction, let `P_b subseteq P_0` satisfy

`|P_b|>=rho |P_0|`,

with `0<rho<=1`. Retained initially admissible partners remain admissible unless a declared state
change creates a new blocker. Every such state change is entered as an AC5 event atom.

For a target/pool system `P=(P_b)_b`, let `Z(P)` be the union of cells that can be inserted by its
individually admissible menu states. For an unchanged anchor `a`, let

`lambda_H(a;Z)`

count compatible unordered pairs of cells in `Z` that form with `a` a line of height at least `H`.

When one menu transition first restricts old targets/pools and then introduces a disjoint set `Y` of
genuinely new possible cells, define

`e_H(a;Z,Y)`

as the number of compatible old--new pairs `(z,y) in Z x Y` collinear with `a` on a height-at-least-`H`
line.

## AC5ag -- sharp admissible density after paid pool depletion -- PROVED

Every target retains at least

`|P_b|-delta |P_0| >= (1-delta/rho)|P_b|`

initially admissible partners. In particular a positive admissible density survives whenever
`delta<rho`.

### Proof

At most the initially blocked set `I_b` can be bad among retained partners before declared new-blocker
events are added. Hence

`|P_b\I_b|>=|P_b|-|I_b|>=|P_b|-delta|P_0|`.

Since `|P_0|<=|P_b|/rho`, the displayed relative bound follows. QED.

Every newly created blocker is excluded from this estimate and appears as its own event atom.

## AC5ah -- restriction cannot create pair-shadow mass -- PROVED

If targets are deleted and every surviving partner pool is restricted, with the possible-cell map
restriction-monotone, then

`Z(P') subseteq Z(P)`

and

`lambda_H(a;Z(P'))<=lambda_H(a;Z(P))`

for every unchanged anchor `a`.

### Proof

Every possible cell after restriction was already possible before restriction. Every compatible pair
in the smaller set is therefore a pair in the larger set. QED.

Thus paid pool depletion alone creates no new pair-shadow-exceptional anchor.

## AC5ai -- exact new-cell pair-shadow inventory -- PROVED

For an old possible-cell set `Z` and a disjoint genuinely new set `Y`,

`lambda_H(a;Z union Y)-lambda_H(a;Z)=e_H(a;Z,Y)+lambda_H(a;Y)`.

If the old load is at most `Theta-eta` and the new load exceeds `Theta`, then

`e_H(a;Z,Y)+lambda_H(a;Y)>eta`.

For integer loads the increment is at least `floor(eta)+1`.

### Proof

Partition compatible unordered pairs in `Z union Y` into old--old, old--new and new--new classes.
Subtract the old--old class. A threshold crossing with margin `eta` requires the asserted increment.
QED.

The two right-hand terms are the complete pair-shadow event inventory for the transition.

## AC5aj -- pathwise charged threshold-crossing bound -- PROVED

Consider a sequence of menu transitions. At transition `j`, first restrict the old system and then
add a genuinely new cell set `Y_j`. Let `A_j` be the anchors that cross from load at most
`Theta-eta` to load greater than `Theta`, where `eta>0`.

Suppose every old--new or new--new incidence counted by AC5ai is assigned to a paid current event atom,
with total paid weight `W`, total reuse at most `R`, and one unit of pair-shadow increment requiring one
unit of charge. Then

`sum_j |A_j| < R W/eta`.

### Proof

AC5ai gives more than `eta` charged units for every crossing anchor. All crossings therefore require
more than `eta sum_j |A_j|` units, while the reuse hypothesis supplies at most `RW`. QED.

This is a pathwise statement and does not assume independence between installation steps.

## AC5ak -- complete GC1--GC3 event interface for one AC menu -- PROVED UNDER THE DECLARED INVENTORY CONTRACT

Suppose one AC5 menu epoch provides:

1. an initial partner-blocker density `delta`;
2. paid depletion leaving pool fraction at least `rho`, with `delta<rho`;
3. explicit event atoms for every new blocker on a retained partner;
4. a pre-addition pair-shadow margin `eta>0` at every nonexceptional unchanged anchor;
5. a complete new-cell list `Y_j` at every step;
6. an occurrence-faithful charge of all AC5ai old--new and new--new incidences to paid current event atoms with reuse at most `R`.

Then the GC1--GC3 part of the AC5 inventory is complete:

- every target retains partner density at least `1-delta/rho` before inventoried state-change blockers;
- pure restriction contributes zero new pair-shadow mass;
- every new pair-shadow exception is represented by an old--new or new--new event cylinder;
- the total number of margin-`eta` threshold crossings is less than `RW/eta`;
- no partner-loss, pool-depletion or pair-shadow event remains outside the event list.

The resulting complete inventory may be inserted directly into the AC5y per-cylinder objective or the
AC5ac aggregate min-cost objective.

### Proof

Apply AC5ag to partner density, AC5ah to the restriction stage, AC5ai to every addition stage and AC5aj
to the pathwise threshold crossings. The declared new-blocker atoms cover the only partner failures
excluded from AC5ag. QED.

## Corrected AC5 frontier

The deterministic GC1--GC3 partner, pool and pair-shadow inventory is now closed for every menu
satisfying the six explicit contracts above. The remaining work is quantitative: prove the initial
`delta` bound and depletion fraction `rho` for each concrete menu, construct the complete new-cell sets,
bound charge reuse `R`, and verify the resulting per-cylinder reverse-load or aggregate min-cost drift
inequality through all intermediate states.

## Finite check

`scripts/verify_ac_gc_pool_shadow_import.py` exhausts small partner pools and abstract pair-shadow
relations. It verifies the sharp density formula, restriction monotonicity, the exact old--new plus
new--new increment identity and the charged threshold-crossing bound.

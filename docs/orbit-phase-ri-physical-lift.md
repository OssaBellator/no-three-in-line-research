# Physical rational-inverse lift of a paid orbit-phase quotient edge

**Branch:** `research/orbit-phase-expansion`

OP4i localizes paid implication occurrences to one rational quotient edge, but
a quotient edge alone is not a physical RI5 block. This note reconstructs the
actual rational-inverse record and base-scale coset from every real two-channel
factor, then gives an exact complete-fibre, root-scale pairing router.

The output is a physically coherent fixed-edge class at the quotient-coset
level. It does not assert that the class is already installed as a completion
component; row/column completion, owner payment, and blocker collateral remain
separate RI5 obligations.

## OP4p -- one real two-channel factor gives an exact physical RI record -- PROVED

Let

\[
P_x=(x,\langle a/x\rangle_p),\qquad
P_u=(u,\langle a/u\rangle_p),\qquad
B_z=(z,\langle b/z\rangle_p)
\]

be a distinct really collinear factor with two points on `H_a` and one point on
`H_b`. Put

\[
r=b/a,\qquad c=z/x,\qquad g=u/x.
\]

Then

\[
\boxed{g=F_r(c)=\frac{c(1-c)}{r-c}},
\]

with companion root

\[
\boxed{c^\dagger=\tau_r(c)=\frac{r(c-1)}{c-r}},
\]

and

\[
F_r(c^\dagger)=g,\qquad cc^\dagger=rg.
\]

For every multiplicative subgroup `H`, define quotient labels

\[
A=cH,\quad B=c^\dagger H,\quad C=gH,\quad R=rH,
\quad S=xH.
\]

They satisfy

\[
\boxed{B=RCA^{-1}},
\]

and the physical source, partner, and anchor cosets are

\[
\boxed{xH=S,\qquad uH=CS,\qquad zH=AS.}
\]

Thus the quotient roots, image, companion, and physical scale are reconstructed
from the actual factor; no quotient-to-physical identification is guessed.

### Proof

The collinearity determinant gives the displayed rational map. Direct
substitution proves `F_r(c^dagger)=g`, and multiplication gives
`cc^dagger=rg`. Passing to quotient cosets yields `AB=RC`, hence
`B=RCA^{-1}`. The final identities follow from `u=gx` and `z=cx`. QED.

## Complete fibres and scale tables

Fix one exact ordered channel pair and one quotient edge. Group occurrences by
the exact rational fibre

\[
\mathcal O(c)=(\{c,\tau_r(c)\},F_r(c)).
\]

A fibre is complete when both roots are genuinely witnessed, with the usual
one-root convention at a fixed point. For a complete fibre `f`, root signs
`+,-`, and physical scale coset `S`, let `a_{f,S},b_{f,S}` be the
factor-conservative occurrence weights on the two roots.

Put

\[
T=\sum_{f,S}(a_{f,S}+b_{f,S}),\qquad
M=\sum_{f,S}\min(a_{f,S},b_{f,S}),\qquad
E=\sum_{f,S}|a_{f,S}-b_{f,S}|.
\]

## OP4q -- paid complete-versus-incomplete fibre split -- PROVED

Let a factor-conservative occurrence family on one quotient edge have total
weight `W`, and let `P` be the number of represented exact ordered channel
pairs. One channel-pair class has weight at least `W/P`. Inside that class,
one of the following holds.

1. Complete fibres carry weight at least `W/(2P)`.
2. Incomplete fibres carry weight greater than `W/(2P)` and return every
   witnessed root, image, missing companion root, physical scale, source
   factor, and carry label.

If at most `q_act` channels occur, then
`P<=q_act(q_act-1)`.

### Proof

Choose a heaviest channel-pair class and split it into complete and incomplete
fibre weight. One side carries at least half. QED.

## OP4r -- coherent root-scale pairing or one-root imbalance -- PROVED

The exact identity

\[
\boxed{T=2M+E}
\]

holds. Consequently, either

\[
\boxed{M\ge T/4,}
\]

and there is a disjoint paid family of complete fibres whose two roots are
actually witnessed at one common scale coset, or

\[
\boxed{E>T/2,}
\]

and one root sign has unmatched excess greater than `T/4`.

### Proof

For nonnegative `a,b`,

\[
a+b=2\min(a,b)+|a-b|.
\]

Sum over `(f,S)`. If `M<T/4`, then `E=T-2M>T/2`; one of the two excess signs
carries more than `E/2>T/4`. Pairing uses disjoint portions of the two
occurrence measures. QED.

## OP4s -- fixed-edge physical-lift router -- PROVED

Fix a scale-count threshold `K>=1` and an exact finite decoration alphabet of
size `L`. A factor-conservative paid family of total weight `W` on one
quotient edge yields one of the following.

1. **Paid incomplete fibres:** weight at least `W/(2P)` with explicit missing
   companions.
2. **Paid one-root scale imbalance:** one sign and one exact profile carry
   weight greater than
   \[
   \boxed{W/(8PL).}
   \]
3. **Physical scale dispersion:** more than `K` coherent scale cosets occur.
4. **One coherent physical fixed-edge class:** one scale and one exact
   decoration carry paired paid weight at least
   \[
   \boxed{W/(8PKL).}
   \]
   Every retained record has actual witnesses of both roots at that scale, and
   OP4p reconstructs all source, image, companion, and scale cosets.

### Proof

Unless outcome 1 holds, OP4q leaves complete-fibre weight
`T>=W/(2P)`. OP4r either gives one-sign excess greater than `T/4`, followed by
the `L`-profile split, or paired coherent weight at least `T/4`. In the latter
case, either more than `K` scales occur or one scale carries at least `1/K` of
the paired weight; split its decoration at cost `L`. Substitute the lower
bound for `T`. QED.

## Consequence for OP5

A fixed quotient edge no longer carries an abstract, scale-free RI label. It
now returns incomplete companion data, a paid one-root scale imbalance,
physical scale dispersion, or one coherent physical fixed-edge class. The
last output is the exact arithmetic input to RI5 fixed-edge installation.

The unresolved work is physical completion and blocker-safe installation, not
reconstruction of the quotient roots or scale cosets.

## Finite check

`scripts/verify_phase_ri_physical_lift.py` enumerates real two-channel factors
over small prime fields, checks the rational identities and quotient-coset
reconstruction for every subgroup, and exhausts small root-by-scale weight
tables to verify `T=2M+E` and the router constants.

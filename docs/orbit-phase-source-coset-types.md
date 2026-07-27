# Source-coset path and cycle profiles in the closed fixed-edge bank

**Branch:** `research/orbit-phase-expansion`

OP4t--OP4x install every coherent physical fixed-edge class through one common I6 completion closure. A failed bank returns one of `C_1,C_2,C_3,B`. This note converts every variable term into an exact finite path/cycle profile with a quantitative raw-weight amplification.

## Partial source-coset map

A compatible active prescription on `r` distinct source cosets fixes:

1. an injective partial map from source cosets to target cosets;
2. one subgroup shift for every prescribed source coset.

Collapse all prescribed cells inside the same source coset to that one coset image and shift. The resulting directed partial permutation has indegree and outdegree at most one.

## OP4y -- complete source-coset type dictionary -- PROVED

For `r<=3`, the partial source-coset map has exactly the following canonical types:

- `r=1`: `P_1`;
- `r=2`: `P_1+P_1`, `P_2`, or `C_2`;
- `r=3`: `P_1+P_1+P_1`, `P_2+P_1`, `P_3`, `C_2+P_1`, or `C_3`.

Hence

\[
\boxed{\nu_1=1,\qquad \nu_2=3,\qquad \nu_3=5.}
\]

### Proof

The prescribed coset map is an injective loop-free partial permutation. Its components are directed paths and cycles. Enumerating all partitions of at most three arcs gives exactly the displayed list. QED.

## OP4z -- exact probability is independent of source-coset type -- PROVED

Fix a compatible rank-`r` source-coset type, its actual source and target cosets, and all `r` subgroup shifts. Under the uniform I6 bank,

\[
\boxed{
\Pr(T)=\frac1{(m)_rh^r}.
}
\]

The probability does not depend on whether the partial map is a path, a cycle or a disjoint union.

### Proof

The prescription fixes `r` distinct images of the `m` source cosets and `r` independent shifts. It leaves `(m-r)!h^{m-r}` states among `m!h^m`. The component arrangement does not change that count. QED.

## Active collateral localization

Let `L_r` bound the number of finite physical/arithmetic decorations retained after fixing one of the `nu_r` source-coset types. Decorations include the physical roots, quotient edge, scale class, line/channel role and any declared carry label.

## OP4aa -- failed active term gives one amplified exact type -- PROVED

Let

\[
G=\left(1-\frac1{mh}\right)W-F>0.
\]

If the failed OP4w bank returns `C_r>=G/4`, then one exact source-coset path/cycle type and one decoration class has raw candidate weight at least

\[
\boxed{
\frac{G(m)_rh^r}{4\nu_rL_r}.
}
\]

### Proof

The term `C_r` is the sum of raw candidate weights multiplied by the common probability `1/[(m)_rh^r]`. Split it among at most `nu_r L_r` exact classes. One class contributes expected weight at least `G/(4nu_rL_r)`. Divide by its exact probability. QED.

Thus:

\[
r=1:\quad \frac{Gmh}{4L_1},
\]

\[
r=2:\quad \frac{G(m)_2h^2}{12L_2},
\]

\[
r=3:\quad \frac{G(m)_3h^3}{20L_3}.
\]

## OP4ab -- exact blocker-type import -- PROVED UNDER THE RI5 REPAIR MENU

Assume the blocker profile alphabet has size `L_B` before the final path/cycle type split. If the failed OP4w bank returns `B>=G/4`, then one of the following exact raw profiles occurs:

1. a singleton affine profile of weight at least
   \[
   \boxed{\frac{(n-1)G}{12L_B}};
   \]
2. a finite small-derangement profile of weight at least
   \[
   \boxed{\frac{G}{12L_B}};
   \]
3. an exact large `(t,s,q)` path/cycle type of weight at least
   \[
   \boxed{\frac{(t)_sG}{216L_B}}.
   \]

### Proof

The closed OP bank uses the same zero/singleton/multiple blocker-repair menu as RI5. Apply RI5ak--RI5at to `B>=G/4`. The singleton and finite-small constants are unchanged. RI5aw shows that refining the large exact overlap profile to a path/cycle type loses at most a factor two. QED.

## OP4ac -- corrected named-output frontier -- PROVED

A failed coherent fixed-edge bank now returns exactly one of:

1. state-independent collateral `F`;
2. one amplified active source-coset path/cycle type from OP4aa;
3. one exact singleton, small or large blocker type from OP4ab.

The active and blocker terms contain no unclassified finite combinatorics. Remaining work is arithmetic interpretation, physical payment, absorption or recurrence of these exact labelled types, plus the incomplete-fibre and scale alternatives preceding the coherent bank.

## Finite check

`scripts/verify_phase_source_coset_types.py` enumerates the rank-at-most-three source-coset type dictionary, exhausts small I6 banks, verifies every exact prescription probability and checks the amplification constants.

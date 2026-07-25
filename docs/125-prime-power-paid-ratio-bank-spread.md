# The paid mixed-ratio bank has exact completion spread

CMR325 constructs a disjoint union of equal-size cylinders. Conditional on one
ratio line `L`, three cells `Q_L` are fixed and the remaining state is a uniform
perfect matching of a complete `(t-3)` by `(t-3)` bipartite graph. This gives
an exact cylinder law and an exact candidate-only collateral identity after the
one guaranteed ratio triple is separated.

Let

\[
m=|\mathcal R|,
\qquad
n=t-3,
\]

and sample uniformly from the bank \(\mathcal B(\mathcal R)\) of CMR324.
Equivalently:

1. choose `L` uniformly from `\mathcal R`;
2. include `Q_L`;
3. complete uniformly on the remaining `n` source and target vertices.

Every candidate cell belongs to at most one designated triple `Q_L`: on each of
the three fan slices, the line intersections are distinct, and no designated
cell lies off those slices.

## 1. Conditional completion cylinders

### Theorem CMR326 — PROVED

Fix `L`. Let `R` be a compatible prescription of `r` candidate cells. Suppose
`R` is compatible with `Q_L`, put

\[
s=|R\cap Q_L|,
\]

and assume `r-s<=n`. Then

\[
\boxed{
\Pr(R\subseteq\pi\mid L)
=
\frac{1}{(n)_{r-s}}.
}
\]

If `R` conflicts with `Q_L`, the conditional probability is zero.

### Proof

The cells of `R` already contained in `Q_L` require no completion edges. The
other `r-s` cells use distinct residual source and target vertices. A uniform
perfect matching of `K_{n,n}` contains that prescription with probability
`1/(n)_{r-s}`. ∎

## 2. Unconditional low-rank atoms

Assume throughout this section that

\[
\boxed{t\ge6,}
\]

so `n>=3` and all rank-three denominators below are defined.

### Corollary CMR327 — PROVED

For every compatible candidate cell `z`, pair `P`, and triple `T`,

\[
\boxed{
\Pr(z\in\pi)
\le
\frac{1}{m}+
\frac{1}{n},
}
\]

\[
\boxed{
\Pr(P\subseteq\pi)
\le
\frac{1}{m}
+
\frac{2}{mn}
+
\frac{1}{(n)_2},
}
\]

and

\[
\boxed{
\Pr(T\subseteq\pi)
\le
\frac{1}{m}
+
\frac{3}{mn}
+
\frac{3}{m(n)_2}
+
\frac{1}{(n)_3}.
}
\]

### Proof

A fixed cell lies in at most one `Q_L`. In that block it is certain; in every
other compatible block CMR326 gives probability `1/n`. Averaging and slightly
overcounting the completion contribution gives the first bound.

For a pair, at most one block contains both prescribed cells in `Q_L`, and at
most two further blocks contain one prescribed cell. All remaining blocks use
two completion cells. CMR326 gives the second inequality.

For a triple, at most one block contains all three cells, at most three blocks
contain one of its three prescribed pairs, and at most three further blocks
contain one prescribed cell. Use the rank `0,1,2,3` conditional probabilities
from CMR326 and again overcount harmlessly. ∎

When CMR309 supplies `m=Omega_p(t)`, the single-cell atom is `O_p(1/t)` and all
three displayed atoms are `O_p(1/t)` because the bank deliberately fixes one
rank-three certificate.

## 3. Exact candidate-only collateral after the paid triple

Continue to assume `t>=6`. For fixed `L`, let `U_s(L)` be the number of
compatible candidate-only collinear triples `T` such that

1. `T` is compatible with `Q_L`;
2. `T` is not `Q_L`;
3. \(|T\cap Q_L|=s\).

Only `s=0,1,2` occur.

### Theorem CMR328 — PROVED

Conditional on `L`, the expected number of candidate-only collinear triples in
the completed state is exactly

\[
\boxed{
1
+
\frac{U_0(L)}{(n)_3}
+
\frac{U_1(L)}{(n)_2}
+
\frac{U_2(L)}{n}.
}
\]

The initial `1` is the designated paid ratio triple `Q_L`.

### Proof

The triple `Q_L` is always present. Every other compatible candidate-only
triple uses exactly `3-s` completion cells when it shares `s` designated cells.
CMR326 gives occurrence probability `1/(n)_{3-s}`. Sum by `s`. ∎

Averaging over the ratio lines gives

\[
\boxed{
\mathbb E\,T_{\mathrm{cand}}
=
1
+
\frac{1}{m}
\sum_{L\in\mathcal R}
\left(
\frac{U_0(L)}{(n)_3}
+
\frac{U_1(L)}{(n)_2}
+
\frac{U_2(L)}{n}
\right).
}
\]

## 4. The rank-two-on-the-paid-line term

### Corollary CMR329 — PROVED

For every `L` and `t>=6`,

\[
\boxed{U_2(L)\le3(t-3).}
\]

Hence

\[
\boxed{\frac{U_2(L)}{n}\le3.}
\]

### Proof

A triple sharing two cells with `Q_L` must use one of the three pairs of
`Q_L`. Each pair determines the same real line `L`; the third cell may be any
other compatible cell on that line. There are at most `t-3` choices after the
three designated cells are removed. Summing over the three pairs gives the
bound. ∎

## 5. Revised weighted-conversion target

The guaranteed destroyed old target and the guaranteed ratio triple cancel at
unit scale. All additional candidate-only collateral is now exposed in the
three normalized quantities of CMR328. Rank two is universally bounded by
CMR329; ranks zero and one are the remaining secant/line-incidence terms and
can be split by primitive height, first separation, and carry signature.

Thus the weighted mixed-fan problem is reduced to the same quotient/carry
energies already present in the prefix and joint-parent analyses. What remains
is a strict average inequality or a batch argument destroying more than one
old target per guaranteed ratio triple.

At `t=5`, CMR326 remains exact for every prescription satisfying `r-s<=2`.
The rank-three formulas are intentionally left to the finite root census rather
than interpreted with zero falling-factorial denominators.

No all-`n` theorem is claimed here. Conditional completion probabilities,
unconditional atoms, and the exact collateral identity are checked in
[`scripts/verify_prime_power_paid_ratio_spread.py`](../scripts/verify_prime_power_paid_ratio_spread.py).

# Rational inverse expansion and simultaneous small doubling

**Branch:** `research/rational-inverse-expansion`

This independent inverse-theory track addresses I12. Its output can simplify or classify structured exceptions encountered by the alternating-core branch, but the theorem can be attacked without the neutralization or multiscale machinery.

## Proved inputs

Let

\[
F_r(x)=\frac{x(1-x)}{r-x}
\]

be the normalized ratio map arising from the Möbius-cycle dynamics.

- I5–I8: small quotient sets give coset covers, absorber banks, and structured anchor propagation;
- I9: a full subgroup coset of order at least three expands to at least two cosets under `F_r`;
- I10: the exact order-two nonexpansion exception is `x^2=r`;
- I11: rank-zero alternating cores expand except through that order-two orbit.

## RI1 — Dense-subset coset expansion — REFUTED AS STATED

### Target statement

Let `H<=F_p^*`, let `C subseteq xH`, and assume

\[
|C|>(1/2+epsilon)|H|.
\]

Prove a quantitative alternative:

1. `F_r(C)` meets at least `(1+c_epsilon)|H|` points or at least two `H`-cosets with density `c_epsilon`; or
2. `H` has order two and the parameters lie in the classified square-root exception; or
3. `C` is contained in an explicit bounded exceptional set associated with poles, zeros, or fixed points of `F_r`.

A quotient-set formulation such as `|F_r(C)/F_r(C)|>= (1+c_epsilon)|C|` is also useful.

The full subgroup `H=F_p^*` refutes this statement: after deleting the pole
and zero, a dense set still has image in the unique `H`-coset and cannot
have more than `|H|` points. The corrected target must assume `H` is
proper and `C subseteq F_p^*\{1,r}`. See
[`rational-inverse-collision-and-obstructions.md`](rational-inverse-collision-and-obstructions.md).

### Proved structural reduction

[`rational-inverse-fibre-energy.md`](rational-inverse-fibre-energy.md)
proves the exact identity

`|F_r(C)| = |C| - (number of full nonfixed collision orbits)`.

For `C subseteq xH`, every collision orbit is a solution in `H^2` of one
explicit bilinear equation. Thus any corrected RI1 failure with
`|F_r(C)| <= (1-delta)|C|` supplies `delta|C|` disjoint solutions on that
curve. The remaining task is the subgroup incidence/classification bound.

[`rational-inverse-subgroup-overlap.md`](rational-inverse-subgroup-overlap.md)
proves RI1c for a full source coset: its exact collision loss is a subgroup
intersection with one explicit Möbius map, up to at most two fixed points.
It also expands that intersection into \(m^2\) explicit multiplicative
character sums for subgroup index \(m\), and proves that only the trivial
character pair can be an \(m\)-th-power main term.

[`rational-inverse-weil-overlap.md`](rational-inverse-weil-overlap.md)
proves RI1d by applying the standard Weil character bound:

\[
\left|J(H;r,x_0)-\frac{p-3}{m^2}\right|<3\sqrt p.
\]

It follows that every subset of one source coset loses at most
\((p-3)/(2m^2)+(3/2)\sqrt p\) image values to internal collision pairs.
The remaining RI1 input is target-coset distribution or quotient growth,
not source-fibre cardinality.

[`rational-inverse-target-cosets.md`](rational-inverse-target-cosets.md)
proves RI1e:

\[
\left|N(x_0H,y_0H)-\frac{p-3}{m^2}\right|<3\sqrt p
\]

for every source and target coset. A dense subset \(C\) therefore meets
at least \(|C|/A_m(p)\) target cosets, with explicit two-coset density
bounds once \(|C|>A_m(p)\). This proves the corrected RI1 target-coset
alternative for every fixed subgroup index and sufficiently large \(p\).
The remaining issue is uniform growing-index control and absorber
conversion.

## RI2 — Union-of-cosets image theorem

### Target statement

Let

\[
C=\bigcup_{i=1}^m x_iH
\]

be a union of full `H`-cosets. Bound the minimum number of `H`-cosets meeting `F_r(C)` in terms of `m`, `|H|`, and the algebraic coincidences among the `x_i`.

The desired form is

\[
N_H(F_r(C))\ge m+c m-O(1)
\]

unless the source cosets form one of finitely many exceptional chains. A weaker polynomial expansion bound is acceptable if it still prevents indefinite alternating recombination.

The domain must explicitly remove or isolate the cosets containing `1` and
the pole `r`; otherwise `F_r(C)` is not a subset of `F_p^*` or is not
defined.

### Small-index case proved

RI2a in
[`rational-inverse-target-cosets.md`](rational-inverse-target-cosets.md)
proves maximal coverage

\[
N_H(F_r(C\setminus\{1,r\}))=m
\]

whenever \(p-3>3(m^2-1)\sqrt p\). This includes every fixed subgroup
index and the asymptotic range
\(m<(1/\sqrt3-o(1))p^{1/4}\). The remaining RI2 problem is the
large-index range, where several source-coset character sums must be
combined rather than bounded separately.

[`rational-inverse-union-collision.md`](rational-inverse-union-collision.md)
proves RI2b--RI2c uniformly in that remaining range. A union of \(s\)
source cosets always meets at least
\(\lceil(s|H|-2)/(2|H|)\rceil\) target cosets. More importantly, if it
meets only \(k\) target cosets, it contains at least
\((s-k)|H|-2\) full collision pairs, and one unordered source-coset pair
carries a \(1/\binom{s+1}{2}\) share on one explicit bilinear subgroup
curve. The remaining incidence problem is therefore two-coset rather
than an arbitrary union.

[`rational-inverse-cross-coset-cap.md`](rational-inverse-cross-coset-cap.md)
proves RI2d--RI2e by applying the four-point Weil calculation uniformly
to every ordered pair of source cosets. A union of \(s\) source cosets
has at most \(s^2A_m(p)/2\) full collision pairs, and therefore

\[
(s-k)|H|\le e+\frac{s^2}{2}A_m(p).
\]

If the right side is smaller than \(|H|\), the image meets at least
\(s\) target cosets. For fixed \(s\), this gives a nontrivial growing
index range through \(m=o(\sqrt p)\); saturation and the genuinely
larger-index regime remain to be classified.

## RI3 — Simultaneous small-doubling classification

### Target statement

For fixed `K`, classify all sets `C subseteq F_p^*` satisfying

\[
|C/C|\le K|C|,
\qquad
|F_r(C)/F_r(C)|\le K|F_r(C)|.
\]

Prove that `C` is covered by `K^{O(1)}` translates of one subgroup `H` and that one of the following holds:

- `|H|=O_K(1)`;
- `C` lies in a bounded union of explicit order-two exceptional chains;
- `F_r` permutes a finite coset configuration that can be listed and absorbed;
- the two quotient sets actually expand by a factor depending only on `K`.

A convex-coset-progression conclusion is insufficient unless it is converted into an executable absorber or expansion statement.

RI1a also reduces the cardinality part of simultaneous nonexpansion to
linear collision mass. RI3 must combine that exact fibre structure with
the two quotient-set hypotheses; fibre degree alone is insufficient.

## RI4 — Order-two chain classification — REFUTED AS STATED

### Target statement

Classify every finite sequence

\[
C_0,C_1,\ldots,C_s,
\qquad C_{i+1}=F_{r_i}(C_i),
\]

in which each `C_i` is covered by order-two subgroup cosets and no quotient-rank expansion occurs. Prove that the chain is periodic with bounded period and has an explicit row-column-preserving absorber state.

Singletons give arbitrarily long nonperiodic counterexamples: any desired
transition `c_i -> c_{i+1}` is realized by
`r_i=c_i+c_i(1-c_i)/c_{i+1}`, while every singleton is covered by an
order-two coset and has quotient rank zero. RI4 must require full or
quantitatively dense cosets and charge pair-collapse mass.

## RI5 — Absorber interface

### Target statement

Every structured set produced by RI1–RI4 either:

1. expands multiplicative quotient complexity by a fixed amount;
2. yields a common-ratio rectangle bank carrying a constant fraction of its syndrome;
3. lies in a finite coset-state bank covered by I6;
4. is an explicit bounded order-two exception with a direct two-colour trade.

This is the exact interface imported by AC3–AC4.

## Suggested tools

- finite-field sum-product for rational functions;
- incidence bounds for equations `F_r(x)/F_r(y)=u`;
- Kneser and critical-pair theory in `F_p^*`;
- character sums over subgroup cosets;
- algebraic geometry of low-degree correspondences between source and image cosets;
- exhaustive classification for small subgroup orders.

## Falsification programme

Search small primes for:

- dense subsets of one coset whose image remains in one coset;
- unions of several cosets that recombine under `F_r`;
- long order-two exceptional chains;
- simultaneous small-doubling examples not predicted by the current templates.

The exact collision involution, subgroup-overlap formula and Weil bound,
full-subgroup RI1 obstruction, and singleton RI4 obstruction are now
proved and checked by `scripts/verify_rational_inverse.py`,
`scripts/verify_rational_subgroup_overlap.py`, and
`scripts/verify_rational_weil_overlap.py`. Target-coset equidistribution
is checked by `scripts/verify_rational_target_cosets.py`.

## Completion criterion

This branch is complete when the corrected RI1–RI5 prove I12 in a form that
either forces quotient expansion or returns an explicit absorbable finite
coset configuration. The unqualified original RI1 and RI4 statements must
not be reinstated.

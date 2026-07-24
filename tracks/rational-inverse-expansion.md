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

## RI1 — Dense-subset coset expansion

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

## RI4 — Order-two chain classification

### Target statement

Classify every finite sequence

\[
C_0,C_1,\ldots,C_s,
\qquad C_{i+1}=F_{r_i}(C_i),
\]

in which each `C_i` is covered by order-two subgroup cosets and no quotient-rank expansion occurs. Prove that the chain is periodic with bounded period and has an explicit row-column-preserving absorber state.

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

## Completion criterion

This branch is complete when RI1–RI5 prove I12 in a form that either forces quotient expansion or returns an explicit absorbable finite coset configuration.
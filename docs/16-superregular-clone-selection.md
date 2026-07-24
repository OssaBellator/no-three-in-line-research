# Superregular clone-selection and spread perfect matchings

This chapter develops the sparse-host endpoint suggested by the degree-constrained selection theorem. It separates three issues:

1. constructing spread distributions on perfect matchings of a dense superregular pair;
2. converting them into spread distributions on saturated two-layer configurations;
3. explaining why spread alone is not yet a local-lemma dependency theorem.

Throughout, a balanced bipartite graph has parts `X,Y` of size `N`.

## 1. Fixed-rank spread by six-cycle switching

A probability distribution on perfect matchings is `q`-spread up to rank `s` if

\[
\Pr(F\subseteq M)\le q^{|F|}
\]

for every matching `F` with `|F|\le s`.

### Theorem SR1 — PROVED

Fix `delta>0` and an integer `s`. There are `epsilon_0>0`, `C=C(delta,s)` and `N_0` such that the following holds.

Let `G` be an `(epsilon,delta)`-superregular balanced bipartite graph with `epsilon\le epsilon_0` and `N\ge N_0`. If `M` is a uniformly random perfect matching of `G`, then

\[
\boxed{
\Pr(F\subseteq M)\le \left(\frac{C}{N}\right)^{|F|}
}
\]

for every matching `F` with `|F|\le s`.

In particular, for the no-three-in-line application it is enough to take `s=3`.

### Proof

We first prove a one-edge marginal bound in every graph obtained after deleting at most `s` vertices from each side.

Let `H` be such a residual graph, with parts of size `m`. For sufficiently large `N`, inheritance of superregularity gives:

- density at least `delta/2`;
- minimum degree at least `(delta/2)m`;
- regularity parameter small compared with `delta`.

Fix an edge `xy` of `H`, with `x` on the left and `y` on the right. Let `Omega_xy` be the perfect matchings containing `xy`, and `Omega_0` the remaining perfect matchings.

Take `M in Omega_xy`. Define

\[
A=M^{-1}(N_H(x)\setminus\{y\}),
\qquad
B=M(N_H(y)\setminus\{x\}).
\]

Both sets have size at least `delta m/3` for large `m`. By regularity,

\[
e_H(A,B)\ge c_0 m^2
\]

for some `c_0=c_0(delta)>0`.

For an edge `ut in E_H(A,B)`, write

\[
v=M(u),\qquad s=M^{-1}(t).
\]

Then

\[
xv,\ ut,\ sy\in E(H).
\]

If `u\ne s`, replace the three matching edges

\[
xy,\ uv,\ st
\]

by

\[
xv,\ ut,\ sy.
\]

This is an alternating six-cycle switch and produces a perfect matching not containing `xy`. At most `m` choices of `ut` have `u=s`; hence every matching in `Omega_xy` has at least `c_1m^2` valid forward switches for some `c_1=c_1(delta)>0`.

Conversely, fix a perfect matching `M'` not containing `xy`. Its partners of `x` and `y` are fixed. To reverse a six-cycle switch, it is enough to choose the third matching edge `ut` of `M'`; there are at most `m` choices. Double counting switch pairs gives

\[
|\Omega_{xy}|c_1m^2\le |\Omega_0|m.
\]

Therefore

\[
\Pr(xy\in M)\le \frac{1}{c_1m}=O_delta(1/N).
\]

Now expose the edges of a fixed matching

\[
F=\{e_1,\ldots,e_r\},\qquad r\le s.
\]

Conditioning on `e_1,...,e_{j-1}` leaves a uniformly random perfect matching of the residual graph obtained by deleting their endpoints. The same one-edge marginal estimate applies at every step. Multiplying the conditional probabilities proves the theorem. `square`

A concrete but deliberately loose constant obtainable from this proof is

\[
C=O(delta^{-3}).
\]

## 2. The clone blow-up preserves superregularity

For every vertex of `G`, create two clones. Replace every original edge by a copy of `K_{2,2}` between its endpoint clones. Denote the resulting graph by `G^(2)`.

### Lemma SR2 — PROVED

If `G` is `epsilon`-regular with density `rho`, then `G^(2)` is `eta`-regular with the same density, where one may take

\[
\eta=(2\epsilon)^{1/3}.
\]

Relative minimum degrees are unchanged. Hence an `(epsilon,delta)`-superregular graph has an `(eta,delta)`-superregular two-clone blow-up.

### Proof

For arbitrary subsets `P,Q` of the original parts, regularity and the trivial small-set bound imply

\[
|e_G(P,Q)-\rho|P||Q||\le 2\epsilon N^2.
\]

Split a clone subset into its two clone-index projections. The discrepancy in the blow-up is a sum of four original discrepancies, and is therefore at most `8epsilon N^2`.

If the two clone subsets have size at least `2eta N`, their product is at least `4eta^2N^2`, so their density error is at most

\[
\frac{8\epsilon N^2}{4\eta^2N^2}
=
\frac{2\epsilon}{\eta^2}
=
\eta.
\]

Every clone has twice the original degree, while the opposite clone class has twice the original size. `square`

Combining SR1 and SR2 gives a self-contained rank-three spread distribution on clone perfect matchings.

## 3. All-rank spread in dense superregular pairs

The following theorem is available in the modern spread-matching literature.

### Theorem SR3 — PUBLISHED THEOREM

For every fixed positive lower density and minimum-degree parameter, every sufficiently regular dense superregular balanced bipartite graph admits a distribution `mu` on perfect matchings such that

\[
\boxed{
\Pr_{M\sim\mu}(F\subseteq M)
\le
\left(\frac{C}{N}\right)^{|F|}
}
\]

for every matching `F`, with `C` depending only on the fixed superregularity parameters.

This is the perfect-matching ingredient used in the spread blow-up lemma. In degree notation `d=Theta(N)`, the bound is equivalently `(K/d)^{|F|}`.

SR1 is not needed to invoke SR3, but it gives an elementary proof at the exact ranks two and three required by duplicate-cell and collinear-triple certificates.

## 4. Two edge-disjoint perfect matchings

Using two original perfect-matching layers is cleaner than selecting one clone perfect matching and then forbidding duplicate cells.

### Theorem SR4 — PROVED FROM SR3

Under the hypotheses of SR3, there exists a distribution on ordered pairs

\[
(M_1,M_2)
\]

of edge-disjoint perfect matchings of `G` such that, for any two prescribed matchings `F_1,F_2`,

\[
\boxed{
\Pr(F_1\subseteq M_1,\ F_2\subseteq M_2)
\le
q^{|F_1|+|F_2|},
\qquad
q=\frac{C}{N}.
}
\]

### Proof

Sample `M_1` from an SR3 distribution on `G`. Removing one perfect matching changes every degree by one and changes every large-pair density by `o(1)`, so `G-M_1` remains superregular with uniformly controlled parameters. Conditional on `M_1`, sample `M_2` from an SR3 distribution on `G-M_1`.

The conditional spread estimate for `M_2` is uniform in `M_1`. Therefore

\[
\Pr(F_1\subseteq M_1,F_2\subseteq M_2)
\le
q^{|F_1|}q^{|F_2|}.
\]

If the prescribed sets are incompatible or overlap, the probability is zero. `square`

The union

\[
S=M_1\cup M_2
\]

has exactly two distinct cells in every row and column.

For an unlabeled edge set `F`, summing over its at most `2^{|F|}` layer assignments gives

\[
\boxed{
\Pr(F\subseteq S)\le (2q)^{|F|}.
}
\]

## 5. Global conflict-mass endpoint

Let `C` be any family of forbidden edge sets in `G`.

### Corollary SR5 — PROVED

If

\[
\boxed{
\sum_{C\in\mathcal C}(2q)^{|C|}<1,
}
\]

then `G` contains two edge-disjoint perfect matchings whose union contains no member of `mathcal C`.

### Proof

For the random two-layer configuration from SR4, the probability that some forbidden set is selected is at most the displayed sum, by the union bound. `square`

For nonaxis collinear triples, if `T(G)` denotes their number, it is sufficient that

\[
\boxed{
8q^3T(G)<1.
}
\]

Since `q=C/N`, this is a genuine endpoint whenever

\[
T(G)<cN^3
\]

for a constant depending on the superregularity parameters.

## 6. What spread does not prove

A `q`-spread measure does not automatically provide a lopsided dependency graph for the forbidden events.

In the complete permutation space, canonical events that use disjoint row and column vertices have the Lu--Szekely negative-dependency property. Conditioning the permutation to lie in an arbitrary candidate graph can create positive correlations between disjoint compatible edge events. Even a four-cycle has two perfect matchings in which opposite edges occur together.

Therefore SR3 cannot simply be substituted into the local-load proof of the complete clone graph.

The rigorous consequences currently available are:

- rank-three cylinder bounds from SR1;
- all-rank spread from SR3;
- the global conflict-mass criterion SR5.

A local-load endpoint requires an additional conflict-avoiding matching theorem or a resampling oracle adapted to superregular perfect matchings.

## 7. The next exact targets

### Target A: superregular resampling oracle

Construct, for every bad partial matching `F`, a random alternating-cycle operation which:

1. removes `F` from the current perfect matching;
2. preserves a known stationary spread distribution;
3. changes only `O(|F|)` local matching edges;
4. creates dependencies only through overlapping clone vertices.

This would upgrade spread to a lopsided local lemma.

### Target B: conflict-free perfect-matching theorem

Apply or specialize modern conflict-free hypergraph matching and covering results to the two-uniform host `G`, with forbidden submatchings of sizes two and three, while using superregularity as the exact-covering reservoir.

### Target C: sparse algebraic spread

The dense theorem has `d=Theta(N)`. A bounded-hyperbola host may have `d=o(N)`. The desired sparse analogue is

\[
\Pr(F\subseteq M)\le\left(\frac{K}{d}\right)^{|F|}
\]

under a suitable expansion or pseudorandomness condition strong enough to rule out edges which are forced to occur together.

The six-cycle proof explains why density matters: a fixed matching edge has `Theta(N^2)` forward six-cycle switches but only `O(N)` reverse descriptions. In a sparse host, longer alternating cycles or rapid mixing of the matching-switch chain are needed to recover a ratio of order `d`.
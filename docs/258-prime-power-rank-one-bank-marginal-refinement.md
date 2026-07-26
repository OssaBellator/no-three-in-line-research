# Rank-one bank collateral has a doubly-stochastic secant-load bound

CMR1222--CMR1229 express fixed-target collateral as a corrected three-rank line
energy.  The universal permanent factor `kappa_n` is unnecessary for rank one.
Under any probability distribution on perfect matchings, the edge marginals are
doubly stochastic, and rank-one new collateral is a linear assignment cost after
old response edges are assigned weight zero.

Retain the degree-two response graph `G`, fixed opposite matching `O`, and old
rematched-layer matching `M`.  For an allowed response edge `a`, define

\[
\boxed{
w_S(a)
=
\mathbf 1_{a\notin M}
\sum_{L\ni a}\binom{o_L}{2}.
}
\]

This is the corrected rank-one owner count `V_1(a)` from CMR1228.  An edge already
in `M` supports only surviving old rank-one triples and therefore has weight zero.

## 1. Exact rank-one load of one response matching

### Theorem CMR1230 -- PROVED

For every response matching `R in PM(G)`, the number `N_1(R)` of new triples with
exactly one response-layer cell is

\[
\boxed{
N_1(R)=\sum_{a\in R}w_S(a).
}
\]

### Proof

A rank-one response triple has one response edge `a` and two fixed `O` cells on one
line through `a`.  If `a in M`, the same three physical cells already belonged to
the old state.  If `a notin M`, every such opposite-layer pair gives a genuinely
new triple.  Distinct response edges own disjoint rank-one triples by CMR1215. ∎

Thus corrected rank-one collateral is an ordinary edge-weighted matching cost.

## 2. Response-bank marginals are doubly stochastic

Let `mu` be any probability distribution on `PM(G)` and put

\[
p_{xy}=\Pr_{R\sim\mu}((x,y)\in R).
\]

### Theorem CMR1231 -- PROVED

The matrix `P=(p_xy)` is doubly stochastic and supported on `G`:

\[
\boxed{
\sum_y p_{xy}=1,
\qquad
\sum_x p_{xy}=1,
\qquad
p_{xy}=0\text{ off }G.
}
\]

### Proof

Every perfect matching uses exactly one edge at each source and target vertex.
Average those indicator identities under `mu`. ∎

No uniformity or permanent estimate is required.

## 3. Row, column and assignment bounds

Define

\[
R_1(G,S)
=
\min\left\{
\sum_x\max_{y:(x,y)\in G}w_S(x,y),
\sum_y\max_{x:(x,y)\in G}w_S(x,y)
\right\},
\]

and

\[
M_1(G,S)
=
\max_{R\in PM(G)}\sum_{a\in R}w_S(a).
\]

### Theorem CMR1232 -- PROVED

For every response distribution `mu`,

\[
\boxed{
\mathbb E_\mu N_1(R)
=
\sum_{a\in G}w_S(a)p_a
\le
M_1(G,S)
\le
R_1(G,S).
}
\]

### Proof

The first identity is CMR1230.  The expectation is a convex combination of
response-matching weights and is at most their maximum.  In each source row the
marginals sum to one, so its contribution is at most the largest row weight.  The
column argument is identical. ∎

The bound is computable without enumerating the response bank.

## 4. Refined complete-bank collateral expectation

Put

\[
\mathcal C_{\ge2}
=
\frac{V_2}{(n)_2}
+
\frac{V_3}{(n)_3},
\]

with the corrected `V_2,V_3` of CMR1223--CMR1224.

### Theorem CMR1233 -- PROVED

For the uniform complete response bank,

\[
\boxed{
\mathbb E N(R)
\le
R_1(G,S)
+
\kappa_n\mathcal C_{\ge2}.
}
\]

### Proof

Apply CMR1232 to corrected rank one and CMR1200 to every corrected rank-two and
rank-three prescription. ∎

This replaces `kappa_n V_1/n` by a doubly-stochastic assignment bound.

## 5. Refined restricted-host improvement criterion

Let `b` be the unavailable allowed-edge count and `m=Phi(S)`.

### Corollary CMR1234 -- PROVED

If

\[
\boxed{
R_1(G,S)
+
\kappa_n
\left[
\mathcal C_{\ge2}
+
\frac{(m+1)b}{n}
\right]
<
D_S(e),
}
\]

then a feasible response state has potential strictly below `m`.

### Proof

Use CMR1233 for new collateral, CMR1203 for destroyed target load, CMR1206 for
unavailable-edge use and CMR1207 for feasibility forcing. ∎

At a positive minimum, the reverse weak inequality is an explicit corrected
rank-one secant-load barrier.

## 6. Large rank-one cost produces one heavy genuinely new edge

### Theorem CMR1235 -- PROVED

\[
\boxed{
\max_{a\in G}w_S(a)
\ge
\frac{R_1(G,S)}{n}.
}
\]

If `R_1(G,S)>=nH`, some allowed edge `a notin M` satisfies `w_S(a)>=H`.

### Proof

Each of the two sums defining `R_1` has `n` nonnegative maxima, all bounded by the
global maximum.  A positive weight contains the indicator `a notin M`. ∎

Thus a large corrected rank-one barrier cannot be carried by unchanged old edges.

## 7. Heavy edge gives a loaded line or a secant star

Fix an allowed edge `a notin M` and an integer `s>=2`.

### Theorem CMR1236 -- PROVED

At least one of the following holds.

1. **Loaded opposite-layer line.** Some line through `a` contains at least `s+1`
   cells of `O`.
2. **Rooted secant star.** At least
   \[
   \boxed{
   \left\lceil
   \frac{w_S(a)}{\binom s2}
   \right\rceil
   }
   \]
   distinct lines through `a` contain at least two cells of `O`.

### Proof

For `a notin M`,

\[
w_S(a)=\sum_{L\ni a}\binom{o_L}{2}.
\]

If branch 1 fails, every summand is at most `binom(s,2)`, so the number of positive
summands has the displayed lower bound. ∎

The theorem claims distinct rooted secant lines.  Matching-compatible simultaneous
extraction remains the separate CMR494/CMR1054 mechanism.

## 8. Corrected rank-one marginal endpoint

### Corollary CMR1237 -- PROVED

For every fixed-target degree-two bank, one of the following is available.

1. The refined inequality CMR1234 gives a feasible strict improvement.
2. Corrected higher-rank line energy or unavailable inventory supplies the barrier.
3. One genuinely new response edge has large rooted secant load.
4. That load yields a loaded opposite-layer line or many distinct secant lines.
5. Complete bank blockage gives the minimal unit-wall descent.

Hence rank-one new collateral is attached directly to loaded-line, secant-star,
height and carry mechanisms without a permanent-loss constant.  The remaining
quantitative work is the corrected rank-two/rank-three expectation and aggregation
over target edges and forbidden extensions.

No all-`n` theorem is claimed.  Corrected matching weights, marginal identities,
assignment bounds and the line/star alternative are checked in
[`scripts/verify_prime_power_rank_one_bank_marginal.py`](../scripts/verify_prime_power_rank_one_bank_marginal.py).

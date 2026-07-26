# Rank-one bank collateral has a doubly-stochastic secant-load bound

CMR1222--CMR1229 express fixed-target collateral as a three-rank line energy.
The universal permanent factor `kappa_n` is unnecessary for rank one.  Under any
probability distribution on perfect matchings, the edge marginals are doubly
stochastic.  Rank-one collateral is therefore a linear assignment cost.

Retain the degree-two response graph `G` and fixed opposite matching `O`.  For an
allowed response edge `a`, define its rooted opposite-layer secant load

\[
w_O(a)
=
\sum_{L\ni a}\binom{o_L}{2}.
\]

This is the rank-one owner count `V_1(a)` from CMR1228.

## 1. Exact rank-one load of one response matching

### Theorem CMR1230 -- PROVED

For every response matching `R in PM(G)`, the number `N_1(R)` of new triples with
exactly one response-layer cell is

\[
\boxed{
N_1(R)=\sum_{a\in R}w_O(a).
}
\]

### Proof

A rank-one new triple has one residual response edge `a` and two fixed `O` cells on
one line through `a`.  There are exactly `w_O(a)` such pairs.  Distinct response
edges own disjoint rank-one triples by CMR1215. ∎

Thus rank-one collateral is an ordinary edge-weighted perfect-matching cost.

## 2. Response-bank marginals are doubly stochastic

Let `mu` be any probability distribution on `PM(G)` and put

\[
p_{xy}=\Pr_{R\sim\mu}((x,y)\in R).
\]

### Theorem CMR1231 -- PROVED

The matrix `P=(p_xy)` is doubly stochastic and is supported on `G`:

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
Average those exact indicator identities under `mu`. ∎

No uniformity or permanent estimate is required.

## 3. Row, column and assignment bounds

Define

\[
R_1(G,O)
=
\min\left\{
\sum_x\max_{y:(x,y)\in G}w_O(x,y),
\sum_y\max_{x:(x,y)\in G}w_O(x,y)
\right\}.
\]

Also define the maximum assignment weight

\[
M_1(G,O)
=
\max_{R\in PM(G)}\sum_{a\in R}w_O(a).
\]

### Theorem CMR1232 -- PROVED

For every response distribution `mu`,

\[
\boxed{
\mathbb E_\mu N_1(R)
=\sum_{a\in G}w_O(a)p_a
\le M_1(G,O)
\le R_1(G,O).
}
\]

### Proof

The first identity is CMR1230 and finite expectation interchange.  The expectation
is a convex combination of response-matching weights and is at most their maximum.
For the row bound, use `sum_y p_xy=1` in every row; the column bound is identical.
Take the smaller bound. ∎

The row/column estimate is computable without enumerating the response bank.

## 4. Refined complete-bank collateral expectation

Put

\[
\mathcal C_{\ge2}
=
\frac{V_2}{(n)_2}
+
\frac{V_3}{(n)_3}.
\]

### Theorem CMR1233 -- PROVED

For the uniform complete response bank,

\[
\boxed{
\mathbb E N(R)
\le
R_1(G,O)
+
\kappa_n\mathcal C_{\ge2}.
}
\]

### Proof

Apply CMR1232 to rank one and CMR1200 separately to every rank-two and rank-three
prescription. ∎

This replaces the earlier rank-one term `kappa_n V_1/n` by an exact marginal
assignment bound.

## 5. Refined restricted-host improvement criterion

Let `b` be the unavailable allowed-edge count in the current host and
`m=Phi(S)`.

### Corollary CMR1234 -- PROVED

If

\[
\boxed{
R_1(G,O)
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

At a positive minimum, the reverse weak inequality is an explicit rank-one
secant-load barrier.

## 6. Large rank-one cost produces one heavy entering edge

### Theorem CMR1235 -- PROVED

\[
\boxed{
\max_{a\in G}w_O(a)
\ge
\frac{R_1(G,O)}{n}.
}
\]

More generally, if `R_1(G,O)>=nH`, some allowed response edge satisfies
`w_O(a)>=H`.

### Proof

Each of the two sums defining `R_1` has `n` nonnegative maxima, all bounded above
by the global maximum edge weight. ∎

Thus failure of the refined improvement criterion cannot hide rank-one collateral
uniformly among all edges.

## 7. Heavy edge gives a loaded line or a secant star

Fix an allowed edge `a` and an integer `s>=2`.

### Theorem CMR1236 -- PROVED

At least one of the following holds.

1. **Loaded opposite-layer line.** Some line through `a` contains at least `s+1`
   cells of `O`.
2. **Rooted secant star.** At least
   \[
   \boxed{
   \left\lceil
   \frac{w_O(a)}{\binom s2}
   \right\rceil
   }
   \]
   distinct lines through `a` contain at least two cells of `O`.

### Proof

If branch 1 fails, every line through `a` contributes at most `binom(s,2)` to

\[
w_O(a)=\sum_{L\ni a}\binom{o_L}{2}.
\]

The number of positive summands is therefore at least the displayed ceiling. ∎

The pairs on distinct lines are physically disjoint outside the common entering
edge only after the usual matching-compatibility extraction; the theorem claims
line distinctness, not automatic simultaneous execution.

## 8. Rank-one marginal endpoint

### Corollary CMR1237 -- PROVED

For every fixed-target degree-two bank, one of the following is available.

1. The refined inequality CMR1234 gives a feasible strict improvement.
2. Higher-rank line energy or unavailable-edge inventory supplies the barrier.
3. One entering edge has large rooted secant load.
4. That load yields a loaded opposite-layer line or many distinct secant lines.
5. Complete bank blockage gives the minimal unit-wall descent.

Hence rank-one collateral is now attached directly to the existing loaded-line,
secant-star, height and carry mechanisms, with no permanent-loss constant.  The
remaining quantitative work is the rank-two/rank-three expectation and the
aggregation of the resulting line certificates over target edges and forbidden
extensions.

No all-`n` theorem is claimed.  Matching marginal identities, weighted assignment
bounds, refined expectation arithmetic and the line/star alternative are checked
in
[`scripts/verify_prime_power_rank_one_bank_marginal.py`](../scripts/verify_prime_power_rank_one_bank_marginal.py).

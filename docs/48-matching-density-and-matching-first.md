# Matching-density barrier and matching-first reservoirs

The sheared parabolic bank separates internal patch geometry from the existence
of a matching reservoir.  This chapter proves that independently sampled old
column and old row templates cannot have positive matching-admissible density
at square-root width.  It then gives a matching-first replacement that exists
for every saturated source configuration and has exact hypergeometric spread.

## 1. A universal matching-density bound

Let `S subseteq [m]^2` be saturated, so its row-column incidence graph has
exactly `2m` edges.  Let `C,Y subseteq [m]` be random coordinate sets of size
`2t`, and let `E` be the event that `S[C,Y]` contains a perfect matching between
`C` and `Y`.  Write `e_S(C,Y)` for the number of source points in `C x Y`.

### Proposition PP3bp -- PROVED

One always has

\[
 \Pr(E)
 \le
 \frac{\mathbb E e_S(C,Y)}{2t}.
\]

If `C` and `Y` are independent and

\[
 \max_x\Pr(x\in C)\le\alpha,
 \qquad
 \max_y\Pr(y\in Y)\le\beta,
\]

then

\[
 \boxed{
 \Pr(E)\le\frac{m\alpha\beta}{t}.
 }
\]

#### Proof

On `E`, the induced graph contains a matching of size `2t`, and therefore
`e_S(C,Y)>=2t`.  Markov's inequality applied in the reverse counting form gives

\[
 2t\Pr(E)
 \le
 \mathbb E e_S(C,Y).
\]

Under independence,

\[
 \mathbb E e_S(C,Y)
 =
 \sum_{(x,y)\in S}\Pr(x\in C)\Pr(y\in Y)
 \le
 2m\alpha\beta,
\]

because `|S|=2m`.  Divide by `2t`. ∎

The proof uses only the sparsity of a saturated source.  No geometric property
of `S` is needed.

## 2. Consequence for independent sheared parabolic boxes

Consider the old-column coordinate family

\[
 C_{A,R}
 =
 \{A+Lj^2+Rj+\varepsilon d:
   0\le j<t,\ \varepsilon\in\{0,1\}\},
\]

where `A` ranges over an interval of size `H_A` and `R` over an interval of
size `H_R`.  Define `Y_{B,S}` analogously with `H_B,H_S` choices.

For a fixed coordinate `x`, fixed `R`, row index `j`, and branch label
`epsilon`, the equation

\[
 x=A+Lj^2+Rj+\varepsilon d
\]

determines at most one `A`.  Hence at most `2t H_R` parameter pairs contain
`x`, and

\[
 \Pr(x\in C_{A,R})\le\frac{2t}{H_A}.
\]

The analogous row bound is `2t/H_B`.

### Corollary PP3bq -- PROVED

If the movement and refill parameter pairs are sampled independently from the
full boxes, the matching-admissible density `delta` satisfies

\[
 \boxed{
 \delta
 \le
 \frac{4mt}{H_AH_B}.
 }
\]

In particular, if `H_A,H_B>=c m` and `t=o(m)`, then

\[
 \delta=O(t/m).
\]

At square-root width `t=Theta(sqrt(m))`, one necessarily has
`delta=O(m^(-1/2))`.  Thus the positive-constant matching density hypothesised
in the simplest use of PP3as cannot arise from independent linear-size offset
boxes in an arbitrary saturated source.

#### Proof

Apply PP3bp with `alpha=2t/H_A` and `beta=2t/H_B`. ∎

This does not refute sheared parabolic patches.  It refutes the independence
assumption between their old-column and old-row templates.  A successful bank
must correlate the two templates through actual source edges.

## 3. Required edge correlation

### Proposition PP3br -- PROVED

Let `(C,Y)` be any distribution supported entirely on matching-admissible
pairs of `2t`-element coordinate sets.  Then

\[
 \sum_{(x,y)\in S}
 \Pr(x\in C,\ y\in Y)
 \ge
 2t.
\]

Consequently some source edge satisfies

\[
 \boxed{
 \Pr(x\in C,\ y\in Y)\ge\frac{t}{m}.
 }
\]

#### Proof

Every supported pair has `e_S(C,Y)>=2t`.  Taking expectations and expanding the
edge count gives the first inequality.  There are `2m` source edges, so one
summand is at least their average `t/m`. ∎

For coordinate marginals of order `t/m`, independent exposure would give joint
mass only of order `t^2/m^2`.  Matching admissibility therefore needs a positive
correlation factor of order `m/t`; at square-root width this factor is of order
`sqrt(m)`.

## 4. A matching-first spread bank

The row-column incidence graph of a saturated configuration is a disjoint union
of even cycles.  Alternating the edges on every cycle decomposes

\[
 S=P_0\mathbin{\dot\cup}P_1
\]

into two perfect matchings.

Fix `k=2t<=m`.  Choose `J` uniformly from `{0,1}` and then choose a uniform
`k`-edge subset `D` of `P_J`.

### Theorem PP3bs -- PROVED

The random set `D` is always a matching reservoir of size `2t`.  Moreover:

1. every source point has deletion probability

\[
 \Pr(e\in D)=\frac{t}{m};
\]

2. every old column and every old row is a reservoir coordinate with probability

\[
 \frac{2t}{m};
\]

3. for any `r` distinct old columns, and likewise for any `r` distinct old rows,

\[
 \Pr(\text{all are reservoir coordinates})
 =
 \frac{(2t)_r}{(m)_r};
\]

4. for `r` specified source points lying in one layer,

\[
 \Pr(\text{all lie in }D)
 =
 \frac12\frac{(2t)_r}{(m)_r},
\]

while the probability is zero if they do not all lie in one layer.

There are exactly

\[
 2\binom{m}{2t}
\]

layer-labelled reservoir states.

#### Proof

Every subset of a perfect matching is a matching, so `D` has distinct row and
column endpoints.  Conditional on the chosen layer, the `m` layer edges are
sampled uniformly without replacement.  The displayed formulas are the usual
hypergeometric cylinder probabilities.  Each source edge belongs to exactly one
layer, giving the factor `1/2` in the edge formulas.  Each old coordinate has
one incident edge in each layer, so its inclusion probability is `2t/m`
regardless of `J`. ∎

The theorem eliminates matching scarcity by choosing the source matching before
choosing the replacement geometry.  It also supplies exact all-rank spread for
the deletion reservoir.

## 5. Revised preparation interface

The unresolved task is no longer to obtain a positive-density matching event
from independent parabolic templates.  The viable order is:

1. sample or select a spread matching reservoir `D` using PP3bs or a refined
   cycle-correlated distribution;
2. construct an internally clean degree-restoring state adapted to the endpoint
   sets of `D`;
3. use PP2l or the multistate bad-box endpoint to select among the adapted
   geometry and protected trade states.

The hard geometric statement is therefore an **endpoint-adapted component
bank**: for many matching-first reservoirs, build sufficiently many clean
movement/refill realizations with small cell, pair, and cross-rung bad-box
probabilities.  Exact matching availability and deletion spread are now closed
for every saturated source.
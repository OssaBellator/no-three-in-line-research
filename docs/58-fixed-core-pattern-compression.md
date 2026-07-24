# Fixed-core cell and pair pattern compression

The global endpoint PP3ci counts geometric triples.  Against a fixed no-three
source set, many triples induce the same forbidden local state event: once a
candidate cell lies on one fixed secant, additional secants through that cell do
not create new restrictions.  The same applies to a candidate patch pair whose
line contains one or two fixed anchors.  This chapter counts distinct forbidden
cell and pair patterns instead of anchor multiplicity.

## 1. Pattern families

Let `E` be an `r`-edge matching block with one width-two new interval, and let
`Omega` be any locally no-three subfamily of its full 36-state bank.  Write

\[
 \delta=\frac{|\Omega|}{36\binom r4}.
\]

Let `F` be a fixed no-three-in-line point set disjoint from the patch support.
Define:

- `C_F`: the set of candidate patch cells lying on a secant through two points
  of `F`;
- `H_F`: the set of same-edge movement/refill candidate pairs whose line
  contains at least one point of `F`;
- `A_F`: the set of all other feasible candidate patch pairs whose line contains
  at least one point of `F`.

A candidate pair is counted once regardless of whether its line contains one or
two fixed anchors.  Feasibility means that the pair occurs together in at least
one full-bank state.

## 2. Exact compressed endpoint

### Theorem PP3cr -- PROVED

The proportion of all full-bank states that lie in `Omega` and create no triple
meeting `F` is at least

\[
 \boxed{
 \delta
 -\frac{2|C_F|}{r}
 -\frac{|H_F|}{r}
 -\frac{4|A_F|}{r(r-1)}.
 }
\]

In particular, a locally and fixed-core clean state exists whenever the boxed
quantity is positive.

#### Proof

A prescribed patch cell occurs in at most a `2/r` fraction of the complete
full-bank state space by PP3cg.  A prescribed same-edge movement/refill pair
occurs in at most a `1/r` fraction, and every other prescribed feasible pair
occurs in at most a `4/[r(r-1)]` fraction.

Remove from `Omega` every state selecting a pattern in `C_F`, `H_F`, or `A_F`.
The number removed is at most the corresponding number in the entire full bank,
so a union bound loses at most the three displayed fractions.  A surviving
state has no fixed-fixed-patch triple because it selects no cell of `C_F`, and
no fixed-patch-patch triple because it selects no pair of `H_F union A_F`.
It was already locally no-three by membership in `Omega`. ∎

The theorem is stronger than counting fixed anchors separately.  The no-three
property of `F` implies that one candidate-pair line contains at most two fixed
points, but PP3cr pays for the line only once.

### Corollary PP3cs -- PROVED

Suppose the local clean density satisfies `delta>=delta_0>0` and

\[
 |C_F|=o(r),
 \qquad
 |H_F|=o(r),
 \qquad
 |A_F|=o(r^2).
\]

Then a `delta_0-o(1)` fraction of the full-bank states are simultaneously local
and fixed-core clean.

For the universal PP3cm pools one may take

\[
 \delta_0=\frac1{36}-o(1).
\]

Thus fixed-core preparation is reduced to three distinct-pattern bounds rather
than the much larger triple counts in PP3ci.

## 3. Combining with directional cleaning

PP3cp can be used before PP3cr.  It may retain many deletion sets even when
`|C_F|` is linear, provided blocked cells do not make many edges unusable or
force too many edges to the same new line.  After restricting to those
cell-blocker-free degree states, only the pair-pattern families `H_F,A_F`
remain.

This gives two interchangeable fixed-core endpoints:

1. **pattern-sparse form:** apply PP3cr directly when `|C_F|=o(r)`;
2. **directionally flexible form:** apply PP3cp when blocked cells are numerous
   but have enough row/column alternatives, then solve the remaining pair-pattern
   problem inside the feasible state domain.

## 4. Universal coarse caps

There are four candidate cells per source edge and four same-edge cross pairs,
so

\[
 |C_F|\le4r,
 \qquad
 |H_F|\le4r.
\]

For each unordered pair of distinct controlling edges there are at most sixteen
candidate-cell pairs, hence

\[
 |A_F|\le16\binom r2=8r(r-1).
\]

These worst-case bounds do not satisfy PP3cr, but they show that the fixed-core
cost depends only on the *local support size*, not on `|F|` or on the number of
secants and anchors passing through one forbidden pattern.  Any geometric
argument saving a fixed positive fraction of the cell and pair patterns can be
inserted directly into the boxed inequality.

## 5. Remaining target after PP3cm

For almost every random matching pool, PP3cm supplies local density
`1/36-o(1)` in the full bank.  It is therefore sufficient to prove, after
choosing the pool interval or applying protected trades, that

\[
 \frac{2|C_F|}{r}
 +\frac{|H_F|}{r}
 +\frac{4|A_F|}{r(r-1)}
 <
 \frac1{36}-o(1),
\]

or to obtain the analogous inequality inside the larger directional domain of
PP3cp.  Cross-block patterns are then handled by PP3ci or PP3bl.

The remaining fixed-core bottleneck is now an explicit support-pattern density
problem.  Secant-star multiplicity by itself is no longer charged.
# Exact high-slice cleaning inside a line-clean paid pair cylinder

CMR330 fixes a paid pair and completes by avoiding one full residual matching.
The matching-space local lemma may be applied directly to the residual complete
bipartite graph.  High-height candidate triples then have only residual ranks
two and three: rank two means one paid cell and two residual cells, while rank
three is disjoint from the paid pair.  The rank-two vertex load is at most two,
and the mod-six rank-three estimate from CMR280 is unchanged after deleting two
source and two target vertices.

Fix a paid pair `P_L` from CMR330.  Put

\[
n=t-2.
\]

Let `F_L` be the residual forbidden matching which contains every remaining
cell of the paid line.  Additional protected real lines contribute their
available residual cells as singleton bad events.

## 1. Residual matching-space local lemma

### Theorem CMR335 — PROVED

In the residual `K_{n,n}`, let

- `S(v)` be the number of forbidden singleton cells incident with a residual
  matching vertex `v`;
- `T_2(v)` be the number of forbidden compatible rank-two prescriptions
  incident with `v`;
- `T_3(v)` be the number of forbidden compatible rank-three prescriptions
  incident with `v`.

If every residual matching vertex satisfies

\[
\boxed{
\frac{S(v)}{n}
+
\frac{T_2(v)}{(n)_2}
+
\frac{T_3(v)}{(n)_3}
\le
\frac{1}{24},
}
\]

then there is a residual perfect matching avoiding every forbidden event.
Together with `P_L`, it is a saturated parent state which omits the old target
endpoint.

### Proof

Choose a uniformly random perfect matching of the residual complete bipartite
graph.  A singleton event has probability `1/n`; compatible rank-two and
rank-three events have probabilities `1/(n)_2` and `1/(n)_3`.  The
Lu--Szekely matching-space negative-dependency graph and the proof of CMR249
apply verbatim.  The displayed per-vertex load is the same `1/24` sufficient
condition. ∎

## 2. Exact high-slice residual loads

Put

\[
H=\left\lceil\frac{21t}{50}\right\rceil.
\]

### Theorem CMR336 — PROVED

Suppose the forbidden rank-two and rank-three events are candidate-only
collinear triples of primitive height at least `H`, classified by whether they
share one or zero paid-pair cells.  Then every residual vertex satisfies

\[
\boxed{T_2(v)\le2}
\]

and

\[
\boxed{
T_3(v)
\le
B(t),
}
\]

where

\[
B(t)
=
\frac{5518}{140625}t^3
+
\frac{30331}{11250}t^2
+
\frac{59}{50}t
-
\frac{14}{9}.
\]

### Proof

Fix a residual cell `w` and one of the two paid cells.  They determine one real
line.  A line of primitive height at least `H>(t-1)/3` contains at most three
board cells, so after the paid cell and `w` are fixed there is at most one
choice for the other residual cell.  The two paid cells therefore contribute
at most two rank-two events through `w`.

Deleting two source and two target coordinates can only decrease the number of
rank-three board conflicts through `w`.  The explicit CMR280 bound for the
full board is `B(t)`. ∎

The matching `F_L` contributes exactly one forbidden singleton at every
residual vertex.  Each additional protected nonaxis real line contributes at
most one further singleton at a residual source or target vertex.

## 3. Exact line-clean high-slice completion

### Theorem CMR337 — PROVED

For every odd

\[
\boxed{t\ge1677,}
\]

and every paid ratio line `L`, there is a target-specific parent permutation
which

1. contains `P_L`;
2. avoids every other cell of `L`;
3. contains no candidate-only collinear triple of primitive height at least
   `ceil(21t/50)`.

### Proof

Use CMR335 with

\[
S(v)=1,
\qquad
T_2(v)\le2,
\qquad
T_3(v)\le B(t).
\]

The remaining margin is

\[
\frac{1}{24}
-
\left(
\frac{1}{t-2}
+
\frac{2}{(t-2)(t-3)}
+
\frac{B(t)}{(t-2)(t-3)(t-4)}
\right)
\]

and equals

\[
\frac{
2731t^3-4579975t^2+5516250t-3875000
}{
1125000(t-2)(t-3)(t-4)
}.
\]

The numerator is positive at `t=1677`.  Its first and second derivatives are
positive there, and the second derivative remains increasing.  It is therefore
positive for every later `t`.  CMR335 supplies the completion. ∎

## 4. Protected-line reserve

### Theorem CMR338 — PROVED

For every odd

\[
\boxed{t\ge2847,}
\]

put

\[
R_4(t)=\left\lfloor\frac{t}{1000}\right\rfloor.
\]

For any family of at most `R_4(t)` protected nonaxis real lines, there is a
completion satisfying CMR337 which additionally avoids every available
residual cell on all protected lines.

### Proof

The forbidden singleton load is at most

\[
\frac{R_4(t)+1}{t-2}
\le
\frac{t/1000+1}{t-2}.
\]

Substitute this together with the CMR336 rank-two and rank-three bounds into
CMR335.  After clearing positive denominators, a sufficient numerator is

\[
803t^3-2286050t^2+2751375t-1937500.
\]

It is positive at `t=2847`, and its first and second derivatives are positive
there and remain increasing. ∎

### Corollary CMR339 — PROVED

Fix one paid ratio line in a globally minimal positive-potential inherited
parent block of odd size `t>=2847`.  At least one of the following holds.

1. A line-clean completion improves the global potential.
2. A required replacement certificate is anchored and opens the existing
   alternating continuation.
3. There are `R_4(t)+1` distinct candidate-only replacement-line signatures,
   all of primitive height below `ceil(21t/50)`, and one line-clean completion
   avoids the first `R_4(t)` together with the entire higher slice.

### Proof

Iterate CMR338 with the paid pair and `F_L` held fixed.  Every completion omits
the old target and avoids the paid line.  If it does not improve, global
minimality requires a replacement certificate.  An anchored certificate gives
the second outcome.  A candidate-only certificate lies below the cleaned
height threshold and on a new line because every available cell of each
previous protected line is absent. ∎

## 5. Revised mixed-ratio endpoint

The paid pair cylinder now has an exact no-return reserve just like the original
target-specific parent bank, but with the paid ratio line removed and no
rank-two-on-that-line collateral.  A frozen mixed fan therefore forces a linear
population of distinct **low-height** replacement lines inside one line-clean
cylinder, unless it improves or opens an anchored continuation.

The remaining mixed-fan task is to charge those lower-height lines to the
opposite-deviation signature of CMR319, the p-adic carry cells of CMR303, or the
closure-envelope expansion ledger.

No all-`n` theorem is claimed here.  Rank-two loads, polynomial margins,
protected-line arithmetic, and exact small line-clean completions are checked
in
[`scripts/verify_prime_power_line_clean_high_slice.py`](../scripts/verify_prime_power_line_clean_high_slice.py).

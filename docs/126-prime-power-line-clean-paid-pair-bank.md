# A line-clean paid pair bank removes the guaranteed ratio triple

CMR325 fixes a complete rank-three ratio certificate.  That gives an exact paid
bank, but the destroyed old target and the guaranteed new triple cancel at unit
scale.  A stronger construction fixes only two cells on the ratio line and
forbids every other cell of that line during completion.  The resulting bank
still destroys the selected old target, but its replacement collateral has no
rank-two-on-the-paid-line term.

Work in a nonroot inherited parent block of size `t`.  Fix the old target
endpoint

\[
z_1=(x_1,y_1)
\]

and a ratio-line family `\mathcal R` from CMR309.  For every `L in \mathcal R`,
let

\[
f_L=(x_1,a_L)
\]

be its unique source-fan cell.  Choose one other available cell `g_L` on `L`
and put

\[
P_L=\{f_L,g_L\}.
\]

The pair is compatible because `L` is nonaxis.  Such a second cell exists
because every line in `\mathcal R` is a candidate-only certificate line.

Delete the two source and two target vertices used by `P_L`.  Put

\[
n=t-2.
\]

The other available cells of `L` form a partial matching in the residual
`K_{n,n}`.  Extend that partial matching arbitrarily to a perfect matching
`F_L`, and let `\mathcal D_L` be the perfect matchings of the residual graph
which avoid every edge of `F_L`.

## 1. Equal-size line-clean cylinders

### Theorem CMR330 — PROVED

For every `L`,

\[
\boxed{|\mathcal D_L|=D_n,}
\]

where `D_n` is the derangement number.  Every completed parent state obtained
from `P_L` and a member of `\mathcal D_L`

1. omits `z_1`;
2. contains `P_L`;
3. contains no other cell of `L`.

Consequently it contains no candidate-only triple using both cells of `P_L`.

### Proof

After deleting the vertices of `P_L`, the target-specific forbidden edge
`z_1` has disappeared because its source `x_1` is already used.  Relabel the
residual source and target vertices so that `F_L` is the identity matching.
The matchings avoiding `F_L` are exactly the `D_n` derangements.

Every remaining cell of `L` belongs to the partial matching extended by `F_L`,
so it is avoided.  Any third point collinear with the two cells of `P_L` lies on
the same real line `L`; hence no such triple occurs. ∎

### Corollary CMR331 — PROVED

For distinct ratio lines `L,L'`, the full completion cylinders are disjoint.
Thus the line-clean pair bank

\[
\mathcal P(\mathcal R)
=
\bigcup_{L\in\mathcal R}
\{P_L\cup\delta:\delta\in\mathcal D_L\}
\]

has exact size

\[
\boxed{|\mathcal P(\mathcal R)|=|\mathcal R|D_n.}
\]

### Proof

The paid pairs contain distinct cells in the same source column `x_1`.  No
perfect matching contains two of them.  CMR330 gives the equal cylinder sizes.
∎

## 2. Conditional derangement spread

### Theorem CMR332 — PROVED

Assume `n>=5`.  Conditional on one line `L`, every allowed residual cell has
probability

\[
\boxed{\frac{1}{n-1}}
\]

under the uniform law on `\mathcal D_L`.  Every compatible allowed residual
rank-`r` prescription, for `r=2,3`, has probability at most

\[
\boxed{
\frac{30}{11(n)_r}.
}
\]

### Proof

After relabelling `F_L` as the identity, this is exactly the uniform
derangement law of CMR176. ∎

## 3. Rank-zero/rank-one collateral identity

For fixed `L`, let

- `V_0(L)` be the number of compatible candidate-only collinear triples
  disjoint from `P_L` and allowed by the residual derangement host;
- `V_1(L)` be the number of such triples sharing exactly one cell with `P_L`.

No allowed triple shares both cells with `P_L`, by CMR330.

### Theorem CMR333 — PROVED

For `t>=7`, conditional on `L`, the expected number of candidate-only
collinear triples in a line-clean completion is at most

\[
\boxed{
\frac{30}{11}
\left(
\frac{V_0(L)}{(n)_3}
+
\frac{V_1(L)}{(n)_2}
\right).
}
\]

### Proof

A triple counted by `V_0(L)` requires three residual derangement edges; a triple
counted by `V_1(L)` requires two.  Apply CMR332 and sum.  CMR330 eliminates the
rank-two class. ∎

## 4. Frozen-bank concentration

### Corollary CMR334 — PROVED

Assume the current state is a globally minimal positive-potential saturated
state and `t>=7`.  For the line-clean bank, at least one of the following holds.

1. Some completion creates an anchored triple involving a fixed outside point,
   yielding the existing anchored alternating continuation.
2. Some completion strictly lowers the global potential.
3. The ratio-line family satisfies
   \[
   \boxed{
   \frac{1}{|\mathcal R|}
   \sum_{L\in\mathcal R}
   \left(
   \frac{V_0(L)}{(n)_3}
   +
   \frac{V_1(L)}{(n)_2}
   \right)
   \ge
   \frac{11}{30}.
   }
   \]

### Proof

Every bank state omits `z_1`, so it destroys the selected old target triple.  If
one state improves, the second alternative holds.  If a required replacement
certificate uses an outside point, the first alternative holds.

Otherwise every globally nonimproving bank state must create at least one
candidate-only triple touching the replacement block.  Its bank-average count
is therefore at least one.  Average CMR333 over the equal-size cylinders and
rearrange. ∎

## 5. Revised mixed-fan endpoint

The mixed-fan obstruction no longer carries an unavoidable rank-two term.  A
frozen line-clean bank forces a constant normalized mass entirely in

- rank-zero residual candidate triples; or
- rank-one secant shadows through one paid-pair endpoint.

These are precisely the modular-syndrome and quotient-incidence quantities
already controlled in the prefix and joint-parent calculations.  The next
strict theorem is to charge the average in CMR334 to low-height carry cells or
to batch several destroyed old targets against one residual certificate.

No all-`n` theorem is claimed here.  Equal cylinder sizes, line avoidance,
derangement atoms, and the exact absence of rank-two collateral are checked in
[`scripts/verify_prime_power_line_clean_pair.py`](../scripts/verify_prime_power_line_clean_pair.py).

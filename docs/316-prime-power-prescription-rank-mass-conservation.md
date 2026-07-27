# Prescription rank mass is exactly conserved by every response law

The normalized side-four and side-five censuses give pointwise probability caps
for rank-one, rank-two and rank-three prescriptions.  A second exact constraint
is independent of the host geometry: every perfect matching contains exactly
`binom(d,r)` rank-`r` submatchings.  Therefore the total probability mass of all
rank-`r` prescriptions is exactly `binom(d,r)` under every response law.

Combining the pointwise caps with this conserved mass gives sharper class
capacities for critical selectors, fixed-interface tables and line-clean rows.

Let `G` be a bipartite response host of side `d` with a nonempty finite family of
perfect matchings.  Let `nu` be any probability law on those matchings.  For a
rank-`r` partial matching `P`, put

\[
p(P)=\Pr_{Q\sim\nu}(P\subseteq Q).
\]

## 1. Exact rank-mass identity

Let `P_r(G)` be the set of all rank-`r` partial matchings contained in at least
one perfect matching of `G`.

### Theorem CMR1702 -- PROVED

For every `0<=r<=d`,

\[
\boxed{
\sum_{P\in\mathcal P_r(G)}p(P)=\binom dr.
}
\]

### Proof

For one sampled perfect matching `Q`, exactly `binom(d,r)` subsets of its `d`
edges have rank `r`.  Hence

\[
\sum_{P\in\mathcal P_r(G)}\mathbf 1_{P\subseteq Q}=\binom dr.
\]

Take expectation under `nu` and interchange the finite sum and expectation. ∎

The identity does not require the uniform response law.

## 2. Corrected candidate-family bound

Let `C_r subseteq P_r(G)` be any corrected family of genuinely new rank-`r`
prescriptions.

### Theorem CMR1703 -- PROVED

\[
\boxed{
\sum_{P\in\mathcal C_r}p(P)\le\binom dr.
}
\]

Equality is possible only when every positive-probability rank-`r` prescription
belongs to the corrected family.

### Proof

All probabilities are nonnegative and `C_r` is a subset of the exact family in
CMR1702. ∎

Thus no corrected rank class can carry more than the universal rank mass.

## 3. Exact integer numerator identity

Assume the response law is rational with common denominator `Z>0`.  Write

\[
p(P)=\frac{n(P)}Z,
\qquad n(P)\in\mathbb Z_{\ge0}.
\]

### Theorem CMR1704 -- PROVED

For every rank `r`,

\[
\boxed{
\sum_{P\in\mathcal P_r(G)}n(P)=Z\binom dr.
}
\]

Every corrected family therefore has integer numerator sum at most

\[
\boxed{Z\binom dr.}
\]

### Proof

Multiply CMR1702 and CMR1703 by `Z`. ∎

For the uniform law one may take `Z=|PM(G)|`.

## 4. Forced prescriptions consume conserved mass

Let `F_r` be the number of rank-`r` prescriptions forced in every response
matching.  Each forced prescription has probability one.

### Theorem CMR1705 -- PROVED

The total probability mass of all nonforced rank-`r` prescriptions is exactly

\[
\boxed{
\binom dr-F_r.
}
\]

In particular,

\[
0\le F_r\le\binom dr.
\]

### Proof

Split the exact identity of CMR1702 into forced and nonforced prescriptions.
Every forced term equals one. ∎

Forced contractions therefore reduce the remaining stochastic mass by one full
unit each.

## 5. Pointwise caps combine with total mass

Let one nonforced corrected class contain `N_r` rank-`r` prescriptions, each
having probability at most `q_r`.

### Theorem CMR1706 -- PROVED

Its expectation satisfies the simultaneous bound

\[
\boxed{
A_r
\le
\min\left\{N_rq_r,\binom dr-F_r\right\}.
}
\]

### Proof

The first bound is the sum of the pointwise caps.  The second is CMR1705 applied
to a subset of the nonforced prescriptions. ∎

The two constraints may dominate in different host classes.

## 6. Side-four and side-five conserved capacities

Use the exact nonforced caps from CMR1690.

### Theorem CMR1707 -- PROVED

For corrected nonforced counts `N_1,N_2,N_3`, one has:

### Side four

\[
\boxed{
A_{\rm class}
\le
\min\left\{\frac34N_1,4-F_1\right\}
+
\min\left\{\frac23N_2,6-F_2\right\}
+
\min\left\{\frac12N_3,4-F_3\right\}.
}
\]

### Side five

Since CMR1667 and CMR1689 find no forced positive rank-at-most-three
prescriptions,

\[
\boxed{
A_{\rm class}
\le
\min\left\{\frac23N_1,5\right\}
+
\min\left\{\frac25N_2,10\right\}
+
\min\left\{\frac14N_3,10\right\}.
}
\]

### Proof

Apply CMR1706 rank by rank and add the three corrected rank contributions. ∎

These improve the purely pointwise capacities whenever a class contains many
prescriptions.

## 7. Exact integer capacity form

Let the rational response law have common denominator `Z`.  Suppose rank-`r`
pointwise caps have numerator bounds

\[
n(P)\le U_r.
\]

### Theorem CMR1708 -- PROVED

A corrected nonforced class has exact integer numerator capacity

\[
\boxed{
C_{\rm mass}
=
\sum_{r=1}^3
\min\left\{N_rU_r,\ Z\left(\binom dr-F_r\right)\right\}.
}
\]

For the side-four and side-five uniform caps, one may use

\[
U_r=\lfloor Zq_r\rfloor.
\]

The exact class numerator is at most `C_mass`.

### Proof

Use the integer pointwise bound and the integer conserved-mass bound from
CMR1704--CMR1705, take their minimum at each rank, and sum. ∎

This capacity can replace the larger pointwise-only capacity in CMR1649 and
CMR1692.

## 8. Rank-mass endpoint

### Corollary CMR1709 -- PROVED

Every rational matching response row now has two simultaneous prescription
capacity laws.

1. Pointwise rook or census probability caps control sparse classes.
2. Exact rank-mass conservation controls large classes.
3. Forced contractions subtract one full unit of stochastic mass each.
4. The rankwise minimum gives an exact integer numerator capacity.
5. These capacities feed the selector gap compiler, line-profile compiler and
   normalized thin-table rows without adding historical episodes.

The remaining task is to combine these matching-level capacities with genuine
geometric offspring classification and destroyed-credit bounds.  No all-`n`
theorem is claimed.

Exact rank-mass identities, rational numerator conservation, forced-mass removal
and side-four/five combined capacities are checked in
[`scripts/verify_prime_power_prescription_rank_mass_conservation.py`](../scripts/verify_prime_power_prescription_rank_mass_conservation.py).

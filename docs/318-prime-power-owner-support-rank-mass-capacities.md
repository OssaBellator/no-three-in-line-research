# Owner-support matching numbers bound recurrent credit mass

CMR1702--CMR1709 conserve total prescription mass by rank. The current
return, selector, line-clean and reused-support rows also retain an absolute
last-entering owner edge. This extra label yields a sharper local law: a response
matching can contain only a matching-sized set of possible owners, and each
selected owner belongs to only `C(d-1,r-1)` rank-`r` submatchings.

The result converts source-row, target-column, token, prefix, carry and interface
support covers directly into expectation or integer numerator capacities. It is
independent of the response denominator and does not assume independence between
owner classes.

Let `G` be a bipartite response host of side `d` with a nonempty perfect-matching
family and let `nu` be any response law. Let `A` be any set of allowed owner
edges and let

\[
\mu(A)
\]

be the maximum matching size of the bipartite graph with edge set `A`.

For each corrected prescription `P`, assume its canonical owner `o(P)` is one of
the edges of `P`. This is the absolute last-entering ownership convention used
throughout the recurrent quotient.

## 1. Response-wise owned-submatching bound

### Theorem CMR1718 -- PROVED

For every perfect matching `Q`, every rank `r>=1`, and every corrected family
`C_r(A)` of rank-`r` prescriptions with owner in `A`,

\[
\boxed{
|\{P\in C_r(A):P\subseteq Q\}|
\le
|Q\cap A|\,C(d-1,r-1).
}
\]

### Proof

Every realized prescription has one owner edge in `Q cap A`. For a fixed edge
of the `d`-edge matching `Q`, exactly `C(d-1,r-1)` rank-`r` submatchings of `Q`
contain that edge. The corrected owned family is a subset of these possibilities.
Sum over the owner edges in `Q cap A`. ∎

The inequality remains valid if not every possible submatching is a genuine
credit.

## 2. Owner-support expectation capacity

### Theorem CMR1719 -- PROVED

For every rank `r>=1`,

\[
\boxed{
\sum_{P\in C_r(A)}\Pr(P\subseteq Q)
\le
\mu(A)\,C(d-1,r-1).
}
\]

### Proof

Take expectation in CMR1718. Since `Q cap A` is a matching in `A`,

\[
|Q\cap A|\le\mu(A)
\]

for every response. ∎

This is an owner-local analogue of the global rank-mass identity.

## 3. Source-row and target-column cover form

Suppose `A` is covered by `s` source vertices and `t` target vertices.

### Theorem CMR1720 -- PROVED

\[
\boxed{
\mu(A)\le s+t.
}
\]

Consequently

\[
\boxed{
\sum_{P\in C_r(A)}\Pr(P\subseteq Q)
\le
(s+t)C(d-1,r-1).
}
\]

### Proof

The selected `s+t` vertices form a vertex cover of `A`. In a bipartite graph,
the matching number is at most every vertex-cover size. Apply CMR1719. ∎

Shared rows or columns among several geometric classes are counted only once
when their owner supports are unioned before applying the theorem.

## 4. Fixed-owner conditional mass

Fix one allowed owner edge `a` and put

\[
p(a)=\Pr(a\in Q).
\]

### Theorem CMR1721 -- PROVED

If `p(a)>0`, then for every corrected rank-`r` family owned by `a`,

\[
\boxed{
\sum_{P:o(P)=a}\Pr(P\subseteq Q\mid a\in Q)
\le
C(d-1,r-1).
}
\]

Equivalently, without conditioning,

\[
\boxed{
\sum_{P:o(P)=a}\Pr(P\subseteq Q)
\le
p(a)C(d-1,r-1).
}
\]

### Proof

Conditional on `a in Q`, the matching `Q` has exactly `C(d-1,r-1)` rank-`r`
submatchings containing `a`. The owned corrected family is a subset. Multiply by
`p(a)` for the unconditional form. ∎

This gives a universal edgewise score cap before any finer height or token
restriction is used.

## 5. Weighted owner-support capacity

Give every corrected rank-`r` credit a nonnegative weight at most `lambda_r`.
Let `W_A(Q)` be the total realized weight of credits whose owners lie in `A`.

### Theorem CMR1722 -- PROVED

\[
\boxed{
\mathbb E W_A(Q)
\le
\mu(A)
\sum_{r=1}^3\lambda_r C(d-1,r-1).
}
\]

If rank `r` has an additional proved multiplicity cap `m_r` per response
prescription, replace `lambda_r` by `m_r lambda_r`.

### Proof

Apply CMR1719 rank by rank, multiply by the rank weight and add. A multiplicity
cap repeats the contribution of one prescription at most `m_r` times. ∎

Thus weighted potential rows and selector restoration weights use the same
owner-support currency.

## 6. Return-selector edge-score specialization

For one owner edge `a`, partition its corrected rank-`r` credits into return and
selector families. Suppose their conditional realized counts are bounded by
`R_r(a)` and `S_r(a)`, with

\[
R_r(a)+S_r(a)\le C(d-1,r-1).
\]

### Theorem CMR1723 -- PROVED

For selector restoration weight `T>=0`, the combined edge score satisfies

\[
\boxed{
h_T(a)
\le
\sum_{r=1}^3\bigl(R_r(a)+T S_r(a)\bigr).
}
\]

In the absence of a finer return/selector split, the universal cap is

\[
\boxed{
h_T(a)
\le
\max\{1,T\}
\left(1+(d-1)+C(d-1,2)\right).
}
\]

The parenthesized quantity equals

\[
1+d(d-1)/2.
\]

### Proof

Condition on `a in Q` and add the weighted conditional counts. The coarse form
uses CMR1721 and assigns every owned prescription the larger of the two weights.
∎

Finer owner, height, token, prefix and carry restrictions can only lower the
`R_r,S_r` values. These caps may be inserted as the class scores `H_s` in
CMR1670--CMR1677.

## 7. Exact integer numerator form

Assume the response law has common denominator `Z>0`.

### Theorem CMR1724 -- PROVED

For rank-dependent integer weights `L_r>=0`, the weighted numerator of all
corrected credits owned in `A` is at most

\[
\boxed{
Z\mu(A)
\sum_{r=1}^3 L_r C(d-1,r-1).
}
\]

If `A` has a source/target cover of size `k`, one may replace `mu(A)` by `k`.

### Proof

Apply CMR1722 with `lambda_r=L_r` and multiply the expectation inequality by
`Z`. CMR1720 gives the cover specialization. ∎

The resulting capacity is directly compatible with the selector denominator-gap
compiler and the final strict integer quotient.

## 8. Owner-support endpoint

### Corollary CMR1725 -- PROVED

Every recurrent class whose canonical owners lie in a known edge support now has
an exact finite capacity compiler.

1. Compute or bound the matching number of the owner support.
2. Alternatively exhibit a small source-row/target-column cover.
3. Multiply by the exact rank-submatching factors `C(d-1,r-1)`.
4. Insert rank weights, selector restoration weight or multiplicity caps.
5. Use the result as a return score cap, selector numerator capacity, line-clean
   expectation bound or reused-support row capacity.
6. Clear the response denominator for a strict integer certificate.

This does not by itself prove all owner supports are small. It reduces the
remaining geometry to matching-number or vertex-cover estimates on exact owner
edge classes, preserving every provenance label. No all-`n` theorem is claimed.

Response-wise owner counts, matching-number capacities, conditional edge scores,
weighted forms and integer numerator bounds are checked in
[`scripts/verify_prime_power_owner_support_rank_mass_capacities.py`](../scripts/verify_prime_power_owner_support_rank_mass_capacities.py).

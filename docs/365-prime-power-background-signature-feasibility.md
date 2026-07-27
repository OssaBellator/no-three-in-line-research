# Necessary feasibility inequalities for survivor-background signatures

CMR2046--CMR2077 give exact scalar signatures and residual point-pair counts for every
populated survivor background. This chapter adds finite inequalities that every
geometrically realizable signature must satisfy before selector or labelled-row work.
They are necessary conditions only.

Let `n=|B|`, let `h_B(L)=|B cap L|` on the canonical response-line universe, and let
`p_B(q)` count unordered background pairs collinear with the response-grid point `q`.

## Theorem CMR2094 -- PROVED

Every tracked line satisfies `0 <= h_B(L) <= n`, and distinct tracked lines support
disjoint unordered background-pair sets. Hence

\[
\boxed{\sum_L \binom{h_B(L)}2\le \binom n2.}
\]

Indeed, two distinct points determine one affine line, so one background pair cannot be
counted by two different tracked lines.

## Theorem CMR2095 -- PROVED

For every parallel class `P` of tracked lines,

\[
\boxed{\sum_{L\in P}h_B(L)\le n.}
\]

A background point lies on at most one line in a fixed parallel class. The exact side-
four/five line universes contain respectively 9 and 18 nontrivial parallel classes.

## Theorem CMR2096 -- PROVED

Let `L_1,...,L_k` be distinct tracked lines concurrent at one rational point. Then

\[
\boxed{\sum_{i=1}^k h_B(L_i)\le n+k-1.}
\]

Every background point other than the common intersection lies on at most one line of
the pencil. If the intersection itself belongs to `B`, it contributes `k` incidences
instead of one, producing the additive `k-1` term.

There are exactly 129 side-four and 1,637 side-five intersection pencils in the
canonical line universes.

## Theorem CMR2097 -- PROVED

The maximum number of tracked response lines through one arbitrary affine point is

\[
\boxed{\mu_4=7,\qquad \mu_5=11.}
\]

Consequently every genuine background satisfies the global incidence inequality

\[
\boxed{\sum_L h_B(L)\le \mu_s n.}
\]

The constants are obtained by exact rational intersection grouping of the finite line
universes; a point not equal to a listed intersection lies on at most one tracked line.

## Theorem CMR2098 -- PROVED

For every response-grid point `q`,

\[
\boxed{
 p_B(q)-\sum_{L\ni q}\binom{h_B(L)}2\ge0.
}
\]

This is the residual nonnegativity theorem of CMR2071, now included in one common
feasibility certificate with the global line constraints.

## Theorem CMR2099 -- PROVED

The line bounds, tracked-pair budget, parallel-class budgets, pencil budgets, global
incidence budget and all response-grid residuals are integer inequalities reconstructed
from the supplied background. A certificate is accepted only when every stored slack
equals the independently recomputed slack and is nonnegative.

These conditions reject impossible signature data early, but they do not characterize
the complete integer realization set of survivor backgrounds.

## Theorem CMR2100 -- PROVED

A deterministic 500-system suite checks both sides and contains 1,837 background
points. It reconstructs 88 tracked-line background pairs and residual point-pair mass
643 while validating every parallel, pencil, concurrency and local residual inequality.
All 500 systems have at least one tight constraint, as expected from empty lines and
zero occupancies.

These totals are regression facts for the fixed synthetic suite, not statistics for the
unpopulated genuine fibres.

## Corollary CMR2101 -- PROVED

`scripts/check_prime_power_background_signature_feasibility.py` builds the canonical
constraint basis, validates arbitrary feasibility certificates, and rejects twelve
independent corruptions. The fixed basis digest is

\[
\texttt{ba1d47beb3e58e7700ecf9cfb08e8fae76c3be0299163311bb0f8d784ef6466c}.
\]

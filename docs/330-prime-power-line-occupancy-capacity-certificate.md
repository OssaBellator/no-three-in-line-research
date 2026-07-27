# One line-occupancy table bounds the complete geometric response energy

CMR1782--CMR1813 give exact marginal, nested-assignment and rank-three fibre
certificates.  A complementary host-level bound is available when the background
line loads are known: compute the maximum number of response points which any
perfect matching can place on each real grid line.

This produces one finite line-occupancy table.  The same table simultaneously
bounds rank-one, rank-two and rank-three response energy.  It is background-
dependent only through the line loads, and every occupancy entry is an ordinary
zero-one assignment optimum.

Let `G` be an embedded bipartite response host of side `d` with at least one
perfect matching.  Let `B` be a fixed background point set disjoint from the
chosen response.  For every real grid line `ell`, put

\[
h_\ell=|B\cap\ell|
\]

and define the exact host occupancy capacity

\[
\tau_G(\ell)
=
\max_{Q\in\operatorname{PM}(G)}|Q\cap\ell|.
\]

Only finitely many lines through at least two relevant grid cells need be stored.
Axis lines have occupancy at most one in every perfect matching and contribute no
rank-two or rank-three term.

## 1. Occupancy is an assignment optimum

For one line `ell`, define the cell score

\[
s_\ell(x)=\mathbf 1_{x\in\ell}.
\]

### Theorem CMR1814 -- PROVED

\[
\boxed{
\tau_G(\ell)
=
\mathcal A_G(s_\ell).
}
\]

Consequently `tau_G(ell)` has an integral bipartite assignment dual and an exact
source/target-cover certificate.

### Proof

The score of one perfect matching under `s_ell` is exactly its number of selected
cells on `ell`.  Maximizing over perfect matchings gives the definition of
`tau_G(ell)`.  Integrality and duality are the standard assignment theorem. ∎

Thus no geometric probability estimate is needed to compute the occupancy table.

## 2. Linewise monotone energy bound

For a response matching `Q`, put

\[
k_\ell=|Q\cap\ell|.
\]

### Theorem CMR1815 -- PROVED

For every line,

\[
\boxed{
 k_\ell\binom{h_\ell}{2}
 +\binom{k_\ell}{2}h_\ell
 +\binom{k_\ell}{3}
\le
 \tau_G(\ell)\binom{h_\ell}{2}
 +\binom{\tau_G(\ell)}{2}h_\ell
 +\binom{\tau_G(\ell)}{3}.
}
\]

### Proof

By definition, `0<=k_ell<=tau_G(ell)`.  Each of the functions

\[
k,
\qquad
\binom k2,
\qquad
\binom k3
\]

is nondecreasing on the nonnegative integers.  Multiply by the nonnegative
background coefficients and add. ∎

This retains the exact background load of each supporting line.

## 3. Complete line-capacity row

Define

\[
\mathcal C_G(B)
=
\sum_\ell
\left[
 \tau_G(\ell)\binom{h_\ell}{2}
 +\binom{\tau_G(\ell)}{2}h_\ell
 +\binom{\tau_G(\ell)}{3}
\right].
\]

### Theorem CMR1816 -- PROVED

Every response perfect matching satisfies

\[
\boxed{
\Psi(B\cup Q)-\Psi(B)
\le
\mathcal C_G(B).
}
\]

Every corrected genuinely new offspring row is bounded by the same quantity.

### Proof

CMR1767 gives the exact line-energy sum with `k_ell`.  Apply CMR1815 on every
line and sum.  CMR1768 bounds every corrected row by the complete line energy. ∎

The maxima on different lines need not be attained by one response; this is an
upper certificate, not an equality claim.

## 4. Rank-one line-trace certificate

Define

\[
C_1(G,B)
=
\sum_\ell
\tau_G(\ell)\binom{h_\ell}{2}.
\]

### Theorem CMR1817 -- PROVED

The rank-one response term satisfies

\[
\boxed{
\max_{Q\in\operatorname{PM}(G)}
\sum_{x\in Q}a_1(x)
\le
C_1(G,B).
}
\]

Moreover, choose for every line an exact assignment dual for `s_ell` and multiply
its vertex weights by `C(h_ell,2)`.  Adding these duals gives a feasible assignment
dual for the complete rank-one score `a_1`, with objective `C_1(G,B)`.

### Proof

Regroup the deterministic rank-one score by lines:

\[
\sum_{x\in Q}a_1(x)
=
\sum_\ell k_\ell\binom{h_\ell}{2}.
\]

Bound `k_ell` by `tau_G(ell)`.  For the dual statement, the weighted sum of the
line-indicator scores is exactly `a_1`; sums of feasible duals remain feasible and
the objectives add. ∎

This is an explicit source/target-cover construction for the rank-one frontier.

## 5. Rank-two occupancy certificate

Define

\[
C_2(G,B)
=
\sum_\ell
\binom{\tau_G(\ell)}{2}h_\ell.
\]

### Theorem CMR1818 -- PROVED

Every response satisfies

\[
\boxed{
\sum_{\{x,y\}\subseteq Q}a_2(\{x,y\})
\le
C_2(G,B).
}
\]

### Proof

The exact rank-two contribution on line `ell` is `C(k_ell,2)h_ell`.  Apply
`k_ell<=tau_G(ell)` and sum. ∎

This may be combined with exact rook marginals or the nested rank-two assignment
by taking the smaller bound class by class.

## 6. Rank-three occupancy certificate

Define

\[
C_3(G)
=
\sum_\ell\binom{\tau_G(\ell)}{3}.
\]

### Theorem CMR1819 -- PROVED

Every response satisfies

\[
\boxed{
\Psi(Q)\le C_3(G).
}
\]

For side four and side five, the exact host numerator table of CMR1809--CMR1810
and the deterministic cap `4` of CMR1807 may replace this linewise sum whenever
they are smaller.

### Proof

The exact rank-three response count is `sum_ell C(k_ell,3)` by CMR1769.  Apply
`k_ell<=tau_G(ell)` line by line. ∎

No background information enters `C_3(G)`.

## 7. Strict integer line-capacity certificate

### Theorem CMR1820 -- PROVED

If destroyed current load is `D` and

\[
\boxed{
\mathcal C_G(B)<D,
}
\]

then every response perfect matching of `G` has strictly smaller potential.

More generally, the three terms `C_1,C_2,C_3` may independently be replaced by
smaller exact marginal, nested-assignment, denominator-specific or corrected-row
bounds.  Any resulting integer sum below `D` is a strict certificate.

### Proof

CMR1816 bounds complete new line energy for every response.  A corrected recurrent
row is no larger.  Strict comparison with the destroyed load gives deterministic
improvement.  Replacing any term by a proved smaller upper bound preserves the
inequality. ∎

This certificate is stronger than an expectation argument when it succeeds,
because every response is improving.

## 8. Line-occupancy endpoint

### Corollary CMR1821 -- PROVED

Every exact geometric fibre now has a finite background-line compiler.

1. Compute `tau_G(ell)` by one zero-one assignment per relevant line.
2. Add the rank-one line duals to obtain a direct cover certificate for `a_1`.
3. Bound rank two by `sum h_ell C(tau_ell,2)`.
4. Bound rank three by `sum C(tau_ell,3)` or the exact side-four/five census.
5. Compare the integer total with destroyed load.
6. Mix this line-capacity route with exact rook marginals and nested assignments
   wherever they are sharper.
7. Preserve line, owner, collision, local-line, interface and CRT provenance when
   the total is split among recurrent child classes.

The remaining work is to insert the actual background line loads and provenance
routing into each of the 740 raw side-four/five hosts and the larger structurally
surviving fibres.  No all-`n` theorem is claimed.

All 740 raw hosts, 96,892 host-line occupancy capacities and 9260 response-energy
checks are verified in
[`scripts/verify_prime_power_line_occupancy_capacity.py`](../scripts/verify_prime_power_line_occupancy_capacity.py).

# Fixed line-clean selector failures have finite obstruction stock or one recurrent target-load atom

CMR541--CMR545 reduce every recurrent persistent-cross branch to one fixed
compatible paid pair and one fixed paid line.  The current restricted host and
the adaptive forbidden-matching extension may still vary from occurrence to
occurrence.  At each failed occurrence, however, CMR544 gives the same exact
weighted obstruction

\[
A_j+\frac{2}{q}+\frac{|B_j|}{q(n-1)}\ge 1,
\qquad
A_j=\frac{30}{11}S_j,
\]

where

\[
S_j=
\frac{V_{0,j}}{(n)_3}
+
\frac{V_{1,j}}{(n)_2}.
\]

This chapter removes the remaining double-counting ambiguity.  For `q>=4`,
every failure has either constant normalized collateral or a linear unavailable
inventory.  The unavailable branch has finite physical edge stock unless one
edge recurs.  The collateral branch has finite rank-zero/rank-one conflict stock
unless one exact candidate triple recurs.  A recurrent rank-one atom is one
fixed secant line through a paid endpoint, distinct from the paid line; a
recurrent rank-zero atom is one fixed residual target-load atom.

Fix one envelope epoch of side `m`, one compatible paid pair

\[
Z=\{z_1,z_2\},
\]

and its nonaxis paid line `L`.  Delete the endpoints of `Z` and put

\[
n=m-2\ge5.
\]

A **selector occurrence** consists of a current host, one adaptive forbidden
matching extending the residual trace of `L`, and the associated line-clean
derangement cylinder.  Let `B_j` be its unavailable allowed residual edges,
and let `V_{0,j},V_{1,j},S_j,A_j` have the CMR333 meaning.  Call the occurrence
**failed at threshold `q`** when no completion has

\[
X_L=0,
\qquad
T_Z<q.
\]

## 1. Constant polarization of every failed selector

### Theorem CMR546 — PROVED

Assume

\[
q\ge4.
\]

Every failed selector occurrence satisfies at least one of

\[
\boxed{
S_j\ge\frac{11}{120}
}
\]

or

\[
\boxed{
|B_j|\ge\frac{q(n-1)}4.
}
\]

Since `|B_j|` is integral, the second conclusion may be written

\[
\boxed{
|B_j|\ge
H_q(n):=
\left\lceil\frac{q(n-1)}4\right\rceil.
}
\]

### Proof

CMR544 says failure implies

\[
\frac{30}{11}S_j+\frac2q+\frac{|B_j|}{q(n-1)}\ge1.
\]

If both displayed conclusions failed, then

\[
\frac{30}{11}S_j<\frac14,
\qquad
\frac2q\le\frac12,
\qquad
\frac{|B_j|}{q(n-1)}<\frac14.
\]

Their sum would be below one, contradiction. ∎

Thus a failed fixed selector cannot hide simultaneously in small collateral
and small unavailable inventory.

## 2. Unavailable inventory: finite edge stock or recurrence

Consider `J_B` failed occurrences assigned to the unavailable branch of
CMR546.  For a residual edge `f`, let

\[
\mu_B(f)=|\{j:f\in B_j\}|.
\]

### Theorem CMR547 — PROVED

Fix an integer

\[
\lambda\ge2.
\]

At least one of the following holds.

1. **Recurrent unavailable edge.**  Some residual edge belongs to at least
   `\lambda` of the sets `B_j`.
2. **Finite unavailable-selector count.**
   \[
   \boxed{
   J_B
   \le
   \frac{(\lambda-1)n^2}{H_q(n)}.
   }
   \]

In the recurrent branch, CMR519 gives either absent-to-present reintroduction
payment or one interval on which that edge remains continuously unavailable
through many selected occurrences.

### Proof

Every `B_j` has at least `H_q(n)` edges by CMR546, so

\[
J_BH_q(n)
\le
\sum_j|B_j|
=
\sum_f\mu_B(f).
\]

There are `n^2` physical residual edges.  If no edge occurs `\lambda` times,
then every multiplicity is at most `\lambda-1`, giving

\[
J_BH_q(n)\le(\lambda-1)n^2.
\]

Rearrange.  The temporal conclusion is CMR519. ∎

The bound deliberately uses the complete residual edge universe, so it remains
valid while the adaptive forbidden matching changes.

## 3. Collateral polarization by rank

Consider one occurrence in the collateral branch

\[
S_j\ge\frac{11}{120}.
\]

### Theorem CMR548 — PROVED

At least one of the following holds.

1. **Rank-zero mass.**
   \[
   \boxed{
   V_{0,j}
   \ge
   \frac{11}{240}(n)_3.
   }
   \]
2. **Rank-one mass.**
   \[
   \boxed{
   V_{1,j}
   \ge
   \frac{11}{240}(n)_2.
   }
   \]

One may assign every collateral occurrence canonically to the first branch
when it holds and otherwise to the second branch.

### Proof

If both normalized terms were below `11/240`, then

\[
S_j=
\frac{V_{0,j}}{(n)_3}
+
\frac{V_{1,j}}{(n)_2}
<
\frac{11}{120},
\]

contradiction. ∎

This separates the two geometric obstruction types already identified in
CMR333--CMR334.

## 4. Exact finite conflict stocks

A rank-zero conflict is an unordered compatible three-edge residual
prescription.  A rank-one conflict consists of one of the two paid cells
together with an unordered compatible two-edge residual prescription.

### Theorem CMR549 — PROVED

The numbers of possible exact conflict atoms satisfy

\[
\boxed{
N_0(n)
\le
\binom n3^2\,3!
=
\frac{(n)_3^2}{6}
}
\]

and

\[
\boxed{
N_1(n)
\le
2\binom n2^2\,2!
=
(n)_2^2.
}
\]

Fix `\lambda>=2`.  Let `J_0,J_1` be the numbers of collateral occurrences
assigned by CMR548 to ranks zero and one.  Then at least one of the following
holds.

1. Some exact rank-zero candidate triple occurs in at least `\lambda`
   rank-zero obstruction sets.
2. Some exact rank-one candidate triple occurs in at least `\lambda`
   rank-one obstruction sets.
3. Both counts are finite:
   \[
   \boxed{
   J_0
   \le
   \frac{40}{11}(\lambda-1)(n)_3
   }
   \]
   and
   \[
   \boxed{
   J_1
   \le
   \frac{240}{11}(\lambda-1)(n)_2.
   }
   \]

Consequently, if no exact conflict atom recurs `\lambda` times, then

\[
\boxed{
J_0+J_1
\le
\frac{40}{11}(\lambda-1)(n)_3
+
\frac{240}{11}(\lambda-1)(n)_2.
}
\]

### Proof

Choose three residual source vertices, three residual target vertices, and a
bijection between them.  This gives the rank-zero stock bound.  For rank one,
choose the paid cell, two residual sources, two residual targets, and one of
the two bijections.

Every rank-zero occurrence contains at least
`(11/240)(n)_3` exact atoms by CMR548.  If every atom occurs at most
`\lambda-1` times, double counting gives

\[
J_0\frac{11}{240}(n)_3
\le
(\lambda-1)\frac{(n)_3^2}{6}.
\]

Rearranging gives the displayed rank-zero bound.  The rank-one calculation is

\[
J_1\frac{11}{240}(n)_2
\le
(\lambda-1)(n)_2^2.
\]

Rearrange again. ∎

Collinearity and forbidden-line restrictions only reduce the actual stocks,
so the complete matching-prescription universes are safe upper bounds.

## 5. Geometry of recurrent conflict atoms

### Theorem CMR550 — PROVED

Fix the paid pair `Z` and paid line `L`.

1. A recurrent rank-zero atom is one fixed candidate-only collinear triple
   disjoint from `Z`.  It is therefore one fixed residual target-load atom.
2. A recurrent rank-one atom has the form
   \[
   C=\{z,r_1,r_2\},
   \qquad z\in Z,
   \]
   where `r_1,r_2` are residual matching edges.  Its supporting line
   `L_C` is fixed and satisfies
   \[
   \boxed{L_C\ne L.}
   \]
   Thus `(L,L_C,z)` is one fixed two-line secant-fan signature through the
   paid endpoint `z`.

### Proof

Exact recurrence fixes the candidate triple itself, hence its supporting real
line.

For rank one, suppose `L_C=L`.  Then the two residual cells `r_1,r_2` lie on
the paid line.  Every line-clean cylinder forbids every residual cell of `L`,
so such a triple cannot belong to `V_1`.  Therefore `L_C\ne L`. ∎

The rank-one recurrent branch is precisely a fixed secant shadow through a
paid endpoint.  The rank-zero branch is precisely a fixed residual modular-
syndrome target.

## 6. Unified fixed-selector history endpoint

### Corollary CMR551 — PROVED

Fix one envelope-labelled compatible paid pair and paid line, one threshold
`q>=4`, and one recurrence threshold `\lambda>=2`.  For any collection of
failed selector occurrences, at least one of the following holds.

1. **Finite unavailable history.**
   \[
   J_B\le
   \frac{(\lambda-1)n^2}{H_q(n)}.
   \]
2. **Unavailable-edge recurrence.**  One residual edge occurs in at least
   `\lambda` unavailable inventories, hence pays reintroduction or becomes
   continuously unavailable on one long interval.
3. **Finite collateral history.**
   \[
   J_C
   \le
   \frac{40}{11}(\lambda-1)(n)_3
   +
   \frac{240}{11}(\lambda-1)(n)_2.
   \]
4. **Fixed rank-zero target atom.**  One exact residual candidate triple recurs
   at least `\lambda` times.
5. **Fixed rank-one secant fan.**  One exact candidate triple through one paid
   endpoint recurs at least `\lambda` times, giving a fixed second line distinct
   from the paid line.

### Proof

Assign every failed occurrence by CMR546, breaking ties in favor of the
unavailable branch.  Apply CMR547 to unavailable occurrences.  Apply
CMR548--CMR550 to collateral occurrences. ∎

## 7. Revised frontier

Repeated failure of a fixed line-clean selector no longer has uncontrolled
double counting.

- The unavailable side has finite physical stock unless one exact edge recurs.
- The collateral side has finite rank-zero/rank-one prescription stock unless
  one exact conflict recurs.
- A recurrent unavailable edge enters the existing reintroduction/persistent-
  blocker machinery.
- A recurrent rank-zero atom is one fixed residual target-load certificate.
- A recurrent rank-one atom is one fixed two-line secant-fan signature through
  a paid endpoint.

The immediate prime-power frontier is now payment for the last two fixed
geometric atoms.  One must feed the rank-zero atom into the existing modular-
syndrome/quotient/carry ledger and the rank-one fan into the paid mixed-ratio,
line-energy, heavy-prefix, protected-reserve, deletion-ancestry, or envelope-
expansion alternatives, while keeping the selector-signature label fixed.

No all-`n` theorem is claimed.  The constants, matching-prescription stock
counts, recurrence arithmetic, and line-separation assertion are checked in
[`scripts/verify_prime_power_fixed_selector_obstruction_stock.py`](../scripts/verify_prime_power_fixed_selector_obstruction_stock.py).

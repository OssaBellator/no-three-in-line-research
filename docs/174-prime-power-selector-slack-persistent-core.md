# Weak dynamic slack is near-static, while persistent contacts amplify to recurrent unavailable cores

CMR587--CMR592 extract recurrent unavailable sets from large dynamic selector
histories.  One edge case remains important: the exact persistent contact from
CMR586 may occur when the canonical dynamic threshold is only one.  In that
case there is no second unavailable edge to extract from every failure.

The selector slack itself resolves this case.  Threshold one means that the
fixed collateral profile lies within `1/[q(n-1)]` of the static boundary, so it
already has a positive constant normalized rank-zero/rank-one mass.  All of the
canonical line, secant-star, primitive-height, wall, prefix, carry, and deletion
conclusions therefore apply with a slightly weaker explicit constant.

When the threshold is at least two, a fixed persistent contact may be
conditioned out of every unavailable inventory.  The remaining inventories
still have size at least `H_P-1`, so exact subset double counting extracts an
additional recurrent set.  On a nested joint-absence interval this produces a
larger persistent unavailable core containing the original contact.  The core
then enters the batch-absorption versus persistent-wall theorem CMR589.

Fix one dynamic canonical protected selector state `P` with residual side
`n>=5`, selector parameter `q>=4`, canonical collateral profile

\[
S_P=
\frac{V_0(P)}{(n)_3}
+
\frac{V_1(P)}{(n)_2},
\qquad
A_P=\frac{30}{11}S_P,
\]

and positive slack

\[
\Delta_P
=
1-\frac2q-A_P
>0.
\]

Its exact unavailable threshold is

\[
H_P
=
\left\lceil q(n-1)\Delta_P\right\rceil.
\]

Every failed occurrence has an unavailable canonical allowed set

\[
B_j\subseteq U_P,
\qquad
|B_j|\ge H_P,
\qquad
|U_P|=N=n(n-1).
\]

## 1. Small unavailable threshold forces collateral mass

### Theorem CMR593 — PROVED

Fix an integer `r>=2`.  If

\[
H_P<r,
\]

then

\[
\boxed{
S_P
\ge
c_{q,n,r}
:=
\frac{11}{30}
\left(
1-rac2q-rac{r-1}{q(n-1)}
\right).
}
\]

In particular, if `H_P=1`, then

\[
\boxed{
S_P
\ge
\widetilde c_{q,n}
:=
\frac{11}{30}
\left(
1-rac2q-rac1{q(n-1)}
\right).
}
\]

For `q>=4` and `n>=5`,

\[
\boxed{
\widetilde c_{q,n}
\ge
\frac{77}{480}.
}
\]

### Proof

Since `H_P=ceil(q(n-1)Delta_P)<r`, one has

\[
q(n-1)\Delta_P
\le
H_P
\le
r-1.
\]

Therefore

\[
A_P
=
1-rac2q-\Delta_P
\ge
1-rac2q-rac{r-1}{q(n-1)}.
\]

Multiply by `11/30`.  For `r=2`, the expression is minimized over
`q>=4,n>=5` at `q=4,n=5`, where it equals

\[
\frac{11}{30}\left(1-rac12-rac1{16}\right)
=
\frac{77}{480}.
\]

∎

Thus a threshold-one selector is not a genuinely sparse geometric exception;
it is a fixed near-static collateral profile.

## 2. Near-static profiles inherit the complete static geometry

### Theorem CMR594 — PROVED

Assume `H_P=1`.  Put

\[
\widetilde c=\widetilde c_{q,n}.
\]

At least one of the following holds.

1. **Rank-zero near-static mass.**
   \[
   \boxed{
   V_0(P)
   \ge
   \frac{\widetilde c}{2}(n)_3.
   }
   \]
2. **One-endpoint rank-one near-static mass.**  Some paid endpoint `z` satisfies
   \[
   \boxed{
   V_1(P;z)
   \ge
   \frac{\widetilde c}{4}(n)_2.
   }
   \]

Every conclusion of CMR559--CMR570 whose proof uses only the lower bound on
`S_P` remains valid with `c_q` replaced by `\widetilde c`.  In particular the
profile reaches a fixed low-height heavy line, a paid-endpoint secant star, a
matching-vertex wall, a heavy full-prefix cell, a dispersed carry-cell family,
or the rank-zero disjoint-deletion endpoint.

### Proof

Apply the rank-polarization proof of CMR558 to the lower bound in CMR593.  The
support-line decomposition, binomial capacities, square-root extraction,
factorial-moment energy, dyadic height localization, matching-wall/prefix/carry
conversion, and disjoint-deletion arguments are homogeneous in the assumed
lower bound for `S_P`; substitute `\widetilde c` throughout. ∎

No availability property of the recurring contact edge is needed in this
branch.

## 3. Conditional recurrent-set extraction

Let a fixed unavailable set

\[
F_0\subseteq U_P,
\qquad
|F_0|=a<H_P,
\]

be contained in every selected inventory `B_j`.  This includes the case where
`F_0` is already continuously unavailable on the selected interval.

### Theorem CMR595 — PROVED

Fix integers

\[
1\le r\le H_P-a,
\qquad
\lambda\ge2.
\]

For any `J` selected failed occurrences, at least one of the following holds.

1. **Additional recurrent set.**  Some fixed `r`-edge set
   \[
   W\subseteq U_P\setminus F_0
   \]
   is contained in at least `\lambda` of the residual inventories
   \[
   B_j\setminus F_0.
   \]
2. **Finite conditioned history.**
   \[
   \boxed{
   J
   \le
   (\lambda-1)
   \frac{\binom{N-a}{r}}
        {\binom{H_P-a}{r}}.
   }
   \]

### Proof

Every residual inventory `B_j\setminus F_0` has size at least `H_P-a` inside
the fixed universe `U_P\setminus F_0` of size `N-a`.  Double-count its
`r`-subsets exactly as in CMR587. ∎

The conditioning preserves the ownership label of the selector and of the
already persistent core.

## 4. Persistent-core amplification

Assume `F_0` remains continuously unavailable on one interval and the
additional set `W` from CMR595 occurs at `\lambda` selected times in that
interval.

### Theorem CMR596 — PROVED

For every integer `\sigma>=2`, at least one of the following holds.

1. **Additional-edge reintroduction payment.**
   \[
   \boxed{
   \sum_{w\in W}I(w)
   \ge
   \left\lceil\frac{\lambda}{\sigma-1}\right\rceil-1.
   }
   \]
2. **Amplified persistent core.**  One subinterval contains at least `\sigma`
   selected occurrences while every edge of
   \[
   \boxed{F_0\cup W}
   \]
   remains continuously unavailable.

### Proof

Apply CMR538 to `W` within the interval.  In its joint-absence branch, `F_0`
remains absent because the new interval is nested inside the original one. ∎

Thus persistent cores can grow without losing their earlier edges.

## 5. A persistent contact amplifies directly to any target rank

Suppose one exact contact edge `f` remains continuously unavailable throughout
`J` selected failed occurrences and `H_P>=2`.

### Theorem CMR597 — PROVED

Fix a target rank

\[
2\le r\le H_P
\]

and integers `\lambda,\sigma>=2`.  At least one of the following holds.

1. **Finite contact-conditioned history.**
   \[
   \boxed{
   J
   \le
   (\lambda-1)
   \frac{\binom{N-1}{r-1}}
        {\binom{H_P-1}{r-1}}.
   }
   \]
2. **Aggregate reintroduction payment.**  A fixed additional `(r-1)`-edge set
   reaches the first branch of CMR596.
3. **Persistent `r`-core containing the contact.**  One subinterval contains at
   least `\sigma` selected occurrences while a fixed `r`-edge set
   \[
   \boxed{W_r\ni f}
   \]
   remains continuously unavailable.

### Proof

Apply CMR595 with `F_0={f}`, `a=1`, and residual rank `r-1`.  In the recurrent
branch apply CMR596. ∎

The theorem avoids an iterative loss: the desired target rank is extracted in
one subset-counting step.

## 6. Unified weak-slack and persistent-contact endpoint

### Corollary CMR598 — PROVED

Fix `q>=4,n>=5`.  Every exact persistent-contact branch of a dynamic canonical
selector reaches at least one of the following endpoints.

1. **Near-static collateral geometry.**  If `H_P=1`, CMR593--CMR594 give a fixed
   positive collateral profile with
   \[
   S_P\ge77/480
   \]
   and the complete line/secant-star/wall/prefix/carry/deletion alternatives.
2. **Finite contact-conditioned history.**  For `H_P>=2`, the bound of CMR597
   holds at every chosen target rank `2<=r<=H_P`.
3. **Aggregate reintroduction payment.**  Additional recurrent edges pay the
   multi-edge return ledger.
4. **Persistent unavailable core.**  A fixed `r`-edge core containing the
   original contact remains jointly unavailable and enters CMR589--CMR591,
   yielding batch protected absorption or a persistent row/column token wall.

Repeated batch absorption has finite depth by CMR590.

### Proof

Split on `H_P=1`.  Use CMR594 in the first case.  In the second case choose any
`2<=r<=H_P`, apply CMR597, and then CMR589--CMR591 to a persistent core. ∎

## 7. Revised frontier

The final single-contact exception is no longer isolated.

- Threshold one is a constant near-static collateral profile.
- Higher thresholds amplify one persistent contact to a persistent unavailable
  core of any chosen rank, unless the conditioned history is finite or pays
  reintroduction.
- Persistent cores yield batch absorption or simultaneous token walls.

The remaining prime-power frontier is temporal reuse of the resulting fixed
near-static wall/prefix/carry certificates and fixed persistent core/token
walls after all batch absorption capacity is exhausted.  The expected exits
remain protected-reserve depletion, deletion ancestry, full-token return, or
strict envelope expansion.

No all-`n` theorem is claimed.  Slack constants, conditional subset counting,
nested joint-absence amplification, and target-rank extraction are checked in
[`scripts/verify_prime_power_selector_slack_core.py`](../scripts/verify_prime_power_selector_slack_core.py).

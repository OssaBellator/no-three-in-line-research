# Static canonical collateral profiles yield heavy lines or large line-signature banks

CMR552--CMR557 attach every high-collateral obstruction to one canonical
selector signature.  Its paid pair, paid line, forbidden matching, allowed
residual host, and complete rank-zero/rank-one conflict profile are fixed.
There is therefore no temporal multiplicity left to control.

This chapter converts that static conflict profile into the line geometry used
elsewhere in the repair programme.  Rank-zero conflicts group by residual
candidate lines.  Rank-one conflicts group by secant lines through one paid
endpoint.  A weighted heavy-or-dispersed split gives either one line containing
many conflict atoms or many distinct line signatures.

Fix one canonical selector signature

\[
\Sigma=(E,Z,L),
\qquad
Z=\{z_1,z_2\},
\]

with residual side

\[
n=m-2\ge5.
\]

Let

\[
\mathcal C_0(\Sigma),
\qquad
\mathcal C_1(\Sigma)
\]

be its exact rank-zero and rank-one candidate-only conflict sets, of sizes

\[
V_0(\Sigma),
\qquad
V_1(\Sigma).
\]

## 1. Exact support-line decomposition

Every candidate-only conflict is a collinear triple of compatible grid cells
and therefore has one unique nonaxis supporting real line.

For a nonaxis line `H`, define

\[
w_0(H)
=
|\{C\in\mathcal C_0(\Sigma):\operatorname{line}(C)=H\}|.
\]

For a paid endpoint `z\in Z` and a line `H` through `z`, define

\[
w_1(z,H)
=
|\{C\in\mathcal C_1(\Sigma):
C\cap Z=\{z\},\ \operatorname{line}(C)=H\}|.
\]

### Theorem CMR558 — PROVED

The conflict counts decompose exactly as

\[
\boxed{
V_0(\Sigma)
=
\sum_H w_0(H)
}
\]

and

\[
\boxed{
V_1(\Sigma)
=
\sum_{z\in Z}
\sum_{H\ni z}w_1(z,H).
}
\]

Every line occurring in the rank-one sum satisfies

\[
\boxed{H\ne L.}
\]

If `k_0(H)` is the number of residual allowed cells which occur in rank-zero
conflicts on `H`, then

\[
\boxed{
w_0(H)\le\binom{k_0(H)}3.
}
\]

If `k_1(z,H)` is the number of residual allowed cells which occur in rank-one
conflicts with paid endpoint `z` on `H`, then

\[
\boxed{
w_1(z,H)\le\binom{k_1(z,H)}2.
}
\]

### Proof

Group each exact conflict by its unique supporting line and, in rank one, by
its unique paid endpoint.  This gives the two partition identities.

CMR550 shows that a rank-one support line cannot equal the paid line.  A
rank-zero atom on `H` is a three-element subset of its involved residual cells,
and a rank-one atom through `z` is a two-element subset of its involved
residual cells.  The binomial capacities follow. ∎

No assumption is made that every subset of cells on a line is an allowed
conflict; only the safe upper capacities are used.

## 2. Static rank polarization

Fix `q>=4` and suppose `\Sigma` is a static collateral signature in the sense
of CMR554.  Put

\[
c_q
=
\frac{11}{30}
\left(1-\frac2q\right).
\]

Thus

\[
S_\Sigma
=
\frac{V_0(\Sigma)}{(n)_3}
+
\frac{V_1(\Sigma)}{(n)_2}
\ge c_q.
\]

### Theorem CMR559 — PROVED

At least one of the following holds.

1. **Rank-zero static mass.**
   \[
   \boxed{
   V_0(\Sigma)
   \ge
   \frac{c_q}{2}(n)_3.
   }
   \]
2. **Rank-one static mass.**
   \[
   \boxed{
   V_1(\Sigma)
   \ge
   \frac{c_q}{2}(n)_2.
   }
   \]

In the rank-one branch, one paid endpoint `z\in Z` satisfies

\[
\boxed{
M_1(z)
:=
\sum_{H\ni z}w_1(z,H)
\ge
\frac{c_q}{4}(n)_2.
}
\]

### Proof

If both normalized rank terms were below `c_q/2`, their sum would be below
`c_q`.  In the rank-one branch, split the conflicts according to which of the
two paid endpoints they contain and apply pigeonhole. ∎

Thus every static profile carries a quantitatively large line-weight sum of one
fixed rank.

## 3. Weighted heavy-or-dispersed line lemma

### Theorem CMR560 — PROVED

Let nonnegative integer weights

\[
a_1,\ldots,a_s
\]

have positive total

\[
M=\sum_i a_i.
\]

For every integer threshold `H>=2`, at least one of the following holds.

1. **Heavy signature.**  Some `a_i>=H`.
2. **Dispersed signatures.**  At least
   \[
   \boxed{
   \left\lceil\frac{M}{H-1}\right\rceil
   }
   \]
   weights are nonzero.

With

\[
H(M)=\max\{2,\lceil\sqrt M\rceil\},
\]

one gets either one weight at least `H(M)` or at least

\[
\boxed{\lfloor\sqrt M\rfloor}
\]

distinct positive-weight signatures.

### Proof

If no weight reaches `H`, every positive weight is at most `H-1`.  Their
number must therefore be at least `\lceil M/(H-1)\rceil`.

For the square-root choice, the displayed quotient is at least
`\lfloor\sqrt M\rfloor`; the case `M=1` is immediate. ∎

This lemma applies to exact conflict multiplicities, not merely to occupied
cells.

## 4. Square-root rank-zero endpoint

Assume the rank-zero branch of CMR559 and put

\[
M_0=V_0(\Sigma).
\]

### Theorem CMR561 — PROVED

At least one of the following holds.

1. **Heavy residual conflict line.**  One nonaxis residual line `H` supports at
   least
   \[
   \boxed{
   H_0=\max\{2,\lceil\sqrt{M_0}\rceil\}
   }
   \]
   exact rank-zero candidate triples.  It then contains at least
   \[
   \boxed{
   k_0(H)
   \ge
   \left\lceil(6H_0)^{1/3}\right\rceil
   }
   \]
   involved residual cells.
2. **Dispersed residual line bank.**  At least
   \[
   \boxed{
   \lfloor\sqrt{M_0}\rfloor
   }
   \]
   distinct nonaxis lines support rank-zero candidate triples.

Since

\[
M_0\ge\frac{c_q}{2}(n)_3,
\]

the dispersed branch has size at least

\[
\boxed{
\left\lfloor
\sqrt{\frac{c_q}{2}(n)_3}
\right\rfloor.
}
\]

### Proof

Apply CMR560 to the weights `w_0(H)`.  In the heavy branch, CMR558 gives

\[
H_0\le w_0(H)\le\binom{k_0(H)}3\le\frac{k_0(H)^3}{6}.
\]

Rearrange.  The quantitative dispersed bound uses CMR559. ∎

The heavy branch is a fixed line-energy concentration.  The dispersed branch
is a large bank of distinct residual line signatures.

## 5. Square-root rank-one endpoint

Assume the rank-one branch of CMR559 and choose a paid endpoint `z` with

\[
M_1(z)\ge\frac{c_q}{4}(n)_2.
\]

### Theorem CMR562 — PROVED

At least one of the following holds.

1. **Heavy paid-endpoint secant.**  One line `H\ne L` through `z` supports at
   least
   \[
   \boxed{
   H_1=\max\{2,\lceil\sqrt{M_1(z)}\rceil\}
   }
   \]
   exact rank-one conflicts.  It then contains at least
   \[
   \boxed{
   k_1(z,H)
   \ge
   \left\lceil\sqrt{2H_1}\right\rceil
   }
   \]
   involved residual cells.
2. **Dispersed secant-fan bank.**  At least
   \[
   \boxed{
   \lfloor\sqrt{M_1(z)}\rfloor
   }
   \]
   distinct secant lines through the fixed paid endpoint `z` support rank-one
   conflicts.

The dispersed branch has size at least

\[
\boxed{
\left\lfloor
\sqrt{\frac{c_q}{4}(n)_2}
\right\rfloor.
}
\]

### Proof

Apply CMR560 to the weights `w_1(z,H)`.  In the heavy branch,

\[
H_1
\le
w_1(z,H)
\le
\binom{k_1(z,H)}2
\le
\frac{k_1(z,H)^2}{2}.
\]

Rearrange.  CMR559 supplies the lower bound for the dispersed branch. ∎

This is an exact repeated-cell secant-star endpoint centred at the fixed paid
cell `z`.

## 6. Canonical static-collateral endpoint

### Corollary CMR563 — PROVED

Every static canonical selector profile reaches one of four fixed geometric
objects.

1. A heavy rank-zero residual conflict line.
2. A square-root-sized bank of distinct rank-zero residual lines.
3. A heavy rank-one secant through one paid endpoint.
4. A square-root-sized secant-star bank through one paid endpoint.

All line weights and line signatures are fixed by the canonical selector
signature.  They are not paid repeatedly over time.

### Proof

Apply CMR559, followed by CMR561 in the rank-zero branch and CMR562 in the
rank-one branch. ∎

## 7. Revised frontier

Static canonical collateral is now expressed entirely in existing geometric
languages.

- Heavy rank-zero lines feed line energy, modular syndrome, quotient incidence,
  carry cells, and heavy-prefix continuation.
- Dispersed rank-zero lines feed protected line reserves and line-signature
  packing.
- Heavy rank-one secants are repeated-cell stars.
- Dispersed rank-one secants are fixed-centre fan banks and feed the paid
  mixed-ratio and fan-factorial carry machinery.

The remaining theorem is to splice the quantitative sizes above into the
strongest existing line-clean and mixed-fan constants, or show that failure of
those executions forces reserve depletion, deletion ancestry, or envelope
expansion.  The dynamic canonical-blocker branch of CMR557 remains the parallel
availability target.

No all-`n` theorem is claimed.  Support-line grouping, binomial capacities,
rank polarization, threshold arithmetic, and square-root alternatives are
checked in
[`scripts/verify_prime_power_static_selector_line_profile.py`](../scripts/verify_prime_power_static_selector_line_profile.py).

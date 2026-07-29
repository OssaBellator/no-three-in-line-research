# Bank-ready audit for rank-three active collateral

**Branch:** `research/rational-inverse-expansion`

RI5bd--RI5bk give exact bank-ready cylinder laws through source-coset rank two.  This note closes the remaining distinct-coset rank-three term.  It does not assert that every normalized rank-three profile is physically bank-ready: every record below retains its three physical source cosets, three target row cosets and three within-coset shifts.

Let

\[
X=\bigcup_{\alpha=1}^m u_\alpha H,
\qquad |H|=h,
\]

and use the uniform I6 bank on the installed physical block.  A **bank-ready rank-three prescription** fixes three distinct source cosets, three distinct target row cosets, an injective assignment between them, and one subgroup shift on each prescribed source coset.

## RI5bl -- exact rank-three I6 cylinder law -- PROVED

Assume `m>=3`.  Every compatible bank-ready rank-three prescription occurs in exactly

\[
(m-3)!h^{m-3}
\]

of the `m!h^m` I6 states.  Hence

\[
\boxed{
\Pr(T)=\frac1{(m)_3h^3}.
}
\]

If the prescription repeats a source coset or a target row coset, this formula is not used; the record is evaluated with its actual lower-rank correlation law or declared incompatible.

### Proof

The prescription fixes three distinct values of the coset permutation and three shift coordinates.  The remaining `m-3` permutation values and `m-3` shifts are free.  Division by the total state count gives the displayed probability. QED.

## RI5bm -- exact weighted rank-three collateral -- PROVED

Let `T_3` be a weighted multiset of compatible bank-ready rank-three records and put

\[
Q_3=\sum_{T\in T_3}c(T).
\]

For a uniform I6 state, the expected rank-three collateral is exactly

\[
\boxed{
\mathbb E C_3=\frac{Q_3}{(m)_3h^3}.
}
\]

No independence between records is required.

### Proof

Every record indicator has the probability from RI5bl.  Sum the weighted indicators and use linearity of expectation. QED.

## RI5bn -- complete bank-ready rank-at-most-three comparison -- PROVED UNDER THE PHYSICAL BLOCK HYPOTHESES

Let `W` be paid fixed-edge weight, `F` state-independent collateral, and let `Q_1,Q_2,Q_3` be the complete raw weights of compatible bank-ready distinct-coset prescriptions of ranks one, two and three.  Let `C_corr` be the exact expected contribution of repeated-coset, incompatible-or-conditionally-repaired, or otherwise correlated records, evaluated by their actual laws.  If

\[
\boxed{
\left(1-\frac1{mh}\right)W
>
F+\frac{Q_1}{mh}
 +\frac{Q_2}{(m)_2h^2}
 +\frac{Q_3}{(m)_3h^3}
 +C_{\rm corr},
}
\]

then one closed physical I6 state strictly lowers the paid potential.

### Proof

RI5a gives expected paid destruction at least `(1-1/(mh))W`.  RI5be, RI5bi and RI5bm give the three exact distinct-coset collateral terms.  Add the remaining exact correlated term.  Strictly positive expected net gain yields one improving state. QED.

## Corrected RI6 frontier

The bank-ready active collateral audit is now exact through source-coset rank three.  Remaining RI6 work is physical bank readiness, arithmetic owner payment, repeated-coset and blocker-repair correlations not already covered by their exact laws, and replenishable-source recurrence.  No generic `rank-three` probability remains uncomputed once the complete physical prescription is fixed.

## Finite check

`scripts/verify_ri_rank_three_bank_audit.py` enumerates small I6 banks, checks every compatible three-coset prescription count, verifies the weighted expectation identity and rejects repeated-source or repeated-target prescriptions from the distinct-coset formula.

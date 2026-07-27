# Rank mass and prescription multiplicity close a loaded line-clean regime

CMR1526--CMR1533 express the exact line-clean off-line collateral row as a sum
of candidate-triple multiplicities times prescription probabilities.
CMR1702--CMR1709 show that every response law has exactly `C(d,r)` total
probability mass in rank `r`. Combining the two facts gives a host-independent
bound once the geometric multiplicity of one response prescription is bounded.

The multiplicity is essential: several genuinely new triples may share the same
response prescription. This chapter retains that factor explicitly. The pure
`(d^3+5d)/6` threshold is valid only for injective candidate families.

Fix a bipartite response host `G` of side `d>=1` with at least one perfect
matching, and let `nu` be any probability law on `PM(G)`. For each rank
`r in {1,2,3}`, let `P_r` be the distinct corrected off-line response
prescriptions. For `P in P_r`, let

\[
m(P)\in\mathbb Z_{\ge0}
\]

be the number of genuinely new candidate triples having prescription `P`, and
put

\[
m_r=\max_{P\in P_r}m(P),
\]

with `m_r=0` when `P_r` is empty.

## 1. Exact multiplicity-weighted expectation

### Theorem CMR1710 -- PROVED

For every line-clean response law,

\[
\boxed{
\mathbb E N_{\mathrm{off}}(Q)
=
\sum_{r=1}^3\sum_{P\in P_r}m(P)\Pr(P\subseteq Q).
}
\]

### Proof

Each candidate triple occurs exactly when its residual response prescription is
contained in the sampled response. Sum one indicator for every candidate triple,
then group equal prescriptions. This is exactly the multiplicity `V_kappa`
grouping of CMR1533 refined to individual prescriptions. ∎

## 2. Multiplicity-corrected rank-mass bound

Define

\[
M_d(m_1,m_2,m_3)
=
\sum_{r=1}^3m_r C(d,r).
\]

### Theorem CMR1711 -- PROVED

\[
\boxed{
\mathbb E N_{\mathrm{off}}(Q)
\le
M_d(m_1,m_2,m_3).
}
\]

If every corrected candidate triple has a distinct response prescription, then
`m_1,m_2,m_3<=1` and

\[
\boxed{
\mathbb E N_{\mathrm{off}}(Q)
\le
C(d,1)+C(d,2)+C(d,3)
=
\frac{d^3+5d}{6}.
}
\]

### Proof

For rank `r`, use `m(P)<=m_r` and CMR1702:

\[
\sum_{P\in P_r}m(P)\Pr(P\subseteq Q)
\le
m_r\sum_{P\in P_r}\Pr(P\subseteq Q)
\le
m_r C(d,r).
\]

Add the three ranks. The injective specialization has `m_r<=1`. ∎

The bound is independent of the forbidden board and response denominator, but
it is not independent of geometric prescription multiplicity.

## 3. Forced-prescription subtraction

Let `F_r` be the number of rank-`r` prescriptions forced in every response and
already routed to the exact common-prescription contraction branch. Assume the
remaining nonforced prescriptions retain multiplicity cap `m_r`.

### Theorem CMR1712 -- PROVED

After forced common prescriptions are removed from the recurrent stochastic row,

\[
\boxed{
\mathbb E N_{\mathrm{off}}(Q)
\le
\sum_{r=1}^3m_r\bigl(C(d,r)-F_r\bigr).
}
\]

### Proof

CMR1705 gives total nonforced rank-`r` probability mass
`C(d,r)-F_r`. Multiply by the maximum remaining multiplicity `m_r` and add the
ranks. ∎

A forced contraction removes its complete prescription mass; its candidate
multiplicity is handled in the contraction branch rather than retained here.

## 4. Pointwise, count and rank-mass caps combine

Let

\[
N_r=\sum_{P\in P_r}m(P)
\]

be the total number of corrected rank-`r` candidate triples. Suppose every
nonforced rank-`r` prescription has probability at most `q_r`.

### Theorem CMR1713 -- PROVED

\[
\boxed{
\mathbb E N_{\mathrm{off}}(Q)
\le
\sum_{r=1}^3
\min\left\{
N_rq_r,
\ m_r\bigl(C(d,r)-F_r\bigr)
\right\}.
}
\]

### Proof

The pointwise bound follows by summing `N_r` candidate-triple probabilities,
each at most `q_r`. The rank-mass bound is CMR1712 rank by rank. Take the
minimum and add. ∎

Thus exact rook probabilities, side-four/five caps and multiplicity-corrected
rank mass are simultaneous constraints.

## 5. Large destroyed-load closure

Let `D` be the destroyed target load of the selected line-clean execution.
CMR1510--CMR1517 prove that the execution creates no new collateral entirely on
the cleaned line.

### Theorem CMR1714 -- PROVED

Assume the actual line-clean response host is nonempty. If

\[
\boxed{
D
>
\sum_{r=1}^3m_r\bigl(C(d,r)-F_r\bigr),
}
\]

then at least one executable line-clean response has strictly smaller potential.

For an injective candidate family it is sufficient that

\[
\boxed{
D
\ge
\frac{d^3+5d}{6}+1.
}
\]

### Proof

The line-local new collateral count is zero. CMR1712 bounds the complete
off-line expectation below `D`. Therefore the finite response average has
strictly smaller potential, and at least one response lies below the current
value. The second statement uses `m_r<=1` and `F_r>=0`. ∎

This theorem separates response feasibility from collateral control. It applies
only after the actual restricted host is known to contain a perfect matching.

## 6. Exact integer numerator certificate

Assume the response law has common denominator `Z>0` and write

\[
\Pr(P\subseteq Q)=n(P)/Z.
\]

Put

\[
A_{\mathrm{off}}
=
\sum_{r=1}^3\sum_{P\in P_r}m(P)n(P).
\]

### Theorem CMR1715 -- PROVED

Strict line-clean improvement is certified by

\[
\boxed{A_{\mathrm{off}}<ZD.}
\]

Moreover

\[
\boxed{
A_{\mathrm{off}}
\le
Z\sum_{r=1}^3m_r\bigl(C(d,r)-F_r\bigr).
}
\]

### Proof

The first inequality clears the response denominator in CMR1710. For the second,
use CMR1704--CMR1705 and the multiplicity cap in each rank. ∎

No numerical approximation is required.

## 7. Rooted-trace specialization

### Theorem CMR1716 -- PROVED

For rooted-target trace recurrence, the same multiplicity-corrected closure
applies and no endpoint-overlap coefficient is needed. If the rooted line-clean
host is nonempty and the destroyed rooted target load exceeds

\[
\sum_{r=1}^3m_r\bigl(C(d,r)-F_r\bigr),
\]

one rooted-target response is a strict improvement.

### Proof

CMR1566--CMR1573 place rooted trace recurrence in a target-disjoint line-clean
host and prove zero new line-local collateral. Apply CMR1714. ∎

The remaining rooted geometric task includes bounding the prescription
multiplicities `m_r`.

## 8. Multiplicity-aware endpoint

### Corollary CMR1717 -- PROVED

The line-clean frontier now has three complementary certificate levels.

1. Exact component-rook expectation with full candidate multiplicities.
2. Exact or universal prescription-count permanent budgets.
3. A rank-mass closure using explicit maximum multiplicities per prescription.

Every actual nonempty line-clean host whose destroyed load exceeds the
multiplicity-corrected nonforced rank mass has a strict-improvement response.
For injective candidate families this becomes the explicit threshold
`(d^3+5d)/6+1`. In general, the unresolved geometry includes proving small
rankwise multiplicity caps; those caps must not be omitted. No all-`n` theorem
is claimed.

Exact weighted rank-mass identities, forced-mass subtraction, pointwise/mass
minima and multiplicity-aware large-load implications are checked in
[`scripts/verify_prime_power_line_clean_rank_mass_large_load.py`](../scripts/verify_prime_power_line_clean_rank_mass_large_load.py).

# Rank mass closes the sufficiently loaded line-clean regime

CMR1526--CMR1533 express the exact line-clean off-line collateral row as a sum
of prescription probabilities. CMR1702--CMR1709 show that every response law
has exactly `C(d,r)` total probability mass in rank `r`. Combining these facts
gives a host-independent bound for the complete line-clean off-line expectation.

This is a genuine strict-improvement range. It does not require a permanent
lower bound, a prescription-count estimate, or a component-rook relaxation.
It applies to any actual nonempty response host after all chosen deletions and
availability restrictions have already been imposed.

Fix a bipartite response host `G` of side `d>=1` with at least one perfect
matching, and let `nu` be any probability law on `PM(G)`. For each rank
`r in {1,2,3}`, let `C_r` be the corrected family of genuinely new off-line
rank-`r` prescriptions. Put

\[
E_{\mathrm{off}}
=
\sum_{r=1}^3\sum_{P\in C_r}\Pr_{Q\sim\nu}(P\subseteq Q).
\]

Empty rank families are allowed when `r>d`.

## 1. Exact expectation form

### Theorem CMR1710 -- PROVED

For every line-clean response law, the expected number of genuinely new
off-line collateral credits is exactly

\[
\boxed{
\mathbb E N_{\mathrm{off}}(Q)
=
\sum_{r=1}^3\sum_{P\in C_r}\Pr(P\subseteq Q).
}
\]

### Proof

Each corrected off-line credit has one residual response prescription of rank
one, two or three. The indicator that the credit is created is the indicator
that its prescription is contained in the sampled response. Sum the indicators
and take expectation. This is the exact row interpretation already used in
CMR1526--CMR1533. ∎

## 2. Absolute rank-mass bound

Define

\[
M_d
=
C(d,1)+C(d,2)+C(d,3)
=
\frac{d^3+5d}{6},
\]

where `C(d,r)=0` for `r>d`.

### Theorem CMR1711 -- PROVED

Every corrected line-clean off-line family satisfies

\[
\boxed{
\mathbb E N_{\mathrm{off}}(Q)
\le
M_d
=
\frac{d^3+5d}{6}.
}
\]

### Proof

For each rank `r`, CMR1703 gives

\[
\sum_{P\in C_r}\Pr(P\subseteq Q)
\le
C(d,r).
\]

Add the three inequalities and simplify the polynomial. ∎

The bound is independent of the forbidden board, response denominator, deleted
line trace and chosen response law.

## 3. Forced-prescription subtraction

Let `F_r` be the number of rank-`r` prescriptions forced in every response and
already routed to the exact common-prescription contraction branch.

### Theorem CMR1712 -- PROVED

After those forced prescriptions are removed from the recurrent stochastic row,

\[
\boxed{
\mathbb E N_{\mathrm{off}}(Q)
\le
\sum_{r=1}^3\bigl(C(d,r)-F_r\bigr).
}
\]

### Proof

CMR1705 shows that the complete nonforced probability mass in rank `r` is
exactly `C(d,r)-F_r`. A corrected nonforced family is a subset of that mass.
Sum over the three ranks. ∎

Thus every forced contraction lowers the universal stochastic collateral budget
by one full unit.

## 4. Pointwise and mass caps combine

Suppose the corrected rank-`r` family has `N_r` prescriptions, every one has
probability at most `q_r`, and `F_r` prescriptions of that rank are forced and
removed.

### Theorem CMR1713 -- PROVED

\[
\boxed{
\mathbb E N_{\mathrm{off}}(Q)
\le
\sum_{r=1}^3
\min\{N_rq_r,\ C(d,r)-F_r\}.
}
\]

### Proof

Apply CMR1706 separately in each rank and add. ∎

The exact rook probabilities, side-four/five census caps, permanent bounds and
rank mass may therefore be used simultaneously rather than as competing
estimates.

## 5. Large destroyed-load closure

Let `D` be the destroyed target load of the selected line-clean execution.
CMR1510--CMR1517 prove that the execution creates no new collateral supported
entirely on the cleaned line.

### Theorem CMR1714 -- PROVED

Assume the actual line-clean response host is nonempty. If

\[
\boxed{
D
>
\sum_{r=1}^3\bigl(C(d,r)-F_r\bigr),
}
\]

then the expected new collateral is strictly smaller than the destroyed load.
Consequently at least one executable line-clean response has strictly smaller
potential.

In particular, without forced-prescription information it is enough that

\[
\boxed{
D\ge M_d+1
=
\frac{d^3+5d}{6}+1.
}
\]

### Proof

The line-local new collateral count is zero. CMR1712 bounds the complete
off-line expectation by the displayed quantity. If that quantity is below `D`,
the expected post-response potential is below the current potential after the
destroyed target load is removed. A finite average below the current value has
at least one response below the current value. ∎

This theorem separates response feasibility from collateral control. It applies
once the actual restricted host has at least one perfect matching; it does not
assert feasibility for an arbitrary unavailable-edge set.

## 6. Exact integer numerator certificate

Assume the response law has common denominator `Z>0`. For each corrected
prescription write

\[
\Pr(P\subseteq Q)=n(P)/Z.
\]

Put

\[
A_{\mathrm{off}}
=
\sum_{r=1}^3\sum_{P\in C_r}n(P).
\]

### Theorem CMR1715 -- PROVED

Strict line-clean improvement is certified by the integer inequality

\[
\boxed{A_{\mathrm{off}}<ZD.}
\]

Moreover

\[
\boxed{
A_{\mathrm{off}}
\le
Z\sum_{r=1}^3\bigl(C(d,r)-F_r\bigr).
}
\]

### Proof

The first inequality is the denominator-cleared expectation comparison. The
second is CMR1704--CMR1705 restricted to the corrected nonforced families. ∎

No numerical approximation is required.

## 7. Rooted-trace specialization

### Theorem CMR1716 -- PROVED

For rooted-target trace recurrence, the same rank-mass closure applies and no
endpoint-overlap coefficient is needed. If the rooted line-clean host is
nonempty and the destroyed rooted target load exceeds the corrected nonforced
rank mass, one rooted-target response is a strict improvement.

### Proof

CMR1566--CMR1573 place rooted trace recurrence in a target-disjoint line-clean
host and prove zero new line-local collateral. Apply CMR1714. ∎

This criterion may be stronger or weaker than the strong/singleton permanent
budget depending on the host; both remain valid and may be compared exactly.

## 8. Large-load endpoint

### Corollary CMR1717 -- PROVED

The line-clean frontier now has three complementary certificate levels.

1. Exact component-rook expectation and integer numerator comparison.
2. Exact or universal prescription-count permanent budgets.
3. A host-independent rank-mass closure for sufficiently large destroyed load.

Every actual nonempty line-clean host with destroyed load greater than its
corrected nonforced rank mass has a strict-improvement response. The unresolved
line-clean regime is therefore confined to targets with destroyed load at most
that finite mass bound, together with response-feasibility cases not covered by
the chosen host construction. No all-`n` theorem is claimed.

Exact rank-mass identities, forced-mass subtraction, pointwise/mass minima and
large-load implications are checked in
[`scripts/verify_prime_power_line_clean_rank_mass_large_load.py`](../scripts/verify_prime_power_line_clean_rank_mass_large_load.py).

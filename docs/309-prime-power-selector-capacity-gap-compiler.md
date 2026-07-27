# Class capacities compile critical selectors into return gaps

CMR1598--CMR1605 reduce every paid-pair selector to either a subunit return
splice or one finitely concentrated critical class.  The remaining finite class
bounds are naturally rational because exact rook probabilities share a common
response denominator.  This chapter shows that integer class capacities compile
directly into a quantitative gap below one and therefore into an exact
restoration cap.

The result gives a direct way to eliminate a proposed critical selector class.
If the sum of proved class capacities is smaller than the response denominator,
criticality is impossible and the entire selector becomes a bounded splice into
the shared return assignment.

Fix one exact selector response host.  Let its candidate-only expectation be

\[
A_L=\sum_{\chi\in\mathcal X}A_\chi,
\]

where `mathcal X` is any finite exact class partition retaining all desired rank,
profile, owner, height, token, prefix, carry, root, thin or interface labels.
Assume all class expectations have common denominator `D>0`:

\[
A_\chi=\frac{a_\chi}{D},
\qquad a_\chi\in\mathbb Z_{\ge0}.
\]

Suppose proved integer capacities satisfy

\[
0\le a_\chi\le C_\chi.
\]

Put

\[
C=\sum_{\chi\in\mathcal X}C_\chi.
\]

## 1. Total capacity upper bound

### Theorem CMR1646 -- PROVED

The selector expectation satisfies

\[
\boxed{A_L\le\frac CD.}
\]

In particular, if

\[
\boxed{C<D,}
\]

then the selector is subunit with exact gap

\[
\boxed{
\eta_C
=
1-\frac CD
=
\frac{D-C}{D}>0.
}
\]

### Proof

Sum the classwise inequalities `a_chi<=C_chi` and divide by `D`. ∎

The capacities may come from exact component-rook numerators, owner assignment
bounds, line-height capacities, token/prefix/carry restrictions or finite table
enumeration.  They need not be attained simultaneously.

## 2. Exact restoration cap from integer slack

Let `n>=2` be the selector response side and let `B=|B_L|` be the unavailable-
edge count in the CMR1558--CMR1565 selector theorem.

### Theorem CMR1647 -- PROVED

If `C<D`, the selector has a candidate-free execution with restoration count at
most

\[
\boxed{
T_C
=
\left\lfloor
\frac{D[2(n-1)+B]}
{(n-1)(D-C)}
\right\rfloor.
}
\]

### Proof

CMR1564 with `eta=eta_C` gives

\[
T_L
\le
\left\lfloor
\frac{2+B/(n-1)}{\eta_C}
\right\rfloor.
\]

Insert `eta_C=(D-C)/D` and combine the rational numerator over `n-1`. ∎

Thus the positive integer slack `D-C` simultaneously measures distance from
criticality and controls the restoration cap.

## 3. Critical-state exclusion

### Theorem CMR1648 -- PROVED

If `C<D`, no realization consistent with the class capacities can satisfy

\[
A_L\ge1.
\]

Conversely, every critical selector satisfying `A_L>=1` forces the necessary
capacity condition

\[
\boxed{C\ge D.}
\]

### Proof

The first statement follows from CMR1646.  The converse is its contrapositive. ∎

This is an exact integer exclusion criterion for every proposed critical class
family.

## 4. Per-prescription capacity form

Suppose class `chi` contains `N_chi` corrected candidate prescriptions and every
one has probability numerator at most `P_chi`, meaning

\[
D\Pr(P\subseteq R)\le P_\chi
\]

for every prescription in the class.

### Theorem CMR1649 -- PROVED

One may take

\[
\boxed{C_\chi=N_\chi P_\chi.}
\]

Consequently

\[
\boxed{
\sum_\chi N_\chi P_\chi<D
}
\]

is a finite integer certificate that the selector is a return splice, with
restoration cap CMR1647.

### Proof

The class numerator `a_chi` is a sum of `N_chi` nonnegative prescription
numerators, each at most `P_chi`. ∎

Exact component-rook counts give exact `P_chi`; the uniform strong, singleton or
overlap prescription bounds give coarser capacities after denominator clearing.

## 5. Partial exact enumeration and residual capacities

Partition the classes into an exactly enumerated set `E` and a bounded residual
set `R`.  Suppose the exact numerator sum on `E` is

\[
a_E=\sum_{\chi\in E}a_\chi
\]

and residual capacities are `C_chi` for `chi in R`.

### Theorem CMR1650 -- PROVED

Put

\[
\boxed{C_{\rm mix}=a_E+\sum_{\chi\in R}C_\chi.}
\]

If `C_mix<D`, then the selector has gap

\[
\boxed{\eta_{\rm mix}=\frac{D-C_{\rm mix}}D}
\]

and restoration cap obtained from CMR1647 with `C=C_mix`.

### Proof

Exact classes contribute their exact numerators.  Bound only the residual
classes and apply CMR1646--CMR1647. ∎

This permits incremental certification: exact thin or exceptional classes may
be enumerated first while broad geometric bounds handle the rest.

## 6. Coupling to the shared return assignment

Let `T_C` be the cap from CMR1647 and use the combined return-selector score

\[
h_{T_C}=g_{\rm ret}+T_Cg_{\rm sel}.
\]

### Theorem CMR1651 -- PROVED

If either

1. a rational assignment dual for `h_{T_C}` has objective below one; or
2. a CMR1630--CMR1637 superlevel cover certificate for `h_{T_C}` is below one,

then the selector together with its repeated-return offspring forms a
subcritical recurrent block.

### Proof

CMR1647 gives the selector row `(T_C,0)`.  CMR1586 or CMR1633 proves
`alpha+T_C beta<1`.  Apply CMR1562. ∎

The capacity and assignment certificates are therefore composable without
introducing a separate selector self-row.

## 7. Refined critical-class test

Assume the class partition has at most `N` classes.

### Theorem CMR1652 -- PROVED

If a selector remains critical, then in addition to `C>=D` there is at least one
class satisfying

\[
\boxed{
C_\chi\ge\left\lceil\frac DN\right\rceil.
}
\]

For the unrefined rank/profile partition one may use

\[
N=3B_n^3.
\]

### Proof

A critical realization has `sum a_chi>=D`.  Since `a_chi<=C_chi`, the capacities
sum to at least `D`; pigeonhole over at most `N` nonnegative capacities. ∎

This necessary condition can discard many refined geometric classes before
exact response enumeration.

## 8. Capacity-gap endpoint

### Corollary CMR1653 -- PROVED

Every finite critical-selector table now has an exact integer compiler.

1. Bound each class numerator by an integer capacity.
2. Sum capacities and compute the slack `D-C`.
3. If the slack is positive, eliminate criticality and obtain the exact
   restoration cap `T_C`.
4. Certify the resulting return-selector block by one shared assignment dual or
   superlevel cover certificate.
5. If the slack is nonpositive, retain only classes meeting the necessary
   capacity threshold of CMR1652 for sharper enumeration.

The remaining work is to supply sufficiently small class capacities from the
inherited geometric bounds and exact thin/interface tables.  No all-`n` theorem
is claimed.

Capacity sums, exact gap conversion, restoration caps and critical-state
exclusion are checked in
[`scripts/verify_prime_power_selector_capacity_gap_compiler.py`](../scripts/verify_prime_power_selector_capacity_gap_compiler.py).

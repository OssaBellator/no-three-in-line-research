# Polynomial-fibre capacities for protected-event addresses

**Branch:** `research/geometric-cleaning`

GC4ah--GC4ak reduce protected-height safety to address incidence caps and top eligible operation weights. Many geometric addresses are determined by one scalar parameter satisfying a fixed polynomial equation. This note turns that algebraic description into an occurrence-faithful capacity.

## GC4al -- nondegenerate polynomial fibre bound -- PROVED

Fix a protected address `p`. Suppose every operation eligible for `p` carries a scalar parameter `t` in a field `F`, distinct operations have distinct `t`, and eligibility implies

\[
F_p(t)=0
\]

for a nonzero polynomial `F_p in F[T]` of degree at most `d_p`. Then

\[
\boxed{|I_p|\le d_p.}
\]

### Proof

A nonzero polynomial of degree at most `d_p` over a field has at most `d_p` distinct roots. The operation-to-parameter map is injective. QED.

## GC4am -- bounded parameter multiplicity -- PROVED

If at most `M_p` eligible operations share one parameter value, then

\[
\boxed{|I_p|\le d_pM_p.}
\]

More generally, if root `t` has declared multiplicity capacity `M_p(t)`, then

\[
\boxed{|I_p|\le\sum_{t:F_p(t)=0}M_p(t).}
\]

### Proof

Partition the eligible operations by their parameter value and apply GC4al to the number of nonempty root fibres. Sum the per-fibre capacities. QED.

## GC4an -- polynomial top-weight capacity -- PROVED

Let `Y_p` be the physically eligible operation set for address `p`, with weights in decreasing order

\[
\lambda_{p,[1]}\ge\lambda_{p,[2]}\ge\cdots.
\]

Under GC4am,

\[
\boxed{
H_p
\le
S_p(d_pM_p)
=
\sum_{i=1}^{\min\{d_pM_p,|Y_p|\}}\lambda_{p,[i]}.
}
\]

Consequently, if

\[
\sum_pS_p(d_pM_p)\le\eta W,
\qquad 0\le\eta<1,
\]

then GC4aj gives the clean-height payment/Hall-deficiency continuation with factor `1-eta`.

### Proof

GC4am supplies an occurrence-faithful incidence cap. Apply the exact top-weight capacity theorem GC4ah and sum over addresses. QED.

## GC4ao -- exact degeneracy router -- PROVED

If a proposed polynomial fibre bound fails, one least exact cause is returned:

1. `F_p` is the zero polynomial, giving a coefficient-degeneracy profile;
2. its degree exceeds the declared `d_p`;
3. the operation-to-parameter multiplicity exceeds `M_p`;
4. an operation does not satisfy the polynomial address equation;
5. the field, eligibility, alias, lineage, context or weight record is not fixed;
6. or the nondegenerate incidence bound and its top-weight capacity hold.

Thus algebraic protected addresses no longer require an unstructured incidence estimate: a nonzero degree-`d` equation gives capacity `dM`, while failure is one explicit coefficient or multiplicity obstruction.

## Corrected GC5 frontier

For address families admitting a one-parameter polynomial description, the incidence problem is closed modulo coefficient degeneracy and bounded physical parameter multiplicity. Remaining work is to derive the polynomial address maps for the actual line, certificate, height and context events, control their fibre multiplicities and eligible top weights, and pay degenerate coefficient profiles or returned Hall cores.

## Finite check

`scripts/verify_gc_polynomial_fibre_capacity.py` exhausts small finite-field polynomials, checks the root bound and bounded-multiplicity extension, and verifies the induced top-weight capacity.
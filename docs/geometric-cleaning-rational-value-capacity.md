# Fixed-ratio capacities for rational line-following charts

**Branch:** `research/geometric-cleaning`

GC4ay--GC4bb resolve a coefficient-degenerate collinearity chart into either an identical pair or a rational line-following relation

\[
X_3-X_1=\lambda(t)(X_2-X_1),
\qquad
\lambda(t)=f(t)/g(t).
\]

This note gives root-count capacities for fixed ratio addresses inside that persistent family.

Assume `g` is nonzero, at most `M` physical operations share one parameter value, and put

\[
D=\max\{\deg f,\deg g\}.
\]

## GC4bc -- fixed-ratio polynomial equation -- PROVED

For a fixed finite ratio `alpha in F`, every parameter with `g(t)!=0` and `lambda(t)=alpha` satisfies

\[
\boxed{f(t)-\alpha g(t)=0.}
\]

Exactly one of the following holds:

1. `f-alpha g` is nonzero and has at most `D` roots;
2. `f-alpha g` is the zero polynomial, so `lambda` is identically the constant `alpha` in `F(t)`.

### Proof

Clear the nonzero denominator. The difference polynomial has degree at most `D`. A nonzero polynomial has at most its degree many roots. If the difference is zero, `f/g=alpha` as a rational function. QED.

## GC4bd -- fixed-ratio physical capacity -- PROVED

In the nonconstant branch of GC4bc, one fixed ratio address has physical incidence at most

\[
\boxed{DM.}
\]

Its protected-event height is bounded by the sum of its `DM` largest eligible operation weights.

The denominator-exception address `g(t)=0` has incidence at most

\[
\boxed{(\deg g)M.}
\]

### Proof

Multiply the parameter root bounds by the physical parameter multiplicity and apply the top-weight capacity theorem GC4an. QED.

## GC4be -- finite ratio-dictionary capacity -- PROVED

Let `A` be a finite dictionary of `J` finite ratio addresses. If `lambda` is nonconstant, the total incidence over all addresses in `A`, together with denominator exceptions, is at most

\[
\boxed{
JDM+(\deg g)M.
}
\]

Chartwise top-weight capacities may be summed using `DM` slots for each finite ratio and `(deg g)M` slots for the denominator class.

### Proof

Apply GC4bd separately to each fixed ratio and to the denominator equation. Summing remains valid even when the coarse upper bounds overlap. QED.

## GC4bf -- complete rational-chart continuation -- PROVED

Every rational line-following chart has one exact continuation:

1. `lambda` is nonconstant, and every fixed ratio address has incidence at most `DM`;
2. a finite ratio dictionary has the aggregate capacity from GC4be;
3. `lambda` is constant, giving one persistent homothetic line family with fixed ratio `alpha`;
4. two moving cells coincide identically;
5. denominator exceptions have incidence at most `(deg g)M`;
6. or one ratio, field, parameter, fibre, chart, alias, lineage, occurrence or weight record fails.

Thus persistent rational line following is split into root-bounded fixed-ratio addresses and one explicit constant-ratio concentration profile.

## Corrected GC5 frontier

Nondegenerate polynomial charts, denominator exceptions and nonconstant rational ratio addresses now have explicit capacities. Remaining work is to pay constant-ratio homothetic families, construct the actual finite ratio dictionaries and control eligible top weights for cleaning operations.

## Finite check

`scripts/verify_gc_rational_value_capacity.py` enumerates finite-field numerator/denominator polynomials, verifies the fixed-ratio equation, constant-ratio criterion and root bounds.
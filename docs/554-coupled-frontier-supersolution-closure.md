# Coupled-frontier supersolution closure

The additive ledger in `docs/543` assumes that the six frontier losses do not
feed back into one another.  Actual geometric adapters may create bounded
secondary obligations: shell choices can alter interaction cost, interaction
choices can alter boundary seams, and so on.  This chapter replaces the absence
of hidden losses by an explicit nonnegative coupling matrix.

Let `b in Q_>=0^6` be the six direct loss rows and let
`C in Q_>=0^(6 by 6)` record certified returned loss, with `C_(i,j)` the amount
charged to row `i` per unit realized loss in row `j`.

## 1. Monotone coupling closure

### Theorem PP3cok -- PROVED / FRONTIER COUPLING FIXED-POINT BOUND

Let `x^(0)=0`, and suppose returned losses are generated recursively with

```text
x^(n+1)<=b+Cx^(n).
```

If there is a nonnegative vector `y` with

```text
y>=b+Cy,
```

then `x^(n)<=y` for every finite propagation depth.  Every coordinatewise limit
of the propagation is also at most `y`; in particular, the least nonnegative
fixed point of `z=b+Cz`, when it exists, is at most `y`.

#### Proof

The zero initial vector is at most `y`.  If `x^(n)<=y`, nonnegativity of `C` and
the supersolution inequality give

```text
x^(n+1)<=b+Cx^(n)<=b+Cy<=y.
```

Induction proves the finite-depth bound, and coordinatewise limits preserve it. ∎

## 2. Finite strict-feasibility certificate

### Theorem PP3col -- PROVED / RATIONAL SUPERSOLUTION LEDGER

For rational `b`, `C`, and `y`, the inequalities

```text
y>=b+Cy,
sum_i y_i<M
```

form a finite exact certificate that every declared direct and returned loss fits
the global margin `M`.  No spectral or floating-point computation is required.
A failed certificate returns either one violated row or the exact aggregate
margin deficit.

#### Proof

The row inequalities are finite rational comparisons.  `PP3cok` bounds every
iterated returned loss by `y`; summing and comparing with `M` gives strict
feasibility. ∎

## 3. Adapter-derived six-row fixture

### Theorem PP3com -- PROVED / COUPLED SIX-FRONTIER FIXTURE

Take the direct rows, in boundary, Hall, threshold, prefix, shell, interaction
order,

```text
b=(7/120, 11723/524288, 1/24, 1/40, 1/40, 1/48).
```

The first five are the stored adapter rows of `docs/549--553`; the interaction
row is the exact `alpha<beta` optimum of `docs/542` with
`alpha=1/48`, `beta=1/32`.

Let the only nonzero couplings be

```text
C_(boundary,interaction)=1/200,
C_(Hall,boundary)=1/100,
C_(threshold,Hall)=1/120,
C_(prefix,threshold)=1/160,
C_(shell,prefix)=1/120,
C_(interaction,shell)=1/200.
```

Then

```text
y=(59,23,42,26,26,22)/1000
```

satisfies `y>=b+Cy`, and

```text
sum_i y_i=99/500,
1/4-sum_i y_i=13/250.
```

The balanced-integerization overhead `6/N` is smaller than this slack for every
`N>=116`.  Combining the adapter thresholds gives a common abstract threshold
`N>=120`.

#### Proof

Substitution verifies the six rational row inequalities.  Their sum is the
displayed value.  Direct comparison gives `6/116<13/250`, while the boundary row
requires `N>=120`. ∎

## 4. Stored exact audit

The audit `scripts/check_coupled_frontier_supersolution.py` verifies every
supersolution inequality using `Fraction` arithmetic, reconstructs the exact
normal-fan interaction optimum through length 300, proves the sharp rounding-only
threshold 116, and checks the coupled strict inequality for every length from 120
through 5000.

## 5. Prime-patching consequence

Cross-frontier feedback need not be absent.  It must instead be exposed as a
finite nonnegative coupling matrix with one rational supersolution below the
global margin.  The stored matrix shows that the six adapter fixtures remain
compatible with substantial slack and improves the abstract all-length threshold
from 361 to 120.  The coefficients are still synthetic; the final integration
frontier is to derive the actual coupling matrix and direct rows from the
prime-patching geometry.

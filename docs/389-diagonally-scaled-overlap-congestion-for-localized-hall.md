# Diagonally scaled overlap congestion for localized Hall transport

`docs/383` reduces localized Hall cuts to the Perron eigenvalue of the normalised
weighted-overlap Gram matrix, while `docs/386` bounds that eigenvalue by an
unscaled Gershgorin row sum.  This chapter allows a positive diagonal scaling.
The resulting criterion removes the square-root normalisation and gives an exact
variational form in terms of weighted neighbourhood congestion.

The statements are general.  No uniform congestion estimate for the prime-
patching transport graph is claimed.

## 1. Scaled overlap congestion

For a nonempty source subset `U`, retain

```text
D(x)    = v(N(x)),
O(x,x') = v(N(x) intersect N(x')),
H_U(x,x') = O(x,x')/sqrt(D(x)D(x')).
```

Let `a:U->(0,infinity)` be any positive scaling and define

```text
C_a(U)
 = max_(x in U)
   [sum_(x' in U) O(x,x') a(x')]
   /[D(x)a(x)].
```

The diagonal term `x'=x` contributes one.

### Theorem PP3bvd -- PROVED / SCALED PERRON OVERLAP CRITERION

For every positive scaling `a`,

```text
lambda(U) <= C_a(U),
```

where `lambda(U)` is the largest eigenvalue of `H_U`.  Moreover

```text
lambda(U) = inf_(a>0) C_a(U).
```

Consequently

```text
v(N(U)) >= S_1(U)/C_a(U)
```

and

```text
w(U)/v(N(U))
 <= C_a(U) w(U)/S_1(U).
```

#### Proof

Put `p(x)=sqrt(D(x))a(x)`.  Then

```text
(H_U p)(x)/p(x)
 = [sum_(x') O(x,x')a(x')]/[D(x)a(x)].
```

The Collatz--Wielandt inequality for the nonnegative matrix `H_U` gives
`lambda(U)<=max_x(H_Up)(x)/p(x)=C_a(U)`.  Its variational form gives equality
after taking the infimum over positive vectors; reducible overlap graphs are
handled componentwise or by a positive epsilon perturbation.  Substitute the
bound into `PP3bun`. ∎

Thus the spectral constant is exactly the least possible maximum weighted
overlap congestion after a positive reweighting of the sources.

## 2. Average target multiplicity

Choose the unscaled value `a(x)=1`.  Define

```text
C(U)
 = max_(x in U)
   [sum_(x' in U) O(x,x')]/D(x).
```

If

```text
n_U(y)=#{x in U:y in N(x)},
```

then double counting gives

```text
sum_(x' in U) O(x,x')
 = sum_(y in N(x)) v(y)n_U(y).
```

### Corollary PP3bve -- PROVED / AVERAGE TARGET-CONGESTION BOUND

For every nonempty source subset,

```text
lambda(U)
 <= C(U)
 = max_x
   [sum_(y in N(x)) v(y)n_U(y)]/D(x)
 <= max_(y in N(U)) n_U(y).
```

Therefore

```text
v(N(U)) >= S_1(U)/C(U).
```

#### Proof

The first inequality is `PP3bvd` with `a=1`.  The displayed identity follows by
interchanging the source and target sums.  The ratio is a capacity-weighted
average of `n_U(y)` over `N(x)`, so it is at most the largest target
multiplicity. ∎

This criterion has no square roots: it asks how many sources, on average, reuse
a target seen from one fixed source.

## 3. Inverse-support consequence

### Theorem PP3bvf -- PROVED / SCALED-CONGESTION INVERSE-SUPPORT ENVELOPE

Suppose a flaw with `s` compatible sources satisfies

```text
D(x) >= a_0 s w(x)
```

for every source.  If every nonempty source subset `U` admits a positive scaling
`a_U` with

```text
C_(a_U)(U) <= C_0,
```

then

```text
gamma <= C_0/(a_0 s).
```

It is sufficient, more concretely, that either

```text
C(U) <= C_0
```

for every subset, or that every reached target has multiplicity at most `C_0`
inside the subset.

#### Proof

The source-capacity hypothesis gives `S_1(U)>=a_0 s w(U)`.  Apply `PP3bvd` to
each subset and maximise the resulting Hall ratio.  The concrete conditions
follow from `PP3bve`. ∎

The Hall frontier is now a weighted congestion problem.  Microscopic subsets can
still be handled by exact overlap identities; mesoscopic subsets may be attacked
by choosing a useful source scaling, bounding average target multiplicity, or
proving that the overlap reuse graph has a bounded Perron load.

The next theorem identifier after this chapter is `PP3bvg`.

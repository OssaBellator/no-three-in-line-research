# Weighted second-moment and spectral overlap criteria for localized Hall transport

`docs/380` controls localized Hall cuts by the first two terms of weighted
inclusion--exclusion. That bound is exact for two sources, but for larger source
sets its right-hand side can become nonpositive even when the union has large
capacity. This chapter gives a positive second-moment alternative and a spectral
normal form for the same weighted neighbourhood geometry.

The statements are general. No asymptotic expansion estimate for the prime-
patching transport graph is claimed.

## 1. Weighted second-moment union bound

Let `X` be a finite source set, `Y` a finite target set, and let every target
`y` have positive capacity `v(y)`. For a source `x`, write `N(x)` for its target
neighbourhood and

```text
D(x) = v(N(x)).
```

For a nonempty source subset `U`, define the target multiplicity

```text
n_U(y) = #{x in U : y in N(x)}
```

and put

```text
S_1(U) = sum_y v(y) n_U(y) = sum_(x in U) D(x),
S_2(U) = sum_y v(y) n_U(y)^2.
```

Equivalently, with

```text
O(x,x') = v(N(x) intersect N(x')),
```

one has

```text
S_2(U)
 = sum_(x in U) D(x)
   + 2 sum_{{x,x'} subset U} O(x,x').
```

### Proposition PP3bul -- PROVED / WEIGHTED SECOND-MOMENT UNION BOUND

For every nonempty source subset `U`,

```text
v(N(U)) >= S_1(U)^2 / S_2(U).
```

Consequently,

```text
w(U)/v(N(U))
 <= w(U) S_2(U) / S_1(U)^2
```

for every positive source-weight function `w`.

#### Proof

All terms outside `N(U)` vanish. Weighted Cauchy--Schwarz gives

```text
S_1(U)^2
 = [sum_(y in N(U)) sqrt(v(y)) * sqrt(v(y)) n_U(y)]^2
 <= [sum_(y in N(U)) v(y)]
    [sum_(y in N(U)) v(y)n_U(y)^2]
 = v(N(U)) S_2(U).
```

Rearranging proves the union bound, and taking reciprocals proves the Hall-ratio
bound. ∎

Unlike the two-term Bonferroni lower bound, this estimate is always positive.
It is complementary rather than uniformly stronger: for two sources the exact
pair formula from `PP3bud` remains sharper.

## 2. Capacity density and overlap congestion

Define

```text
r(U)     = S_1(U)/w(U),
theta(U) = 2 sum_{{x,x'} subset U} O(x,x') / S_1(U).
```

Then `S_2(U)=S_1(U)[1+theta(U)]`.

### Corollary PP3bum -- PROVED / POSITIVE LOCALIZATION FACTORIZATION

Every nonempty source subset obeys

```text
w(U)/v(N(U)) <= [1+theta(U)]/r(U).
```

Hence a flaw with `s` compatible sources satisfies

```text
gamma <= C/s
```

whenever every nonempty source subset satisfies

```text
r(U) >= a s,
theta(U) <= theta_0,
```

with

```text
C = (1+theta_0)/a.
```

#### Proof

Substitute `S_2=S_1(1+theta)` into `PP3bul` and use
`r=S_1/w`. The uniform inverse-support statement follows by taking the maximum
over source subsets. ∎

This separates localized charge into two positive quantities: one-source
capacity density and aggregate overlap congestion.

## 3. Spectral overlap normal form

For a fixed nonempty subset `U`, form the weighted overlap Gram matrix

```text
G_U(x,x') = v(N(x) intersect N(x')),
```

where the diagonal is `G_U(x,x)=D(x)`. Let `Delta_U` be the diagonal matrix with
entries `D(x)`, and define

```text
H_U = Delta_U^(-1/2) G_U Delta_U^(-1/2).
```

This is positive semidefinite: it is the Gram matrix of the capacity-weighted
normalised incidence vectors. Write

```text
lambda(U) = largest eigenvalue of H_U.
```

### Theorem PP3bun -- PROVED / SPECTRAL LOCALIZED-HALL CRITERION

For every nonempty source subset `U`,

```text
v(N(U)) >= S_1(U)/lambda(U),
```

and therefore

```text
w(U)/v(N(U)) <= lambda(U) w(U)/S_1(U).
```

In particular, if a flaw with `s` compatible sources satisfies

```text
D(x) >= a s w(x)
```

for every source and

```text
lambda(U) <= Lambda
```

for every nonempty source subset, then

```text
gamma <= Lambda/(a s).
```

#### Proof

Let `d` be the vector with coordinates `sqrt(D(x))`. Then

```text
S_2(U) = d^T H_U d
       <= lambda(U) ||d||_2^2
       = lambda(U) S_1(U).
```

Insert this into `PP3bul` to obtain

```text
v(N(U)) >= S_1(U)^2/S_2(U) >= S_1(U)/lambda(U).
```

The ratio bound follows by reciprocation. Under the one-source hypothesis,
`S_1(U)>=a s w(U)`, so every subset ratio is at most `Lambda/(a s)`; maximise over
`U`. ∎

The criterion gives a concrete larger-subset target suggested by the exact
`m=10` scale profile. Microscopic subsets can still be handled by the exact
one-, two-, and bounded-order overlap formulas. Mesoscopic subsets can instead
be controlled by bounding the spectral norm of the normalised overlap Gram
matrix, or by proving an equivalent heat-kernel expansion estimate.

The theorem does not establish such a bound for the audited transport graph.

The next theorem identifier after this chapter is `PP3buo`.

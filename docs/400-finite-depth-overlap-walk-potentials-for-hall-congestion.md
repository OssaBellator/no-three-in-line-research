# Finite-depth overlap-walk potentials for Hall congestion

`docs/389` identifies localized Hall congestion with the Perron value of a
normalized overlap operator, and `docs/394` gives an exact two-sided Schur
variational principle.  This chapter supplies a canonical sequence of positive
source potentials obtained by repeated overlap walks.  Their congestion bounds
decrease monotonically to the exact spectral constant.

The statements are general.  They do not prove a uniform finite-depth bound for
the prime-patching transport graph.

## 1. The normalized overlap walk

Fix a nonempty source subset `U`.  Retain

```text
D(x)=v(N(x)),
O(x,x')=v(N(x) intersect N(x')).
```

Define

```text
K(x,x')=O(x,x')/D(x).
```

Because `O(x,x)=D(x)`, every diagonal entry of `K` is one.  The matrix `K` is
similar to the normalized Gram matrix

```text
H_U(x,x')=O(x,x')/sqrt(D(x)D(x')),
```

so both have the same spectral radius `lambda(U)`.

Start from the all-one potential

```text
a_0(x)=1
```

and iterate

```text
a_(t+1)=K a_t.
```

Every `a_t` is strictly positive.  Define the depth-`t` upper ratio

```text
c_t(U)=max_x a_(t+1)(x)/a_t(x).
```

### Theorem PP3bwl -- PROVED / MONOTONE PERRON-WALK CERTIFICATES

For every `t>=0`,

```text
lambda(U)<=c_(t+1)(U)<=c_t(U).
```

Moreover

```text
lim_(t->infinity) c_t(U)=lambda(U).
```

#### Proof

The Collatz--Wielandt inequality applied to the positive vector `a_t` gives

```text
lambda(U)<=max_x (K a_t)(x)/a_t(x)=c_t(U).
```

By definition,

```text
K a_t<=c_t a_t
```

coordinatewise.  Applying the nonnegative matrix `K` gives

```text
K a_(t+1)=K^2 a_t<=c_t K a_t=c_t a_(t+1),
```

so `c_(t+1)<=c_t`.

The support graph of `K` is undirected because `O` is symmetric.  On each
connected component, `K` is irreducible and has positive diagonal, hence is
primitive.  Perron--Frobenius theory gives convergence of the coordinate ratios
for `K^t 1` to that component's Perron value.  Taking the maximum over the block
diagonal components gives convergence to the largest component value, namely
`lambda(U)`. ∎

Thus the exact spectral optimum has a canonical decreasing hierarchy of finite
certificates; no optimization over arbitrary potentials is required to define
the hierarchy.

## 2. Explicit bounded-depth walk formula

### Proposition PP3bwm -- PROVED / ROOTED OVERLAP-WALK EXPANSION

For every `t>=1`,

```text
a_t(x_0)
 = sum_(x_1,...,x_t in U)
   product_(i=0)^(t-1)
   O(x_i,x_(i+1))/D(x_i).
```

Consequently `c_t(U)` depends only on normalized overlap walks of length at most
`t+1` rooted at one source.

At the first two depths,

```text
c_0(U)
 = max_x [sum_(x') O(x,x')]/D(x),
```

which is the average target-multiplicity bound of `PP3bve`, while, writing

```text
r(x)=sum_(x') O(x,x')/D(x),
```

one has

```text
c_1(U)
 = max_x
   [sum_(x') O(x,x') r(x')]
   /[D(x)r(x)].
```

#### Proof

Expand the matrix product `K^t 1` entry by entry.  The depth-zero and depth-one
forms are the cases `t=0` and `t=1` in the ratio definition. ∎

The first refinement therefore reweights a source according to the congestion
seen one overlap step beyond it.

## 3. Hall and inverse-support consequences

### Theorem PP3bwn -- PROVED / FINITE-DEPTH HALL ENVELOPE

For every nonempty source subset `U` and every depth `t`,

```text
v(N(U))>=S_1(U)/c_t(U)
```

and

```text
w(U)/v(N(U))
 <= c_t(U) w(U)/S_1(U).
```

If a flaw with `s` compatible sources satisfies

```text
D(x)>=a_0 s w(x)
```

for every source and every nonempty subset obeys

```text
c_t(U)<=C_t,
```

then

```text
gamma<=C_t/(a_0 s).
```

#### Proof

Use the potential `a_t` in `PP3bvd`; its scaled congestion is exactly

```text
C_(a_t)(U)=max_x (K a_t)(x)/a_t(x)=c_t(U).
```

The Hall inequalities follow from `PP3bvd`.  The source-capacity hypothesis gives
`S_1(U)>=a_0 s w(U)`, and maximizing over subsets proves the inverse-support
bound. ∎

### Corollary PP3bwo -- PROVED / BOUNDED-DEPTH CONGESTION WITNESS

If a proposed depth-`t` bound `c_t(U)<=C` fails, then some root source `x` has

```text
a_(t+1)(x)>C a_t(x).
```

Equivalently, the total normalized mass of length-`t+1` overlap walks rooted at
`x` exceeds `C` times the corresponding length-`t` mass.

Thus failure of a finite-depth Hall certificate is witnessed by one bounded-depth
rooted overlap-walk tree, rather than only by a global eigenvector.

#### Proof

This is the definition of the maximum ratio `c_t(U)`, together with the walk
formula `PP3bwm`. ∎

## 4. Revised Hall frontier

Microscopic subsets may be handled by exact pair and triple overlap formulas.
Mesoscopic subsets now admit a systematic finite-depth hierarchy:

```text
c_0>=c_1>=c_2>=...>=lambda(U).
```

A bounded depth that already falls below the required inverse-support constant
closes the subset.  Persistent failure yields a bounded overlap-walk witness at
that depth, providing a local object for geometric classification.

## 5. Finite diagnostic

The script

```bash
python scripts/check_overlap_walk_potentials.py
```

computes exact rational Collatz ratios on a stored three-source overlap system
and checks monotone upper and lower walk certificates through depth eight.

The next theorem identifier after this chapter is `PP3bwp`.

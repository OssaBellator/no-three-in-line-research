# Transient ordering of threshold permutation layers

`docs/521` decomposes an integral conservative threshold matrix into
collision-free permutation layers. The decomposition fixes full-period totals,
but geometric loads can still spike if the layers are executed in a poor order.
This chapter gives an exact transient sequencing certificate.

Let layers `1,...,M` be permutation matrices. Layer `i` has a rational
observable vector `z_i in Q^d`, and let

```text
z_bar=(1/M) sum_i z_i,       w_i=z_i-z_bar.
```

Thus `sum_i w_i=0`.

## 1. Exact subset sequencing dynamic program

### Theorem PP3clh -- PROVED / LAYER PREFIX-DISCREPANCY DP

For `S subseteq {1,...,M}`, define `D(S)` as the smallest possible maximum
`l_infinity` discrepancy over prefixes of an ordering of `S`. Then

```text
D(empty)=0,
D(S)=min_(i in S) max(
    D(S\{i}),
    ||sum_(j in S) w_j||_infinity).
```

The recurrence is exact. Stored last-layer choices reconstruct an optimal
ordering, and exhaustion of all smaller values is a finite lower certificate.

#### Proof

In an ordering whose last layer is `i`, every proper prefix belongs to the
ordering of `S\{i}`. The final prefix vector is `sum_(j in S)w_j`, independent
of which layer is last. Minimizing over `i` proves the recurrence. ∎

## 2. Additive-potential quotient

### Theorem PP3cli -- PROVED / PERMUTATION-OBSERVABLE QUOTIENT

Suppose an observable weight on source-action pair `(s,a)` has the form

```text
W_sa=r_s+c_a+W_tilde_sa.
```

Every permutation layer has the same contribution from `r_s+c_a`. Therefore
its centered vector `w_i` depends only on `W_tilde`; additive source and action
potentials disappear exactly from the transient sequencing problem.

#### Proof

A permutation layer uses every source once and every action once, so
`sum_s r_s+sum_a c_a` is independent of the permutation. Centering subtracts
this common quantity. ∎

## 3. Collision-free transient realization

### Theorem PP3clj -- PROVED / ORDERED PERMUTATION-LAYER CERTIFICATE

Executing the layers in an ordering certified by `PP3clh` preserves the exact
matrix totals and keeps every slot collision-free. At every prefix `t`, the
observable error from `t z_bar` is bounded by `D({1,...,M})` in `l_infinity`.

#### Proof

Reordering does not change the sum of the permutation matrices. Each individual
layer remains a matching between sources and action channels. The prefix bound
is precisely the definition of the centered partial sums optimized by
`PP3clh`. ∎

## 4. Stored exact fixture

The audit `scripts/check_steinitz_threshold_layer_ordering.py` uses the four
cyclic permutations of four actions and layer observable vectors

```text
(3,0), (0,3), (2,1), (1,2).
```

All 24 layer orders are checked. The exact minimum prefix discrepancy is one,
and exactly two orders attain it:

```text
(2,1,0,3), (3,0,1,2).
```

The four layers use every one of the sixteen source-action pairs exactly once.

## 5. Prime-patching consequence

A conservative threshold schedule can now be compiled into physical,
collision-free slots without sacrificing transient load control. The exact
sequencing problem is finite and automatically quotients irrelevant additive
potentials.

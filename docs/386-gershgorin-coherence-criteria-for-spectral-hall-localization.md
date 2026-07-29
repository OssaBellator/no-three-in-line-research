# Gershgorin and coherence criteria for spectral Hall localization

`docs/383` reduces larger localized Hall cuts to the largest eigenvalue of a
normalised weighted-overlap Gram matrix.  This chapter turns that spectral
quantity into directly combinatorial row-sum, pair-coherence, and overlap-degree
conditions.

The statements are general.  No uniform overlap estimate for the prime-patching
transport graph is claimed.

## 1. Normalised overlap row sums

For a nonempty source subset `U`, retain the notation

```text
D(x)       = v(N(x)),
O(x,x')    = v(N(x) intersect N(x')),
H_U(x,x')  = O(x,x') / sqrt(D(x)D(x')).
```

The diagonal entries of `H_U` are one.  Define the normalised overlap row sum

```text
R_U(x)
 = sum_(x' in U, x' != x)
   O(x,x') / sqrt(D(x)D(x')),

R(U) = max_(x in U) R_U(x).
```

### Theorem PP3buu -- PROVED / GERSHGORIN LOCALIZED-HALL CRITERION

For every nonempty source subset,

```text
lambda(U) <= 1 + R(U),
```

where `lambda(U)` is the largest eigenvalue from `PP3bun`.  Consequently

```text
v(N(U)) >= S_1(U)/(1+R(U))
```

and

```text
w(U)/v(N(U))
 <= [1+R(U)] w(U)/S_1(U).
```

In particular, if a flaw with `s` compatible sources satisfies

```text
D(x) >= a s w(x)
```

for every source and

```text
R(U) <= R_0
```

for every nonempty source subset, then

```text
gamma <= (1+R_0)/(a s).
```

#### Proof

The matrix `H_U` is symmetric, positive semidefinite, has diagonal one, and has
nonnegative off-diagonal entries.  Gershgorin's theorem places every eigenvalue
in a disk centred at one with radius at most `R(U)`, so
`lambda(U)<=1+R(U)`.  Substitute this into `PP3bun`.  Under the one-source
capacity hypothesis, `S_1(U)>=a s w(U)`, giving the final bound. ∎

This replaces an eigenvalue computation by a maximum normalised weighted-overlap
degree.

## 2. Pair coherence and sparse overlap graphs

Define the pair coherence on `U` by

```text
mu(U)
 = max_(x != x' in U)
   O(x,x')/sqrt(D(x)D(x')).
```

Let `Delta_overlap(U)` be the maximum degree of the graph joining two sources
when their target neighbourhoods have positive weighted intersection.

### Corollary PP3buv -- PROVED / COHERENCE AND OVERLAP-DEGREE BOUNDS

For `k=|U|`,

```text
R(U) <= (k-1) mu(U).
```

More sharply,

```text
R(U) <= Delta_overlap(U) mu(U).
```

Therefore

```text
w(U)/v(N(U))
 <= [1+(k-1)mu(U)] w(U)/S_1(U)
```

and also

```text
w(U)/v(N(U))
 <= [1+Delta_overlap(U)mu(U)] w(U)/S_1(U).
```

#### Proof

Each row contains at most `k-1` off-diagonal terms, each at most `mu(U)`.  If
only positive-overlap neighbours are counted, at most `Delta_overlap(U)` terms
are nonzero.  Apply `PP3buu`. ∎

The degree form can stay bounded on large subsets even when the crude factor
`k-1` grows.

## 3. A microscopic/mesoscopic split

### Theorem PP3buw -- PROVED / TWO-REGIME SPECTRAL REDUCTION

Fix a subset threshold `K`.  Suppose a flaw with `s` compatible sources satisfies

```text
D(x) >= a s w(x)
```

for every source.  Assume further that

```text
mu(U) <= mu_0       whenever |U| <= K,
R(U)  <= R_infty    whenever |U| > K.
```

Then

```text
gamma
 <= (1/(a s))
    max(1+(K-1)mu_0, 1+R_infty).
```

The same statement holds with `R_infty` replaced by
`Delta_infty mu_infty` whenever the large-subset overlap graph has maximum
degree at most `Delta_infty` and pair coherence at most `mu_infty`.

#### Proof

For `|U|<=K`, apply `PP3buv` and the bound
`R(U)<=(K-1)mu_0`.  For larger subsets, apply `PP3buu` with `R_infty` or the
sparse-degree specialization.  The weighted Hall optimum is the maximum over
all nonempty source subsets. ∎

The exact `m=10` count-maximizer profile suggests `K=6` as a natural microscopic
stress-test scale, but `docs/381` does not classify every flaw and therefore does
not justify fixing `K=6` in an asymptotic theorem.  The value of this reduction
is methodological: bounded-order overlap identities and spectral expansion can
be proved or audited independently and then combined by one maximum.

The next theorem identifier after this chapter is `PP3bux`.

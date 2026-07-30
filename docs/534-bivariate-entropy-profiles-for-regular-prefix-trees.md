# Bivariate entropy profiles for regular prefix trees

`docs/528` obtains the total asymptotic count for one regular-language prefix-tree
family. The same algebraic equation also records how typical legal trees split
between unary continuation steps and binary branching steps. This chapter gives
an exact bivariate profile and its entropy maximizer.

Let

```text
T(z;u,v)=z(1+uT+vT^2),
```

where `z` marks leaves, `u` marks unary continuation nodes, and `v` marks binary
branching nodes.

## 1. Exact profile coefficients

### Theorem PP3cmc -- PROVED / BIVARIATE LAGRANGE PROFILE

For `n>=1`, `j>=0`, and `a=n-1-2j>=0`,

```text
[z^n u^a v^j] T
 = (n-1)!/(a! j! (j+1)!).
```

All other coefficients vanish.

#### Proof

Lagrange inversion gives

```text
[z^n]T=(1/n)[t^(n-1)](1+ut+vt^2)^n.
```

Choose `a` linear factors, `j` quadratic factors, and therefore `j+1` constant
factors. The resulting multinomial coefficient divided by `n` is the displayed
integer. ∎

## 2. Entropy profile and typical proportions

### Theorem PP3cmd -- PROVED / LEGAL-TREE PROFILE ENTROPY

Let `j/n -> beta` with `0<beta<1/2`. Then

```text
(1/n) log [z^n u^(n-1-2j) v^j]T
 -> h(beta)
 = -2 beta log beta -(1-2 beta) log(1-2 beta).
```

The function is strictly concave and has its unique maximum at `beta=1/3`, where
`h(beta)=log 3`. Under the uniform distribution on legal trees with `n` leaves,
the terminal, unary, and binary proportions therefore concentrate
exponentially around `(1/3,1/3,1/3)`.

#### Proof

Apply Stirling's formula to `PP3cmc`; the three multinomial proportions tend to
`beta`, `1-2beta`, and `beta`. Differentiation gives
`h'(beta)=2 log((1-2beta)/beta)`, so the unique stationary point is `1/3`, and
`h''(beta)<0`. Strict concavity gives a positive entropy gap away from every
fixed neighborhood of `1/3`; summing only `O(n)` profiles preserves exponential
concentration. ∎

## 3. Finite coefficient oracle

### Theorem PP3cme -- PROVED / PROFILE-COUNT CERTIFICATE

The profile polynomial at fixed `n` is obtained from the finite list
`0<=j<=floor((n-1)/2)` using `PP3cmc`. Summing it recovers the exact scalar
coefficient of `T=z(1+T+T^2)`, while any prescribed unary or branching cap is
certified by a finite coefficient sum.

#### Proof

The support relation `a+2j=n-1` leaves only finitely many profiles. Their exact
integer sum is the univariate specialization `u=v=1`; restricting the sum
implements any finite profile constraint. ∎

## 4. Stored exact fixture

The audit `scripts/check_regular_prefix_entropy_profile.py` verifies the profile
formula and the scalar recurrence through 100 leaves. At `n=30`, the two peak
branching counts are `j=9` and `j=10`, each with coefficient

```text
168212023980,
```

and the total legal-tree count is `593742784829`. The exact entropy maximizer is
`beta=1/3`, matching the growth constant three from `PP3clm`.

## 5. Prime-patching consequence

The support-chord schedule family now has more than a total entropy estimate.
Exact coefficients quantify how many legal marker trees remain after imposing a
branching or continuation budget, and the entropy profile identifies the
asymptotically dominant geometry.

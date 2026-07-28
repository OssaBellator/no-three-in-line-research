# Weighted neighbourhood-overlap criteria for localized Hall transport

`docs/378` shows that 60 of the 68 constant-one failures in the exact `m=10`
transition window arise only on proper source subsets. This chapter converts
that observation into a structural expansion criterion expressed through
one-source neighbourhood capacities and pairwise weighted overlaps.

The statements are general. They do not prove that the required overlap bounds
hold uniformly in the prime-patching transport graph.

## 1. Weighted Bonferroni expansion

Let `X` be a finite source family and `Y` a finite target family. Give each
source a positive weight `w(x)` and each target a positive capacity `v(y)`. For
`A subset Y`, write

```text
v(A) = sum_{y in A} v(y),
```

and let `N(x)` be the target neighbourhood of source `x`. Define

```text
D(x)    = v(N(x)),
O(x,x') = v(N(x) intersect N(x')).
```

For `U subset X`, put `w(U)=sum_{x in U}w(x)` and
`N(U)=union_{x in U}N(x)`.

### Proposition PP3buc -- PROVED / WEIGHTED BONFERRONI HALL BOUND

For every nonempty source subset `U`,

```text
v(N(U))
 >= sum_{x in U} D(x)
    - sum_{{x,x'} subset U} O(x,x').
```

Consequently, whenever the right-hand side is positive,

```text
w(U)/v(N(U))
 <= w(U) /
    [sum_{x in U}D(x)-sum_{{x,x'} subset U}O(x,x')].
```

#### Proof

Apply the first two terms of the weighted inclusion-exclusion formula to the
sets `N(x)`. Target capacities are positive, so the first Bonferroni lower bound
gives the stated inequality. Dividing by the positive lower bound proves the
ratio estimate. ∎

## 2. Exact two-source obstruction

### Proposition PP3bud -- PROVED / PAIR-OVERLAP CHARACTERIZATION

For two distinct sources `x,x'`, the Hall ratio is exactly

```text
[w(x)+w(x')]
------------------------------- .
D(x)+D(x')-O(x,x')
```

At compatible-source count `s`, this pair violates the constant-one inverse-
support target `gamma <= 1/s` exactly when

```text
O(x,x')
 > D(x)+D(x') - s[w(x)+w(x')].
```

Thus every two-source localized violation is precisely an excessive weighted
neighbourhood-overlap event.

#### Proof

For two sets, inclusion-exclusion is exact:

```text
v(N(x) union N(x'))=D(x)+D(x')-O(x,x').
```

The displayed inequality is obtained by comparing the exact ratio with `1/s`
and cross multiplying positive quantities. ∎

This applies directly to the strongest localized violation recorded in
`docs/378`: its maximizing Hall subset has two sources. The remaining structural
question is therefore not merely how many targets each source reaches, but how
much weighted target capacity the two source neighbourhoods share.

## 3. A stratified inverse-support criterion

For each subset size `k`, define

```text
d_k = inf_{|U|=k}
      [sum_{x in U}D(x)]/w(U),

o_k = sup_{|U|=k}
      [sum_{{x,x'} subset U}O(x,x')]/w(U).
```

### Theorem PP3bue -- PROVED / LOCAL-OVERLAP REDUCTION

If `d_k>o_k` for every nonempty subset size `k`, then the weighted Hall optimum
satisfies

```text
gamma <= max_k 1/(d_k-o_k).
```

In particular, for a flaw with `s` compatible sources, the inverse-support bound

```text
gamma < C/s
```

follows if

```text
d_k-o_k > s/C
```

for every relevant subset size `k`.

A convenient sufficient specialization is the following. Suppose for constants
`a,b>0` that

```text
D(x) >= a s w(x)
```

for every source, and

```text
O(x,x') <= b[w(x)+w(x')]
```

for every distinct pair. Then every `k`-source subset obeys

```text
v(N(U))/w(U) >= a s - b(k-1),
```

and hence

```text
w(U)/v(N(U)) <= 1/[a s-b(k-1)]
```

whenever the denominator is positive.

#### Proof

`PP3buc` gives

```text
v(N(U))/w(U)
 >= [sum D(x)]/w(U)
    - [sum O(x,x')]/w(U)
 >= d_k-o_k.
```

Taking reciprocals and then the maximum over subset sizes proves the first
claim. Under the specialized hypotheses,

```text
sum_{{x,x'} subset U}[w(x)+w(x')]
 = (k-1)w(U),
```

so the Bonferroni lower bound becomes `a s-b(k-1)`. ∎

## 4. Consequence for the exact frontier

The exact transition audit already shows that full-neighbourhood capacity is not
enough: `15/17` of the failures are localized. `PP3buc--PP3bue` identify the
next finite and asymptotic statistic to audit:

1. one-source reached capacity `D(x)` relative to source weight;
2. pairwise weighted overlap `O(x,x')`;
3. the residual higher-order correction for larger Hall subsets.

The two- and three-source extremal witnesses in `docs/378` make the first two
nontrivial subset sizes immediately relevant. A successful all-scale theorem
could combine pair-overlap control for small subsets with heat-kernel or global
expansion control for larger subsets.

No finite numerical overlap census is claimed in this chapter.

The next theorem identifier after this chapter is `PP3buf`.

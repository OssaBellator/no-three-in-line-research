# Complementary slackness for randomized threshold kernels

`docs/437` gives a primal--dual linear program for source-randomized
multiplicity thresholds.  This chapter records the exact gap decomposition.
It turns every nonoptimal kernel into either an underpriced loaded target or a
source using an overpriced threshold class.

## 1. Primal and dual notation

For source `x` and threshold option `h`, let `P_(x,h)` be its retained-action
probability row.  A primal mixture `alpha_(x,h)` has target loads

```text
L_y=sum_(x,h) alpha_(x,h) P_(x,h)(y),
lambda=max_y L_y.
```

Let `z` be a target-price distribution.  Define

```text
c_(x,h)(z)=sum_y z_y P_(x,h)(y),
m_x(z)=min_h c_(x,h)(z),
Phi(z)=sum_x m_x(z).
```

## 2. Exact primal--dual gap

### Theorem PP3cbp -- PROVED / THRESHOLD GAP DECOMPOSITION

For every feasible primal mixture `alpha` and target-price distribution `z`,

```text
lambda-Phi(z)
 =sum_y z_y(lambda-L_y)
  +sum_(x,h) alpha_(x,h)[c_(x,h)(z)-m_x(z)].
```

Both terms on the right are nonnegative.

#### Proof

Because `sum_y z_y=1`,

```text
lambda-sum_y z_y L_y=sum_y z_y(lambda-L_y).
```

Also interchange the source, threshold, and target sums to obtain

```text
sum_y z_yL_y=sum_(x,h)alpha_(x,h)c_(x,h)(z).
```

Subtract `sum_x m_x(z)` and group by source. ∎

## 3. Exact complementary slackness

### Corollary PP3cbq -- PROVED / ACTIVE TARGETS AND CHEAP THRESHOLDS

A primal--dual pair is optimal with equal value exactly when

1. every target with `z_y>0` is saturated: `L_y=lambda`;
2. every threshold with `alpha_(x,h)>0` minimizes `c_(x,h)(z)` for its source.

#### Proof

The two nonnegative sums in `PP3cbp` vanish exactly under the two displayed
conditions. ∎

Thus an exact optimum has a finite certificate consisting only of active target
columns and price-minimizing threshold classes.

## 4. Quantitative obstruction localization

### Theorem PP3cbr -- PROVED / SUBOPTIMALITY MASS CERTIFICATE

If every used nonminimal threshold has reduced cost at least `delta` and their
total primal mass is `a`, then

```text
lambda-Phi(z)>=a delta.
```

Likewise, if target prices place mass `b` on columns with slack at least
`epsilon`, then the gap is at least `b epsilon`.

#### Proof

Keep only the indicated terms in the two nonnegative sums of `PP3cbp`. ∎

This gives a deterministic audit route: a failed mixed threshold kernel returns
one priced target slack or one source-threshold reduced-cost class carrying
positive mass.

## 5. Exact diagnostic

Run

```bash
python scripts/check_threshold_lp_complementary_slackness.py
```

The script verifies the exact mixed optimum `3/5`, deterministic optimum `5/6`,
uniform-price complementary slackness, the deterministic gap `7/30`, and a
nonuniform price vector exposing reduced-cost mass `2/15`.

The next theorem identifier after this chapter is `PP3cbs`.

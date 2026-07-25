# Exact joint trace budget for adaptive marked cascades

Proposition PP3aik records that adaptive sub-square-root cascade sizing is
compatible with marked credit-line self-recapture thinning.  The explicit choice
in PP3aih gives a sharper closed-form calculation.

Put

```text
W=sqrt(R)
```

and let the planned cascade depth satisfy `1<=d=o(W)`.  Choose

```text
q=floor(sqrt(W/d)).
```

Ignoring the harmless floor, the cumulative selected size is `dq=sqrt(dW)`, and
the total trace-failure scale over all `d` generations is

```text
d q^3/R = 1/sqrt(Wd).
```

Both quantities tend to their required limits simultaneously.  No additional
diagonal choice or unspecified slowly varying factor is needed.

## 1. Exact scale identities

### Proposition PP3aio -- PROVED

For

```text
q<=sqrt(W/d),
R=W^2,
```

one has

```text
dq/W <= sqrt(d/W)
```

and

```text
dq^3/R <= 1/sqrt(Wd).
```

Consequently, whenever `d=o(W)` and `W->infinity`,

```text
dq=o(W),
dq^3/R=o(1).
```

#### Proof

The first inequality is

```text
d sqrt(W/d)/W=sqrt(d/W).
```

For the second,

```text
d (W/d)^(3/2)/W^2
=
1/sqrt(Wd).
```

Both right-hand sides tend to zero under the displayed hypotheses. ∎

The floor in the definition of `q` only decreases the left-hand sides.

## 2. Joint zero-self-trace selection

Suppose every generation has an ambient marked layer of size

```text
Q_j>=cR
```

for one fixed `c>0`.  For generation `j`, the selected-credit off-diagonal trace
failure probability is at most

```text
K_0 q^3/Q_j
```

for one absolute or fixed host constant `K_0`, by PP3afp and the marked
source-valid thinning interface.

### Theorem PP3aip -- PROVED / CONDITIONAL ON UNIFORM MARKED HOST PREPARATION

Under the preceding hypotheses, all `d` generations admit source-valid marked
subbanks with zero selected-credit self-trace simultaneously with positive
probability.  Indeed the union-bound failure probability is at most

```text
(K_0/c) d q^3/R=o(1).
```

#### Proof

Condition sequentially on the history before generation `j`.  Uniform marked
host preparation gives the same conditional failure bound at every history in
the supported path.  Sum those conditional probabilities over `j` and apply
PP3aio.  Independence is unnecessary. ∎

The statement is a finite-horizon sequential selection theorem.  It does not
assume that all future hosts are fixed in advance.

## 3. Joint support cleaning

Suppose the support-degree exceptional event at generation `j` has conditional
probability `eta_j`, after the adaptive thresholds of PP3agc are imposed.

### Corollary PP3aiq -- PROVED

If the marked hosts are prepared uniformly so that

```text
sum_{j=1}^d eta_j=o(1),
```

then one may impose simultaneously along the whole cascade:

1. source-validity regularization;
2. zero selected-credit self-trace;
3. the support-degree cleaning conclusions required at each marked centre.

The total conditional failure probability is

```text
o(1)+(K_0/c)dq^3/R=o(1).
```

#### Proof

Use the union bound for the support exceptions and Theorem PP3aip for trace
failure.  Sequential conditioning again replaces independence. ∎

A sufficient uniform condition is `eta_j=o(1/d)`.

## 4. Relation to cumulative final support

The same explicit `q` gives

```text
S<=dq<=sqrt(dW)=o(W).
```

Therefore:

- final binary domain loss is `o(R)` by PP3aii;
- every failed final unary margin gives a star of degree `omega(W)` by PP3aij;
- selected-credit self-trace can be removed at all planned generations by
  PP3aip.

### Corollary PP3air -- PROVED

For every planned depth `d=o(W)`, the explicit subbank choice

```text
q=floor(sqrt(W/d))
```

simultaneously satisfies the cumulative final-support budget and the joint
selected-credit trace budget.  The only additional probabilistic requirement is
uniform summability of the marked source/support-host exceptional
probabilities.

Thus the cascade frontier is not blocked by an incompatibility between keeping
the final state below `sqrt(R)` and cleaning selected-credit traces at every
generation.

## 5. Finite diagnostic

The quantities in PP3aio are reported by

```text
scripts/check_adaptive_cascade_budget.py.
```

The stored example has `W=10^6`, `d=100`, and `q=100`, giving

```text
dq/W=0.01,
dq^3/R=0.0001.
```

Both inequalities are attained at the scale predicted by the exact formulas.
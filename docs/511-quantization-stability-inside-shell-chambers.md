# Quantization stability inside shell chambers

`docs/499` gives a rational chamber fan for multiparametric shell attenuation,
and `docs/505` rounds a feasible attenuation upward.  This chapter identifies a
finite denominator after which target quantization cannot change the active
shell chamber or its dual price.

Let a shell value function be represented by finitely many rational dual
vertices,

```text
F(b)=max_(y in Y) y dot b.
```

## 1. Unique-chamber perturbation radius

### Theorem PP3cjl -- PROVED / DUAL-GAP CHAMBER STABILITY

Suppose `y_*` is uniquely active at `b`.  Define

```text
gamma=min_(y!=y_*) (y_*-y) dot b > 0,
L=max_(y!=y_*) ||y_*-y||_1.
```

If `||delta||_infinity < gamma/L`, then `y_*` remains uniquely active at
`b+delta`.

#### Proof

For every competitor `y`,

```text
(y_*-y) dot (b+delta)
 >= gamma-||y_*-y||_1 ||delta||_infinity
 > 0.
```

Thus every old strict dominance inequality remains strict. ∎

## 2. Denominator threshold

### Theorem PP3cjm -- PROVED / CHAMBER-PRESERVING TARGET QUANTIZATION

Let `b^(M)=ceil(Mb)/M` componentwise.  Since
`||b^(M)-b||_infinity<1/M`, every integer

```text
M > L/gamma
```

preserves the unique active dual vertex.  On all such denominators,

```text
F(b^(M))=y_* dot b^(M)
```

with the same exact marginal shell prices.

#### Proof

Apply `PP3cjl` to the componentwise rounding error. ∎

## 3. Finite chamber audit

### Theorem PP3cjn -- PROVED / QUANTIZED-CHAMBER WITNESS

A chamber-preservation claim is certified by the active dual vertex, its gap,
the `l_1` radii to all competitors, and the quantized target.  Failure returns a
specific competing dual vertex that ties or overtakes the claimed chamber.

#### Proof

The finite dominance inequalities are necessary and sufficient for activity in
the max-of-affine representation. ∎

## 4. Stored exact fixture

The audit `scripts/check_shell_chamber_quantization_stability.py` uses

```text
F(a,b,c)=max(a,b,c,(a+b+c)/2)
```

at `(3/5,1/2,2/5)`.  The central dual `(1/2,1/2,1/2)` has gap `3/20`; its maximum
`l_1` distance to a coordinate dual is `3/2`.  Hence every denominator
`M>=11` is certified to remain central.  At `M=11`, the quantized target is
`(7/11,6/11,5/11)`.  Auditing all denominators through 100 finds only the
expected denominator-two tie.

## 5. Prime-patching consequence

Once a shell target lies a positive rational distance inside one chamber,
finite quantum implementation eventually preserves not only feasibility but the
entire active dual explanation and its marginal prices.

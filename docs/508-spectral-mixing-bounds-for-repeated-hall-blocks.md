# Spectral mixing bounds for repeated Hall blocks

`docs/502` accelerates exact xor convolution by Walsh transformation.  This
chapter extracts a uniform tail bound from the same spectrum, so a long repeated
Hall tag has a certified reverse-load envelope without computing every power.

Let `G=(Z/2Z)^r`, let `b:G->Z_+` be one block's compatibility-count function,
and let `B=sum_s b(s)`.  Write `f=b/B` and use the Walsh transform

```text
fhat(chi)=sum_(s in G) f(s) chi(s).
```

## 1. Exact repeated-block spectrum

### Theorem PP3cjc -- PROVED / WALSH POWER FORMULA

For every `n>=1`, the syndrome distribution after `n` independent repeated
blocks is `f^(*n)`, and

```text
widehat(f^(*n))(chi)=fhat(chi)^n.
```

The exact integer count at syndrome `s` is

```text
B^n |G|^(-1) sum_chi fhat(chi)^n chi(s).
```

#### Proof

Xor addition makes repeated compatibility the group convolution of the block
functions.  Characters diagonalize convolution, and Walsh inversion gives the
stated count. ∎

## 2. Uniform spectral tail

### Theorem PP3cjd -- PROVED / HALL-SYNDROME MIXING ENVELOPE

For every syndrome `s`,

```text
|f^(*n)(s)-1/|G||
 <= |G|^(-1) sum_(chi!=1) |fhat(chi)|^n.
```

If `rho=max_(chi!=1)|fhat(chi)|<1`, then the right side is at most
`(|G|-1)rho^n/|G|`.

#### Proof

The trivial character contributes exactly `1/|G|` in Walsh inversion.  Apply
the triangle inequality to the remaining characters, then bound each magnitude
by `rho^n`. ∎

## 3. Reverse-load horizon

### Theorem PP3cje -- PROVED / FINITE SPECTRAL LOAD CERTIFICATE

Suppose a compatible syndrome class contributes reverse load at most its
probability divided by a residual Hall degree `d`.  Then after `n` blocks every
syndrome has load at most

```text
1/(d|G|) + [1/(d|G|)] sum_(chi!=1)|fhat(chi)|^n.
```

The least `n` at which this expression meets a prescribed rational tolerance is
an exact finite mixing horizon.  Failure returns a nontrivial character with
excess spectral magnitude or a syndrome attaining the larger exact load.

#### Proof

Divide the probability bound of `PP3cjd` by `d`.  All Walsh coefficients and
powers are finite rational numbers for a finite integer block. ∎

## 4. Stored exact fixture

The audit `scripts/check_spectral_hall_mixing_bounds.py` uses the rank-three
block count vector

```text
(2,2,1,1,1,1,1,1).
```

Its Walsh spectrum is `(10,0,2,0,2,0,2,0)`, so the nontrivial radius is `1/5`.
The exact maximum deviations from uniformity are

```text
3/40, 3/200, 3/1000, 3/5000, 3/25000, ...
```

The sharp one-percent horizon is three blocks.  With residual Hall degree
`20`, the resulting load envelope is `4/625`.  Exact convolution and Walsh
reconstruction agree through power twelve.

## 5. Prime-patching consequence

Repeated Hall-color protection now has a closed spectral tail.  Once a local
block has nontrivial Walsh radius below one, arbitrarily many repetitions have
an exponentially shrinking ambiguity term and a finite exact stopping horizon.

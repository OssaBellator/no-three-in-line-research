# Noncommuting transfer products for Hall transport

The Fourier arguments in `docs/520` exploit convolution and hence commuting
syndrome operators. Position-dependent Hall gadgets can instead act by
noncommuting transfer matrices. A periodic product still gives an exact finite
mixing and reverse-load certificate.

Let `S` be a finite syndrome-state set. Block `t` has a nonnegative integer
transfer matrix `M_t`; entry `(x,y)` counts the local completions carrying state
`x` to state `y`. Assume every row of `M_t` has the same sum `d_t`.

## 1. Exact transfer-product counting

### Theorem PP3cle -- PROVED / NONCOMMUTING HALL PRODUCT

For an initial count row vector `v_0`, the compatible syndrome counts after
blocks `1,...,n` are exactly

```text
v_n=v_0 M_1 M_2 ... M_n.
```

Sparse predecessor tables reconstruct a compatible local-block sequence for
every positive final entry. No commutativity assumption is required.

#### Proof

Matrix multiplication sums over the intermediate syndrome state and multiplies
the independent local completion counts. Induction on the number of blocks
gives the formula. Recording one positive predecessor at each multiplication
step reconstructs a witness. ∎

## 2. Periodic spectral mixing

### Theorem PP3clf -- PROVED / PERIOD-PRODUCT SPECTRAL TAIL

Suppose the block sequence has period `p`, and put

```text
K=M_1...M_p,       D=d_1...d_p.
```

If `K/D` is primitive and diagonalizable, with stationary row distribution
`pi` and non-Perron eigenvalue modulus at most `rho/D<1`, then an exactly
computable constant `C` satisfies

```text
||v_0 K^m/D^m - (sum v_0) pi||_infinity
    <= C (rho/D)^m.
```

For a non-diagonalizable product, the same finite Jordan computation gives a
polynomial factor times `(rho/D)^m`.

#### Proof

Separate the Perron rank-one projection from the remaining spectral
projections in the exact Jordan decomposition of `K`. The Perron term is
`D^m pi`; every other Jordan block contributes its eigenvalue to the `m`th
power, multiplied by a polynomial of degree below the block size. ∎

## 3. Reverse-load stopping rule

### Theorem PP3clg -- PROVED / TRANSFER-MIXING HALL HORIZON

If the residual Hall degree is `d`, then after `mp` blocks the reverse load into
one target is at most

```text
(max_s (v_0 K^m)_s) / (d D^m sum v_0).
```

The first `m` at which the spectral envelope or the exact product meets a target
cap is a finite certified mixing horizon.

#### Proof

The numerator is the largest compatible syndrome class. At most that fraction
of colors can use one syndrome, and Hall degree `d` divides its load among at
least `d` targets. ∎

## 4. Stored exact fixture

The audit `scripts/check_noncommuting_hall_transfer_products.py` uses

```text
A = ((2,1,0),(0,2,1),(1,0,2)),
B = ((2,1,0),(1,0,2),(0,2,1)).
```

They have row sum three and do not commute. Their period product is

```text
K=AB=((5,2,2),(2,2,5),(2,5,2))
```

with eigenvalues `9,3,-3`. Starting from syndrome zero, after `m` periods the
counts are exactly

```text
((9^m+2*3^m)/3, (9^m-3^m)/3, (9^m-3^m)/3).
```

The maximum deviation from uniformity is `2/3^(m+1)`. Four periods, or eight
blocks, are necessary and sufficient for one-percent uniformity. With Hall
degree twelve, the exact load at that horizon is `83/2916`.

## 5. Prime-patching consequence

Localized Hall transport may now alternate genuinely different finite gadgets.
The long product is compressed to one period matrix, while exact predecessors
retain a concrete geometric decoding witness.

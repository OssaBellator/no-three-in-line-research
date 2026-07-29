# Heterogeneous Fourier products for Hall transport

`docs/514` treats repeated copies of one q-ary Hall syndrome block.  Actual
prime-patching layers may alternate several block types.  Convolution on a finite
abelian syndrome group still diagonalizes the complete heterogeneous product.

Let `G` be a finite abelian group.  Block `t` has a nonnegative count kernel
`K_t:G->Z_{>=0}` with total `M_t`; its normalized kernel is `mu_t=K_t/M_t`.

## 1. Exact heterogeneous powering

### Theorem PP3ckm -- PROVED / CHARACTERWISE PRODUCT FORMULA

For any sequence of blocks `1,...,n`, the compatible-syndrome count vector is

```text
K_1 * K_2 * ... * K_n.
```

For every character `chi` of `G`,

```text
hat K(chi)=product_t hat K_t(chi).
```

Fourier inversion therefore reconstructs every exact syndrome count without
enumerating compatible block assignments.

#### Proof

Syndromes add in `G`, so assignment counts convolve.  Characters turn convolution
into multiplication.  Fourier inversion on the finite group is exact. ∎

## 2. Nonstationary mixing bound

### Theorem PP3ckn -- PROVED / PRODUCT SPECTRAL TAIL

Put

```text
rho_t=max_(chi nontrivial) |hat mu_t(chi)|.
```

Then the normalized product distribution `nu_n` satisfies

```text
||nu_n-uniform||_infinity
 <= (|G|-1)/|G| product_(t=1)^n rho_t.
```

In particular a periodic list of heterogeneous blocks mixes exponentially at the
geometric mean of its nontrivial character products.

#### Proof

Fourier inversion expresses the deviation at one syndrome as the average of the
nontrivial Fourier coefficients.  Each coefficient is a product and is bounded
by `product rho_t`; summing the `|G|-1` terms gives the inequality. ∎

## 3. Reverse-load horizon

### Theorem PP3cko -- PROVED / HETEROGENEOUS HALL STOPPING RULE

If the residual geometric Hall degree is `d`, then after `n` blocks the reverse
load of one observed syndrome is at most

```text
(1/|G|+(|G|-1)/|G| product_t rho_t)/d.
```

The first `n` at which this expression meets a requested cap is a certified
finite mixing horizon.  Exact Fourier inversion can replace the envelope by the
sharp count whenever required.

#### Proof

The largest syndrome probability is bounded by uniform mass plus the preceding
`l_infinity` deviation.  At most that fraction of compatible colors can route to
one target, and division by Hall degree gives the load. ∎

## 4. Stored exact fixture

The audit `scripts/check_heterogeneous_hall_fourier_products.py` alternates two
kernels on `Z/3Z`:

```text
A=(5,1,1),   B=(3,2,2).
```

Both have total seven; their nontrivial count eigenvalues are four and one.  The
power-seven count vector is

```text
(274685,274429,274429).
```

Seven blocks are necessary and sufficient for deviation at most `1/4000`.  With
Hall degree 18 the exact maximum load is `274685/14823774`.

## 5. Prime-patching consequence

Hall-color transport may now switch among several local coding gadgets without
losing a closed-form ambiguity certificate.  The only long product data are the
nontrivial character eigenvalues of the finite block types.

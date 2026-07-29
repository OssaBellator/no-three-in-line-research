# Q-ary Fourier mixing for Hall syndromes

`docs/502` diagonalizes repeated binary syndrome blocks by Walsh characters, and
`docs/508` turns the nontrivial spectrum into a stopping rule. Hall tags over
`F_q` require the same mechanism on a general finite additive syndrome group.

Let `G` be a finite abelian group, let `mu:G->[0,1]` be a rational block
syndrome distribution, and write `mu^{*n}` for its `n`-fold convolution.
Characters are denoted by `chi` and the normalized Fourier transform by

```text
hat(mu)(chi)=sum_(g in G) mu(g) chi(g).
```

## 1. Exact diagonalization

### Theorem PP3cju -- PROVED / FINITE-ABELIAN SYNDROME FOURIER FORMULA

For every character `chi`,

```text
hat(mu^{*n})(chi)=hat(mu)(chi)^n.
```

Consequently every exact syndrome count after `n` repeated blocks is recovered
by finite Fourier inversion.

#### Proof

Characters turn convolution into multiplication. Iterating gives the power
formula, and character orthogonality gives inversion. ∎

## 2. Uniformity tail and Hall load

### Theorem PP3cjv -- PROVED / Q-ARY SPECTRAL MIXING BOUND

Let

```text
rho=max_(chi nontrivial) |hat(mu)(chi)|.
```

Then for every syndrome `s`,

```text
|mu^{*n}(s)-1/|G|| <= (|G|-1) rho^n / |G|.
```

If every surviving color has residual Hall degree at least `d`, the reverse load
is at most

```text
[1/|G|+(|G|-1)rho^n/|G|]/d.
```

#### Proof

Fourier inversion separates the trivial character, which contributes `1/|G|`.
The remaining `|G|-1` terms each have modulus at most `rho^n/|G|`. Division by
the residual degree gives the Hall load bound. ∎

## 3. Stored ternary fixture

### Theorem PP3cjw -- PROVED / NINE-SYNDROME EXACT AUDIT

The audit `scripts/check_qary_hall_fourier_mixing.py` uses
`G=F_3^2` and integer block multiplicities

```text
mu(0)=3,
mu(+-e_1)=mu(+-e_2)=1,
```

of total mass seven. The Fourier magnitudes are exactly `7,4,1`; after
normalization the nontrivial radius is `4/7`. The zero-syndrome count after `n`
blocks is

```text
[7^n+4*4^n+4]/9.
```

Exact convolution shows that seven blocks are necessary and sufficient for
one-percent `l_infinity` distance from uniformity. At Hall degree 18, the exact
seven-block maximum load is `32929/4941258`.

## 4. Prime-patching consequence

Nonbinary algebraic Hall tags now have the same scalable stopping certificate as
binary tags: a finite character table, an exact convolution power, and an
explicit reverse-load horizon.

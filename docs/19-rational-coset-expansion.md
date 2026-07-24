# Rank-zero rational expansion for the Möbius transition

The preceding inverse theory reduces low-complexity cycle cores to subgroup cosets and coset progressions. This chapter proves that a full subgroup coset of order at least three cannot remain a single subgroup coset after applying the normalized Möbius transition

\[
F_r(c)=\frac{c(1-c)}{r-c},
\qquad r\in\mathbb F_p^*\setminus\{1\}.
\]

This is an exact rank-zero case of the rational-expander target.

## 1. Full-coset non-preservation

Let `H<=F_p^*` have order `h`, let `x in F_p^*`, and put

\[
C=xH.
\]

Assume `r notin C`, so `F_r` is defined on `C`. If `1 in C`, then `0 in F_r(C)`, and therefore `F_r(C)` is not contained in a multiplicative coset. Thus the only nontrivial case also has `1 notin C`.

### Theorem I9 — PROVED

If

\[
h\ge3,
\]

then there is no `y in F_p^*` such that

\[
\boxed{F_r(xH)\subseteq yH.}
\]

Equivalently, the rational image of a full `H`-coset meets at least two distinct `H`-cosets.

### Proof

Suppose for contradiction that

\[
F_r(xH)\subseteq yH.
\]

Set

\[
A=x^h,
\qquad B=y^h.
\]

The elements of `xH` are precisely the `h` distinct roots of

\[
T^h-A.
\]

For every such root `c`, the containment assumption gives

\[
F_r(c)^h=B.
\]

Hence

\[
c^h(1-c)^h-B(r-c)^h=0.
\]

Therefore the polynomial

\[
P(T)=T^h(1-T)^h-B(r-T)^h
\]

is divisible by `T^h-A`.

Modulo `T^h-A`, the polynomial `P` has the same remainder as

\[
A(1-T)^h-B(r-T)^h.
\]

For each `1<=j<=h-1`, the coefficient of `T^j` in that remainder is

\[
(-1)^j\binom hj
\left(A-Br^{h-j}\right).
\]

Because `h` divides `p-1`, one has `h<p`; hence every binomial coefficient `binom(h,j)` with `0<j<h` is nonzero modulo `p`.

Divisibility forces all these coefficients to vanish. Taking `j=h-1` and `j=h-2` gives

\[
A=Br,
\qquad A=Br^2.
\]

Since `A,B,r` are nonzero, this implies `r=1`, contrary to hypothesis. `square`

## 2. Exact order-two exception

The order-two case is the only possible nontrivial exception.

### Theorem I10 — PROVED

Let

\[
H=\{1,-1\}.
\]

Then

\[
F_r(xH)
\]

is contained in one `H`-coset if and only if

\[
\boxed{x^2=r.}
\]

In that exceptional case,

\[
\boxed{F_r(x)=F_r(-x)=-1,}
\]

so the image is the singleton `{-1}`.

### Proof

If the two image values lie in one `H`-coset, their ratio is `1` or `-1`.

The equation

\[
F_r(-x)=-F_r(x)
\]

reduces to

\[
2x(r-1)=0,
\]

which is impossible for odd `p`, nonzero `x`, and `r ne 1`.

The equation

\[
F_r(-x)=F_r(x)
\]

reduces to

\[
x^2=r.
\]

When this holds,

\[
F_r(x)=\frac{x(1-x)}{x^2-x}=-1
\]

and the same is true for `-x`. `square`

## 3. Consequence for alternating closure

### Corollary I11 — PROVED

Suppose an inverse step produces a full multiplicative coset `xH` of normalized anchor ratios.

- If `|H|>=3`, the next ratio set `F_r(xH)` necessarily occupies at least two `H`-cosets.
- If `|H|=2`, failure of quotient expansion is possible only for the explicitly classified square-root configuration `x^2=r`.

Thus a rank-zero alternating core cannot remain rank-zero with the same quotient support indefinitely, except through an order-two exceptional orbit.

This does not yet prove termination: two or more target cosets may later recombine, and a union of several source cosets can have overlapping images. It does, however, rule out the simplest persistent PFR obstruction.

## 4. Remaining rational inverse target

### Target I12 — OPEN

Classify sets `C` with bounded multiplicative doubling for which `F_r(C)` also has bounded multiplicative doubling.

Theorems I9--I11 solve the exact full-coset-to-one-coset case. The next useful levels are:

1. prove quantitative expansion when `C` has density greater than `1/2` in one large subgroup coset;
2. bound how many `H`-cosets can contain `F_r(C)` when `C` is a union of `m` full `H`-cosets;
3. combine those bounds with the coset-union absorber bank from Theorem I6;
4. classify all order-two exceptional chains.

Finite-field sum-product estimates for rational functions are natural external tools for the quantitative versions, but the exact full-coset theorem above is elementary.
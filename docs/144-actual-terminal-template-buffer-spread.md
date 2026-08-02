# Actual terminal template census and buffer-cycle spread

PX341--PX345 show that the actual product construction has base degree one and
that every trajectory residual has order at most two.  This chapter makes the
remaining labelled templates explicit and upgrades the buffer escape from one
existence statement to a quadratic-size bank with support-sensitive spread.

The bank estimate is useful because terminal collateral is no longer sampled
from a constant family.  It is averaged over two fresh ambient labels.  A
certificate depending on one buffer variable receives one factor `1/n`; a
certificate depending on both receives `1/n^2`.

## 1. Exact order-two trajectory templates

Let `Q={u,v}` be an acyclic historical-union residual.  The two off-diagonal
cells are

\[
\alpha=u\to v,\qquad \beta=v\to u.
\]

They are forbidden by the opposite-layer base matching `P` or by the releasable
historical union `H`.

### Theorem PX346 -- PROVED

Up to exchanging `u` and `v`, there are exactly two actual order-two residual
templates.

1. **Base-saturated:** both `alpha` and `beta` belong to `P`.
2. **Mixed:** one of `alpha,beta` belongs to `P` and the other belongs to `H`.

There is no third case.

### Proof

Both off-diagonal cells must be forbidden because the allowed digraph on `Q`
is empty.  The historical union is acyclic, so it cannot contain both opposite
arcs.  Hence at least one arc lies in `P`.  Since the two opposite arcs form a
partial matching, `P` may contain either one or both.  Relabelling identifies
the two one-base-one-history orientations. \(\square\)

Thus the abstract extreme-ray family of PX339 is unnecessary on the actual
trajectory branch: its base/historical template space has two unlabelled
order-two members and the trivial order-one member.

## 2. Quadratic buffer banks

Use the notation of PX342--PX343.  Put

\[
\Delta=\Delta_{\rm ord},
\qquad
d_*=\mathfrak d(n).
\]

For one core label `u`, let `Omega_1(u)` be the ordered pairs `(a,b)` giving the
allowed noncollinear three-cycle

\[
u\to a\to b\to u.
\]

For two core labels `u,v`, let `Omega_2(u,v)` be the ordered pairs `(a,b)`
giving the allowed internally triple-free four-cycle

\[
u\to a\to v\to b\to u.
\]

### Theorem PX347 -- PROVED

The bank sizes satisfy

\[
\boxed{
|\Omega_1(u)|
\ge
(n-\Delta)(n-2\Delta-2-2d_*)
}
\]

and

\[
\boxed{
|\Omega_2(u,v)|
\ge
(n-2\Delta-2)(n-2\Delta-5-4d_*).
}
\]

In particular, if

\[
\boxed{
n\ge4\Delta+10+8d_*,
}
\]

then both banks have size at least `n^2/4`.

### Proof

For `Omega_1`, there are at least `n-Delta` choices for the first allowed
buffer `a`.  For each `a`, the common allowed-neighbour intersection for `b`
has size at least `n-2Delta`; remove `u,a` and at most `2d_*` hyperbola
solutions from PX342.

For `Omega_2`, the first common-neighbour intersection has size at least
`n-2Delta`; remove `u,v`.  For each `a`, the second common-neighbour
intersection has the same initial size; remove `u,v,a`, the two unique
line-intersection exceptions, and the at most `4d_*` solutions to the two
nonzero product equations of PX343.  The simplified lower bound follows by
making each factor at least `n/2`. \(\square\)

## 3. Buffer-variable spread

A prospective inserted cell in a buffer cycle determines either:

- the first buffer label `a`;
- the second buffer label `b`; or
- both labels.

For a compatible collection `E` of prospective cells, let `nu(E)` be the
number of buffer labels determined by `E`, so `nu(E) in {1,2}`.

### Theorem PX348 -- PROVED

Under the simplified size hypothesis of PX347, the uniform measure on either
buffer bank satisfies

\[
\boxed{
\Pr(E\subseteq W_{a,b})
\le
\frac4{n^{\nu(E)}}.
}
\]

In particular, every prescribed spoke cell has probability at most `4/n`, and
every event fixing both buffer labels has probability at most `4/n^2`.

### Proof

The total bank has at least `n^2/4` states.  Fixing one buffer label leaves at
most `n` ordered pairs; fixing both leaves at most one.  Divide by the bank
lower bound. \(\square\)

This is a support-excess estimate in the buffer variables rather than the
endpoint labels of the original rematching block.

## 4. Terminal collateral transfer

Let `C_1` be a weighted family of prospective certificates whose occurrence
determines exactly one buffer label, and let `C_2` be the family determining
both.  Write their total weights as `W_1^buf` and `W_2^buf`.

### Theorem PX349 -- PROVED

For a uniform valid buffer cycle,

\[
\boxed{
\mathbb E T_{\rm ext}
\le
\frac{4W_1^{\rm buf}}n
+
\frac{4W_2^{\rm buf}}{n^2}.
}
\]

The internal rank-three contribution is identically zero.

### Proof

Apply PX348 certificate by certificate and sum the weights.  PX342--PX343
exclude every triple consisting of three inserted cells. \(\square\)

The estimate remains valid after deleting any further buffer states, with the
constant multiplied by the reciprocal retained density.

## 5. Direct terminal sign criterion

### Corollary PX350 -- PROVED

Suppose the core carries `s in {1,2}` injectively assigned old certificates.
If

\[
\boxed{
s
>
\frac{4W_1^{\rm buf}}n
+
\frac{4W_2^{\rm buf}}{n^2},
}
\]

then some valid buffer cycle strictly lowers the full triple potential.

Otherwise the terminal obstruction has explicit normalized concentration:

\[
\boxed{
\frac{W_1^{\rm buf}}n
+
\frac{W_2^{\rm buf}}{n^2}
\ge
\frac{s}{4}.
}
\]

The first summand is rank-one/one-buffer concentration and the second is a
two-buffer pair-line or mixed-shadow concentration.  These are precisely the
geometric sectors decoded by PX228--PX262 and PX319--PX323.

### Proof

Every bank state destroys at least `s` designated old certificates and has no
internal creation.  PX349 bounds average external creation.  A strict
expectation gap gives an improving state.  Negating the gap gives the displayed
concentration alternative. \(\square\)

Thus the actual terminal frontier is no longer an arbitrary finite cone.  It is
a quantitative dichotomy between immediate two-buffer improvement and one of
the already named rank-one/rank-two geometric concentrations.

## 6. Verification

Run

```bash
python scripts/verify_product_buffer_cycle_spread.py
```

The verifier enumerates random one- and two-core banks, checks the exact bank
lower bounds before simplification, verifies the one-/two-buffer cylinder
multiplicities, and confirms the expectation transfer on random weighted
certificate families.

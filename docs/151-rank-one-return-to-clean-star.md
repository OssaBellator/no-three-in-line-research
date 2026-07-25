# Rank-one terminal returns force large clean stars

PX356--PX385 leave only two persistent rank-one return types after the exact
buffer-bank cover is expanded:

1. a one-variable coordinate family with at most `n` candidate centres;
2. a two-variable generic family with at most `n^2` candidate centres.

The weighted cover lower bounds scale with the parent destruction `D`.
Averaging over the candidate centres therefore forces one centre of rank-one
weight `Omega(D)`.  PX228 converts that weight into an endpoint-disjoint clean
star of order `Omega(D/K)`.

Combined with the weighted-return amplification of PX363 and the incidence
caps of PX366--PX369, this gives a bounded return depth from the actual
terminal buffer bank back to the established large-block clean-star/loaded-line
interface.

## 1. Coordinate rank-one averaging

Let `C_coord` be one exact one-variable coordinate rank-one family from PX354.
For every candidate centre `f`, let

\[
\mu(f)
=
|\{\{z,z'\}:f,z,z'\text{ are collinear fixed-point blockers}\}|.
\]

The family contains at most `n` candidate centres and

\[
|C_{\rm coord}|=\sum_f\mu(f).
\]

### Theorem PX386 -- PROVED

If the coordinate family is the weighted one-variable outcome of PX357 for a
bank of designated destruction `D`, then some candidate centre satisfies

\[
\boxed{
\mu(f)\ge\frac{D}{48}.
}
\]

Consequently, under selected-line occupancy bound `K`, that centre has an
endpoint-disjoint clean star of order at least

\[
\boxed{
\frac{D}{48K}.
}
\]

### Proof

PX357 gives

\[
|C_{\rm coord}|\ge\frac{Dn}{48}.
\]

There are at most `n` coordinate centres, so one has weight at least `D/48`.
Apply PX228. \(\square\)

The repeated-pair coordinate-line degeneracy of PX370 is already a loaded-line
child, so PX386 covers the nondegenerate case.

## 2. Generic rank-one averaging

Let `C_gen` be one exact two-variable generic rank-one family.  Its centres lie
in the buffer candidate field, which has at most `n^2` cells, and again

\[
|C_{\rm gen}|=\sum_f\mu(f).
\]

### Theorem PX387 -- PROVED

If the generic family is the weighted two-variable outcome of PX357 for a bank
of designated destruction `D`, then some candidate centre satisfies

\[
\boxed{
\mu(f)\ge\frac{D}{32}.
}
\]

It therefore centres a clean star of order at least

\[
\boxed{
\frac{D}{32K}.
}
\]

### Proof

PX357 gives

\[
|C_{\rm gen}|\ge\frac{Dn^2}{32}.
\]

Average over at most `n^2` centres and apply PX228. \(\square\)

### Corollary PX388 -- PROVED REDUCTION

For every threshold `T`, a rank-one terminal return satisfies one of:

1. a loaded selected line;
2. a clean-star child of order at least `T`; or
3. the parent designated destruction obeys

   \[
   D<48KT
   \]

   in the coordinate case, or

   \[
   D<32KT
   \]

   in the generic case.

Thus rank-one return cannot remain diffuse once `D` is large compared with the
line-occupancy scale.

## 3. One-variable bounded return depth

Assume throughout this section that

\[
q_{\rm ch}=n^{o(1)},
\qquad
K=n^{o(1)}.
\]

Consider a return chain in which the weighted two-variable alternative has not
occurred and no compatible endpoint block above the square-root ambient
threshold has yet appeared.

PX363 gives, after two consecutive high-point one-variable returns,

\[
D\ge
\left(\frac{n}{384q_{\rm ch}}\right)^{3/4}
=n^{3/4-o(1)}.
\]

### Theorem PX389 -- PROVED REDUCTION

For all sufficiently large `n`, the next one-variable return after those two
high-point generations cannot be a directed-path family.  If it is coordinate
rank one, it yields a clean-star child of order

\[
\boxed{n^{3/4-o(1)}}.
\]

Hence a chain of one-variable terminal returns reaches the large-block
clean-star interface after at most three high-point generations, unless a
large compatible endpoint block appears earlier.

### Proof

PX366 permits a directed-path outcome only while `D=O(n^(1/3))`, contradicted
by `D=n^(3/4-o(1))`.

For coordinate rank one, PX386 gives star order at least

\[
D/(48K)=n^{3/4-o(1)}.
\]

This is strictly above `n^(1/2+epsilon)` for some fixed positive `epsilon` and
all sufficiently large `n`. \(\square\)

## 4. Two-variable bounded return depth

### Theorem PX390 -- PROVED REDUCTION

If a weighted two-variable outcome occurs for parent destruction `D`, PX361
produces a one-point child with designated destruction at least

\[
D_1\ge\frac{Dn}{64}.
\]

Starting from an original terminal core, `D>=1`, so `D_1>=n/64`.  For all
sufficiently large `n`, the next terminal return cannot be:

1. directed path, by PX366;
2. mixed cross-buffer, by PX368; or
3. generic rank one without producing a clean star of order

   \[
   \boxed{n^{1-o(1)}}
   \]

   by PX387.

A coordinate rank-one return likewise produces a clean star of order
`n^(1-o(1))` by PX386, while its repeated-pair degeneracy is a loaded line.

### Proof

The first two exclusions follow from `D_1>=n/64`, which exceeds the
`O(n^(1/3))` and absolute `64` caps.  Rank-one averaging gives star order at
least

\[
D_1/(48K)
\]

or `D_1/(32K)`, both equal to `n^(1-o(1))`. \(\square\)

Thus a two-variable terminal return reaches the large-block star/line interface
in at most one additional return generation.

## 5. Actual terminal-return theorem

### Theorem PX391 -- PROVED REDUCTION

Assume `q_ch=n^(o(1))`, `K=n^(o(1))`, and the ambient order is above the
explicit buffer/divisor thresholds of PX342--PX350.

Every actual order-one or order-two trajectory terminal core has one of the
following outcomes.

1. An improving buffer cycle exists.
2. A compatible endpoint block above the square-root ambient threshold is
   produced by PX374--PX380.
3. A clean star above the square-root ambient threshold is produced within at
   most three one-variable high-point returns.
4. A two-variable return produces a clean star or loaded line above the
   square-root ambient threshold within one additional return.

Every block/star/line outcome enters the large-block strict-sign-or-child
interface PX334--PX335 and the loaded-line cubic destruction theorem
PX240--PX244.

### Proof

Apply PX350.  A nonimproving bank yields one of the PX354 sectors.  Use the
support-cover and weighted-thinning alternatives PX371--PX380.  If a large
endpoint block occurs, item 2 holds.  Otherwise follow weighted one-point
returns.  PX389 handles a purely one-variable chain, and PX390 handles the
first two-variable occurrence. \(\square\)

### Corollary PX392 -- PROVED REDUCTION

The actual trajectory-terminal branch no longer has an independent asymptotic
obstruction family.  Above the explicit divisor thresholds, it returns after
bounded causal depth to one of the already established large-block decoder
interfaces.

The remaining all-`n` work is:

1. verify the finitely many ambient orders below the buffer/divisor threshold;
2. insert PX391 into the global product induction;
3. ensure the large-block child forest and terminal-return forest use one
   common lexicographic potential without duplicating blocker credit.

PX392 is not exact infinite product closure.  It closes the asymptotic
trajectory-terminal alternative under the stated subpower channel and
line-occupancy hypotheses.

## 6. Verification

Run

```bash
python scripts/verify_product_rank_one_return_star.py
```

The verifier checks the averaging constants, the one- and two-variable return
recurrences, and the exponent comparisons used in PX389--PX391.
# Finite product witnesses at side lengths 6, 8, 9, and 10

This note records explicit saturated no-three configurations found inside the
mixed-radix product searches. They are finite certificates only; they do not
prove multiplicative closure.

For a permutation pair `(pi_0,pi_1)` on `[N]`, write

\[
S(\pi_0,\pi_1)
=
\{(x,\pi_r(x)):x\in[N],\ r\in\{0,1\}\}.
\]

## Finite certificate at 6 — PROVED

The pair

\[
\pi_0=(3,0,5,2,4,1),
\qquad
\pi_1=(4,1,3,0,5,2)
\]

defines a saturated no-three configuration of 12 points in `[6]^2`.

It arises from the `3 x 2` cycle-phase product in a crossed radix orientation.
A second side-six certificate arises from the enlarged `2 x 3` full-host
selector:

\[
(1,5,3,0,4,2),
\qquad
(3,1,5,2,0,4).
\]

## Finite certificate at 8 — PROVED

The pair

\[
\pi_0=(2,3,1,0,7,6,4,5),
\qquad
\pi_1=(4,5,7,6,1,0,2,3)
\]

defines a saturated no-three configuration of 16 points in `[8]^2`.

It arises from the `4 x 2` cycle-phase product in the ordinary radix
orientation.

## Finite certificate at 9 — PROVED

The pair

\[
\pi_0=(3,6,1,8,0,2,5,7,4),
\]

\[
\pi_1=(4,1,3,6,8,0,7,2,5)
\]

defines a saturated no-three configuration of 18 points in `[9]^2`.

It arises from a degree-two selection in the crossed `3 x 3` factor-product
host. It is not a cycle-phase state.

## Finite certificate at 10 — PROVED

The pair

\[
\pi_0=(4,2,1,3,0,9,6,8,7,5),
\]

\[
\pi_1=(5,7,8,6,9,0,3,1,2,4)
\]

defines a saturated no-three configuration of 20 points in `[10]^2`.

It arises from the blockwise-reversed `2 x 5` construction in
[`docs/36-blockwise-digit-permutations.md`](36-blockwise-digit-permutations.md).
Unlike every unmodified global `2 x 5` host, this locally permuted host contains
a no-three degree-two state.

## Verification

Run

```bash
python scripts/verify_product_witnesses.py
```

The script checks that each layer is a permutation, the layers are pointwise
disjoint, and every one of the `binom(2N,3)` point triples has nonzero integer
determinant.

These examples provide exact finite constructions relevant to PC5, but they do
not supply a generating family or an arithmetic coverage theorem.

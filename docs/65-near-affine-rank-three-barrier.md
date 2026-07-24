# Near-affine barrier for rank-three strong-complete spread

For primes `p congruent to 1 mod 4`, the affine strong complete mappings

\[
f_{i,b}(x)=ix+b,
\qquad i^2=-1,
\]

are natural high-degree seeds for the PX98 switching graph.  This chapter shows
that no distribution obtained by changing only a small part of such a seed can
have rank-three spread.

The obstruction is elementary: almost every triple of unchanged rows still
lies on one fixed affine graph.

Let

\[
\mathcal A_p
=
\{f_{i,b}:i^2=-1,\ b\in\mathbb F_p\}.
\]

There are exactly `2p` maps in `A_p`.  Choose a base map `F` uniformly from
`A_p`, then choose an arbitrary random permutation `G`, possibly depending on
`F`.  Put

\[
D=d_H(F,G)
\]

for their Hamming distance.

## Theorem PX101 -- PROVED

For some matching cylinder `E` of three row-image edges,

\[
\boxed{
\Pr(E\subseteq\operatorname{graph}(G))
\ge
\frac{
\mathbb E\binom{p-D}{3}
}{
2p\binom p3
}.
}
\]

Consequently, if the law of `G` is rank-three spread with constant `K`, meaning

\[
\Pr(E\subseteq\operatorname{graph}(G))
\le
\frac K{(p)_3}
\]

for every three-edge matching cylinder, then

\[
\boxed{
\mathbb E\binom{p-D}{3}
\le
\frac{Kp}{3}.
}
\]

In particular, constant rank-three spread requires the number of unchanged rows
`p-D` to have cubic scale at most `O(p)`; a typical output can retain only
`O(p^(1/3))` rows of its affine seed.

### Proof

For every base map `f_(i,b)` and every three-element row set `X`, let

\[
E(i,b,X)
=
\{(x,f_{i,b}(x)):x\in X\}.
\]

These cylinders are all distinct.  Indeed, one edge fixes `b` once `i` is
known, and a cylinder on two distinct rows cannot lie on both slopes `i` and
`-i`.

There are therefore exactly

\[
2p\binom p3
\]

root-affine three-edge cylinders.

For a realized pair `(F,G)`, every three rows on which `G` agrees with `F` give
one root-affine cylinder contained in `G`.  Hence `G` contains at least

\[
\binom{p-D}{3}
\]

members of the root-affine cylinder family associated with the sampled base.
It may contain additional members associated with the other affine bases.

Sum the cylinder indicators over the complete root-affine family and take
expectations.  The sum is at least

\[
\mathbb E\binom{p-D}{3}.
\]

One cylinder therefore has probability at least the average over the
`2p binom(p,3)` cylinders, proving the first bound.

If every cylinder has probability at most `K/(p)_3`, use

\[
(p)_3=6\binom p3
\]

to obtain

\[
\frac{
\mathbb E\binom{p-D}{3}
}{2p\binom p3}
\le
\frac K{6\binom p3},
\]

which rearranges to the second assertion. \(\square\)

## Corollary PX101a -- PROVED

If `D<=p-q` almost surely, so every output agrees with its affine seed on at
least `q` rows, then the rank-three spread constant must satisfy

\[
\boxed{
K\ge\frac{3}{p}\binom q3.
}
\]

Thus:

- retaining a positive fraction of the affine rows forces `K=Omega(p^2)`;
- retaining `p^alpha` rows forces `K=Omega(p^(3alpha-1))`;
- a constant `K` is possible only when `q=O(p^(1/3))`.

## 2. Consequence for four-trade dynamics

One PX98 trade changes four rows.  A bounded number of trades leaves
`p-O(1)` affine rows and therefore has rank-three constant `Omega(p^2)`.  More
generally, any switching process intended to establish PX97 must globally mix
almost every row; local perturbation around the high-degree affine seeds is
insufficient.

This does not rule out the PX98 route.  It changes its required form:

1. the process must run for enough successful trades to rewrite essentially the
   whole permutation;
2. a proof needs global expansion or rapid mixing, not only many neighbours of
   the affine starting states;
3. the large order-thirteen component from PX99 is relevant because it already
   contains maps at full Hamming distance from the affine core.

PX101 also explains the poor asymptotic cylinders of the one-trade descendant
measure despite its `Theta(p^3)` distinct states.

## 3. Verification

Run

```bash
python scripts/verify_product_near_affine_barrier.py
```

The verifier checks uniqueness of every root-affine cylinder, evaluates the
exact lower bound for all possible retained-row counts, and confirms the
order-thirteen one-trade descendants satisfy the predicted obstruction.
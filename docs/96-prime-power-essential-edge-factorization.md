# Essential edges at the half-degree parent endpoint

CMR208 preserves a parent matching host until its minimum degree reaches
`ceil(t/2)`. A further certificate deletion could fail only if the chosen cell
belonged to every perfect matching of the residual host. Hall's theorem shows
that this cannot happen at the half-degree threshold.

Let `H=(L,R;E)` be a balanced bipartite graph with `|L|=|R|=t` and at least one
perfect matching. An edge is **essential** if it belongs to every perfect
matching of `H`.

## 1. Exact Hall characterization

### Theorem CMR210 — PROVED

An edge `e=uv`, with `u\in L` and `v\in R`, is essential if and only if there
are sets

\[
u\in A\subseteq L,
\qquad
v\in B\subseteq R
\]

such that

\[
|A|=|B|,
\qquad
N_H(A)=B,
\qquad
N_H(v)\cap A=\{u\}.
\]

For every such pair `(A,B)`, perfect matchings factor canonically:

\[
\boxed{
\operatorname{PM}(H)
\cong
\{e\}
\times
\operatorname{PM}\bigl(H[A\setminus\{u\},B\setminus\{v\}]\bigr)
\times
\operatorname{PM}\bigl(H[L\setminus A,R\setminus B]\bigr).
}
\]

### Proof

Suppose first that `e` is essential. Then `H-e` has no perfect matching. Hall's
theorem supplies `A\subseteq L` with

\[
|N_{H-e}(A)|<|A|.
\]

Since `H` has a perfect matching,

\[
|N_H(A)|\ge|A|.
\]

The two neighbourhoods differ by at most the endpoint `v`, so equality is
forced throughout:

\[
|N_{H-e}(A)|=|A|-1,
\qquad
N_H(A)=N_{H-e}(A)\cup\{v\},
\qquad
|N_H(A)|=|A|.
\]

In particular `u\in A`, the edge `uv` is the only edge from `A` to `v`, and
with `B=N_H(A)` all three displayed conditions hold.

Conversely, suppose such `A,B` exist. Every perfect matching must match the
`|A|` vertices of `A` bijectively onto `B`, because there are no edges from `A`
to `R\setminus B`. The vertex `v` has only the neighbour `u` inside `A`, so
every perfect matching contains `uv`.

After fixing `uv`, the remaining vertices of `A` match inside `B`, and
cardinality forces the complementary vertices to match internally. This gives
the product factorization. ∎

## 2. Minimum-degree constraints

### Theorem CMR211 — PROVED

Assume

\[
\delta(H)\ge2,
\]

and let `uv` be essential with Hall factor `(A,B)`. Put
`a=|A|=|B|`. Then

\[
\boxed{
\delta(H)\le a\le t-\delta(H).
}
\]

### Proof

Every vertex of `A` has all its neighbours in `B`, so `a\ge\delta(H)`.

The case `a=t` is impossible because then `A=L`, while
`N_H(v)\cap A=\{u\}` would give `\deg(v)=1`. Hence `R\setminus B` is nonempty.
Choose `w\in R\setminus B`. Since `B=N_H(A)`, the vertex `w` has no neighbour
in `A`; all its neighbours lie in `L\setminus A`, a set of size `t-a`.
Therefore

\[
\delta(H)\le t-a,
\]

which proves the upper bound. ∎

This complementary-side bound is the decisive constraint. It is stronger than
the one obtained from the endpoint `v` alone.

## 3. Half-degree hosts have no essential edge

### Theorem CMR212 — PROVED

Let `t\ge4`, and suppose

\[
\delta(H)\ge\left\lceil\frac t2\right\rceil.
\]

Then `H` has no essential edge. Equivalently, for every edge `e\in E(H)`, the
graph `H-e` still has a perfect matching.

### Proof

If `t` is odd, CMR211 would require

\[
\left\lceil\frac t2\right\rceil
\le a\le
\left\lfloor\frac t2\right\rfloor,
\]

which is impossible.

Let `t=2h` be even. CMR211 forces `a=h`. Every vertex of `A` has degree at least
`h`, has no neighbours outside the `h`-set `B`, and therefore is adjacent to
every vertex of `B`. In particular `v` has every vertex of `A` as a neighbour,
contradicting

\[
N_H(v)\cap A=\{u\}
\]

because `h\ge2`. ∎

Thus the final host produced by CMR208 is not merely matchable: every one of its
allowed cells is individually deletable while preserving some perfect
matching.

## 4. Every terminal certificate can be deleted once

### Corollary CMR213 — PROVED

Let `H` be a half-degree residual parent host from CMR208, and let `Q` be any
rank-`1/2/3` candidate certificate realized by at least one perfect matching of
`H`.

For every prescribed edge `e\in Q`, the graph `H-e` has a perfect matching, and
no perfect matching of `H-e` realizes `Q`.

### Proof

CMR212 says that `e` is not essential, so `H-e` retains a perfect matching.
Every realization of `Q` contains `e`, hence none remains after the deletion.
∎

## 5. One-step cover replacement

### Corollary CMR214 — PROVED

Suppose a candidate family `\mathcal C` covers every perfect matching of a
half-degree host `H`. Choose any certificate `Q\in\mathcal C` which is realized
by at least one perfect matching, and choose any prescribed edge `e\in Q`.

Then

1. `H-e` has at least one perfect matching;
2. every perfect matching of `H-e` is covered by a certificate from
   `\mathcal C` not containing `e`;
3. the certificate `Q` has been eliminated from the residual cover problem.

### Proof

The first and third assertions are CMR213. Every perfect matching of `H-e` is
also a perfect matching of `H`, so the original cover supplies a certificate.
No certificate containing `e` can occur in `H-e`, proving the second assertion.
∎

This is a strict replacement step: one may remove an arbitrary currently
realized candidate cylinder and retain a nonempty matching state space.

## 6. Revised internal endpoint

CMR209 reduces internal no-return to repeated replacement of a linear
rank-three family. CMR212--CMR214 show that the first replacement step can never
be blocked by a forced parent cell, at either parity.

After one deletion the minimum degree may fall below `t/2`, so indefinite
cell-by-cell deletion does not follow automatically. The remaining theorem is
to organize the sequence of CMR214 replacements so that one of the following
occurs before matching flexibility is exhausted:

1. an anchored rank-one or rank-two wall exposes an executable bank;
2. deleted cells accumulate in a new Hall rectangle that forces envelope
   expansion or a smaller host decomposition;
3. the replacement certificates consume new primitive line/carry signatures;
4. the residual host retains a half-degree subhost after regularization.

No all-`n` theorem is claimed here. Essential-edge equivalence and exhaustive
small half-degree hosts are checked in
[`scripts/verify_prime_power_essential_edges.py`](../scripts/verify_prime_power_essential_edges.py).

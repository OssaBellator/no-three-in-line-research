# Dyadic candidate-only bands as bounded conflict systems

CMR222 isolates a cubic population of candidate-only triples in one dyadic
primitive-height band. At high enough primitive height, that band satisfies the
standard bounded-conflict hypotheses from conflict-free hypergraph matching
theory.

Work in the normalized inherited parent board `[0,t-1]^2`. For a dyadic integer
`H`, let `\mathcal C_H` be the family of compatible collinear triples whose
primitive unoriented direction `(u,v)` satisfies

\[
H\le\max\{|u|,|v|\}<2H.
\]

The host graph is the derangement graph

\[
G_t=K_{t,t}\setminus I.
\]

Its graph edges are candidate cells, and each member of `\mathcal C_H` is a
three-edge conflict.

## 1. Maximum conflict degree

### Theorem CMR223 — PROVED

Every candidate cell belongs to fewer than

\[
\boxed{3t^2}
\]

conflicts from `\mathcal C_H`.

### Proof

Fix a cell `z`. The number of unoriented integer directions with

\[
H\le\max\{|u|,|v|\}<2H
\]

is at most

\[
\frac{(4H-1)^2-(2H-1)^2}{2}
=
6H^2-2H
<6H^2.
\]

For one such primitive direction, put

\[
K=\max\{|u|,|v|\}\ge H.
\]

The integer parameters `q` for which `z+q(u,v)` remains in the board occupy an
interval of length at most `(t-1)/K`. Hence the line has at most

\[
1+\left\lfloor\frac{t-1}{K}\right\rfloor
\]

board points, and at most `(t-1)/H` other points besides `z`. The number of
triples on that line containing `z` is therefore at most

\[
\binom{\lfloor(t-1)/H\rfloor}{2}
<
\frac{t^2}{2H^2}.
\]

Multiplication by fewer than `6H^2` directions gives fewer than `3t^2`
conflicts. Compatibility and the missing diagonal only decrease the count. ∎

## 2. Conflict pair codegree

### Theorem CMR224 — PROVED

Every compatible pair of candidate cells belongs to at most

\[
\boxed{\frac tH}
\]

conflicts from `\mathcal C_H`.

### Proof

Two cells determine one real line and one primitive direction. If its height is
outside the band, the codegree is zero. Otherwise the line contains at most

\[
1+\left\lfloor\frac{t-1}{H}\right\rfloor
\]

board points, so after the fixed pair is removed there are fewer than `t/H`
choices for the third point. ∎

## 3. Verification of the published boundedness conditions

Fix `epsilon>0` and assume

\[
H\ge t^\epsilon.
\]

### Corollary CMR225 — PROVED

For all sufficiently large `t`, the host `G_t` and conflict system
`\mathcal C_H` satisfy the standard conflict-free matching hypotheses with
base degree `d=t`, conflict rank `ell=3`, and exponent `epsilon`:

1. `G_t` is `(t-1)`-regular and has graph codegree at most one;
2. every conflict has size three;
3. the maximum conflict degree is below
   \[
   3d^2;
   \]
4. the maximum conflict pair codegree is at most
   \[
   d^{1-\epsilon};
   \]
5. the extra neighbourhood conditions for size-two conflicts are vacuous.

### Proof

The host statements are immediate. CMR223 gives the degree condition with
`ell=3`. CMR224 and `H>=t^epsilon` give

\[
\Delta_2(\mathcal C_H)
\le\frac tH
\le t^{1-\epsilon}.
\]

The bounded-conflict definition has no further conditions when every conflict
has size three. ∎

## 4. Almost-perfect band avoidance

### Theorem CMR226 — PROVED FROM A PUBLISHED THEOREM

For every fixed `epsilon>0`, every sufficiently large `t`, and every dyadic
band with

\[
H\ge t^\epsilon,
\]

the derangement graph `G_t` contains a matching of size

\[
(1-o(1))t
\]

which contains no candidate-only collinear triple from `\mathcal C_H`.

### Proof

Apply the conflict-free hypergraph matching theorem of Glock, Joos, Kim, Kühn,
and Lichev to the two-uniform host `G_t` and the conflict hypergraph
`\mathcal C_H`. The host is asymptotically regular with degree `d=t`, has
constant codegree, and CMR225 verifies the required conflict degree and
codegree conditions. The theorem supplies a conflict-free almost-perfect
matching. ∎

This application is asymptotic and almost-perfect. It does not yet produce the
exact parent permutation needed by the alternating closure.

## 5. Exact-completion target

The 2026 conflict-free matching-and-covering theorem of Joos, Mubayi, and Smith
shows that an almost-perfect conflict-free matching can be extended to cover a
specified vertex class when a suitable reserve hypergraph and mixed-conflict
system satisfy additional degree and codegree hypotheses.

For the inherited parent problem, the natural setup is:

- `P`: parent source columns;
- `Q`: main copies of parent rows;
- `R`: reserve copies of the same parent rows;
- main and reserve edges both representing grid cells;
- mixed conflicts forbidding repeated use of one original row and every
  candidate triple involving reserve edges.

The remaining exact-band theorem is to verify the mixed-conflict conditions in
this duplicated-row reserve model. Success would give a full parent
permutation avoiding one high-height band, not merely an almost-perfect
matching.

No all-`n` theorem is claimed here. The band-degree and pair-codegree bounds are
checked exactly on small grids in
[`scripts/verify_prime_power_band_conflicts.py`](../scripts/verify_prime_power_band_conflicts.py).

# Universal line-clean cylinders have a cheap-rollback or forced-factorization availability theorem

CMR492--CMR496 give every compatible paid pair an exact full-parent line-clean
cylinder, but execution inside a restricted current host may require restoring
edges which were previously deleted or reserved. This chapter gives that
availability problem the same minimum-cost normalization used for terminal
rollback.

Fix a compatible pair `Z` in a parent block of side `m`, delete its two source
and two target vertices, and put

\[
n=m-2.
\]

Let `K=K_{n,n}` be the residual complete bipartite graph. Let `F_L` be the
perfect matching used in CMR492 to cover every remaining cell of the paid line,
and define the line-clean universe

\[
U_L=E(K)\setminus F_L.
\]

For `n\ge2`, `U_L` has perfect matchings: after relabelling `F_L` as the identity,
these are exactly derangements.

Let

\[
G\subseteq K
\]

be the current residual available host after all hard constraints have been
encoded as edge deletions. Put

\[
G_L=G-F_L.
\]

No matchability assumption on `G_L` is required.

## 1. Line-clean rollback number

Define

\[
\kappa_L(G)
=
\min\{|M\setminus E(G_L)|:M\in\operatorname{PM}(U_L)\}.
\]

### Theorem CMR497 — PROVED

For every `n\ge2`,

\[
\boxed{0\le\kappa_L(G)\le n.}
\]

A minimum-cost line-clean matching `M` supplies a restoration footprint

\[
R_M=M\setminus E(G_L)
\]

with

\[
|R_M|=\kappa_L(G),
\qquad
M\in\operatorname{PM}(G_L+R_M).
\]

Moreover,

\[
\kappa_L(G)=0
\]

if and only if the current residual host already contains a line-clean
completion of the paid pair.

### Proof

The line-clean universe has a perfect matching by CMR492. Every such matching
has exactly `n` edges, so its number of unavailable edges is at most `n`. Choose
one minimizing that number. Restoring precisely its unavailable edges makes the
matching available. Cost zero is equivalent to containment in `G_L`. ∎

Thus full-parent line-clean availability requires restoring at most one
residual matching's worth of edges.

## 2. Minimum restoration sets are forced

Let `M` be minimum cost, put

\[
R=R_M,
\qquad
H=G_L+R.
\]

### Theorem CMR498 — PROVED

Every edge of `R` is essential in `H`. Consequently:

1. `R` is a matching;
2. every perfect matching of `H` contains all edges of `R`;
3. restriction gives the exact factorization
   \[
   \boxed{
   \operatorname{PM}(H)
   \cong
   \{R\}
   \times
   \operatorname{PM}\bigl(H-V(R)\bigr).
   }
   \]

If `|R|=k`, the residual factor has side `n-k`.

### Proof

Suppose `r\in R` were avoidable by some perfect matching `N` of `H`. Then

\[
N\setminus E(G_L)
\subseteq
R\setminus\{r\},
\]

so `N` would be a line-clean matching with restoration cost at most `|R|-1`,
contradicting minimality. Hence every restored edge is essential. Essential
edges form a matching, and deleting their endpoints gives the displayed product
bijection. ∎

Expensive line-clean availability is therefore exact lower-dimensional host
factorization.

## 3. Threshold availability dichotomy

### Corollary CMR499 — PROVED

Fix an integer

\[
1\le q\le n+1.
\]

Exactly one of the following numerical alternatives holds.

1. **Cheap line-clean rollback.**
   \[
   \boxed{\kappa_L(G)<q.}
   \]
   Restoring fewer than `q` unavailable residual edges realizes a line-clean
   completion of the paid pair.
2. **Strict line-clean factorization.** A minimum restoration set has size
   \[
   \kappa_L(G)\ge q,
   \]
   is forced in the available line-clean host, and factors the remaining
   matching problem to side at most
   \[
   \boxed{n-q.}
   \]

For `q=n+1`, the cheap branch always holds by CMR497.

### Proof

Apply CMR498 to a minimum restoration set and split according to whether its
size is below `q`. ∎

This is the exact availability analogue of CMR441.

## 4. Exact token and conflict payment

Assume the parent side is

\[
t=p^h.
\]

### Theorem CMR500 — PROVED

A minimum line-clean restoration footprint `R` has exact labelled full-token
incidence

\[
\boxed{
\mathcal I(R)
=(p+1)(h-1)|R|.
}
\]

In the cheap branch `|R|<q`,

\[
\boxed{
\mathcal I(R)
<(p+1)(h-1)q.
}
\]

Let `\mathcal C` be any candidate edge-set family which is host-clean in `G_L`.
Every member of `\mathcal C` contained in `G_L+R` uses a restored edge, and

\[
\boxed{
|\{C\in\mathcal C:C\subseteq G_L+R\}|
\le
|R|\,\Delta(\mathcal C).
}
\]

For a harmonic packet of weight `W`, the number of recreated represented triples
is at most

\[
\boxed{
2(t-1)^2W|R|.
}
\]

### Proof

The token identity is CMR444 applied to the distinct restored edges. If a
candidate set appears after restoring `R` but uses no edge of `R`, it was already
contained in `G_L`, contradicting host cleanliness. Assign each recreated set
to one restored edge and use maximum edge degree. The harmonic estimate is
CMR386. ∎

Thus cheap availability is fully priced in the existing token and packet
ledgers.

## 5. Application to the final mixed-cycle branches

### Corollary CMR501 — PROVED

For every rooted secant-star arm of CMR494 and every bottleneck pair of CMR496,
the universal line-clean bank has the following exact endpoint in any restricted
residual host.

For every threshold `q`, either

1. fewer than `q` residual edges are restored to realize a line-clean completion,
   with labelled incidence below
   \[
   (p+1)(h-1)q
   \]
   and harmonic recreation bounded by CMR500; or
2. the minimum restoration footprint is a forced matching of size at least `q`
   and factors the residual problem from side `m-2` to side at most
   \[
   \boxed{m-2-q.}
   \]

### Proof

Apply CMR499--CMR500 to the CMR492 cylinder associated with the chosen rooted
arm or bottleneck pair. ∎

## 6. Revised frontier

The line-clean splice now has both construction and availability accounting.

- The full-parent cylinder exists with exact size `D_{m-2}`.
- Current-host availability costs at most `m-2` restored edges.
- Cheap restoration has exact token and packet price.
- Expensive restoration is strict forced-core factorization.

What remains is the **selection step inside the cheap branch**: among the
line-clean completions made available by a small restoration footprint, find one
which destroys more inherited target load than the rollback collateral it
recreates, or prove that every completion forces protected-reserve depletion,
a heavy prefix/carry signature, or envelope expansion. This is the natural
place to combine CMR334 frozen-bank averaging with CMR500.

No all-`n` theorem is claimed. Minimum restoration cost, essentiality of minimum
footprints, exact factorization, and conflict-support arithmetic are checked in
[`scripts/verify_prime_power_line_clean_rollback.py`](../scripts/verify_prime_power_line_clean_rollback.py).

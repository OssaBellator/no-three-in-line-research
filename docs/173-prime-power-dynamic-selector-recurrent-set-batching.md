# Recurrent unavailable selector sets batch into protected absorption or one persistent wall

CMR582--CMR586 give a finite ledger for single protected-contact edges.  A
failed dynamic canonical selector contains more information: at every
occurrence it has at least `H_P` unavailable edges in one fixed canonical
allowed universe.  Double-counting subsets of those inventories extracts a
whole recurrent unavailable edge set, not merely one recurrent edge.

On a joint-absence interval, the recurrent set has an exact matching-versus-
cover decomposition relative to the protected partial matching.  A large
matching on unprotected vertices is absorbed in one batch.  If that matching
is small, Konig's theorem covers the recurrent set by the protected vertices
plus a small additional vertex set, forcing one row or column containing many
simultaneously unavailable edges.  That wall enters the existing heavy-prefix
and dispersed-token machinery without temporal ambiguity.

Fix one dynamic protected selector state

\[
P=Q_L\cup R
\]

of size

\[
k=|P|
\]

on a residual complete bipartite graph of side `n`.  Let `F_P` be its canonical
forbidden perfect matching and put

\[
U_P=E(K_{n,n})\setminus F_P,
\qquad
N=|U_P|=n(n-1).
\]

Let `H_P>=1` be the exact dynamic-unavailability threshold from CMR554.  Thus
every failed occurrence `j` has an unavailable set

\[
B_j\subseteq U_P,
\qquad
|B_j|\ge H_P.
\]

## 1. Uniform recurrent-set extraction

### Theorem CMR587 — PROVED

Fix integers

\[
1\le r\le H_P,
\qquad
\lambda\ge2.
\]

For any collection of `J` failed occurrences, at least one of the following
holds.

1. **Exact recurrent unavailable set.**  Some fixed `r`-edge set
   \[
   W\subseteq U_P
   \]
   is contained in at least `\lambda` of the unavailable inventories `B_j`.
2. **Finite `r`-subset history.**
   \[
   \boxed{
   J
   \le
   (\lambda-1)
   \frac{\binom Nr}{\binom{H_P}r}.
   }
   \]

### Proof

Every occurrence contributes at least `binom(H_P,r)` pairs `(j,W)` with
`W\subseteq B_j` and `|W|=r`.  There are `binom(N,r)` possible sets `W`.  If
none occurs in `\lambda` inventories, every one occurs at most `\lambda-1`
times.  Hence

\[
J\binom{H_P}r
\le
(\lambda-1)\binom Nr.
\]

Rearrange. ∎

The cases `r=1` and `r=2` recover single-edge recurrence and exact pair
recurrence, while larger `r` extracts a genuine common unavailable core.

## 2. Joint absence or aggregate reintroduction

Suppose one `r`-edge set `W` occurs in `\lambda` selected inventories.  For
`f\in W`, let `I(f)` count absent-to-present reintroductions during the fixed
envelope epoch.

### Theorem CMR588 — PROVED

For every integer `\sigma>=2`, at least one of the following holds.

1. **Aggregate reintroduction payment.**
   \[
   \boxed{
   \sum_{f\in W}I(f)
   \ge
   \left\lceil\frac{\lambda}{\sigma-1}\right\rceil-1.
   }
   \]
2. **Jointly persistent unavailable set.**  One continuous interval contains at
   least `\sigma` selected occurrences while every edge of `W` remains
   unavailable throughout the interval.

### Proof

Apply the multi-edge absence-run theorem CMR538 to the fixed set `W`. ∎

Thus the only unpriced recurrent-set branch is a set of distinct edges which
are simultaneously and continuously unavailable.

## 3. Persistent matching or small vertex cover

Assume `W` is jointly persistent.  Let

\[
W^\circ
=
\{uv\in W:u,v\notin V(P)\}
\]

be the edges whose two endpoints are unprotected.  Let

\[
\nu=\nu(W^\circ)
\]

be the matching number of the bipartite graph with edge set `W^\circ`.

### Theorem CMR589 — PROVED

Fix an integer `s>=1`.  At least one of the following holds.

1. **Batch protected absorption.**  If `\nu>=s`, there is an `s`-edge matching
   \[
   S\subseteq W^\circ
   \]
   such that
   \[
   \boxed{P\cup S}
   \]
   is a partial matching.  Its canonical extension defines an exact
   derangement cylinder of size `D_n` which avoids all `s` edges of `S` at zero
   residual restoration cost.
2. **Small-cover persistent wall.**  If `\nu<s`, there is a vertex set
   \[
   C\subseteq V(K_{n,n})\setminus V(P)
   \]
   with
   \[
   |C|=\nu\le s-1
   \]
   such that every edge of `W` meets
   \[
   \boxed{V(P)\cup C.}
   \]
   Consequently some source or target vertex is incident with at least
   \[
   \boxed{
   d
   \ge
   \left\lceil\frac r{2k+s-1}\right\rceil
   }
   \]
   distinct edges of `W`.

All edges in the resulting wall remain continuously unavailable throughout the
joint interval.

### Proof

If `\nu>=s`, choose an `s`-edge matching in `W^\circ`.  Its endpoints avoid
`V(P)`, so `P\cup S` is a partial matching.  Apply the canonical extension
CMR571.

If `\nu<s`, Konig's theorem gives a vertex cover `C` of `W^\circ` with
`|C|=\nu`.  Every edge of `W\setminus W^\circ` meets `V(P)`, while every edge
of `W^\circ` meets `C`.  Hence `V(P)\cup C`, of size at most `2k+s-1`, covers
all `r` edges of `W`.  Pigeonhole gives the degree bound. ∎

The cover vertices in `C` identify compatibility congestion among otherwise
unprotected persistent edges; the vertices in `V(P)` identify protected-core
contacts.

## 4. Bulk absorption has finite depth

### Theorem CMR590 — PROVED

Suppose the batch-absorption branch of CMR589 is always taken with exactly `s`
new edges.  Starting from a protected matching of size `k_0`, the number of
successful batch-growth steps is at most

\[
\boxed{
\left\lfloor\frac{n-k_0}{s}\right\rfloor.
}
\]

After `a` successful steps the protected matching has size exactly

\[
k_0+as.
\]

### Proof

Every selected batch is a matching on vertices outside the current protected
matching, so all `s` edges may be added and protected size increases by `s`.
A partial matching has at most `n` edges. ∎

This is the batched form of the one-edge absorption chase CMR575.

## 5. Persistent walls yield simultaneous token structure

Assume the second branch of CMR589 gives a row or column wall of `d` persistent
edges.  Fix any nonroot depth `b` and one direction label.

### Theorem CMR591 — PROVED

For every integer `H>=2`, at least one of the following holds.

1. **Heavy persistent token.**  One full-prefix token contains at least `H`
   wall edges.
2. **Dispersed persistent tokens.**  At least
   \[
   \boxed{
   \left\lceil\frac d{H-1}\right\rceil
   }
   \]
   pairwise distinct full-prefix token cells are occupied.

With `H=\lceil\sqrt d\rceil` and the usual interpretation for `d=1`, the wall
gives one token containing at least `\lceil\sqrt d\rceil` simultaneously
unavailable edges or at least `\lfloor\sqrt d\rfloor` simultaneously occupied
tokens.

The `d` distinct wall edges carry exact labelled nonroot token incidence

\[
\boxed{
d(p+1)(h-1)
}
\]

in a parent of side `t=p^h`.

### Proof

Partition the varying coordinate of the row or column wall by residue modulo
`p^b`, exactly as in CMR512--CMR515.  The classes partition the `d` edges.  If
none reaches `H`, at least `ceil(d/(H-1))` classes are occupied.  CMR413 gives
the exact labelled incidence. ∎

Unlike a temporal union of contact edges, this wall is simultaneously absent
throughout one common interval.

## 6. Combined recurrent-set batching endpoint

### Corollary CMR592 — PROVED

Fix parameters

\[
1\le r\le H_P,
\qquad
s\ge1,
\qquad
\lambda,\sigma\ge2.
\]

Every failed history of one dynamic protected selector reaches at least one of
the following endpoints.

1. **Finite subset history.**
   \[
   J
   \le
   (\lambda-1)
   \frac{\binom{n(n-1)}r}{\binom{H_P}r}.
   \]
2. **Aggregate reintroduction payment.**  One recurrent `r`-set reaches CMR588.
3. **Batch protected absorption.**  At least `s` simultaneously unavailable,
   pairwise compatible, unprotected edges are added to the protected matching.
4. **Persistent row/column wall.**  One vertex is incident with at least
   \[
   \left\lceil\frac r{2k+s-1}\right\rceil
   \]
   simultaneously unavailable edges, which reach CMR591.

Repeated branch 3 has at most the number of growth steps in CMR590.

### Proof

Apply CMR587.  In the recurrent branch apply CMR588.  On a joint-absence
interval apply CMR589.  Use CMR590 in the matching branch and CMR591 in the
cover branch. ∎

## 7. Revised frontier

Dynamic selector failure now has a batched common-epoch normal form.

- Large histories contain a recurrent unavailable edge set, not only a single
  recurrent edge.
- Recurrent sets pay aggregate reintroduction or become jointly persistent.
- Joint persistence gives bulk matching absorption or a persistent wall
  covered by the protected core plus a small Konig cover.
- Bulk absorption has finite depth.
- Persistent walls feed exact heavy/dispersed token structure with simultaneous
  absence and selector ownership.

The remaining prime-power task is temporal payment for reuse of one fixed
persistent wall/token certificate and the final fixed-contact branch after the
batched absorption capacity is exhausted.  The expected exits remain protected
reserve depletion, deletion ancestry, full-token return, or strict envelope
expansion.

No all-`n` theorem is claimed.  Subset-incidence counting, joint-absence
arithmetic, matching-cover decomposition, bulk-growth bounds, and persistent
wall token partitioning are checked in
[`scripts/verify_prime_power_dynamic_selector_batching.py`](../scripts/verify_prime_power_dynamic_selector_batching.py).

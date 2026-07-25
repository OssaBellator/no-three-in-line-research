# Disjoint rank-zero conflict packings are deleted, fully forced, or paid by distinct restoration

CMR564--CMR568 leave one new static object: a pairwise cell-disjoint packing of
rank-zero candidate-only conflict triples on distinct lines.  Such a packing
has an exact monotone response.

Process its triples inside one matching-preserving deletion pass.  If a triple
contains a nonessential edge, delete one such edge and kill the triple.  If no
edge is deletable, all three edges are essential.  Essentiality persists, and
the final essential core is a matching of size at most the parent side.
Because the packed triples are edge-disjoint, at most one third of the core can
support fully forced packed triples.

If a later rollback or ancestor reset recreates a killed triple, it must restore
that triple's deleted edge.  The deleted edges are distinct, so recreation pays
restoration and full-token incidence linearly.

## 1. Packed conflict deletion pass

Let

\[
G_0
\]

be a balanced bipartite host of side `t` with a perfect matching.  Let

\[
\mathcal P=\{C_1,\ldots,C_R\}
\]

be candidate-only collinear triples such that

\[
\boxed{
C_i\cap C_j=\varnothing
\qquad(i\ne j).
}
\]

Each `C_i` is a compatible three-edge partial matching.

Process the triples in any order.  At step `i`, in the current host `G_{i-1}`:

- if some edge `e_i\in C_i` is nonessential, put
  \[
  G_i=G_{i-1}-e_i;
  \]
- otherwise put
  \[
  G_i=G_{i-1}
  \]
  and call `C_i` fully forced.

### Theorem CMR569 — PROVED

Every host in the pass has a perfect matching.

For every processed triple, exactly one of the following outcomes is recorded.

1. **Killed conflict.**  One edge of the triple is deleted while a perfect
   matching survives.
2. **Fully forced conflict.**  All three edges are essential in the current
   host.

Every edge of a fully forced conflict remains essential for the rest of the
pass.

### Proof

Deleting a nonessential edge preserves at least one perfect matching by
definition.  If no edge is nonessential, all three are essential.

CMR426 gives persistence of essentiality under later edge deletions which
preserve a perfect matching. ∎

Thus no packed conflict can block the pass without becoming a terminal
essential certificate.

## 2. Fully forced packing bound

Let

\[
F_{\mathcal P}
\]

be the number of fully forced packed triples.

### Theorem CMR570 — PROVED

One has

\[
\boxed{
F_{\mathcal P}
\le
\left\lfloor\frac t3\right\rfloor.
}
\]

Consequently at least

\[
\boxed{
R-\left\lfloor\frac t3\right\rfloor
}
\]

packed conflicts are killed whenever that quantity is positive.

### Proof

Every fully forced triple contributes its three edges to the final essential
core by CMR569.  The packed triples are pairwise edge-disjoint, so these
contributions are distinct.

CMR429 says the final essential core is a matching of size at most `t`.
Therefore

\[
3F_{\mathcal P}\le t.
\]

Rearrange.  Every non-forced processed triple is killed. ∎

The bound remains valid even if different packed triples share source or target
vertices: in that case they cannot all contribute essential edges to one
matching core, so the estimate can only improve.

## 3. Exact deleted-edge code

Let

\[
\mathcal K\subseteq\mathcal P
\]

be the killed triples and let

\[
D_{\mathcal P}
=
\{e_C:C\in\mathcal K\}
\]

contain the one deleted edge selected from each killed triple.

### Theorem CMR571 — PROVED

The map

\[
\boxed{
C\longmapsto e_C
}
\]

is injective.  Hence

\[
\boxed{
|D_{\mathcal P}|=|\mathcal K|.
}
\]

Every triple in `\mathcal K` is absent from the final deletion-pass host.

### Proof

The packed triples are edge-disjoint, so deleted edges selected from different
triples are distinct.  Each killed triple is missing its selected edge, and
later steps only delete more edges. ∎

The killed packing therefore has a private one-edge deletion code.

## 4. Recreation requires distinct restoration

Let `G_*` be the final host of the deletion pass.  Restore an arbitrary edge
set

\[
R\subseteq E(G_0)\setminus E(G_*).
\]

Consider any perfect matching or candidate state in `G_*+R`.

### Theorem CMR572 — PROVED

If `s` killed packed triples are completely present in `G_*+R`, then

\[
\boxed{
|R\cap D_{\mathcal P}|\ge s.
}
\]

Equivalently, every recreated killed conflict uses its own private restored
edge.

For parent side

\[
t=p^h,
\]

those `s` distinct restored edges carry exact labelled full-token incidence

\[
\boxed{
s(p+1)(h-1).
}
\]

### Proof

A killed triple `C` is missing its private edge `e_C` from `G_*`.  Complete
presence of `C` after restoration therefore requires `e_C\in R`.  CMR571 makes
the required edges distinct across killed triples.

CMR413 assigns exactly `(p+1)(h-1)` labelled nonroot full-token incidences to
each physical edge. ∎

Thus rollback cannot recreate many packed conflicts with one common restored
edge.

## 5. Combined rank-zero packing endpoint

### Corollary CMR573 — PROVED

Apply the pass to the pairwise cell-disjoint rank-zero packing supplied by
CMR567--CMR568.  At least one of the following exact outcomes holds.

1. **Large monotone deletion payment.**  At least
   \[
   R-\left\lfloor\frac t3\right\rfloor
   \]
   conflict lines are killed by distinct matching-preserving edge deletions.
2. **Fully forced terminal packing.**  At most
   \[
   \left\lfloor\frac t3\right\rfloor
   \]
   packed triples survive as fully forced rank-three certificates.
3. **Rollback recreation payment.**  Recreating `s` killed packed conflicts
   later requires `s` distinct restored edges and exact labelled token incidence
   `s(p+1)(h-1)`.

### Proof

Combine CMR569--CMR572. ∎

## 6. Revised frontier

The disjoint-support rank-zero branch is now paid.

- Monotone deletions kill all but at most `t/3` packed triples.
- Survivors are fully forced terminal certificates.
- Any later recreation pays private restored edges linearly.

The static canonical branch therefore remains open only on:

1. heavy single conflict lines;
2. repeated-cell secant stars, whose mixed-ratio/carry execution must be
   attached to the quantitative sizes from CMR568.

The dynamic branch remains one persistent canonical allowed edge.  Its
reintroduction, cross-deficiency, reserve-depletion, or envelope-expansion
payment is separate.

No all-`n` theorem is claimed.  Deletion-pass preservation, essential-core
capacity, private deleted-edge codes, and restoration incidence are checked in
[`scripts/verify_prime_power_disjoint_conflict_deletion.py`](../scripts/verify_prime_power_disjoint_conflict_deletion.py).

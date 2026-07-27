# Absolute last-entering owners and total geometric witness fate manifests

CMR1894--CMR1901 reconstruct every primitive geometric witness before aggregation.
The remaining semantic gap is to attach the absolute last-entering response-edge
owner and to record what happens to every witness before the labelled coefficient
table is exported.

This chapter gives a finite manifest and exact checker for that interface.  It
does **not** prove that an arbitrary correction-rule name or auxiliary-certificate
identifier is semantically valid.  Those rule-specific obligations remain separate.
It does prove that every raw witness is present exactly once, has the mechanically
correct last-entering owner, and is assigned one explicit fate.

Let `G` be a finite bipartite response host, let `PM(G)` be its nonempty perfect
matching set, and let `E_ext(G)` be the set of edges occurring in at least one
response.  Fix a strict total entry order

\[
\prec
\]

on `E_ext(G)`.

For a primitive rank-`r` witness `w`, write `P(w)` for its compatible response-edge
prescription, with `1<=r<=3`.

## 1. Unique absolute last-entering owner

Define

\[
\operatorname{own}(w)
=
\max_{\prec} P(w).
\]

### Theorem CMR1902 -- PROVED

Every primitive witness has one unique absolute last-entering owner.

### Proof

`P(w)` is a finite nonempty subset of a strict total order.  Therefore it has a
unique maximum. ∎

The definition is independent of the background witness coordinates once the
response prescription is fixed.

## 2. Exact owner partition

For each extendable edge `e`, let

\[
\mathcal W_e
=
\{w:\operatorname{own}(w)=e\}.
\]

### Theorem CMR1903 -- PROVED

The complete primitive witness family is the disjoint union

\[
\boxed{
\mathcal W
=
\bigsqcup_{e\in E_{\mathrm{ext}}(G)}
\mathcal W_e.
}
\]

### Proof

CMR1902 assigns every witness exactly one owner.  Distinct owner classes cannot
intersect. ∎

Thus all rank-one, rank-two and rank-three primitive multiplicities may be
aggregated owner-by-owner without duplication.

## 3. Owner-labelled retained and dominated routes

A manifest declares recurrent child states with explicit owner fields.  A witness
with owner `e` may be marked:

- `retained`, with coefficient multiplicity one; or
- `dominated`, with an explicit positive upper multiplicity.

In either case the declared recurrent child must also carry owner `e`.

### Theorem CMR1904 -- PROVED

For every accepted retained or dominated witness, the exported coefficient remains
inside its exact last-entering owner class.

### Proof

The checker recomputes `own(w)` from the complete entry order and prescription,
then requires equality with the child state's owner field. ∎

### Corollary CMR1905 -- PROVED

Let `S` be a set of owner edges.  If every recurrent retained or dominated child
of a parent row has owner in `S`, then the recurrent geometric export is closed
inside the owner support `S`.

This is only an owner-support statement.  Collision, local-line, interface, root,
thin and CRT labels must still be retained separately.

## 4. Total witness fate partition

Every primitive witness must receive exactly one of four fates.

1. **Retained.** Export one coefficient to a recurrent child with the same owner.
2. **Deleted.** Export zero coefficients and cite a nonempty correction-evidence
   identifier.
3. **Transferred.** Export one coefficient to either:
   - a declared off-diagonal child at strictly smaller stratum; or
   - a declared auxiliary child.
4. **Dominated.** Export an explicit positive integer multiplicity to a recurrent
   child with the same owner and cite an upper-bound evidence identifier.

### Theorem CMR1906 -- PROVED

An accepted manifest is a total partition of the reconstructed primitive witness
set.  No witness is omitted, duplicated or assigned two fates.

### Proof

The checker reconstructs the exact rank-one, rank-two and rank-three witness sets
from the host, background points and collinearity predicate.  It converts every
manifest record to the same canonical witness key and requires set equality in
each rank, with duplicate keys rejected. ∎

Silent witness deletion is therefore impossible in an accepted manifest.

## 5. Structural transfer surface

### Theorem CMR1907 -- PROVED

Every accepted transferred witness has one of the following declared structural
targets:

\[
\boxed{
\text{off-diagonal child at lower stratum}
\quad\text{or}\quad
\text{auxiliary child}.
}
\]

### Proof

The checker compares the target state's role and stratum with the parent state.
A recurrent same-stratum target is rejected as a transfer. ∎

This theorem validates the finite transfer **surface**.  It does not prove that a
named auxiliary module is subcritical or that a declared structural descent is
actually executed by the underlying policy.  Those facts require their existing
module and transition verifiers.

## 6. Exact coefficient export

For a witness `w`, define its exported multiplicity

\[
m(w)=
\begin{cases}
1,&\text{retained or transferred},\\
0,&\text{deleted},\\
m_w\ge1,&\text{dominated}.
\end{cases}
\]

Aggregate by `(rank, child, prescription)`.

### Theorem CMR1908 -- PROVED

The accepted manifest exports the unique integer table

\[
c^{(r)}_{j}(P)
=
\sum_{\substack{w:\,P(w)=P\\
                 \operatorname{child}(w)=j}}
m(w).
\]

Every nondeleted primitive witness contributes at least one unit to exactly one
exported bin.  Any coefficient inflation above one is visible only through an
explicit dominated multiplicity.

### Proof

CMR1906 gives a unique fate.  The checker applies the displayed multiplicity rule
and accumulates one canonical bin per rank, child and prescription. ∎

The theorem is conditional on the semantic validity of cited deletion,
domination and auxiliary evidence.  The checker verifies that evidence identifiers
are present, not that their mathematical claims are true.

## 7. Executable endpoint

### Corollary CMR1909 -- PROVED

`check_geometric_owner_fate_manifest.py` provides an exact executable owner/fate
surface.

It:

1. enumerates every response matching;
2. recomputes all extendable prescriptions;
3. reconstructs every primitive rank-one, rank-two and rank-three witness;
4. requires a strict total order on all extendable edges;
5. recomputes the unique last-entering owner;
6. validates recurrent owner preservation;
7. validates transfer-role and stratum syntax;
8. requires one explicit fate for every witness;
9. exports the labelled integer coefficient bins.

Its deterministic self-test checks 400 systems containing 5,586 primitive
witnesses, partitioned as:

| fate | witnesses |
|---|---:|
| retained | 1,552 |
| transferred | 1,461 |
| dominated | 1,339 |
| deleted | 1,234 |

It also rejects eleven independently corrupted manifests.

The current semantic frontier is now narrower: supply rule-specific proofs for
every deletion, domination and auxiliary transfer, and attach the remaining
collision, local-line, interface, root, thin and CRT labels without altering the
owner partition.

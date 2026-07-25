# Coarse prefix resets have an exact fine-token reintroduction profile

CMR347--CMR350 isolate token-compatible edge reintroduction as one dynamic
source of repeated thin-blocker visits.  This chapter computes that source for
old-cell-clean prefix rematchings.  One coarse move can return only one old
matching edge for each row in the relevant finer residue class.  Consequently
one descending pass has only linear-polylogarithmic token-labelled return mass.

Work in a normalized inherited parent board of side

\[
t=p^h,
\]

with `p` an odd prime.  A depth-`r` prefix block has `t/p^r` columns.  In the
recursive prefix schedule its row set is a complete row fibre

\[
R_{r,a,\ell}
=
\{y:y\equiv \rho_{r,\ell}(a)\pmod {p^r}\},
\]

where, for fixed `r` and layer `ell`, the map `a -> rho_{r,a,ell}` is a
permutation of the `p^r` residues.  CMR93--CMR94 preserve these row fibres while
finer blocks are processed.

Fix a finer row-prefix direction token

\[
\tau=(b,c,\theta),
\qquad
1\le b<h,
\qquad
c\in\mathbb Z/p^b\mathbb Z.
\]

As in CMR348, its ambient endpoint universe is

\[
U_\tau
=
\{(x,y)\in[t]^2:y\equiv c\pmod {p^b}\}.
\]

The direction `theta` labels geometric certificates but does not alter the edge
count.

## 1. Exact host churn under one old-cell-clean rematching

Let `B` be a set of `q` columns and `R` a set of `q` rows.  Write

\[
K=B\times R.
\]

Let `M` be the current matching of the moving layer on `K`, and let `L` be the
partial matching formed by forbidden opposite-layer cells which lie in `K`.
Saturation gives

\[
M\cap L=\varnothing.
\]

Let `M'` be an old-cell-clean replacement matching satisfying

\[
M'\cap(M\cup L)=\varnothing.
\]

Put

\[
H=K\setminus(M\cup L),
\qquad
H'=K\setminus(M'\cup L).
\]

### Theorem CMR351 — PROVED

The allowed matching host changes by the exact identities

\[
\boxed{H'\setminus H=M},
\qquad
\boxed{H\setminus H'=M'}.
\]

Thus every old moving-layer cell becomes newly allowed, and no other edge is
reintroduced by this one-layer reset.

The coordinate-dual statement holds when the opposite layer is rematched while
the layer whose host is being measured is fixed: the old opposite-layer
forbidden matching is exactly the set returned to the host, except for cells
outside the measured row set.

### Proof

An edge belongs to `H'\H` exactly when it is excluded by `M union L` but not by
`M' union L`.  The three matchings are pairwise disjoint on their common host,
so this set is exactly `M`.  The reverse difference is symmetric.  For an
opposite-layer reset, interchange the roles of the moving forbidden matching
and the fixed matching. ∎

This theorem is a host statement.  If a residual deletion mask `D` is retained
through the reset, then the actual available sets are `H\D` and `H'\D`, and the
returned set is `M\D`.  Hence all later bounds remain valid as upper bounds in
a peeled residual host.

## 2. One coarse block returns a flat fine-depth profile

Consider a depth-`r` prefix block, with

\[
0\le r<b.
\]

Its size is

\[
q=\frac{t}{p^r}.
\]

Call the block **tau-compatible** when its row-fibre residue extends the token
residue at the coarse depth:

\[
\rho_{r,a,\ell}\equiv c\pmod {p^r}.
\]

### Theorem CMR352 — PROVED

An old-cell-clean one-layer rematching of a tau-compatible depth-`r` block
reintroduces exactly

\[
\boxed{
\frac{q}{p^{b-r}}
=
\frac{t}{p^b}
}
\]

old matching edges in `U_tau` at the full host level.  A noncompatible block
reintroduces none.

With an arbitrary persistent residual deletion mask, the actual number of
returned available edges in `U_tau` is at most `t/p^b`.

### Proof

The old matching is a bijection from the `q` block columns to the complete row
fibre `R`.  If the coarse row residue is incompatible with `c`, no row of `R`
has residue `c modulo p^b`.  If it is compatible, exactly

\[
\frac{q}{p^{b-r}}
\]

rows of `R` extend the fixed coarse residue to `c modulo p^b`.  The matching
uses each such row exactly once.  Apply CMR351.  A retained deletion mask can
only suppress returned edges. ∎

The count is independent of the coarse depth `r`.  A coarser block is larger,
but its rows are spread across proportionally more depth-`b` residue classes.

## 3. Ancestor-reset factorization

Follow a descending prefix schedule.  Once a depth-`b` token has been exposed,
only later repairs at depths `r<b` are coarser than that token.  For every
`r<b` and moving layer `ell`, the quotient row-prefix permutation gives one
unique depth-`r` block whose row fibre is tau-compatible.

Let

\[
A_{\tau,r,\ell}
\]

be the number of old-cell-clean rematchings of that compatible block after the
token is exposed.  Include an opposite-layer rematching only when its forbidden
matching meets the measured layer host.  Put

\[
A_\tau
=
\sum_{r=0}^{b-1}\sum_{\ell=0}^1 A_{\tau,r,\ell}.
\]

### Theorem CMR353 — PROVED UNDER THE DESCENDING PREFIX SCHEDULE

The coarse-reset contribution to the CMR347 reintroduction mass satisfies

\[
\boxed{
I_\tau^{\mathrm{coarse}}
\le
\frac{t}{p^b}A_\tau.
}
\]

At the unpeeled full-host level, equality holds whenever every counted moving
matching is relevant to the measured host.

### Proof

CMR94 preserves the depth-`r` quotient row fibres until scale `r` is processed,
so there is one compatible block per relevant moving layer.  CMR352 bounds each
such reset by `t/p^b`.  Sum with multiplicity.  CMR351 gives equality before
independent residual deletions suppress returned edges. ∎

Thus the previously abstract edge-return term factors into a universal
per-reset capacity and an explicit count of compatible ancestor resets.

## 4. One-pass fine-to-coarse budget

A **one-pass schedule** rematches every depth-`r` block in each layer at most
once before moving to a coarser depth.  It need not rematch every block.

### Theorem CMR354 — PROVED UNDER THE ONE-PASS HYPOTHESIS

For every token `tau=(b,c,theta)`,

\[
\boxed{A_\tau\le 2b}
\]

and therefore

\[
\boxed{
I_\tau^{\mathrm{coarse}}
\le
\frac{2bt}{p^b}.
}
\]

Combining with CMR347 gives the executable token-endpoint bound

\[
\boxed{
D_\tau
\le
\frac{t^2}{p^b}
+
\frac{2bt}{p^b}.
}
\]

If only the measured layer is rematched, every displayed factor `2` may be
removed.

### Proof

There are `b` coarser depths `r=0,...,b-1` and at most two relevant moving
layers.  At each depth and layer there is one compatible block, used at most
once.  Apply CMR353 and then CMR347. ∎

The token-labelled aggregate is also explicit.

### Corollary CMR355 — PROVED UNDER THE ONE-PASS HYPOTHESIS

Summing over every nonroot token in the parent block gives

\[
\boxed{
\sum_{\theta\in\mathbb P^1(\mathbb F_p)}
\sum_{b=1}^{h-1}
\sum_{c\bmod p^b}
I_{(b,c,\theta)}^{\mathrm{coarse}}
\le
(p+1)t\,h(h-1).
}
\]

For fixed prime base this is

\[
O_p\!\left(t\log^2 t\right).
\]

### Proof

At depth `b` there are `p^b` row residues and `p+1` projective directions.
CMR354 contributes at most `2bt/p^b` to each token.  Hence the depth-`b` sum is
at most

\[
2(p+1)bt.
\]

Finally

\[
2\sum_{b=1}^{h-1}b=h(h-1).
\]

∎

This is a labelled upper bound: one returned edge may be counted once for every
direction.  It is therefore safe even before geometric direction support is
used.

## 5. Repeated reset is the only unbounded coarse source

The one-pass hypothesis can be removed at the price of recording reset
multiplicity.

### Theorem CMR356 — PROVED

Fix an integer `m>=0`.  If every tau-compatible depth-layer block is rematched
at most `m` times after the token is exposed, then

\[
\boxed{
I_\tau^{\mathrm{coarse}}
\le
\frac{2bmt}{p^b}
}
\]

and

\[
\boxed{
D_\tau
\le
\frac{t^2}{p^b}
+
\frac{2bmt}{p^b}.
}
\]

Conversely, if either inequality fails, some one of the at most `2b`
compatible depth-layer blocks has been rematched more than `m` times.

### Proof

The multiplicity assumption gives `A_tau<=2bm`.  Apply CMR353 and CMR347.  The
converse is the contrapositive. ∎

CMR350's exact two-step return uses precisely the mechanism isolated here: the
same ancestor host is reset again.  Static token recurrence is therefore not
caused by a large number of unrelated fine cells; it is caused by repeated use
of one of finitely many compatible ancestor slots.

## 6. Witness visits are already executable continuations

The additive witness term in CMR349 is not an unclassified geometric family.
Its individual certificates obey the general primitive-line trichotomy of
CMR314--CMR342.

### Corollary CMR357 — PROVED

Every witness-escape certificate at a repeated token opens an executable CMR75
prefix continuation:

1. an external witness leaves at a strict earlier depth and preserves the Hall
   pair as the unique closest pair;
2. an internal non-equilateral witness transfers ownership to a strictly deeper
   closest pair; or
3. an equilateral witness lies wholly in one common prefix block.

A chain which repeatedly takes only the deeper internal alternative has length
at most `h-1-b`.

### Proof

Apply CMR315--CMR317 and CMR340--CMR343 to the individual compatible triple.
Those statements use only its primitive line parameters, not the heaviness of
the population from which it was selected. ∎

Thus the repeated-token frontier has two genuinely dynamic terms rather than
three:

- repeated resetting of one compatible ancestor depth-layer slot; and
- the width of the fully forced CMR217 exchange-ancestry DAG.

Witness escapes already supply an executable branch, although a global theorem
must still prevent those branches from returning through ancestor resets.

## 7. Revised frontier

For a single descending pass, coarse prefix recreation is now quantitatively
closed at `O_p(t log^2 t)` token-labelled mass.  For arbitrary closure histories,
CMR356 converts unbounded edge return into repeated use of one fixed ancestor
slot.  The next theorem should therefore attach a monotone payment to repeated
resets of that slot, for example:

1. coarse target load destroyed by the reset;
2. strict enlargement of the closure envelope;
3. an exchange-ancestry edge which has not appeared at that slot before; or
4. reserve consumption in exact high-band completion.

Joint-parent resets which do not preserve the recursive descendant fibres still
need a separate profile; CMR351 remains available there at the full envelope
scale.

No all-`n` theorem is claimed here.  Exact host churn, p-adic return profiles,
one-pass sums, and reset-multiplicity thresholds are checked in
[`scripts/verify_prime_power_coarse_reset_profile.py`](../scripts/verify_prime_power_coarse_reset_profile.py).

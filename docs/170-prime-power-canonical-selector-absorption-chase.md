# Persistent canonical selector edges admit a finite absorption chase or hit the protected trace core

CMR552--CMR557 reduce the dynamic side of a canonical selector to one exact
allowed edge which is repeatedly unavailable. The canonical forbidden matching
is an accounting choice and may be enlarged by a partial matching of recurrent
unavailable edges while preserving the paid-line trace.

A recurrent edge is absorbable precisely when it is vertex-disjoint from the
already protected partial matching. Every successful absorption increases that
matching by one edge, so at most `n-|Q_L|` such steps are possible. A
nonabsorbable recurrent edge shares a source or target vertex with the
paid-line trace or with an earlier absorbed edge, exposing a fixed row/column
contact signature.

Fix one envelope-labelled compatible paid pair and paid line, with residual
complete bipartite graph

\[
K=K_{n,n}.
\]

Let `Q=Q_L` be the residual paid-line trace and put

\[
\ell=|Q|.
\]

A protected absorption set `R` is a partial matching vertex-disjoint from `Q`.
Put

\[
P=Q\cup R.
\]

## 1. Canonical protected extension

### Theorem CMR571 — PROVED

Every protected partial matching `P` has a canonical perfect-matching extension

\[
\boxed{F_P}
\]

obtained by retaining `P` and matching the unused source and target lists in
increasing order.

The cylinder

\[
\mathcal D_P
=
\{\delta\in\operatorname{PM}(K):\delta\cap F_P=\varnothing\}
\]

has exact size

\[
\boxed{|\mathcal D_P|=D_n.}
\]

Every cylinder state avoids every residual paid-line cell and every absorbed
edge of `R`.

### Proof

The two sides have equal numbers of unused vertices. Pairing their ordered
lists extends `P` to a perfect matching. Relabel `F_P` as the identity; avoiding
perfect matchings are exactly the `D_n` derangements. Since `Q\cup R\subseteq
F_P`, all protected edges are avoided. ∎

## 2. Exact criterion for one more absorption

Let `f=uv` be a residual edge not already in `F_P`.

### Theorem CMR572 — PROVED

There exists a perfect matching extending `P\cup\{f\}` if and only if

\[
\boxed{\{u,v\}\cap V(P)=\varnothing.}
\]

In the affirmative case, the order-preserving extension gives a canonical new
cylinder of size `D_n` which avoids `f` at zero residual restoration cost.

In the negative case, `f` shares at least one endpoint with the unique
protected edge of `P` at that endpoint.

### Proof

If `f` meets `V(P)`, then `P\cup\{f\}` is not a partial matching. If it is
disjoint, it is a partial matching in the complete residual graph and extends
by matching the unused ordered lists. Apply CMR571. ∎

## 3. Protected-core contact signatures

Call `f` blocked by `P` when it fails CMR572.

### Theorem CMR573 — PROVED

Every blocked edge has one or two exact contact signatures

\[
\boxed{(f,r,\varepsilon),}
\]

where `r\in P` is the unique protected edge sharing the relevant endpoint and

\[
\varepsilon\in\{\mathrm{source},\mathrm{target}\}.
\]

For a protected matching of size `k=|P|`, every blocked edge meets one of the
`2k` protected vertices. Hence any set `B` of distinct blocked edges contains
one protected source or target vertex incident with at least

\[
\boxed{\left\lceil\frac{|B|}{2k}\right\rceil}
\]

members.

### Proof

CMR572 gives a shared endpoint and matching uniqueness gives the protected edge
at that endpoint. The cover and degree bound follow by pigeonhole over
`V(P)`. ∎

When `r\in Q`, this is a paid-line trace contact. When `r\in R`, it is contact
with an earlier absorbed recurrent edge.

## 4. One-stage dynamic endpoint

At a fixed protected state `P`, let its canonical profile be dynamic with
threshold `H_P>=1` as in CMR554.

### Theorem CMR574 — PROVED

Fix `\lambda>=2`. For any collection of failed occurrences of the selector
owned by `P`, at least one of the following holds.

1. **Finite stage history.** The number of failures is at most
   \[
   \boxed{
   \frac{(\lambda-1)n(n-1)}{H_P}
   \le(\lambda-1)n(n-1).
   }
   \]
2. **Reintroduction payment.** One canonical allowed edge recurs and pays many
   absent-to-present returns.
3. **Persistent absorbable edge.** One recurrent edge stays unavailable on a
   long interval and is disjoint from `P`; add it to `R` by CMR572.
4. **Persistent protected-core contact.** One recurrent edge stays unavailable
   on a long interval and is blocked by `P`, giving CMR573.

### Proof

Apply CMR555. In the recurrence branch apply the absence-run theorem CMR519,
then CMR572. ∎

## 5. Finite-depth absorption chase

Start with `R_0=\varnothing`, `P_0=Q`. Whenever CMR574 gives a persistent
absorbable edge `f_i`, put

\[
R_{i+1}=R_i\cup\{f_i\},
\qquad
P_{i+1}=Q\cup R_{i+1}.
\]

### Theorem CMR575 — PROVED

The chase has at most

\[
\boxed{n-\ell}
\]

successful growth steps.

Before static collateral, reintroduction payment, or protected-core contact,
the total number of nonrecurrent failed occurrences across all stages is at
most

\[
\boxed{
(\lambda-1)n(n-1)(n-\ell+1).
}
\]

### Proof

Every successful step adds one edge to a partial matching containing `Q`, so
`|R|\le n-\ell`. There are at most `n-\ell+1` visited states. Sum the coarse
CMR574 finite-stage bound over them. ∎

## 6. Unified canonical-selector endpoint

### Corollary CMR576 — PROVED

The repeated-failure history of one base canonical selector reaches at least
one of:

1. the CMR575 finite dynamic bound;
2. static collateral geometry from CMR570;
3. reintroduction/full-token return payment;
4. a persistent protected trace/core contact;
5. full absorption, where the protected matching has size `n` and every
   further allowed edge meets the protected core.

### Proof

Iterate CMR574 and use CMR575. A static state invokes CMR570. ∎

## 7. Revised frontier

Static collateral is converted to low-height lines, secant stars, matching
walls, heavy prefixes, dispersed carry cells, or the disjoint-conflict deletion
endpoint. Dynamic unavailability admits at most `n-|Q_L|` absorption steps and
polynomial nonrecurrent history. Every irreducible recurrent edge contacts one
fixed protected source or target vertex.

The remaining frontier is payment for repeated protected-core contacts and
reuse of the fixed wall/prefix/carry certificates. The expected alternatives
are Hall-wall concentration, protected-reserve loss, deletion ancestry,
full-token return, or envelope expansion.

No all-`n` theorem is claimed. Canonical extension, absorption, blocked-edge
covers, chase length, and accumulated history bounds are checked in
[`scripts/verify_prime_power_canonical_selector_absorption.py`](../scripts/verify_prime_power_canonical_selector_absorption.py).

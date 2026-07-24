# Alternating exchange ancestry for certificate deletion

CMR212 says that every edge of the half-degree parent host is initially
deletable. After several deletions, some remaining edge may become essential.
Its essentiality is not opaque: it is caused by the most recent deleted edge
through one alternating cycle.

## 1. One deletion creating one essential edge

### Theorem CMR215 — PROVED

Let `H` be a balanced bipartite graph with a perfect matching. Let `f` be an
edge such that `H-f` still has a perfect matching. Let `e!=f` be an edge which
is not essential in `H` but is essential in `H-f`.

Then:

1. every perfect matching of `H` which avoids `e` contains `f`;
2. for every
   \[
   M\in\operatorname{PM}(H-f)
   \]
   and every
   \[
   M'\in\operatorname{PM}(H),
   \qquad e\notin M',
   \]
   the alternating cycle of `M triangle M'` containing `e` also contains `f`.

In particular, immediately before the deletion, one alternating-cycle flip
exchanges `e` against `f`.

### Proof

If a perfect matching avoided both `e` and `f`, it would be a perfect matching
of `H-f` avoiding `e`, contradicting the essentiality of `e` there. This proves
the first assertion.

The symmetric difference of two perfect matchings is a disjoint union of even
alternating cycles. The matching `M` avoids `f`, while `M'` contains `f` by the
first assertion. Suppose the cycle containing `e` did not contain `f`. Flip
only that cycle in `M`. The resulting perfect matching still avoids `f`, hence
belongs to `H-f`, but it avoids `e`. This again contradicts essentiality in
`H-f`. ∎

## 2. First-essentiality time in a deletion sequence

Consider a sequence

\[
H_0\supset H_1\supset\cdots\supset H_m,
\qquad
H_i=H_{i-1}-f_i,
\]

where every `H_i` has at least one perfect matching.

### Theorem CMR216 — PROVED

Suppose an edge `e` is nonessential in `H_{i-1}` and essential in `H_i`.
Then `e` and `f_i` lie on one alternating cycle in `H_{i-1}`. Flipping that
cycle exchanges a perfect matching containing `e` and avoiding `f_i` with a
perfect matching avoiding `e` and containing `f_i`.

### Proof

Apply CMR215 with `H=H_{i-1}` and `f=f_i`. ∎

Assume now that `H_0` is the half-degree host from CMR208. By CMR212 it has no
essential edge. Hence every edge essential at a later time has a positive
**first-essentiality time** and one CMR216 exchange cycle attached to the
deletion at that time.

## 3. Certificate-directed deletion

At step `i`, suppose one chooses a candidate certificate `C_i` realized by a
perfect matching of `H_{i-1}`, chooses a prescribed cell `f_i in C_i`, and
deletes `f_i` while retaining a perfect matching. This is the CMR214
replacement rule whenever the current host still has no essential edge in the
chosen certificate.

### Theorem CMR217 — PROVED

Let `C_*` be a rank-`1/2/3` certificate realized by a perfect matching of
`H_m`. If every prescribed edge of `C_*` is essential in `H_m`, then for each
edge `e in C_*` there is an earlier index

\[
1\le\tau(e)\le m
\]

such that

1. `e` first becomes essential when `f_{tau(e)}` is deleted;
2. `e` and `f_{tau(e)}` lie on one alternating exchange cycle in
   `H_{tau(e)-1}`;
3. `f_{tau(e)}` belongs to the earlier certificate `C_{tau(e)}`.

Thus every fully forced terminal certificate has at most three directed
ancestry links to strictly earlier peeled certificates.

### Proof

Every edge of `C_*` is present in `H_m` and essential there, but no edge was
essential in `H_0`. Let `tau(e)` be the first index at which it is essential.
CMR216 gives the exchange cycle with `f_{tau(e)}`, and the certificate-directed
deletion rule gives the final assertion. ∎

## 4. Acyclic certificate ancestry

### Corollary CMR218 — PROVED

Orient every ancestry link from a later fully forced certificate to the earlier
certificate whose deleted cell created the relevant essential edge.

The resulting dependency graph is acyclic. Along every directed edge, the
deletion-time label strictly decreases. Every directed path has length at most
`m` and terminates at a certificate having a deletable prescribed cell at the
time it is processed.

### Proof

A link from `C_*` to `C_{tau(e)}` points to the deletion step `tau(e)` strictly
before the terminal time at which `C_*` is considered. Repeating the argument
strictly decreases a nonnegative integer time label, so directed cycles are
impossible and every path terminates. ∎

This is the first genuine no-return invariant inside the half-degree residual
host: candidate certificates may reappear geometrically, but their forced-cell
explanations cannot form a directed cycle within one deletion pass.

## 5. Revised internal endpoint

The remaining task is quantitative. One must combine the acyclic exchange
ancestry with the prime-power geometry:

- bound how many certificate descendants one deleted cell can create at one
  first-separation/carry signature;
- show that a long ancestry tree forces many distinct primitive directions or
  quotient cells;
- or resample the alternating exchange cycles simultaneously so that several
  terminal certificates are avoided at once.

CMR218 rules out circular dependence on previously deleted cells, but it does
not yet bound the width of the dependency DAG. That width is the current
fixed-envelope obstruction.

No all-`n` theorem is claimed here. The exchange-cycle assertion and ancestry
acyclicity are checked exhaustively in
[`scripts/verify_prime_power_exchange_ancestry.py`](../scripts/verify_prime_power_exchange_ancestry.py).

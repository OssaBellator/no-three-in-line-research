# A concentrated support atom batches many candidates through one edge split

CMR878--CMR885 show that every long stable-owner completeness path concentrates
many canonical new triples on one support atom. A support atom still may represent
a physical cell without a fixed layer label, or a matching vertex with several
incident cells. Finite local incidence converts either case to one exact labelled
edge repeated in many canonical triple prescriptions.

One binary prescription split on that edge then processes all associated
candidates simultaneously. The deletion branch removes every state using the
edge. The conditioned branch fixes and contracts the edge, lowering state
cardinality by one and turning every associated rank-three target into a
rank-two residual prescription.

Fix one labelled two-layer owner of side `n`, and let `\mathcal C_z` be `d`
distinct canonical labelled triples whose supports all contain one atom `z`.

## 1. Physical-cell concentration stabilises a layer label

### Theorem CMR886 -- PROVED

If `z` is one physical grid cell, then one of its two labelled layer edges occurs
in at least

\[
\boxed{\left\lceil\frac d2\right\rceil}
\]

triple prescriptions of `\mathcal C_z`.

### Proof

Every selected occurrence of the physical cell belongs to exactly one of the two
permutation layers. Partition the signatures by that layer label. ∎

## 2. Matching-vertex concentration stabilises an incident edge

### Theorem CMR887 -- PROVED

If `z` is one source or target vertex in one labelled layer, then one exact
labelled edge incident with `z` occurs in at least

\[
\boxed{\left\lceil\frac dn\right\rceil}
\]

triple prescriptions of `\mathcal C_z`.

### Proof

At a fixed source vertex, the incident selected edge is determined by one of at
most `n` target coordinates. At a fixed target vertex, it is determined by one
of at most `n` source coordinates. Partition and average. ∎

The distinct-cell wall branch of CMR874 is the case where this incidence is
spread among many exact edges.

## 3. Uniform labelled-edge concentration

### Corollary CMR888 -- PROVED

For either type of support atom, one exact labelled physical edge `e` belongs to
at least

\[
\boxed{
q
\ge
\left\lceil\frac{d}{2n}\right\rceil
}
\]

distinct canonical triple prescriptions.

### Proof

CMR886 gives the stronger divisor two and CMR887 gives the stronger divisor `n`.
Both imply the displayed uniform bound for `n>=1`. ∎

Retain the corresponding distinct triple family

\[
\mathcal C_e=\{C_1,\ldots,C_q\}.
\]

## 4. Exact binary edge split

For a feasible state family `\mathcal F`, define

\[
\mathcal F-e=\{R\in\mathcal F:e\notin R\},
\qquad
\mathcal F_e=\{R\in\mathcal F:e\in R\}.
\]

### Theorem CMR889 -- PROVED

One has the disjoint partition

\[
\boxed{
\mathcal F=(\mathcal F-e)\sqcup\mathcal F_e.
}
\]

Every candidate state whose canonical triple belongs to `\mathcal C_e` lies in
`\mathcal F_e` and is absent from `\mathcal F-e`.

### Proof

A labelled state either contains `e` or omits it, exclusively. Every triple in
`\mathcal C_e` contains `e`. ∎

Thus one edge decision batches all `q` candidate signatures.

## 5. Exact contraction of the conditioned edge

Define

\[
\mathcal F_e/e
=
\{R\setminus\{e\}:R\in\mathcal F_e\}.
\]

### Theorem CMR890 -- PROVED

Restriction gives an exact bijection

\[
\boxed{
\mathcal F_e
\cong
\{e\}\times(\mathcal F_e/e).
}
\]

The corresponding layer matching side decreases by one. The physical cell of
`e` remains unavailable to the opposite layer.

### Proof

Every conditioned state contains the same labelled edge. Remove its matching
endpoints in its own layer and retain its physical exclusion in the other layer.
Removing and adjoining `e` are inverse. ∎

## 6. Associated target triples become rank-two prescriptions

### Theorem CMR891 -- PROVED

For every `C_i\in\mathcal C_e`, the residual prescription

\[
P_i=C_i\setminus\{e\}
\]

has exactly two labelled edges and is compatible in the contracted joint-state
family. Moreover

\[
\boxed{
C_i\subseteq R
\iff
P_i\subseteq R\setminus\{e\}
}
\]

for every `R\in\mathcal F_e`.

### Proof

The original target has three compatible selected edges and contains `e`.
Removing one leaves a compatible rank-two partial joint state. The occurrence
identity is immediate from conditioning on `e`. ∎

The conditioned branch therefore enters the compatible-pair cylinder,
product-rectangle, essential-transfer, or pair-recurrence machinery.

## 7. Pair multiplicity or many distinct residual pairs

Let the `q` associated target signatures be distinct. Their residual pairs may
repeat.

### Theorem CMR892 -- PROVED

For every integer `lambda>=2`, at least one of the following holds.

1. One exact residual labelled pair occurs in at least `lambda` associated target
   signatures.
2. The number of distinct residual pairs is at least
   \[
   \boxed{
   \left\lceil\frac{q}{\lambda-1}\right\rceil.
   }
   \]

### Proof

Apply the multiplicity/support pigeonhole principle to the residual pair
signatures. ∎

The first branch is a fixed rank-two prescription; the second is a compatible
pair bank after the existing matching-vertex packing/cover extraction.

## 8. Support-atom batching endpoint

### Corollary CMR893 -- PROVED

If one support atom lies in `d` distinct canonical new-triple signatures, then a
single exact labelled edge batches at least `ceil(d/(2n))` of them. The complete
family has two exact continuations:

1. delete that edge, simultaneously removing all batched candidate states which
   use it;
2. condition on and contract that edge, converting all batched triples to
   rank-two residual pair signatures.

The conditioned pairs then yield exact pair recurrence, a large pair bank,
matching-vertex concentration, matching-preserving deletion, essential
contraction, or strict product descent. Hence repeated support concentration is a
branch-merging mechanism rather than a new source of width.

### Proof

Use CMR888--CMR892 and the rank-two endpoints CMR492--CMR545 and CMR629--CMR655.
∎

No all-`n` theorem is claimed. Atom-to-edge incidence, binary partitions,
conditioned contraction, rank-two transfer, and pair multiplicity are checked in
[`scripts/verify_prime_power_support_atom_edge_batching.py`](../scripts/verify_prime_power_support_atom_edge_batching.py).

# Canonical new triples pack disjointly or concentrate on one support atom

CMR862--CMR869 attach one canonical new labelled target triple to every
nonimproving target-destroying candidate. This chapter aggregates many such
signatures. Each triple is represented by its three physical cells and its six
layer-labelled matching endpoints. A maximal disjoint support packing gives
either many globally compatible rank-three prescriptions or a small cover which
concentrates many candidate signatures on one physical cell, source vertex, or
target vertex.

Fix one side-`n` labelled owner. The support universe consists of

1. the `n^2` physical grid cells;
2. the `2n` layer-labelled source vertices;
3. the `2n` layer-labelled target vertices.

Hence

\[
\boxed{|\Omega_n|=n^2+4n.}
\]

For a canonical new labelled triple `C`, define `\operatorname{supp}(C)` to be
its three physical cells together with the labelled source and target endpoint
of every one of its three labelled edges.

## 1. Every target support has size nine

### Theorem CMR870 -- PROVED

For every selected nonaxis target triple,

\[
\boxed{|\operatorname{supp}(C)|=9.}
\]

### Proof

The three physical target cells are distinct. Within each permutation layer,
selected edges have distinct sources and targets. Endpoints in different layers
remain distinct because the layer label is part of the support atom. Thus the
three labelled edges contribute six distinct endpoint atoms, disjoint in type
from the three physical-cell atoms. ∎

The support records physical layer-disjointness as well as matching
compatibility.

## 2. Exact multiplicity or many distinct triple signatures

Let `M` candidate episodes supply canonical labelled triples, counted with
multiplicity.

### Theorem CMR871 -- PROVED

For every integer `lambda>=2`, at least one of the following holds.

1. One exact labelled triple occurs in at least `lambda` episodes.
2. The number `L` of distinct labelled triple signatures satisfies
   \[
   \boxed{
   L\ge\left\lceil\frac{M}{\lambda-1}\right\rceil.
   }
   \]

### Proof

If every signature has multiplicity at most `lambda-1`, divide total multiplicity
by that bound. ∎

The recurrent-signature branch enters CMR770--CMR776 and the forced-triple
continuation CMR868.

## 3. Support matching or a small support cover

Let `\mathcal C` be a family of `L` distinct canonical triple signatures. Fix an
integer `s>=2`.

### Theorem CMR872 -- PROVED

At least one of the following holds.

1. **Disjoint support bank.** There are `s` triples whose nine-atom supports are
   pairwise disjoint.
2. **Small support cover.** There is a set `W\subseteq\Omega_n` with
   \[
   \boxed{|W|\le9(s-1)}
   \]
   meeting every support in `\mathcal C`.

### Proof

Take a maximal family of pairwise disjoint supports. If it has size at least `s`,
use the first branch. Otherwise the union of the maximal family has size at most
`9(s-1)`. Maximality implies every remaining support meets that union. ∎

This is an exact historical-signature statement; the triples need not occur in
one selected state.

## 4. Cover concentration

### Theorem CMR873 -- PROVED

In the small-cover branch, one support atom belongs to at least

\[
\boxed{
\left\lceil
\frac{L}{9(s-1)}
\right\rceil
}
\]

distinct canonical triple signatures.

The atom is exactly one of:

1. one physical grid cell;
2. one source vertex in one labelled layer;
3. one target vertex in one labelled layer.

### Proof

Assign every triple to the first cover atom in its support and average over at
most `9(s-1)` atoms. ∎

Thus support concentration is already a recurrent target cell or a labelled
matching-vertex fan.

## 5. Matching-vertex concentration refines to a wall or cell star

Suppose one labelled source or target vertex belongs to `d` distinct canonical
triple signatures. For every triple choose the incident physical cell on that
vertex.

### Theorem CMR874 -- PROVED

At least one of the following holds.

1. The signatures use at least
   \[
   \boxed{\lceil\sqrt d\rceil}
   \]
   distinct physical cells on the fixed row or column vertex.
2. One physical cell belongs to more than `\sqrt d` distinct canonical triple
   signatures.

### Proof

If `c` distinct cells are used and `c<\lceil\sqrt d\rceil`, one cell has
multiplicity at least `d/c>\sqrt d`. ∎

The first branch is a candidate wall with distinct cells; the second is an exact
repeated-cell target star.

## 6. A disjoint support bank is globally compatible

### Theorem CMR875 -- PROVED

If `C_1,...,C_s` have pairwise disjoint nine-atom supports, then the union of
their `3s` labelled edges

\[
P=C_1\sqcup\cdots\sqcup C_s
\]

is a compatible partial joint state:

1. within each layer, its source and target vertices are distinct;
2. no physical cell is used by both layers or by two prescriptions;
3. every triple remains one collinear rank-three subprescription.

### Proof

All possible matching and physical conflicts were included as support atoms.
Disjoint supports exclude each conflict. ∎

The theorem asserts compatibility, not automatic extension in the current host.
Extension enters the existing low-rank prescription, essentiality, and product
machinery.

## 7. Branch-path payment for disjoint canonical triples

Consider a completeness path which encounters and resolves the `s` rejected
candidate signatures of a disjoint support bank using CMR867.

### Theorem CMR876 -- PROVED

Before an owner or endpoint exit, each bank signature contributes at least one
of:

1. deletion of one labelled edge from its private three-edge prescription;
2. entry into its conditioned forced-triple branch;
3. contraction or loss of one of its support endpoints.

The deletion edges charged in branch 1 are distinct across the bank. The
conditioned triples in branch 2 are pairwise compatible and physically disjoint.

### Proof

CMR867 resolves a signature through one of its three deletion children or its
conditioned branch. Support disjointness makes deletion edges from different
triples distinct and gives the compatibility statement by CMR875. Endpoint loss
or owner change is the only way a later signature ceases to define the same
prescription. ∎

Hence a large disjoint bank consumes distinct deletion stock, produces several
independent forced certificates, or forces structural descent.

## 8. New-triple support endpoint

### Corollary CMR877 -- PROVED

A history of `M` nonimproving target-destroying candidates at one owner reaches,
for arbitrary thresholds `lambda,s>=2`, at least one of:

1. one exact labelled new triple in `lambda` episodes;
2. `s` pairwise support-disjoint canonical target triples;
3. one physical cell in at least
   \[
   \left\lceil
   \frac{1}{9(s-1)}
   \left\lceil\frac{M}{\lambda-1}\right\rceil
   \right\rceil
   \]
   distinct signatures;
4. one labelled matching vertex with the same incidence lower bound, refined by
   CMR874 to a distinct-cell wall or repeated-cell star;
5. finite distinct deletion payment, compatible forced-certificate packing,
   contraction, owner change, or strict potential improvement.

Thus a wide constant-arity completeness history exposes either independent
rank-three prescriptions or one exact geometric concentration. It cannot remain
an unstructured exponential branch tree.

### Proof

Apply CMR871, then CMR872--CMR876 to the distinct-signature family. ∎

No all-`n` theorem is claimed. Support sizes, multiplicity bounds, maximal
packing/cover, concentration, compatibility, and branch-payment arithmetic are
checked in
[`scripts/verify_prime_power_new_triple_support_packing.py`](../scripts/verify_prime_power_new_triple_support_packing.py).

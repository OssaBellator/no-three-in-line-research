# Fixed-interface and thin tables admit exact symmetry normalization

CMR1614--CMR1621 make every fixed-interface and bounded thin-side base table
finite.  A direct enumeration still repeats many rows that differ only by source
and target names.  This chapter proves an exact normalization and orbit rule.
Every opposite matching and forbidden target may be sent to one standard pair,
and the remaining stabilizer acts on deleted traces, fixed-interface
prescriptions and offspring labels without changing rook counts or response
probabilities.

The reduction is exact only when the retained geometric labels are relabelled
equivariantly.  It does not permit collision, local-line, owner or CRT provenance
to be discarded.

Let the source and target vertex sets both be `[d]={0,...,d-1}`.  A source
permutation `sigma` and target permutation `tau` act on an edge by

\[
(i,j)\longmapsto(\sigma(i),\tau(j)).
\]

## 1. Relabelling preserves matching data

### Theorem CMR1654 -- PROVED

For every bipartite edge set `E` and every pair of permutations `(sigma,tau)`,
relabelling gives bijections between:

1. partial matchings of every rank in `E`;
2. perfect matchings of `E`;
3. perfect matchings containing any compatible prescription `P`; and
4. perfect matchings of every contracted board `E/P`.

Consequently all rook numbers, perfect-matching counts and contracted
prescription probabilities are invariant under relabelling.

### Proof

Permutations are bijections on source and target vertices.  They preserve edge
incidence, disjointness, rank and containment.  Apply the inverse permutations
to obtain the inverse maps. ∎

In particular,

\[
\Pr(P\subseteq Q)
=
\Pr((\sigma,\tau)P\subseteq(\sigma,\tau)Q)
\]

under the relabelled response law.

## 2. Normalize the opposite matching

Let `O` be any perfect matching, written as a permutation

\[
O=\{(i,o(i)):i\in[d]\}.
\]

### Theorem CMR1655 -- PROVED

The target relabelling

\[
\tau=o^{-1}
\]

sends `O` to the identity matching

\[
I_d=\{(i,i):i\in[d]\}.
\]

### Proof

The edge `(i,o(i))` is sent to `(i,o^{-1}(o(i)))=(i,i)`. ∎

Thus the thin/interface table never needs to enumerate all `d!` opposite
matchings separately.

## 3. Normalize the forbidden target

After CMR1655, let the forbidden target edge be

\[
e=(a,c),
\qquad a\ne c,
\]

because `e` is disjoint from the identity opposite matching.

### Theorem CMR1656 -- PROVED

There is a simultaneous source-target permutation `pi` satisfying

\[
\pi(a)=0,
\qquad
\pi(c)=1.
\]

It preserves the identity matching and sends the target to

\[
\boxed{e_0=(0,1).}
\]

Consequently all pairs `(O,e)` with `e notin O` lie in one relabelling orbit.

### Proof

Choose any permutation with the displayed values.  Simultaneous relabelling
sends `(i,i)` to `(pi(i),pi(i))`, preserving the identity matching, and sends
`(a,c)` to `(0,1)`.  Combine with CMR1655. ∎

The raw factor

\[
d!\,d(d-1)
\]

of opposite-matching and target choices may therefore be replaced by one
normalized pair.

## 4. Residual stabilizer

Fix

\[
O=I_d,
\qquad e=e_0=(0,1).
\]

### Theorem CMR1657 -- PROVED

Every simultaneous permutation `pi` satisfying

\[
\pi(0)=0,
\qquad
\pi(1)=1
\]

preserves both `O` and `e_0`.  These permutations form a stabilizer isomorphic to

\[
\boxed{S_{d-2}.}
\]

It acts on deleted partial matchings, fixed-interface prescriptions, return
labels and offspring prescriptions.

### Proof

Such a permutation fixes the target endpoints and maps every identity edge to
another identity edge.  Its unrestricted action on `{2,...,d-1}` is exactly
`S_{d-2}`. ∎

Additional symmetries, such as layer transposition, may be used only when the
full labelled row is proved invariant under them.  They are not assumed here.

## 5. Canonical orbit code

For one normalized exact state, retain a finite labelled object

\[
\Sigma=(X,P,\lambda),
\]

where `X` is the deleted partial matching, `P` is the fixed-interface
prescription and `lambda` contains every retained owner, local-line, collision,
root, thin and CRT label.

Assume the labels have an explicit equivariant action under the stabilizer.
Define the canonical code

\[
\boxed{
\operatorname{can}(\Sigma)
=
\min_{\pi\in S_{d-2}}\operatorname{code}(\pi\Sigma)
}
\]

in any fixed lexicographic encoding.

### Theorem CMR1658 -- PROVED

Two normalized states in the same stabilizer orbit have the same canonical
code.  States with different canonical codes are never identified by this
normalization.

### Proof

The orbit of `pi Sigma` equals the orbit of `Sigma`; taking the minimum over the
same finite set gives the same code.  The second statement is immediate from
the definition. ∎

Canonical coding is a computational deduplication, not a projection which drops
labels.

## 6. Orbit-invariant response rows

Let a response law be equivariant: relabelling the parent state relabels its
response matching with the same probability.  Let offspring classes carry the
same label action.

### Theorem CMR1659 -- PROVED

All states in one stabilizer orbit have offspring rows which are permutations of
one another.  After indexing children by their canonical orbit codes, the rows
are identical.

Therefore one exact rational row need be computed per canonical parent orbit.

### Proof

CMR1654 gives a probability-preserving bijection of response matchings.
Equivariance preserves genuine-new-credit status, absolute last-entering owner
and all retained labels.  Thus offspring counts are transported bijectively and
canonical child codes agree by CMR1658. ∎

This is an exact symmetry quotient, unlike an unproved merging of unrelated
interface labels.

## 7. Certificate lifting from the orbit table

Let `A_orb` be the exact recurrent matrix indexed by canonical orbits and let
`A_lab` be the fully labelled matrix obtained by expanding every orbit.

### Theorem CMR1660 -- PROVED

If the response laws and offspring labels satisfy CMR1659, every positive strict
certificate

\[
A_{\rm orb}v<v
\]

lifts to a positive strict certificate for `A_lab` by assigning the same weight
to all labelled states in one orbit.

### Proof

Each labelled parent row has the same canonical child totals as its orbit row.
Substituting orbit-constant weights makes its weighted offspring sum equal to the
corresponding orbit-row sum. ∎

The lifted certificate may then enter the label-preserving SCC and CRT gluing
protocol of CMR1622--CMR1629.

## 8. Symmetry-normalized thin-table endpoint

### Corollary CMR1661 -- PROVED

For every fixed thin-side cap, the exact fixed-interface/thin table may be
constructed by the following smaller procedure.

1. Normalize the opposite matching to `I_d`.
2. Normalize the forbidden target to `(0,1)`.
3. Enumerate only deleted traces, interface prescriptions and retained labels.
4. Canonicalize them under the residual `S_{d-2}` stabilizer.
5. Compute one exact rook row per canonical orbit.
6. Search a strict rational or integer certificate on the orbit table.
7. Lift the certificate to the fully labelled table and then apply labelled SCC
   gluing.

This removes redundant vertex naming but preserves every collision, local-line,
owner and CRT label needed to determine future rows.  The remaining task is to
execute the normalized tables for the required thin regimes and prove their
orbit matrices subcritical.  No all-`n` theorem is claimed.

Normalization, stabilizer canonicalization, matching counts and exact
prescription-probability invariance are checked in
[`scripts/verify_prime_power_fixed_interface_symmetry_normalization.py`](../scripts/verify_prime_power_fixed_interface_symmetry_normalization.py).

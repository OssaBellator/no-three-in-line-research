# Finite strip words and the periodic transition quotient

BDA3c localizes a failed product bank once a finite profile map is
available. BDA1 already supplies a finite part of that profile. This note
separates that genuinely finite strip word from the still-unbounded
geometric address and records the exact recurrence consequence when the
full address is compressed.

## BDA3e -- finite intrinsic \(q\)-word

A replacement cell in a denominator-\(q\) chamber has the intrinsic
decoration

\[
\bigl(r,s,t'\bigr)
\in
(\mathbb Z/q\mathbb Z)^2
\times
(\mathbb Z/q\mathbb Z)^\times,
\]

where \(r,s\) are the two BDA1 strip residues and \(t'\) is the reduced
interpolation numerator. There are

\[
A_q=q^2\varphi(q)
\]

possible decorations.

For a collateral prescription using one, two, or three replacement
cells, record its positive block-rank pattern and list the cell
decorations, ordering blocks and cells by their active row coordinates.

### Lemma BDA3e -- PROVED

The resulting intrinsic \(q\)-word takes at most

\[
\boxed{
6\bigl(q^2\varphi(q)\bigr)^3
}
\]

values.

### Proof

BDA3d gives six positive block-rank patterns. A triple has at most three
replacement cells, each with one of \(A_q\) decorations. Padding words
of length one or two to length three only enlarges the count, so the
number of pattern--word pairs is at most \(6A_q^3\). The row order is
canonical because the selected blocks are row-disjoint and every local
state is a matching. \(\square\)

For the perfect chamber \(\mathcal C_{0,0}\), the two strip residues are
both zero, reducing the local alphabet to at most \(\varphi(q)\). The
larger bound is retained because translated and reverse-colour chambers
use the full BDA1 normalization.

The lemma is deliberately not called the complete BDA3 profile theorem.
A collateral triple also has a geometric address: block identities,
unchanged anchors, coarse carry quotients, and channel data. BDA3 still
has to show that this address either has \(O_q(1)\) effective types or
itself yields the periodic/paid structure required by BDA4.

## BDA4a -- finite transition-cycle reduction

Suppose the remaining arithmetic supplies a complete finite profile set
\(\Sigma_q\): two local configurations with the same profile have the
same allowed non-improving successor profiles and the same terminal
classification. Let \(Q_q\) be the directed graph of non-improving
profile transitions and put \(L_q=|\Sigma_q|\).

### Lemma BDA4a -- PROVED

Every non-improving trajectory of more than \(L_q\) transitions contains
a directed cycle of length at most \(L_q\). Consequently, if every
directed cycle of \(Q_q\) is either:

1. an explicitly absorbable periodic template; or
2. forced to spend current paid incidence from a finite nonreusable
   budget on each traversal,

then no unpaid unclassified trajectory can continue indefinitely.

If every profile has a unique nonterminal successor, the trajectory is
eventually periodic after fewer than \(L_q\) steps, with period at most
\(L_q\).

### Proof

Among the first \(L_q+1\) visited profiles, two are equal. The segment
between their first two occurrences is a directed closed walk and
contains a directed cycle of length at most \(L_q\). If successors are
unique, returning to the same profile forces the subsequent profile
sequence to repeat, giving eventual periodicity.

In the general directed case, an infinite trajectory still visits a
directed cycle. By hypothesis that cycle is absorbable or consumes paid
incidence. Repeated unpaid traversal of an unclassified cycle is
therefore impossible. \(\square\)

Thus BDA4 does not need to classify arbitrary infinite histories. It
needs a complete finite refinement of the intrinsic word and a
classification of the finitely many cycles in its transition quotient.

`scripts/verify_bda_finite_transition.py` checks the strip-word count and
exhaustively verifies eventual periodicity for every deterministic map on
at most four profiles.

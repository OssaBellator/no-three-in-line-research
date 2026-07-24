# Rank-three anchor-link extraction

AC1b gives exact anchor and anchor-pair incidence identities. For a heavy
rank-three anchor, the remaining purely combinatorial extraction can be
made exact by passing to its link graph.

Let \(\mathcal F\) be a family of three-anchor certificates and fix an
anchor cell \(v\). The link graph \(L_v\) has the other anchor cells as
vertices and has an edge \(\{x,y\}\) for every certificate
\(\{v,x,y\}\in\mathcal F\). Distinct three-point certificates give
distinct link edges, including when several certificates lie on one rich
line.

Write

\[
d(v)=|\mathcal F_v|,
\qquad
d(v,x)=|\{C\in\mathcal F:\{v,x\}\subseteq C\}|.
\]

## AC1c -- pair concentration or endpoint-disjoint star

### Lemma AC1c -- PROVED

For every integer \(\Delta\geq1\), one of the following holds:

1. some second anchor \(x\) satisfies
   \[
   d(v,x)>\Delta;
   \]
2. there is a subfamily \(\mathcal S\subseteq\mathcal F_v\) of size
   \[
   \boxed{
   |\mathcal S|
   \geq
   \frac{d(v)}{2\Delta-1}
   }
   \]
   such that any two certificates in \(\mathcal S\) intersect in the
   anchor \(v\) and no other anchor cell.

### Proof

The degree of \(x\) in \(L_v\) is exactly \(d(v,x)\). If the first
alternative fails, \(L_v\) has maximum degree at most \(\Delta\).

Greedily choose an edge of \(L_v\) and delete every edge meeting one of
its endpoints. A chosen edge deletes at most

\[
\deg(x)+\deg(y)-1\leq2\Delta-1
\]

edges, including itself. The resulting matching therefore has at least
\(d(v)/(2\Delta-1)\) edges. Translating those link edges back to
certificates gives the desired endpoint-disjoint star.
\(\square\)

The same argument for rank-two certificates is immediate: certificates
containing a fixed anchor already have distinct second anchor cells.

## Effect on AC1 and AC2

Combining AC1b and AC1c resolves the combinatorial part of the
one-anchor alternative. Once AC1's normalized heavy family has an anchor
of degree \(D\), it yields either:

- a pair with codegree greater than the chosen threshold, which is the
  input to the quotient/carry classification; or
- an endpoint-disjoint alternating star of size at least
  \(D/(2\Delta-1)\), which is a direct candidate for the AN3
  neutralization and AC2a compatibility machinery.

What remains arithmetic is to choose \(\Delta\) so that a high pair
codegree forces one of AC1's quotient, carry, or denominator labels, and
to attach current destroyed-incidence weight to the extracted star. The
link lemma preserves certificate multiplicity but does not manufacture
paid weight.

`scripts/verify_anchor_link.py` exhaustively checks the greedy matching
bound for all simple link graphs on at most six vertices.

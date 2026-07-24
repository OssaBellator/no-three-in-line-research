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

## AC1d -- paid anchor-link extraction

Give each certificate \(C\in\mathcal F_v\) a nonnegative current
destroyed-incidence weight \(w(C)\), and put

\[
W_v=\sum_{C\in\mathcal F_v}w(C).
\]

### Lemma AC1d -- PROVED

For every integer \(\Delta\geq1\), one of the following holds:

1. some second anchor \(x\) satisfies \(d(v,x)>\Delta\);
2. there is an endpoint-disjoint star
   \(\mathcal S\subseteq\mathcal F_v\) with
   \[
   \boxed{
   \sum_{C\in\mathcal S}w(C)
   \geq
   \frac{W_v}{2\Delta-1}.
   }
   \]

### Proof

If the first alternative fails, the link graph \(L_v\) has maximum
degree at most \(\Delta\). Order its edges arbitrarily and greedily give
each edge the first colour not used on an incident earlier edge. An edge
\(xy\) has at most

\[
(\deg(x)-1)+(\deg(y)-1)\leq2\Delta-2
\]

incident edges, so at most \(2\Delta-1\) colours are used. Every colour
class is a matching and hence gives an endpoint-disjoint star. The
weights of the colour classes sum to \(W_v\), so a heaviest class has
weight at least \(W_v/(2\Delta-1)\). \(\square\)

## Effect on AC1 and AC2

Combining AC1b and AC1c resolves the combinatorial part of the
one-anchor alternative. Once AC1's normalized heavy family has an anchor
of degree \(D\), it yields either:

- a pair with codegree greater than the chosen threshold, which is the
  input to the quotient/carry classification; or
- an endpoint-disjoint alternating star of size at least
  \(D/(2\Delta-1)\), which is a direct candidate for the AN3
  neutralization and AC2a compatibility machinery.

AC1d strengthens the second alternative: when the heavy family is
already weighted by current destroyed incidence, the extracted star
retains at least a \(1/(2\Delta-1)\) fraction of that paid mass. Thus no
separate paid-weight conversion is needed in the bounded-pair-codegree
case. What remains arithmetic is to choose \(\Delta\) and convert the
high-codegree alternative into a quotient, carry, or denominator class
that itself retains current paid incidence. Neither link lemma
manufactures paid weight if its input weights are merely latent
candidate counts.

`scripts/verify_anchor_link.py` exhaustively checks both the maximal
matching bound and the \(2\Delta-1\)-colour weighted partition for all
simple link graphs on at most six vertices.

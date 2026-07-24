# Fixed-rank, two-layer, and conflict-mass composition

This note proves the probabilistic implications in SAS3--SAS5. The
host-specific work remains in SAS1--SAS2: one must construct a measure
satisfying the conditional edge bound and prove that it survives deletion
of the first matching.

## SAS3a -- conditional edge bounds imply fixed-rank spread

Let \(M\) be a random perfect matching. Fix \(s\geq1\), and suppose that
for every compatible matching \(Q\) with \(|Q|<s\) and every edge \(e\)
compatible with \(Q\),

\[
\Pr(e\in M\mid Q\subseteq M)\leq \frac Cd
\]

whenever the conditioning event has positive probability.

### Lemma SAS3a -- PROVED

For every matching \(F\) with \(|F|\leq s\),

\[
\boxed{\Pr(F\subseteq M)\leq(C/d)^{|F|}.}
\]

### Proof

Order the edges \(F=\{e_1,\ldots,e_k\}\). The chain rule gives

\[
\Pr(F\subseteq M)
=
\prod_{i=1}^k
\Pr(e_i\in M\mid e_1,\ldots,e_{i-1}\in M).
\]

Every factor is at most \(C/d\) by hypothesis. If a conditioning event has
probability zero, the desired cylinder probability is already zero.
\(\square\)

This identifies the exact stability obligation in SAS3. An unconditional
one-edge estimate is insufficient; it must hold after deleting the
vertices of every prescribed matching of rank at most \(s-1\).

## SAS4a -- two-layer spread composition

Let \(M_1\) be a random perfect matching and, conditional on \(M_1\), let
\(M_2\) be an edge-disjoint random perfect matching. Assume

\[
\Pr(Q\subseteq M_1)\leq(C/d)^{|Q|}
\]

for every matching \(Q\), and, almost surely in \(M_1\),

\[
\Pr(Q\subseteq M_2\mid M_1)\leq(C/d)^{|Q|}
\]

for every matching \(Q\subseteq E\setminus M_1\).

### Theorem SAS4a -- PROVED

For every edge set \(F\),

\[
\boxed{
\Pr(F\subseteq M_1\cup M_2)
\leq
\left(\frac{2C}{d}\right)^{|F|}.
}
\]

Moreover \(M_1\cup M_2\) is a simple graph with degree exactly two at every
row and column vertex.

### Proof

If \(F\subseteq M_1\cup M_2\), assigning each edge to a layer containing it
gives a map \(\chi:F\to\{1,2\}\). Put \(F_i=\chi^{-1}(i)\). For a fixed
assignment, if either \(F_i\) is not a matching, its event has probability
zero. Otherwise,

\[
\begin{aligned}
\Pr(F_1\subseteq M_1,\ F_2\subseteq M_2)
&=
\mathbb E\left[
\mathbf1_{\{F_1\subseteq M_1\}}
\Pr(F_2\subseteq M_2\mid M_1)
\right]\\
&\leq
(C/d)^{|F_2|}\Pr(F_1\subseteq M_1)\\
&\leq
(C/d)^{|F|}.
\end{aligned}
\]

If \(M_1\) happens to contain an edge of \(F_2\), edge-disjointness makes
the inner probability zero, so the same inequality applies. There are at
most \(2^{|F|}\) assignments. The union bound proves the displayed spread
estimate.

Each layer has degree one at every row and column, and edge-disjointness
prevents a doubled edge. Their union is therefore a simple 2-factor.
\(\square\)

The only unproved clause of the original SAS4 target is now the
host-specific assertion that \(G-M_1\) retains the SAS1 hypotheses and
admits the conditional measure above.

## SAS5a -- global conflict endpoint

Let \(\mathcal C\) be any family of forbidden edge sets.

### Corollary SAS5a -- PROVED

Under the hypotheses of SAS4a, if

\[
\sum_{F\in\mathcal C}
\left(\frac{2C}{d}\right)^{|F|}<1,
\]

then some simple saturated 2-factor avoids every member of
\(\mathcal C\).

### Proof

By SAS4a and the union bound, the probability that
\(M_1\cup M_2\) contains any forbidden set is strictly less than one.
Hence a conflict-free outcome has positive probability. The outcome is a
simple saturated 2-factor by SAS4a. \(\square\)

If \(\mathcal C\) consists of \(T(G)\) collinear candidate triples, the
explicit sufficient condition is

\[
\boxed{
T(G)<\frac{d^3}{(2C)^3}.
}
\]

Thus the \(T(G)<c d^3\) statement in SAS5 is valid with
\(c=(2C)^{-3}\) once the two conditional spread measures exist. Finding an
intended algebraic host with this triple count remains open.

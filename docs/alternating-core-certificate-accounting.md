# Normalized certificate accounting and finite signature exposure

This note proves two bookkeeping components of AC1 and AC3.  The results
preserve line-certificate multiplicity exactly.  They do not prove that a
heavy normalized family has quotient/carry structure, or that an exposed
signature cannot later be recycled.

## AC1a -- failure selects a normalized certificate rank

Retain the AN4 notation and put

\[
G=D_\star-F_\star,
\qquad
U_r=\frac{T_r}{(t)_r}
\quad (r=1,2,3),
\]

where \((t)_r=t(t-1)\cdots(t-r+1)\).  Thus

\[
\mathcal N=128(U_1+U_2+U_3).
\]

### Lemma AC1a -- PROVED

Assume \(G>0\) and no state in the AN3 bank lowers the triple potential.
Then

\[
\mathcal N\geq G,
\]

and for some \(r\in\{1,2,3\}\),

\[
\boxed{U_r\geq \frac{G}{384}.}
\]

If the rank-\(r\) certificates are partitioned into \(L\) labelled
families, one labelled family has normalized weight at least

\[
\boxed{\frac{G}{384L}.}
\]

### Proof

For every bank state,

\[
\Phi(S_\pi)-\Phi(S)
=
F_\star-D_\star+
\bigl(\Phi(S_\pi)-\Phi(Z)\bigr).
\]

The left side is nonnegative by hypothesis.  Averaging therefore gives

\[
\mathbb E[\Phi(S_\pi)-\Phi(Z)]\geq G.
\]

AN4 bounds the same expectation above by \(\mathcal N\), proving the first
inequality.  One of the three nonnegative \(U_r\) is at least one third of
their sum, so it is at least \(G/(3\cdot128)\).  Partitioning that family
and applying the pigeonhole principle proves the labelled conclusion.
\(\square\)

The relevant labels may include endpoint layer, ordered hyperbola channel
tuple, quotient-ratio cell, carry type, and wrap-center type.  AC1a remains
uniform whenever the number \(L\) of first-stage labels is bounded in the
bounded-channel universe.

## Exact incidence identities

Let \(\mathcal F\) be any rank-\(r\) certificate family, counted with the
same multiplicity as \(T_r\).  For an anchor-block cell \(v\), let
\(d(v)\) count certificates containing \(v\).  For compatible distinct
cells \(u,v\), let \(d(u,v)\) count certificates containing both.

### Lemma AC1b -- PROVED

\[
\boxed{\sum_v d(v)=r|\mathcal F|,}
\]

and, for \(r\geq2\),

\[
\boxed{\sum_{\{u,v\}}d(u,v)=\binom r2|\mathcal F|.}
\]

Consequently, for every threshold \(\Delta>0\), either some anchor cell has
degree at least \(\Delta\), or the anchor support of \(\mathcal F\) has
size greater than \(r|\mathcal F|/\Delta\).

### Proof

Count incident pairs \((C,v)\) with \(C\in\mathcal F\) and \(v\in C\) in
the two possible orders.  Each certificate contributes exactly \(r\)
incidences.  The pair identity is the same double count with unordered
pairs of its anchor cells.  If every degree is below \(\Delta\), the first
identity forces more than \(r|\mathcal F|/\Delta\) support cells.
\(\square\)

Certificates on a real line containing four or more selected points are
not collapsed into one line event here: each constituent triple remains a
separate member of \(\mathcal F\), exactly as in the definition of
\(\Phi\) and \(T_r\).

AC1a--AC1b reduce AC1 to its geometric step: a large labelled family with
dispersed anchor support must force quotient concentration, carry
concentration, or one reduced denominator.  No independence assertion is
used in this reduction.

## AC3a -- finite signature-exposure potential

Let \(\Sigma\) be the disjoint union of all signature types which AC2 is
allowed to expose.  Suppose every signature is encoded by at most \(k\)
integer coordinates in \([-p^2,p^2]\) and at most \(k\) labels from a set
of size \(L=p^{O(1)}\).  This includes product carries, same-channel cross
carries, coordinate carries, rational-center numerator/denominator data,
and bounded-channel/coset labels.

For a closure state \(s\), let \(E_s\subseteq\Sigma\) be the signatures
exposed so far and define

\[
\Xi_{\rm exp}(s)=|E_s|.
\]

### Lemma AC3a -- PROVED

\[
0\leq\Xi_{\rm exp}\leq
L^k(2p^2+1)^k=p^{O(1)}.
\]

If a nonterminal transition exposes a signature not in \(E_s\), then

\[
\Xi_{\rm exp}(s')\geq\Xi_{\rm exp}(s)+1.
\]

Previously exposed signatures never disappear from this potential.

### Proof

The encoding gives the displayed cardinality bound for \(\Sigma\).
Exposure history is updated by union,

\[
E_{s'}=E_s\cup E_{\rm new},
\]

so it is monotone, and a genuinely new signature increases its cardinality
by at least one. \(\square\)

AC3a proves properties 1--3 of the proposed potential for transitions
which return a new signature.  The unresolved no-recycling theorem must
show that every repeated-signature transition instead yields a paid bank,
a BDA delegation, or a classified rational-inverse exception.  Merely
re-encountering an old label cannot be charged as progress.

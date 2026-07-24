# Canonical primal completion of repair conflicts

AC3t--AC3u require a scope-complete conflict graph before a
same-token fan can be treated as a product of private states.  Listing
pairwise collisions by hand is unsafe: one new collinear triple may use
cells from three different repairs even though no two repairs share a
cell.

This note removes that logical gap.  Every potential term and every
local feasibility condition has a finite cell scope.  Project each such
scope onto all repair envelopes which it meets and replace that
incidence hyperedge by its clique.  An independent family in the
resulting primal graph has no cross-factor of any order.  Its
collateral is therefore exactly additive, not merely bounded by a
union estimate.

The construction is deliberately conservative.  Its graph may be
dense.  The last theorem below gives every dense return a finite
witness-incidence label so that AC2c--AC2d can process it without
forgetting current paid weight.  Bounding or arithmetically classifying
that dense return remains a separate obligation.

## Finite repair-factor systems

Let \(\Omega\) be a finite cell universe and let \(Z\subseteq\Omega\)
be a fixed common state.  A finite repair family \(\mathcal J\) has
private envelopes

\[
P_j\subseteq\Omega\setminus Z
\qquad (j\in\mathcal J)
\]

and finite local state families

\[
\mathcal X_j\subseteq 2^{P_j}.
\]

The envelope contains every cell which any local state of that repair
may install.  It is allowed to be larger than each individual state.

Write the potential as a finite sum of scoped factors

\[
\Phi(X)
=
\sum_{a\in\mathcal F}
\phi_a(X\cap Q_a),
\qquad
Q_a\subseteq\Omega.
\]

No sign or monotonicity assumption on \(\phi_a\) is needed for the
additivity theorem.  The triple potential is the special case in which
\(\mathcal F\) is the set of real-collinear triples,
\(Q_a=a\), and

\[
\phi_a(U)=w(a)\mathbf1_{a\subseteq U}.
\]

Thus a line containing more than three points contributes one factor
for every one of its three-subsets; rich-line multiplicity is retained
exactly.

Local feasibility conditions are represented in the same way.  A
constraint \(b\in\mathcal H\) has a finite scope \(R_b\subseteq\Omega\)
and an allowed relation

\[
\mathcal L_b\subseteq 2^{R_b}.
\]

A state \(X\) is legal for \(b\) when
\(X\cap R_b\in\mathcal L_b\).  Row, column, replacement-cell, and
protected-bank conditions all fit this form.  A genuinely global
condition can be represented with scope \(\Omega\); this remains exact,
but it correctly makes every pair of repairs which it can see
incompatible.

## The canonical primal graph

The **canonical primal conflict graph**
\(G_{\rm pr}\) has vertex set \(\mathcal J\).  Distinct repairs \(j,k\)
are adjacent when at least one of the following holds:

1. \(P_j\cap P_k\ne\varnothing\);
2. some potential scope \(Q_a\) meets both \(P_j\) and \(P_k\);
3. some constraint scope \(R_b\) meets both \(P_j\) and \(P_k\).

Paid-certificate overlap is added in AC3w below.  Equivalently, form
the incidence hypergraph whose hyperedges are the sets of repairs met
by an envelope cell, factor scope, or constraint scope, and replace
every hyperedge by a clique.  This is the ordinary primal, or
two-section, graph of that incidence system.

## AC3v -- exact scope completion

### Theorem AC3v -- PROVED

Let \(\mathcal I\subseteq\mathcal J\) be independent in
\(G_{\rm pr}\).  Choose \(S_j\in\mathcal X_j\) for every
\(j\in\mathcal I\).  Assume the following local legality condition for
every \(b\in\mathcal H\):

- if \(R_b\) meets no selected envelope, then
  \(Z\cap R_b\in\mathcal L_b\);
- if \(R_b\) meets the unique selected envelope \(P_j\), then
  \((Z\cup S_j)\cap R_b\in\mathcal L_b\).

Then:

1. the envelopes \(P_j\), \(j\in\mathcal I\), are pairwise disjoint;
2. the joint state
   \[
   Z\cup\bigcup_{j\in\mathcal I}S_j
   \]
   satisfies every constraint in \(\mathcal H\); and
3. the exact potential identity
   \[
   \boxed{
   \Phi\left(Z\cup\bigcup_{j\in\mathcal I}S_j\right)-\Phi(Z)
   =
   \sum_{j\in\mathcal I}
   \bigl(\Phi(Z\cup S_j)-\Phi(Z)\bigr)
   }
   \]
   holds.

In particular, no two-repair or higher-order cross-certificate is
omitted from the graph.

### Proof

The first assertion follows from conflict rule 1.

Fix a constraint \(b\).  Independence and conflict rule 3 imply that
\(R_b\) meets at most one selected envelope.  If it meets none, the
joint state's restriction to \(R_b\) equals \(Z\cap R_b\).  If it meets
only \(P_j\), that restriction equals
\((Z\cup S_j)\cap R_b\).  The corresponding local hypothesis makes it
legal in either case.  Notice that \(Z\) itself need not be a complete
exact cover: it may have a temporary hole in every row or column filled
by its unique selected repair.

It remains to prove the displayed identity.  Fix one potential factor
\(a\).  By conflict rule 2, \(Q_a\) meets at most one selected
envelope.  If it meets none, the contribution of \(a\) to both sides
is zero after subtracting its value on \(Z\).  If it meets only
\(P_j\), its restriction in the joint state is exactly its restriction
in \(Z\cup S_j\).  Every other one-repair difference for this factor is
zero.  Hence the identity holds factor by factor, and summing over
\(\mathcal F\) proves it.

Finally, if one factor scope meets \(m\geq2\) selected envelopes, rule 2
would place every pair of those repairs in a clique.  In particular, a
rank-three certificate with one cell in each of three envelopes
creates a triangle, so those three repairs cannot all belong to an
independent family. \(\square\)

### Before-and-after form

If \(S_j^-\) and \(S_j^+\) are two local states for every
\(j\in\mathcal I\), apply AC3v to both product states and subtract.  One
gets

\[
\boxed{
\Phi\left(Z\cup\bigcup_jS_j^+\right)
-
\Phi\left(Z\cup\bigcup_jS_j^-\right)
=
\sum_j
\bigl(
\Phi(Z\cup S_j^+)-\Phi(Z\cup S_j^-)
\bigr).
}
\]

Thus both created and destroyed certificate weights add exactly on an
independent family.

### Common-phase specialization

For AC3p--AC3u, let the common phase be
\(\alpha\in\mathcal A\) and replace \(Z\) by its common state
\(Z_\alpha\).  Let each \(P_j\) contain all private cells used by any
state at any common phase, and build one primal graph from these full
envelopes.  AC3v then holds separately for every \(\alpha\).

Against any fixed reference state \(Y\), put

\[
f(\alpha)=\Phi(Z_\alpha)-\Phi(Y)
\]

and

\[
c_j(\alpha,x)
=
\Phi(Z_\alpha\cup S_j(\alpha,x))-\Phi(Z_\alpha).
\]

For an independent fan the exact joint change is

\[
\boxed{
\Phi\left(
Z_\alpha\cup\bigcup_jS_j(\alpha,x_j)
\right)-\Phi(Y)
=
f(\alpha)+\sum_jc_j(\alpha,x_j).
}
\]

Consequently the additive collateral contract in AC3p.1 and AC3t is
not an extra probabilistic assumption for these finite scoped systems:
it follows from the canonical primal graph.  Upper bounds may replace
the exact \(c_j\)'s without changing that conclusion.

## AC3w -- exact paid-certificate accounting

Let \(\mathcal D\) be a finite set of current paid certificate tokens
with weights \(w(d)\geq0\).  Give repair \(j\) a private paid set
\(D_j\subseteq\mathcal D\), and let
\(D_\circ\subseteq\mathcal D\) be a common paid set, disjoint from every
\(D_j\).  Add the fourth conflict rule

\[
D_j\cap D_k\ne\varnothing
\quad\Longrightarrow\quad
jk\in E(G_{\rm pr}).
\]

### Theorem AC3w -- PROVED

For every independent family \(\mathcal I\),

\[
\boxed{
w\left(
D_\circ\cup\bigcup_{j\in\mathcal I}D_j
\right)
=
w(D_\circ)+
\sum_{j\in\mathcal I}w(D_j).
}
\]

If the chosen joint state destroys every certificate in the displayed
union, this is its exact certified paid weight.  In a shared-token fan,
take \(D_\circ=\{\pi\}\) and remove \(\pi\) from all private paid sets.
Then \(w(\pi)\) appears once, irrespective of the fan size.

### Proof

The fourth conflict rule makes the private sets \(D_j\),
\(j\in\mathcal I\), pairwise disjoint.  They are also disjoint from
\(D_\circ\) by definition.  Additivity of a weighted disjoint union
gives the identity. \(\square\)

Combining AC3v and AC3w gives the precise AC3p.1 comparison

\[
f(\alpha)+\sum_jc_j(\alpha,x_j)
<
w(D_\circ)+\sum_jw(D_j).
\]

For a pure same-token fan with no additional private paid
certificates, the right side is exactly \(w(\pi)\), not
\(|\mathcal I|w(\pi)\).

## Finite structural witness labels

The canonical graph can be too dense for direct AC2a extraction.  Its
edges nevertheless have finite, checkable causes.

Fix total orders on cells and on factor and constraint identifiers.
Also fix a declared common/fixed envelope \(B\), disjoint from all
private envelopes and containing every common state \(Z_\alpha\).
For an oriented pair \((j,k)\) with disjoint envelopes and a scoped
witness

\[
Q=\{e_1<\cdots<e_s\}
\]

meeting both envelopes, record the incidence word

\[
\tau_{j,k}(Q)\in
\{\mathtt J,\mathtt K,\mathtt B,\mathtt O\}^{s},
\]

where a cell is labelled by membership in \(P_j\), \(P_k\), \(B\), or
the remaining universe.  Because the envelopes and \(B\) are disjoint,
the label is unambiguous.  A cross-witness word contains both
\(\mathtt J\) and \(\mathtt K\).

Give each edge one canonical label by the following priority:

1. envelope overlap;
2. private paid-certificate overlap;
3. the kind and incidence word of the least potential-factor witness;
4. the kind and incidence word of the least constraint witness.

Only one cause is retained for descent; the graph itself still contains
every cause.

## AC3x -- finite labelled dense return

### Theorem AC3x -- PROVED

Suppose the scoped factor and constraint kinds form a set of size
\(q\), and every such scope has rank at most \(r\).  The canonical edge
labelling above uses at most

\[
\boxed{
T
\leq
2+
q\sum_{s=1}^{r}4^s
}
\]

labels.  For one rank-three certificate kind, there are at most
\(4^3=64\) incidence words, and only

\[
\boxed{
4^3-2\cdot3^3+2^3=18
}
\]

of them contain both endpoint symbols and can be cross-certificate
words.

Consequently, if positive object weights satisfy the AC2c overload

\[
\sum_{k\in N[j]}w(k)>K\,w(j),
\qquad K>1,
\]

then AC2d localizes more than

\[
\boxed{
\frac{K-1}{T}w(j)
}
\]

of neighbouring paid weight to one explicit structural label.  Within
that label class it returns AC2d's compatible paid family, heavier
neighbour, broad same-label star, or deeper restricted overload.

### Proof

For each rank \(s\), there are at most \(4^s\) words on the four-symbol
alphabet.  Sum over the possible ranks and \(q\) kinds, then add the
two overlap labels.  For \(s=3\), inclusion--exclusion gives
\(4^3-3^3-3^3+2^3=18\) words containing both
\(\mathtt J\) and \(\mathtt K\).

The canonical priority assigns one of these at most \(T\) labels to
every edge.  Apply AC2d to the overloaded closed neighbourhood.  Its
first pigeonhole inequality and its recursive alternatives are exactly
the stated conclusions. \(\square\)

The structural word records *how* a factor meets two repair envelopes;
it does not classify the slope, carry, quotient, denominator, or orbit
arithmetic of that factor.  AC3x therefore closes the scope audit and
preserves paid mass through a dense failure, but it does not claim the
remaining arithmetic classification.

## Concrete grid interface

For a finite grid closure move, take:

- \(\Omega\) to be the finite candidate-cell universe;
- \(\mathcal F\) to contain every real-collinear triple which can occur
  in that universe, with its exact syndrome weight;
- \(\mathcal H\) to contain all row, column, replacement-cell, and
  declared protected-bank scopes;
- \(P_j\) to be the union of the cells in every local state of repair
  \(j\); and
- \(D_j\) to contain every privately claimed current certificate.

This is an explicit finite construction, even when enumerating it is
expensive.  AC3v verifies scope completeness for every independent
family produced from it.  AC3w prevents double payment, and AC3x turns
density into a finite witness-labelled AC2d return.

AC3y--AC3z in
[`alternating-core-phase-sensitivity-localization.md`](alternating-core-phase-sensitivity-localization.md)
further reduce the same-token output.  Every phase-sensitive dense
class retains at least one ninth of its weight on one flipped block and
one discrepancy kind, and exact phase values compress to their
behavioral quotient.  The remaining frontier is completeness of the
concrete arithmetic chart, or classification of its explicit
same-label one-block derivative.

`scripts/verify_ac_primal_conflicts.py` exhausts arbitrary Boolean
factors on a four-cell system, grid factor/constraint states on a
\(3\times3\) universe, higher-order triple projection, paid-set
additivity, and the rank-three incidence-word count.

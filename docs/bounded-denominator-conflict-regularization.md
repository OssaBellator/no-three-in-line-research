# Linear-mass conflict regularization for chamber blocks

BDA2a supplies a valid local state bank on every selected chamber block.
The next issue is to choose many blocks with bounded labelled interaction.
The following deterministic lemma isolates the exact global estimate that
the \(q\)-stripe arithmetic must provide.

Let \(\mathcal B\) be \(n\) candidate blocks.  For distinct blocks
\(u,v\), let \(m(u,v)\) be the nonnegative integer multiplicity of their
support, pair-certificate, and triple-certificate conflicts.  Put

\[
M=\sum_{\{u,v\}\subseteq\mathcal B}m(u,v),
\qquad
\ell(v)=\sum_{u\neq v}m(u,v).
\]

All pairwise incompatibilities must receive positive multiplicity; labels
may contribute additional multiplicity.

## BDA3a -- sparse-conflict regularization

### Theorem BDA3a -- PROVED

Suppose

\[
M\leq Dn.
\]

Then there is a subfamily \(\mathcal R\subseteq\mathcal B\) with

\[
|\mathcal R|\geq\frac n2
\]

such that every block has internal conflict mass at most \(4D\).
Moreover, \(\mathcal R\) contains a pairwise compatible subfamily
\(\mathcal I\) of size

\[
\boxed{
|\mathcal I|
\geq
\frac{|\mathcal R|}{\lfloor4D\rfloor+1}
\geq
\frac{n}{2(\lfloor4D\rfloor+1)}.
}
\]

If blocks carry nonnegative paid weights \(w(v)\), then either

\[
\sum_{v\in\mathcal I}w(v)
\geq
\frac{\sum_{v\in\mathcal B}w(v)}
{2(\lfloor4D\rfloor+1)}
\]

for a compatible \(\mathcal I\), or more than half of the paid weight is
carried by blocks whose conflict load exceeds \(4D\).

### Proof

Double counting gives

\[
\sum_{v\in\mathcal B}\ell(v)=2M\leq2Dn.
\]

Fewer than \(n/2\) blocks can have load greater than \(4D\).  Let
\(\mathcal R\) contain the remaining blocks.  It has size at least
\(n/2\), and deleting other blocks can only lower its internal loads.

Because every incompatible neighbour contributes at least one unit of
integer conflict mass, the incompatibility graph induced by
\(\mathcal R\) has maximum degree at most \(\lfloor4D\rfloor\).  Greedy
colouring uses at most \(\lfloor4D\rfloor+1\) colours.  Its largest colour
class is a compatible family of the displayed size.

For the weighted assertion, if \(\mathcal R\) carries at least half of
the total paid weight, its heaviest colour class has at least the claimed
weight.  Otherwise the discarded high-load blocks carry more than half
of the weight, which is the second alternative.
\(\square\)

## Interface left to the \(q\)-stripe geometry

For fixed \(q\), a bound

\[
M\leq D_q n
\]

immediately gives the linear-size, \(O_q(1)\)-load compatible block family
requested in BDA3.  If this bound fails on the paid part, the theorem
returns a precise obstruction rather than a generic dense graph: positive
paid mass lies on blocks with superconstant labelled conflict load.  BDA3
must use the explicit wrap residues to convert that high-load alternative
into a \(q\)-periodic template.

This does not follow from bounded pair codegree, and the theorem does not
claim it does.  It reduces BDA3's combinatorial selection step to one
auditable arithmetic estimate on total labelled conflict mass.

`scripts/verify_bda_conflict_regularization.py` exhaustively checks the
regularization and colouring bounds for all simple conflict graphs on at
most six blocks.

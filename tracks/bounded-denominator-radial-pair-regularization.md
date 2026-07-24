# Co-anchored radial-pair load regularization

BDA4d extracts adjacent radial parameters \(h,h+q\) with one fixed
primitive factor pair

\[
d=(a,b),
\qquad
c=(u,v),
\]

and one common rank-one increment \(qdc^{\mathsf T}\).  That
type-level conclusion does not by itself say that occurrences of the
two relative addresses share an anchor.  This note treats the exact
next case: once paid co-anchored occurrences are available, their
supports can be regularized in rows and columns.  Bounded support load
yields a compatible subfamily, while high load forces an affine anchor
chain of one of five types.

For an integer anchor \(P=(x,y)\), define the anchored triple

\[
T_h(P)
=
\{P,\ P+hu\,d,\ P+hv\,d\}
\]

and the adjacent radial-pair support

\[
\boxed{
\mathcal R_h(P)=T_h(P)\cup T_{h+q}(P).
}
\]

It has at most five cells, corresponding to the roles

\[
\boxed{
0,\quad hu,\quad hv,\quad(h+q)u,\quad(h+q)v.
}
\]

The BDA3g hypotheses make \(a,b,u,v\) nonzero; coincident roles can only
decrease the support size.

For a family \(\mathcal F\) of co-anchored records \((P,h)\), meaning
that both triples in \(\mathcal R_h(P)\) are available occurrences, let
the load of a row or column be the number of records whose support meets
it.  Give every record an arbitrary nonnegative paid weight.

## BDA4e -- compatible family or affine anchor concentration

### Theorem BDA4e -- PROVED

Fix an integer threshold \(\Lambda\geq1\).

If every row and column has load at most \(\Lambda\), then the conflict
graph on \(\mathcal F\), joining two records when their supports share a
row or column, has maximum degree at most

\[
\boxed{10(\Lambda-1).}
\]

Consequently \(\mathcal F\) partitions into at most

\[
\boxed{10(\Lambda-1)+1}
\]

row-column-compatible subfamilies.  One subfamily carries at least

\[
\boxed{
\frac{1}{10(\Lambda-1)+1}
}
\]

of the total paid weight.

Otherwise a row or column has load \(L\geq\Lambda+1\).  At least
\(\lceil L/5\rceil\) of its incident records share one role.  Moreover,
one role carries at least one fifth of the total paid weight incident
to that coordinate.  Each selected role class has the following exact
form.  For a heavy row \(X\), its anchor first coordinates obey one of

\[
\boxed{
x=X
}
\]

or

\[
\boxed{
x=X-(h+s q)w a,
\qquad
s\in\{0,1\},
\quad
w\in\{u,v\}.
}
\]

For a heavy column \(Y\), the corresponding alternatives are

\[
\boxed{
y=Y
}
\]

or

\[
\boxed{
y=Y-(h+s q)w b,
\qquad
s\in\{0,1\},
\quad
w\in\{u,v\}.
}
\]

Thus failure of bounded-load compatibility returns a paid
one-dimensional affine anchor chain, not an unclassified translation
cloud.

### Proof

Every support uses at most five rows and five columns.  Fix one record.
Each of its rows is shared with at most \(\Lambda-1\) other records, and
the same is true of each column.  Taking the union of these possible
neighbours gives degree at most

\[
5(\Lambda-1)+5(\Lambda-1)=10(\Lambda-1).
\]

A graph of maximum degree \(\Delta\) is greedily
\((\Delta+1)\)-colourable.  Every colour class is row-column
compatible.  Since the classes partition the paid weight, a heaviest
class carries at least the reciprocal fraction displayed above.

Now let a row \(X\) meet \(L\) supports.  For each incident record,
choose one of its roles lying in that row.  There are at most five role
types, so one occurs at least \(\lceil L/5\rceil\) times.  The root role
has row coordinate \(x\).  A role indexed by
\((s,w)\in\{0,1\}\times\{u,v\}\) has row coordinate

\[
x+(h+s q)wa.
\]

Setting this equal to \(X\) gives exactly the asserted affine anchor
law.  The five role classes also partition the incident paid weight, so
a heaviest class carries at least one fifth of it.  The column proof is
identical with \(y,b,Y\) in place of \(x,a,X\). \(\square\)

## BDA4f -- capped paid co-anchor extraction

Fix the \(J\) radial slots in one residue class from BDA4d, ordered so
successive slots differ by \(q\).  Let \(\mathcal A\) be a set of
anchors.  For anchor \(P\) and slot \(j\), let

\[
0\leq w_{P,j}\leq\beta
\]

be the aggregate current paid weight of occurrences of that relative
type at \(P\).  Put

\[
W=\sum_{P\in\mathcal A}\sum_{j=1}^J w_{P,j}.
\]

Give an adjacent co-anchored pair \((j,j+1)\) the safely transferable
weight

\[
\min\{w_{P,j},w_{P,j+1}\}.
\]

### Theorem BDA4f -- PROVED

The total adjacent-pair overlap weight satisfies

\[
\boxed{
\Omega
=
\sum_{P\in\mathcal A}
\sum_{j=1}^{J-1}
\min\{w_{P,j},w_{P,j+1}\}
\geq
\bigl(2W-\beta|\mathcal A|(J+1)\bigr)_+.
}
\]

The radial edges at every anchor split into their odd and even parity
classes.  Each class uses every radial slot at most once.  Therefore one
global parity class is a family of radially disjoint co-anchored pairs
with paid weight at least

\[
\boxed{
\frac12
\bigl(2W-\beta|\mathcal A|(J+1)\bigr)_+.
}
\]

In particular, if for some \(\varepsilon>0\),

\[
W\geq
\left(\frac12+\varepsilon\right)
\beta|\mathcal A|(J+1),
\]

then one parity class carries at least

\[
\boxed{
\varepsilon\beta|\mathcal A|(J+1)
}
\]

of paid co-anchored pair weight.

### Proof

For one anchor, use the layer-cake representation

\[
w_j=\int_0^\beta\mathbf1_{\{w_j\geq t\}}\,dt.
\]

At level \(t\), let \(S_t\subseteq\{1,\ldots,J\}\) be the occupied
slots.  If \(S_t\) has \(R_t\) runs, the number \(e_t\) of occupied
adjacent pairs is

\[
e_t=|S_t|-R_t.
\]

The \(J-|S_t|\) empty slots give

\[
R_t\leq J-|S_t|+1,
\]

and hence

\[
e_t\geq2|S_t|-J-1.
\]

Integrating this inequality gives

\[
\begin{aligned}
\sum_{j=1}^{J-1}\min\{w_j,w_{j+1}\}
&=\int_0^\beta e_t\,dt\\
&\geq
2\sum_{j=1}^Jw_j-\beta(J+1).
\end{aligned}
\]

The left side is nonnegative, so the positive part may be inserted.
Sum over anchors and use
\(\sum_P(x_P)_+\geq(\sum_Px_P)_+\) to obtain the first box.

Odd path edges are vertex-disjoint, as are even path edges.  These two
classes partition \(\Omega\), so the heavier class carries at least
half.  Substitution of the density hypothesis proves the last
display. \(\square\)

## Interface to BDA2--BDA5

Combine BDA4d, BDA4f, and BDA4e on a dense fixed-atlas radial profile.

- If paid occupancy across anchors exceeds the BDA4f half-capacity
  threshold, a parity class supplies quantified co-anchored pairs.
- If their row and column loads are bounded, a constant fraction of
  that pair weight survives as a compatible product family.  Its
  normalized collateral can be tested directly by BDA3b.
- If a load is high, a constant share of that current incidence lies on
  one of five explicit affine anchor laws.  A second row/column
  concentration would fix both anchor coordinates as affine functions
  of \(h\), producing a single translated radial chain; otherwise the
  remaining free coordinate is the exact incidence that must be paid or
  regularized.

Below the BDA4f threshold, the paid radial profile obeys the explicit
low-occupancy inequality

\[
W<
\left(\frac12+\varepsilon\right)
\beta|\mathcal A|(J+1);
\]

this is now the precise dispersed-anchor alternative.  The missing BDA
absorber theorem is narrowed to bounding that alternative from the
syndrome incidence, treating the affine anchor chains returned by high
load, and proving the local state comparison for
\(qdc^{\mathsf T}\).

`scripts/verify_bda_radial_pair_regularization.py` enumerates small
anchored radial-pair families, checks the five-role support formula,
the degree and colouring bounds, paid-weight retention, every heavy
row/column affine anchor identity, and the capped weighted path-overlap
inequality.

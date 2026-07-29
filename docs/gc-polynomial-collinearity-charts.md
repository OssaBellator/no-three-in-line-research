# Polynomial motion charts for protected collinearity events

**Branch:** `research/geometric-cleaning`

GC4ap--GC4as derive a quadratic protected-address map when three cells move affinely in one operation parameter. This note extends the same mechanism to polynomial and piecewise-polynomial operation charts.

Let

\[
X_i(t)\in F[t]^2,
\qquad i=1,2,3,
\]

be polynomial cell trajectories over a field `F`. Put

\[
p=\deg(X_2-X_1),
\qquad
q=\deg(X_3-X_1),
\]

where vector degree is the maximum coordinate degree.

## GC4at -- polynomial collinearity degree bound -- PROVED

The collinearity polynomial

\[
F_X(t)=\det(X_2(t)-X_1(t),X_3(t)-X_1(t))
\]

has degree at most

\[
\boxed{p+q.}
\]

In particular, if every coordinate of every `X_i` has degree at most `d`, then

\[
\boxed{\deg F_X\le2d.}
\]

### Proof

Each determinant term is a product of one coordinate of `X_2-X_1` and one coordinate of `X_3-X_1`, so each term has degree at most `p+q`. Their difference has no larger degree. QED.

## GC4au -- exact polynomial-chart capacity -- PROVED

Suppose `F_X` is not the zero polynomial and at most `M_p` physical operations share one parameter value. Then one protected address represented by this chart has incidence at most

\[
\boxed{(p+q)M_p.}
\]

For a uniform degree-`d` chart this becomes `2dM_p`. Its exact top-weight capacity is therefore

\[
\boxed{H_p\le S_p((p+q)M_p).}
\]

### Proof

A nonzero degree-at-most-`p+q` polynomial has at most `p+q` roots in a field. Apply GC4am and GC4an. QED.

## GC4av -- coefficient-degeneracy router -- PROVED

Write

\[
F_X(t)=c_0+c_1t+\cdots+c_Dt^D,
\qquad D\le p+q.
\]

The chart is identically collinear exactly when

\[
\boxed{c_0=c_1=\cdots=c_D=0.}
\]

Otherwise its actual incidence bound may use `deg F_X` rather than the coarser value `p+q`.

### Proof

A polynomial is the zero polynomial exactly when every coefficient is zero. The sharper root count is its actual degree. QED.

## GC4aw -- piecewise-polynomial chart router -- PROVED

Suppose the physically eligible operations for address `p` split into `J` disjoint charts. Chart `j` has collinearity degree bound `D_j`, parameter multiplicity `M_j`, and eligible top-weight function `S_{p,j}`. If no chart is coefficient-degenerate, then

\[
\boxed{
|I_p|\le\sum_{j=1}^J D_jM_j
}
\]

and

\[
\boxed{
H_p
\le
\sum_{j=1}^J S_{p,j}(D_jM_j).
}
\]

If the charts share operations, first assign every operation to its least chart; failure of that assignment is one alias or chart-membership defect.

### Proof

Apply GC4au separately on the disjoint charts and sum. Least-chart assignment makes an overlapping chart family disjoint without losing occurrences. QED.

## GC4ax -- complete polynomial-event continuation -- PROVED

Every protected collinearity event with a finite polynomial chart dictionary has one exact continuation:

1. a nondegenerate chart contributes capacity `S_{p,j}(D_jM_j)`;
2. one chart has an identically-zero coefficient profile;
3. one physical parameter fibre exceeds `M_j`;
4. one trajectory exceeds its declared degree;
5. one field, chart, alias, lineage, context or eligible-weight record fails.

Thus non-affine polynomial event families are reduced to finite coefficient and multiplicity data.

## Corrected GC5 frontier

Affine and polynomial one-parameter collinearity events now have explicit capacities. Remaining work is to produce a finite chart dictionary for the actual cleaning operations, bound chart count, degree, fibre multiplicity and top eligible weights, and pay coefficient-degenerate charts, genuinely non-polynomial events or returned Hall cores.

## Finite check

`scripts/verify_gc_polynomial_collinearity_charts.py` exhausts small finite-field polynomial trajectories, checks the determinant degree bound, root counts, coefficient degeneracy and piecewise capacity sums.
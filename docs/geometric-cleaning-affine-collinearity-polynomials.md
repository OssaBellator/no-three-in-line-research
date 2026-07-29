# Quadratic address maps for affine collinearity events

**Branch:** `research/geometric-cleaning`

GC4al--GC4ao turn a nonzero scalar polynomial address equation into a protected-event incidence capacity. This note derives such equations for the basic geometric event in the cleaning argument: collinearity of cells moving affinely with one operation parameter.

Let

\[
X_i(t)=x_i+t u_i\in F^2,
\qquad i=1,2,3,
\]

where `F` is a field and `t` is the scalar operation parameter.

## GC4ap -- affine collinearity is quadratic -- PROVED

The three cells are collinear exactly when

\[
F_X(t)=\det(X_2(t)-X_1(t),X_3(t)-X_1(t))=0.
\]

Writing

\[
a_0=x_2-x_1,\quad a_1=u_2-u_1,
\qquad
b_0=x_3-x_1,\quad b_1=u_3-u_1,
\]

one has

\[
\boxed{
F_X(t)=c_0+c_1t+c_2t^2,
}
\]

with

\[
\boxed{
 c_0=\det(a_0,b_0),
\quad
 c_1=\det(a_1,b_0)+\det(a_0,b_1),
\quad
 c_2=\det(a_1,b_1).
}
\]

### Proof

Expand `det(a_0+t a_1,b_0+t b_1)` bilinearly. QED.

## GC4aq -- exact degeneracy profile -- PROVED

The collinearity equation is identically zero in `t` if and only if

\[
\boxed{c_0=c_1=c_2=0.}
\]

Otherwise it has at most two roots in `F`.

The three coefficient equalities are therefore the exact affine-family degeneracy profile: they say that the entire one-parameter family is collinear, rather than merely one or two operation states.

### Proof

A polynomial of degree at most two is the zero polynomial exactly when all three coefficients vanish. A nonzero degree-at-most-two polynomial over a field has at most two roots. QED.

## GC4ar -- quadratic protected-address capacity -- PROVED

Fix a protected line/certificate address `p`. Suppose every eligible operation has an affine parameterization as above, at most `M_p` physical operations share one parameter value, and the coefficient triple is not zero. Then

\[
\boxed{|I_p|\le2M_p.}
\]

If the eligible operation weights for `p` are ordered decreasingly, its exact certified capacity is

\[
\boxed{
H_p\le S_p(2M_p).
}
\]

If the polynomial is linear or constant nonzero, the sharper root count one or zero may be used.

### Proof

GC4ap--GC4aq give at most two parameter roots. Apply GC4am for physical parameter multiplicity and GC4an for top-weight capacity. QED.

## GC4as -- affine-event dictionary router -- PROVED

For a finite dictionary of affine collinearity addresses, each address has one exact continuation:

1. nondegenerate quadratic profile with incidence at most `2M_p`;
2. nondegenerate linear profile with incidence at most `M_p`;
3. nonzero constant profile with no eligible operation;
4. the exact coefficient-degeneracy profile `c_0=c_1=c_2=0`;
5. excessive physical parameter multiplicity;
6. failure of the affine chart, field, eligibility, alias, lineage, context or weight record.

Thus every protected event represented by three affine moving cells has an explicit degree-two capacity or one finite coefficient obstruction.

## Corrected GC5 frontier

The line-event polynomial map is now derived for affine one-parameter operation families. Remaining work is to put the actual cleaning operations into such affine charts, bound physical parameter multiplicities and eligible top weights, and pay the identically-collinear coefficient profiles, non-affine events or returned Hall cores.

## Finite check

`scripts/verify_gc_affine_collinearity_polynomials.py` exhausts small finite-field affine triples, checks the coefficient formula, root bound and coefficient-degeneracy equivalence.
# Duplicated-reservoir reduction for exact strong-complete completion

PX141 gives a pseudorandom almost-perfect matching in the strong-complete host

\[
e(x,y)=(x,y,x-y,x+y).
\]

The missing step is exact completion without reusing a column, difference, or
sum value already occupied by the first matching.  This chapter records a
standard two-stage encoding which separates the old and new reservoirs while
remembering projection collisions as mixed conflicts.

Let the common row class be

\[
P=\{R_x:x\in\mathbb F_p\}.
\]

Take two disjoint copies of the three non-row classes,

\[
Q=C^0\dot\cup D^0\dot\cup S^0,
\qquad
R=C^1\dot\cup D^1\dot\cup S^1.
\]

For every \(x,y\in\mathbb F_p\), define

\[
e_0(x,y)=\{R_x,C^0_y,D^0_{x-y},S^0_{x+y}\},
\]

and

\[
e_1(x,y)=\{R_x,C^1_y,D^1_{x-y},S^1_{x+y}\}.
\]

Write \(\mathcal H_1=\{e_0(x,y)\}\) and
\(\mathcal H_2=\{e_1(x,y)\}\).

A mixed pair \(\{e_0(x,y),e_1(x',y')\}\) is a **projection collision** when
at least one corresponding projected coordinate agrees:

\[
y=y',
\qquad
x-y=x'-y',
\qquad\text{or}\qquad
x+y=x'+y'.
\]

Only corresponding coordinate classes are compared.  Equality of, for
example, a column label with a difference label is irrelevant.

## Theorem PX158 -- PROVED

The duplicated host has the following exact parameters.

1. Every row vertex has degree \(p\) in each of \(\mathcal H_1\) and
   \(\mathcal H_2\).
2. Every non-row vertex has degree \(p\) in its own copy.
3. Each of \(\mathcal H_1\) and \(\mathcal H_2\) is linear: two vertices in
   distinct classes determine at most one edge.
4. A fixed completion edge \(e_1(x',y')\) has exactly

   \[
   \boxed{3p-2}
   \]

   projection-collision partners in \(\mathcal H_1\).
5. For a fixed old edge \(e_0(x,y)\) and a fixed completion row \(x'\), at
   most three edges of \(\mathcal H_2\) on row \(x'\) collide with it.
6. Consequently the total number of mixed collision pairs using one fixed
   completion row is

   \[
   \boxed{p(3p-2)}.
   \]

### Proof

The degree and linearity statements follow because any one coordinate leaves
one free field parameter, while any two of

\[
x,\quad y,\quad x-y,\quad x+y
\]

from distinct labelled classes determine \((x,y)\).

For one fixed completion edge, the three collision equations each define a
set of exactly \(p\) old edges.  Every pair of these equations determines the
same old edge \(e_0(x',y')\), so all three sets have the same unique common
intersection.  Inclusion-exclusion gives

\[
3p-3+1=3p-2.
\]

For a fixed old edge and completion row, each of the three equations determines
at most one completion column.  Summing the exact completion-edge degree over
the \(p\) edges of one row gives the final count. \(\square\)

## Theorem PX159 -- PROVED

Let \(M\subseteq\mathcal H_1\cup\mathcal H_2\) be a matching which covers every
row vertex exactly once and contains no projection-collision pair.  Project
both reservoir copies to the original labels:

\[
C^0_z,C^1_z\mapsto C_z,
\qquad
D^0_z,D^1_z\mapsto D_z,
\qquad
S^0_z,S^1_z\mapsto S_z.
\]

Then the projected edges form a perfect matching of the original
strong-complete host.  Equivalently, they define a strong-complete mapping of
\(\mathbb F_p\).

### Proof

There are exactly \(p\) selected edges, one for each row.  Inside each
reservoir copy, matching disjointness prevents repetition of a column,
difference, or sum coordinate.  Across the two copies, projection-collision
freeness prevents repetition after projection.  Thus each of the three
projected non-row classes contains \(p\) distinct selected labels and hence is
covered exactly once.  The projected set is therefore a perfect matching.
\(\square\)

## Relation to the conflict-free covering theorem

This is the tripartite architecture of Joos--Mubayi--Smith:

- \(P\) is the designated row class;
- \(\mathcal H_1\) uses one row and three vertices of \(Q\);
- \(\mathcal H_2\) uses one row and three vertices of \(R\).

With \(d=p\), the host is exactly regular, has pair codegree one, and satisfies

\[
\Delta_R(\mathcal H_2)=\delta_P(\mathcal H_2)=p,
\qquad
d_{\mathcal H_2}(x,v)\le1.
\]

The mixed projection collisions have one old and one new edge, so they belong
to the one-completion-edge extension of the theorem's conflict conditions,
not to the simplified condition which assumes at least two new edges.  PX158
provides the exact linear degree estimates needed for that check.

## Boundary

PX158--PX159 solve only the exact-cover bookkeeping.  They do not by themselves
preserve the secant and affine-triangle multiplicities from PX141.  Any exact
completion theorem must additionally control the new repeated-shape
occurrences introduced by \(\mathcal H_2\).

## Verification

Run

```bash
python scripts/verify_product_duplicated_reservoir.py
```

The verifier checks the exact collision degrees and exhausts small mixed
\(P\)-perfect matchings to confirm the projection theorem.

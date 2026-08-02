# Mixed-shape stars and exact subpower triangle completion

PX163 controls affine-triangle occurrences using three completion edges.  This
chapter handles the two mixed sectors and combines all previous ingredients to
obtain an exact strong-complete mapping with subpower affine-triangle
multiplicity.

Number the three roles of a labelled occurrence by

\[
0,1,2.
\]

For a role set \(I\subseteq\{0,1,2\}\), interpret the roles in \(I\) as old
edges from \(\mathcal H_1\) and the complementary roles as completion edges
from \(\mathcal H_2\).

## 1. Anchored secant tests

The same padded-weight method as PX161 also applies to rank-two secants.

## Theorem PX164 -- PROVED USING THE PX141 EXTERNAL INPUT

For every fixed \(\eta>0\), the first-stage almost-matching may be chosen so
that, simultaneously for every prospective completion edge \(e\), every
allowed scalar secant slope \(r\), and either role of the ordered secant,

\[
\boxed{
\#\{f\in M_1:\ (e,f)\text{ realizes the prescribed slope and roles}\}
\le p^\eta.
}
\]

### Proof

For fixed \((e,r,i)\), the raw one-edge test has exactly \(p-1\) host edges:
choose the nonzero row step, after which the prescribed slope fixes the image.
Pad it with a small multiple of the indicator of all host edges disjoint from
\(e\).  The padded weight has mass \(\Theta(p^{1+\eta/2})\), bounded atoms,
and no nontrivial lower-rank concentration condition.  It is therefore a
trackable one-uniform test in the matching theorem used by PX141.  There are
only \(O(p^3)\) such tests, so they may be included simultaneously.  The
resulting upper bound is \(O(p^{\eta/2})\), hence at most \(p^\eta\) for large
\(p\). \(\square\)

PX164 is recorded for the subsequent secant-completion stage.  The rest of this
chapter concerns affine triangles.

## 2. Five-occurrence star conflicts

Fix one compatible shape, one old-role pattern \(I\), and one centre role
\(c\).  A **five-star** consists of five distinct labelled occurrences which
all use the same graph edge in role \(c\), while their two-edge leaf sets are
pairwise disjoint.

Use the following centre patterns:

1. \(|I|=0\): all three centre roles;
2. \(|I|=1\): all three centre roles;
3. \(|I|=2\): only the two old centre roles.

The omitted case is a completion-centred star with two old leaves.  PX161
already bounds that completion-centred occurrence degree by \(p^\eta\), so no
one-completion-edge conflict is needed.

## Theorem PX165 -- PROVED

The union of all displayed five-star systems is simply bounded for the
duplicated host and every sufficiently large prime.

If a matching avoids these stars, then for every fixed affine shape:

- every graph edge has degree at most \(48\) in the all-completion occurrence
  sector;
- every graph edge has degree at most \(48\) in the one-old/two-completion
  sector;
- every old graph edge has degree at most \(32\) in the
  two-old/one-completion sector.

### Proof

Fix the shape, role pattern, centre role, and centre graph edge.  The nonzero
step determines one occurrence, so there are \(p-1\) possible occurrences.
After fixing one leaf graph edge, its role is one of two possibilities and the
step is determined.  Thus the link graph at the centre has maximum degree at
most two.

If it contains no matching of size five, a maximal link matching has at most
four edges and its at most eight vertices cover the link.  Hence the number of
occurrences centred at the fixed edge is at most

\[
8\cdot2=16.
\]

Summing over the possible centre roles and old-role patterns gives the stated
constants.

It remains to check boundedness.  A five-star contains

\[
1+2\cdot5=11
\]

graph edges.  Before fixing rows, it has at most

\[
C p^3\cdot p^2\cdot p^5=Cp^{10}
\]

parameter choices: shape, centre edge, and five steps.  Requiring one
completion row reduces this to \(O(p^9)\), and two completion rows reduce it to
\(O(p^8)\).

Suppose additionally that \(j'\) old graph edges are fixed.  In the centre
patterns retained above, every occurrence has at most one old leaf.  After the
shape is fixed, the first fixed old edge removes two scalar parameters, and
each later fixed old edge removes at least one further step parameter.  Thus
the one-row codegree is at most

\[
O(p^{9-j'}).
\]

The simply bounded thresholds for a conflict of total size eleven are

\[
p^{11+\varepsilon^4},
\qquad
p^{11-j'-\varepsilon},
\qquad
p^{11-\varepsilon},
\]

for the row degree, old-edge codegree, and two-row degree respectively.  The
three displayed counts have a polynomial margin of at least \(p^2\).
Therefore (D1)--(D4) hold. \(\square\)

## 3. Deterministic row buckets for mixed occurrences

Fix

\[
a\in\{1,2\}
\]

old roles, one distinguished old role among them, and put

\[
b=3-a.
\]

Partition the scalar rows into

\[
B=\lceil p^\beta\rceil
\]

balanced buckets, each of size at most \(\lceil p/B\rceil\).  Assign an
occurrence to the bucket containing the row of its distinguished old edge.

For each affine shape, role pattern, and bucket, declare a conflict whenever
\(q\) pairwise graph-edge-disjoint occurrences belong to that category.  Such
a conflict has

\[
j_1=aq,
\qquad
j_2=bq.
\]

## Theorem PX166 -- PROVED

Fix constants

\[
0<\beta<1,
\qquad
q\ge4,
\qquad
\varepsilon>0
\]

such that

\[
\boxed{
\beta(q-1)>3+2\varepsilon.
}
\]

Then the mixed row-bucket conflict systems for \(a=1\) and \(a=2\) are simply
bounded for every sufficiently large prime.

Assume also that the five-stars from PX165 are avoided and that the first-stage
matching satisfies PX161.  Then, for every fixed affine shape, the final
matching has at most

\[
O_q(p^\beta)
\]

one-old/two-completion occurrences and at most

\[
O_q(p^{\eta+\beta})
\]

two-old/one-completion occurrences.

### Proof of boundedness

For one shape and bucket, the total number of labelled occurrences is

\[
O(p^3/B).
\]

If one completion row is fixed, the distinguished old row has
\(O(p/B)\) choices, the step is determined, and the image has \(p\) choices.
Thus the count is \(O(p^2/B)\).  Two fixed completion rows give at most
\(O(p)\) choices in one occurrence.

After summing over shapes, buckets, and the finite role choices, the number of
conflicts through one completion row is at most

\[
C_q\frac{p^{3q+2}}{B^{q-1}},
\]

and through two completion rows at most

\[
C_q\frac{p^{3q+1}}{B^{q-1}}.
\]

These satisfy (D2) and (D4) because \(j_1+j_2=3q\) and the hypothesis gives
more than the required powers \(p^2\) and \(p^{1+\varepsilon}\).

For (D3), fix \(j'\) old edges which occupy \(k\) of the \(q\) occurrences.
Conditional on the shape, one fixed old edge in an occurrence reduces its
three local parameters by two, and a second fixed old edge in the same
occurrence reduces them by one more.  Hence the touched occurrences have at
most

\[
O(p^{2k-j'})
\]

choices.  Ignore the bucket saving on those occurrences and retain it on the
untouched ones.  The one-row codegree is at most

\[
C_q
\frac{p^{3q-k-j'+3}}{B^{q-k}}.
\]

After comparison with the (D3) threshold

\[
p^{3q-j'-\varepsilon},
\]

it is enough that

\[
B^{q-k}\ge p^{3-k+\varepsilon}.
\]

Only \(k=1,2,3\) are nontrivial.  They follow from
\(\beta(q-1)>3+2\varepsilon\) and \(\beta<1\).  Thus all simply bounded
conditions hold.

### Proof of occurrence bounds

In the one-old sector, PX165 gives maximum occurrence degree at most \(48\).
Within one bucket, absence of a \(q\)-matching and the maximal-matching cover
argument from PX162 give \(O_q(1)\) occurrences.  There are three old-role
patterns and \(B\) buckets.

In the two-old sector, PX165 bounds degrees at old edges, while PX161 bounds the
degree at every completion edge by \(p^\eta\).  Thus the maximum occurrence
degree is \(O(p^\eta)\), and the same cover argument gives
\(O_q(p^\eta)\) occurrences per bucket and role pattern. \(\square\)

## 4. Exact subpower-triangle completion

## Theorem PX167 -- PROVED USING EXTERNAL MATCHING THEOREMS

For every fixed \(\gamma>0\), every sufficiently large prime \(p\) has a
strong-complete mapping

\[
f:\mathbb F_p\longrightarrow\mathbb F_p
\]

such that every compatible affine-triangle shape has multiplicity at most

\[
\boxed{p^\gamma.}
\]

### Proof

Choose small positive constants \(\eta,\beta\) with

\[
\eta+\beta<\gamma,
\qquad
\beta<1,
\]

then choose \(\varepsilon\) sufficiently small and fixed \(q\) sufficiently
large that

\[
\beta(q-1)>3+2\varepsilon.
\]

Use the first-stage conflict-free matching theorem with the padded test
functions from PX141 and PX161 appended to its polynomial-sized test family.
The theorem explicitly allows polynomially many trackable and semi-trackable
tests.  Since the old conflict system is empty here, their conflict-sharing
conditions are vacuous.  We obtain an almost-matching \(M_1\) with:

- at most \(p^\eta\) all-old occurrences of every affine shape;
- at most \(p^\eta\) anchored two-old occurrences for every prospective
  completion edge and role.

On the duplicated host, take the union of:

1. the projection-collision conflicts from PX160;
2. the five-star conflicts from PX165;
3. the pure-completion bucket conflicts from PX163;
4. the mixed row-bucket conflicts from PX166.

PX160 gives a mixed-bounded system for the one-completion-edge conflicts.
PX163, PX165, and PX166 give simply bounded systems with at least two
completion edges.  Their finite union is mixed-bounded after a harmless
reduction of \(\varepsilon\).  The Joos--Mubayi--Smith covering theorem gives a
row-perfect conflict-free duplicated matching, and PX159 projects it to a
perfect matching of the original strong-complete host.

For one fixed affine shape, split its occurrences by the number of completion
edges:

\[
\begin{array}{c|c}
\text{completion edges}&\text{bound}\\
\hline
0&p^\eta\\
1&O_q(p^{\eta+\beta})\\
2&O_q(p^\beta)\\
3&O_q(p^\beta).
\end{array}
\]

The last line uses the five-star degree bound together with the PX163 buckets,
improving the raw PX163 estimate by a factor of \(p\).  Since
\(\eta+\beta<\gamma\), the total is at most \(p^\gamma\) for sufficiently
large \(p\). \(\square\)

PX167 completes the affine-triangle part of exact pseudorandom completion.  It
does not yet give the required secant bound \(\mu(f)=p^{1+o(1)}\).  PX164 is
the first input for that remaining rank-two stage.

## Verification

Run

```bash
python scripts/verify_product_mixed_shape_conflicts.py
```

The verifier checks anchored secant populations, link codegree at most two,
balanced-bucket occurrence totals, one-row counts, and two-row counts through
prime order eleven.

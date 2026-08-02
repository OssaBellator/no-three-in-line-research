# High-arity repeated-shape conflicts in the completion reservoir

PX161 controls every affine-triangle occurrence containing one prospective
completion edge and two old edges.  This chapter treats the opposite pure
sector: occurrences whose three graph edges all come from the completion
reservoir.

The main point is that pairwise repeated-occurrence conflicts are too dense,
but a fixed high-arity conflict gains a bucket factor for every additional
occurrence.

Fix a compatible affine shape

\[
\sigma=(r,t,s).
\]

Its labelled occurrences are

\[
(u,a),
\quad
(u+h,a+rh),
\quad
(u+th,a+srh),
\qquad
u,a\in\mathbb F_p,\quad h\in\mathbb F_p^*.
\]

Regard these occurrences as a three-uniform multihypergraph
\(\mathcal T_\sigma\) whose vertices are host edges.  Multiplicity records the
possible labelled roles.

## Theorem PX162 -- PROVED

For every compatible shape \(\sigma\):

1. the number of labelled occurrences is

   \[
   \boxed{p^2(p-1)};
   \]

2. every scalar row belongs to exactly

   \[
   \boxed{3p(p-1)}
   \]

   occurrences;
3. every host edge belongs to exactly

   \[
   \boxed{3(p-1)}
   \]

   occurrences.

Let \(N\) be any matching in the host, and color the labelled occurrences of
\(\mathcal T_\sigma[N]\) with \(B\) colors.  Suppose no color class contains
\(q\) pairwise edge-disjoint occurrences.  Then

\[
\boxed{
|\mathcal T_\sigma[N]|
\le
9(q-1)(p-1)B.
}
\]

### Proof

The parametrisation gives \(p\) choices for \(u\), \(p\) choices for \(a\),
and \(p-1\) choices for \(h\).  Compatibility makes all three graph edges
pairwise disjoint in the four-partite host.

For a fixed row and one of the three roles, choose the other free row parameter
and the base image in \(p(p-1)\) ways.  Summing over the three roles gives the
row incidence.  For a fixed graph edge and one role, the nonzero step \(h\) is
the only remaining choice, giving \(3(p-1)\).

For the final statement, fix one color and take a maximal matching in its
occurrence multihypergraph.  It has size at most \(q-1\), and its at most
\(3(q-1)\) host edges meet every occurrence of that color.  Each such host
edge has occurrence degree at most \(3(p-1)\), so the color contains at most

\[
3(q-1)\cdot3(p-1)=9(q-1)(p-1)
\]

labelled occurrences.  Sum over the \(B\) colors. \(\square\)

## 2. Random bucketing reaches the covering-theorem margin

Use the duplicated completion reservoir from PX158.  Independently assign each
labelled all-completion occurrence a uniform color in

\[
[B]=\{1,\ldots,B\}.
\]

For each compatible shape and color, declare a conflict whenever \(q\)
pairwise edge-disjoint occurrences of that shape receive that color.  Such a
conflict consists of exactly \(3q\) completion edges.

## Theorem PX163 -- PROVED

Fix constants

\[
\beta>0,
\qquad
q\ge2,
\qquad
\varepsilon>0
\]

such that

\[
\boxed{\beta(q-1)>3+\varepsilon.}
\]

Put

\[
B=\lceil p^\beta\rceil.
\]

For every sufficiently large prime there is a coloring of all labelled
all-completion affine-triangle occurrences such that the resulting conflict
system is \((p,3q,\varepsilon)\)-simply bounded in the sense of the
Joos--Mubayi--Smith covering theorem.

Consequently, any row-perfect completion matching avoiding these conflicts has,
for every affine shape \(\sigma\), at most

\[
\boxed{
9(q-1)(p-1)\lceil p^\beta\rceil
}
\]

all-completion occurrences of \(\sigma\).

### Proof

Conditions (D1) and (D3) are immediate: every conflict has \(3q\ge2\)
completion edges and no old edges, so the old-edge codegree condition is
vacuous.

There are at most \(p^3\) compatible shapes.  For one fixed shape, PX162 gives
fewer than \(p^3\) occurrences, fewer than \(3p^2\) occurrences containing one
fixed row, and at most \(6p\) occurrences containing two fixed distinct rows.

Consider uncolored ordered \(q\)-tuples of pairwise edge-disjoint occurrences.
For one fixed row \(x\), choose the shape, choose which occurrence contains
\(x\), choose that occurrence, and then choose the remaining occurrences.  The
number is at most

\[
C_q p^3\,p^2\,(p^3)^{q-1}
=
C_q p^{3q+2}.
\]

For two fixed rows \(x,y\), either they lie in the same occurrence or in two
different occurrences.  In both cases the corresponding count is at most

\[
C_q p^{3q+1}.
\]

A fixed \(q\)-tuple is monochromatic with probability

\[
B^{1-q}.
\]

Hence the expected number of conflicts through one row is at most

\[
C_q p^{3q+2}B^{1-q},
\]

and through one row pair at most

\[
C_q p^{3q+1}B^{1-q}.
\]

The simply bounded thresholds are respectively

\[
p^{3q+\varepsilon^4}
\qquad\text{and}\qquad
p^{3q-\varepsilon}.
\]

By Markov's inequality, followed by a union bound over the \(p\) rows and fewer
than \(p^2\) row pairs, the probability that any threshold fails is at most

\[
O_q\!\left(
 p^{3-\beta(q-1)-\varepsilon^4}
+
 p^{3+\varepsilon-\beta(q-1)}
\right),
\]

which tends to zero by the displayed hypothesis.  Thus a desired coloring
exists.  The occurrence bound now follows from PX162. \(\square\)

## 3. Significance and remaining mixed sector

Choose \(\beta\) arbitrarily small and then choose the fixed arity \(q\) large
enough that \(\beta(q-1)>3+\varepsilon\).  PX163 then bounds the all-completion
contribution to every affine shape by

\[
O_{q}(p^{1+\beta}).
\]

Together with PX141 and PX161, the exact-completion decomposition is now:

1. all-old occurrences: at most \(p^\eta\) by PX141;
2. one completion edge and two old edges: at most \(3p^\eta\) per completion
   edge by PX161;
3. three completion edges: controlled by PX163;
4. two completion edges and one old edge: still open.

The fourth sector is the next bottleneck.  It requires a mixed high-arity
conflict system in which each occurrence contains one selected old edge and two
completion edges.  The raw first moments have the correct scale, but the
mixed-degree and old-edge codegree conditions must be verified uniformly over
all overlap patterns.

## Verification

Run

```bash
python scripts/verify_product_high_arity_shape_conflicts.py
```

The verifier checks the exact occurrence, row-incidence, and edge-incidence
counts at small primes.  It also exhausts small three-uniform hypergraphs to
check the maximal-matching cover inequality used in PX162.

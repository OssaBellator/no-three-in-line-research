# Exact strong-complete seeds with subpower orbit parameters

PX167 proves exact completion with subpower affine-triangle multiplicity.  The
remaining affine-orbit parameter is the maximum secant multiplicity.  This
chapter controls the all-completion secants by a randomly colored star system
and combines it with the anchored old--new estimate PX164.

Fix an allowed scalar slope

\[
r\notin\{0,1,-1\}.
\]

Its labelled ordered secants are

\[
(u,a),
\quad
(u+h,a+rh),
\qquad
u,a\in\mathbb F_p,\quad h\ne0.
\]

## 1. Colored secant stars

Independently color every labelled all-completion ordered secant with one of

\[
B=\lceil p^\alpha\rceil
\]

colors.  An \(m\)-star conflict consists of \(m\) same-slope, same-color
secants which have the same first graph edge and have distinct second graph
edges.  Its union contains \(m+1\) completion edges.

## Theorem PX168 -- PROVED

Fix constants

\[
\alpha>0,
\qquad
m\ge2,
\qquad
\varepsilon>0
\]

such that

\[
\boxed{
\alpha(m-1)>2+\varepsilon.
}
\]

For every sufficiently large prime there is a coloring for which the colored
secant-star system is \((p,m+1,\varepsilon)\)-simply bounded.

Every row-perfect matching avoiding these conflicts has, for every allowed
slope \(r\), at most

\[
\boxed{
(m-1)p\lceil p^\alpha\rceil
}
\]

labelled all-completion ordered secants of slope \(r\).

### Proof

For one slope there are exactly

\[
p^2(p-1)
\]

labelled ordered secants.  Each scalar row occurs in
\(2p(p-1)\) of them, and every host edge occurs in \(p-1\) secants in each
fixed role.

Before coloring, a star is specified by the slope, its centre graph edge, and
\(m\) nonzero steps, so there are \(O_m(p^{m+3})\) stars.  Fixing one
completion row leaves \(O_m(p^{m+2})\) choices, and fixing two rows leaves
\(O_m(p^{m+1})\).

The probability that the \(m\) labelled secants have one color is

\[
B^{1-m}.
\]

Thus the expected star count through one row is

\[
O_m(p^{m+2}B^{1-m}),
\]

and through one row pair it is

\[
O_m(p^{m+1}B^{1-m}).
\]

The simply bounded thresholds are

\[
p^{m+1+\varepsilon^4}
\qquad\text{and}\qquad
p^{m+1-\varepsilon}.
\]

Markov's inequality and a union bound over the \(p\) rows and fewer than
\(p^2\) row pairs give total failure probability

\[
O_m\!\left(
 p^{2-\varepsilon^4-\alpha(m-1)}
+
 p^{2+\varepsilon-\alpha(m-1)}
\right)=o(1).
\]

Hence a simply bounded coloring exists.  Conditions (D1) and (D3) are
immediate because every conflict is all-completion.

In an avoiding matching, fix a slope, color, and selected first graph edge.
There are fewer than \(m\) possible selected second edges.  Summing over the
\(p\) selected first edges and \(B\) colors proves the displayed bound.
\(\square\)

## 2. Exact subpower affine-orbit seeds

## Theorem PX169 -- PROVED USING EXTERNAL MATCHING THEOREMS

For every fixed \(\gamma>0\), every sufficiently large prime \(p\) has a
strong-complete mapping \(f\) satisfying

\[
\boxed{
\mu(f)\le p^{1+\gamma},
\qquad
\tau(f)\le p^\gamma.
}
\]

### Proof

Choose

\[
0<\eta,\alpha<\gamma
\]

and then choose \(m\) so that

\[
\alpha(m-1)>2+\varepsilon
\]

for the sufficiently small covering-theorem parameter \(\varepsilon\).
Run the augmented two-stage construction from PX167, adding the colored
secant-star conflicts from PX168 and the anchored secant tests from PX164.
The additional star system is simply bounded, so the finite union of all
triangle, secant, and projection conflict systems remains mixed-bounded after
a harmless reduction of \(\varepsilon\).

PX167 gives

\[
\tau(f)\le p^\gamma
\]

after making its internal exponents smaller if necessary.

Fix an allowed secant slope and split its ordered pairs by the number of
completion edges.

### Two old edges

The PX141 secant test gives

\[
(1+o(1))(p-1)=O(p)
\]

ordered pairs.

### One old and one completion edge

PX164 gives at most \(p^\eta\) old partners for each prospective completion
edge and either ordered role.  There are at most \(p\) completion edges, so
this sector contributes at most

\[
2p^{1+\eta}.
\]

### Two completion edges

PX168 contributes at most

\[
(m-1)p\lceil p^\alpha\rceil
=O_m(p^{1+\alpha}).
\]

Because \(\eta,\alpha<\gamma\), the sum is at most \(p^{1+\gamma}\) for all
sufficiently large primes. \(\square\)

## 3. Affine-orbit consequence

PX129 converts one deterministic seed into a three-parameter affine-orbit
measure.  Its normalized cylinder constants are

\[
K_1=1,
\qquad
K_2=\frac{\mu(f)}p,
\qquad
K_3=\frac{p-2}{p}\tau(f).
\]

## Corollary PX170 -- PROVED

For every fixed \(\gamma>0\) and every sufficiently large prime, there is an
affine-orbit probability distribution on strong-complete mappings with

\[
\boxed{
K_1=1,
\qquad
K_2\le p^\gamma,
\qquad
K_3\le p^\gamma.
}
\]

Moreover, in the two normalized protected directions, choose the first-stage
mapping \(\Phi\) from this orbit, independently choose \(h\) from the same
orbit, and put

\[
P=h\circ\Phi.
\]

Then every joint matching cylinder of rank \(k\le3\) has probability at most

\[
\boxed{
\frac{p^{2\gamma}}{(p)_k^2}.
}
\]

### Proof

The first assertion is immediate from PX129 and PX169.  The conditional
composition is the same as PX131: after conditioning on \(\Phi\), prescribed
values of \(P\) become a matching cylinder for \(h\).  Multiply the two
one-stage bounds. \(\square\)

PX170 proves the protected-rainbow spread hypothesis with an arbitrarily small
fixed power loss, rather than the absolute constant conjectured from the
finite seeds.  Whether this loss is small enough for the final rectangle
local-load argument is the next product-construction calculation.

## Verification

Run

```bash
python scripts/verify_product_secant_completion_conflicts.py
```

The verifier checks the exact ordered-secant population, row incidence, edge
incidence, and fixed-row-pair counts through prime order thirteen.

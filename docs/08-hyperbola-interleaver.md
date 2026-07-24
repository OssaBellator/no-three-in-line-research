# Complementary modular hyperbolas and interleavers

Let \(p\) be an odd prime and \(n=p-1\). For \(c\in\mathbb F_p^\times\), define

\[
H_c=\{(x,y)\in[1,p-1]^2:xy\equiv c\pmod p\}.
\]

Each \(H_c\) is a permutation graph.

## 1. Four-point line cap

### Theorem H1 — PROVED

For distinct \(a,b\), the union \(H_a\cup H_b\):

- has exactly two points in every row and column;
- has at most four points on every real line;
- has no monochromatic collinear triple.

### Proof

On a line \(Ax+By=C\), substituting \(y=c/x\pmod p\) gives a nonzero quadratic

\[
Ax^2-Cx+Bc\equiv0\pmod p,
\]

unless the line fixes one coordinate, in which case there is at most one point. Thus each hyperbola contributes at most two points. ∎

## 2. Bichromatic displacement multiplicity

### Theorem H2 — PROVED

Fix \(c,d\) and nonzero displacement \((r,s)\). There are at most two ordered pairs

\[
P\in H_c,
\qquad P+(r,s)\in H_d.
\]

Substitution yields

\[
sx^2+(rs-d+c)x+rc\equiv0\pmod p.
\]

Therefore a union of \(q\) hyperbolas has displacement multiplicity at most \(2q^2\).

## 3. Dyadic secant shadow

If every exact displacement appears at most \(\mu\) times, then in a dyadic primitive-height band \([H,2H)\):

- there are \(O(\mu pH)\) selected pairs;
- each supporting line has \(O(p/H)\) grid cells.

### Theorem H3 — PROVED

\[
\Xi_H(S)\le C\mu p^2
\]

uniformly in \(H\).

For \(q\) hyperbolas, \(\Xi_H=O(q^2p^2)\).

## 4. Low-syndrome pair

Let \(T(a,a;b)\) count real triples with two points from \(H_a\) and one from \(H_b\). Every third grid point on a secant of \(H_a\) belongs to a unique hyperbola channel.

Hence

\[
\sum_{b\ne a}T(a,a;b)=\Sigma(H_a)=O(p^2\log p).
\]

Averaging over ordered pairs gives:

### Theorem H4 — PROVED

Some distinct \(a,b\) satisfy

\[
\sum_L\binom{|(H_a\cup H_b)\cap L|}{3}=O(p\log p).
\]

Thus there is a saturated seed with only \(O(n\log n)\) triple certificates and at most four points per line.

## 5. Hamiltonian-cycle representation

Following an \(H_a\) edge from column \(x\) to a row and an \(H_b\) edge back to a column multiplies \(x\) by \(b/a\).

### Theorem H5 — PROVED

If \(d=\operatorname{ord}_{\mathbb F_p^\times}(b/a)\), the row-column incidence graph is a union of \((p-1)/d\) cycles of length \(2d\). If \(b/a\) is primitive, it is one Hamiltonian cycle.

Every Hamiltonian saturated configuration can be written

\[
S_\pi=
\{(i,\pi(i)),(i,\pi(i+1)):i\in\mathbb Z_n\}.
\]

This gives a cyclic-interleaver subproblem: find \(\pi\) so that \(S_\pi\) is no-three-in-line.

## 6. Sparse-edit decoder

If a configuration differs from a bounded union of hyperbolas in at most \(r\le H\) points, the dyadic shadow remains \(O(p^2)\). Algebraic-helper rectangle switches have total scale-\(H\) collateral \(O(p^2)\).

Therefore if the scale-\(H\) triple syndrome is larger than \(Cp\), some helper switch decreases it.

A stalled decoder forces the residual syndrome into a small high-degree error core, analogous to an LDPC trapping set.

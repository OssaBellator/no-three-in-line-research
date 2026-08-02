# Mixed-radix product constructions

This chapter develops
[`tracks/all-n-product-construction.md`](../tracks/all-n-product-construction.md).
It completes the saturation task for every global radix orientation, gives exact
determinant identities and line/codegree bounds, and reduces phase selection to
an exact width-three SAT instance. It does **not** prove multiplicative closure.

All grids are zero-indexed. Write saturated factor configurations as

\[
S_m=\{(i,\sigma_r(i)):i\in[m],\ r\in\{0,1\}\},
\qquad
S_n=\{(u,\tau_s(u)):u\in[n],\ s\in\{0,1\}\}.
\]

The two permutations in each factor are pointwise disjoint.

## 1. Cycle phases and four radix orientations

Let

\[
\pi=\tau_1^{-1}\tau_0
\]

and write \(C(u)\) for the orbit of \(u\) under \(\pi\). For every output layer
\(r\), coarse row \(i\), and orbit \(C\), choose

\[
\varepsilon_{r,i,C}\in\{0,1\}.
\]

There are two ways to flatten one coordinate pair:

- `c` (coarse-major): \(\phi_c(a,b)=nb+a\) when \(a\in[n]\), \(b\in[m]\);
  in the notation below this is \(ni+u\);
- `f` (fine-major): \(\phi_f(i,u)=mu+i\).

For clarity, define the row coordinate by

\[
X_c(i,u)=ni+u,\qquad X_f(i,u)=mu+i,
\]

and define the column coordinate analogously,

\[
Y_c(j,v)=nj+v,\qquad Y_f(j,v)=mv+j.
\]

An orientation is a word

\[
\theta=(\theta_x,\theta_y)\in\{c,f\}^2.
\]

For each row digit pair \((i,u)\), put

\[
j=\sigma_r(i),\qquad
s=\varepsilon_{r,i,C(u)},\qquad
v=\tau_s(u),
\]

and define

\[
\boxed{
\Pi_r^\theta\bigl(X_{\theta_x}(i,u)\bigr)
=
Y_{\theta_y}(j,v).
}
\]

Let \(P^\theta_{m,n}(\varepsilon)\) be the union of the two graphs.

### Theorem PX1 — PROVED

For every orientation \(\theta\in\{c,f\}^2\), each \(\Pi_r^\theta\) is a
permutation of \([mn]\), and the two graphs are cell-disjoint. Hence every
cycle-phase state has exactly \(2mn\) cells and exactly two points in every row
and column. It is constructible in \(O(mn)\) operations once the phases are
given.

### Proof

Both \(X_c,X_f\) are bijections from \([m]\times[n]\) to \([mn]\), and both
\(Y_c,Y_f\) are bijections from \([m]\times[n]\) to \([mn]\).

Fix \(r\) and a target coarse column \(j\). Then
\(i=\sigma_r^{-1}(j)\) is unique. For every orbit \(C\) of \(\pi\),

\[
\tau_0(C)=\tau_1(\pi(C))=\tau_1(C).
\]

Thus either restriction \(\tau_0|_C\) or \(\tau_1|_C\) bijects \(C\) onto the
same fine-column set. Choosing one restriction independently on each orbit
gives a permutation of \([n]\). Therefore the map
\((i,u)\mapsto(j,v)\) is a bijection, and composing with either pair of digit
flattenings gives a permutation of \([mn]\).

For a fixed scalar row, the decoded pair \((i,u)\) is the same in both output
layers. Their coarse columns are \(\sigma_0(i)\ne\sigma_1(i)\), so their
decoded column pairs differ and hence their scalar columns differ. \(\square\)

If \(\pi\) has \(c\) orbits, the family has \(2^{2mc}\) phase states in each
orientation.

## 2. General mixed-radix determinant

For an orientation \(\theta\), define positive coefficients by

\[
(a_i,a_u)=
\begin{cases}
(n,1),&\theta_x=c,\\
(1,m),&\theta_x=f,
\end{cases}
\qquad
(a_j,a_v)=
\begin{cases}
(n,1),&\theta_y=c,\\
(1,m),&\theta_y=f.
\end{cases}
\]

Thus an encoded point is

\[
F_\theta(i,j,u,v)
=
(a_i i+a_u u,\ a_j j+a_v v).
\]

For three digit quadruples, put

\[
\Delta_{ij}=\det((i_0,j_0),(i_1,j_1),(i_2,j_2)),
\]

\[
\Delta_{uv}=\det((u_0,v_0),(u_1,v_1),(u_2,v_2)),
\]

and define the two hybrid determinants

\[
\Delta_{iv}=\det((i_0,v_0),(i_1,v_1),(i_2,v_2)),
\]

\[
\Delta_{uj}=\det((u_0,j_0),(u_1,j_1),(u_2,j_2)).
\]

### Theorem PX2 — PROVED

For every orientation,

\[
\boxed{
\det(F_\theta(P_0),F_\theta(P_1),F_\theta(P_2))
=
a_i a_j\Delta_{ij}
+a_i a_v\Delta_{iv}
+a_u a_j\Delta_{uj}
+a_u a_v\Delta_{uv}.
}
\]

### Proof

Write the two difference vectors as

\[
(a_i\Delta i+a_u\Delta u,\ a_j\Delta j+a_v\Delta v)
\]

and expand their determinant bilinearly. The coarse, two hybrid, and fine terms
are exactly the four displayed terms. \(\square\)

The four specializations are

\[
\begin{array}{c|l}
cc & n^2\Delta_{ij}+n\Delta_{iv}+n\Delta_{uj}+\Delta_{uv},\\
cf & n\Delta_{ij}+nm\Delta_{iv}+\Delta_{uj}+m\Delta_{uv},\\
fc & n\Delta_{ij}+\Delta_{iv}+nm\Delta_{uj}+m\Delta_{uv},\\
ff & \Delta_{ij}+m\Delta_{iv}+m\Delta_{uj}+m^2\Delta_{uv}.
\end{array}
\]

### Corollary PX2a — PROVED

In the ordinary `cc` orientation, a collinear triple satisfies

\[
\Delta_{uv}=n\kappa,\qquad |\kappa|\le n-2,
\]

and

\[
\boxed{
n\Delta_{ij}+\Delta_{iv}+\Delta_{uj}+\kappa=0.
}
\]

### Proof

Reduce the `cc` identity modulo \(n\). Since three points in \([n]^2\) have

\[
|\Delta_{uv}|\le(n-1)^2<n^2,
\]

write \(\Delta_{uv}=n\kappa\) with \(|\kappa|\le n-2\), then divide by \(n\).
\(\square\)

## 3. Four cross-block types

Let \(c\) and \(f\) be the numbers of distinct coarse and fine projected points
in a product triple.

### Theorem PX3 — PROVED

If both factors are no-three, every bad product triple has

\[
(c,f)\in\{(2,2),(2,3),(3,2),(3,3)\}.
\]

For an arbitrary orientation, its exact resonance is obtained from PX2 by
setting \(\Delta_{ij}=0\) exactly when \(c=2\), and setting
\(\Delta_{uv}=0\) exactly when \(f=2\). Thus:

\[
\begin{array}{c|l}
(2,2)&a_i a_v\Delta_{iv}+a_u a_j\Delta_{uj}=0,\\
(2,3)&a_i a_v\Delta_{iv}+a_u a_j\Delta_{uj}
      +a_u a_v\Delta_{uv}=0,\\
(3,2)&a_i a_j\Delta_{ij}+a_i a_v\Delta_{iv}
      +a_u a_j\Delta_{uj}=0,\\
(3,3)&a_i a_j\Delta_{ij}+a_i a_v\Delta_{iv}
      +a_u a_j\Delta_{uj}+a_u a_v\Delta_{uv}=0.
\end{array}
\]

In the `cc` orientation these become

\[
\begin{array}{c|l}
(2,2)&\Delta_{ij}=\Delta_{uv}=0,\quad
       \Delta_{iv}+\Delta_{uj}=0,\\
(2,3)&\Delta_{ij}=0,\quad
       \Delta_{uv}=n\kappa\ne0,\quad
       \Delta_{iv}+\Delta_{uj}+\kappa=0,\\
(3,2)&\Delta_{ij}\ne0,\quad
       \Delta_{uv}=0,\quad
       n\Delta_{ij}+\Delta_{iv}+\Delta_{uj}=0,\\
(3,3)&\Delta_{ij}\ne0,\quad
       \Delta_{uv}=n\kappa\ne0,\quad
       n\Delta_{ij}+\Delta_{iv}+\Delta_{uj}+\kappa=0.
\end{array}
\]

Here \(|\kappa|\le n-2\), so type \((2,3)\) is impossible in the `cc`
orientation when \(n=2\).

### Proof

If \(c=1\), flattening restricts to an invertible diagonal affine image of
three fine points, so a product collinearity would be a forbidden fine
collinearity. Similarly \(f=1\) would give a forbidden coarse collinearity.
Thus \(c,f\ge2\).

With three projected points, exactly two distinct points give determinant zero,
while three distinct points give nonzero determinant by the factor no-three
property. Substitute these alternatives into PX2 and PX2a. \(\square\)

This completes the classification part of PC2 for all four radix orientations.
Eliminating the resulting resonances remains open.

## 4. Exact type-\((2,2)\) direction resonance

Let

\[
A=\operatorname{diag}(a_i,a_j),
\qquad
B=\operatorname{diag}(a_u,a_v).
\]

A type-\((2,2)\) triple can be relabelled as

\[
F_\theta(c_0,f_0),\qquad
F_\theta(c_0,f_1),\qquad
F_\theta(c_1,f_0).
\]

### Theorem PX4 — PROVED

The three points above are collinear if and only if

\[
\boxed{
\det\bigl(B(f_1-f_0),A(c_1-c_0)\bigr)=0.
}
\]

Thus type \((2,2)\) is precisely equality of a weighted fine secant direction
and a weighted coarse secant direction.

### Proof

Subtract the first point. The two difference vectors are
\(B(f_1-f_0)\) and \(A(c_1-c_0)\). Their determinant vanishes exactly when the
three flattened points are collinear. \(\square\)

For `cc` and `ff`, both diagonal matrices are scalar, so this is ordinary
parallelism of the two factor secants. In the two crossed orientations it is an
anisotropically weighted parallelism.

The full four-layer tensor host can therefore never be no-three: both saturated
factors contain horizontal and vertical secants, giving immediate
type-\((2,2)\) triples. Any successful product must select a strict subfamily
of tensor cells, as PX1 does.

## 5. Product-compatible repairs

### Theorem PX5 — PROVED

Toggling one phase \(\varepsilon_{r,i,C}\) removes and inserts exactly \(|C|\)
cells in every orientation. It preserves every row and column, is supported on
one coarse factor point \((i,\sigma_r(i))\), and keeps both factor projections
inside \(S_m,S_n\).

### Proof

The toggle replaces \(\tau_s(u)\) by \(\tau_{1-s}(u)\) for \(u\in C\). Since

\[
\tau_0(C)=\tau_1(C),
\]

the affected decoded fine-column set is unchanged. PX1 preserves global
saturation in every orientation. The coarse projection is fixed, and every
fine projection remains an edge of \(S_n\). \(\square\)

This closes the row-column and factor-protection parts of PC6.

## 6. Factor-product host line and codegree bounds

For an orientation \(\theta\), define the full factor-product host

\[
\mathcal H^\theta_{m,n}
=
\{F_\theta(c,f):c\in S_m,\ f\in S_n\}.
\]

The digit flattening is injective, so this host has \(4mn\) cells. Every
cycle-phase state is a subset of this host.

### Theorem PX6 — PROVED

Every real line meets \(\mathcal H^\theta_{m,n}\) in at most

\[
\boxed{4\min(m,n)}
\]

points. More precisely:

1. for a fixed coarse projection \(c\in S_m\), a line contains at most two host
   points of the form \(F_\theta(c,f)\);
2. for a fixed fine projection \(f\in S_n\), a line contains at most two host
   points of the form \(F_\theta(c,f)\).

Consequently, a fixed pair of host points has at most

\[
4\min(m,n)-2
\]

possible third host points collinear with it.

### Proof

Fix a line \(\ell\) and a coarse point \(c\). The map

\[
f\longmapsto F_\theta(c,f)=Ac+Bf
\]

is an invertible diagonal affine map in the fine variables. The inverse image
of \(\ell\) is therefore a real line or the empty set. Since \(S_n\) has no
three collinear points, at most two \(f\in S_n\) lie in that inverse image.
There are \(2m\) choices of \(c\), giving at most \(4m\) host points.

The same argument with \(f\) fixed and \(c\mapsto Ac+Bf\) gives at most \(4n\).
Take the smaller bound. The pair-codegree statement follows by removing the
fixed pair from its unique line. \(\square\)

### Corollary PX6a — PROVED

The number \(T(\mathcal H^\theta_{m,n})\) of collinear host triples satisfies

\[
T(\mathcal H^\theta_{m,n})
\le
\frac{1}{3}
\binom{4mn}{2}
\bigl(4\min(m,n)-2\bigr).
\]

### Proof

For each unordered pair, there are at most
\(4\min(m,n)-2\) possible third points. Every unordered collinear triple is
counted by its three pairs. \(\square\)

PX6 gives a uniform projection-signature multiplicity bound for PC6. A sharper
bound organized by the arithmetic carry values in PX2 is still open.

## 7. Exact phase selection as width-three SAT

Let the phase variables be

\[
z_{r,i,C}=\varepsilon_{r,i,C}.
\]

There are \(V=2mc\) variables when the inner transition has \(c\) cycles.
Every one of the \(2mn\) point positions depends on exactly one phase variable.

### Theorem PX7 — PROVED

For fixed factor pairs and a fixed radix orientation, existence of a no-three
cycle-phase product is equivalent to satisfiability of an explicitly
constructible CNF formula with

\[
V=2mc
\]

variables, clause width at most three, and at most

\[
\boxed{
8\binom{2mn}{3}
}
\]

clauses.

### Construction and proof

Take an unordered triple of point positions. It depends on at most three
distinct phase variables. For each assignment to those variables, compute the
three resulting integer cells. If they are collinear, add the clause that
excludes exactly that partial assignment: for an assigned bit zero use the
positive literal, and for an assigned bit one use the negative literal.

There are at most eight assignments for each position triple, giving the
displayed clause bound. A complete phase assignment satisfies every clause if
and only if no position triple becomes collinear, which is exactly the desired
no-three condition. The formula is constructible in
\(O((mn)^3)\) determinant checks. \(\square\)

The verifier implements this reduction and an exact DPLL model counter. It also
checks the DPLL counts against direct enumeration on the smallest instances.

## 8. Four-orientation phase obstruction

### Claim PX8 — REFUTED

The following stronger claim is false:

> Given two saturated no-three factor pairs, one of the four global radix
> orientations and one independent cycle-phase state always gives a no-three
> product.

Take

\[
\sigma_0=(0,1),\qquad \sigma_1=(1,0),
\]

\[
\tau_0=(0,2,1),\qquad \tau_1=(1,0,2).
\]

Both factor unions are saturated and no-three. The fine transition is one
3-cycle, so each orientation has four phase bits and sixteen states. Direct
enumeration finds a collinear triple in all

\[
4\cdot16=64
\]

orientation/phase states. The script checks saturation, PX2, and an explicit
integer collinearity witness for each state.

Thus changing only digit significance does not repair the cycle-phase route.
PC3 needs a larger state space: non-global digit bijections, block offsets,
additional factor-compatible trades, or a repair theorem.

## 9. Verification and finite results

Run

```bash
python scripts/verify_product_construction.py
python scripts/verify_product_construction.py --extended
```

Here `c` means coarse-major and `f` means fine-major. The exact model counts
are:

| `(m,n)` | States per orientation | `cc` | `cf` | `fc` | `ff` |
|---|---:|---:|---:|---:|---:|
| `(2,2)` | 64 | 20 | 20 | 20 | 4 |
| `(2,3)` | 128 | 0 | 0 | 0 | 0 |
| `(3,2)` | 512 | 0 | 8 | 8 | 0 |
| `(3,3)` | 1024 | 0 | 0 | 0 | 0 |
| `(2,4)` | 18560 | 0 | 0 | 0 | 48 |
| `(4,2)` | 20480 | 16 | 64 | 64 | 0 |
| `(3,4)` | 590848 | 0 | 0 | 0 | 0 |
| `(4,3)` | 40960 | 0 | 0 | 0 | 0 |
| `(2,5)` | 2048 | 0 | 0 | 0 | 0 |
| `(5,2)` | 131072 | 0 | 0 | 0 | 0 |

The first four size pairs run by default. The remaining six use `--extended`.
These are finite checks, not an asymptotic theorem. Positive counts show that
radix orientation genuinely changes feasibility, but the many zero rows show
that no global orientation is a universal phase theorem.

## 10. Status against PC1--PC6

- **PC1 complete:** PX1 handles all four global radix orientations.
- **PC2 partial:** PX2--PX4 give the general determinant, four-type
  classification, and exact type-\((2,2)\) resonance. Eliminating the remaining
  resonances is open.
- **PC3 open:** PX8 refutes the enlarged global-orientation phase route.
- **PC4--PC5 open:** no useful multiplicative closure or arithmetic coverage
  theorem is proved.
- **PC6 partial:** PX5 gives executable factor-protected trades; PX6 gives
  uniform line, pair-codegree, and projection-signature bounds. Arithmetic
  carry-signature multiplicity and a terminating repair theorem remain open.

# Common-line alternating rectangle bank

PP3ny produces a positive-density family of target-rich nonaxis lines. Every
good line carries two matching traces:

- owner/replacement endpoint cells;
- Hall-target endpoint cells.

Pairing one cell from each trace gives an alternating rectangle whose chosen
diagonal lies on the obstruction line and whose opposite diagonal lies off that
line. This chapter extracts a linear resource-disjoint bank of such rectangles.

## 1. Rectangle candidates on one line

For a good line \(\ell\), write

\[
P_\ell
=
\{(x_i,y_j):\ell_{ij}=\ell\}
\]

for its owner/replacement trace and

\[
T_\ell
=
\mathcal A\cap\ell
\]

for its Hall-target trace.

For distinct cells

\[
p=(x_1,y_1)\in P_\ell,
\qquad
t=(x_2,y_2)\in T_\ell,
\]

define the opposite diagonal

\[
p^*=(x_1,y_2),
\qquad
t^*=(x_2,y_1).
\]

The signed rectangle is

\[
-\mathbf1_p-\mathbf1_t+\mathbf1_{p^*}+\mathbf1_{t^*}.
\]

### Proposition PP3oh -- PROVED

The four cells are distinct and the signed rectangle has zero row and column
sums. The two positive cells do not lie on \(\ell\).

If \(\ell\) has slope \(a\), then the line through \(p^*,t^*\) has slope
\(-a\).

#### Proof

Because \(\ell\) is nonaxis, two distinct points on it use distinct rows and
columns. Thus the four rectangle corners are distinct and the standard
alternating signs cancel in every used row and column.

If \(p^*\) lay on \(\ell\), then \(\ell\) would contain two points with old
column \(x_1\), forcing it to be vertical. The same applies to \(t^*\).
Finally,

\[
\dfrac{y_1-y_2}{x_2-x_1}=-a.
\]

∎

Thus every candidate rectangle moves two same-line cells to an opposite-slope
diagonal while preserving saturation margins.

## 2. Number of rectangle candidates

Let \(\mathscr G\) be the good-line family from PP3nx. Put

\[
\mathcal R
=
\{(\ell,p,t):\ell\in\mathscr G,
\ p\in P_\ell,
\ t\in T_\ell,
\ p\ne t\}.
\]

### Proposition PP3oi -- PROVED

For every fixed \(\delta>0\), the near-extremal line alternative satisfies

\[
|\mathcal R|=\Omega(q^3).
\]

#### Proof

On every good line,

\[
|P_\ell|\ge q^{1/3-\delta},
\qquad
|T_\ell|\ge q^{1-\delta}.
\]

For sufficiently large \(q\), deleting the at most
\(|P_\ell\cap T_\ell|\le|P_\ell|\) equal pairs loses only a vanishing fraction
of \(|P_\ell||T_\ell|\).

More directly, PP3nx gives

\[
\sum_{\ell\in\mathscr G}|P_\ell||T_\ell|
=
\Omega(q^3).
\]

The total number of equal pairs is at most

\[
\sum_{\ell\in\mathscr G}|P_\ell|
=O(q^2),
\]

because every typed owner/replacement pair belongs to one line. Subtract. ∎

## 3. Endpoint-resource degree

View every rectangle candidate as a four-element set of endpoint resources: the
two old columns and two old rows used by \(p,t\).

### Proposition PP3oj -- PROVED

Every endpoint resource belongs to at most \(2q^2\) members of
\(\mathcal R\).

#### Proof

Fix an old-column resource; the row-resource proof is transposed.

First count candidates in which the resource belongs to the owner/replacement
cell \(p\). There are at most \(q\) endpoint cells \(p=(x_i,y_j)\) using the
fixed column, one for each replacement row. The line of each such typed cell
contains at most \(q\) target cells, giving at most \(q^2\) candidates.

Next count candidates in which the resource belongs to the target cell \(t\).
There are at most \(q\) target cells in the fixed column. For one fixed target
cell and one owner \(i\), at most one replacement index \(j\) puts
\(z_i,(x_i,y_j),t\) on one line, by PP3nm. Hence at most \(q\) typed
owner/replacement cells pair with that target. This contributes at most another
\(q^2\). ∎

The bound uses typed multiplicity and remains valid when many owners determine
the same geometric line.

## 4. Linear resource-disjoint rectangle bank

### Theorem PP3ok -- PROVED

The candidate family \(\mathcal R\) contains

\[
\Omega(q)
\]

rectangles whose four endpoint resources are pairwise disjoint across the bank.
Consequently all negative diagonals are pairwise row/column-disjoint, and all
positive diagonals are also pairwise row/column-disjoint.

#### Proof

Take a maximal matching in the four-uniform resource hypergraph of rectangle
candidates. One selected rectangle uses four resources. By PP3oj, deleting all
candidates meeting those resources removes at most \(8q^2\) candidates.
Since PP3oi gives \(|\mathcal R|=\Omega(q^3)\), maximality requires
\(\Omega(q)\) selected rectangles. ∎

Thus the near-extremal line obstruction contains a linear formal alternating
rectangle bank.

## 5. Installation interface

### Corollary PP3ol -- PROVED AS A CONDITIONAL CONVERSION INTERFACE

Suppose a subbank of the PP3ok rectangles can be installed so that:

1. its negative diagonals are present in the current endpoint state;
2. its positive diagonals are source-admissible;
3. the positive-diagonal insertion shadow is below the removal credit supplied by
   the negative diagonals.

Then switching every installed rectangle preserves all old row and column
counts, keeps the no-three property, and strictly decreases the relevant
controller-shadow or owner-line potential.

#### Proof

PP3oh gives exact row/column cancellation. Source admissibility gives geometric
validity, and the paid potential identity PP3ib or PP3kx gives strict decrease
when insertion cost is below removal credit. Resource-disjointness permits the
rectangles to be switched simultaneously. ∎

The unresolved common-line step is now an **installation theorem** for a linear
row/column-disjoint rectangle bank. Rectangle extraction itself is closed.
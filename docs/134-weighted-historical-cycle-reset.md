# Weighted historical cycle resets for trajectory-saturated cores

PX291--PX293 show that a genuinely cycle-free terminal block has a completely
forbidden row and column.  The historical part of such a row is not merely an
obstruction: releasing one historical return cell can close an allowed directed
path into the saturated endpoint and create a principal cycle trade.

The released cell may recreate old designated certificates.  The correct
criterion is therefore weighted.  A reset is improving when the current
obligations destroyed around the cycle exceed the live ancestor obligations
charged to the released historical cell.

## 1. Hybrid termination potential

Let `U_j` and `d_j` be the unresolved and designated coordinates of PX280.  Put

\[
\mathcal T=\sum_j(U_j+d_j)
\]

and let `V` be the lexicographic vector

\[
V=(U_0,d_0,U_1,d_1,\ldots,U_d,d_d).
\]

Order states by the pair `(mathcal T,V)`, first by the integer `mathcal T` and
then lexicographically by `V`.

### Theorem PX294 -- PROVED

Every causal transition of PX280 strictly decreases `(mathcal T,V)`.  In
addition, any terminal reset which destroys `A` live obligations and recreates
at most `B<A` ancestor obligations strictly decreases `(mathcal T,V)`, even if
one shallower coordinate temporarily increases.

### Proof

An immediate improvement or designated neutralization decreases `mathcal T`.
A child conversion removes one unresolved unit and creates one deeper
designated unit, so `mathcal T` is unchanged while `V` decreases exactly as in
PX280.  A reset with `B<A` decreases `mathcal T` by at least `A-B`; its effect
on `V` is irrelevant.  The ordered pair is well founded because both entries
range over finite nonnegative integer sets. \(\square\)

Thus a controlled ancestor return is permitted when it pays more current debt
than it revives.

## 2. One released historical edge

Let `A_F` be the terminal allowed label digraph.  Assume it is acyclic and let
`v` be a sink, so row `v` is completely forbidden.  Decompose

\[
F=F_0\cup H,
\]

where `F_0` is the base forbidden graph of maximum row and column degree
`Delta_0`, and `H` is the union of historical position matchings.

Give every label `x` a positive integer current-obligation weight `a_x`.  For a
historical cell `e=(v,c)`, let `h_e` be the number of live ancestor obligations
which can be recreated by returning row `v` to column `c`.

Suppose there is an allowed directed path

\[
P:c=x_0\to x_1\to\cdots\to x_\ell=v.
\]

Releasing the one historical cell `(v,c)` closes the directed cycle

\[
c\to x_1\to\cdots\to v\to c.
\]

### Theorem PX295 -- PROVED

The resulting principal cycle reset destroys current obligation weight at least

\[
A(P)=\sum_{i=0}^{\ell}a_{x_i}
\]

and recreates ancestor weight at most `h_(v,c)`.  Consequently it strictly
decreases the hybrid potential whenever

\[
\boxed{h_{(v,c)}<A(P).}
\]

### Proof

All path edges are currently allowed.  The closing edge is the unique released
historical cell, so the displayed cycle is executable and moves every endpoint
on the path.  By the causal deletion identity PX235, moving endpoint `x_i`
destroys all current obligations charged to its current position, of total
weight at least `a_(x_i)`.  No other historical cell is used.  Therefore the
only ancestor obligations which can return are those whose unique return cell
is `(v,c)`, at most `h_(v,c)`.  Apply PX294. \(\square\)

The column-source version is symmetric.

## 3. Failure forces a historical star field

Let

\[
R(v)=\{c:\text{there is an allowed directed path from }c\text{ to }v\}
\]

be the reverse basin of the sink.  For each `c in R(v)-{v}`, the cell `(v,c)` is
forbidden because row `v` is full.  At most `Delta_0` such cells belong to the
base graph.

For a threshold `tau>=2`, write `R_tau(v)` for vertices `c` for which some
allowed `c`-to-`v` path has current weight at least `tau`.

### Theorem PX296 -- PROVED

If no weighted historical cycle reset improves, then row `v` contains at least

\[
\boxed{|R_\tau(v)|-\Delta_0}
\]

historical cells of recurrence load at least `tau`.

Each such cell is a candidate centre supporting `h_e` live ancestor witness
pairs.  If every witness line has at most `K` live background points, PX228
extracts from that cell an endpoint-disjoint secant star of order at least

\[
\boxed{\tau/K.}
\]

### Proof

For every `c in R_tau(v)`, choose a path of weight at least `tau`.  If `(v,c)` is
historical, failure of PX295 gives `h_(v,c)>=tau`.  At most `Delta_0` of the
cells can be base-forbidden.  The star extraction is PX228 applied to the live
ancestor pairs charged to the historical cell. \(\square\)

Thus a nonresettable saturated row is a coordinate field of quantitatively
heavy historical return centres.

## 4. Long paths force one large return star

Assume unit current weights `a_x>=1`.  Let

\[
x_0\to x_1\to\cdots\to x_L=v
\]

be an allowed path of maximum length into `v`.

### Corollary PX297 -- PROVED

If no weighted reset improves, then some historical cell in row `v` has
recurrence load at least

\[
\boxed{L-\Delta_0+1}
\]

whenever `L>=Delta_0`.

Consequently, under background line cap `K`, one historical return cell centres
an endpoint-disjoint star of order at least

\[
\boxed{(L-\Delta_0+1)/K.}
\]

### Proof

For every `i<L`, the reverse cell `(v,x_i)` is forbidden.  At most `Delta_0` of
these reverse cells are base cells.  Among the first `Delta_0+1` path vertices,
some reverse cell is historical.  If its index is `i<=Delta_0`, the closed
cycle has at least `L-i+1>=L-Delta_0+1` vertices.  Failure of PX295 forces at
least that much recurrence load.  Apply PX228. \(square\)

## 5. Reset-or-field terminal interface

### Corollary PX298 -- PROVED

Every trajectory-saturated sink has one of the following outcomes.

1. **Improving historical reset.**  One released historical edge closes an
   allowed path and strictly lowers the hybrid obligation potential.
2. **Heavy historical return cell.**  A long allowed path forces one large live
   ancestor star at a historical position.
3. **Coordinate historical field.**  A large reverse basin forces many heavy
   historical return centres in the same row.
4. **Small reverse basin.**  The set `R(v)` is small and can be passed directly
   to the exact terminal optimizer PX273--PX276.

The source-column statement is symmetric.  Hence trajectory saturation is no
longer an anonymous terminal obstruction: it either resets, returns to the
clean-star/coordinate-field decoder, or localizes to an explicitly small exact
subproblem.

## 6. Verification

Run

```bash
python scripts/verify_product_weighted_historical_reset.py
```

The verifier generates random acyclic allowed digraphs, checks all historical
cycle-reset inequalities, validates the hybrid potential order, verifies the
reverse-basin heavy-cell count, and tests the long-path bound.
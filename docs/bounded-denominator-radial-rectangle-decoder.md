# Radial rectangle decoder and blocker classification

BDA4d--BDA4f reduce a dense bounded-denominator radial profile to
co-anchored adjacent levels and then regularize their row/column load.
This note gives the local state comparison for one such pair.

Let

\[
d=(a,b),
\qquad
c=(u,v),
\qquad
H=h+q,
\]

with \(h,q>0\) and \(a,b,u,v\ne0\).  At anchor \(P\), suppose the active
permutation layer contains the clean five-cell support

\[
\boxed{
P,\quad
P+hu\,d,\quad
P+hv\,d,\quad
P+Hu\,d,\quad
P+Hv\,d,
}
\]

using five distinct rows and five distinct columns.  The two paid
radial triples are

\[
T_h(P)=\{P,P+hu\,d,P+hv\,d\},
\]

\[
T_H(P)=\{P,P+Hu\,d,P+Hv\,d\}.
\]

For one role \(w\in\{u,v\}\), put

\[
A_w=P+hw\,d,
\qquad
B_w=P+Hw\,d.
\]

Write \(A_w=(x_1,y_1)\), \(B_w=(x_2,y_2)\), and define the opposite
rectangle diagonal

\[
C_w=(x_1,y_2),
\qquad
D_w=(x_2,y_1).
\]

Let the second permutation layer be the blocker layer.

## BDA5a -- exact local decoder trichotomy

### Theorem BDA5a -- PROVED

For each \(w\in\{u,v\}\):

1. replacing \(A_w,B_w\) by \(C_w,D_w\) preserves the active row and
   column sets;
2. the new cells are distinct and are not already used by the active
   layer;
3. the anchor and new diagonal are noncollinear, with exact determinant
   \[
   \boxed{
   \det(C_w-P,D_w-P)
   =
   -ab\,w^2q(2h+q)\ne0.
   }
   \]

Let

\[
b_w=
\bigl|\{C_w,D_w\}\cap M_{\mathrm{block}}\bigr|.
\]

Exactly one of the following applies.

- **Empty diagonal, \(b_w=0\).**  The one-layer rectangle switch
  \(A_w,B_w\rightsquigarrow C_w,D_w\) is admissible.
- **Full diagonal, \(b_w=2\).**  Exchanging the colours of the four
  rectangle cells is an admissible two-layer phase flip: the active
  layer takes \(C_w,D_w\), and the blocker layer takes \(A_w,B_w\).
- **Single blocker, \(b_w=1\).**  One desired cross cell is empty and
  the other is an explicitly identified blocker-layer cell.  This is a
  one-blocker alternating-path seed.

Both the empty-diagonal switch and the full-diagonal phase flip remove
one cell from each of \(T_h(P)\) and \(T_H(P)\), hence destroy both paid
radial triples.  They replace the same-role collinear triple
\(\{P,A_w,B_w\}\) by the noncollinear triple
\(\{P,C_w,D_w\}\).

If neither role supplies an empty-diagonal switch or a full-diagonal
phase flip, then

\[
\boxed{b_u=b_v=1.}
\]

The clean-support hypothesis makes the two rectangle row sets and
column sets disjoint.  Hence these are two row-column-disjoint,
explicit one-blocker alternating-path seeds.

### Proof

The two rectangle diagonals use the same two rows and columns, proving
row-column preservation.  Since the active layer is a matching and
already uses those rows and columns at \(A_w,B_w\), neither cross cell
can be another active cell.  The endpoints differ by \(qw(a,b)\), so
the rows, columns, and cross cells are distinct.

After translating \(P\) to the origin,

\[
C_w=(hwa,Hwb),
\qquad
D_w=(Hwa,hwb).
\]

Therefore

\[
\begin{aligned}
\det(C_w,D_w)
&=ab\,w^2(h^2-H^2)\\
&=-ab\,w^2q(2h+q),
\end{aligned}
\]

which is nonzero over the integer grid.

If neither cross cell belongs to the blocker layer, both are empty in
the two-layer configuration and the one-layer switch is admissible.  If
both belong to the blocker layer, the two layers occupy complementary
perfect matchings of the same \(2\times2\) row-column rectangle.
Swapping those matchings preserves every row and column in both layers
and preserves inter-layer disjointness.  If exactly one cross cell is
blocked, the other is empty and the blocker is precisely exposed.

In either admissible state, \(A_w\) and \(B_w\) leave the active layer,
so both paid triples are destroyed.  The determinant calculation gives
the asserted replacement geometry.

Finally, if neither of the first two cases occurs for either role, both
blocker counts equal one.  Cleanliness gives distinct rows and columns
for the four active radial endpoints, so the two corresponding
rectangles, their blockers, and their exposed empty cells are
row-column-disjoint. \(\square\)

## BDA5b -- local paid comparison

Let \(D_h,D_H\geq0\) be the paid weights assigned to the two radial
triples.  For an admissible empty-diagonal switch or full-diagonal phase
flip \(S\), let \(\operatorname{Coll}(S)\) be the total weight of newly
created candidate triples, including both colours in the phase-flip
case.

### Corollary BDA5b -- PROVED

If one admissible state satisfies

\[
\boxed{
\operatorname{Coll}(S)<D_h+D_H,
}
\]

then it strictly lowers the paid triple potential while preserving both
permutation layers.

If no such state is available, then every role is accounted for by one
of two explicit facts:

1. its admissible state's collateral is at least \(D_h+D_H\); or
2. it is one of the two disjoint single-blocker seeds from BDA5a.

### Proof

Every admissible state destroys both paid radial triples by BDA5a.
Subtracting its newly created collateral gives net change at most
\(\operatorname{Coll}(S)-(D_h+D_H)\), which is negative under the
displayed hypothesis.  If no improving admissible state exists, every
geometrically available state fails that inequality, while unavailable
roles are classified by the BDA5a trichotomy. \(\square\)

## BDA5c -- coupled derangement of single blockers

Suppose \(t\ge2\) row-column-disjoint single-blocker rectangles have
been selected from clean co-anchored radial pairs, using at most the two
roles of each pair.  Label their active rectangle endpoints by
\(A_j,B_j\), and their blocked cross cells by

\[
Q_j=(c_j,r_j),
\]

and their empty cross cells by \(Z_j\).  The cells \(Q_j\) belong to the
blocker layer.  Row-column disjointness makes the columns
\(c_1,\ldots,c_t\) distinct and the rows \(r_1,\ldots,r_t\) distinct.

For a fixed-point-free permutation \(\pi\in S_t\), simultaneously:

1. switch every active diagonal \(A_j,B_j\) to \(Q_j,Z_j\);
2. remove the blocker cells \(Q_j\);
3. insert the blocker-layer matching
   \[
   \boxed{
   \{(c_j,r_{\pi(j)}):1\leq j\leq t\}.
   }
   \]

### Theorem BDA5c -- PROVED

Every such coupled state preserves all rows and columns in both
permutation layers and keeps the layers disjoint.  It moves every
selected blocker, makes every active rectangle switch admissible, and
destroys both paid radial triples in every represented co-anchored
pair.

A coupled state exists for every \(t\ge2\), for example from the cyclic
shift \(j\mapsto j+1\pmod t\).

For \(t\ge7\), let \(\Omega_t\) be the uniform bank of all
fixed-point-free permutations.  Then

\[
\boxed{
|\Omega_t|\geq\frac{t!}{128},
}
\]

and every prescribed compatible partial blocker matching of rank \(r\)
has cylinder probability at most

\[
\boxed{
\frac{128}{(t)_r}.
}
\]

### Proof

The active rectangle switches preserve their pairwise disjoint row and
column sets.  Removing \(Q_j\) from the blocker layer frees exactly
column \(c_j\) and row \(r_j\), so the displayed replacement is a
perfect matching on the same selected columns and rows.

After the active switch, the unique active cell in column \(c_j\) is
\(Q_j=(c_j,r_j)\).  A blocker replacement
\((c_j,r_{\pi(j)})\) equals it only when \(\pi(j)=j\).  Thus a
fixed-point-free replacement is disjoint from the entire active layer.
All selected active endpoints leave.  Every represented radial pair has
at least one selected role, so BDA5a destroys both of its paid triples.

The cyclic shift proves existence.  The bank \(\Omega_t\) is AN1 with
only the original diagonal positions forbidden.  Its count and cylinder
bounds follow directly from AN1. \(\square\)

## BDA5d -- coupled-bank collateral criterion

Let \(D\) be the total paid weight of the distinct radial triples
destroyed by the represented co-anchored pairs.  After performing all
deterministic active rectangle switches, let \(F\) be their fixed
collateral together with collateral using no replacement blocker cell.
For \(r=1,2,3\), let \(T_r\) be the total weight of candidate
monochromatic triples that use exactly \(r\) mutually compatible
nonforbidden cells of the blocker replacement matching.

### Corollary BDA5d -- PROVED

For \(t\ge7\), if

\[
\boxed{
D
>
F
+
128\left(
\frac{T_1}{t}
+
\frac{T_2}{t(t-1)}
+
\frac{T_3}{t(t-1)(t-2)}
\right),
}
\]

then one coupled two-layer state strictly lowers the paid triple
potential.

### Proof

BDA5c destroys paid weight \(D\) in every state.  Its AN1 cylinder
bound shows that the expected variable collateral is at most the
normalized sum in the display.  Add the fixed collateral \(F\) and
average over \(\Omega_t\). \(\square\)

## BDA5e -- unconditional clean-pair decoder

### Corollary BDA5e -- PROVED

Every clean co-anchored adjacent radial pair has a
row-column-preserving one- or two-layer decoder state that destroys both
paid radial triples:

1. an empty role uses the one-layer rectangle switch;
2. a full role uses the two-colour phase flip;
3. if neither exists, both roles are singly blocked and their two
   disjoint rectangles use the unique size-two derangement in BDA5c.

Thus blocker occupancy is never a local obstruction for a clean pair.
Only the explicitly measurable collateral of the resulting state can
prevent a potential decrease.

### Proof

The first two cases are BDA5a.  In the remaining case, BDA5a gives two
row-column-disjoint single-blocker rectangles, one for each role of the
same pair.  Apply BDA5c with \(t=2\); the transposition is fixed-point
free and hence supplies the required coupled state.  Either role switch
removes one endpoint from each paid triple, so the coupled state
destroys both. \(\square\)

BDA5a--BDA5e resolve the local common-increment geometry and the
multi-pair single-blocker obstruction.  The remaining global work is to
bound the explicitly named collateral of the rectangle or coupled
derangement banks, and to handle clean-support failure or the affine
anchor concentration returned by BDA4e.  No other local blocking
pattern exists on a clean co-anchored radial family.

`scripts/verify_bda_radial_rectangle_decoder.py` exhaustively checks the
rectangle determinant and row-column preservation for small integer
parameters, enumerates all compatible blocker-layer occupancies, and
verifies the empty/full/single-blocker classification, two-role
fallback, and coupled blocker derangements.

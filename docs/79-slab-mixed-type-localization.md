# Slab separation and mixed-type localization

PP3gb removes a same-slot movement/refill pair together with a movement point
from another macro.  The ordered slab geometry gives a broader sign
separation: any two movement points belonging to distinct macros determine a
positive-slope line, while every refill point lies strictly to their right and
below the new-row region.  Hence no refill point can complete that pair.

## 1. Distinct-macro movement pairs

Use the column-slab architecture of PP3ga--PP3gb.  Thus

\[
 C_1<C_2<\cdots<C_M
\]

are disjoint old-column slabs, and

\[
 A_1<A_2<\cdots<A_M
\]

are the corresponding consecutive movement-row blocks.  Every movement point
of macro `i` belongs to `C_i x A_i`, while every refill point has the form

\[
 (B,y),\qquad B>m,\quad y\le m.
\]

### Theorem PP3gn -- PROVED

Let `P` and `Q` be movement points from two distinct macros.  No refill point
from any macro is collinear with `P,Q`.

#### Proof

Suppose `P in C_i x A_i` and `Q in C_j x A_j` with `i<j`.  Write

\[
 P=(x,a),\qquad Q=(x',a').
\]

The slab orders give

\[
 x<x',\qquad a<a'.
\]

Therefore the line `PQ` has positive slope.  Every refill point `F=(B,y)`
satisfies

\[
 B>m\ge x',\qquad y\le m<a'.
\]

But to the right of `Q`, a positive-slope line has ordinate strictly larger
than `a'>m`.  Hence `F` cannot lie on `PQ`. ∎

This argument is independent of the slot-edge domains, the internal local
lemma, and the assignment of refill labels.

## 2. Transposed statement

Use instead the row-slab architecture of PP3gc: old-row slabs and refill-column
blocks are ordered in the same direction.

### Corollary PP3go -- PROVED

No movement point from any macro is collinear with two refill points belonging
to distinct macros.

#### Proof

Transpose PP3gn. ∎

## 3. Mixed-event localization

Call a patch point type `M` or `F` according as it is a movement or refill
point.

### Corollary PP3gp -- PROVED

In the column-slab architecture, every surviving cross-macro triple of type
`2M+1F` has both movement points in the same macro.

In the row-slab architecture, every surviving cross-macro triple of type
`1M+2F` has both refill points in the same macro.

Consequently, the corresponding mixed rank-three events involve at most two
macro variables: one macro supplies the repeated point type and one macro
supplies the third point.

#### Proof

If the two movement points in a `2M+1F` triple belonged to distinct macros,
PP3gn would forbid the triple.  The refill statement is its transpose. ∎

This is stronger than the earlier same-slot cancellation PP3gd.  It removes
all distinct-macro repeated-type pairs, including pairs controlled by two
different slots and two different source edges.

## 4. Active-slot degree reduction

Let each macro contain

\[
 n=2W
\]

slots and let

\[
 N=Mn=2MW
\]

be the total slot count.

### Proposition PP3gq -- PROVED

In the column-slab architecture, the number of formal `2M+1F` slot triples
containing a fixed slot and not already excluded by PP3gp is at most

\[
 \boxed{
 (n-1)(N-n)+(M-1)\binom n2.
 }
\]

The same bound holds for `1M+2F` triples in the row-slab architecture.

#### Proof

If the fixed slot supplies one of the repeated-type movement points, choose the
other movement slot from the same macro in `n-1` ways and the refill slot from
another macro in `N-n` ways.

If the fixed slot supplies the refill point, choose one of the other `M-1`
macros and two movement slots inside it, giving `(M-1) binom(n,2)` choices.
There are no other surviving macro patterns by PP3gp. ∎

Since `n=2W`, the bound is

\[
 O(MW^2)=O(TW),
\]

rather than the unpruned `Theta(T^2)` partner-pair count.  At the balanced
exponents this saves a factor of `M=m^{23/80+o(1)}`.  It is not yet small enough
for PP3gi by itself, but it reduces the remaining completion-energy problem to
same-macro secants tested against one other macro.

## 5. Revised residual event classes

After column-slab separation, the cross-macro patch-only relations consist of:

1. all-movement triples;
2. all-refill triples;
3. `2M+1F` triples whose two movement points lie in one macro;
4. `1M+2F` triples.

The row-slab architecture has the transposed list.  Thus the unresolved mixed
class is no longer a fully three-macro population.  A completion-energy theorem
may exploit one internally generated secant family per macro and its incidences
with the other macro pools.

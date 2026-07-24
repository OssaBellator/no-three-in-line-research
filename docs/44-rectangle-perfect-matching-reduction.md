# Rectangle perfect-matching reduction for arbitrary-map PX28 states

PX39 removes the selected fine permutation as a gauge coordinate.  For the
canonical side-two outer factor, the remaining normalized state has an even
cleaner description: it is a perfect matching of four-corner rectangles
controlled by three independent permutations.

This chapter gives the exact reduction and classifies every possible bad
triple.  It turns the unrestricted PX28 existence problem into a dense
conflict-free perfect-matching problem.

## 1. Three-permutation rectangle normal form

Normalize the first coarse row and column block maps to the identity.  Write

\[
p=\alpha_1,
\qquad
t=\tau,
\qquad
r=\beta_1\circ\tau.
\]

Because `beta_1` and `tau` are permutations, `p,t,r` may be chosen independently
from `Sym([n])`.  Conversely,

\[
\beta_1=r\circ t^{-1}.
\]

For one orientation define the two scalar row embeddings

\[
X_0(u)=
\begin{cases}
u,&\theta_x=c,\\
2u,&\theta_x=f,
\end{cases}
\qquad
X_1(v)=
\begin{cases}
n+v,&\theta_x=c,\\
2v+1,&\theta_x=f,
\end{cases}
\]

and analogously

\[
Y_0(w)=
\begin{cases}
w,&\theta_y=c,\\
2w,&\theta_y=f,
\end{cases}
\qquad
Y_1(z)=
\begin{cases}
n+z,&\theta_y=c,\\
2z+1,&\theta_y=f.
\end{cases}
\]

For each `u in [n]`, put

\[
R_u
=
\{X_0(u),X_1(p(u))\}
\times
\{Y_0(t(u)),Y_1(r(u))\}.
\]

### Theorem PX41 -- PROVED

Every normalized arbitrary-map PX28 state for the canonical side-two outer
factor is exactly

\[
\boxed{
Q(p,t,r)=\bigcup_{u\in[n]}R_u
}
\]

for a unique ordered triple of permutations `p,t,r`.  Conversely every such
triple gives a saturated PX28 state of `4n` points in `[2n]^2`.

### Proof

The two outer layers select the four combinations of coarse row block
`i in {0,1}` and coarse column block `j in {0,1}`.  In row block zero the fine
row digit is `u`; in row block one it is `p(u)`.  In column block zero the fine
column digit is `t(u)`; in column block one it is

\[
\beta_1(t(u))=r(u).
\]

Thus the four selected points indexed by `u` are precisely the four Cartesian
corners of `R_u`.

Since `p,t,r` are permutations, the first and second row coordinates each occur
once as rectangle sides, and the same is true for both column-coordinate
families.  Hence every scalar row and column contains exactly the two corners
of one rectangle.  Conversely `beta_1=r t^{-1}` realizes every triple. \(\square\)

## 2. Exact bad-triple classification

A rectangle has two adjacent-corner pairs in its rows, two adjacent-corner pairs
in its columns, and two opposite-corner diagonal pairs.

### Theorem PX42 -- PROVED

Every real-collinear triple in `Q(p,t,r)` has exactly one of the following two
forms.

1. **Diagonal conflict:** two opposite corners of one rectangle `R_u` together
   with one corner of a different rectangle `R_v`.
2. **Transversal conflict:** one corner from each of three distinct rectangles.

No other rectangle-multiplicity pattern is possible.

### Proof

Three corners of one nondegenerate rectangle are never collinear: their
absolute determinant is the product of the rectangle's nonzero width and
height.

Suppose a bad triple contains two corners of one rectangle.  If those corners
are adjacent, they lie in one scalar row or scalar column.  Saturation says that
this row or column contains exactly those two selected points, so no third
selected point lies on their line.  Therefore the two same-rectangle corners
must be opposite corners.  The third point belongs to another rectangle,
giving the diagonal case.

If no rectangle contributes two points, the three points come from three
distinct rectangles, giving the transversal case. \(\square\)

This separates the unrestricted-map geometry into two explicit obstruction
families.  The diagonal family is pairwise at the rectangle level; the
transversal family is genuinely ternary.

## 3. Conflict-free perfect-matching formulation

Let `U,P,T,R` be four disjoint copies of `[n]`.  Form the complete four-partite
four-uniform hypergraph

\[
\mathcal K_n
=
U\times P\times T\times R.
\]

Associate the hyperedge

\[
e=(u,p_0,t_0,r_0)
\]

with the rectangle having row coordinates

\[
X_0(u),\quad X_1(p_0)
\]

and column coordinates

\[
Y_0(t_0),\quad Y_1(r_0).
\]

A perfect matching of `K_n` is exactly a triple of permutations `p,t,r`.
Declare two matching edges conflicting when their two rectangles contain a
diagonal bad triple, and declare three matching edges conflicting when one
corner from each rectangle forms a transversal bad triple.

### Corollary PX42a -- PROVED

A no-three arbitrary-map PX28 state exists at base side `n` if and only if the
complete four-partite hypergraph `K_n` has a perfect matching avoiding every
explicit two-edge and three-edge rectangle conflict.

### Proof

PX41 identifies perfect matchings with saturated PX28 states.  PX42 says that
all collinear triples are represented by exactly the declared conflict sets.
Avoiding all conflicts is therefore equivalent to the no-three property.
\(\square\)

This is a more structured endpoint than the host-cell CNF of PX10.  The
candidate hypergraph is complete and highly symmetric; all difficulty has been
moved into rank-two and rank-three conflicts on rectangle choices.

## 4. Consequences for the remaining bottleneck

The exact PC4 question for the side-two outer factor is now:

> For which `n` does the complete four-partite matching instance `K_n` contain a
> perfect matching avoiding all diagonal and transversal rectangle conflicts?

PX40 gives the complete answer through `n=5`: yes for `n=2,4,5`, and no for
`n=3`.  PX37 rules out only the smaller affine-map subfamily at `n=6,7`; the
full rectangle-matching problem remains open there.

The reduction suggests three concrete routes.

1. Prove conflict-degree or spread bounds sufficient for a conflict-free
   perfect matching.
2. Find a recursive rectangle template that produces successful matchings at
   infinitely many side lengths.
3. Derive a structured obstruction certificate when every perfect matching
   meets a diagonal or transversal conflict.

## Verification

Run

```bash
python scripts/verify_product_rectangle_reduction.py
```

The script exhausts every three-permutation rectangle state for bases two
through four and checks saturation and the complete diagonal/transversal
classification of every bad triple.

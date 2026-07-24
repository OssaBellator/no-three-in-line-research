# Rectangle perfect-matching reduction for arbitrary-map PX28 states

PX39 removes the selected fine permutation as a gauge coordinate.  For the
canonical side-two outer factor, every normalized state has an even cleaner
description: it is a perfect matching of four-corner rectangles controlled by
three independent permutations.

## 1. Three-permutation rectangle normal form

Normalize the first coarse row and column block maps to the identity and write

\[
p=\alpha_1,
\qquad
t=\tau,
\qquad
r=\beta_1\circ\tau.
\]

The permutations `p,t,r` are independent, and conversely

\[
\beta_1=r\circ t^{-1}.
\]

For one orientation define

\[
X_0(u)=
\begin{cases}u,&\theta_x=c,\\2u,&\theta_x=f,\end{cases}
\qquad
X_1(v)=
\begin{cases}n+v,&\theta_x=c,\\2v+1,&\theta_x=f,\end{cases}
\]

and

\[
Y_0(w)=
\begin{cases}w,&\theta_y=c,\\2w,&\theta_y=f,\end{cases}
\qquad
Y_1(z)=
\begin{cases}n+z,&\theta_y=c,\\2z+1,&\theta_y=f.\end{cases}
\]

For each `u in [n]`, put

\[
R_u
=
\{X_0(u),X_1(p(u))\}
\times
\{Y_0(t(u)),Y_1(r(u))\}.
\]

### Theorem PX43 -- PROVED

Every normalized arbitrary-map PX28 state for the canonical side-two outer
factor is exactly

\[
\boxed{Q(p,t,r)=\bigcup_{u\in[n]}R_u}
\]

for a unique ordered triple of permutations `p,t,r`.  Conversely every such
triple gives a saturated PX28 state of `4n` points in `[2n]^2`.

### Proof

The two outer layers select all four combinations of coarse row block and coarse
column block.  In row block zero the fine row digit is `u`; in row block one it
is `p(u)`.  In column block zero the digit is `t(u)`; in column block one it is

\[
\beta_1(t(u))=r(u).
\]

Hence the four selected points indexed by `u` are precisely the Cartesian
corners of `R_u`.  Since `p,t,r` are permutations, every scalar row and column
contains exactly the two corners of one rectangle.  Conversely
`beta_1=r t^{-1}` realizes every triple. \(\square\)

## 2. Exact bad-triple classification

### Theorem PX44 -- PROVED

Every real-collinear triple in `Q(p,t,r)` has exactly one of the following
forms.

1. **Diagonal conflict:** two opposite corners of one rectangle `R_u` together
   with one corner of a different rectangle `R_v`.
2. **Transversal conflict:** one corner from each of three distinct rectangles.

### Proof

Three corners of one nondegenerate rectangle are not collinear: their absolute
determinant is the product of the rectangle's nonzero width and height.

If a bad triple contains two adjacent corners of one rectangle, their line is a
scalar row or column.  Saturation says that line contains exactly those two
selected points.  Therefore two same-rectangle points in a bad triple must be
opposite corners, giving the diagonal case.  If no rectangle contributes two
points, the three points belong to three distinct rectangles, giving the
transversal case. \(\square\)

## 3. Conflict-free perfect-matching formulation

Let `U,P,T,R` be four disjoint copies of `[n]` and form the complete
four-partite four-uniform hypergraph

\[
\mathcal K_n=U\times P\times T\times R.
\]

Associate an edge

\[
e=(u,p_0,t_0,r_0)
\]

with the rectangle having row coordinates `X_0(u),X_1(p_0)` and column
coordinates `Y_0(t_0),Y_1(r_0)`.  A perfect matching of `K_n` is exactly a
triple of permutations `p,t,r`.

Declare two matching edges conflicting when their rectangles contain a
diagonal bad triple.  Declare three matching edges conflicting when one corner
from each rectangle forms a transversal bad triple.

### Corollary PX44a -- PROVED

A no-three arbitrary-map PX28 state exists at base side `n` if and only if
`K_n` has a perfect matching avoiding every explicit two-edge and three-edge
rectangle conflict.

### Proof

PX43 identifies perfect matchings with saturated PX28 states, and PX44 lists
all possible collinear triples. \(\square\)

This endpoint is more structured than the host-cell CNF of PX10: the candidate
hypergraph is complete and symmetric, while all difficulty lies in rank-two
and rank-three rectangle conflicts.

## 4. Exact boundary through base seven

PX40 and PX48 give the complete unrestricted answer through `n=7`:

| Base side | Rectangle template exists? |
|---:|---|
| 2 | yes |
| 3 | no |
| 4 | yes |
| 5 | yes |
| 6 | no |
| 7 | no |
| 8 | open |

The negative results at six and seven concern the full arbitrary-permutation
rectangle family, not only affine maps.  The next decisive finite case is base
eight: success would allow the proved side-four closure to iterate to side
sixteen, while an exact obstruction would rule out that recursion inside PX28.

The remaining routes are now precise:

1. sharpen conflict-degree or spread estimates enough for a conflict-free
   perfect-matching theorem;
2. construct recursive rectangle templates at infinitely many side lengths;
3. derive structured obstruction certificates when every perfect matching has a
   diagonal or transversal conflict;
4. extend the normal form to two inner layers or the full degree-two selector.

## Verification

Run

```bash
python scripts/verify_product_rectangle_reduction.py
python scripts/verify_product_unrestricted_six_seven.py --side 6
python scripts/verify_product_unrestricted_six_seven.py --side 7
```

The first script checks the normal form and conflict classification through base
four.  The latter scripts exhaust the complete rectangle matching instances at
bases six and seven.

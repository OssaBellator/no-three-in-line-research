# Two-column normal form and exact selector moves

The complete side-two outer host has normal form

\[
g_{ijs}=Q^jTH^sP^i,
\qquad i,j,s\in\{0,1\}.
\]

For the side-seven frontier it is useful to separate geometric column placement
from the abstract degree-two selector.  This removes one artificial coupling in
the search variables and gives an exact degree-preserving move graph.

## 1. Two independent column permutations

Put

\[
A_0=T,
\qquad
A_1=QT.
\]

### Theorem PX499 -- PROVED

Every full-selector normal-form host can be written uniquely as

\[
\boxed{
 g_{ijs}=A_jH^sP^i.
}
\]

Conversely, arbitrary permutations `A_0,A_1,P` and the prescribed relative
permutation `H` determine a normal-form host by

\[
T=A_0,
\qquad
Q=A_1A_0^{-1}.
\]

Thus the two coarse column blocks have independent fine-coordinate
permutations.

### Proof

For `j=0`, the original formula is `TH^sP^i=A_0H^sP^i`.  For `j=1`, it is
`QTH^sP^i=A_1H^sP^i`.  Conversely, substitution of the displayed `T,Q` gives
`QT=A_1`.  Uniqueness follows from `A_0=T` and `A_1=QT`. \(\square\)

For a radix orientation `epsilon_x epsilon_y`, the scalar point belonging to
abstract edge `(i,u;j,s)` is

\[
x=
\begin{cases}
ni+u,&\epsilon_x=c,\\
2u+i,&\epsilon_x=f,
\end{cases}
\]

and

\[
y=
\begin{cases}
nj+A_j(H^sP^i(u)),&\epsilon_y=c,\\
2A_j(H^sP^i(u))+j,&\epsilon_y=f.
\end{cases}
\]

## 2. Abstract degree-two selectors

Use abstract row vertices `(i,u)` and abstract column vertices `(j,w)`.  The
four host edges from `(i,u)` are

\[
(i,u)\longrightarrow (j,H^sP^i(u)),
\qquad j,s\in\{0,1\}.
\]

Every abstract row and column has degree four.

### Theorem PX500 -- PROVED

Let `F` be any spanning degree-two subgraph of the abstract host.  Then for every
choice of `A_0,A_1` and every radix orientation, its scalar image has exactly two
selected points in each scalar row and column.

Moreover, if an even cycle alternates between edges of `F` and edges of its
complement, flipping the cycle produces another spanning degree-two selector.
The move is independent of `A_0,A_1` and preserves host membership exactly.

### Proof

Scalar rows are bijective images of the abstract row vertices, so row degree is
unchanged.  In coarse column block `j`, the map `w -> A_j(w)` is a permutation;
hence abstract degree two at `(j,w)` becomes scalar degree two at its unique
image column.  Interleaving instead of concatenating the digits changes only
the displayed coordinate formula, not the bijection.

On an alternating cycle, every incident abstract row and column loses one
selected edge and gains one unselected edge.  All other degrees are unchanged.
Every flipped edge already belongs to the four-regular abstract host.
\(\square\)

This gives a clean search decomposition:

1. choose `P` and an abstract selector `F`;
2. move within the selector space by alternating cycles;
3. optimise the two independent geometric permutations `A_0,A_1`;
4. test real collinearity only after scalar embedding.

The theorem does not assert that the alternating-cycle graph of all selectors is
connected, nor that a side-seven no-three selector exists.

## Verification

Run

```bash
python scripts/verify_product_side_seven_two_column_normal_form.py
```

The verifier compares the original and two-column formulas, checks the converse
reconstruction, constructs random degree-two selectors by two matching layers,
and verifies alternating-cycle degree preservation in all four orientations.
# Two-block rainbow transposition decoder

PX253--PX255 reduce the coordinate-star-field construction to mixed certificate
weights between two matching blocks. The first new sector is `(1,1)`: one cell
from each random block and one fixed background anchor.

This sector has the same proper-colouring structure as PX191--PX195. A mixed
collision can be destroyed by transposing its selected edge in either block.
If no transposition improves, one off-matching cell has a large shadow against
the other selected block, which again yields a loaded line or clean star.

## 1. Mixed anchor-colour potential

Let `G_1,G_2` be balanced candidate bipartite graphs of orders `n_1,n_2`, with
forbidden row and column degrees at most `Delta_1,Delta_2`. Let `M_1,M_2` be
selected perfect matchings and `Z` a fixed background set. For every `z in Z`,
colour each candidate edge by its real line through `z`; this is proper within
each source row and target column.

Define

\[
\Phi_{12}(M_1,M_2)
=
\sum_{z\in Z}\sum_\gamma
|\{e\in M_1:\chi_z(e)=\gamma\}|
|\{g\in M_2:\chi_z(g)=\gamma\}|.
\]

It is exactly the number of triples with one selected cell from each block and
one anchor in `Z`.

## 2. Destruction by either transposition bank

### Theorem PX256 -- PROVED

Every current mixed collision is destroyed by at least

\[
\boxed{n_1-1-2\Delta_1}
\]

executable transpositions in block one and at least

\[
\boxed{n_2-1-2\Delta_2}
\]

in block two. Its total destruction multiplicity is at least

\[
\boxed{\delta_{12}=n_1+n_2-2-2(\Delta_1+\Delta_2).}
\]

### Proof

Fix a collision `e_i,g,z`. Block one has `n_1-1` possible transposition
partners. At most `Delta_1` fail at each of the two cross positions. Properness
shows neither inserted cross retains the colour of `e_i`, so the unchanged
block-two edge `g` loses the collision. The other block is symmetric. \(\square\)

## 3. Aggregate two-bank inequality

For an allowed off-matching edge `f` of block one, put

\[
\lambda_{1\to2}(f)
=|\{(z,g)\in Z\times M_2:f,g,z\text{ are collinear}\}|,
\]

and let `S_(1->2)` be the sum over all such `f`. Define the reverse direction
symmetrically.

### Theorem PX257 -- PROVED

Summing over executable transpositions in both blocks,

\[
\boxed{
\sum_{\omega\in\Omega_1}\Delta_\omega\Phi_{12}
+
\sum_{\eta\in\Omega_2}\Delta_\eta\Phi_{12}
\le
\mathcal S_{1\to2}+\mathcal S_{2\to1}
-
\delta_{12}\Phi_{12}.
}
\]

Hence some transposition improves when the destruction term exceeds the two
shadow sums.

### Proof

PX256 counts destruction incidences. In either transposition bank every
off-matching cross edge occurs in at most one swap, so every new mixed collision
is charged once to its directional shadow. There is no two-inserted-edge term:
a mixed collision uses exactly one cell from each block. \(\square\)

## 4. Local-minimum shadow extraction

Let `Lambda_(1->2)` and `Lambda_(2->1)` be the directional maximum shadows.

### Corollary PX258 -- PROVED

At a joint transposition-local minimum with `Phi_12>0`,

\[
\boxed{
\delta_{12}\Phi_{12}
\le
n_1(n_1-1)\Lambda_{1\to2}
+
n_2(n_2-1)\Lambda_{2\to1}.
}
\]

Thus at least one directional maximum is at least its corresponding half of
this lower bound.

### Proof

At a local minimum every transposition change in PX257 is nonnegative. Each
block has at most `n_i(n_i-1)` off-matching cells. \(\square\)

## 5. Heavy cross-shadows return to first-generation geometry

Let

\[
L_Z^{12}=
\max_{f,g}|\{z\in Z:f,g,z\text{ are collinear}\}|.
\]

### Theorem PX259 -- PROVED

For a cell `f` with directional shadow `Lambda` and every threshold `K`, either
one line through `f` contains more than `K` selected cells of the other block,
or `f` centres an endpoint-disjoint clean star of order at least

\[
\boxed{\frac{\Lambda}{L_Z^{12}+K}.}
\]

### Proof

Form the incidence graph on `Z` and the other selected matching. The degree of a
selected matching cell is at most `L_Z^(12)`. If every anchor degree is at most
`K`, greedy bipartite matching extraction gives the displayed star; otherwise
an anchor line is loaded. \(\square\)

Thus the mixed `(1,1)` sector recursively decodes to the same loaded-line or
clean-star geometry as the one-block collision potential.

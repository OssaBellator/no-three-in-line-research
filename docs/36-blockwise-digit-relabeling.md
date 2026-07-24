# Blockwise digit relabelling and the side-ten escape

This chapter enlarges the global mixed-radix product hosts of Chapters 27--35
without enlarging the ambient `mn x mn` grid.  The new freedom is to relabel the
fine row digits independently inside each coarse row block and the fine column
digits independently inside each coarse column block.

It produces an exact saturated no-three configuration at side ten from a
`2 x 5` factor pair, thereby breaking the positive defect gap proved for all
four unmodified global product hosts.  It does **not** prove multiplicative
closure.

## 1. Blockwise digit maps

Let

\[
S_m=\{(i,\sigma_r(i)):i\in[m],\ r\in\{0,1\}\}
\]

and

\[
S_n=\{(u,\tau_s(u)):u\in[n],\ s\in\{0,1\}\}
\]

be saturated no-three factor configurations.  For every coarse row `i`, choose

\[
\rho_i\in\operatorname{Sym}([n]),
\]

and for every coarse column `j`, choose

\[
\gamma_j\in\operatorname{Sym}([n]).
\]

Define the blockwise scalar row maps

\[
X_c^\rho(i,u)=ni+\rho_i(u),
\qquad
X_f^\rho(i,u)=m\rho_i(u)+i,
\]

and the blockwise scalar column maps

\[
Y_c^\gamma(j,v)=nj+\gamma_j(v),
\qquad
Y_f^\gamma(j,v)=m\gamma_j(v)+j.
\]

For an orientation

\[
\theta=(\theta_x,\theta_y)\in\{c,f\}^2,
\]

put

\[
F_{\theta,\rho,\gamma}(i,j,u,v)
=
\bigl(X_{\theta_x}^\rho(i,u),Y_{\theta_y}^\gamma(j,v)\bigr).
\]

The full blockwise product host is

\[
\mathcal H^{\theta,\rho,\gamma}_{m,n}
=
\{F_{\theta,\rho,\gamma}(i,\sigma_r(i),u,\tau_s(u)):
 r,s\in\{0,1\}\}.
\]

## Theorem PX24 -- PROVED

For arbitrary block permutations `rho_i` and `gamma_j`, the host

\[
\mathcal H^{\theta,\rho,\gamma}_{m,n}
\]

is a simple four-regular bipartite graph between the `mn` scalar rows and the
`mn` scalar columns.  Consequently every spanning degree-two subgraph is a
saturated `2mn`-cell configuration and decomposes into two disjoint permutation
layers.

### Proof

Both blockwise row flattenings are bijections from `[m] x [n]` to `[mn]`:
inside coarse block `i`, the map `rho_i` is a permutation.  The same argument
applies to the column flattenings.

Fix a decoded row pair `(i,u)`.  There are two distinct coarse columns

\[
\sigma_0(i),\qquad\sigma_1(i)
\]

and, independently, two distinct fine columns

\[
\tau_0(u),\qquad\tau_1(u).
\]

Because every `gamma_j` is injective, these four decoded column pairs give four
distinct scalar columns.

Conversely, fix a decoded target column pair `(j,w)`, where the pre-relabelling
fine digit is

\[
v=\gamma_j^{-1}(w).
\]

For each outer layer `r` there is a unique

\[
i=\sigma_r^{-1}(j),
\]

and for each inner layer `s` there is a unique

\[
u=\tau_s^{-1}(v).
\]

These four choices give four distinct scalar rows.  Thus the host is simple and
four-regular.  The degree-two and two-permutation conclusions follow exactly as
in PX9 by alternating the edges on every cycle of the selected two-regular
bipartite graph. \(\square\)

The blockwise maps are generally not one global affine transformation of the
integer grid.  Therefore the four-term determinant identity PX2 does not reduce
their geometry to the original digit determinants without additional case
information.

## 2. A one-inner-layer twisted product

The enlarged host contains a simpler explicit saturated subfamily.  Fix one
inner permutation layer `s`.  Define

\[
Q_s^{\theta,\rho,\gamma}
=
\left\{
F_{\theta,\rho,\gamma}
\bigl(i,\sigma_r(i),u,\tau_s(u)\bigr):
 r\in\{0,1\},\ i\in[m],\ u\in[n]
\right\}.
\]

## Theorem PX25 -- PROVED

For every choice of factors, blockwise digit maps, orientation, and fixed inner
layer `s`, the set

\[
Q_s^{\theta,\rho,\gamma}
\]

has exactly `2mn` cells and is the union of two disjoint permutation graphs.
Hence it has exactly two cells in every scalar row and column and is
constructible in `O(mn)` time.

### Proof

For fixed outer layer `r`, the decoded map

\[
(i,u)\longmapsto\bigl(\sigma_r(i),\tau_s(u)\bigr)
\]

is a bijection of `[m] x [n]`.  Composing it with the blockwise row and column
bijections gives one permutation graph on `[mn]`.  The two outer layers are
disjoint because

\[
\sigma_0(i)\ne\sigma_1(i)
\]

for every `i`. \(\square\)

Theorem PX25 reduces one enlarged construction problem to choosing the block
maps and one factor permutation so that the resulting two permutation graphs
have no collinear triple.

## 3. Exact side-ten construction

Take the saturated side-two factor

\[
\sigma_0=(0,1),
\qquad
\sigma_1=(1,0),
\]

and the saturated side-five factor

\[
\tau_0=(0,2,1,4,3),
\qquad
\tau_1=(2,4,0,3,1).
\]

Let

\[
q(u)=4-u.
\]

Use the block maps

\[
\rho_0=\operatorname{id},
\qquad
\rho_1=q,
\]

\[
\gamma_0=\operatorname{id},
\qquad
\gamma_1=q,
\]

and the fine-major/fine-major orientation `ff`.

## Theorem PX26 -- PROVED FINITE

The one-inner-layer state

\[
Q_1^{ff,\rho,\gamma}
\]

is a saturated no-three configuration of twenty cells in `[10]^2`.
Equivalently, it is the union of the two permutation graphs

\[
\pi_0=(4,2,1,3,0,9,6,8,7,5),
\]

\[
\pi_1=(5,7,8,6,9,0,3,1,2,4).
\]

Thus

\[
D(10)=20.
\]

### Verification

The verifier checks that both displayed sequences are permutations, are
pointwise disjoint, belong to the blockwise product state above, and that all

\[
\binom{20}{3}
\]

integer determinants are nonzero.

This construction defeats the unmodified-host lower bound PX23: all four
global `2 x 5` hosts had minimum defect at least two, while one local reversal
of the fine digits in the second coarse row and second coarse column removes
all defects without changing the side length.

## 4. Complete identity/reversal census

Restrict every block map to either

\[
\operatorname{id}
\quad\text{or}\quad
q(u)=4-u.
\]

There are sixteen assignments to the two coarse row blocks and two coarse
column blocks.  Work with the 32 layer-unordered saturated no-three side-five
factors and all four radix orientations.

## Theorem PX27 -- PROVED FINITE

Exactly four of the sixteen block-map patterns admit any no-three degree-two
product-host state.  They are precisely the patterns in which

\[
\rho_0\ne\rho_1
\qquad\text{and}\qquad
\gamma_0\ne\gamma_1.
\]

For each of these four equivalent patterns:

- 13 factor/orientation hosts contain a no-three degree-two state;
- those successes involve 9 of the 32 layer-unordered side-five factors;
- 7 factor/orientation hosts are already solved by the one-inner-layer family
  PX25;
- those simple successes involve 7 distinct side-five factors.

Every other identity/reversal pattern has zero successful host states and zero
successful one-inner-layer states.

### Proof

Enumerate all 32 layer-unordered side-five factor pairs, all four orientations,
and all sixteen block-map assignments.  For each four-regular host, perform an
exact row-by-row degree-two search with determinant pruning.  Independently test
both one-inner-layer states from PX25.  The counts above result. \(\square\)

The finite census shows that variation in both coordinate families is essential
inside this smallest reversal-only enlargement: varying only coarse row blocks
or only coarse column blocks does not remove the `2 x 5` obstruction.

## 5. Verification and updated boundary

Run

```bash
python scripts/verify_product_blockwise_reversal.py
```

The script uses only the standard library and checks the full sixteen-pattern
census, not just the displayed side-ten witness.

PX24--PX27 establish that the positive `2 x 5` defect gap is an obstruction to
the **global** mixed-radix host, not to product composition inside the same
ambient side length.  The next useful target is an infinite theorem selecting
blockwise maps from a controlled family, such as affine permutations of the
fine digits, while proving no-three feasibility or returning a structured
obstruction.

PC4 and PC5 remain open: one finite side-ten escape does not give an infinite
multiplicative closure class or arithmetic coverage.

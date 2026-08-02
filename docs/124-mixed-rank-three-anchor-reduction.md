# Mixed rank-three sectors reduce to the rainbow decoder

PX253--PX255 organize two-block certificates by ranks `(r_1,r_2)`. PX256--PX259
handle `(1,1)`. The remaining mixed rank-three sectors `(2,1)` and `(1,2)` are
ordinary one-block rainbow collisions with the other selected matching acting
as the anchor set.

## 1. Exact anchor reduction

For `g in M_2`, colour block-one candidate edges by their line through `g`, and
put

\[
\Phi_{21}(M_1;M_2)
=
\sum_{g\in M_2}\sum_\gamma
\binom{|\{e\in M_1:\chi_g(e)=\gamma\}|}{2}.
\]

### Theorem PX260 -- PROVED

`Phi_21` is exactly the number of collinear triples with two compatible selected
cells from block one and one selected cell from block two. The symmetric
potential counts `(1,2)`.

### Proof

For a fixed anchor `g`, two block-one cells form a triple with `g` exactly when
they receive the same line colour. Sum the monochromatic pairs. \(\square\)

## 2. General-degree transposition inequality

### Theorem PX261 -- PROVED

Every current `(2,1)` collision is destroyed by at least

\[
\boxed{2(n_1-2-2\Delta_1)}
\]

executable block-one transpositions. With the PX194 one-inserted and
two-inserted creation shadows `S_1,S_2`, now using anchor set `M_2`,

\[
\boxed{
\sum_\omega
[\Phi_{21}(M_1^\omega;M_2)-\Phi_{21}(M_1;M_2)]
\le
\mathcal S_1+\mathcal S_2
-2(n_1-2-2\Delta_1)\Phi_{21}.
}
\]

### Proof

Move either of the two colliding edges while leaving the other fixed. There are
`n_1-2` partners and at most `2Delta_1` failures. Properness destroys the old
colour collision. The two moved-endpoint swap families are disjoint. Creation
is charged exactly as in PX194. \(\square\)

## 3. Local-minimum decoder

Let `Lambda` be the maximum one-inserted shadow and let

\[
L_2=
\max_{f,f'}|\{g\in M_2:f,f',g\text{ are collinear}\}|.
\]

### Theorem PX262 -- PROVED

At a block-one transposition-local minimum,

\[
\boxed{
2(n_1-2-2\Delta_1)\Phi_{21}
\le
n_1(n_1-1)\Lambda
+
L_2\binom{n_1}{2}.
}
\]

A cell attaining `Lambda` either lies on a line carrying more than `K_1`
selected block-one cells with one block-two anchor, or centres an
endpoint-disjoint clean star in `M_2 times M_1` of order at least

\[
\boxed{\frac{\Lambda}{L_2+K_1}.}
\]

The symmetric statement closes `(1,2)`.

### Proof

Bound `S_1` by the number of off-matching cells times `Lambda`, and `S_2` by
`L_2` times the number of transpositions. Insert into PX261. The geometric
extraction is the same bipartite shadow matching used in PX195a. \(\square\)

Every mixed rank-at-most-three sector in PX254 now has an explicit decoder back
to loaded-line or clean-star geometry. The remaining issue is amortized strict
sign and terminal absorption, not mixed-sector classification.

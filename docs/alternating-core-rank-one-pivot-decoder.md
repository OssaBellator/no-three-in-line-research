# Executable rectangle decoder for rank-one collateral pivots

**Branch:** `research/alternating-core-chain`

AC3fa--AC3fo reduce every failed executable BDA/RI bank and every explicit RI fixed, moving or blocker profile to created-cell rank one, two or three relative to a fixed parent configuration. This note terminates the purely local existence and payment questions for rank one. In a realized two-layer state, every rank-one triple has one distinguished cell absent from the parent configuration and two parent-current context cells. Aggregating by that pivot cell gives disjoint current-certificate payment buckets. A two-column rectangle switch removes the pivot and destroys its whole bucket; the opposite layer is repaired by the exact zero/singleton/two-intersection menu.

## Rank-one pivot buckets

Fix a parent two-layer union `M` and one realized legal descendant state `S`. Let `C_1(S;M)` be a weighted family of current collinear triples `T` in the union of the two layers with

$$
|T\setminus M|=1.
$$

For each such triple, write

$$
p(T)
$$

for its unique pivot cell in `T\setminus M`. For a pivot `z`, put

$$
\mathcal P_z=\{T\in C_1(S;M):p(T)=z\},
$$

and let

$$
W_z=\sum_{T\in\mathcal P_z}w(T).
$$

The two context cells of a triple may lie in either layer. Only the pivot's own layer is used for the decoder below.

## AC3fs -- exact pivot rectangle decoder -- PROVED

Assume `W_z>0`, and let `L_z` be the permutation layer containing `z`. Choose any other cell `a_z` of `L_z`. Such a cell exists: a current triple requires a grid with at least two columns, and `L_z` is a full permutation layer. Write

$$
z=(c_0,r_0),
\qquad
a_z=(c_1,r_1).
$$

In `L_z`, replace the active diagonal

$$
\{(c_0,r_0),(c_1,r_1)\}
$$

by the opposite diagonal

$$
z'=(c_0,r_1),
\qquad
a_z'=(c_1,r_0).
$$

This switch preserves that layer's row and column sets, removes `z`, and therefore destroys every certificate in `P_z`.

Let the opposite permutation layer occupy `t` of the two desired cross cells, where `t` is `0,1` or `2`. A legal repaired opposite layer always exists:

1. `t=0`: leave it unchanged;
2. `t=1`: transpose the unique blocked desired cell with any other cell of the opposite permutation;
3. `t=2`: transpose the two blocked rows, equivalently exchange the two rectangle diagonals between the layers.

Every resulting state is a legal two-layer permutation state and destroys certified current weight at least `W_z`.

### Proof

The two selected cells are distinct cells of one permutation layer, so they use distinct rows and columns. The opposite diagonal is disjoint from that layer and preserves its row and column sets. Every triple in `P_z` contains `z`, regardless of the layers of its two context cells, so removal of `z` destroys the entire bucket.

For the opposite layer, the zero and two cases are the standard empty-diagonal switch and phase flip. In the singleton case the grid has at least two columns, so the opposite permutation has another cell. Transposing the blocked desired cell with any other opposite-layer cell preserves all opposite-layer rows and columns. Neither replacement can equal a cell of the switched first layer: one uses a selected active column with the wrong active row, and the other uses the selected active row in a different column. This is the RI5h singleton-repair argument. QED.

## AC3ft -- exact private payment by pivot aggregation -- PROVED

The pivot buckets partition `C_1(S;M)`. In particular, for distinct pivots `z!=z'`,

$$
\boxed{
\mathcal P_z\cap\mathcal P_{z'}=\varnothing.
}
$$

Give the pivot decoder at `z` the private paid set `P_z`. Then every finite pivot family `X` satisfies the exact payment identity

$$
\boxed{
\sum_{z\in X}W_z
=
w\left(\mathop{\dot\bigcup}_{z\in X}\mathcal P_z\right).
}
$$

Thus pivot decoders do not double-count destroyed certificates. An aggregated pivot of integer capacity may be split into distinguishable paid copies exactly as in AC3do.

### Proof

A rank-one triple has exactly one cell outside the fixed parent set `M`, so it has exactly one pivot. The buckets therefore partition the triple family. AC3fs destroys every certificate in its own bucket, and disjoint union gives the payment identity. QED.

## Scope-complete pivot envelopes

For a pivot `z`, let `E_z` contain:

- the pivot, selected same-layer partner and both cross cells;
- every opposite-layer cell used by the zero/singleton/two-intersection repair menu;
- the private paid bucket `P_z`;
- every row, column, replacement, potential-factor, protected-bank and feasibility scope meeting any local state.

Build the canonical AC3v primal graph on the pivot decoders.

## AC3fu -- paid pivot bank or explicit overload -- PROVED

Let a realized rank-one family have total current weight

$$
W_1=\sum_zW_z.
$$

For every `K>=1`, one of the following holds.

1. One pivot decoder has closed-neighbourhood paid load greater than `K W_z`; AC3fr localizes the overload to one explicit role-labelled cell, row, column, cross-triple or protected witness.
2. An independent executable pivot family has certified payment
   $$
   \boxed{D\ge W_1/K.}
   $$
   Every product of its local repair choices is legal, and every state destroys all represented pivot buckets.

### Proof

AC3ft gives disjoint private paid sets. AC3v includes every interaction in the primal graph and makes independent envelopes jointly legal and additive. Apply AC2c. The dense alternative uses the AC3fp--AC3fr dictionary. QED.

## AC3fv -- pivot-product comparison and reverse ticket -- PROVED

Choose independently from the finite local repair menu of every decoder in an executable pivot family. Relative to the realized state `S`, every newly created triple has AC3fa rank one, two or three. Let `N'_k` be its exact expected weight at new-cell rank `k`.

Then

$$
\boxed{
\mathbb E[\text{destroyed certified payment}]=D,
}
$$

$$
\boxed{
\mathbb E[\text{created collateral}]=N'_1+N'_2+N'_3.
}
$$

If `D>N'_1+N'_2+N'_3`, one product state improves. If no product state improves, one rank has expected weight at least

$$
\boxed{D/3\ge W_1/(3K).}
$$

Give the axis-parallel rectangle

$$
\tau_z=
(
\text{layer},
\{c_0,c_1\},
\{r_0,r_1\},
\text{exact local decorations}
)
$$

one capacity-one ticket, independent of which diagonal is currently occupied. The reverse rectangle switch has the same row set, column set and decorations, and therefore cannot occur immediately in the unticketed transition graph.

### Proof

AC3fs destroys every private bucket in every local state, while AC3ft and AC3v give exact additivity. AC3fa partitions all genuinely new collateral by pre-transition rank, proving the expectation identities and the failed-bank `D/3` return. The reverse switch exchanges the two diagonals of the same row-column rectangle, so both directions consume the same ticket. QED.

## Interface to the fixed and variable rank-one outputs

The theorem applies whenever a realized state and its parent configuration are fixed.

- A state-independent RI closure rank-one term is present in every closed-I6 state, so its closure cell is directly a pivot.
- A universal crossed-closure or `mh=2` transfer rank-one term is handled identically in the layer containing its unique new cell.
- A realized BDA decoder, companion rectangle, moving-channel or crossed-blocker rank-one output supplies the same unique-pivot partition after that local state is fixed.

For expected variable collateral, AC3fs is applied after selecting a realizing state; it does not assert that all raw candidate pivots occur simultaneously.

## Consequence

Rank-one collateral no longer lacks a local executable move or a valid payment map.

- The unique new cell is the pivot.
- All current rank-one triples with that pivot form one private paid bucket.
- A legal rectangle decoder removes the pivot and destroys the whole bucket.
- Scope-complete extraction gives a paid product bank or an explicit AC3fr overload.
- Failure returns a new rank-one, rank-two or rank-three profile at loss `1/(3K)`.
- Immediate rectangle reversal is ticketed by the full rectangle address.

The remaining rank-one work is global no-recycling across successive parent configurations and termination of the explicit overload/same-role stars, not existence of a pivot deletion.

## Finite check

`scripts/verify_ac_rank_one_pivot_decoder.py` normalizes both permutation layers on small grids, exhausts pivot rectangles and all opposite-layer occupancies, verifies every legal repair, arbitrary-layer context-bucket destruction, private pivot assignment, rank-three failed ledgers and reverse-ticket identity.

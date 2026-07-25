# Saturated empty-partner alternative menu

**Branch:** `research/alternating-core-chain`

AC3gr--AC3gu show that a saturated pivot has one fused or split blocker pattern and at least `n-3` empty partner rectangles. Empty rectangles are especially rigid: the opposite layer is unchanged, and different partner choices insert disjoint pairs of cross cells. This note turns those choices into a quantified alternative-target menu. Either one empty partner improves immediately, or the failed alternatives amplify to pairwise disjoint created-certificate buckets and one realized row/column-arm pivot class.

## Setup

Fix a legal parent union `S`, a current pivot

$$
z=(c_0,r_0)
$$

in one permutation layer, and a privately paid pivot bucket of weight `W`. For a same-layer partner

$$
a_c=(c,r_c),
\qquad c\ne c_0,
$$

write

$$
X_c=(c_0,r_c),
\qquad
Y_c=(c,r_0)
$$

for the opposite diagonal. Call `c` an **empty partner** when neither `X_c` nor `Y_c` belongs to the opposite layer.

Let `E_z` be the set of empty partners and put

$$
m=|E_z|.
$$

By AC3gs,

$$
\boxed{
m=n-2\text{ in the fused case},
\qquad
m=n-3\text{ in the split case}.
}
$$

Thus `m>0` for every `n>=4`. The only zero-menu case is the finite `n=3` split pattern.

For `c in E_z`, let `S_c` be the state obtained by switching `z,a_c` to `X_c,Y_c` and leaving the opposite layer unchanged. Let `C_c` be the weighted family of union triples present in `S_c` but not in `S`.

## AC3gv -- exact empty-partner menu and disjoint creation buckets -- PROVED

For every empty partner `c`:

1. `S_c` is a legal pair of disjoint permutation layers;
2. `z` is absent from `S_c`, so the full private pivot bucket of weight `W` is destroyed;
3. the only cells of `S_c\setminus S` are `X_c,Y_c`;
4. every triple in `C_c` contains `X_c` or `Y_c` and has created-cell rank one or two relative to `S`.

For distinct empty partners `c!=d`,

$$
\boxed{
\mathcal C_c\cap\mathcal C_d=\varnothing.
}
$$

### Proof

The active-layer rectangle switch preserves its row and column sets. Empty-partner status says the two inserted cross cells are absent from the opposite layer, so no blocker repair is required and the layers remain disjoint. Removing `z` destroys every privately paid triple in its pivot bucket.

The active switch removes `z,a_c` and inserts exactly `X_c,Y_c`; the opposite layer is unchanged. Hence every newly present triple contains at least one of those two inserted cells and has new-cell rank at most two.

For `c!=d`, the four cells `X_c,Y_c,X_d,Y_d` are distinct. Empty-partner status also makes all four absent from the parent union. State `S_c` contains `X_c,Y_c` but contains neither `X_d` nor `Y_d`, and conversely for `S_d`. A triple newly present in both states would have to contain a new cell from each state's inserted pair, which is impossible. QED.

## AC3gw -- failed empty-menu amplification -- PROVED

Let

$$
C_c=w(\mathcal C_c).
$$

Exactly one of the following holds.

1. Some empty partner satisfies
   $$
   C_c<W,
   $$
   and `S_c` strictly lowers the union-triple potential.
2. Every empty partner is nonimproving, and then
   $$
   \boxed{C_c\ge W\quad(c\in E_z)}
   $$
   and the pairwise disjoint raw creation mass satisfies
   $$
   \boxed{
   \sum_{c\in E_z}C_c\ge mW.
   }
   $$

### Proof

Every state destroys certified weight at least `W`. If its created weight is smaller than `W`, it improves. Otherwise its created weight is at least `W`. Sum over the pairwise disjoint buckets from AC3gv. QED.

## Cross-arm and rank orientation

For every created triple in `C_c`, choose its least new cell under the fixed physical-cell order. The chosen pivot is either `X_c` on the fixed column `c_0`, or `Y_c` on the fixed row `r_0`. Record also whether the triple has created-cell rank one or two.

This partitions the failed empty-menu mass into four classes:

$$
(\text{column arm},1),
\quad
(\text{column arm},2),
\quad
(\text{row arm},1),
\quad
(\text{row arm},2).
$$

## AC3gx -- heavy cross-arm class -- PROVED

Assume no empty partner improves. One of the four arm/rank classes has total raw weight at least

$$
\boxed{
\frac{mW}{4}.
}
$$

For that class, one empty partner state realizes current certificate weight at least

$$
\boxed{
\frac W4.
}
$$

Across different targets in the selected arm, the oriented pivot cells are distinct and lie on one fixed row or one fixed column through `z`.

### Proof

AC3gw gives total raw mass at least `mW`. The four classes partition that mass, so one has at least `mW/4`. Averaging over the `m` target states gives one target with at least `W/4` in that class. The cells `X_c=(c_0,r_c)` have distinct rows as `c` varies because the pivot layer is a permutation, while the cells `Y_c=(c,r_0)` have distinct columns. QED.

## AC3gy -- saturated-menu continuation -- PROVED

Assume `m>0` and no empty partner improves. Fix the target state and arm/rank class from AC3gx. Apply AC3gg--AC3gj to its realized current certificates. For every `K>=1`, one of the following holds.

1. AC3fr returns one explicit role-labelled overload at the selected cross pivot.
2. There is an executable union-safe pivot family with private payment at least
   $$
   \boxed{
   \frac{W}{4K}.
   }
   $$
3. The pivot product fails and returns one next-generation created-cell rank of expected weight at least
   $$
   \boxed{
   \frac{W}{12K}.
   }
   $$

The new pivot address lies on the fixed row or column arm of the original saturated pivot. All original line, source-rank, channel, closure, blocker, denominator, RI and carry decorations remain attached.

### Proof

AC3gx supplies a legal state containing a realized created-certificate class of weight at least `W/4`. AC3gg orients it without loss. AC3gi retains `1/K` of that payment or returns an overload, and AC3gj returns one of three next ranks at a further factor `1/3` if the pivot product fails. QED.

## Consequence

For `n>=4`, full partner saturation cannot remain only a historical recurrence label. Its empty partners form a legal alternative-target menu with pairwise disjoint creation buckets. The output is one of:

- an improving empty rectangle;
- a quantified row- or column-arm pivot continuation;
- an explicit AC3fr overload;
- or a next created-cell rank at scale `W/(12K)`.

The remaining exceptional local case is the `n=3` split saturation pattern, which has two singleton-blocked partners and no empty partner. The remaining global issue is no-recycling of the resulting cross-arm pivots and termination of any same-role overload or affine profile they retain.

## Finite check

`scripts/verify_ac_saturated_empty_menu.py` exhausts normalized disjoint permutation pairs through grid size seven, verifies the exact empty-menu size, all created three-sets, rank at most two, pairwise bucket disjointness, four-way weighted arm/rank localization and the `1/(4K),1/(12K)` composition constants.
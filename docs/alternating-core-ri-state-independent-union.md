# State-independent union support in the closed I6 bank

**Branch:** `research/alternating-core-chain`

AC3cc--AC3cg classify cells fixed in the active layer, while AC3cu--AC3cx classify cells fixed in the repaired blocker layer. A union configuration has one further logical possibility: a cell could be active in some bank states and blocker in the others. This note proves that such layer transfer is possible only in the minimal two-state I6 bank and then forms one exact alternating rectangle.

## Joint-state support

For an I6 active state `eta` and a conditional blocker repair `omega`, write

$$
U_{eta,omega}=D_eta\cup M_{1,eta,omega}.
$$

A cell is **union-fixed** when it belongs to every `U_{eta,omega}`. We ignore cells already present in every unchanged part of the current union, since a triple using only those cells is not new collateral.

## AC3cy -- union-fixed cell trichotomy -- PROVED

Assume the fixed-edge bank is nontrivial, so `mh>=2`, and the full I6 bank of `m!h^m` active states is used. Every new union-fixed cell belongs to one of the following classes.

1. **Active-fixed closure cell.** It is one of the RI5f closure cells classified by AC3cc.
2. **Blocker-fixed closure rectangle.** It is one of the two crossed cells produced by the same pair of blocked closure anchors in every active state, as classified by AC3cv.
3. **Two-state layer-transfer rectangle.** We have
   $$
   \boxed{mh=2,}
   $$
   so the I6 bank has exactly two active states. On the two physical block columns, one state uses one diagonal of an axis-parallel rectangle and the other state uses the opposite diagonal. The current blocker contains one of those diagonals in the state where it is active-blocked, and the unique `t=2` repair inserts the other diagonal. A union-fixed transferred cell lies on that other diagonal.

### Proof

Let `z` be a new union-fixed cell. If `z` is active in every I6 state, AC3cc makes it a closure cell.

Suppose `z` is not active in at least one state `eta`. Since it is union-fixed and not a current blocker cell, it must be a new blocker cell present in every conditional repair of `eta`. AC3cu forces `t_eta=2`, and `z` is one crossed corner of the rectangle determined by the two selected current blocker cells. The cell `z` uniquely determines those two blocker anchors from its column and row.

If `z` is never active, the same two anchors are selected in every active state. AC3cv then makes them fixed closure cells, giving class 2.

It remains that `z` is active in some states and not in others. Let its column be `x`. In every state where `z` is absent from the active layer, the selected blocker anchor in column `x` must instead be active. Thus the active row at `x` has at most two possible values: the row of `z` and the current blocker row in column `x`.

In the full I6 bank, a fixed physical column takes exactly `mh` distinct active rows, one for every target-coset/shift choice. Therefore `mh<=2`. Nontriviality gives `mh=2`. The only possibilities are `(m,h)=(2,1)` or `(1,2)`, and in either case `m!h^m=2`; the physical block has exactly two columns and two target rows. Its two active states are the two perfect matchings of that `2 by 2` block, hence the two rectangle diagonals. The conditional `t=2` blocker repair uses the opposite diagonal. This is class 3. QED.

## AC3cz -- exact two-state rectangle identities -- PROVED

In the layer-transfer case, write the blocker-anchor diagonal as

$$
q_1=(c_1,r_1),
\qquad
q_2=(c_2,r_2),
$$

and the transferred diagonal as

$$
z_{12}=(c_1,r_2),
\qquad
z_{21}=(c_2,r_1).
$$

Then

$$
\boxed{z_{12}+z_{21}=q_1+q_2}
$$

coordinatewise. The two I6 active states alternate between the two diagonals, while the blocker repair alternates oppositely, so all four rectangle corners belong to every union state.

If the transferred cells are I6 channel cells with product parameters `lambda_12` and `lambda_21`, their products satisfy

$$
\boxed{
(c_1r_2)(c_2r_1)=(c_1r_1)(c_2r_2).
}
$$

Thus the product of the transferred-channel parameters equals the product of the blocker-anchor products.

### Proof

The coordinate identity is the rectangle identity. The product identity is obtained by multiplying the four coordinates and regrouping. QED.

## State-independent triple support

A fixed geometric triple present in every union state but absent from the current configuration must contain at least one new union-fixed cell. Otherwise all three of its cells were already present currently, so the triple was not newly created.

## AC3da -- total state-independent collateral router -- PROVED

For the no-three-in-line triple potential, every new state-independent collateral triple contains at least one of:

1. an RI5f closure cell;
2. a crossed cell from one universal two-closure blocker rectangle;
3. a cell from one `mh=2` layer-transfer rectangle.

Consequently the entire state-independent term has an exact geometric decomposition

$$
\boxed{
F=F_{closure}+F_{closure\text{-}cross}+F_{transfer},
}
$$

up to contributions already present in the current configuration, which are not new collateral.

Each term enters an existing finite router.

- `F_closure` enters AC3cc--AC3cg.
- `F_closure-cross` enters AC3cw--AC3cx.
- `F_transfer` is supported on one exact two-state rectangle. Split by one or two transferred cells; direction/offset concentration gives a fixed-centre line star or the exact transferred-pair secant.

For any finite arithmetic profile alphabet of size `L`, one support-type/profile class carries at least

$$
\boxed{F/(3L).}
$$

### Proof

Apply AC3cy to a new cell of every state-independent new triple. The three support types partition the term. Weighted pigeonhole gives the profile bound, and the listed routers apply by construction. QED.

## Consequence

There is no residual diffuse `F_rest` for the geometric triple potential. State-independent collateral is fully supported on closure cells or on one of two exact rectangle mechanisms. The remaining work is payment/termination of those explicit closure and rectangle profiles, not further classification of an unspecified fixed term.

## Finite check

`scripts/verify_ac_ri_state_independent_union.py` enumerates small full I6 banks and blocker permutations, computes every conditional repaired union, and verifies that new common union cells are closure cells, universal closure-crossed cells, or cells of an `mh=2` two-state alternating rectangle.
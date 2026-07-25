# State-independent active collateral from RI completion closure

**Branch:** `research/alternating-core-chain`

AC3bh moves every state-independent collateral contribution into `F`. This note isolates the active-layer part. In a nontrivial closed I6 bank, no cell of the physical source block is common to all bank states. Therefore every new state-independent active triple must use the fixed RI5f boundary-closure matching.

## Setup

Let `X` be the physical I6 source block, let `Y` be the outside endpoint columns of the RI5f boundary paths, and let

$$
Q=\{q_P=(y_P,M_0(v_P)):P\text{ a boundary path}\}
$$

be the closure cells. The cells of `Q` have distinct columns and distinct rows. Every closed I6 active state equals one I6 matching on `X`, the fixed closure matching `Q` on `Y`, and the current active matching outside `X\cup Y`.

Write

$$
F=F_{\rm act}+F_{\rm rest},
$$

where `F_act` is the total weight of new active-layer triples present in every closed I6 state, and `F_rest` contains the remaining state-independent terms, including any blocker-layer contribution.

## AC3cc -- state-independent active support theorem -- PROVED

Assume the paid comparison has positive residual margin

$$
\left(1-\frac1{mh}\right)W-F>0.
$$

Then `mh>=2`. No cell in a column of `X` belongs to every I6 state. Consequently, every new active-layer triple counted by `F_act` contains at least one closure cell from `Q`.

### Proof

If `mh=1`, the paid-destruction coefficient is zero, so the displayed positive margin is impossible. Thus `mh>=2`.

For a fixed column in `X`, an I6 state chooses one of `m` target cosets and one of `h` shifts. Every compatible prescribed cell has probability `1/(mh)<1`; an incompatible cell has probability zero. Hence no cell over `X` is common to all bank states.

Outside `X\cup Y`, the active matching is unchanged. On `Y`, the only active cells in every closed state are the closure cells `Q`. A triple using only unchanged outside cells was already present in the current active layer and is not new collateral. Therefore every new state-independent active triple contains a closure cell. QED.

## AC3cd -- exact closure-count split -- PROVED

For `j=1,2,3`, let `F_j` be the total weight of state-independent active triples containing exactly `j` closure cells. Then

$$
\boxed{
F_{\rm act}=F_1+F_2+F_3.
}
$$

If `F_act>=D`, one closure-count class has weight at least `D/3`.

### Proof

AC3cc gives at least one closure cell, and a triple has at most three cells. The three classes partition the active contribution. QED.

## AC3ce -- heavy closure path or boundary-path spread -- PROVED

For a closure cell `q in Q`, define its active closure load

$$
L(q)=\sum_{T\ni q}w(T),
$$

where the sum runs over state-independent new active triples. If `b=|Q|` is the number of boundary paths, then

$$
\sum_{q\in Q}L(q)
=F_1+2F_2+3F_3
\ge F_{\rm act}.
$$

Consequently:

1. one boundary path has closure-cell load at least
   $$
   \boxed{F_{\rm act}/b};
   $$
2. for every cap `beta>0`, either one closure cell has load greater than `beta`, or
   $$
   \boxed{b\ge F_{\rm act}/\beta}.
   $$

In the second outcome the closure cells form a row-column-disjoint physical matching of the displayed size.

### Proof

The incidence identity counts every triple once for each of its closure cells. Average over `b` closure cells. If every load is at most `beta`, the same identity gives `F_act<=b beta`. QED.

## AC3cf -- finite closure geometry -- PROVED

Every closure-count class has an exact geometric address.

1. **One closure cell.** A triple has one closure cell `q` and two unchanged current context cells. Its exact line passes through `q`; record its primitive direction and the context pair. For one fixed `q`, direction concentration returns many directions or one heavy exact line through `q`.
2. **Two closure cells.** The closure pair determines one exact secant line. The third cell is an unchanged current context cell on that line. Record the unordered closure pair, primitive line direction, and context cell.
3. **Three closure cells.** The collateral object is one exact collinear triple of the closure matching `Q`.

For any finite profile alphabet of size `L`, one closure-count/profile class carries weight at least

$$
\boxed{
F_{\rm act}/(3L).
}
$$

### Proof

The geometric descriptions are immediate from the closure count and collinearity. The profile fibres partition one of the three classes selected by AC3cd. QED.

## AC3cg -- active fixed-term router -- PROVED

If the state-independent active term is heavy, it returns one of the following explicit outputs:

1. one heavily loaded RI5f boundary path and its closure-cell context star;
2. many row-column-disjoint boundary closures;
3. a heavy exact line through one closure cell;
4. a heavy closure-pair secant with current-context incidence;
5. a heavy exact collinear triple of closure cells;
6. one finite closure-count/arithmetic profile of weight at least `F_act/(3L)`.

Every output retains the complete boundary-path provenance: the first selected column, outside endpoint column, released current row, closure cell, path length, physical scale, quotient labels, and carry decorations.

This classifies the active portion of `F`. The residual fixed-term frontier is `F_rest`, especially any blocker-layer contribution, together with termination of the explicit closure-star/secant/triple outputs.

## Finite check

`scripts/verify_ac_ri_closure_collateral.py` exhausts small cyclic I6 banks to verify that their common block support is empty when `mh>=2`. It also exhausts small closure-count weight systems, checks the incidence identity, the heavy-path/spread bounds, and the three-way profile loss.
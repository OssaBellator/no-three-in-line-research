# State-independent blocker collateral in the closed I6 bank

**Branch:** `research/alternating-core-chain`

AC3cc--AC3cg classify the active-layer part of the state-independent term `F`. This note classifies the part created by conditional blocker repair. The result is rigid: a new blocker cell is common to every conditional repair only in the unique two-blocker transposition, and such a cell can be common to the whole I6 bank only when the two blocked desired cells are fixed RI5f closure cells.

## Conditional common blocker support

Fix one closed I6 active state `eta`. Let

$$
Q_eta=D_eta\cap M_1,
\qquad
t_eta=|Q_eta|,
$$

and let `Omega(eta)` be the RI5h--RI5m blocker-repair menu. Write

$$
I_eta=\bigcap_{omega\in Omega(eta)} M_{1,eta,omega}
$$

for the cells present in every repaired blocker matching conditional on `eta`. A cell is **new** when it is not in the current blocker matching `M_1`.

## AC3cu -- conditional common-cell classification -- PROVED

Assume the blocker permutation has size `n>=3`.

1. If `t_eta=0`, then `I_eta=M_1`; there is no new common cell.
2. If `t_eta=1`, the full auxiliary-transposition menu has no new common cell.
3. If `t_eta>=3`, the all-derangements menu has no new common cell.
4. If `t_eta=2`, write
   $$
   Q_eta=\{q_1=(c_1,r_1),q_2=(c_2,r_2)\}.
   $$
   The derangement is unique and the new common cells are exactly
   $$
   \boxed{
   z_{12}=(c_1,r_2),
   \qquad
   z_{21}=(c_2,r_1).
   }
   $$

### Proof

The cases `t=0` and `t=2` are immediate. For `t=1`, every auxiliary blocker cell gives a different transposition. A new crossed cell in column `c_1` has the auxiliary row and therefore varies with the auxiliary choice; the other crossed cell has the auxiliary column and also varies. Since `n>=3`, at least two auxiliaries are available, so no new cell belongs to every menu state.

For `t>=3`, a proposed new cell is one prescribed off-diagonal arc `i->j` in the derangement. There is a derangement avoiding this arc. For `t=3`, use the other directed 3-cycle. For `t>=4`, choose a cyclic derangement after ordering the vertices so that `j` is not the successor of `i`. Hence no replacement arc is present in every derangement. QED.

## AC3cv -- global universal-pair rigidity -- PROVED

Assume the closed I6 bank is nontrivial, so `mh>=2`. If one new blocker cell belongs to every joint active/blocker state, then all of the following hold.

1. Every active state has blocker occupancy exactly two.
2. The same unordered pair of blocker cells is selected in every active state.
3. Both selected desired cells are fixed RI5f closure cells.
4. The common new blocker support is the crossed diagonal of their exact axis-parallel rectangle.

### Proof

AC3cu forces `t_eta=2` in every active state. A new crossed cell `z=(c_i,r_j)` determines its two current blocker anchors uniquely: the current blocker cell in column `c_i` and the current blocker cell in row `r_j`. Therefore the selected pair is independent of `eta`.

A desired cell selected for every `eta` lies in the intersection of all closed active states. AC3cc proves that no cell over the I6 source block `X` is common when `mh>=2`. Outside the selected support the two current permutation layers are disjoint, so no blocker cell there is a desired active cell. The only remaining common desired cells are the fixed RI5f closure matching `Q`. Thus both anchors are closure cells. AC3cp supplies the crossed rectangle. QED.

## Fixed blocker term

Let `F_blk` be the total weight of new collateral triples which are present in every joint state and contain at least one blocker cell created by the conditional repair. Contributions already present in the current configuration are excluded.

## AC3cw -- exact fixed-blocker support -- PROVED

Either

$$
\boxed{F_blk=0,}
$$

or there are exactly two fixed blocked closure cells

$$
q_1=(c_1,r_1),
\qquad
q_2=(c_2,r_2),
$$

such that every active state has blocker intersection `{q_1,q_2}` and every triple counted by `F_blk` contains one or both crossed cells

$$
z_{12}=(c_1,r_2),
\qquad
z_{21}=(c_2,r_1).
$$

The two crossed cells satisfy

$$
\boxed{z_{12}+z_{21}=q_1+q_2}
$$

coordinatewise and retain the full boundary-path provenance of both closure anchors.

### Proof

A triple counted by `F_blk` contains a new blocker cell common to every joint state. Apply AC3cv. The coordinate identity is AC3cp. QED.

## AC3cx -- fixed-blocker geometric router -- PROVED

Assume `F_blk>0`. Split its triples by the number `k` of crossed cells they contain.

$$
k\in\{1,2\}.
$$

One value of `k` carries weight at least `F_blk/2`.

1. **One crossed cell.** One of `z_12,z_21` has context-star load at least `F_blk/4`. Every triple has that crossed cell and two fixed current-context cells. Direction/offset concentration returns many directions, many parallel offsets, or one heavy exact line through the crossed cell.
2. **Two crossed cells.** The crossed pair determines one exact secant line, and the third cell is a fixed current-context cell on that line. This class has weight at least `F_blk/2` when selected.

For any finite arithmetic profile alphabet of size `L`, one exact crossed-count/profile class carries weight at least

$$
\boxed{F_blk/(2L).}
$$

Thus the variable-blocker portion of `F_rest` is either zero or enters the existing closure-pair rectangle/secant and fixed-centre context routers. The only residual state-independent term is the contribution not created by active completion or blocker repair.

### Proof

Every new common blocker cell belongs to the fixed crossed pair from AC3cw, and a triple has at most three cells. Weighted pigeonhole gives the two-way crossed-count split and the profile bound. In the one-cell class, the two crossed cells split the incidence weight, giving `F_blk/4`. The geometric descriptions are immediate. QED.

## Consequence

The state-independent term now has the decomposition

$$
F=F_act+F_blk+F_other,
$$

where `F_act` is classified by AC3cc--AC3cg, `F_blk` is classified above, and `F_other` contains only contributions invariant for reasons unrelated to active completion or conditional blocker movement. In particular, there is no diffuse state-independent blocker-repair loss.

## Finite check

`scripts/verify_ac_ri_fixed_blocker_collateral.py` exhausts small blocker permutations and repair menus, computes their common new cells, verifies the unique `t=2` exception, and checks the global closure-pair and weighted-router conclusions on small nontrivial I6 banks.
# Single-witness matching neutralization and local margin

**Branch:** `research/geometric-cleaning`

GC2dr--GC2dv show that compatible prospective line/cell witnesses execute globally once every exact
witness has a legal local operation and positive expected margin.  This note supplies the local
single-witness calculation.  It uses the same bounded-degree matching family as AN1--AN4, but centres it
on the designated repeated moved cell of a bridge, chord or transversal witness.

The result is exact at the witness level: the designated source is destroyed in every local state,
rank-one through rank-three collateral has the usual falling-factorial spread, and failure of positive
margin localizes to one fixed-switch term or one heavy local rank inventory.

## Local witness model

Fix one exact non-axis bridge, chord or transversal witness `v`.  It has:

- occurrence-faithful current source weight `a_v>0`;
- one designated moved star block of size `t>=7`;
- one designated source cell `z_v` in that block;
- an allowed matching family `Omega_v` with forbidden-position degree at most two;
- the original position of `z_v` forbidden in every matching;
- fixed supporting cells and fixed-switch preparation cost `f_v>=0`.

The current source occurrence contains `z_v`; every other source cell is outside the local moved block
or is fixed by the declared local operation.

Assume the **single-witness matching contract**:

1. every matching in `Omega_v` is a legal balanced local state;
2. changing the position of `z_v` destroys the named current source occurrence;
3. fixed-only new certificates are included in `f_v`;
4. every other new weighted rank-three certificate is listed exactly once and requires `r` matching
   cells from the moved block, for one `r in {1,2,3}`;
5. a compatible prescription of `r` matching cells has probability at most `128/(t)_r`;
6. current/prospective and lineage statuses are occurrence-faithful;
7. failure returns the least exact block, line, cell-role or context field.

Let `T_r(v)` be the total listed prospective weight requiring exactly `r` matching cells, and put

`E_AN(v)=128*[T_1(v)/t+T_2(v)/(t)_2+T_3(v)/(t)_3]`.

## GC2dw -- designated source destruction -- PROVED

Every local matching state destroys the named source occurrence of weight `a_v`.  Consequently the
local destroyed current weight `d_v` satisfies

`d_v>=a_v`.

### Proof

The source contains the designated cell `z_v` in its original position.  That position is forbidden in
every allowed matching, so `z_v` moves in every local state.  The other source cells are fixed and no
other local action restores the same exact occurrence.  Thus the source is absent from every resulting
state. QED.

No weight from another witness is used in this statement.

## GC2dx -- exact local collateral expectation -- PROVED

For a uniformly random matching in `Omega_v`, the expected nonfixed new collateral satisfies

`e_v<=E_AN(v)`.

Hence the expected local potential change obeys

`E[Delta Phi_v]<=f_v-a_v+E_AN(v)`.

### Proof

A listed certificate requiring `r` matching cells appears with probability at most `128/(t)_r` by the
matching contract.  Summing its weighted indicator over the exact list gives the displayed bound for
`e_v`.  Fixed-only terms contribute `f_v`, while GC2dw destroys at least `a_v`. QED.

The list is occurrence-faithful, so aliases are aggregated before the expectation is taken.

## GC2dy -- positive single-witness margin -- PROVED

Define

`m_v=a_v-f_v-E_AN(v)`.

If `m_v>0`, some legal local matching state decreases the cleaning potential by at least `m_v`:

`Delta Phi_v<=-m_v<0`.

More generally, `m_v>=epsilon*a_v` implies one local state decreases the potential by at least
`epsilon*a_v`.

### Proof

GC2dx gives an average at most `-m_v`.  Some state is at most the finite average.  Substitute the
uniform-margin inequality for the second statement. QED.

This is the exact local-margin input required by GC2dt.

## GC2dz -- failed margin rank localization -- PROVED

Suppose no local matching state gives strict descent.  Then one of the following holds:

1. `f_v>=a_v`;
2. one rank `r in {1,2,3}` satisfies

   `128*T_r(v)/(t)_r>=(a_v-f_v)/3`,

   and therefore

   `T_r(v)>=(a_v-f_v)*(t)_r/384`;

3. one field of the single-witness matching contract fails.

### Proof

If all contract fields hold and no state descends, the actual average collateral is at least
`a_v-f_v`.  GC2dx bounds that actual average above by `E_AN(v)`.  If `a_v<=f_v`, alternative 1 holds.
Otherwise `E_AN(v)>=a_v-f_v>0`.  The three nonnegative rank contributions to `E_AN(v)` have sum at
least `a_v-f_v`, so one is at least one third of that amount.  Rearranging gives the inventory bound.
QED.

Thus failure cannot remain an unspecified local collateral cloud.

## GC2ea -- bridge/chord/transversal local router -- PROVED UNDER THE SINGLE-WITNESS MATCHING CONTRACT

Every exact current bridge, chord or transversal line/cell witness with a designated AN matching block
has one continuation:

1. a legal local neutralization with strict cleaning descent;
2. fixed-switch cost at least the named source weight;
3. a rank-one, rank-two or rank-three prospective inventory satisfying the GC2dz lower bound;
4. or one exact legality, certificate-completeness, occurrence or context failure.

For a compatible family `I`, if every witness satisfies

`a_v-f_v-E_AN(v)>=epsilon*a_v`,

then GC2dt gives one product state with total decrease at least

`epsilon*sum_(v in I) a_v`.

Combined with GC2dq, a cross-tuple input of weight `W` gives decrease at least

`epsilon*W/[2*N^2*ell_N*(2D_out+1)]`

outside the axis, block-overload and cause-failure branches.

### Proof

Apply GC2dw--GC2dz to one witness.  For a compatible family, the local operation and complete local
certificate list satisfy the product hypotheses of GC2dr--GC2dt, so the margins add without further
loss.  Substitute the retained-weight bound from GC2dq. QED.

## Corrected GC frontier

The final compatible-family execution problem is reduced to a concrete one-witness matching budget.
For each bridge, chord or transversal, the designated moved-cell operation is explicit and destroys the
named source in every state.  The remaining local obstruction is now one of:

- fixed-switch cost comparable with the source;
- a heavy exact rank-one, rank-two or rank-three prospective inventory;
- failure of the local matching or certificate-completeness contract;
- block-tuple overload, high created-pair multiplicity or an outer context branch.

The next geometric task is to classify or charge the three heavy local rank inventories, rather than to
construct a global product execution law.

## Finite check

`scripts/verify_geometric_single_witness_local_margin.py` enumerates small forbidden-position matching
families, verifies movement of every designated original cell and checks all sampled partial matching
probabilities against `128/(t)_r`.  It then samples weighted local inventories and verifies the strict
margin and failed-margin rank-localization inequalities.

# Cross-tuple regularization of repeated line and cell witnesses

**Branch:** `research/geometric-cleaning`

GC2dh--GC2dl reduce one failed product-collateral block tuple to an axis collision or one exact
non-axis line with repeated moved-cell incidence.  The remaining issue is aggregation across many
different bridge, chord and transversal tuples: a certificate must not pay twice, and simultaneous
installation can fail through shared blocks, line causes, cell causes or an unrecorded global
context.

This note gives one occurrence-faithful aggregate ledger and a conflict-graph router.  After a
uniform geometric loss, either the axis ledger is already heavy, one star block is overloaded, a
bounded line/cell cause pays the incompatibility, or a compatible witness family retains explicit
weight.

## Tuple and witness notation

Let `T` be a finite family of exact cross-star block tuples.  Each exact product certificate belongs
to exactly one tuple and one profile from GC2dc.  Give the certificates normalized expected weights
and let

`W=sum_(tau in T) V_tau`

be the total tuple mass.

For tuple `tau`, split

`V_tau=V_tau^axis+V_tau^non`

as in GC2dh.

In the non-axis part, apply GC2di and then choose one **designated moved role**:

- for a bridge, the least of its two moved star blocks;
- for an oriented chord, its double block;
- for a transversal, the least of its three star blocks.

Inside the designated block, assign each certificate canonically to one moved cell.  For a chord,
which has two moved cells in its double block, use the lexicographically least of those two cells.
Thus each selected certificate contributes exactly one designated moved-cell incidence.

A **witness vertex** records:

1. the exact block tuple;
2. the profile and designated block role;
3. the selected non-axis line;
4. the selected repeated moved cell;
5. for a bridge, the selected fixed `Z` cell;
6. and the exact current/prospective/support role used by the cause ledger.

## GC2dm -- aggregate axis-or-witness ledger -- PROVED

Put

`ell_N=|L_N|<=binom(N^2,2)`.

Either the total axis mass satisfies

`W_axis=sum_tau V_tau^axis>=W/2`,

or the non-axis tuples contain witness vertices of total occurrence-faithful weight `C` satisfying

`C>=W/[2*N^2*ell_N]`.

No exact product certificate is counted in two witness vertices.

### Proof

If the axis inequality fails, then

`W_non=sum_tau V_tau^non>W/2`.

For a bridge tuple, GC2di selects one exact fixed-cell/line class of weight at least

`V_tau^non/(N*ell_N)`.

For a chord or transversal it selects a line class of weight at least

`V_tau^non/ell_N`,

which is at least the same bridge-safe lower bound.  After choosing one designated moved incidence
per certificate, the selected line contains at most `N` candidate moved cells, so one repeated cell
retains at least another `1/N` fraction.

Thus tuple `tau` contributes witness weight at least

`V_tau^non/(N^2*ell_N)`.

The tuple certificate families are disjoint, and the designated-incidence rule assigns each selected
certificate once.  Summing over tuples gives

`C>=W_non/(N^2*ell_N)>W/(2*N^2*ell_N)`. QED.

The chord's two-incidence gain from GC2dj is deliberately not used here; the weaker one-incidence
assignment guarantees exact no-double-counting.

## Conflict causes

Put a graph on the witness vertices.  Join two vertices when their associated witness installations
or chargeback uses are incompatible.

Fix a block threshold `K_B>=1`.  If some star block occurs in more than `K_B` witness tuples, call it
a **block-tuple overload**.

Assume otherwise that every conflict edge has a canonical orientation toward one of its endpoints'
declared causes.  For a vertex `v`, an outgoing edge must be certified by one of:

1. a star block in its tuple;
2. its exact non-axis line atom;
3. its exact repeated moved-cell role.

Let `Delta_L` be the maximum number of witness occurrences chargeable to one exact line cause and
`Delta_C` the corresponding maximum for one exact cell-role cause.  Under GC3j--GC3l one may use

`Delta_L=2t`

for a non-axis line and the exact rectangle-role value

`Delta_C=rho_max`

for the repeated cells.

Any incompatibility not admitting one of these labels is returned as a global-context or
contract-failure witness.

## GC2dn -- bounded oriented conflict load -- PROVED

If no block-tuple overload occurs, every witness vertex has outgoing conflict degree at most

`D_out=3*(K_B-1)+(Delta_L-1)+(Delta_C-1)`.

### Proof

A cross-star tuple contains at most three star blocks.  For each of them there are at most `K_B-1`
other witness vertices containing that block.  The vertex's line cause reaches at most
`Delta_L-1` other witness occurrences, and its cell-role cause reaches at most `Delta_C-1`.
Summing these safe bounds gives `D_out`.  Multiple labels on one edge only reduce the union count.
QED.

## GC2do -- finite degeneracy and weighted compatible extraction -- PROVED

The undirected witness conflict graph is `2D_out`-degenerate and therefore colourable with at most

`2D_out+1`

colours.

Consequently it has a compatible witness family of total weight at least

`C/(2D_out+1)`.

### Proof

Restrict the canonical edge orientation to any induced subgraph.  Every remaining vertex still has
outdegree at most `D_out`, so the subgraph has at most `D_out` times its vertex count in directed
edges.  Its average undirected degree is therefore at most `2D_out`, and it has a vertex of degree at
most `2D_out`.  Repeated deletion gives `2D_out`-degeneracy and a greedy
`2D_out+1` colouring.

The colour classes are compatible and their weights sum to `C`, so a heaviest class has at least the
displayed fraction. QED.

## GC2dp -- occurrence-faithful payment and installation interface -- PROVED AS AN INTERFACE

The compatible family from GC2do retains distinct exact certificate occurrences.  Therefore:

1. if the line/cell causes are current paid causes, their selected weights may be charged without
   certificate reuse;
2. if the witnesses are prospective installation objects, the compatible colour class is a valid
   simultaneous-installation candidate under the declared product legality contract;
3. if a witness changes from prospective to current, that transition must be recorded by the
   existing lineage or occurrence gate;
4. if an incompatibility uses a cause outside the tuple blocks, selected line or selected cell role,
   its least exact global-context field is returned rather than silently charged.

### Proof

GC2dm partitions exact certificate occurrences by tuple and uses one designated incidence per
selected certificate.  GC2do only discards vertices; it never duplicates their occurrence sets.
The four conclusions are exactly the current/prospective and occurrence-faithfulness contracts
already used in GC2ch--GC2cw and GC3g--GC3n. QED.

## GC2dq -- cross-tuple line/cell router -- PROVED UNDER THE CAUSE-COMPLETE CONTRACT

For total cross-star tuple mass `W>0` and block threshold `K_B`, at least one of the following holds:

1. an axis row/column collision carries mass at least `W/2`;
2. one star block occurs in more than `K_B` selected witness tuples;
3. a named line, cell-role, current/support or global-context cause violates the declared bounded
   cause contract;
4. a compatible witness family retains weight at least

   `W/[2*N^2*ell_N*(2D_out+1)]`,

   where

   `D_out=3*(K_B-1)+(Delta_L-1)+(Delta_C-1)`.

Under the current-paid version of the contract, alternative 4 is a no-double-counting chargeback
family.  Under the prospective version, it is a simultaneous installation family.

### Proof

Apply GC2dm.  In the non-axis branch, test the block threshold and cause-completeness hypotheses.  If
they hold, use GC2dn and GC2do, then substitute the lower bound for `C`.  GC2dp supplies the
payment/installation interpretation. QED.

## Corrected GC frontier

Cross-star product collateral is no longer only a collection of unrelated line/cell witnesses.
Across all block tuples it now yields:

- heavy axis collision mass;
- an exact high block-tuple incidence;
- a bounded line/cell cause payment;
- a compatible occurrence-faithful witness family with explicit weight;
- or one least global-context/contract failure.

The remaining work is to execute the compatible prospective family in the complete cleaning move,
feed block-tuple overloads into labelled GC4 recursion, and handle identity-sensitive or unbounded
lineage recycling and high created-pair multiplicity.

## Finite check

`scripts/verify_geometric_cross_tuple_line_cell_regularization.py` samples weighted tuple systems and
oriented cause graphs.  It checks the uniform `1/(N^2 ell_N)` witness extraction, exact tuple
no-double-counting, the outgoing cause bound, `2D_out` degeneracy and the weighted
`1/(2D_out+1)` compatible extraction.

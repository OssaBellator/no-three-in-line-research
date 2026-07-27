# Involutive reversal of composed-only swap outputs

**Branch:** `research/sparse-algebraic-spread`

SAS5gg--SAS5gk return a large composed-only output bank with conjunction table `(0,0,0,1)`. This note records an exact involution that prevents the same operation square from recycling that bank as composed-only again: after the composed move becomes the new base state, the table reverses to current-only `(1,0,0,0)`.

## Two commuting swaps

Let `gamma` and `delta` be disjoint balanced column swaps, so they commute and are involutions. For a record `Q`, write its occurrence table relative to base state `S` as

\[
t_S(Q)=
(x_{00},x_{10},x_{01},x_{11}),
\]

where the four entries are the indicators in

\[
S,\quad \gamma S,\quad \delta S,\quad \gamma\delta S.
\]

Let the composed state `S'=gamma delta S` become the new base, retaining the same unordered operation square.

## SAS5gl -- exact table-reversal involution -- PROVED

\[
\boxed{
t_{S'}(Q)=
(x_{11},x_{01},x_{10},x_{00}).
}
\]

Applying the transformation twice returns the original table.

### Proof

From base `S'`, the four square states are

\[
S'=\gamma\delta S,
\qquad
\gamma S'=\delta S,
\qquad
\delta S'=\gamma S,
\qquad
\gamma\delta S'=S,
\]

using commutativity and involutivity. Reading the old indicators in that order gives the displayed reversal. QED.

## SAS5gm -- composed-only becomes current-only -- PROVED

The two positive-curvature tables are exchanged:

\[
\boxed{
(0,0,0,1)\longleftrightarrow(1,0,0,0).
}
\]

Hence every record in a composed-only output bank is an exact current-only record relative to the installed composed state and the reverse operation square. It is destroyed by either constituent reverse swap and by their composition.

### Proof

Substitute the two tables into SAS5gl. QED.

## SAS5gn -- lossless weighted-bank reversal -- PROVED

Let `P_comp` be any alias-aggregated weighted composed-only bank assigned to an interaction-independent family of operation squares. After installing every composed move, the same total weight `P_comp` is a current-only payment bank for the reverse squares. No signature split, incidence loss or new arithmetic classification is needed.

### Proof

SAS5gm applies record by record. Table reversal does not change record identity, weight or its assigned square. Alias aggregation is therefore preserved and the full weight transfers. QED.

## SAS5go -- corrected recycling router -- PROVED

After a composed-only bank is installed, one of the following must occur before that mass can be returned as composed-only output again.

1. The same exact operation square is used: the bank is current-only payment by SAS5gn, not composed-only output.
2. At least one operation-square field changes: an endpoint column, label pair, row-shape/record address, boundary role or base-state signature changes.
3. A legality or interaction-independence contract fails and is returned as a named obstruction.

Thus immediate same-square composed-only recycling is impossible. Any longer recycling trajectory must move through the already finite exact square/profile address dictionary and may be handled by new-address tickets or an exact profile cycle.

### Proof

Outcome 1 is SAS5gn. If the table is again composed-only but the same square is not being interpreted in reverse, some field determining the square or its record assignment has changed, giving outcome 2. If the square cannot be retained because a declared hypothesis fails, return outcome 3. QED.

## Consequence for SAS6

The composed-only branch of SAS5gk is no longer a self-loop. Its output is immediate current payment for the reverse square, or it forces an exact operation signature change. Remaining work is global payment of opposite-swap barriers, legality of the relevant square families, and termination or payment of the finite signature-change cycles.

## Finite check

`scripts/verify_sparse_composed_only_reversal.py` exhausts all sixteen Boolean conjunction tables, verifies the reversal involution, and checks it on explicit balanced states under two disjoint commuting swaps.

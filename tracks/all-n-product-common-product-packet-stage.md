# All-n product track: common-product packet stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-support-four-stage.md`](all-n-product-support-four-stage.md).
PX207--PX209 pay support-four collateral on blocks above the ambient
`N^(2/3+epsilon)` scale.  PX210--PX212 now decode and release large support-four
mass in the remaining range.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Support-four product normal form | **COMPLETE** | PX210 identifies support-four pairs through one anchor with vertex-disjoint pairs of arcs on one equal-product level. |
| Heavy packet extraction | **COMPLETE** | PX211 converts anchor-weighted support-four mass into a quantitative common-anchor/common-product packet. |
| Packet transposition release | **COMPLETE** | PX212 gives a constant-density, fixed-rank-spread matching bank avoiding all forbidden cells and every packet-certified two-cycle. |
| External packet collateral | **OPEN** | The release bank may create certificates through other anchors and product levels. |
| Rank-one and rank-three sectors | **OPEN** | Their scale-sensitive constants are not yet fully paid by destroyed mass. |
| Absolute recursion depth | **OPEN** | No theorem yet proves that packet release plus the earlier decoders terminates in bounded depth. |
| Infinite exact closure | **OPEN** | No exact all-side doubling theorem follows yet. |

## 1. Exact packet decoder

For one anchor `z=(a,b)`, define

\[
A_i=x_i-a,
\qquad
B_j=y_j-b.
\]

At product level `p`, form the directed packet

\[
\mathcal P_z(p)
=
\{i\to\ell:i\ne\ell,\ A_iB_\ell=p\}.
\]

PX210 proves that support-four pairs through `z` are exactly the
vertex-disjoint arc pairs inside these packets.  If `Q_z^(4)` is their number,
PX211 extracts one vertex-disjoint packet of order at least

\[
\frac{2Q_z^{(4)}}{3t^2}.
\]

Globally, if `W_(2,4)` is the anchor-weighted support-four load, some packet has
order at least

\[
\frac{2W_{2,4}}{3|Z|t^2}.
\]

Thus cubic-per-anchor support-four mass forces a linear packet.

## 2. Packet collisions are two-cycles

Relabel a vertex-disjoint packet of order `h` so its base row-column
correspondence is the identity.  A matching in the packet subgrid is a
permutation `pi in S_h`.

For two packet indices `r,s`, the cross pair certified by the common product
level is selected exactly when

\[
\pi(r)=s,
\qquad
\pi(s)=r.
\]

Therefore the complete packet-certified collision family is exactly the set of
two-cycles of `pi`.

## 3. Constant-spread release bank

Let the inherited forbidden graph have maximum row and column degree `Delta`.
PX212 combines forbidden singleton events with permutation two-cycle events in
one canonical lopsided local lemma.

If

\[
h\ge\max(32,32\Delta),
\]

then at least

\[
e^{-4\Delta-4}h!
\]

packet permutations avoid every forbidden cell and every two-cycle.  The
uniform release measure satisfies

\[
\Pr(E\subseteq M)
\le
\frac{e^{4\Delta+4}}{(h)_{|E|}}.
\]

Thus a large common-product packet can be neutralized without losing the
fixed-rank spread needed for collateral accounting.

## 4. Updated proof tasks

1. **External packet collateral.** Bound one-, two-, and three-cell certificates
   created by the PX212 release bank outside the extracted anchor/product level.
2. **Destroyed-mass accounting.** Quantify how many old support-four collisions
   the packet release removes relative to its external expected load.
3. **Overlapping packets.** Extract edge-disjoint or low-overlap packets from
   several heavy anchors and release them in one batch.
4. **Small packet absorption.** Handle extracted packets below
   `max(32,32Delta)` by finite enumeration or bounded composite trades.
5. **Rank-one support two.** Prove the analogous anchor/product reduction for
   one-replacement/two-background certificates.
6. **Rank-three short cycles.** Release the directed three-cycle core while
   preserving bounded-forbidden spread.
7. **Depth-two theorem.** Combine packet release with PX190, PX194, and PX204 to
   show strict net improvement after at most two generations.
8. **Closure conversion.** Install the terminating decoder in the universal
   low-syndrome product seed PX63.

The immediate frontier is item 1: calculate the exact collateral profile of the
no-two-cycle release measure.  The formerly diffuse support-four obstruction is
now an executable packet bank.

## 5. Verification

```bash
python scripts/verify_product_common_product_packet.py
```

The verifier checks the packet identity and extraction inequality on random
integer grids, exact small-order released-family counts, the mixed-rank LLL
inequalities, and the equivalence between packet-certified collisions and
permutation two-cycles.

The classical no-three-in-line conjecture and infinite product closure remain
open.
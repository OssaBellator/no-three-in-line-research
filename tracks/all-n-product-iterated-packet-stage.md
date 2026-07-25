# All-n product track: iterated product-packet release stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-conditioned-packet-release-stage.md`](all-n-product-conditioned-packet-release-stage.md).
PX210--PX214 extract and release one common-product packet with conditioned
fixed-rank spread. PX215--PX218 now iterate that mechanism: distinct product
levels overlap in at most two cells, residual support-four mass extracts another
level, and any fixed packet family admits one simultaneous release measure.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| One-packet release | **COMPLETE** | PX212--PX214 give existence, spread, conditioning, and external-load transfer. |
| Product-level overlap | **COMPLETE** | PX215 proves that two distinct anchor-product packets share at most two candidate cells. |
| Second-packet extraction | **COMPLETE** | PX216 converts every positive residual support-four mass into a new product level, quantitatively. |
| Fixed packet packing | **COMPLETE** | PX217 releases any `k` packets jointly when `h>=32 max(1,Delta,k)`. |
| Conditioned packet packing | **COMPLETE** | PX218 shows that exposure adds one complementary partial matching per packet and gives conditioned spread. |
| Packet-certified support four | **ELIMINATED EXACTLY** | Every cross event certified by every released packet has probability zero. |
| Absolute packet count | **OPEN** | No theorem yet proves that an absolute number of extracted packets pays all external rank-two mass. |
| External rank one and rank three | **OPEN** | Their geometric weights are not yet fully below the destroyed-mass scale. |
| Infinite exact closure | **OPEN** | No terminating all-side doubling theorem follows yet. |

## 1. Product levels form a sparse algebraic family

For anchor `z=(a,b)` and nonzero product `p`, the packet is

\[
\mathcal P_z(p)
=
\{i\to j:(x_i-a)(y_j-b)=p\}.
\]

Each packet is a partial matching. PX215 subtracts two rectangular-hyperbola
equations and obtains a line. Therefore distinct product levels have intersection
at most two.

This gives an exact low-overlap statement for every packet extracted in later
generations; it does not rely on randomness or generic coordinates.

## 2. Residual support-four decoder

Let `S` be the levels already included in the release measure and let
`W_(2,4)^res` be the remaining anchor-weighted support-four mass. PX216 gives a
new level of size at least

\[
\frac{2W_{2,4}^{\rm res}}{|Z|h^2}.
\]

In particular,

\[
W_{2,4}^{\rm res}
\ge
\eta |Z|h^3
\]

forces another packet with at least `2 eta h` arcs. Thus large residual rank-two
mass cannot stay diffuse across anchors and product values.

## 3. Joint release measure

For `k` packet partial matchings, include one canonical rank-two bad event for
every packet-certified cross. Together with the inherited forbidden cells, the
canonical permutation conflict graph has:

- singleton-to-packet dependency at most `2k(h-1)`;
- packet-to-packet dependency at most `4k(h-1)`;
- packet-to-singleton dependency at most `4Delta`.

PX217 uses witnesses

\[
x_1=\frac2h,
\qquad
x_2=\frac4{h^2}
\]

and proves density at least

\[
e^{-4\Delta-4k}.
\]

The uniform joint-release measure has cylinder bound

\[
\Pr(E\subseteq M)
\le
\frac{e^{4\Delta+4k}}{(h)_{|E|}}.
\]

The result applies to the complete product-level packet, not only to one
vertex-disjoint matching extracted from that level.

## 4. Sequential exposure

For one packet, an exposed edge has at most one complementary edge which would
finish a packet-certified cross. Over an arbitrary partial exposure, these
complementary positions form one partial matching.

For `k` packets, the union has degree at most `k`. PX218 therefore replaces
`Delta` by `Delta+k`, independently of the exposure rank. In residual order `n`,
conditioned cylinders satisfy

\[
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\le
\frac{e^{4\Delta+8k}}{(n)_{|E_1|}}.
\]

Thus fixed packet packing remains compatible with the sequential certificate
accounting developed in PX198--PX214.

## 5. Remaining proof tasks

1. **Absolute packet-count theorem.** Show that after a bounded number of greedy
   packet extractions, the residual support-four load falls below the PX214
   improvement threshold.
2. **Packet-energy potential.** Find a potential on anchor-product levels which
   decreases whenever a new packet is added to the release family.
3. **Many-packet constant control.** Improve the `e^(4k)` spread loss, or prove
   that only bounded `k` is ever required.
4. **External rank-one geometry.** Bound one release cell plus two background
   points on the packet subgrid.
5. **External rank-three geometry.** Combine PX189 with the joint-release cylinder
   law to pay all-candidate packet-subgrid triples with usable constants.
6. **Destroyed old mass.** Relate packet-certified candidate energy to defects
   present in the current selected state.
7. **Depth-two accounting.** Combine the packet family with loaded-line and clean-
   star recursion and prove strict net descent.
8. **Closure conversion.** Insert the terminating decoder into PX63.

The immediate frontier is item 1 or item 2. The second-packet extraction and the
probability theory for every fixed packet family are no longer missing inputs.

## 6. Verification

```bash
python scripts/verify_product_iterated_packet_release.py
```

The verifier checks product-level intersections, the residual extraction
inequalities, exact joint packet-cross avoidance at order eight, all symbolic
`k`-packet local-lemma inequalities, the density estimate, and the conditioned
one-partial-matching-per-packet structure.

The classical no-three-in-line conjecture and infinite product closure remain
open.

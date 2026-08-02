# All-n product track: iterated product-packet release stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-conditioned-packet-release-stage.md`](all-n-product-conditioned-packet-release-stage.md).
PX210--PX218 provide iterated packet extraction and joint release. PX219--PX220
pay internal rank-three collateral after packet-compatible thinning. PX221
refutes bounded termination for unrestricted candidate energy, PX222 preserves a
logarithmic packet window, and PX223--PX224 recover logarithmic concentration for
**old selected defects**.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| One-packet release | **COMPLETE** | PX212--PX214 give existence, spread, conditioning, and external-load transfer. |
| Product-level overlap | **COMPLETE** | PX215 proves that distinct anchor-product packets share at most two candidate cells. |
| Second-packet extraction | **COMPLETE** | PX216 converts every positive residual support-four mass into a new product level. |
| Fixed packet packing | **COMPLETE** | PX217 releases any fixed packet family jointly. |
| Conditioned packet packing | **COMPLETE** | PX218 adds one complementary partial matching per packet under exposure. |
| Internal packet rank three | **CONTROLLED** | PX219--PX220 give linear expected internal rank-three collateral on a square-root packet restriction. |
| Absolute candidate packet count | **REFUTED** | PX221 gives geometric-progression grids requiring `Omega(h)` product levels. |
| Logarithmic packet window | **PROVED** | PX222 gives polynomial spread for `O(log h)` released packets. |
| Selected packet-cross structure | **COMPLETE** | PX223 proves that old selected crosses in one level are disjoint transpositions. |
| Heavy old-defect levels | **CONTROLLED** | PX224 gives only `O(log h)` linearly heavy levels in an `O(h log h)` low-syndrome block. |
| Diffuse old-defect levels | **OPEN / ACTIVE FRONTIER** | Every remaining level has sublinear old load, but no descent theorem yet exploits that dispersion. |
| External rank one | **OPEN** | One release cell plus two background points is not yet below the destroyed-mass scale. |
| Infinite exact closure | **OPEN** | No terminating all-side doubling theorem follows yet. |

## 1. Joint product-packet release

For anchor `z=(a,b)` and nonzero product `p`, put

\[
\mathcal P_z(p)
=
\{i\to j:(x_i-a)(y_j-b)=p\}.
\]

PX215 proves two distinct levels intersect in at most two cells. PX216 shows that
residual support-four mass `W_(2,4)^res` extracts a new level of size at least

\[
\frac{2W_{2,4}^{\rm res}}{|Z|h^2}.
\]

PX217 releases `k` packets jointly with density at least

\[
e^{-4\Delta-4k}
\]

and cylinder constant `e^(4Delta+4k)`. PX218 gives conditioned constant
`e^(4Delta+8k)` because each packet contributes one complementary partial
matching after exposure.

## 2. Internal rank-three control

PX219 retains a designated packet subset of order

\[
s\ge\frac12\sqrt h
\]

whose complete candidate subgrid has `O(s^4)` internal triples. PX220 then gives

\[
\mathbb E\Phi_{3,\rm int}
=
O\!\left(e^{4\Delta+4k}s\right),
\]

while every one of the designated packet's `binom(s,2)` cross events has
probability zero.

## 3. Candidate-energy barrier

For geometric-progression packet coordinates, PX221 computes total candidate
packet energy

\[
\frac{h(h-1)(2h-1)}6.
\]

One level removes at most `binom(h,2)`, so reducing the energy by half requires
at least `(2h-1)/6` levels. Therefore bounded packet termination is false for
unrestricted candidate energy.

PX222 nevertheless shows that `k<=kappa log h` costs only polynomial spread:
`h^(4kappa)` before conditioning and `h^(8kappa)` afterward. Support-excess
sectors can still overcome this loss when their power saving is large enough.

## 4. Selected-defect packet decomposition

For the current matching `M`, let `d_alpha(M)` count old selected crosses from
product level `alpha`. PX223 proves that these crosses form disjoint
transpositions on the packet arcs, so

\[
d_\alpha(M)
\le
\frac h2.
\]

Moreover,

\[
D_{2,4}(M)
=
\sum_\alpha d_\alpha(M)
\]

with anchor multiplicity.

For threshold `tau`, PX224 gives

\[
\#\{\alpha:d_\alpha(M)\ge\tau\}
\le
\frac{D_{2,4}(M)}\tau.
\]

Thus if `D_(2,4)(M)<=C h log h` and `tau=eta h`, only

\[
\frac C\eta\log h
\]

levels are heavy. All can be included in one logarithmic packet release, and all
old defects carried by them disappear exactly.

## 5. Active diffuse frontier

After releasing every linearly heavy selected-defect level, each remaining level
has load below `eta h`. The next theorem must use this dispersion rather than
extract another candidate-heavy packet blindly.

Viable targets are:

1. **Diffuse averaging.** Prove that many low-load product levels give an average
   packet move with negative expected collateral.
2. **Cross-level decoder.** Show that diffuse levels sharing many endpoints or
   anchors force a loaded line, clean star, or bounded composite batch.
3. **Defect-weighted potential.** Charge each selected defect to an anchor-product
   resource and prove strict decrease under logarithmic joint release.
4. **External rank one.** Bound one replacement cell plus two background points
   on the thinned packet subgrid.
5. **Minimal-support sectors.** Pay sectors which receive no or only one support-
   excess power.
6. **Destroyed-versus-created constants.** Insert the heavy-level destruction
   count into PX218 and prove strict net improvement.
7. **Closure conversion.** Apply a terminating decoder to PX63.

The immediate frontier is item 1, 2, or 3. Heavy selected-defect levels and
internal rank three are no longer missing inputs.

## 6. Verification

```bash
python scripts/verify_product_iterated_packet_release.py
python scripts/verify_product_thinned_joint_packet.py
python scripts/verify_product_packet_count_barrier.py
python scripts/verify_product_defect_heavy_packets.py
```

The verifiers check packet intersections and extraction, joint release and
conditioning, packet-compatible thinning, exact rank-three transfer, the
candidate packet-count barrier, selected-cross disjointness, exact old-defect
decomposition, heavy-level counting, and removal of all included old packet
crosses.

The classical no-three-in-line conjecture and infinite product closure remain
open.

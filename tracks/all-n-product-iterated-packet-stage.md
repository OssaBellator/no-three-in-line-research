# All-n product track: iterated product-packet release stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-conditioned-packet-release-stage.md`](all-n-product-conditioned-packet-release-stage.md).
PX210--PX214 extract and release one common-product packet with conditioned
fixed-rank spread. PX215--PX218 iterate that mechanism. PX219--PX220 pay internal
rank-three collateral after packet-compatible square-root thinning, while
PX221--PX222 identify the sharp packet-count barrier and the surviving
logarithmic release window.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| One-packet release | **COMPLETE** | PX212--PX214 give existence, spread, conditioning, and external-load transfer. |
| Product-level overlap | **COMPLETE** | PX215 proves that two distinct anchor-product packets share at most two candidate cells. |
| Second-packet extraction | **COMPLETE** | PX216 converts every positive residual support-four mass into a new product level, quantitatively. |
| Fixed packet packing | **COMPLETE** | PX217 releases any `k` packets jointly when `h>=32 max(1,Delta,k)`. |
| Conditioned packet packing | **COMPLETE** | PX218 shows that exposure adds one complementary partial matching per packet and gives conditioned spread. |
| Packet-certified support four | **ELIMINATED EXACTLY** | Every cross event certified by every released packet has probability zero. |
| Internal packet rank three | **CONTROLLED** | PX219--PX220 give a square-root packet restriction with linear expected internal rank-three collateral. |
| Absolute packet count | **REFUTED FOR CANDIDATE ENERGY** | PX221 gives geometric-progression grids requiring `Omega(h)` product levels to remove a fixed energy fraction. |
| Logarithmic packet window | **PROVED** | PX222 gives polynomial density/spread for `O(log h)` released packets and explicit support-excess thresholds. |
| External rank one | **OPEN** | One release cell plus two background points is not yet below the destroyed-mass scale. |
| Defect-weighted termination | **OPEN** | No theorem yet bounds the number of heavy levels carrying old selected defects. |
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
every packet-certified cross. PX217 uses witnesses

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

For `k` packets, sequential exposure adds at most one complementary partial
matching per packet. PX218 therefore replaces `Delta` by `Delta+k`, independently
of the exposure rank, and gives residual cylinder constant `e^(4Delta+8k)`.

## 4. Internal rank-three collateral

PX219 applies PX189 to one designated packet correspondence. It retains

\[
s\ge\frac12\sqrt h
\]

indices whose complete packet subgrid contains only `O(s^4)` compatible
collinear triples. The designated packet still has `s` arcs and certifies
`binom(s,2)` crosses.

PX220 applies the joint-release cylinder law and obtains

\[
\mathbb E\Phi_{3,\rm int}
=
O\!\left(e^{4\Delta+4k}s\right).
\]

Thus internal rank three is linear while the designated packet cross family is
quadratic. The conditioned statement has constant `e^(4Delta+8k)`.

## 5. Packet-count barrier

For geometric-progression coordinates `x_i=y_i=2^i` and anchor zero, product
levels have sizes

\[
1,2,\ldots,h-1,h,h-1,\ldots,2,1.
\]

PX221 computes total candidate support-four energy

\[
\frac{h(h-1)(2h-1)}6.
\]

One level contains at most `binom(h,2)` energy, so reducing the total by half
requires at least `(2h-1)/6` released levels. Therefore the former absolute
packet-count target is false without extra weighting by the current selected
state.

## 6. Logarithmic packet window

PX222 substitutes

\[
k\le\kappa\log h
\]

into PX217--PX218. The unconditioned cylinder loss is at most `h^(4kappa)` and
the conditioned loss at most `h^(8kappa)`, up to fixed `Delta` factors.

A square-root-thinned support-`u`, rank-`r` sector still gains a power when

\[
\kappa<\frac{u-r}{8}
\]

unconditionally, or

\[
\kappa<\frac{u-r}{16}
\]

after exposure. This leaves a viable route through logarithmically many
**defect-heavy** packets, but not through all candidate-heavy levels.

## 7. Remaining proof tasks

1. **Defect-level concentration.** Prove that old selected defects occupy only
   `O(log h)` heavy anchor-product levels.
2. **Defect-weighted packet potential.** Replace unrestricted candidate energy by
   a potential charging only current defects and prove strict decrease under
   joint release.
3. **External rank-one geometry.** Bound one release cell plus two background
   points on the thinned packet subgrid.
4. **Minimal-support sectors.** Control sectors which receive no or only one
   support-excess power.
5. **Destroyed old mass.** Relate packet-certified candidate crosses to defects
   actually present in the current matching.
6. **Many-packet constants.** Sharpen the `e^(4k)` and `e^(8k)` losses in the
   logarithmic regime.
7. **Depth-two accounting.** Combine defect-heavy packet release with loaded-line
   and clean-star recursion and prove strict net descent.
8. **Closure conversion.** Insert the terminating decoder into PX63.

The immediate frontier is item 1 or item 2. Candidate-energy bounded termination
is now refuted, while internal rank three and the probability theory for fixed
or logarithmic packet families are no longer missing inputs.

## 8. Verification

```bash
python scripts/verify_product_iterated_packet_release.py
python scripts/verify_product_thinned_joint_packet.py
python scripts/verify_product_packet_count_barrier.py
```

The verifiers check product-level intersections, residual extraction, exact joint
release, conditioned complement structure, packet-compatible thinning, exact
rank-three transfer, the geometric-progression energy identity, the linear
packet-count lower bound, and logarithmic spread exponents.

The classical no-three-in-line conjecture and infinite product closure remain
open.

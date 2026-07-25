# Square-root-thinned joint packets have linear rank-three collateral

PX215--PX218 iterate product-packet extraction and release, but the external-load
interface still contains rank-three certificates formed entirely inside the
packet subgrid. This chapter combines the universal square-root thinning theorem
PX189 with the `k`-packet cylinder law PX217.

The conclusion is exact at the asymptotic scale needed by packet recursion: after
thinning one designated packet from order `h` to order

\[
s=\Omega(\sqrt h),
\]

all internal candidate triples have total count `O(s^4)`, hence only `O(s)`
expected released collateral. At the same time the designated packet still
certifies `binom(s,2)` rank-two cross events, all of which have probability zero.

Let

\[
A=\{(x_i,y_i):i\in[h]\}
\]

be the correspondence cells of one extracted vertex-disjoint product packet.
The row endpoint labels and column endpoint labels are disjoint, and both
coordinate lists are injective. Let `P_1` be the resulting designated packet,
normalized to the identity correspondence, and let

\[
P_1,P_2,\ldots,P_k
\]

be any fixed family of product packets on the same packet subgrid.

## 1. Packet-compatible square-root thinning

### Theorem PX219 -- PROVED

For every sufficiently large `h`, there is a set `J subseteq [h]` with

\[
\boxed{
|J|=s\ge\frac12\sqrt h
}
\]

such that the complete restricted candidate grid

\[
\{x_i:i\in J\}
\times
\{y_i:i\in J\}
\]

contains only

\[
\boxed{O(s^4)}
\]

collinear triples with distinct rows and columns.

Every packet `P_nu` restricts to a partial matching on the selected row and
column sets. The designated packet `P_1` restricts to exactly `s` correspondence
arcs and therefore certifies

\[
\boxed{\binom s2}
\]

rank-two packet crosses.

### Proof

Apply PX189 to the endpoint family `A`. It supplies `J` of the stated size with
`T(J)=O(s^4)` compatible collinear triples in the complete selected grid.
Restricting a partial matching preserves the partial-matching property.

The normalized designated packet contains the correspondence arc `i->i` for
every selected index `i`. Every unordered pair of these arcs certifies one cross
event, giving exactly `binom(s,2)`. \(\square\)

No entropy from the additional packets is needed for this thinning step.

## 2. Linear expected internal rank-three load

Let `F_J` be the inherited forbidden-position graph on the selected subgrid, with
maximum row and column degree at most `Delta`. Let

\[
\Omega_J
=
\Omega(F_J;\{P_1|_J,\ldots,P_k|_J\})
\]

be the joint-release family from PX217.

### Theorem PX220 -- PROVED

Assume

\[
\boxed{
s\ge32\max(1,\Delta,k).}
\]

For a uniformly random matching `M` in `Omega_J`, the expected number of internal
collinear triples satisfies

\[
\boxed{
\mathbb E\Phi_{3,\rm int}(M)
=
O\!\left(e^{4\Delta+4k}s\right).
}
\]

Every one of the `binom(s,2)` designated-packet cross events has probability
zero. Consequently the internal rank-three expectation is lower order than the
quadratic designated-packet certificate family:

\[
\frac{\mathbb E\Phi_{3,\rm int}(M)}{\binom s2}
=
O\!\left(\frac{e^{4\Delta+4k}}s\right).
\]

At every fixed recursion depth and fixed packet count, this ratio tends to zero.

### Proof

PX219 leaves `O(s^4)` compatible candidate triples. Each is a rank-three partial
matching. PX217 bounds its probability by

\[
\frac{e^{4\Delta+4k}}{(s)_3}.
\]

Summing over all internal triples gives

\[
O\!\left(
 e^{4\Delta+4k}
 \frac{s^4}{(s)_3}
\right)
=
O\!\left(e^{4\Delta+4k}s\right).
\]

Every designated-packet cross is one of the forbidden rank-two events defining
`Omega_J`, so its probability is zero. \(\square\)

### Corollary PX220a -- PROVED

After conditioning on a compatible rank-`a` partial matching, put `n=s-a`. If

\[
n\ge32\max(1,k,\Delta+k),
\]

then every residual internal rank-three family has expected weight at most

\[
\boxed{
 e^{4\Delta+8k}
 \frac{W_{3,\rm int}^{\rm res}}{(n)_3}.
}
\]

In particular, if a residual thinning or deletion leaves `O(n^4)` internal
triple weight, the conditioned expectation remains

\[
O\!\left(e^{4\Delta+8k}n\right).
\]

This is PX218 applied to the residual rank-three family.

## 3. Consequence for packet recursion

PX219--PX220 remove internal rank three as an asymptotic obstruction to releasing
one or any fixed number of product packets.

- the designated packet retains a quadratic cross family;
- every such cross is eliminated exactly;
- internal candidate triples create only linear expected collateral;
- the same statement survives bounded-rank exposure.

This does not yet prove strict descent because the current selected state need
not contain all packet-certified crosses. The remaining terms are:

1. external rank-one certificates involving two background points;
2. rank-two collisions through unreleased anchor-product levels;
3. the relation between packet candidate energy and old selected defect mass;
4. a bound on the number of packet rounds needed for termination.

The immediate geometric frontier is therefore external rank one or the
packet-energy potential, not internal rank three.

## 4. Verification

Run

```bash
python scripts/verify_product_thinned_joint_packet.py
```

The verifier constructs arithmetic and random packet correspondences, finds
square-root subsets with bounded normalized triple count, checks that restricted
packets remain partial matchings, enumerates a small joint-release family, and
verifies the rank-three expectation and quadratic packet-cross comparison.

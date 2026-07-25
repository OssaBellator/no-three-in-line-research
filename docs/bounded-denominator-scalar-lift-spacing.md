# Scalar-lift spacing for radial decoder profiles

**Branch:** `research/bounded-denominator-absorbers`

BDA5q reduces every non-wall one-cell decoder channel to the integer scalar

$$
s = h det(d,e),
$$

where `d=(a,b)` is the primitive radial direction, `e=(r,t)` is the primitive context direction, and `h` is the radial scale. This note classifies all integer lifts of one fixed residue of that scalar.

## Setup

Normalize

$$
d=(a,b),\qquad e=(r,t),\qquad a>0,\ r>0,
$$

with both vectors primitive, and assume

$$
δ=det(d,e)=at-br\ne0.
$$

Put

$$
g=gcd(|δ|,q),\qquad m=q/g.
$$

## BDA5u -- scalar congruence and modulus-geometry duality -- PROVED

Fix one scalar residue `ξ` modulo `q`. The positive integers `h` satisfying

$$
hδ ≡ ξ \pmod q
$$

have the following exact description.

1. There is no solution unless `g` divides `ξ`.
2. When a solution exists, all solutions form one residue class modulo

$$
m=q/g.
$$

Moreover, the two primitive directions have the same projective class modulo `g`, and their rational slopes satisfy

$$
|b/a-t/r|
=
|δ|/(ar)
\ge
 g/(||d||_∞ ||e||_∞).
$$

Thus small scalar-lift spacing and strong geometric separation are complementary: their controlling moduli multiply to `q`.

### Proof

Write `δ=gδ₀` and `q=gm`. The congruence is soluble only when `g|ξ`. After writing `ξ=gξ₀`, it becomes

$$
hδ₀ ≡ ξ₀ \pmod m.
$$

Because `g=gcd(|δ|,q)`, the integers `δ₀` and `m` are coprime. Hence `δ₀` is invertible modulo `m`, and there is exactly one residue class of solutions modulo `m`.

Since `g|det(d,e)` and both vectors are unimodular modulo `g`, they define the same point of the projective line over `Z/gZ`. Explicitly, a determinant-one change of coordinates sends `d` to `(1,0)`. The transformed vector `e` then has second coordinate zero modulo `g`; unimodularity forces its first coordinate to be a unit, so it is a unit multiple of the transformed `d`.

Finally,

$$
|b/a-t/r|=|δ|/(ar).
$$

The determinant is a nonzero multiple of `g`, while `a≤||d||_∞` and `r≤||e||_∞`, giving the displayed separation. QED.

## BDA5v -- dense scalar chain or separated directions -- PROVED

Fix exact vectors `d,e` and one soluble scalar residue. Let

$$
1≤h_1<h_2<...<h_K≤H
$$

be distinct admissible radial lifts. Then

$$
H ≥ 1 + (q/g)(K-1).
$$

Equivalently,

$$
K ≤ ceil(Hg/q).
$$

If `K≥ρH` and `H≥2/ρ`, then

$$
g ≥ ρq/2
$$

and therefore

$$
|b/a-t/r|
≥
ρq/(2||d||_∞||e||_∞).
$$

Hence a linearly dense repeated scalar profile forces a quantitatively separated pair of primitive directions.

There is also an adjacent-lift alternative. Let `J` be the number of available integers in the selected residue class modulo `m=q/g` inside `[1,H]`. Among the occupied lifts there are at least

$$
E=max(0,2K-J-1)
$$

adjacent occupied pairs `h,h+m`, and at least `ceil(E/2)` of them can be chosen disjointly. Every such pair has the same scalar increment

$$
(h+m)δ-hδ
=
mδ
=
q(δ/g).
$$

### Proof

BDA5u puts all admissible lifts in one residue class modulo `m`, so successive occupied values differ by at least `m`. This gives the height and counting inequalities.

If `K≥ρH` and `H≥2/ρ`, then `K-1≥ρH/2`. The height inequality gives

$$
m≤(H-1)/(K-1)≤2/ρ,
$$

so `g=q/m≥ρq/2`. BDA5u then gives the slope separation.

For the adjacency statement, view the `J` available values as a path of slots spaced by `m`. The same run-counting argument as BDA4d gives at least `2K-J-1` occupied adjacent edges and a disjoint matching of at least half of them. The scalar increment is direct substitution. QED.

## Interface to BDA6

A repeated visible scalar state can no longer be treated as an arbitrary integer lift family.

- If `g` is small, radial lifts are sparse because their spacing is `q/g`.
- If `g` is large, the radial and context directions are quantitatively separated and already coincide projectively modulo the large divisor `g`.
- If the scalar chain is dense inside its allowed progression, it supplies many disjoint adjacent lifts with one common scalar increment `q(δ/g)`.
- The extreme case `g=q` is the residue-wall regime: `d` and `e` lie in the same projective class modulo `q`, while their distinct integer lifts are separated by the BDA3k Farey bound.

The remaining transition work is therefore to route the common scalar increment or the large-modulus direction pair into the existing carry, anchor, and radial-pair decoders.

## Finite check

`scripts/verify_bda_scalar_lift_spacing.py` exhausts small denominators and primitive direction pairs. It checks congruence solvability, uniqueness modulo `q/g`, projective coincidence modulo `g`, the slope-separation inequality, dense-chain bounds, and adjacent-lift extraction.
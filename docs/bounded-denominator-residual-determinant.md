# Residual determinant normal form for dense scalar profiles

**Branch:** `research/bounded-denominator-absorbers`

BDA5u--BDA5v show that a fixed non-wall scalar profile is controlled by

$$
δ=det(d,e),\qquad g=gcd(|δ|,q),\qquad m=q/g.
$$

The admissible radial lifts are spaced by `m`, and adjacent lifts have scalar increment `q(δ/g)`. This note identifies `δ/g` as the unique transverse integer of the direction pair and proves that dense recurrence confines it to a finite library.

## Unimodular coordinates

Let

$$
d=(a,b)
$$

be the primitive radial direction. Choose one integer complement

$$
f=(c,d_2)
$$

with

$$
det(d,f)=ad_2-bc=1.
$$

Such a complement exists because `gcd(a,|b|)=1`.

Let `e` be a primitive context direction with `δ=det(d,e)≠0`. Put

$$
g=gcd(|δ|,q),\qquad k=δ/g,\qquad m=q/g.
$$

## BDA5w -- transverse determinant normal form -- PROVED

There is one unique integer `α` such that

$$
e=αd+δf=αd+gk f.
$$

The parameters satisfy

$$
gcd(|k|,m)=1
$$

and

$$
gcd(α,g)=1.
$$

For a soluble scalar residue `ξ`, the congruence

$$
hδ ≡ ξ \pmod q
$$

reduces exactly to

$$
hk ≡ ξ/g \pmod m.
$$

Thus `k` is the invertible transverse coefficient at the residual modulus `m`, while `g` is the projective-coincidence modulus.

### Proof

The ordered pair `(d,f)` is a unimodular basis of `Z^2`. Write `e=αd+βf`. Taking the determinant with `d` gives `β=det(d,e)=δ`, proving existence and uniqueness. Equivalently, `α=det(e,f)`.

By the definition of `g`, removing `g` from both `δ` and `q` leaves coprime integers `k` and `m`.

Modulo `g`, the decomposition is `e≡αd`. If a prime divided both `α` and `g`, then both coordinates of `e` would vanish modulo that prime because `d` is integral, contradicting primitivity of `e`. Hence `gcd(α,g)=1`.

Finally write `δ=gk`, `q=gm`, and `ξ=gξ_0`. Dividing the soluble congruence by `g` gives the reduced equation. QED.

## BDA5x -- finite increment library under dense recurrence -- PROVED

Put

$$
A=||d||_∞,\qquad B=||e||_∞.
$$

The residual transverse coefficient obeys

$$
|k| ≤ 2AB/g.
$$

Suppose one scalar residue profile has `K` admissible radial lifts in `[1,H]`, with

$$
K≥ρH,\qquad H≥2/ρ.
$$

Then BDA5v gives `g≥ρq/2`, and therefore

$$
|k| ≤ 4AB/(ρq).
$$

Every adjacent admissible pair `h,h+m` has the common scalar increment

$$
qk.
$$

Consequently the dense profile uses at most

$$
2 floor(4AB/(ρq))
$$

possible nonzero signed increment types before imposing the coprimality condition `gcd(|k|,m)=1`.

In particular, if

$$
q>4AB/ρ,
$$

no linearly dense scalar chain with those exact direction norms can exist.

### Proof

The determinant estimate is

$$
|δ|=|at-br|≤|a||t|+|b||r|≤2AB.
$$

Divide by `g` to obtain the first bound. Under the density hypothesis, substitute `g≥ρq/2`. The increment identity is BDA5v:

$$
(h+m)δ-hδ=mδ=(q/g)(gk)=qk.
$$

There are at most twice the integer part of the absolute bound for nonzero signed `k`. If the bound is below one, no nonzero integer `k` exists. QED.

## Combined transition output

A dense repeated scalar profile now gives all of the following simultaneously.

1. A large projective-coincidence divisor `g`.
2. A residual modulus `m=q/g` on which `k` is a unit.
3. A bounded transverse integer `k`.
4. Many disjoint adjacent radial lifts with one increment `qk`.
5. The exact direction equation `e=αd+gk f`, with `α` a unit modulo `g`.

When the primitive shape `AB` is already bounded by BDA4d, the possible increment `qk` belongs to a finite library depending only on `q`, the density threshold, and that shape bound. The next geometric task is to realize these repeated increments as compatible anchored rectangle or alternating trades.

## Finite check

`scripts/verify_bda_residual_determinant.py` exhausts small primitive direction pairs and denominators. It constructs unimodular complements, verifies the unique transverse decomposition, both coprimality assertions, reduced scalar congruences, norm bounds, and the dense finite-increment estimate.
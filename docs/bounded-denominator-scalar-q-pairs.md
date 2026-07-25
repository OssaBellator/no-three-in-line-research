# Extracting genuine q-adjacent radial pairs from scalar chains

**Branch:** `research/bounded-denominator-absorbers`

BDA5u places one scalar-residue family in an arithmetic progression with step

$$
m=q/g,
$$

where `g=gcd(|det(d,e)|,q)`. Consecutive scalar slots differ by `m`, but the existing BDA4e radial decoder uses the genuine adjacent scales `h,h+q`. Since `q=gm`, a jump of exactly `g` scalar slots is one decoder-adjacent radial jump.

## Slot model

Let the available scalar lifts be

$$
h_j=h_0+jm,\qquad 0<=j<J.
$$

Let `S` be the occupied slot set and put `K=|S|`. Join slot `j` to slot `j+g` whenever both exist and are occupied. In radial coordinates this edge is exactly

$$
h_j \longleftrightarrow h_j+q.
$$

The slot graph is the disjoint union of at most `g` paths, one for each index residue modulo `g`.

## BDA5y -- q-step radial-pair extraction -- PROVED

The number of occupied q-step edges is at least

$$
E_q=max(0,2K-J-g).
$$

At least

$$
ceil(E_q/2)
$$

of these edges can be selected with pairwise disjoint radial parameters.

Every selected edge is a genuine BDA4e adjacent radial pair

$$
(h,h+q)
$$

with the same primitive radial direction and the same fixed scalar-profile data.

### Proof

Split the `J` slots into the at most `g` paths indexed by `j mod g`. Within each path, decompose the occupied vertices into runs. Across all paths, every empty slot can increase the total number of occupied runs by at most one, and the `g` paths contribute at most `g` initial runs. Hence the number `R` of occupied runs satisfies

$$
R<=J-K+g.
$$

A run with `l` occupied vertices contains `l-1` occupied q-step edges. Summing over all runs gives

$$
K-R
>=
K-(J-K+g)
=
2K-J-g.
$$

This proves the edge bound. Each path is an ordinary path graph, so alternating edges in every occupied run select a matching of at least half of its edges. Summing gives at least `ceil(E_q/2)` disjoint pairs. QED.

## Density consequences

If

$$
K >= (J+g+L)/2,
$$

then the scalar family contains at least `L` occupied q-step edges and at least `ceil(L/2)` disjoint BDA4e radial pairs.

In particular, if `K>=ρJ` with `ρ>1/2`, then

$$
E_q >= (2ρ-1)J-g.
$$

Thus whenever `J` is large compared with `g/(2ρ-1)`, a positive fraction of the scalar slots yields disjoint genuine decoder pairs.

## Scalar and direction increments on extracted pairs

Retain the BDA5w notation

$$
δ=gk.
$$

For every extracted pair `h,h+q`, the determinant scalar changes by

$$
(h+q)δ-hδ=qδ=qgk.
$$

The channel vectors themselves use the standard BDA adjacent scales `h` and `h+q`, so no new rectangle construction is required. The extracted pairs enter BDA4e--BDA5e directly, carrying the already fixed primitive directions, valuation profile, channel word, and anchor data.

## Interface to BDA6

A recurrent scalar profile now has three quantitative outcomes.

1. Sparse occupancy in its `q/g` progression.
2. Large projective divisor and bounded residual increment from BDA5w--BDA5x.
3. Dense occupancy producing many disjoint genuine `h,h+q` radial pairs by BDA5y.

Outcome 3 returns the problem to the proved radial-pair regularization and rectangle-decoder pipeline. The remaining issue is compatibility of the extracted anchors and support, not scalar arithmetic.

## Finite check

`scripts/verify_bda_scalar_q_pairs.py` exhausts small slot paths, divisors `g`, and every occupied subset. It checks the `2K-J-g` edge bound, the disjoint matching bound, the radial difference `q=gm`, and the scalar increment `qδ`.
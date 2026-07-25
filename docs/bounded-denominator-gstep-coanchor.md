# Weighted co-anchor extraction on interlaced scalar paths

**Branch:** `research/bounded-denominator-absorbers`

BDA5y extracts unweighted `h,h+q` pairs from a scalar progression with step `m=q/g`. The paid absorber application needs the weighted, co-anchored version. This note extends BDA4f from one radial path to the `g` interlaced scalar paths.

## Weighted scalar slots

Let

$$
h_j=h_0+jm,\qquad 0<=j<J,\qquad q=gm.
$$

Let `A` be a set of anchors. For anchor `P` and slot `j`, let

$$
0<=w_{P,j}<=β
$$

be the paid weight of the fixed scalar-profile occurrence at `P`. Put

$$
W=sum_P sum_j w_{P,j}.
$$

The safely transferable weight of the q-adjacent pair `j,j+g` is

$$
min(w_{P,j},w_{P,j+g}).
$$

Define the total q-pair overlap

$$
Ω_g=sum_P sum_{j=0}^{J-g-1} min(w_{P,j},w_{P,j+g}).
$$

## BDA5z -- weighted g-step co-anchor extraction -- PROVED

The overlap satisfies

$$
Ω_g >= (2W-β|A|(J+g))_+.
$$

The q-step edges on each anchor split into two global parity classes, and every class uses each radial slot at most once. Therefore one parity class is a radially disjoint co-anchored family with paid weight at least

$$
(1/2)(2W-β|A|(J+g))_+.
$$

In particular, if

$$
W >= (1/2+ε)β|A|(J+g),
$$

then one parity class carries at least

$$
εβ|A|(J+g)
$$

of paid genuine `h,h+q` pair weight.

### Proof

Fix one anchor and use the layer-cake representation of each slot weight. At level `t`, let `S_t` be the occupied slots. The q-step graph is the union of the at most `g` paths indexed by slot residue modulo `g`. If `R_t` is the total number of occupied runs across those paths, then

$$
R_t<=J-|S_t|+g.
$$

The number `e_t` of occupied q-step edges is `|S_t|-R_t`, so

$$
e_t>=2|S_t|-J-g.
$$

Integrating from `0` to `β` gives

$$
sum_{j=0}^{J-g-1} min(w_j,w_{j+g})
>=
2sum_j w_j-β(J+g).
$$

Insert the positive part, sum over anchors, and use `sum(x_P)_+ >= (sum x_P)_+`.

Each residue path is bipartite by edge parity. Taking the same two parity labels across every anchor and residue path partitions all q-step edges into two classes, each vertex-disjoint in radial slots. One class carries at least half the overlap. QED.

## Direct compatibility interface

Apply BDA4e to the heavier parity class with row/column load threshold `Λ`.

- If every row and column has load at most `Λ`, a row-column-compatible subfamily carries at least

$$
Ω_g / (2(10(Λ-1)+1))
$$

of the lower-bound pair weight before any additional geometric cleaning.
- If a load exceeds `Λ`, BDA4e returns one of the five explicit affine anchor laws, carrying at least one fifth of the paid incidence at that heavy coordinate.

Thus a scalar profile above the BDA5z half-capacity threshold enters the existing radial decoder pipeline without a new co-anchor hypothesis. Below the threshold it satisfies the explicit dispersed-anchor inequality

$$
W < (1/2+ε)β|A|(J+g).
$$

## Interface to BDA6

The scalar-lift route now terminates in one of four named outputs:

1. sparse scalar occupancy;
2. a finite transverse increment library;
3. a paid compatible family of genuine q-adjacent radial pairs;
4. one of the five paid affine anchor chains from BDA4e.

Outcome 3 passes directly to BDA5a--BDA5g. The unresolved scalar branch is therefore only the explicit dispersed-anchor inequality or an affine anchor chain, not the existence of co-anchored decoder pairs.

## Finite check

`scripts/verify_bda_gstep_coanchor.py` exhausts small capped slot-weight vectors and interlacing parameters. It checks the weighted overlap inequality, the two parity classes, radial disjointness, the density consequence, and additive combination across anchors.
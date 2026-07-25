# Exact overlap-variation routing on BDA scalar paths

**Branch:** `research/bounded-denominator-absorbers`

BDA5z extracts paid co-anchored `h,h+q` pairs when the total adjacent overlap is large. Its remaining output was recorded only as a dispersed-anchor inequality. This note replaces that inequality by an exact identity on the `g` interlaced scalar paths. Small pair overlap forces paid mass onto path endpoints or onto oriented `q`-step weight jumps, producing explicit one-sided missing-partner fronts.

## Interlaced paths

Retain the BDA5z slot system

$$
h_j=h_0+jm,
\qquad
0\le j<J,
\qquad
q=gm,
$$

with anchor-slot weights `w_{P,j}>=0`. Put

$$
W=\sum_P\sum_{j=0}^{J-1}w_{P,j}
$$

and

$$
\Omega_g
=
\sum_P\sum_{j=0}^{J-g-1}
\min\{w_{P,j},w_{P,j+g}\}.
$$

For every anchor `P` and residue `0<=r<g` represented among the slots, read the sequence

$$
w_{P,r},w_{P,r+g},w_{P,r+2g},\ldots
$$

as one scalar path. Let `B_g` be the total endpoint weight of these paths, counting the unique vertex of a one-vertex path twice. Let

$$
V_g
=
\sum_P\sum_{j=0}^{J-g-1}
|w_{P,j+g}-w_{P,j}|
$$

be the total `q`-step variation.

## BDA5ae -- exact overlap-variation identity -- PROVED

The three quantities satisfy

$$
\boxed{
2(W-\Omega_g)=B_g+V_g.
}
$$

### Proof

For one path with weights `a_0,...,a_n`,

$$
2\min(a_i,a_{i+1})
=
a_i+a_{i+1}-|a_{i+1}-a_i|.
$$

Summing over its edges gives

$$
2\sum_{i=0}^{n-1}\min(a_i,a_{i+1})
=
2\sum_{i=0}^{n}a_i-a_0-a_n-
\sum_{i=0}^{n-1}|a_{i+1}-a_i|.
$$

For a one-vertex path the same formula reads `0=2a_0-2a_0`. Sum over all anchors and residue paths. QED.

## BDA5af -- pair bank, endpoint front, or variation front -- PROVED

Fix `0<=theta<=1`. At least one of the following holds.

1. **Paid pair bank.** We have
   $$
   \Omega_g\ge\theta W,
   $$
   and one BDA5z parity class is radially disjoint and carries genuine `h,h+q` pair weight at least
   $$
   \boxed{\theta W/2.}
   $$
2. **Endpoint front.** Distinct scalar-path endpoint slots carry total weight greater than
   $$
   \boxed{(1-\theta)W/2.}
   $$
3. **Variation front.** The total `q`-step variation satisfies
   $$
   \boxed{V_g>(1-\theta)W.}
   $$

### Proof

If the first outcome fails, BDA5ae gives

$$
B_g+V_g=2(W-\Omega_g)>2(1-\theta)W.
$$

Hence either `B_g>(1-theta)W` or `V_g>(1-theta)W`. A physical endpoint slot occurs at most twice in the endpoint multiset, so distinct endpoint slots retain at least `B_g/2`. QED.

## Oriented unmatched mass

Define the downward and upward excesses

$$
E^-_g
=
\sum_P\sum_{j=0}^{J-g-1}
(w_{P,j}-w_{P,j+g})_+,
$$

$$
E^+_g
=
\sum_P\sum_{j=0}^{J-g-1}
(w_{P,j+g}-w_{P,j})_+.
$$

Then

$$
V_g=E^-_g+E^+_g.
$$

An edge contributing to `E^-_g` has paid mass at scale `h_j` unmatched by the selected family at `h_j+q`; an edge contributing to `E^+_g` has the reverse orientation.

## BDA5ag -- oriented parity-disjoint missing-partner fronts -- PROVED

If the variation-front outcome of BDA5af holds, then one orientation has excess at least

$$
V_g/2>(1-\theta)W/2.
$$

Split the edges of that orientation by the two global BDA5z parity classes. One parity class is slot-disjoint and carries oriented excess at least

$$
\boxed{
V_g/4
>
(1-\theta)W/4.
}
$$

Thus the variation output is a paid slot-disjoint family of exact records

$$
(P,h,\pm,q,e),
$$

where `e>0` is current paid weight present on one side of a genuine `q`-adjacent pair but unmatched on the other side. Every record retains the full denominator, primitive directions, scalar residue, role word, and affine-anchor provenance of its profile.

### Proof

The two orientations partition the absolute variation, so one carries at least half. The same two edge parities used in BDA5z partition the selected oriented edges, and each parity uses every scalar slot at most once. Weighted pigeonhole gives the displayed quarter. QED.

## BDA5ah -- exact replacement of the dispersed-anchor output -- PROVED

For every threshold `theta`, one exact BDA scalar profile now returns:

1. a radially disjoint paid `h,h+q` pair bank of weight at least `theta W/2`;
2. a paid family of distinct extreme scalar slots of weight greater than `(1-theta)W/2`;
3. or a paid slot-disjoint family of oriented one-sided `q`-partner deficits of weight greater than `(1-theta)W/4`.

The endpoint and oriented-front outputs are finite geometric records, not inequalities. They expose exactly where the selected profile fails to supply a co-anchored pair: at the end of an interlaced scalar path or across a specific `q`-step weight jump.

For the frequently useful choice `theta=1/2`, the three guaranteed scales are respectively

$$
\boxed{W/4,\qquad W/4,\qquad W/8.}
$$

The pair output enters BDA4e and the proved radial decoder. The remaining scalar work is now installation/payment or denominator descent for an explicit endpoint or oriented missing-partner front, together with the five affine heavy-load chains. The former unnamed dispersed-anchor inequality is no longer a terminal state.

## Finite check

`scripts/verify_bda_overlap_variation.py` exhausts small interlaced weighted paths, checks the exact overlap-variation identity, endpoint multiplicities, pair/endpoint/variation dichotomy, orientation split, parity disjointness, and the `theta=1/2` constants. It also checks additive combination across several anchors.

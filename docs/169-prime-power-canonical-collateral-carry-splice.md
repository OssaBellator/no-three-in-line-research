# Canonical collateral line energy feeds matching walls, heavy prefixes, or dispersed carry cells

CMR558--CMR563 classify every static canonical selector profile as a heavy
line, a paid-endpoint secant star, a cell-disjoint residual bank, or a residual
repeated-cell star. This chapter makes the connection to the existing
prime-power geometry quantitative.

The fixed profile has an exact factorial-moment line energy. Dyadic
localization by primitive line height gives many fixed line signatures in one
height band. For rank-zero mass, the CMR355--CMR358 conversion applies:
choose one compatible pair on each line, then obtain a matching-vertex fan or
a matching-compatible family with common first-separation depth and projective
direction, followed by a heavy full-prefix cell or many occupied full-prefix
cells.

Rank-one mass is even more localized. Its distinct supporting lines already
form a fan through one paid endpoint. If the mass instead concentrates on one
line, the line has quantitatively low primitive height.

Fix a static canonical selector signature `\Sigma` in an inherited envelope of
side

\[
m=p^g,
\qquad
n=m-2\ge5,
\]

with paid pair `Z`, paid line `L`, and static threshold `q>=4`. Put

\[
c_q=\frac{11}{30}\left(1-\frac2q\right).
\]

Use the line-profile notation `r_K,T_0(K),T_1(z,K)` from CMR559.

## 1. Fixed factorial-moment line energy

### Theorem CMR564 — PROVED

The profiles satisfy

\[
\boxed{\sum_K(r_K)_3\ge6V_0}
\]

and, for every paid endpoint `z`,

\[
\boxed{
\sum_{\substack{K\ni z\\K\ne L}}(r_K)_2
\ge2V_1(z).
}
\]

Consequently a static profile satisfies at least one of

\[
\boxed{\sum_K(r_K)_3\ge3c_q(n)_3}
\]

or

\[
\boxed{
\sum_{\substack{K\ni z\\K\ne L}}(r_K)_2
\ge\frac{c_q}{2}(n)_2
}
\]

for some paid endpoint `z`.

### Proof

CMR559 gives

\[
T_0(K)\le\binom{r_K}{3}=\frac{(r_K)_3}{6}
\]

and

\[
T_1(z,K)\le\binom{r_K}{2}=\frac{(r_K)_2}{2}.
\]

Sum and apply CMR558. ∎

## 2. Dyadic primitive-height localization

Write every nonaxis line in primitive direction form and let

\[
K(K)=\max\{|u_K|,|v_K|\}
\]

be its primitive height. Put

\[
B=\lceil\log_2m\rceil.
\]

For dyadic `H`, let `J_{0,H}` count rank-zero supporting lines and let
`J_{1,H}(z)` count rank-one supporting lines through `z` with

\[
H\le K(K)<2H.
\]

A line in this band contains at most

\[
q_H=1+\left\lfloor\frac{m-1}{H}\right\rfloor
\]

parent-board cells.

### Theorem CMR565 — PROVED

If the rank-zero alternative of CMR558 holds, some dyadic `H` satisfies

\[
\boxed{
J_{0,H}\frac{\binom{q_H}{3}}{(n)_3}
\ge\frac{c_q}{2B}.
}
\]

If the rank-one alternative holds at endpoint `z`, some dyadic `H` satisfies

\[
\boxed{
J_{1,H}(z)\frac{\binom{q_H}{2}}{(n)_2}
\ge\frac{c_q}{4B}.
}
\]

### Proof

Partition the exact line sums of CMR559 into at most `B` dyadic height bands.
One band carries at least a `1/B` fraction of the relevant normalized mass.
Use the line capacities `binom(q_H,3)` and `binom(q_H,2)`. ∎

## 3. Explicit line-count bounds

### Theorem CMR566 — PROVED

Assume `m>=20`. In the rank-zero case,

\[
\boxed{
J_{0,H}>
\frac{5c_q}{11}\frac{H^3}{B}
\ge\frac{H^3}{12B}.
}
\]

Assume `m>=7`. In the rank-one case,

\[
\boxed{
J_{1,H}(z)
\ge\frac{c_q}{16}\frac{H^2}{B}
\ge\frac{11}{960}\frac{H^2}{B}.
}
\]

### Proof

For rank zero, use the occupancy estimate from CMR354,

\[
\frac{\binom{q_H}{3}}{(n)_3}<\frac{11}{10H^3},
\]

in CMR565. For rank one, use

\[
\frac{\binom{q_H}{2}}{(n)_2}\le\frac4{H^2}
\]

for `m>=7`. Finally `c_q>=11/60`. ∎

## 4. Heavy lines have low primitive height

### Theorem CMR567 — PROVED

Let a nonaxis line of primitive height `K` contain `r>=2` parent-board cells.
Then

\[
\boxed{K\le\frac{m-1}{r-1}.}
\]

Consequently a rank-one line supporting `H` atoms satisfies

\[
\boxed{K\le\frac{m-1}{\rho_2(H)-1},}
\]

and a rank-zero line supporting `H` atoms satisfies

\[
\boxed{K\le\frac{m-1}{\rho_3(H)-1}.}
\]

### Proof

Successive integer points differ by a primitive vector whose largest
coordinate magnitude is `K`. The extreme points among `r` board points differ
by at least `(r-1)K` in one coordinate and at most `m-1`. Apply CMR560--CMR561.
∎

## 5. Rank-zero height bands enter the CMR355--CMR358 conversion

Choose one profile triple on each of the `J=J_{0,H}` lines from CMR565 and one
compatible pair from every triple.

### Theorem CMR568 — PROVED

Put

\[
A=\lceil\sqrt J\rceil.
\]

At least one of the following holds.

1. One source or target matching vertex is incident with at least `A` selected
   lines.
2. There is a matching-compatible pair family of size at least
   \[
   R=\left\lfloor\frac{J}{4A}\right\rfloor.
   \]
   It contains a subfamily of size at least
   \[
   M=\left\lfloor\frac{R}{g(p+1)}\right\rfloor
   \]
   with common first-separation depth and projective direction. This subfamily
   yields either one full prefix cell carrying at least
   \[
   \boxed{\left\lceil\frac{M}{m^{2/3}}\right\rceil}
   \]
   pairs, or more than
   \[
   \boxed{\frac{M}{m^{2/3}}}
   \]
   occupied full prefix cells.

### Proof

Apply CMR355, then CMR356 and CMR358 in the nonfan branch. ∎

## 6. Rank-one bands are already paid-endpoint fans

### Theorem CMR569 — PROVED

In the rank-one branch of CMR558, at least one of the following holds.

1. One supporting secant is heavy and has the low-height bound of CMR567.
2. Many distinct supporting lines through one fixed paid endpoint give a
   repeated-cell secant star with pairwise disjoint residual arms.
3. The dyadic band from CMR565 contains at least the number of fixed
   paid-endpoint secants in CMR566, all through the same endpoint and in one
   primitive-height band.

### Proof

Combine CMR560, CMR565--CMR567. ∎

## 7. Canonical collateral-to-carry endpoint

### Corollary CMR570 — PROVED

Every static canonical selector reaches one of:

1. a low-height heavy rank-one secant;
2. a paid-endpoint secant star with disjoint residual arms;
3. a low-height heavy rank-zero residual line;
4. a residual matching-vertex fan;
5. a heavy full-prefix cell;
6. a dispersed family of full-prefix cells.

All lines, endpoints, atom supports, height bands, first-separation signatures,
and prefix cells retain their canonical selector owner.

### Proof

Apply CMR558, followed by CMR567--CMR569. ∎

## 8. Revised frontier

Static canonical collateral is now spliced into existing prime-power objects.
Heavy profile lines have low primitive height; rank-one line banks are fixed
secant stars; rank-zero line banks convert to matching walls, heavy prefix
cells, or dispersed carry cells. The parallel cell-disjoint rank-zero packing
is handled by CMR577--CMR581.

The remaining work is dynamic payment for reuse of fixed wall/prefix/carry
certificates and for the persistent canonical-edge branch.

No all-`n` theorem is claimed. Factorial moments, dyadic localization,
occupancy constants, low-height bounds, and the quantitative carry splice are
checked in
[`scripts/verify_prime_power_canonical_collateral_carry.py`](../scripts/verify_prime_power_canonical_collateral_carry.py).

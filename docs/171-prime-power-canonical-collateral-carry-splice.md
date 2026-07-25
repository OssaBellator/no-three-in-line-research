# Canonical collateral line energy feeds matching walls, heavy prefixes, or dispersed carry cells

CMR558--CMR568 classify every static canonical selector profile as a heavy
conflict line, a repeated-cell secant star, or a linear rank-zero line system
with a disjoint conflict packing.  CMR569--CMR573 pay the disjoint-packing
branch by matching-preserving deletion, forced-core terminality, and private
restoration edges.

This chapter makes the remaining line geometry quantitative in the
prime-power coordinates.  The fixed profile has an exact factorial-moment line
energy.  Dyadic localization by primitive height gives many fixed line
signatures in one height band.  Rank-zero bands then enter the CMR355--CMR358
matching-wall/prefix/carry conversion.  Rank-one bands are already fixed-centre
secant fans, while a heavy line has explicitly low primitive height.

Fix a static canonical selector signature `\Sigma` in an inherited envelope of
side

\[
m=p^g,
\qquad
n=m-2\ge5,
\]

with paid pair `Z`, paid line `L`, and selector threshold `q>=4`.  Put

\[
c_q=\frac{11}{30}\left(1-\frac2q\right).
\]

Use the exact support-line weights `w_0(\Lambda),w_1(z,\Lambda)` and involved
cell counts `k_0(\Lambda),k_1(z,\Lambda)` from CMR558.

## 1. Fixed factorial-moment line energy

### Theorem CMR574 — PROVED

The rank-zero and rank-one profiles satisfy

\[
\boxed{
\sum_{\Lambda}(k_0(\Lambda))_3
\ge
6V_0
}
\]

and, for every paid endpoint `z`,

\[
\boxed{
\sum_{\substack{\Lambda\ni z\\\Lambda\ne L}}
(k_1(z,\Lambda))_2
\ge
2M_1(z),
}
\]

where `M_1(z)` is the number of rank-one atoms using `z`.

Consequently every static selector satisfies at least one of

\[
\boxed{
\sum_{\Lambda}(k_0(\Lambda))_3
\ge
3c_q(n)_3
}
\]

or

\[
\boxed{
\sum_{\substack{\Lambda\ni z\\\Lambda\ne L}}
(k_1(z,\Lambda))_2
\ge
\frac{c_q}{2}(n)_2
}
\]

for some paid endpoint `z`.

### Proof

CMR558 gives

\[
w_0(\Lambda)
\le
\binom{k_0(\Lambda)}3
=
\frac{(k_0(\Lambda))_3}{6}
\]

and

\[
w_1(z,\Lambda)
\le
\binom{k_1(z,\Lambda)}2
=
\frac{(k_1(z,\Lambda))_2}{2}.
\]

Sum the exact support-line decompositions.  The final alternatives follow from
the rank polarization CMR559. ∎

Thus a static selector carries a fixed positive line-energy density, not only
a large atom count.

## 2. Dyadic primitive-height localization

Write every nonaxis line `\Lambda` in primitive direction form and put

\[
K(\Lambda)=\max\{|u_\Lambda|,|v_\Lambda|\}.
\]

Let

\[
B=\lceil\log_2m\rceil.
\]

For dyadic `H`, let `J_{0,H}` count rank-zero supporting lines and let
`J_{1,H}(z)` count rank-one supporting lines through `z` satisfying

\[
H\le K(\Lambda)<2H.
\]

Every line in this band contains at most

\[
q_H=1+\left\lfloor\frac{m-1}{H}\right\rfloor
\]

parent-board cells.

### Theorem CMR575 — PROVED

If the rank-zero alternative of CMR559 holds, some dyadic `H` satisfies

\[
\boxed{
J_{0,H}
\frac{\binom{q_H}{3}}{(n)_3}
\ge
\frac{c_q}{2B}.
}
\]

If the rank-one alternative holds at endpoint `z`, some dyadic `H` satisfies

\[
\boxed{
J_{1,H}(z)
\frac{\binom{q_H}{2}}{(n)_2}
\ge
\frac{c_q}{4B}.
}
\]

### Proof

Partition the exact line-weight sums of CMR558 into at most `B` positive
height bands.  In the rank-zero case one band carries at least

\[
\frac1B\frac{V_0}{(n)_3}
\ge
\frac{c_q}{2B}.
\]

A line in that band supports at most `binom(q_H,3)` rank-zero atoms.  The
rank-one proof is identical, using

\[
M_1(z)/(n)_2\ge c_q/4
\]

and the two-cell capacity. ∎

The selected height band is fixed by the canonical selector profile.

## 3. Explicit line-count bounds

### Theorem CMR576 — PROVED

Assume `m>=20`.  In the rank-zero case the band from CMR575 satisfies

\[
\boxed{
J_{0,H}
>
\frac{5c_q}{11}
\frac{H^3}{B}
\ge
\frac{H^3}{12B}.
}
\]

Assume `m>=7`.  In the rank-one case the band from CMR575 satisfies

\[
\boxed{
J_{1,H}(z)
\ge
\frac{c_q}{16}
\frac{H^2}{B}
\ge
\frac{11}{960}
\frac{H^2}{B}.
}
\]

### Proof

The occupancy estimate proved inside CMR354 is

\[
\frac{\binom{q_H}{3}}{(n)_3}
<
\frac{11}{10H^3}
\]

for a positive-contribution rank-zero band when `m>=20`.  Substitute it into
CMR575 and use `c_q>=11/60`.

For rank one, positive contribution gives `q_H>=2`.  For `m>=7` and dyadic
`H`,

\[
\frac{\binom{q_H}{2}}{(n)_2}
\le
\frac4{H^2}.
\]

Substitute this into CMR575 and again use `c_q>=11/60`. ∎

The powers three and two are the exact factorial-moment scales of rank-zero
and rank-one atoms.

## 4. Heavy lines have low primitive height

### Theorem CMR577 — PROVED

Let a nonaxis line of primitive height `K` contain `r>=2` parent-board cells.
Then

\[
\boxed{
K\le\frac{m-1}{r-1}.
}
\]

Consequently:

1. a rank-one line supporting `A` atoms and containing at least `r_1` involved
   cells satisfies
   \[
   \boxed{K\le\frac{m-1}{r_1-1}};
   \]
2. a rank-zero line supporting `A` atoms and containing at least `r_0` involved
   cells satisfies
   \[
   \boxed{K\le\frac{m-1}{r_0-1}}.
   \]

The cell lower bounds may be taken from CMR561--CMR562.

### Proof

Successive integer points on a primitive line differ by a primitive vector
whose largest coordinate magnitude is `K`.  Among `r` ordered board points,
the extreme points differ by at least `(r-1)K` in one coordinate.  That
difference is at most `m-1`. ∎

Thus every heavy fixed conflict line is automatically a low-height quotient
and carry object.

## 5. Rank-zero height bands enter the CMR355--CMR358 conversion

Fix the rank-zero band from CMR575.  Choose one profile triple on each of its
`J=J_{0,H}` distinct lines and one compatible pair from every triple.

### Theorem CMR578 — PROVED

Put

\[
A=\lceil\sqrt J\rceil.
\]

At least one of the following holds.

1. **Matching-vertex fan.**  One source or target matching vertex is incident
   with at least `A` selected lines.
2. **Common-signature compatible family.**  There is a matching-compatible
   pair family of size at least
   \[
   R=
   \left\lfloor\frac{J}{4A}\right\rfloor.
   \]
   It contains a subfamily of size at least
   \[
   M=
   \left\lfloor\frac{R}{g(p+1)}\right\rfloor
   \]
   with one common first-separation depth and projective direction.  That
   subfamily yields either
   - one full prefix cell carrying at least
     \[
     \boxed{\left\lceil\frac{M}{m^{2/3}}\right\rceil}
     \]
     pairs; or
   - more than
     \[
     \boxed{\frac{M}{m^{2/3}}}
     \]
     occupied full prefix cells.

### Proof

The chosen pairs determine distinct real lines.  Apply CMR355 with threshold
`A`.  In the nonfan branch apply CMR356 and then CMR358. ∎

The first branch is an existing matching-vertex wall.  The final branches are
executable heavy-prefix geometry or a dispersed absolute carry-cell family.

## 6. Rank-one bands are fixed paid-endpoint fans

### Theorem CMR579 — PROVED

In the rank-one branch of CMR559, at least one of the following holds.

1. One supporting secant line is heavy and has the low-height bound of CMR577.
2. The CMR564 secant-star branch gives pairwise disjoint residual arms through
   one fixed paid endpoint.
3. The dyadic band from CMR575 contains at least the number of fixed
   paid-endpoint secants in CMR576, all through the same endpoint and all in one
   primitive-height band.

### Proof

The first two alternatives are CMR562 and CMR564.  Apply CMR577 to the heavy
line.  The third conclusion is CMR575--CMR576, noting that the endpoint was
fixed before the height partition. ∎

## 7. Canonical collateral-to-carry endpoint

### Corollary CMR580 — PROVED

Every static canonical selector reaches one of the following fixed endpoints.

1. A low-height heavy rank-one secant through a paid endpoint.
2. A paid-endpoint secant star with disjoint residual arms.
3. A low-height heavy rank-zero residual line.
4. A residual matching-vertex fan.
5. A full prefix cell carrying many common-signature line pairs.
6. A dispersed family of full prefix cells carrying common-signature line
   pairs.
7. The disjoint rank-zero packing endpoint already paid by CMR569--CMR573.

All lines, endpoints, atom supports, height bands, first-separation signatures,
and prefix cells retain their canonical selector owner.

### Proof

Apply CMR559.  Use CMR577 and CMR579 in the rank-one case.  In the rank-zero
case use CMR565--CMR568 and CMR578; the disjoint-packing subbranch is paid by
CMR569--CMR573. ∎

## 8. Revised frontier

The static canonical-collateral branch is fully spliced into previously proved
prime-power objects.

- Heavy profile lines have explicit low primitive height.
- Rank-one line banks are fixed paid-endpoint secant stars.
- Rank-zero line banks convert to matching walls, executable heavy prefix cells,
  dispersed carry cells, or the already-paid deletion packing.
- Every charge retains its selector owner.

The remaining work is dynamic payment for reuse of these fixed wall/prefix/
carry certificates and for the persistent canonical-edge branch of CMR557.
The required progress alternatives remain protected-reserve depletion,
full-token return, deletion ancestry, strict potential decrease, or envelope
expansion.

No all-`n` theorem is claimed.  Factorial-moment identities, dyadic
localization, occupancy constants, low-height bounds, and the quantitative
CMR355--CMR358 splice are checked in
[`scripts/verify_prime_power_canonical_collateral_carry.py`](../scripts/verify_prime_power_canonical_collateral_carry.py).

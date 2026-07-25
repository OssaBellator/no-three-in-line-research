# Canonical collateral line energy feeds matching walls, heavy prefixes, or dispersed carry cells

CMR558--CMR563 classify every static canonical selector profile as a heavy
line, a paid-endpoint secant star, a cell-disjoint residual bank, or a residual
repeated-cell star.  This chapter makes the connection to the existing
prime-power geometry quantitative.

The fixed profile has an exact factorial-moment line energy.  Dyadic
localization by primitive line height then gives many fixed line signatures in
one height band.  For rank-zero mass, the CMR355--CMR358 conversion applies
verbatim: choose one compatible pair on each line, then obtain a matching-
vertex fan or a matching-compatible family with common first-separation depth
and projective direction, followed by a heavy full-prefix cell or many occupied
full-prefix cells.

Rank-one mass is even more localized.  Its distinct supporting lines already
form a fan through one paid endpoint.  If the mass instead concentrates on one
line, the line has quantitatively low primitive height.

Fix a static canonical selector signature `\Sigma` in an inherited envelope of
side

\[
m=p^g,
\qquad
n=m-2\ge5,
\]

with paid pair `Z`, paid line `L`, and static threshold `q>=4`.  Put

\[
c_q=\frac{11}{30}\left(1-\frac2q\right).
\]

Use the line-profile notation `r_K,T_0(K),T_1(z,K)` from CMR559.

## 1. Fixed factorial-moment line energy

### Theorem CMR564 — PROVED

The rank-zero and rank-one profiles satisfy

\[
\boxed{
\sum_K (r_K)_3
\ge
6V_0
}
\]

and, for every paid endpoint `z`,

\[
\boxed{
\sum_{\substack{K\ni z\\K\ne L}}(r_K)_2
\ge
2V_1(z).
}
\]

Consequently a static profile satisfies at least one of

\[
\boxed{
\sum_K(r_K)_3
\ge
3c_q(n)_3
}
\]

or

\[
\boxed{
\sum_{\substack{K\ni z\\K\ne L}}(r_K)_2
\ge
\frac{c_q}{2}(n)_2
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

Sum the inequalities and use the exact line decompositions of `V_0` and
`V_1(z)`.  The final alternatives follow from CMR558. ∎

Thus the static selector carries a fixed positive line-energy density; it is
not merely a large atom count.

## 2. Dyadic primitive-height localization

Write every nonaxis line in primitive direction form and let

\[
K(K)=\max\{|u_K|,|v_K|\}
\]

be its primitive height.  Put

\[
B=\lceil\log_2m\rceil.
\]

For dyadic `H`, let `\mathfrak L_{0,H}` be the rank-zero supporting lines with

\[
H\le K(K)<2H,
\]

and let `\mathfrak L_{1,H}(z)` be the corresponding rank-one lines through
`z`.  Write their cardinalities as `J_{0,H}` and `J_{1,H}(z)`.

A line in this band contains at most

\[
q_H=1+\left\lfloor\frac{m-1}{H}\right\rfloor
\]

parent-board cells.

### Theorem CMR565 — PROVED

If the rank-zero alternative of CMR558 holds, some dyadic `H` satisfies

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

Partition the exact line sums of CMR559 into at most `B` positive dyadic
height bands.  In the rank-zero case, one band carries at least

\[
\frac1B\frac{V_0}{(n)_3}
\ge
\frac{c_q}{2B}.
\]

Every line in the band contributes at most `binom(q_H,3)/(n)_3`.  The rank-one
proof is identical, using

\[
V_1(z)/(n)_2\ge c_q/4
\]

and the two-cell occupancy bound. ∎

The height-band label is fixed by the canonical selector profile.

## 3. Explicit line-count bounds

### Theorem CMR566 — PROVED

Assume `m>=20`.  In the rank-zero case, the band from CMR565 satisfies

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

Assume `m>=7`.  In the rank-one case, the band from CMR565 satisfies

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

For rank zero, the occupancy estimate proved in CMR354 is

\[
\frac{\binom{q_H}{3}}{(n)_3}
<
\frac{11}{10H^3}
\]

for every positive-contribution band when `m>=20`.  Substitute it into CMR565
and rearrange.  Since `c_q>=11/60`, the second bound follows.

For rank one, positive contribution implies `q_H>=2`.  Also

\[
q_H\le1+\frac{m-1}{H}.
\]

For `m>=7` and dyadic `H`, the elementary estimate

\[
\frac{\binom{q_H}{2}}{(n)_2}
\le
\frac4{H^2}
\]

holds.  Substitute into CMR565.  Again use `c_q>=11/60`. ∎

The rank-zero exponent three and rank-one exponent two are the exact
factorial-moment scales of their profile atoms.

## 4. Heavy lines have low primitive height

### Theorem CMR567 — PROVED

Let a nonaxis line of primitive height `K` contain `r>=2` parent-board cells.
Then

\[
\boxed{
K\le\frac{m-1}{r-1}.
}
\]

Consequently:

1. a rank-one line supporting `H` profile atoms has
   \[
   \boxed{
   K\le
   \frac{m-1}{\rho_2(H)-1};
   }
   \]
2. a rank-zero line supporting `H` profile atoms has
   \[
   \boxed{
   K\le
   \frac{m-1}{\rho_3(H)-1}.
   }
   \]

### Proof

Successive integer points on a primitive line differ by a primitive vector
whose largest coordinate magnitude is `K`.  Among `r` ordered board points,
the extreme points differ by at least `(r-1)K` in one coordinate.  That
difference is at most `m-1`, proving the first inequality.  Apply the occupancy
conclusions of CMR560 and CMR561. ∎

Thus a heavy canonical collision line is automatically a low-height line,
which is exactly the input expected by quotient and carry analysis.

## 5. Rank-zero height bands enter the CMR355--CMR358 conversion

Fix the rank-zero band supplied by CMR565 and choose one profile triple on each
of its `J=J_{0,H}` distinct lines.  Choose one compatible pair from every
triple.

### Theorem CMR568 — PROVED

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
   with one common first-separation depth and one common projective direction.
   That subfamily then yields either
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

The chosen pairs lie on distinct real lines.  Apply CMR355 with threshold
`A`.  In the nonfan branch apply CMR356 to extract a common
first-separation/projective-direction signature and then CMR358 to obtain the
heavy-cell or dispersed-cell conclusion. ∎

The first branch is an existing matching-vertex wall.  The last two branches
are respectively executable heavy-prefix geometry and a dispersed absolute
carry-cell family.

## 6. Rank-one bands are already paid-endpoint fans

### Theorem CMR569 — PROVED

In the rank-one branch of CMR558, at least one of the following holds.

1. One supporting secant line is heavy and therefore has the low-height bound
   of CMR567.
2. There are many distinct supporting lines through one fixed paid endpoint
   `z`; choosing one atom on each line gives a repeated-cell secant star with
   pairwise disjoint residual arms.
3. More quantitatively, the dyadic band from CMR565 contains at least the
   number of fixed paid-endpoint secants in CMR566, all through the same `z`
   and all in one primitive-height band.

### Proof

The first two alternatives are CMR560.  The low-height conclusion is CMR567.
The third is CMR565--CMR566, noting that the endpoint `z` was fixed before the
height partition. ∎

## 7. Canonical collateral-to-carry endpoint

### Corollary CMR570 — PROVED

Every static canonical selector signature reaches one of the following fixed
geometric endpoints.

1. A low-height heavy rank-one secant through a paid endpoint.
2. A paid-endpoint secant star with disjoint residual arms.
3. A low-height heavy rank-zero residual line.
4. A residual matching-vertex fan.
5. A full prefix cell carrying many common-signature line pairs.
6. A dispersed family of full prefix cells carrying common-signature line
   pairs.

All lines, paid endpoints, atom supports, height bands, first-separation
signatures, and prefix cells are owned by the canonical selector signature.

### Proof

Apply CMR558.  Use CMR567 and CMR569 in the rank-one case.  In the rank-zero
case, use CMR561 for a direct heavy-line/star/bank endpoint, or use the dyadic
band CMR565 followed by CMR568. ∎

## 8. Revised frontier

The static canonical-collateral branch is now fully spliced into previously
proved prime-power objects.  It no longer ends at an anonymous fixed conflict
profile.

- Heavy profile lines have explicit low primitive height.
- Many rank-one lines are a fixed paid-endpoint secant star.
- Many rank-zero lines convert to a matching-vertex wall, an executable heavy
  prefix cell, or dispersed carry cells.
- Every charge retains its canonical selector owner, so the selector-level
  no-double-counting ledger survives the geometric conversion.

The remaining work is dynamic payment for reuse of these fixed wall/prefix/
carry certificates and for the persistent canonical-edge branch of CMR557.
The required progress alternatives remain protected-reserve depletion,
full-token return, deletion ancestry, strict potential decrease, or envelope
expansion.

No all-`n` theorem is claimed.  Factorial-moment identities, dyadic
localization, occupancy constants, low-height bounds, and the quantitative
CMR355--CMR358 splice are checked in
[`scripts/verify_prime_power_canonical_collateral_carry.py`](../scripts/verify_prime_power_canonical_collateral_carry.py).

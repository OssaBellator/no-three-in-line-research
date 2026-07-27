# Packed secant loads give explicit rank-one multiplicity bounds

CMR1734--CMR1741 identify rank-one prescription multiplicity with a secant sum

\[
\sum_{\ell\ni x} C(h_B(\ell),2).
\]

The line heights through one response point partition the background points by
primitive direction. Convexity therefore gives an exact extremal packing bound:
for fixed background size and maximum line load, the largest possible secant sum
is obtained by filling as many directions as possible to the maximum height.

This removes the separate secant-direction count from the coarsest rank-one
multiplicity estimate and turns the remaining line-clean and owner-support
thresholds into explicit functions of two geometric parameters.

Fix integers `N>=0` and `H>=1`. Write

\[
N=qH+r,
\qquad
0\le r<H.
\]

Define

\[
\Phi(N,H)=qC(H,2)+C(r,2).
\]

## 1. Convex packing lemma

### Theorem CMR1742 -- PROVED

Let `h_1,...,h_s` be nonnegative integers satisfying

\[
0\le h_i\le H,
\qquad
\sum_i h_i=N.
\]

Then

\[
\boxed{
\sum_i C(h_i,2)
\le
\Phi(N,H).
}
\]

The bound is attained by `q` entries equal to `H`, one entry equal to `r` when
`r>0`, and all remaining entries zero.

### Proof

If `0<a<=b<H`, moving one unit from `a` to `b` changes the sum by

\[
C(a-1,2)+C(b+1,2)-C(a,2)-C(b,2)=b-a+1>0.
\]

Thus every non-extremal pair of positive entries can be made more unequal while
increasing the objective. Iteration fills entries to `H` one at a time, leaving
at most one positive remainder. The resulting vector has the displayed form and
value `Phi(N,H)`. ∎

This is the exact integer maximum, not an asymptotic relaxation.

## 2. Rank-one multiplicity from background size and height

Let `B` be a background point set of size `N`, fix a response point `x`, and
assume every line through `x` contains at most `H` background points.

### Theorem CMR1743 -- PROVED

\[
\boxed{
m(\{x\})\le\Phi(N,H).}
\]

### Proof

By CMR1738, rank-one multiplicity is the sum of `C(h_theta(x),2)` over primitive
directions through `x`. Every background point lies in exactly one such
direction class, so the heights sum to `N`, and each is at most `H`. Apply
CMR1742. ∎

The bound requires no separate estimate for the number of heavy directions.

## 3. Linear relaxation

### Theorem CMR1744 -- PROVED

\[
\boxed{
\Phi(N,H)
\le
\frac{(H-1)N}{2}.
}
\]

Consequently

\[
\boxed{
m(\{x\})\le\frac{(H-1)|B|}{2}.}
\]

### Proof

For every `0<=h<=H`,

\[
C(h,2)=h(h-1)/2\le h(H-1)/2.
\]

Sum over the direction classes. The packed value is the maximum among those
sums, so it obeys the same bound. ∎

The packed integer value should be used for exact certificates; the linear form
is convenient for symbolic comparisons.

## 4. Combined rankwise multiplicity caps

Assume every background line relevant to a rank-two prescription contains at
most `H_2` background points. Let `H_1` be the maximum background load on a line
through one response point.

### Theorem CMR1745 -- PROVED

The rankwise prescription multiplicities satisfy

\[
\boxed{
m_1\le\Phi(|B|,H_1),
\qquad
m_2\le H_2,
\qquad
m_3=1.
}
\]

### Proof

Use CMR1743 for rank one, CMR1735 for rank two, and CMR1734 for rank three. ∎

When one common background line-height cap `H` is available, one may take
`H_1=H_2=H`.

## 5. Explicit line-clean mass threshold

Put

\[
M_{\mathrm{pack}}
=
\Phi(|B|,H_1)C(d,1)
+H_2C(d,2)
+C(d,3).
\]

### Theorem CMR1746 -- PROVED

For every actual nonempty line-clean response host consistent with the displayed
background bounds,

\[
\boxed{
\mathbb E N_{\mathrm{off}}
\le
M_{\mathrm{pack}}.
}
\]

After `F_r` forced common prescriptions are removed, replace the three rank
masses by `C(d,r)-F_r`.

Hence destruction of load `D>M_pack` gives a strict-improvement response.

### Proof

Insert the multiplicity caps of CMR1745 into CMR1711--CMR1714. ∎

This is a fully explicit large-load threshold in terms of response side,
background size and two line-height caps.

## 6. Owner-support packed threshold

Let `A` be a possible-owner edge support with matching number `mu(A)`.

### Theorem CMR1747 -- PROVED

Expected new collateral owned in `A` is at most

\[
\boxed{
\mu(A)
\left[
\Phi(|B|,H_1)
+H_2(d-1)
+C(d-1,2)
\right].
}
\]

Destruction above this quantity gives a strict response whenever every retained
child owner lies in `A`.

### Proof

Insert CMR1745 into the owner-support closure CMR1726--CMR1727. ∎

A source/target cover size may replace `mu(A)`.

## 7. Integer slack and overflow alternatives

Define

\[
S_{\mathrm{pack}}
=
D-
\mu(A)
\left[
\Phi(|B|,H_1)+H_2(d-1)+C(d-1,2)
\right].
\]

### Theorem CMR1748 -- PROVED

1. `S_pack>0` is an exact integer sufficient condition for the owner-supported
   row to be a strict improvement.
2. If the condition fails, at least one of the following must hold:
   - the owner-support matching number is large;
   - the background line-height cap `H_2` is large;
   - the packed rank-one secant value `Phi(|B|,H_1)` is large;
   - the destroyed load is too small.
3. Under a rational response law, multiplication by the common denominator gives
   a strict integer certificate with the same sign.

### Proof

The first and third statements are CMR1747 and denominator clearing. The second
is the contrapositive decomposition of the displayed nonnegative upper bound. ∎

This identifies the exact geometric quantities requiring refinement after a
failed packed certificate.

## 8. Packed-secant endpoint

### Corollary CMR1749 -- PROVED

The coarsest geometric prescription-multiplicity compiler now uses only:

1. background size `|B|`;
2. a maximum rank-one secant line load `H_1`;
3. a maximum rank-two line load `H_2`;
4. the owner-support matching number or cover size; and
5. destroyed load.

Rank-one multiplicity is bounded by the exact packed value `Phi(|B|,H_1)`, rank
two by `H_2`, and rank three by one. Finer primitive-direction or component-rook
classes remain available whenever the packed bound is too weak. No all-`n`
theorem is claimed.

Convex packing, exact attainment, linear relaxation and the resulting line-clean
and owner-support thresholds are checked in
[`scripts/verify_prime_power_packed_secant_multiplicity.py`](../scripts/verify_prime_power_packed_secant_multiplicity.py).

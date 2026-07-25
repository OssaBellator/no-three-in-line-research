# Bernoulli-thinned packet corrections and strict sign

PX300--PX304 convert diffuse packet defects into either a clean-star child or a
matching `Q` of commuting correcting transpositions. This chapter supplies the
missing sign mechanism for the second outcome.

Activate the disjoint corrections independently. Old packet destruction is
linear in the activation probability. Every newly created collinear triple
uses new cells from at most three activated transpositions, so creation is a
polynomial of degree at most three. Therefore any positive first-order gap can
be isolated by sufficiently light thinning. The only obstruction to that gap
is a correction edge whose two prospective cells carry large rank-one or
same-edge rank-two load, which again decodes to a clean star unless the packet
mass is already linear-scale.

## 1. Bernoulli correction bank

Let `Q` be a matching in the packet correction graph of PX300. For
`e in Q`, let `tau_e` swap the two current target columns on the rows of `e`, and
let `w_e` be its old anchor-weighted packet destruction. Put

\[
W(Q)=\sum_{e\in Q}w_e.
\]

Choose each `e in Q` independently with probability `p` and execute all chosen
transpositions. They commute by PX301.

Classify every prospective new collinear triple by the number of distinct
correction edges whose new cells it uses. Let `C_u(Q)` be the number of such
certificates with support `u`, for `u=1,2,3`. For support one we allow the
upper-bound convention that fixed old cells from inactive correction edges are
present; this can only overcount creation.

### Theorem PX305 -- PROVED

For `0<=p<=1`,

\[
\boxed{
\mathbb E[\Phi(M_p)-\Phi(M)]
\le
-pW(Q)+pC_1(Q)+p^2C_2(Q)+p^3C_3(Q).
}
\]

### Proof

An old packet defect assigned to `e` survives exactly when `e` is inactive,
because no other correction edge touches its two selected cells. Thus the
expected designated old destruction is `pW(Q)`.

A new triple contains at most three selected cells and therefore new cells from
at most three disjoint correction edges. A certificate with support `u`
requires all those `u` edges to be active, an event of probability `p^u`.
Additional inactivity requirements only lower its probability. Sum over all
prospective certificates. Any other old triples destroyed by the move improve
the inequality. \(\square\)

## 2. First-order gap implies an actual improvement

### Corollary PX306 -- PROVED

If

\[
\boxed{g=W(Q)-C_1(Q)>0,}
\]

then some subset of `Q` gives a strict total decrease of `Phi`.

More explicitly, put `B=C_2(Q)+C_3(Q)`. If `B=0`, take `p=1`. Otherwise take

\[
\boxed{p=\min\left(1,\frac{g}{2B}\right).}
\]

Then

\[
\boxed{
\mathbb E[\Phi(M_p)-\Phi(M)]\le-\frac{pg}{2}<0.
}
\]

### Proof

For `p<=1`, the higher-order contribution is at most `p^2B`. The chosen value
satisfies `pB<=g/2` when `p<1`; when `p=1`, its definition implies `B<=g/2`.
Apply PX305. Negative expectation implies that at least one deterministic,
necessarily nonempty, activated subset strictly improves `Phi`. \(\square\)

Thus support-two and support-three collateral cannot block a positive
first-order gap.

## 3. Exact first-order load of one correction

Fix one correction edge `e={r,s}`. Let its two new packet cells be `f_e^1` and
`f_e^2`, and let `X_e` be the fixed point set obtained by deleting the two old
selected cells changed by `e`.

Define

\[
\mu_e(f)=
|\{\{x,y\}\subseteq X_e:f,x,y\text{ are collinear}\}|
\]

and

\[
\lambda_e=
|\{x\in X_e:f_e^1,f_e^2,x\text{ are collinear}\}|.
\]

### Theorem PX307 -- PROVED

The support-one creation load of `e` is exactly

\[
\boxed{
c_e=\mu_e(f_e^1)+\mu_e(f_e^2)+\lambda_e.
}
\]

Consequently

\[
\boxed{C_1(Q)=\sum_{e\in Q}c_e.}
\]

### Proof

Every triple created when only `e` is active contains at least one of its two
new cells. The possibilities are disjoint:

1. `f_e^1` and two points of `X_e`;
2. `f_e^2` and two points of `X_e`;
3. both new cells and one point of `X_e`.

These are counted by the three displayed terms. Because the correction edges
of `Q` are row-disjoint, a support-one new cell identifies its unique edge, so
summing over `e` has no duplication. \(\square\)

## 4. No candidate star bounds the linear coefficient

Let `K` majorize all relevant line occupancies in the following sense.

- For each prospective new cell, every line through it contains at most `K`
  fixed points from `X_e`.
- The line through the two new cells of one correction contains at most `K`
  fixed points.
- The selected-point star extraction of PX303 uses the same upper bound `K` on
  eligible noncentre points per line.

### Theorem PX308 -- PROVED

Fix an integer `T>=1`. If no prospective new cell of a correction in `Q`
centres an endpoint-disjoint secant star of order `T`, then

\[
\boxed{c_e<K(2T+1)\quad\text{for every }e\in Q}
\]

and hence

\[
\boxed{C_1(Q)<|Q|K(2T+1).}
\]

### Proof

Apply PX228 with the fixed set `X_e`. Absence of a star of order `T` gives
`mu_e(f_e^i)<KT` for both new cells. The pair-line term satisfies
`lambda_e<=K`. Insert these bounds into PX307 and sum. \(\square\)

## 5. Quantitative packet strict-sign-or-child theorem

### Theorem PX309 -- PROVED

Let the packet correction graph have total old defect mass `D_pkt(M)`. For
integers `R,T>=1`, at least one of the following occurs.

1. A selected point centres a clean star of order at least `R/K`.
2. A prospective packet cell centres a clean star of order at least `T`.
3. There is a subset of commuting packet corrections which strictly lowers the
   full triple potential `Phi`.
4. The old packet mass satisfies

   \[
   \boxed{
   D_{\rm pkt}(M)
   \le
   \frac{(2R-1)hK(2T+1)}2.
   }
   \]

### Proof

Apply PX304 at threshold `R`. Its high-degree outcome gives item 1. Otherwise
there is a correction matching `Q` with

\[
W(Q)\ge\frac{D_{\rm pkt}(M)}{2R-1}
\]

and `|Q|<=h/2`. If item 2 fails, PX308 gives

\[
C_1(Q)<\frac h2K(2T+1).
\]

If item 4 also fails, then `W(Q)>C_1(Q)`, and PX306 gives item 3. \(\square\)

This is the strict-sign-or-child interface for packet mass, up to an explicit
linear-scale residual.

### Corollary PX310 -- PROVED

Assume `D_pkt(M)>=12hK^2` and put

\[
T=
\left\lfloor
\sqrt{\frac{D_{\rm pkt}(M)}{12hK^2}}
\right\rfloor,
\qquad
R=KT.
\]

Then either the full triple potential has a strict improving correction subset,
or a selected point or prospective packet cell centres a clean star of order at
least

\[
\boxed{
T=
\left\lfloor
\sqrt{\frac{D_{\rm pkt}(M)}{12hK^2}}
\right\rfloor.
}
\]

### Proof

Here `T>=1`. The residual bound in PX309 is strictly smaller than

\[
3hK^2T^2
\]

because `2KT-1<2KT` and `2T+1<=3T`. By the definition of `T`,

\[
3hK^2T^2\le D_{\rm pkt}(M)/4<D_{\rm pkt}(M),
\]

so item 4 is impossible. The first three outcomes give the conclusion. \(\square\)

The unresolved packet range is therefore reduced to

\[
\boxed{D_{\rm pkt}(M)<12hK^2.}
\]

For bounded line occupancy this is linear in the block order. Large diffuse
packet mass now satisfies the exact strict-sign-or-clean-star interface required
by PX280.

## 6. Verification

Run

```bash
python scripts/verify_product_packet_bernoulli_strict_sign.py
```

The verifier enumerates Bernoulli activation subsets, checks the degree-three
expectation polynomial, validates the explicit choice of `p`, confirms the
single-edge first-order decomposition on finite point configurations, and tests
the constants in PX309--PX310.

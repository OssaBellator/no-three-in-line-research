# Secant-star carry dispersion

This chapter treats the secant-star output of the common-ratio conversion theorem. Together with the aligned-anchor carry-cell theorem, it converts every non-improving paid bank into explicit growth of carry complexity or a perfect-affine exception.

Throughout, `p` is an odd prime and

\[
H_c=\{(x,\langle c/x\rangle_p):1\le x<p\}.
\]

## 1. Product-carry levels

For a point

\[
P=(x,\langle c/x\rangle_p)\in H_c,
\]

define its product carry

\[
\kappa_c(P)
=
\frac{x\langle c/x\rangle_p-c}{p}.
\]

Thus

\[
xy=c+p\kappa_c(P)
\]

as an exact integer identity.

For an integer `j`, let

\[
L_{c,j}
=
\{(x,y)\in H_c:xy=c+pj\}.
\]

Define

\[
\Delta_p
=
\max_{1\le N<p^2}\tau(N).
\]

### Lemma SC1 — PROVED

Every product-carry level satisfies

\[
\boxed{|L_{c,j}|\le\tau(c+pj)\le\Delta_p.}
\]

Consequently,

\[
\boxed{\Delta_p=p^{o(1)}.}
\]

### Proof

Every point of `L_{c,j}` is an ordered factorisation

\[
xy=c+pj
\]

with `1<=x,y<p`. Choosing `x` determines `y`, so the number of points is at most the number of positive divisors of `c+pj`. The final statement is the classical divisor bound. \(\square\)

## 2. Carry signatures in one secant star

Fix a candidate point `Z` and two hyperbola channels `H_b,H_c`. Let `E` be a family of real-collinear endpoint-disjoint pairs

\[
\{P,Q\},
\qquad
P\in H_b,
\quad
Q\in H_c,
\]

whose joining lines all pass through `Z`.

The **product-carry signature** of such a pair is

\[
\bigl(\kappa_b(P),\kappa_c(Q)\bigr).
\]

When `b=c`, the signature is treated as an unordered pair of carry levels.

### Theorem SC2 — PROVED

If `s(E)` is the number of product-carry signatures represented by `E`, then

\[
\boxed{|E|\le\Delta_p\,s(E).}
\]

Equivalently,

\[
\boxed{s(E)\ge\frac{|E|}{\Delta_p}.}
\]

Without the endpoint-disjoint assumption, the weaker bound

\[
|E|\le\Delta_p^2s(E)
\]

always holds.

### Proof

Fix a signature `(j,k)`. All first endpoints lie in `L_{b,j}` and all second endpoints lie in `L_{c,k}`. Because the pairs are endpoint-disjoint, their number is at most

\[
\min\{|L_{b,j}|,|L_{c,k}|\}
\le\Delta_p.
\]

For a same-channel diagonal signature, the same conclusion follows because an endpoint-disjoint matching on `L_{b,j}` has at most `|L_{b,j}|/2` edges.

Summing over represented signatures proves the first bound. Without disjointness, a fixed level pair supports at most the Cartesian-product bound `Delta_p^2`. \(\square\)

The theorem is deliberately independent of the candidate point and the line geometry. It uses only the exact integer product carries forced by the standard lift.

## 3. Combined alternating carry transition

Return to a paid common-ratio bank with:

- `m` disjoint rectangle blocks;
- current destroyed incidence `D`;
- `q` ambient hyperbola channels.

The common-ratio conversion theorem gives either an improving rectangle, a secant star, or an aligned-anchor class.

For an aligned-anchor class, use the notation of the aligned carry-cell theorem:

- `s_nd` is the number of nondegenerate aligned carry signatures;
- `E_deg` is the number of anchors in degenerate, perfectly aligned signatures;
- `mathfrak d(p)=p^{o(1)}` is the per-signature divisor bound.

### Theorem SC3 — PROVED

At least one of the following holds.

1. **Improvement.** Some admissible common-ratio rectangle strictly lowers the triple potential.

2. **Secant-star carry dispersion.** There is a switched candidate point and a fixed outside channel pair supporting at least
   \[
   \boxed{
   \frac{D}{4m q(q+1)\Delta_p}
   }
   \]
   distinct product-carry signatures.

3. **Aligned carry dispersion.** Some aligned-anchor class has at least
   \[
   \boxed{
   \frac{D}{8q\mathfrak d(p)}
   }
   \]
   nondegenerate carry signatures.

4. **Perfect affine alignment.** At least
   \[
   \boxed{\frac{D}{8q}}
   \]
   distinct aligned anchors lie in degenerate signatures and are exactly affine-interpolated between their switched endpoints.

### Proof

If the secant-star alternative of the conversion theorem occurs, it supplies at least

\[
\frac{D}{2m q(q+1)}
\]

outside pairs through one candidate point and one channel pair. The endpoint-disjoint extraction loses at most a factor two, leaving

\[
|E|\ge\frac{D}{4m q(q+1)}.
\]

Apply Theorem SC2.

If the aligned-anchor alternative occurs, its multiplicity satisfies

\[
\Lambda\ge\frac{D}{4q}.
\]

The aligned carry-cell theorem gives

\[
\Lambda\le\mathfrak d(p)s_{nd}+E_{deg}.
\]

Therefore either

\[
E_{deg}\ge\frac D{8q}
\]

or

\[
\mathfrak d(p)s_{nd}\ge\frac D{8q}.
\]

This proves the remaining alternatives. \(\square\)

## 4. What this changes

The two collateral quantities from the weighted conversion theorem are now replaced by explicit carry outputs:

\[
\boxed{
\text{paid bank}
\Longrightarrow
\text{improvement, carry dispersion, or perfect alignment}.
}
\]

Neither a high secant star nor a high aligned-anchor class can remain an unlabelled obstruction.

The remaining termination problem is now:

> Construct a monotone potential for alternating closure that charges newly created product-carry and coordinate-carry signatures, and prove that repeated carry dispersion either exhausts the available signature budget or enters a perfect-alignment/subgroup-coset exception that can be absorbed explicitly.

This is narrower than controlling `Theta` and `Lambda` directly. The required potential must combine:

- syndrome incidence;
- active row/column blocks;
- multiplicative quotient complexity;
- product-carry signature count;
- aligned coordinate-carry signature count;
- mass in perfect-interpolation cells.

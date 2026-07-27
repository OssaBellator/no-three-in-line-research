# Geometric formulas determine prescription multiplicity

CMR1710--CMR1733 isolate prescription multiplicity as the remaining correction
between distinct matching prescriptions and genuinely new geometric credits.
For collinear triples, that multiplicity has an exact elementary form.

Rank three is automatically injective. Rank two multiplicity is the background
point load on one determined line. Rank one multiplicity is the number of
background pairs lying with the response point on a common line, equivalently a
sum of `C(h,2)` over background secants through that point.

These formulas connect the new multiplicity frontier directly to the existing
line-height, primitive-direction, owner and support classes.

Let `B` be a finite background point set and `U` a disjoint finite response point
set in the real affine plane. A candidate triple is a three-element collinear
set `T subseteq B union U` containing at least one response point. Its response
prescription is

\[
P(T)=T\cap U.
\]

For a fixed nonempty prescription `P`, let `m(P)` be the number of candidate
triples with response prescription exactly `P`.

## 1. Rank-three prescriptions are injective

### Theorem CMR1734 -- PROVED

If `|P|=3`, then

\[
\boxed{m(P)\in\{0,1\}.}
\]

For every compatible collinear rank-three prescription,

\[
\boxed{m(P)=1.}
\]

### Proof

A candidate triple has exactly three points. If all three are response points,
the triple is the prescription itself. It exists exactly when those three points
are distinct and collinear. ∎

Thus the rank-three multiplicity cap in CMR1711 and CMR1726 is always `m_3=1`.

## 2. Exact rank-two line-load formula

Let `P={x,y}` contain two distinct response points and let `ell(x,y)` be their
unique real line.

### Theorem CMR1735 -- PROVED

\[
\boxed{
m(P)=|B\cap\ell(x,y)|.
}
\]

### Proof

A candidate triple with response prescription `{x,y}` has one background point
`b`. It is collinear exactly when `b` lies on the unique line through `x,y`.
Every such background point gives one distinct triple, and no other background
point does. ∎

Consequently any background line-load bound `H_2` gives the uniform rank-two
multiplicity cap

\[
\boxed{m_2\le H_2.}
\]

## 3. Exact rank-one secant formula

Fix a response point `x`. For every real line `ell` through `x`, put

\[
h_B(\ell)=|B\cap\ell|.
\]

### Theorem CMR1736 -- PROVED

\[
\boxed{
m(\{x\})
=
\sum_{\ell\ni x}C(h_B(\ell),2),
}
\]

where only lines with `h_B(ell)>=2` contribute.

### Proof

A candidate triple with sole response point `x` is obtained by choosing an
unordered pair `{b_1,b_2}` of background points collinear with `x`. The pair lies
on a unique line through `x`. Conversely every pair counted by
`C(h_B(ell),2)` produces one distinct triple. Different lines through `x` cannot
contain the same unordered background pair. ∎

The formula counts actual geometric triples, not merely distinct response
prescriptions.

## 4. Uniform line-load and secant-count bounds

Suppose every line through `x` contains at most `H_1` background points, and let
`L_x` be the number of lines through `x` containing at least two background
points.

### Theorem CMR1737 -- PROVED

\[
\boxed{
m(\{x\})\le L_x C(H_1,2).}
\]

Also, without any line-load information,

\[
\boxed{
m(\{x\})\le C(|B|,2).}
\]

### Proof

Apply the bound `h_B(ell)<=H_1` termwise in CMR1736. The second inequality counts
all unordered background pairs, only some of which are collinear with `x`. ∎

Thus rank-one multiplicity separates into a secant-direction count and a
background line-height bound.

## 5. Primitive-direction form

For a primitive unoriented direction `theta`, let `ell_theta(x)` be the unique
line through `x` of direction `theta`, and put

\[
h_\theta(x)=|B\cap\ell_\theta(x)|.
\]

### Theorem CMR1738 -- PROVED

\[
\boxed{
m(\{x\})
=
\sum_\theta C(h_\theta(x),2).}
\]

If at most `S_x` primitive directions have `h_theta(x)>=2` and every one has
height at most `H_1`, then

\[
\boxed{
m(\{x\})\le S_x C(H_1,2).}
\]

### Proof

Lines through a fixed point are in bijection with primitive unoriented
directions. Rewrite the sum of CMR1736 using this indexing and apply the uniform
bounds. ∎

This is the exact interface with primitive-height, direction-token and rooted
line classes already retained in the quotient.

## 6. Explicit line-clean rank-mass bound

Define

\[
M_1=\max_{x\in U}\sum_{\ell\ni x}C(h_B(\ell),2),
\]

and

\[
M_2=\max_{x\ne y\in U}|B\cap\ell(x,y)|.
\]

### Theorem CMR1739 -- PROVED

For every line-clean response law whose corrected off-line candidates use
background set `B`,

\[
\boxed{
\mathbb E N_{\mathrm{off}}
\le
M_1 C(d,1)
+M_2 C(d,2)
+C(d,3).
}
\]

After `F_r` forced common prescriptions are removed, the bound improves to

\[
\boxed{
M_1\bigl(C(d,1)-F_1\bigr)
+M_2\bigl(C(d,2)-F_2\bigr)
+\bigl(C(d,3)-F_3\bigr).
}
\]

### Proof

CMR1734 gives `m_3=1`, CMR1735 gives `m_2<=M_2`, and CMR1736 gives
`m_1<=M_1`. Insert these multiplicity caps into CMR1711--CMR1712. ∎

This turns the abstract line-clean multiplicities into explicit geometric line
statistics.

## 7. Owner-support specialization

Let `A` be a possible-owner edge support of matching number `mu(A)`.

### Theorem CMR1740 -- PROVED

The expected new collateral canonically owned in `A` is at most

\[
\boxed{
\mu(A)
\left[
M_1+M_2(d-1)+C(d-1,2)
\right].
}
\]

Therefore destruction above this quantity gives a strict response whenever all
retained child owners lie in `A`.

### Proof

Insert the exact multiplicity caps `m_1=M_1`, `m_2=M_2`, `m_3=1` into the
owner-support bound CMR1726. ∎

A source/target cover size may replace `mu(A)` by CMR1720.

## 8. Geometric multiplicity endpoint

### Corollary CMR1741 -- PROVED

The prescription-multiplicity frontier now has an exact normal form.

1. Rank three has multiplicity one.
2. Rank two multiplicity is one background line load.
3. Rank one multiplicity is one secant sum `sum C(h,2)` through the response
   point.
4. Primitive directions index the rank-one sum exactly.
5. These quantities insert directly into multiplicity-aware line-clean,
   selector, return and small-owner-support certificates.
6. A failed multiplicity certificate must therefore arise from a large
   background line load, many heavy secant directions, or insufficient destroyed
   credit.

The remaining geometric task is to bound `M_1` and `M_2` by the inherited
owner, line-height, token, prefix, carry and fixed-interface classes. No all-`n`
theorem is claimed.

Rank-one secant formulas, rank-two line loads, rank-three injectivity, primitive-
direction grouping and the resulting mass bounds are checked in
[`scripts/verify_prime_power_geometric_prescription_multiplicity.py`](../scripts/verify_prime_power_geometric_prescription_multiplicity.py).

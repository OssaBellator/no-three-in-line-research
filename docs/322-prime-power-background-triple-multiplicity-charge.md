# Background triples charge high prescription multiplicity

CMR1734--CMR1749 reduce geometric prescription multiplicity to background line
loads. A second exact reduction separates genuinely low-load geometry from
existing background-triple currency.

On a line containing `h` background points, rank-one multiplicity contributes
`C(h,2)` background pairs and rank-two multiplicity contributes `h` background
points. For `h>=3`, these quantities are controlled by the `C(h,3)` existing
background triples on the same line. Only a line with exactly two background
points contributes rank-one pair multiplicity without an existing background
triple, and only two rank-two point slots remain outside triple currency.

This chapter supplies bounded-congestion charge maps. The maps may enter a
potential proof only when the charged background triples are current labelled
credits and are not charged elsewhere without an explicit congestion allowance.

## 1. Local pair/triple inequalities

### Theorem CMR1750 -- PROVED

For every integer `h>=0`,

\[
\boxed{
C(h,2)
\le
\mathbf 1_{h=2}+3C(h,3),
}
\]

and

\[
\boxed{
h\le2+C(h,3).}
\]

### Proof

For `h=0,1,2`, inspect directly. For `h>=3`,

\[
C(h,2)=\frac{3}{h-2}C(h,3)\le3C(h,3).
\]

Also `h-2<=C(h,3)` for `h>=3`, with equality at `h=3`; this proves the second
inequality. ∎

The constants isolate the exact low-load exceptions.

## 2. Rank-one pair-only/triple-shadow decomposition

Fix a response point `x`. For every line `ell` through `x`, put

\[
h_\ell=|B\cap\ell|.
\]

Define the pair-only secant count

\[
S_2(x)=|\{\ell\ni x:h_\ell=2\}|
\]

and the background triple shadow

\[
T_3(x)=\sum_{\ell\ni x}C(h_\ell,3).
\]

### Theorem CMR1751 -- PROVED

The rank-one prescription multiplicity satisfies

\[
\boxed{
m(\{x\})\le S_2(x)+3T_3(x).}
\]

### Proof

CMR1736 gives `m({x})=sum C(h_ell,2)`. Apply the first inequality of CMR1750 on
every line and sum. ∎

Thus every rank-one multiplicity unit is either one pair-only secant or one of at
most three charges to a background triple on the same line.

## 3. Rank-two low-slot/triple-shadow decomposition

Let `P={x,y}` be a rank-two response prescription and let

\[
h=|B\cap\ell(x,y)|.
\]

### Theorem CMR1752 -- PROVED

\[
\boxed{
m(P)=h\le2+C(h,3).}
\]

### Proof

CMR1735 gives `m(P)=h`. Apply the second inequality of CMR1750. ∎

Hence at most two background-point choices per response pair remain outside
background-triple currency.

## 4. Uniform charged multiplicity caps

Suppose every relevant response point satisfies

\[
S_2(x)\le S,
\qquad
T_3(x)\le T_1,
\]

and every line determined by a rank-two response prescription satisfies

\[
C(|B\cap\ell|,3)\le T_2.
\]

### Theorem CMR1753 -- PROVED

One may take

\[
\boxed{
m_1\le S+3T_1,
\qquad
m_2\le2+T_2,
\qquad
m_3=1.}
\]

### Proof

Use CMR1751, CMR1752 and rank-three injectivity CMR1734. ∎

These caps may be compared with the packed-height caps of CMR1745 and the smaller
one used class by class.

## 5. Charged line-clean mass bound

### Theorem CMR1754 -- PROVED

For a line-clean response law consistent with the charged caps,

\[
\boxed{
\mathbb E N_{\mathrm{off}}
\le
(S+3T_1)C(d,1)
+(2+T_2)C(d,2)
+C(d,3).
}
\]

After forced common prescriptions are removed, replace `C(d,r)` by
`C(d,r)-F_r`.

If the actual response host is nonempty and destroyed load exceeds the resulting
quantity, one response is a strict improvement.

### Proof

Insert CMR1753 into the multiplicity-aware rank-mass closure
CMR1711--CMR1714. ∎

This bound is useful when existing background-triple currency is smaller than the
coarse line-height packing value.

## 6. Charged owner-support bound

Let `A` be a possible-owner edge support with matching number `mu(A)`.

### Theorem CMR1755 -- PROVED

Expected new collateral owned in `A` is at most

\[
\boxed{
\mu(A)
\left[
S+3T_1+(2+T_2)(d-1)+C(d-1,2)
\right].
}
\]

Destruction above this quantity gives a strict response whenever every retained
child owner lies in `A`.

### Proof

Insert CMR1753 into CMR1726--CMR1727. ∎

A source/target cover size may replace `mu(A)`.

## 7. Explicit bounded-congestion charge maps

### Theorem CMR1756 -- PROVED

For every background line of load `h>=3`, there exist deterministic finite maps
with the following properties.

1. Every unordered background pair on the line is assigned to one background
   triple on the line and one slot in `{1,2,3}`, with no triple-slot receiving
   more than one pair.
2. After reserving any two background points, every remaining background point
   is assigned to one background triple on the line, with no triple receiving
   more than one assigned point.

For a line of load two, its unique pair is retained as one pair-only secant. For
rank two, the first two point choices are retained as the two low slots.

### Proof

The first target set has size `3C(h,3)`, at least `C(h,2)` by CMR1750, so choose
an injection after fixing any deterministic order. The second target set has
size `C(h,3)`, at least `h-2`; order the points and triples and choose an
injection. The low-load statements are definitions of the residual classes. ∎

The maps preserve the supporting real line and may therefore retain line,
height, owner, token, prefix and carry provenance.

## 8. Charging endpoint and honesty rule

### Corollary CMR1757 -- PROVED

High prescription multiplicity now has a two-part normal form.

1. Rank-one multiplicity is pair-only secant currency plus background-triple
   currency with congestion at most three.
2. Rank-two multiplicity is two low point slots plus background-triple currency
   with congestion at most one.
3. Rank three remains injective.
4. Exact line-clean and owner-support bounds follow from the corresponding
   charged capacities.
5. Every use of background-triple currency in the final quotient must retain an
   explicit current credit label and the stated congestion; historical or
   already-spent triples may not be charged again.

The remaining geometric frontier is therefore reduced further to pair-only
secants, current background-triple shadows and their exact labelled ownership.
No all-`n` theorem is claimed.

Local binomial inequalities, point-system shadows, bounded-congestion cardinality
maps and the resulting line-clean/owner-support bounds are checked in
[`scripts/verify_prime_power_background_triple_multiplicity_charge.py`](../scripts/verify_prime_power_background_triple_multiplicity_charge.py).

# Harmonic packing cleans several intermediate-height bands at once

CMR376 gives exact target-specific completion for one dyadic primitive-height
band. The per-edge conflict degree has an exact height decomposition: at height
`K` there are `4 phi(K)` unoriented primitive directions. A family of heights
whose reciprocal sum is below `3/2` therefore remains within the
Joos--Mubayi--Smith maximum-degree threshold. In particular, any two dyadic
bands beginning at height at least five can be cleaned simultaneously.

Work in the duplicated-row target-specific model of CMR372--CMR376. Let
`\mathcal K` be a set of positive primitive heights and put

\[
W(\mathcal K)=\sum_{K\in\mathcal K}\frac1K.
\]

Let `\mathcal C_{\mathcal K}` and `\mathcal D_{\mathcal K}` be the main and
mixed candidate-only triple systems whose primitive heights lie in
`\mathcal K`.

## 1. Exact direction count at one height

### Theorem CMR385 — PROVED

For every integer `K>=1`, the number of unoriented primitive integer directions
`(u,v)` satisfying

\[
\max\{|u|,|v|\}=K
\]

is exactly

\[
\boxed{4\varphi(K)}.
\]

### Proof

Modulo simultaneous sign, choose either the representative with `u=K` and
`|v|<K`, or the representative with `v=K` and `|u|<K`. Each side contributes
`2\varphi(K)` primitive choices. For `K=1` the same formula gives the four
horizontal, vertical, and diagonal unoriented directions. ∎

## 2. Harmonic conflict-degree bound

### Theorem CMR386 — PROVED

Every represented candidate cell belongs to at most

\[
\boxed{
4\sum_{K\in\mathcal K}
\varphi(K)
\binom{\left\lfloor\frac{t-1}{K}\right\rfloor}{2}
}
\]

candidate-only triples of heights in `\mathcal K`. Consequently,

\[
\boxed{
\Delta(\mathcal C_{\mathcal K})
\le
2(t-1)^2W(\mathcal K).
}
\]

The same bound holds for the geometric mixed-conflict degree through one fixed
reserve edge.

### Proof

Fix one cell and one primitive direction of height `K`. The integral line
parameters for which the translated point remains in the board form an
interval containing at most

\[
1+\left\lfloor\frac{t-1}{K}\right\rfloor
\]

points. Hence at most

\[
\binom{\lfloor(t-1)/K\rfloor}{2}
\]

triples on that line contain the fixed cell. Sum over the `4\varphi(K)`
directions from CMR385. Finally use

\[
\varphi(K)\le K,
\qquad
\binom{x}{2}\le\frac{x^2}{2}.
\]

Copy labels do not change the represented-cell count, so the reserve-edge
statement is identical. ∎

## 3. Mixed boundedness for a harmonic height family

### Theorem CMR387 — PROVED

Fix `\eta>0`. Assume

\[
\min\mathcal K\ge t^\eta
\]

and

\[
W(\mathcal K)<\frac32.
\]

Choose fixed `\epsilon` below both `\eta/2` and the Joos--Mubayi--Smith
structural threshold. Then, for all sufficiently large `t`,

1. `\mathcal C_{\mathcal K}` is `(t,3,\epsilon)`-bounded;
2. `\mathcal D_{\mathcal K}` is
   `(t,3,\epsilon,\epsilon^4)` mixed-bounded.

### Proof

CMR386 gives

\[
\Delta(\mathcal C_{\mathcal K})
<3(t-1)^2<3t^2,
\]

which is (C2). Two represented cells determine one real line and hence one
primitive height, so the pair codegree of the union is still bounded by

\[
\frac{t}{\min\mathcal K}
\le t^{1-\eta}
\le t^{1-\epsilon}.
\]

This is (C3).

The mixed proof of CMR375 is unchanged. Every estimate using fixed-edge
conflict degree now uses CMR386 and remains below `3t^2`; every estimate using
a fixed represented pair keeps the same `t/min K` bound because one pair
determines one height. Row-copy conflicts are unchanged. Thus (E1)--(E6) hold
with the same positive power slack. ∎

## 4. Exact harmonic-family completion

### Theorem CMR388 — PROVED FROM JOOS--MUBAYI--SMITH

Under the hypotheses of CMR387, there exists a complete target-specific parent
permutation containing no candidate-only collinear triple whose primitive
height belongs to `\mathcal K`.

### Proof

Apply the mixed-bounded covering theorem exactly as in CMR376, using CMR373 for
the hosts and CMR387 for the main and mixed conflicts. Decode by CMR372. ∎

## 5. Two dyadic bands at once

For `H>=1`, put

\[
S_H=\sum_{K=H}^{2H-1}\frac1K.
\]

### Corollary CMR389 — PROVED

Let `H_1,H_2` be two distinct dyadic lower endpoints satisfying

\[
H_1,H_2\ge\max\{5,t^\eta\}.
\]

For all sufficiently large `t`, one complete target-specific parent permutation
avoids every candidate-only triple in both bands

\[
H_i\le\max\{|u|,|v|\}<2H_i,
\qquad i=1,2.
\]

### Proof

The sequence `S_H` is strictly decreasing because

\[
S_{H+1}-S_H
=
\frac1{2H}+
\frac1{2H+1}-\frac1H
=
-\frac1{2H(2H+1)}.
\]

At `H=5`,

\[
S_5
=
\frac15+\frac16+\frac17+\frac18+\frac19
=
\frac{1879}{2520}
<
\frac34.
\]

Therefore each selected dyadic band has harmonic weight below `3/4`, and their
union has weight below `3/2`. Apply CMR388. ∎

## 6. Revised scheduling endpoint

Exact completion is no longer restricted to one band: any harmonic packet of
weight below `3/2`, and in particular any two intermediate dyadic bands, can be
cleaned in one move. The total harmonic weight from height `t^eta` to order `t`
is still `Theta(log t)`, so a constant number of packets cannot cover all
intermediate heights. The remaining theorem is a packet-scheduling/no-return
statement, not a single-packet existence theorem.

No all-`n` theorem is claimed here. Direction counts, harmonic weights, and
finite band-degree inequalities are checked in
[`scripts/verify_prime_power_harmonic_band_packing.py`](../scripts/verify_prime_power_harmonic_band_packing.py).

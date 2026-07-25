# Harmonic packing cleans several intermediate-height bands at once

CMR376 gives exact target-specific completion for one dyadic primitive-height
band. At exact height `K` there are `4\varphi(K)` unoriented primitive
directions. A family of heights whose reciprocal sum is below `3/2` therefore
stays within the Joos--Mubayi--Smith maximum-degree threshold. In particular,
any two dyadic bands beginning at height at least five can be cleaned
simultaneously.

Work in the duplicated-row model of CMR372--CMR376. Let `\mathcal K` be a set
of positive primitive heights and put

\[
W(\mathcal K)=\sum_{K\in\mathcal K}\frac1K.
\]

Let `\mathcal C_{\mathcal K}` and `\mathcal D_{\mathcal K}` be the corresponding
main and mixed candidate-only triple systems.

## 1. Exact direction count

### Theorem CMR385 — PROVED

For every integer `K\ge1`, the number of unoriented primitive integer directions
with

\[
\max\{|u|,|v|\}=K
\]

is exactly

\[
\boxed{4\varphi(K)}.
\]

### Proof

Modulo simultaneous sign, choose either `u=K, |v|<K` or
`v=K, |u|<K`. Each side contributes `2\varphi(K)` primitive choices. The
formula also gives the four height-one directions. ∎

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
\le2(t-1)^2W(\mathcal K).
}
\]

The same bound holds for geometric mixed conflicts through one fixed reserve
edge.

### Proof

For one direction of height `K`, the admissible line parameters through a fixed
cell form an interval with at most

\[
1+\left\lfloor\frac{t-1}{K}\right\rfloor
\]

points. Hence at most

\[
\binom{\lfloor(t-1)/K\rfloor}{2}
\]

triples on that line contain the fixed cell. Sum over CMR385's directions, then
use `\varphi(K)\le K` and `\binom{x}{2}\le x^2/2`. Copy labels do not change the
represented-cell count. ∎

## 3. Mixed boundedness for a harmonic family

### Theorem CMR387 — PROVED

Fix `\eta>0`. Assume

\[
\min\mathcal K\ge t^\eta,
\qquad
W(\mathcal K)<\frac32.
\]

Choose fixed `\epsilon` below `\eta/2` and the structural threshold in the
Joos--Mubayi--Smith theorem. For all sufficiently large `t`,

1. `\mathcal C_{\mathcal K}` is `(t,3,\epsilon)`-bounded;
2. `\mathcal D_{\mathcal K}` is
   `(t,3,\epsilon,\epsilon^4)` mixed-bounded.

### Proof

CMR386 gives

\[
\Delta(\mathcal C_{\mathcal K})<3(t-1)^2<3t^2.
\]

Two represented cells determine one real line and one primitive height, so the
pair codegree of the union remains below

\[
\frac{t}{\min\mathcal K}
\le t^{1-\eta}
\le t^{1-\epsilon}.
\]

The mixed proof of CMR375 is unchanged: fixed-edge estimates use CMR386,
fixed-pair estimates use the same pair-codegree bound, and row-copy conflicts
are unchanged. Thus (E1)–(E6) retain positive power slack. ∎

## 4. Exact harmonic-family completion

### Theorem CMR388 — PROVED FROM JOOS--MUBAYI--SMITH

Under the hypotheses of CMR387, there exists a complete target-specific parent
permutation containing no candidate-only collinear triple whose primitive
height belongs to `\mathcal K`.

### Proof

Apply the mixed-bounded covering theorem as in CMR376, using CMR373 for the
hosts and CMR387 for the main and mixed conflict systems. Decode by CMR372. ∎

## 5. Two dyadic bands at once

For `H\ge1`, put

\[
S_H=\sum_{K=H}^{2H-1}\frac1K.
\]

### Corollary CMR389 — PROVED

Let `H_1,H_2` be distinct dyadic lower endpoints satisfying

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
\frac1{2H}+\frac1{2H+1}-\frac1H
=
-\frac1{2H(2H+1)}.
\]

Moreover,

\[
S_5
=
\frac15+\frac16+\frac17+\frac18+\frac19
=
\frac{1879}{2520}
<\frac34.
\]

Each selected band has harmonic weight below `3/4`; their union has weight
below `3/2`. Apply CMR388. ∎

Exact completion is therefore available for any harmonic packet of weight below
`3/2`, including any two intermediate dyadic bands. The total harmonic weight
from `t^\eta` to order `t` is still `\Theta(\log t)`, so a constant number of
packets cannot cover every intermediate height. The remaining theorem is a
packet-scheduling/no-return statement.

No all-`n` theorem is claimed here. Direction counts, harmonic weights, and
finite degree inequalities are checked in
[`scripts/verify_prime_power_harmonic_band_packing.py`](../scripts/verify_prime_power_harmonic_band_packing.py).

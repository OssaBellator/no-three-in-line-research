# Uniform local-bank theorem

## 1. Admissibility graph

Let \(B\) be a certified target batch, \(|B|=t\), and \(P\) a partner pool, \(|P|=p\). Define a bipartite graph \(\Gamma\) where \(e\in B\) is adjacent to \(f\in P\) when the corresponding rectangle switch is individually admissible at height at least \(H\).

Assume

\[
d_\Gamma(e)\ge(1-\delta)p
\quad(e\in B),
\]

and \(t\le\beta p\) with \(\delta+\beta<1\). Put

\[
K=(1-\delta-\beta)^{-1}.
\]

## 2. Spread injection

### Lemma L1 — PROVED

There is a distribution on matchings covering all targets such that any compatible set \(F\) of \(r\) prescribed assignments satisfies

\[
\Pr(F\subseteq Q)\le(K/p)^r.
\]

### Proof

Expose targets sequentially and choose uniformly among unused admissible partners. At every step at least

\[
(1-\delta)p-(t-1)\ge(1-\delta-\beta)p=p/K
\]

choices remain. Multiply conditional probabilities. ∎

## 3. Cell realisation multiplicity

### Lemma L2 — PROVED

Every grid cell is inserted by at most two target-partner assignments.

### Proof

A cell \((a,b)\) can be the cross-cell \((x_e,y_f)\) only for the unique target in column \(a\) and unique partner in row \(b\). It can be the other cross-cell \((x_f,y_e)\) only for the unique target in row \(b\) and unique partner in column \(a\). ∎

## 4. Anchor-load cap

Let \(Z\) be the set of possible inserted cells. For an unchanged selected point \(a\), define \(\lambda_H(a;Z)\) as the number of compatible unordered pairs \(\{z,z'\}\subseteq Z\) such that \(a,z,z'\) lie on a line of height at least \(H\).

Assume

\[
\lambda_H(a;Z)\le\Theta
\]

for every unchanged anchor.

### Lemma L3 — PROVED

The number \(A_2\) of anchored assignment-pair conflicts satisfies

\[
A_2\le8n\Theta.
\]

### Proof

A cell pair has at most four assignment-pair realisations by Lemma L2. There are at most \(2n\) anchors. ∎

## 5. Local-bank drift

### Theorem L4 — PROVED UNDER HYPOTHESES

Some simultaneous switch satisfies

\[
\Psi_H(S')\le
\Psi_H(S)-t
+
\frac{8K^2n\Theta}{p^2}
+
\frac{4K^2\ell_Ht}{p}
+
\frac{8K^3\ell_Ht^2}{p}.
\]

If

\[
p\ge\alpha n,
\quad
\Theta\le\eta n,
\quad
t\le\gamma H,
\]

with

\[
\eta\le\frac{\alpha^2}{64K^2},
\quad
H\ge\frac{64K^2}{\alpha},
\quad
\gamma\le\frac{\alpha}{128K^3},
\]

then

\[
\Psi_H(S')\le\Psi_H(S)-\frac58t.
\]

## 6. Remaining hypothesis

The theorem shifts the burden to two geometric regularity statements:

1. each certified target has a positive-density admissible partner set;
2. every unchanged anchor has scale-sensitive pair-shadow load \(O(n)\).

These are not known uniformly after arbitrary intermediate switches.

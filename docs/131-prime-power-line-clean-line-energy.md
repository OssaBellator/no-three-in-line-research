# Line-clean two-slice banks force a strict real-line energy

The universal line-clean bank CMR360 has a stronger probability law when the
two paid cells lie on two fixed matching vertices. This is the geometry of
width-two chords, width-three full triples, and source-source-target mixed-fan
families. An external real line can meet the paid support in at most two bank
cylinders, so its triple probability is controlled by its board occupancy.

Work in a parent board of size `t` and put

\[
n=t-2.
\]

Let `\mathcal L` be a line-clean family of size `m`. For every
`L\in\mathcal L`, suppose

\[
P_L=\{(x_1,a_L),(x_2,b_L)\},
\qquad x_1\ne x_2,
\]

where the `a_L` are pairwise distinct and the `b_L` are pairwise distinct.
Sample uniformly from the disjoint union of the `m` CMR360 derangement
cylinders. For a nonaxis real line `M`, let `s_M` be the number of compatible
available parent-board cells on `M`.

## 1. One-line atom

### Theorem CMR351 — PROVED

The probability that the sampled state contains at least one candidate-only
collinear triple on `M` is at most

\[
\boxed{
\frac{30}{11}
\left[
\frac{\binom{s_M}{3}}{(n)_3}
+
\frac{2}{m}\frac{\binom{s_M-1}{2}}{(n)_2}
\right].
}
\]

Binomial coefficients with upper argument below the lower one are zero.

### Proof

A line meets each fixed source slice in at most one cell. Since paid cells on
each slice are distinct across cylinders, at most one cylinder has its first
paid cell on `M`, and at most one has its second paid cell there.

In every cylinder, a triple on `M` disjoint from the paid pair requires three
residual derangement edges. There are at most `\binom{s_M}{3}` prescriptions,
each with probability at most `30/[11(n)_3]` by CMR332. In either exceptional
cylinder sharing one paid cell with `M`, a triple using that paid cell requires
two residual edges; there are at most `\binom{s_M-1}{2}` such prescriptions,
each with probability at most `30/[11(n)_2]`. Average over the `m` equal-size
cylinders. If `M=L` for one paid cylinder, line-cleaning makes its true
contribution zero, so the displayed estimate only overcounts. ∎

## 2. Frozen-bank line energy

Let `\mathfrak L` be the real lines supporting at least one candidate-only
triple in some bank state.

### Theorem CMR352 — PROVED

Assume every bank state is globally nonimproving and no bank state creates an
anchored certificate. Then

\[
\boxed{
\sum_{M\in\mathfrak L}
\left[
\frac{\binom{s_M}{3}}{(n)_3}
+
\frac{2}{m}\frac{\binom{s_M-1}{2}}{(n)_2}
\right]
\ge\frac{11}{30}.
}
\]

### Proof

Every state omits the selected old target endpoint. A globally nonimproving
state must therefore contain a replacement triple. Under the anchored-free
hypothesis it is candidate-only, so the line events cover the entire bank
probability space. Sum CMR351 and use the union bound. ∎

This is a strict target-versus-collateral inequality: the destroyed old target
forces positive real-line occupancy energy, with no rank-two contribution from
the paid line itself.

## 3. Dyadic height localization

Let

\[
K(M)=\max\{|u_M|,|v_M|\}
\]

be primitive height, and put

\[
B=\left\lceil\log_2t\right\rceil.
\]

For dyadic `H`, let `J_H` count lines with

\[
H\le K(M)<2H.
\]

Such a line has at most

\[
q_H=1+\left\lfloor\frac{t-1}{H}\right\rfloor
\]

board cells.

### Corollary CMR353 — PROVED

Some dyadic band satisfies

\[
\boxed{
J_H
\left[
\frac{\binom{q_H}{3}}{(n)_3}
+
\frac{2}{m}\frac{\binom{q_H-1}{2}}{(n)_2}
\right]
\ge\frac{11}{30B}.
}
\]

### Proof

Partition the positive-height lines in CMR352 into at most `B` dyadic bands.
One band contributes at least `1/B` of the energy. Replace every occupancy in
that band by the common upper bound `q_H`. ∎

## 4. Cubic line-signature lower bound

### Corollary CMR354 — PROVED

Assume

\[
t\ge20,
\qquad
m\ge t-9.
\]

Then the band from CMR353 contains at least

\[
\boxed{
J_H\ge
\frac{11}{90}\frac{H^3}{\lceil\log_2t\rceil}.
}
\]

### Proof

If `q_H\le2`, the band contains no candidate triple and cannot carry positive
CMR353 energy. Hence `H\le(t-1)/2`, and

\[
q_H\le\frac{3(t-1)}{2H}.
\]

For `t\ge20`,

\[
(n)_3\ge\left(\frac{4(t-1)}5\right)^3,
\]

which gives

\[
\frac{\binom{q_H}{3}}{(n)_3}<\frac{11}{10H^3}.
\]

Also

\[
\frac{2}{m}\frac{\binom{q_H-1}{2}}{(n)_2}
\le\frac{21}{20H^3}.
\]

The last inequality is equivalent to

\[
11t^3-264t^2+1041t-1124\ge0,
\]

which holds at `t=20` and thereafter because its first two derivatives are
positive. Thus the CMR353 bracket is below `3/H^3`; rearrangement proves the
claim. ∎

A frozen two-slice line-clean bank therefore forces

\[
J_H=\Omega\left(\frac{H^3}{\log t}\right)
\]

distinct replacement-line signatures in one height band. CMR355–CMR359 convert
this energy to matching-vertex walls, executable heavy prefix cells, or
dispersed absolute carry cells.

No all-`n` theorem is claimed here. The line atoms, dyadic localization, and
cubic lower bound are checked in
[`scripts/verify_prime_power_line_clean_energy.py`](../scripts/verify_prime_power_line_clean_energy.py).

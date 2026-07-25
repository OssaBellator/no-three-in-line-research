# Line-clean two-slice banks force a strict real-line energy

The universal line-clean bank of CMR347 has a stronger probability law when
the two paid cells lie on two fixed matching vertices.  This is exactly the
geometry of the width-two chords, the width-three full triples, and the
source-source-target mixed-fan families.  Any external real line can then meet
the paid support in at most two bank cylinders.  The probability that the
completed state contains a triple on that line is therefore controlled by the
cube of its board occupancy.

Work in a parent board of size `t` and put

\[
n=t-2.
\]

Let `\mathcal L` be a line-clean family of size `m`.  For every `L in
\mathcal L`, suppose the paid pair has the form

\[
P_L=\{(x_1,a_L),(x_2,b_L)\},
\qquad x_1\ne x_2,
\]

where the `a_L` are pairwise distinct and the `b_L` are pairwise distinct.
Sample uniformly from the disjoint union of the `m` line-clean derangement
cylinders.

For a nonaxis real line `M`, let `s_M` be the number of compatible available
parent-board cells on `M`.

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
\frac{2}{m}
\frac{\binom{s_M-1}{2}}{(n)_2}
\right].
}
\]

Binomial coefficients with an upper argument below the lower one are read as
zero.

### Proof

The line `M` meets each fixed source slice in at most one cell.  Since the paid
cells on each slice are distinct across `L`, at most one cylinder has its first
paid cell on `M`, and at most one cylinder has its second paid cell on `M`.
Thus at most two cylinders share a paid cell with `M`.

In every cylinder, candidate triples on `M` which avoid the paid pair use three
residual derangement cells.  There are at most `binom(s_M,3)` such
prescriptions, each with probability at most

\[
\frac{30}{11(n)_3}
\]

by CMR332.  In either exceptional cylinder sharing one paid cell with `M`, a
triple using that paid cell requires two residual cells.  There are at most
`binom(s_M-1,2)` such prescriptions, each with probability at most

\[
\frac{30}{11(n)_2}.
\]

Average over the `m` equal-size cylinders and apply the union bound.  If
`M=L` for one paid cylinder, line-cleaning makes its true contribution zero;
the displayed estimate only overcounts it. ∎

## 2. Frozen-bank line energy

Let `\mathfrak L` be the set of all real lines which support at least one
candidate-only triple in some state of the bank.

### Theorem CMR352 — PROVED

Assume that every bank state is globally nonimproving and that no bank state
creates an anchored certificate involving a fixed outside point.  Then

\[
\boxed{
\sum_{M\in\mathfrak L}
\left[
\frac{\binom{s_M}{3}}{(n)_3}
+
\frac{2}{m}
\frac{\binom{s_M-1}{2}}{(n)_2}
\right]
\ge
\frac{11}{30}.
}
\]

### Proof

Every bank state omits the selected old target endpoint.  If it is globally
nonimproving, it must contain a replacement collinear triple.  Under the
anchored-free hypothesis that triple is candidate-only, so the events

\[
\{\text{the state contains a triple on }M\},
\qquad M\in\mathfrak L,
\]

cover the entire bank probability space.  Sum the CMR351 atom bounds and use
the union bound. ∎

This is a strict target-versus-collateral inequality: the destroyed old target
forces a positive real-line occupancy energy, with no rank-two contribution
from the paid line itself.

## 3. Dyadic height localization

Let the primitive height of `M` be

\[
K(M)=\max\{|u_M|,|v_M|\}.
\]

Put

\[
B=\left\lceil\log_2 t\right\rceil.
\]

For a dyadic value `H`, let `J_H` be the number of lines in `\mathfrak L` with

\[
H\le K(M)<2H.
\]

A line in this band has at most

\[
q_H=1+\left\lfloor\frac{t-1}{H}\right\rfloor
\]

board cells.

### Corollary CMR353 — PROVED

Some dyadic height band satisfies

\[
\boxed{
J_H
\left[
\frac{\binom{q_H}{3}}{(n)_3}
+
\frac{2}{m}
\frac{\binom{q_H-1}{2}}{(n)_2}
\right]
\ge
\frac{11}{30B}.
}
\]

### Proof

Partition the positive-height lines in CMR352 into the at most `B` dyadic
bands.  One band contributes at least `1/B` of the total energy.  Replace every
line occupancy in that band by the common upper bound `q_H`. ∎

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
J_H
\ge
\frac{11}{90}
\frac{H^3}{\lceil\log_2t\rceil}.
}
\]

In particular a frozen width-two, width-three, or two-slice mixed-fan bank
forces

\[
J_H=\Omega\left(\frac{H^3}{\log t}\right)
\]

distinct replacement-line signatures in one primitive-height band.

### Proof

If `q_H<=2`, the band has no candidate triples and cannot carry the positive
CMR353 energy.  Hence

\[
H\le\frac{t-1}{2}.
\]

Then

\[
q_H
\le
1+\frac{t-1}{H}
\le
\frac{3(t-1)}{2H}.
\]

For `t>=20`,

\[
(n)_3=(t-2)(t-3)(t-4)
\ge
\left(\frac{4(t-1)}5\right)^3,
\]

so

\[
\frac{\binom{q_H}{3}}{(n)_3}
<
\frac{11}{10H^3}.
\]

Also

\[
\frac{2}{m}
\frac{\binom{q_H-1}{2}}{(n)_2}
\le
\frac{(t-1)^3}{2(t-9)(t-2)(t-3)}\frac1{H^3}
\le
\frac{21}{20H^3}.
\]

The last inequality is equivalent to

\[
11t^3-264t^2+1041t-1124\ge0,
\]

which holds at `t=20` and thereafter because its first two derivatives are
positive from that point onward.  The bracket in CMR353 is therefore below

\[
\frac3{H^3}.
\]

Rearranging CMR353 proves the claim. ∎

The remaining low-height problem has consequently become an energy-to-carry
conversion: assign the `Omega(H^3/log t)` real lines in the selected band to
first-separation, quotient, and primitive carry cells, then prove bounded reuse
or an executable prefix continuation.  The generic matching-space part no
longer loses the strict target advantage.

No all-`n` theorem is claimed here.  The line atoms, dyadic localization, and
explicit cubic lower bound are checked in
[`scripts/verify_prime_power_line_clean_energy.py`](../scripts/verify_prime_power_line_clean_energy.py).

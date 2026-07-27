# Exact reverse-flow law for remote cylinders under stationary resampling

**Branch:** `research/superregular-resampling`

SRR1b and SRR1c characterize stationary flaw-removal kernels, while the
existing remote-event clause bounds a remote event by the chance that a switch
meets its neighbourhood. The sharper invariant is the reverse flow from each
unflawed state back into the flaw event. This note gives an exact cylinder
identity and turns the general lopsided comparison into a column-load balancing
problem for the switching flow.

## Setup

Let `Omega=A sqcup B` be a finite state space with the uniform measure `mu`.
The set `A` is the flaw event. Let `K` be a symmetric stochastic kernel such
that

\[
K(a,A)=0\qquad(a\in A).
\]

Thus every resampling step from a flawed state removes the flaw and uniform
measure is stationary. For `b in B`, define its reverse flaw-entry load

\[
q(b)=K(b,A)=\sum_{a\in A}K(b,a).
\]

Let `X` be uniform on `A` and let `Y` be one `K`-step from `X`.

## SRR2c -- exact reverse-flow cylinder law -- PROVED

For every nonempty `C subseteq B`, write

\[
\bar q_C=\frac1{|C|}\sum_{b\in C}q(b),
\qquad
\bar q_B=\frac1{|B|}\sum_{b\in B}q(b).
\]

Then

\[
\boxed{
\Pr(Y\in C)
=\frac{|C|}{|A|}\bar q_C
=\mu(C\mid B)\frac{\bar q_C}{\bar q_B}.
}
\]

Moreover

\[
\boxed{\bar q_B=\frac{|A|}{|B|}.}
\]

### Proof

By symmetry,

\[
\Pr(Y\in C)
=\frac1{|A|}\sum_{a\in A}\sum_{b\in C}K(a,b)
=\frac1{|A|}\sum_{b\in C}\sum_{a\in A}K(b,a)
=\frac{|C|}{|A|}\bar q_C.
\]

Every row indexed by `a in A` sends total mass one into `B`, so symmetry gives

\[
\sum_{b\in B}q(b)
=\sum_{a\in A}\sum_{b\in B}K(a,b)
=|A|.
\]

Hence `bar q_B=|A|/|B|`. Substitution yields the conditional-uniform form.
QED.

## SRR2d -- cylinder balance criterion -- PROVED

For `eta>=0`, if

\[
\bar q_C\le(1+\eta)\bar q_B,
\]

then

\[
\boxed{
\Pr(Y\in C)\le(1+\eta)\mu(C\mid B).
}
\]

If

\[
|\bar q_C-\bar q_B|\le\eta\bar q_B,
\]

then the two-sided comparison

\[
\boxed{
(1-\eta)\mu(C\mid B)
\le\Pr(Y\in C)
\le(1+\eta)\mu(C\mid B)
}
\]

holds. In particular, if `q` is constant on `B`, the resampled output is
exactly uniform on `B`.

### Proof

Divide the exact identity of SRR2c by `mu(C|B)` and use the assumed average-load
bound. QED.

## SRR2e -- switching-flow formulation -- PROVED

Suppose `K` is obtained from feasible symmetric Hall-flow weights
`w_{ab}` on a switching graph `Gamma subseteq A x B`, with

\[
\sum_b w_{ab}=1\quad(a\in A),
\qquad
\sum_a w_{ab}\le1\quad(b\in B).
\]

Then

\[
\boxed{q(b)=\sum_{a:ab\in\Gamma}w_{ab}.}
\]

Therefore the lopsided remote-cylinder comparison is equivalent to controlling
the average column load of a feasible switching flow on each remote cylinder.
Hall feasibility alone supplies the total column load `|A|`; it does not force
that load to be evenly distributed over remote cylinders.

### Proof

The symmetric kernel places `w_{ab}` on both orientations of each switching
edge and the unused column capacity on the self-loop at `b`. Summing the
entries from `b` into `A` gives the displayed column load. Apply SRR2c. QED.

## Complete-host specialization

For the one-edge flaw in `K_{N,N}`, the standard four-cycle oracle has

\[
q(b)=\frac1{N-1}
\]

for every unflawed matching `b`. SRR2d therefore recovers the stronger exact
statement: after resampling a matching containing the distinguished edge, the
output is uniform among all perfect matchings avoiding that edge.

## Consequence for SRR2

The general superregular remote-cylinder problem now has a precise target.
Construct a bounded-cycle feasible switching flow whose reverse column load is
nearly constant on every relevant remote partial-matching cylinder. Counting
forward switches only in flawed states is insufficient; the required object is
a cylinder-balanced fractional Hall flow.

This note does not prove that such a flow exists in every superregular host.
It removes ambiguity about the exact quantitative property that the switching
construction must establish.

## Finite check

`scripts/verify_reverse_flow_cylinder_law.py` exhausts all half-integral
feasible Hall-flow matrices with at most two flawed and three unflawed states,
constructs the symmetric stationary kernels, and verifies the exact identity
for every nonempty remote cylinder.

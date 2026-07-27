# Reverse-flow transfer of spread inventories into AC5

**Branch:** `research/alternating-core-chain`

AC5l--AC5p audit a random AC menu once its law has prescribed-pair cylinder
bounds.  Complete and dense-host matching measures provide such laws directly,
but a local stationary resampling oracle is usually described by a switching
kernel rather than by an explicit uniform menu.  This note gives the exact
transfer rule.

The only new quantitative field is the reverse flaw-entry load of the
switching flow on each event cylinder.  No independence between successive
resampling steps is assumed.

## Stationary flaw-removal setup

Let

\[
\Omega=A\sqcup B
\]

be a finite matching state space with the uniform measure.  The set `A` is one
local flaw event and `B` its complement.  Let `K` be a symmetric stochastic
kernel satisfying

\[
K(a,A)=0\qquad(a\in A).
\]

Thus every step from a flawed state removes the flaw and the uniform measure
on `Omega` is stationary.  For `b in B`, put

\[
q(b)=K(b,A).
\]

Let `X` be uniform on `A` and let `Y` be one `K`-step from `X`.  Write `nu` for
the uniform measure on `B`.

## AC5y -- exact resampled-cylinder law -- PROVED

For every nonempty event cylinder `C subseteq B`, define

\[
\bar q_C=\frac1{|C|}\sum_{b\in C}q(b),
\qquad
\bar q_B=\frac1{|B|}\sum_{b\in B}q(b).
\]

Then

\[
\boxed{
\Pr(Y\in C)
=\nu(C)\frac{\bar q_C}{\bar q_B},
\qquad
\bar q_B=\frac{|A|}{|B|}.
}
\]

### Proof

By symmetry,

\[
\Pr(Y\in C)
=\frac1{|A|}\sum_{a\in A}\sum_{b\in C}K(a,b)
=\frac1{|A|}\sum_{b\in C}\sum_{a\in A}K(b,a)
=\frac{|C|}{|A|}\bar q_C.
\]

Every flawed row sends total mass one into `B`, so

\[
\sum_{b\in B}q(b)
=\sum_{a\in A}\sum_{b\in B}K(a,b)
=|A|.
\]

Therefore `bar q_B=|A|/|B|`; substitution gives the first identity. QED.

## AC5z -- reverse-balanced spread transfer -- PROVED

Assume the uniform unflawed law `nu` is `K_0/p`-spread on the relevant
prescribed target-partner pairs.  For `k in {1,2,3}`, assume every compatible
`k`-pair cylinder `C` used by the AC5 event inventory obeys

\[
\boxed{\bar q_C\le \rho_k\bar q_B.}
\]

Then the resampled output law satisfies

\[
\boxed{
\Pr(Y\in C)
\le
\rho_k\left(\frac{K_0}{p}\right)^k
}
\]

for every such `k`-pair cylinder.

In particular, exact reverse balance `rho_k=1` transfers the original spread
bound without loss.  A pointwise bound

\[
q(b)\le\rho\bar q_B\qquad(b\in B)
\]

is sufficient with `rho_k=rho` for every rank, but the theorem only needs the
weaker average bound on the actual AC5 cylinders.

### Proof

AC5y gives

\[
\Pr(Y\in C)
=\nu(C)\frac{\bar q_C}{\bar q_B}
\le \rho_k\nu(C).
\]

Apply the `K_0/p`-spread bound for `nu(C)`. QED.

The factor `rho_k` occurs once per event cylinder, not once per prescribed
pair.  Replacing `K_0` by `rho K_0` is valid but unnecessarily weaker for
`k>=2`.

## AC5aa -- reverse-flow event expectation bound -- PROVED

Let `E_{2,J}` and `E_{3,J}` be complete two-choice and three-choice event
inventories in one line band `J`, with sizes `M_{2,J}` and `M_{3,J}`.  Under
the AC5z hypotheses,

\[
\boxed{
\mathbb E N_J
\le
\rho_2\left(\frac{K_0}{p}\right)^2M_{2,J}
+
\rho_3\left(\frac{K_0}{p}\right)^3M_{3,J}.
}
\]

### Proof

Choose one representing cylinder for every possible created triple.  Its
indicator probability has the AC5z bound of the corresponding rank.  Sum the
indicators.  Overcounting in the complete inventory only enlarges the right
side. QED.

Thus AC5o remains valid after replacing its two rank contributions by their
respective reverse-flow factors.  Put

\[
\Gamma_J^{\rm rf}
=
\rho_{2,J}\left(\frac{K_0}{p}\right)^2M_{2,J}
+
\rho_{3,J}\left(\frac{K_0}{p}\right)^3M_{3,J}.
\]

## AC5ab -- reverse-flow protected-safe drift import -- PROVED

For one resampled menu, if

\[
\boxed{
\Gamma_{\rm cur}^{\rm rf}
+t\Gamma_{\rm high}^{\rm rf}<t,
}
\]

then one output state creates no protected-band triple and at most `t-1`
current-band triples.  Hence it passes AC5g--AC5h and strictly decreases
`Psi_H`.

For a multistep random installation path, suppose the final current inventory
has expectation at most `Gamma_cur^rf` and the protected inventory at step `j`
has expectation at most `Gamma_high,j^rf`, each obtained from its own
reverse-flow cylinder bounds.  If

\[
\boxed{
\Gamma_{\rm cur}^{\rm rf}
+t\sum_j\Gamma_{{\rm high},j}^{\rm rf}<t,
}
\]

then one complete path is protected-safe at every intermediate step and has
final current count at most `t-1`.

### Proof

The first statement is AC5n with the AC5aa expectations.  For the second use
AC5p.  Those arguments use only the unconditional expectations of the final
and intermediate badness variables; they do not require independence between
resampling steps. QED.

## Switching-flow interpretation

When `K` is built from feasible symmetric Hall-flow weights `w_ab` on a
flaw-removing switching graph,

\[
q(b)=\sum_{a\in A}w_{ab}.
\]

Therefore AC5z asks for average column-load balance only on the finite
rank-two and rank-three cylinders appearing in the complete current/protected
event inventories.  Full pointwise near-regularity of the switching graph is
sufficient but not necessary.

## Consequence for AC5

A local superregular resampling oracle can enter the AC5 audit through three
separate verifiable inputs:

1. a baseline spread law for the uniform unflawed matching space;
2. a feasible bounded-support stationary switching flow;
3. reverse column-load ratios `rho_2,rho_3` on the actual current and protected
   event cylinders.

The remaining theorem is construction of such cylinder-balanced flows for the
nonuniform and restricted AC menus.  Stationarity or Hall feasibility alone
does not bound the `rho_k` factors.

## Finite check

`scripts/verify_ac_reverse_flow_spread_import.py` exhausts half-integral
feasible switching flows with at most two flawed and three unflawed states,
checks AC5y's exact law on every cylinder, and verifies the rank-weighted event
and protected-drift inequalities on finite inventories.

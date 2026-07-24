# Target-specific matching loads and localized line walls

CMR245--CMR247 treat line unions in a parent bank which moves one designated
old endpoint. The actual candidate events are smaller rank-`1/2/3` matching
cylinders. Their target-specific law and matching-space local loads give a
cubic candidate-only concentration at one parent source row or target column.

Fix a parent board of size `t` and one designated old target cell `z_*`.
Let

\[
\Omega_*
=
\{\pi\in S_t:z_*\notin\pi\}.
\]

For `r=1,2,3`, let `\mathcal F_r` be the distinct compatible rank-`r` candidate
prescriptions which support a possible new real triple after the target endpoint
is moved.

## 1. Exact target-specific cylinder law

### Theorem CMR248 — PROVED

The target-specific state count is

\[
\boxed{|\Omega_*|=(t-1)(t-1)!.}
\]

For every compatible rank-`r` prescription `Q` not containing `z_*`,

\[
\Pr_{\pi\in\Omega_*}(Q\subseteq\pi)
\le
\frac{(t-r)!}{(t-1)(t-1)!}.
\]

In particular the rank maxima are

\[
\boxed{
\alpha_1=\frac1{t-1},
\qquad
\alpha_2=\frac1{(t-1)^2},
\qquad
\alpha_3=\frac1{(t-1)^2(t-2)}.
}
\]

Consequently, if the candidate cylinders cover all target-specific states, then

\[
\boxed{
\frac{|\mathcal F_1|}{t-1}
+
\frac{|\mathcal F_2|}{(t-1)^2}
+
\frac{|\mathcal F_3|}{(t-1)^2(t-2)}
\ge1.
}
\]

If the cover is candidate-only, then

\[
\boxed{|\mathcal F_3|\ge(t-1)^2(t-2).}
\]

### Proof

Exactly `(t-1)!` of the `t!` permutations contain `z_*`, giving the state
count. At most `(t-r)!` permutations contain one compatible rank-`r`
prescription. Dividing gives the atom bound and its three simplifications.
The cover inequalities follow from the union bound. ∎

## 2. Target-specific matching-space local lemma

For a board vertex `v`, let

\[
T_r(v)
=
|\{F\in\mathcal F_r:v\in V(F)\}|.
\]

### Theorem CMR249 — PROVED

If every board vertex satisfies

\[
\boxed{
\frac{\mathbf1_{v\in V(z_*)}}t
+
\frac{T_1(v)}t
+
\frac{T_2(v)}{(t)_2}
+
\frac{T_3(v)}{(t)_3}
\le\frac1{24},
}
\]

then there is a parent permutation which omits `z_*` and avoids every candidate
prescription. It destroys the selected old target triple and creates no new
triple touching the replacement block.

### Proof

Choose a uniformly random perfect matching of the complete `t` by `t` board.
Use one singleton bad event for `z_*` and one canonical event for every
candidate prescription. Their probabilities are `1/t` and `1/(t)_r`,
respectively. The displayed expression is the event-probability load at one
board vertex.

The Lu--Szekely matching-space negative-dependency graph and the proof of CMR219
apply verbatim. Assigning `x_A=2\Pr(A)`, the `1/24` vertex-load bound keeps the
adjacent `x`-mass below one half for every event. The lopsided local lemma gives
a perfect matching avoiding all bad events. ∎

Only the two endpoints of `z_*` pay the singleton load; all other board vertices
have no old-cell term.

## 3. Anchored-free concentration

### Theorem CMR250 — PROVED

Assume `t>=48` and suppose no target-specific parent state improves the current
state. If the candidate cover has no rank-one or rank-two events, then some
board source row or target column `v` satisfies

\[
\boxed{
T_3(v)>\frac{(t)_3}{48}.
}
\]

The triples counted by `T_3(v)` occupy more than

\[
\boxed{\frac t{24}}
\]

distinct nonaxis real-line signatures. One dyadic primitive-height band
contains more than

\[
\boxed{
\frac{t}{24\lceil\log_2t\rceil}
}
\]

of those distinct lines.

### Proof

The contrapositive of CMR249 gives a vertex `v` with

\[
\frac{\mathbf1_{v\in V(z_*)}}t+
\frac{T_3(v)}{(t)_3}>
\frac1{24}.
\]

For `t>=48`, the first term is at most `1/48`, proving the cubic lower bound.

A nonaxis line meets one fixed board source row or target column in at most one
cell. If it has at most `t` board cells, the number of compatible triples on
that line containing its wall cell is at most

\[
\binom{t-1}{2}.
\]

Therefore the number of distinct line signatures is greater than

\[
\frac{(t)_3/48}{\binom{t-1}{2}}
=
\frac t{24}.
\]

There are at most `\lceil\log_2t\rceil` dyadic primitive-height bands, so the
last assertion follows by averaging. ∎

## 4. Executable removal of one localized wall

### Corollary CMR251 — PROVED

Under the hypotheses of CMR250, choose any

\[
m=\left\lfloor\frac t{24}\right\rfloor
\]

distinct line signatures from the concentrated wall. There is a
target-specific parent permutation avoiding every available candidate cell on
those `m` lines.

Its required covering certificate is either rank one or rank two, yielding an
anchored alternating continuation, or is a candidate-only triple on a line
outside the removed family.

### Proof

For `t>=48`, one has `m\le t-2`. Apply CMR245 to the chosen lines. The resulting
permutation omits `z_*`, so it destroys the selected old target. Global
nonimprovement forces a new covering certificate. No candidate-only
certificate can use a removed line because every available cell on that line is
absent and `z_*` is also absent. ∎

CMR251 is a localized no-return step: one complete cubic wall at a fixed board
vertex can be removed at once, and any replacement candidate-only certificate
uses a new real-line signature.

## 5. Revised cylinder endpoint

The candidate-only obstruction is simultaneously constrained in three ways:

- globally it contains at least `(t-1)^2(t-2)` distinct rank-three cylinders;
- locally one board row or column supports more than `(t)_3/48` of them;
- geometrically that local population occupies more than `t/24` distinct lines,
  one dyadic band carrying a logarithmic fraction.

The remaining theorem is to iterate CMR251 without recycling the same
first-separation or carry accounts, or to apply an exact conflict-free
completion to the dyadic line band supplied by CMR250.

No all-`n` theorem is claimed here. Exact target-cylinder atoms and the local
line-count arithmetic are checked in
[`scripts/verify_prime_power_target_specific_load.py`](../scripts/verify_prime_power_target_specific_load.py).

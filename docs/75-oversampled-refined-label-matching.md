# Oversampled refined label matching

PP3ff requires a matching of movement/refill label pairs whose source-edge
domains are simultaneously fixed-pair safe and same-edge-anchor safe. A
minimum-degree hypothesis is convenient but stronger than necessary. When the
candidate label reservoir has size `L>>W`, global boundary-shadow and bad-label
incidence averages already force a matching of size `W`.

## 1. Average fixed-pair compatibility

Let `A_0,B_0` be candidate movement and refill label sets, both of size `L`. Use
the notation of PP3ea and put

\[
 b_M(A)=R-|C_A|,
 \qquad
 b_R(B)=R-|D_B|.
\]

Define

\[
 \mathcal S_M=\sum_{A\in A_0}b_M(A),
 \qquad
 \mathcal S_R=\sum_{B\in B_0}b_R(B).
\]

Let `G_gamma` be the fixed-pair compatibility graph joining `(A,B)` when

\[
 |C_A\cap D_B|\ge\gamma R.
\]

### Proposition PP3fs -- PROVED

The number of missing edges of `G_gamma` is at most

\[
 \boxed{
 L\frac{\mathcal S_M+\mathcal S_R}{(1-\gamma)R}.
 }
\]

Consequently

\[
 \boxed{
 |E(G_\gamma)|
 \ge
 L^2
 -
 L\frac{\mathcal S_M+\mathcal S_R}{(1-\gamma)R}.
 }
\]

#### Proof

For every label pair,

\[
 |C_A\cap D_B|
 \ge
 R-b_M(A)-b_R(B).
\]

Therefore a missing edge satisfies

\[
 b_M(A)+b_R(B)>(1-\gamma)R.
\]

Summing `b_M(A)+b_R(B)` over all `L^2` label pairs gives

\[
 L\mathcal S_M+L\mathcal S_R.
\]

Each missing pair contributes more than `(1-gamma)R`, proving the bound. ∎

This is an average version of the boundary-shadow criterion PP3ee--PP3eg.

## 2. Removing same-edge-anchor-heavy label pairs

Fix `0<epsilon<gamma`. Let `J_{gamma,epsilon}` be the refined graph from PP3ff,
so an edge of `G_gamma` remains only when

\[
 |U_{A,B}|\le\epsilon R.
\]

Define the exact bad-label incidence

\[
 \mathcal U
 =
 \sum_{A\in A_0}\sum_{B\in B_0}|U_{A,B}|.
\]

Let

\[
 \mathcal E=\mathcal E(E,F)
\]

be the pool-anchor divisor energy from PP3fe. Then

\[
 \mathcal U\le\mathcal E.
\]

### Proposition PP3ft -- PROVED

The refined graph satisfies

\[
 \boxed{
 |E(J_{\gamma,\epsilon})|
 \ge
 L^2
 -
 L\frac{\mathcal S_M+\mathcal S_R}{(1-\gamma)R}
 -
 \frac{\mathcal U}{\epsilon R}.
 }
\]

Hence also

\[
 \boxed{
 |E(J_{\gamma,\epsilon})|
 \ge
 L^2
 -
 L\frac{\mathcal S_M+\mathcal S_R}{(1-\gamma)R}
 -
 \frac{\mathcal E}{\epsilon R}.
 }
\]

Its maximum matching size `nu(J)` satisfies

\[
 \boxed{
 \nu(J_{\gamma,\epsilon})
 \ge
 \left\lceil
 \frac{|E(J_{\gamma,\epsilon})|}{L}
 \right\rceil.
 }
\]

#### Proof

At most `mathcal U/(epsilon R)` label pairs can satisfy
`|U_{A,B}|>epsilon R`. Remove these from the edge lower bound of PP3fs. The
second displayed edge bound follows from PP3fe.

For the matching bound, König's theorem gives a vertex cover of size `nu(J)`.
Every vertex covers at most `L` graph edges, so

\[
 |E(J)|\le \nu(J)L.
\]

Rearrange and use integrality. ∎

The exact incidence `mathcal U` can be much smaller than `mathcal E`, because
many anchor witnesses may certify the same bad source edge for one label pair.

## 3. Direct macro theorem

### Theorem PP3fu -- PROVED FROM THE STANDARD LOCAL LEMMA

Suppose

\[
 \boxed{
 L^2
 -
 L\frac{\mathcal S_M+\mathcal S_R}{(1-\gamma)R}
 -
 \frac{\mathcal U}{\epsilon R}
 >
 (W-1)L
 }
\]

and

\[
 \boxed{
 48(2W)^2\le(\gamma-\epsilon)^2R.
 }
\]

Then the matching pool supports a saturated width-`W` macro patch that:

1. is internally no-three-in-line;
2. uses `2W` distinct source edges;
3. has no fixed-pair source blocker;
4. has no same-edge anchored source triple.

The same conclusion follows from the stronger arithmetic hypothesis obtained by
replacing `mathcal U` with `mathcal E`.

#### Proof

The first inequality and PP3ft give a matching of size at least `W` in
`J_{gamma,epsilon}`. Restrict to the matched labels. Every matched label pair
has a refined domain of size at least `(gamma-epsilon)R`. Apply PP3ff. ∎

Under the stronger PP3fg numerical condition, the resulting conditional macro
distribution also has fixed-rank cylinder bound

\[
 \frac{e^{q/2}}{((\gamma-\epsilon)R)^q}.
\]

## 4. Normalized form

Put

\[
 \sigma
 =
 \frac{\mathcal S_M+\mathcal S_R}{RL},
 \qquad
 \eta_U
 =
 \frac{\mathcal U}{RL^2},
 \qquad
 \eta_E
 =
 \frac{\mathcal E}{RL^2}.
\]

Thus `eta_U<=eta_E`.

### Corollary PP3fv -- PROVED

The refined graph has matching number at least

\[
 \boxed{
 L
 \left(
 1-
 \frac{\sigma}{1-\gamma}
 -
 \frac{\eta_U}{\epsilon}
 \right)
 }
\]

up to the integer ceiling. In particular, PP3fu applies whenever

\[
 \boxed{
 \frac WL
 <
 1-
 \frac{\sigma}{1-\gamma}
 -
 \frac{\eta_U}{\epsilon}
 }
\]

with fixed positive slack, together with the local-lemma width inequality. A
fully arithmetic sufficient form replaces `eta_U` by `eta_E`.

#### Proof

Divide the PP3ft edge lower bound by `L` and use its matching estimate. ∎

Thus one does not need normalized shadow and bad-label incidence tending to zero
when `L` substantially exceeds `W`. It is enough that their combined density
loss is smaller than the unused label fraction `1-W/L`.

## 5. Prime-gap-scale use

For one macro pool, the installed width is

\[
 W=\Theta(\sqrt R).
\]

The candidate boundary reservoir may be much larger, because unused labels cost
no row or column degree. Taking, for example,

\[
 L=CW
\]

with fixed `C>1` permits a constant fraction of label pairs to be removed while
retaining a `W`-matching. Larger oversampling gives proportionally more room for
boundary-shadow and same-edge-anchor concentration.

The remaining first-half bottleneck of the prime-patching route is therefore the
explicit averaged estimate

\[
 \boxed{
 \frac{\mathcal S_M+\mathcal S_R}{(1-\gamma)RL}
 +
 \frac{\mathcal U}{\epsilon RL^2}
 <
 1-
 \frac WL.
 }
\]

The divisor-energy fallback replaces `mathcal U` by `mathcal E`.

Failure forces either a positive-density boundary shadow or a positive-density
bad-label matrix. The latter may arise from divisor-energy concentration, but
the exact incidence formulation allows duplicate anchor witnesses to be
compressed before arithmetic estimates are applied. These are precisely the
structured alternatives targeted by protected rectangles, cycle flips, and
carry/divisor dispersion.
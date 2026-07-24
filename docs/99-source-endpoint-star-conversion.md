# Source-endpoint star conversion

The source-star alternative PP3hx has a common **source endpoint**: one source
point belongs to many noncontroller blocker pairs for many candidate entries.
This is not the same geometry as the common-candidate secant star in AN2--AN4.
The correct first conversion is to move the common source endpoint itself.

## 1. Free and captive star centres

Fix the controller pools and candidate-entry universe `V` used by the monotone
potential PP3ij.  Let `p` be a source point occurring as a blocker endpoint in
`C_star` bad entries.

Call `p` **free** when it is not one of the source edges used as a controller in
`V`.  Otherwise call it **captive**.

### Proposition PP3ki -- PROVED

If `p` is free, deleting `p` removes at least

\[
 \boxed{C_{\rm star}}
\]

units from the controller-shadow potential before any replacement points are
inserted.

#### Proof

Every one of the `C_star` entries has a chosen blocker pair `{p,s}` disjoint
from its controller edge.  The potential counts that entry in the weight of
`{p,s}`.  Deleting `p` removes all these incidences.  They are distinct
entry-incidence units even when several entries use the same blocker partner.
∎

The free condition is needed only to preserve the fixed controller
infrastructure during iteration.

## 2. A large endpoint layer containing the centre

The controller pools lie in one perfect-matching layer and occupy

\[
 MR=(ab+o(1))m<m
\]

points.  The other matching layer contains no controller points.

### Proposition PP3kj -- PROVED

For every free star centre `p`, its permutation layer contains a set

\[
 R_0=\{p=r_1,r_2,\ldots,r_Q\}
\]

of pairwise row- and column-disjoint source points, all disjoint from the
controller infrastructure, with

\[
 \boxed{Q=\Theta(m).}
\]

#### Proof

If `p` belongs to the noncontroller matching layer, take any linear-sized subset
of that layer containing `p`.  If it belongs to the controller layer but outside
the selected pools, the unused part of that layer has size

\[
 m-MR=(1-ab+o(1))m,
\]

and contains `p`.  Points in one permutation layer have distinct rows and
columns. ∎

## 3. Distinguished-endpoint permutations

Write

\[
 R_0=\{(x_i,y_i):i\in[Q]\},
 \qquad r_1=p.
\]

For a permutation `pi` with no fixed points, put

\[
 R_\pi=\{(x_i,y_{\pi(i)}):i\in[Q]\}.
\]

### Proposition PP3kk -- PROVED

Every source-admissible derangement `pi` preserves saturation, preserves every
controller edge, and deletes the star centre `p`.  Its potential change is

\[
 \Psi_V(S_\pi)-\Psi_V(S)
 =
 \mathcal I(\pi)-\mathcal C(R_0),
\]

with

\[
 \boxed{\mathcal C(R_0)\ge C_{\rm star}.}
\]

Consequently

\[
 \mathcal I(\pi)<C_{\rm star}
\]

is sufficient for strict improvement.

#### Proof

The endpoint-permutation degree identity is PP3ia--PP3ib.  All removed endpoints
are outside the controller infrastructure by PP3kj, so every controller edge is
preserved.  A derangement moves `p`.  Proposition PP3ki supplies the displayed
credit lower bound. ∎

At the PP3hy scale one has `C_star=Omega(m)`, which is larger than the
prime-gap patch width.

## 4. Zero-unary distinguished host

Build the source-safe endpoint host on `R_0` as in PP3in, delete the diagonal,
and remove all recapture and residual unary-shadow cells as in PP3jy.  Denote the
resulting graph by

\[
 G_0(p).
\]

The distinguished index of `p` is an ordinary left and right resource of this
balanced graph.  Because the diagonal is absent, every perfect matching of
`G_0(p)` moves `p` automatically.

### Theorem PP3kl -- PROVED FROM PP3kb

Assume `G_0(p)` is `(epsilon,delta)`-superregular and that its anchored-pair,
binary-shadow-pair, and inserted-triple counts satisfy

\[
 K^2\dfrac{P_0+|B_0|}{Q^2}
 +
 K^3\dfrac{Q_0}{Q^3}
 <1,
\]

where `K=K(delta)` is the PP3kb constant.  Then the free source-star branch has a
source-admissible endpoint trade with zero insertion shadow and strict negative
controller-shadow change.

#### Proof

Apply PP3kb to `G_0(p)`.  The resulting perfect matching is source-admissible and
has zero insertion shadow.  It moves `p`, and PP3kk gives removal credit at least
`C_star>0`. ∎

The theorem does not require an alternating rectangle switch and does not use a
common candidate point.

## 5. Hall obstruction for the star bank

### Corollary PP3km -- PROVED

If the zero-unary distinguished host `G_0(p)` has no perfect matching, there are
sets `X,Y` with

\[
 |X|+|Y|>Q
\]

such that `X cross Y` is entirely contained in the source-unary, recapture, or
unary insertion-shadow support.  For every fixed `alpha>0`, this gives either a
macroscopic forbidden rectangle or fewer than `alpha Q` almost-completely
forbidden endpoint fibres.

#### Proof

Apply PP3jz--PP3ka to `G_0(p)`. ∎

Thus the free star branch has the same exact unary endpoint as the resource
branch.

## 6. The captive-centre obstruction

If the star centre belongs to a fixed controller edge, moving it changes the
controller identity and hence changes the candidate-entry universe `V`.  The
fixed-potential termination theorem PP3il cannot then be invoked directly.

### Proposition PP3kn -- PROVED

The source-star branch splits exactly into:

1. a free centre, reduced by PP3kl to a zero-unary Hall/superregular endpoint;
2. a captive centre lying in the selected controller matching pools.

The older claim that every source-star is directly aligned with AN2--AN4 is not
valid without an additional conversion: AN2--AN4 require many blocker pairs
through one common candidate point, whereas PP3hx gives many blocker pairs
sharing one source endpoint and generally having different candidate points.

#### Proof

The first statement is the definition of free and captive centres together with
PP3kj--PP3kl.  The geometric distinction follows from the hypotheses of PP3hx
and AN2. ∎

## 7. Revised star target

The remaining source-star work is now precise.

- For a free centre, prove the distinguished zero-unary host is superregular or
  convert its Hall rectangle.
- For a captive centre, either replace the fixed controller infrastructure by a
  dynamically relabelled potential, or perform a controller-preserving trade on
  the blocker partners instead of moving the centre.

This is strictly narrower than an unspecified alternating-star conversion and
removes a previously hidden mismatch between the two star geometries.

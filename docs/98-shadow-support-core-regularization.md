# Shadow-support core regularization

PP3jx records a rich recapture fibre, unary shadow fibre, or binary shadow star
when the maximum endpoint-resource degree is large.  A single rich resource is
not terminal: endpoint trades may discard `o(q)` indices while retaining
positive removal credit and all source-validity estimates.  This chapter
identifies the actual persistent obstruction as a linear support core.

## 1. High-resource sets

Use a two-scale endpoint bank of size `q` from PP3jn.  For an endpoint index
`s`, let its two typed resources be its left old-column resource and right
old-row resource.  Define

\[
 d_{\rm un}(s)
 =
 \max\{d_{\rm rec}(s_L)+d_1(s_L),
       d_{\rm rec}(s_R)+d_1(s_R)\}
\]

and

\[
 d_{\rm bin}(s)
 =
 \max\{d_2(s_L),d_2(s_R)\}.
\]

Deleting endpoint index `s` removes both typed resources, its selected old
point, and its one designated removal-credit unit.  All forbidden source and
shadow supports can only decrease.

### Proposition PP3kd -- PROVED

Let `H` be a set of endpoint indices.  After deleting `H`, the remaining bank:

1. remains a tied endpoint bank in one permutation layer;
2. retains at least `q-|H|` designated removal-credit units;
3. has no larger source-invalid, recapture, unary-shadow, or binary-shadow
   support degree than before deletion;
4. preserves every controller edge because the resource extraction keeps all
   selected blocker endpoints disjoint from the controller infrastructure.

#### Proof

The endpoint points have distinct old rows and columns.  Restricting to a subset
therefore leaves another tied endpoint bank.  Each retained resource entry still
supplies its designated credit.  Support families are induced subfamilies, so
degrees do not increase.  Controller preservation is PP3hy and PP3ik. ∎

## 2. Deleting a sublinear exceptional set

### Theorem PP3ke -- PROVED

Suppose there is a sequence `epsilon_q=o(1)` and a set `H` of `o(q)` endpoint
indices such that every `s` outside `H` satisfies

\[
 d_{\rm un}(s)\le\epsilon_q q,
 \qquad
 d_{\rm bin}(s)\le\epsilon_q q^2.
\]

Then the resource bank contains a source-admissible endpoint trade with zero
insertion shadow and positive removal credit.

#### Proof

Delete `H`.  The remaining size is

\[
 q'=(1-o(1))q.
\]

By PP3kd the source-validity terms from PP3jn remain `o(1)`, while

\[
 d_{\rm rec}+d_1=o(q'),
 \qquad
 d_2=o((q')^2).
\]

Apply PP3jw.  At least one designated credit unit remains, and the chosen trade
has zero insertion cost. ∎

Thus isolated rich fibres and stars are removable bookkeeping, not asymptotic
obstructions.

## 3. Linear support-core alternative

### Corollary PP3kf -- PROVED

If PP3ke cannot be applied along an infinite sequence of bank sizes, then there
is a constant `rho>0` and an infinite subsequence on which at least one of the
following holds.

1. At least `rho q` endpoint indices satisfy

   \[
    d_{\rm un}(s)\ge\rho q.
   \]

2. At least `rho q` endpoint indices satisfy

   \[
    d_{\rm bin}(s)\ge\rho q^2.
   \]

#### Proof

If neither statement holds for every fixed positive `rho`, choose a sequence
`rho_q` tending to zero slowly enough that the union of indices violating

\[
 d_{\rm un}(s)<rho_q q,
 \qquad
 d_{\rm bin}(s)<rho_q q^2
\]

has size `o(q)`.  Proposition PP3ke then applies, a contradiction. ∎

This is a compactness-free diagonal argument on finite degree sequences.

## 4. Global support lower bounds

Let `U` be the simple union of the recapture and residual unary-shadow cell
supports, and let `B` be the simple binary shadow-support family.

### Proposition PP3kg -- PROVED

Under alternative 1 of PP3kf,

\[
 \boxed{|U|\ge\dfrac{rho^2}{4}q^2.}
\]

Under alternative 2,

\[
 \boxed{|B|\ge\dfrac{rho^2}{8}q^3.}
\]

The constants are deliberately loose.

#### Proof

A unary support cell is incident to at most two endpoint indices after the left
and right typed resources are identified with their underlying indices.  Thus
`rho q` indices of degree at least `rho q` contribute at least `rho^2q^2`
incidences, and division by four safely covers the two typed sides and the two
endpoints of one cell.

A compatible binary support event uses at most four endpoint indices.  The
`rho q` high indices contribute at least `rho^2q^3` incidences.  Division by
eight safely covers four resources and the two typed copies. ∎

The exact constants may be replaced by `1/2` and `1/4` with a more careful typed
count.  Only the quadratic and cubic scales are used later.

## 5. Matchings inside the support cores

### Corollary PP3kh -- PROVED

A unary support core with `|U|>=c q^2` contains a matching of endpoint cells of
size at least `c q/2`.

A binary support core with `|B|>=c q^3` has the following star-or-matching
alternative for every `D>=1`:

- one typed endpoint resource belongs to at least `D` binary support events; or
- there are at least `c q^3/(4D)` binary support events whose four typed endpoint
  resources are pairwise disjoint.

#### Proof

For the unary graph, a maximal matching has at most `2q` incident edge fibres,
so König's theorem or the greedy bound gives matching size at least
`|U|/(2q)`.

For the binary family, view each event as a hyperedge on at most four typed
resources.  If the maximum degree is below `D`, greedily selecting one event and
deleting all intersecting events removes fewer than `4D` events per selection.
∎

Taking `D=Theta(q^2)` shows that a cubic binary core either contains a genuine
quadratic resource star or a linear family of resource-disjoint binary shadow
events.

## 6. Revised support obstruction

The resource branch now has a three-level endpoint.

1. Absorb every unary support into the zero-unary host `G_0` of PP3jy.  Failure
   gives the Hall rectangle PP3jz.
2. If the unary host is usable and all exceptional support resources are
   sublinear, delete them and apply PP3ke.
3. Otherwise obtain either a quadratic unary support core or a cubic binary
   support core, together with the matchings/stars of PP3kh.

Consequently the remaining conversion problem is not caused by one accidental
rich fibre.  It is caused by a macroscopic forbidden rectangle, a linear family
of rich unary fibres, or a cubic binary conflict core.

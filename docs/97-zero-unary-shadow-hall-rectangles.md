# Zero-unary-shadow hosts and Hall rectangles

The support endpoint PP3jv treats designated recapture cells and residual unary
shadow cells as canonical permutation events.  A stronger option is to remove
all of them from the endpoint host before sampling.  Their degrees may then be a
positive fraction of the bank size; the only exact obstruction is failure of a
perfect matching in the reduced host.

## 1. The zero-unary-shadow host

Use the source-safe endpoint host `G_safe` of PP3in on a `q`-endpoint bank.  Let

\[
 F_{\rm rec}
\]

be the designated-credit recapture graph of PP3jo and let

\[
 \mathcal U_{\rm sh}
\]

be the residual unary insertion-shadow support of PP3jt.  Define

\[
 \boxed{
 G_0
 =
 G_{\rm safe}
 \setminus
 \bigl(F_{\rm rec}\cup\mathcal U_{\rm sh}\bigr).
 }
\]

Thus an edge of `G_0` is an endpoint cell that is source-safe, does not directly
recapture a designated credit incidence, and has no positive residual unary
controller shadow.

### Proposition PP3jy -- PROVED

Every perfect matching `M` of `G_0` preserves the selected old row and column
degrees and has all of the following properties.

1. No inserted cell collides with the retained source.
2. No inserted cell lies on a secant through two retained source points.
3. No designated credit incidence is directly recaptured through its unchanged
   endpoint.
4. The residual unary insertion-shadow cost is zero.

Every remaining source violation uses two or three inserted cells, and every
remaining insertion-shadow term uses two inserted cells.

#### Proof

The first two statements are PP3in.  The third is PP3jp because every cell of
`F_rec` is absent.  The fourth follows from the definition of
`mathcal U_sh`.  The source and shadow classifications then follow exactly as in
PP3in and PP3ju. ∎

## 2. Exact Hall rectangle

Let the left and right endpoint resources of `G_0` both have size `q`.

### Theorem PP3jz -- PROVED

Exactly one of the following holds.

1. `G_0` has a perfect matching.
2. There are nonempty sets `X` of left resources and `Y` of right resources such
   that

   \[
    \boxed{|X|+|Y|>q}
   \]

   and

   \[
    \boxed{X\times Y\subseteq E(\overline{G_0}).}
   \]

In the second case every cell of `X times Y` belongs to at least one of the
following simple support families:

- the source-unary forbidden support;
- the designated recapture support;
- the residual unary insertion-shadow support.

#### Proof

If Hall's condition fails, choose `X` with `|N(X)|<|X|` and put

\[
 Y=R\setminus N(X).
\]

There is no edge of `G_0` between `X` and `Y`, while

\[
 |X|+|Y|
 =
 |X|+q-|N(X)|
 >q.
\]

Conversely, such a rectangle gives

\[
 |N(X)|\le q-|Y|<|X|,
\]

so Hall fails.  The support classification is the definition of `G_0`. ∎

This is an exact obstruction, not a density estimate.

## 3. Fibre-or-rectangle form

### Corollary PP3ka -- PROVED

Fix `0<alpha<=1/2`.  If `G_0` has no perfect matching, then one of the following
holds.

1. **Macroscopic forbidden rectangle:** there are `X,Y` with

   \[
    |X|,|Y|\ge\alpha q
   \]

   and `X times Y` entirely forbidden.  In particular the simple unary support
   contains at least `alpha^2 q^2` cells on this rectangle.

2. **Near-complete fibre block:** fewer than `alpha q` resources on one side are
   each forbidden from more than `(1-alpha)q` resources on the other side.

#### Proof

Take the Hall rectangle from PP3jz.  If both sides have size at least
`alpha q`, the first alternative holds.  Otherwise, say `|X|<alpha q`.  Since
`|X|+|Y|>q`, one has `|Y|>(1-alpha)q`, and every resource in `X` is forbidden
from all of `Y`.  The transposed case is identical. ∎

Thus a single rich recapture or unary-shadow fibre is not terminal: it may be
removed by endpoint pruning.  Persistent failure requires either a linear
forbidden rectangle or a small block of almost completely forbidden fibres.

## 4. Zero-cost superregular endpoint

Let `P_0` count compatible edge pairs of `G_0` whose cells have a retained source
anchor, let `Q_0` count three-edge matchings whose cells are collinear, and let
`B_0` be the simple family of compatible edge pairs having positive binary
insertion shadow.  Count every pair or triple once.

### Theorem PP3kb -- PROVED FROM SR1

Fix constants `delta>0` and sufficiently small `epsilon>0`.  There is a constant
`K=K(delta)` such that the following holds for all sufficiently large `q`.
Assume `G_0` is `(epsilon,delta)`-superregular and

\[
 \boxed{
 K^2\dfrac{P_0+|B_0|}{q^2}
 +
 K^3\dfrac{Q_0}{q^3}
 <1.
 }
\]

Then some perfect matching of `G_0` is source-admissible and has complete
insertion cost zero.  Hence every endpoint bank with positive removal credit
strictly decreases the controller-shadow potential.

#### Proof

Choose a uniform perfect matching of `G_0`.  By SR1, a prescribed compatible
pair or triple is selected with probability at most `(K/q)^2` or `(K/q)^3`.
A union bound over the source-anchored pairs, inserted collinear triples, and
binary shadow-support pairs gives positive probability that none occurs.
PP3jy has already removed all unary source and shadow terms.  Avoiding `B_0`
removes every binary insertion-shadow term, so the insertion cost is zero.
Positive removal credit and PP3id give strict improvement. ∎

The theorem permits constant unary forbidden density whenever the remaining host
is superregular.  It is strictly stronger than charging every forbidden unary
cell through `d_rec/q+d_1/q`.

## 5. Complementary-degree version

### Corollary PP3kc -- PROVED

The existence of a perfect matching in `G_0` follows whenever every nonedge
`ab` satisfies

\[
 \boxed{d_{G_0}(a)+d_{G_0}(b)\ge q.}
\]

Failure therefore supplies both the Hall rectangle PP3jz and a complementary
low-degree nonedge.

#### Proof

Apply the bipartite Ore criterion PP3gj. ∎

The Ore condition alone does not provide the spread needed to remove the pair
and triple conflicts.  It is nevertheless the exact unary allocation endpoint
and a sharper structural target for protected rectangle or tomographic trades.

## 6. Revised unary obstruction

The resource-bank conversion no longer ends at a rich unary fibre.  After all
unary supports are absorbed into `G_0`, one has:

- a zero-cost improving endpoint trade by PP3kb; or
- a Hall rectangle with `|X|+|Y|>q`; or
- a non-superregular but matchable host whose pair/triple conflicts require a
  conflict-free matching upgrade.

The remaining unary problem is therefore a robust matching problem in one
explicit endpoint graph, not a local-lemma degree bound on individual forbidden
cells.

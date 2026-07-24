# Deletion-aware random matching-block profiles

PP3cm counts source anchors deletion-blindly.  The random block construction has
more structure: after choosing one four-edge deletion in every block, the union
of deleted source edges is a uniform fixed-size subset of the matching layer.
This gives exact survival factors for source anchors and removes every
controller-anchor collision.

## 1. Uniform deletion union

Use the random labelled equipartition from PP3ck.  In every block `E_i`, choose a
uniform four-edge deletion `D_i subseteq E_i`, independently between blocks, and
then choose the two ordered pair partitions uniformly.  Put

\[
 D=\bigcup_{i=1}^K D_i.
\]

Thus `|D|=4K`.

### Proposition PP3co -- PROVED

The random set `D` is a uniform `4K`-subset of the matching layer `P`.

More generally, condition on any controlled patch event that:

- names `q` distinct controller edges;
- prescribes the block label of every controller;
- prescribes any movement/refill line choices for those controllers;
- forces all `q` controller edges to be deleted.

Conditional on that event, the remaining set

\[
 D\setminus R
\]

is a uniform `(4K-q)`-subset of `P setminus R`, where `R` is the controller set.

#### Proof

The complete experiment is invariant under every permutation of the source
matching edges.  Hence the distribution of the fixed-size set `D` is uniform.
After conditioning on a controlled event, every permutation fixing the named
controller edges preserves the event and acts transitively on subsets of the
remaining edges of a given size.  Therefore the conditional deletion union is
uniform on the claimed family. ∎

The statement does not require the blocks to cover the whole layer.

## 2. Exact retained-anchor factor

Let `s` specified source anchors lie in the chosen matching layer, be distinct
from one another, and be disjoint from the `q` controller edges.  Define

\[
 H_{q,s}
 =
 \frac{(m-4K)_s}{(m-q)_s},
 \qquad H_{q,0}=1.
\]

### Corollary PP3cp -- PROVED

Conditional on the controlled patch event, all `s` source anchors survive with
probability exactly `H_{q,s}`.

If a proposed source anchor is itself one of the controller edges, its retained
anchor event has probability zero.

#### Proof

PP3co leaves a uniform `(4K-q)`-subset of the `m-q` noncontroller edges to be
deleted.  The probability that none of the `s` anchors lies in it is

\[
 \frac{\binom{m-q-s}{4K-q}}{\binom{m-q}{4K-q}}
 =
 \frac{(m-4K)_s}{(m-q)_s}.
\]

A controller edge is deleted by the controlled event itself. ∎

For example, a prescribed patch cell has unconditioned probability `2/m`.  If
one distinct matching-layer anchor must remain, the exact joint probability is

\[
 \frac2m\frac{m-4K}{m-1}.
\]

At the finite extreme `r=4` and `Kr=m`, every edge of the selected layer is
deleted and all positive-rank same-layer anchor events vanish.

## 3. Stratified global profile counts

Refine the deletion-blind profile counts from PP3cm as follows.

- `M_1^{(s)}`, for `s=0,1,2`, counts `M_1` signatures whose two source points
  contain exactly `s` points from the selected matching layer.
- `M_h^{(s)}`, `M_2^{(s)}`, and `M_{11}^{(s)}`, for `s=0,1`, count signatures
  whose source anchor lies in the selected layer exactly when `s=1`.

Delete from these families every signature in which a selected-layer source
anchor is one of its candidate controller edges.  Such a triple is impossible by
PP3cp.  The all-patch profiles `M_{h1},M_{21},M_{111}` need no anchor
stratification.

### Proposition PP3cq -- PROVED

Let `W_delta` be the PP3ci left side after conditioning every block to a clean
domain of density at least `delta`.  Then

\[
 \mathbb E W_\delta\le G_\delta^{\rm del},
\]

where

\[
\boxed{
\begin{aligned}
G_\delta^{\rm del}
={}&
\frac{2}{\delta m}
 \sum_{s=0}^2 H_{1,s}M_1^{(s)}
+
\frac{1}{\delta m}
 \sum_{s=0}^1 H_{1,s}M_h^{(s)}
\\
&+
\frac{8(r-1)}{\delta r(m)_2}
 \sum_{s=0}^1 H_{2,s}M_2^{(s)}
+
\frac{4}{\delta^2(m)_2}
 \sum_{s=0}^1 H_{2,s}M_{11}^{(s)}
\\
&+
\frac{2M_{h1}}{\delta^2(m)_2}
+
\frac{16(r-1)M_{21}}{\delta^2r(m)_3}
+
\frac{8M_{111}}{\delta^3(m)_3}.
\end{aligned}
}
\]

#### Proof

Use the same block-assignment probabilities as in PP3cm.  For every profile with
source anchors in the selected layer, PP3cp gives the additional factor
`H_{q,s}`, where `q` is the number of distinct controller edges.  Signatures with
a controller-anchor collision have probability zero and were removed.  Finally,
conditioning each involved block to a clean domain can increase an event
probability by at most one factor `1/delta` per involved block, exactly as in
PP3ch and PP3ci. ∎

Since `H_{q,s}<=1`, this always improves the deletion-blind bound `G_delta`.

## 4. Deletion-aware all-block endpoint

### Theorem PP3cr -- PROVED

In PP3cn, the term `G_delta` may be replaced by `G_delta^{del}`.  Hence a valid
width-`2K` saturated no-three extension exists whenever

\[
 \boxed{
 \frac{L_*}{1-36\delta}+G_\delta^{\rm del}<1.
 }
\]

#### Proof

Repeat the proof of PP3cn, using PP3cq to bound the expected global certificate
mass. ∎

## 5. Scaling consequence and limitation

At the natural prime-gap block scale,

\[
 K=m^{0.525+o(1)},
 \qquad r=m^{0.475+o(1)},
\]

one has

\[
 \frac{4K}{m}=m^{-0.475+o(1)}.
\]

Thus `H_{q,s}=1-o(1)` for every fixed `q,s`.  The deletion-aware correction is
crucial for finite and dense-deletion regimes, and it removes exact
controller-anchor coincidences, but it does not by itself solve the asymptotic
prime-gap-scale retained-shadow problem.  The remaining theorem must compress
the number of distinct controlled signatures, not merely rely on random deletion
of their anchors.
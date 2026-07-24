# Boundary-shadow density dichotomy

PP3ea turns dense slot domains into a source-cell-clean square-root macro patch.
This chapter gives a direct sufficient condition and its exact failure
alternative in terms of boundary-strip cell shadow.

## 1. Blocked-edge counts by label

Use the notation of PP3ea.  Let `A_0` be a candidate set of `L_M` new movement
rows and `B_0` a candidate set of `L_R` new refill columns.  For `A in A_0`, put

\[
 b_M(A)
 =
 |\{e=(x,y)\in E:(x,A)
 \text{ lies on a secant through two points of }F\}|.
\]

Define `b_R(B)` analogously for cells `(B,y)`.

For `0<epsilon<1/2`, call a label **epsilon-good** when its blocked-edge count is
at most `epsilon R`.

### Proposition PP3ee -- PROVED

If there are at least `W` epsilon-good movement labels and at least `W`
epsilon-good refill labels, then the compatibility graph

\[
 G_{1-2\epsilon}
\]

of PP3ea is complete on the chosen labels.  Consequently, for sufficiently
large `R`, they support a source-cell-clean internally no-three macro patch of
width

\[
 \boxed{
 \left\lfloor\frac{(1-2\epsilon)\sqrt R}{16}\right\rfloor.
 }
\]

#### Proof

For one good movement label `A` and one good refill label `B`, their safe edge
sets have sizes at least `(1-epsilon)R`.  Their intersection therefore has size
at least `(1-2epsilon)R`.  Every chosen label pair is compatible with
`gamma=1-2epsilon`, so PP3eb applies. ∎

## 2. Exact failure concentration

Define the total movement and refill boundary shadows

\[
 \mathcal S_M
 =
 \sum_{A\in A_0}b_M(A),
 \qquad
 \mathcal S_R
 =
 \sum_{B\in B_0}b_R(B).
\]

### Corollary PP3ef -- PROVED

If fewer than `W` movement labels are epsilon-good, then

\[
 \boxed{
 \mathcal S_M
 >
 \epsilon R(L_M-W).
 }
\]

The analogous statement holds for refill labels.  Hence failure of the easy
PP3ee criterion forces a blocked-cell core occupying a positive fraction of one
candidate boundary strip.

#### Proof

If fewer than `W` labels have blocked count at most `epsilon R`, then more than
`L_M-W` labels have blocked count greater than `epsilon R`.  Sum their
contributions. ∎

### Corollary PP3eg -- PROVED

If

\[
 \mathcal S_M=o(RL_M),
 \qquad
 \mathcal S_R=o(RL_R),
\]

and `W=o(L_M),o(L_R)`, then one may take `epsilon=o(1)` in PP3ee.  The resulting
macro width is

\[
 (1-o(1))\frac{\sqrt R}{16},
\]

and the conditional cell and ordinary-pair marginals are respectively
`O(1/R)` and `O(1/R^2)`.

#### Proof

Choose `epsilon` tending to zero but larger than both normalized shadow
densities and larger than `W/L_M,W/L_R`.  Corollary PP3ef then guarantees at
least `W` good labels in each direction.  Apply PP3ee and PP3ec. ∎

## 3. Hall-type refinement

The good-label criterion is deliberately stronger than necessary.  Even when a
movement label or refill label individually blocks more than `epsilon R` edges,
it may have large intersections with many labels on the other side.

### Proposition PP3eh -- PROVED

If the compatibility graph `G_gamma` has minimum degree at least `W/2` on both
sides, then PP3ea applies.

#### Proof

PP3ed gives a perfect matching in `G_gamma`, which is the only compatibility
input required by PP3ea. ∎

Thus a failed macro patch forces either:

1. a large boundary cell-shadow core as in PP3ef; or
2. a structured Hall obstruction in the label-pair intersection matrix.

Both alternatives are concrete targets for cycle flips, protected rectangles,
or tomographic trades.

## 4. Global label allocation

For several disjoint matching pools, the candidate new-coordinate region may be
larger than the final installed width.  One may first assign each pool a label
reservoir of size `L` and then retain only `W=Theta(sqrt R)` good labels.
Disjointness of the final selected label sets is sufficient; unused labels cost
no row or column degree.

Consequently, a global preparation theorem may work with oversampling:
construct disjoint candidate strips of size `L>>sqrt R`, prove normalized
shadow `o(1)` in most strips, and invoke PP3eg.  The final extension width counts
only the selected labels.
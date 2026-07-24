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

and `W=o(L_M),o(L_R)`, then one may select `W` good labels in each direction and
their abstract compatibility graph is complete with density parameter
`1-o(1)`.

#### Proof

Choose `epsilon` tending to zero but larger than both normalized shadow
densities and larger than `W/L_M,W/L_R`.  Corollary PP3ef then guarantees at
least `W` good labels in each direction. ∎

This corollary is a label-selection statement only.  Turning a selected subset
of numerical labels into a width-`W` saturated grid patch requires the selected
new rows and columns to be exactly the final new coordinates, or requires a
separate saturation-preserving allocation theorem.

## 3. Hall-type refinement

The good-label criterion is deliberately stronger than necessary.  Even when a
movement label or refill label individually blocks more than `epsilon R` edges,
it may have large intersections with many labels on the other side.

### Proposition PP3eh -- PROVED

If the compatibility graph `G_gamma` on the `W` labels that will actually be
installed has minimum degree at least `W/2` on both sides, then PP3ea applies.

#### Proof

PP3ed gives a perfect matching in `G_gamma`, which is the only compatibility
input required by PP3ea. ∎

Thus a failed macro patch forces either:

1. a large boundary cell-shadow core as in PP3ef; or
2. a structured Hall obstruction in the label-pair intersection matrix.

Both alternatives are concrete targets for cycle flips, protected rectangles,
or tomographic trades.

## 4. Coordinate-budget warning

A numerical label in `[m+1,m+L]` is an actual row or column of the final grid.
If a construction selects only `W<L` labels and inserts no points on the other
labels, then it is not saturated on `[m+L]^2`.  Reinterpreting it as a patch on
`[m+W]^2` also fails when a selected label exceeds `m+W`.  An arbitrary
order-preserving compression of the selected labels does not preserve
collinearity in general.

Therefore unused numerical labels are **not free**.  The earlier informal
oversampling shortcut is invalid without an additional interface.  Two valid
uses of a larger candidate reservoir are:

1. prove that the selected labels already form the complete consecutive final
   coordinate set;
2. allocate all final new labels globally among several macro variables, so
   every new row and column is used exactly twice.

The second option leads to a global balanced label-allocation and matching
problem.  It can still exploit average boundary-shadow information, but it must
cover every final label rather than discard the labels not chosen by one macro.
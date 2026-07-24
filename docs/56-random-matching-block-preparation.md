# Random matching-block preparation and global profile cancellation

The full width-two block endpoint PP3ci is stated after the matching layer has
already been divided into labelled blocks.  This chapter performs that division
randomly.  The factors contributed by random block membership cancel the
`1/r`, `1/r^2`, and `1/r^3` state probabilities in PP3ci, reducing the
preparation problem to global normalized incidence counts on one perfect
matching layer.

## 1. Uniform labelled equipartitions

Let `P` be a perfect matching of size `m`.  Fix integers `K,r>=1` with `Kr<=m`.
Choose disjoint labelled sets

\[
 E_1,\ldots,E_K\subseteq P,
 \qquad |E_i|=r,
\]

uniformly from all ordered choices.  Edges outside their union remain fixed.
For a finite set `R` of distinct source edges and a map
`phi:R -> {1,...,K}`, write

\[
 s_i=|\phi^{-1}(i)|,
 \qquad s=|R|.
\]

### Proposition PP3ck -- PROVED

The probability that every edge `e in R` belongs to its prescribed block
`E_{phi(e)}` is

\[
 \boxed{
 \frac{\prod_i (r)_{s_i}}{(m)_s}.
 }
\]

#### Proof

Expose the ordered block positions as `Kr` labelled slots, with `r` slots of
each block label, and fill them by a uniformly random injection from `P`.  The
specified `s` edges occupy distinct slots.  There are `(m)_s` possible ordered
slot images for them, while exactly `prod_i (r)_{s_i}` images use the prescribed
block labels. ∎

This formula remains valid when `Kr<m`; the unassigned source edges simply
occupy the unused positions.

## 2. Random balancing of local-cleaning signatures

Reserve one width-two interval for every block label.  Before choosing the
partition, form the following labelled signature families on source edges.

- `B_*`: a block label, two possible retained block edges, a distinct controller
  edge, and a controller candidate cell collinear with the two retained points.
- `A_{1,*}`: a block label, one possible retained block edge, a distinct
  controller edge, and a feasible same-edge movement/refill pair collinear with
  the retained point.
- `A_{2,*}`: a block label, one possible retained edge, two distinct controller
  edges, and a feasible ordinary patch pair collinear with the retained point.

Let their cardinalities be `B_*`, `A_{1,*}`, and `A_{2,*}`.  For a realised
block `E_i`, let `B_i,A_{1,i},A_{2,i}` be the corresponding signatures whose
source edges all lie in `E_i`, and define the PP3ca load

\[
 \lambda_i=
 \frac{4B_i}{r}
 +\frac{4A_{1,i}}{r}
 +\frac{12A_{2,i}}{r(r-1)}.
\]

### Proposition PP3cl -- PROVED

For the uniform labelled equipartition,

\[
 \boxed{
 \mathbb E\sum_i\lambda_i
 =
 \frac{4(r-1)(r-2)B_*}{(m)_3}
 +\frac{4(r-1)A_{1,*}}{(m)_2}
 +\frac{12(r-2)A_{2,*}}{(m)_3}.
 }
\]

#### Proof

A `B_*` signature or an `A_{2,*}` signature uses three distinct source edges
and survives exactly when all three enter its prescribed block.  PP3ck gives
probability `(r)_3/(m)_3`.  An `A_{1,*}` signature uses two distinct edges and
has probability `(r)_2/(m)_2`.  Multiply by the three coefficients in
`lambda_i` and simplify. ∎

Write the displayed expectation as `L_*`.

## 3. Global deletion-blind certificate profiles

For every block label and every source edge, expose the four width-two support
cells controlled by that edge: two movement cells and two refill cells.  Count
candidate collinear triples before choosing the partition.  Ignore source-edge
deletions when making these counts, so they are deletion-blind upper bounds.
Discard a candidate signature if one source edge would have to belong to two
different block labels.

Use the following seven global labelled counts.

- `M_1`: two source points and one candidate cell controlled by one edge in one
  prescribed block.
- `M_h`: one source point and a same-edge movement/refill pair in one block.
- `M_2`: one source point and an ordinary pair controlled by two distinct edges
  in one block.
- `M_{11}`: one source point and one cell in each of two prescribed blocks.
- `M_{h1}`: a same-edge pair in one block and one cell in another block.
- `M_{21}`: an ordinary pair in one block and one cell in another block.
- `M_{111}`: one cell in each of three prescribed blocks.

Let `W_delta` denote the PP3ci left side after a partition is realised, using a
common clean-domain density lower bound `delta`.

### Proposition PP3cm -- PROVED

For `0<delta<=1`,

\[
 \mathbb E W_\delta\le G_\delta,
\]

where

\[
 \boxed{
 G_\delta=
 \frac{2M_1+M_h}{\delta m}
 +\frac{8(r-1)M_2}{\delta r(m)_2}
 +\frac{4M_{11}+2M_{h1}}{\delta^2(m)_2}
 +\frac{16(r-1)M_{21}}{\delta^2r(m)_3}
 +\frac{8M_{111}}{\delta^3(m)_3}.
 }
\]

#### Proof

A one-edge signature enters its prescribed block with probability `r/m`.  A
two-edge same-block signature has probability `(r)_2/(m)_2`; a two-block
one-edge-per-block signature has probability `r^2/(m)_2`.  Similarly, a
`2+1` signature has probability `(r)_2r/(m)_3`, and a three-block signature has
probability `r^3/(m)_3`.  Multiply these probabilities by the seven coefficients
in PP3ci and simplify.  Deletion-blind counting and duplicate controlled
signatures can only increase the expectation. ∎

The important feature is that the leading powers of `r` cancel.  Apart from the
harmless factors `(r-1)/r`, the resulting criterion is normalized by `m`,
`m^2`, and `m^3`, not by the block scale.

## 4. An all-block preparation theorem

The canonical adjacent geometry is one of the 36 full width-two geometries.  If
`lambda_i<1`, PP3ca gives at least

\[
 (1-\lambda_i)\binom r4
\]

clean canonical states.  Therefore the full 36-state bank in block `i` has clean
density at least `(1-lambda_i)/36`.

Fix `0<delta<1/36` and put

\[
 \tau=1-36\delta.
\]

Call a block under-dense if `lambda_i>tau`.  The number `U` of under-dense
blocks satisfies

\[
 U\le\frac{1}{\tau}\sum_i\lambda_i.
\]

### Theorem PP3cn -- PROVED

If

\[
 \boxed{
 \frac{L_*}{1-36\delta}+G_\delta<1,
 }
\]

then some labelled equipartition gives a valid saturated no-three extension of
width `2K`.

#### Proof

For a random equipartition,

\[
 \mathbb E(U+W_\delta)
 \le
 \frac{L_*}{1-36\delta}+G_\delta<1.
\]

Hence one partition satisfies `U+W_delta<1`.  Since `U` is a nonnegative
integer, this forces `U=0`; every block then has full-bank clean density at least
`delta`.  It also gives `W_delta<1`.  Apply PP3ci to the independent uniform
choices from the clean block domains.  Equal margins preserve two points in
every row and column. ∎

Unlike an argument that discards bad blocks, PP3cn uses every reserved new
coordinate interval.  This is essential: leaving an interval unused would break
saturation, and compressing the remaining coordinates need not preserve
collinearity.

## 5. Prime-gap-scale interpretation

Take

\[
 K\asymp m^{0.525},
 \qquad
 r\asymp m^{0.475},
 \qquad Kr\le m.
\]

PP3cn reduces the constant-width route to two global estimates on one matching
layer:

1. the labelled local-signature expression `L_*` must be small enough that every
   block retains density at least `delta`;
2. the normalized global profile expression `G_delta` must be below the
   remaining unit budget.

The target is no longer a separate regularity statement for each of
`m^0.525` blocks.  It is a global secant-shadow and anchored-pair count whose
random equipartition automatically distributes controller edges to the block
scale.

The theorem is sufficient, not necessary.  Deletion-aware profile counts,
nonuniform block-state measures, or a local-lemma analysis after the partition
can all improve the displayed bound.
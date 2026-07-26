# Terminal high-support source pencils are converted or impossible

PP3ann--PP3ant reduce residual positive support at a marked centre to a support-
free helper block or a terminal fixed-core pencil with `N^(1-o(1))` variable
extensions.  This chapter closes the high-support **source** classes inside that
terminal alternative.

For inserted collinear triples, the completion theorem PP3jk says that fixing all
other endpoint indices determines the last index.  A growing fixed-core pencil is
therefore impossible.

For a rank-four anchored pair, fixing the marked centre and the two nonvariable
helper indices fixes one inserted cell and one row or column of the other.  A
retained source anchor determines the variable cell uniquely.  Hence a terminal
pencil with many variable extensions uses equally many distinct retained anchors.
After layer and controller-status refinement, those anchors form a target-size
credited endpoint bank.

Thus no high-support source class remains as a terminal near-linear pencil.

## 1. Typed rank-four anchored-pair pencil

Fix a canonical rank-four anchored-pair orientation containing the marked centre
`c`.  Fix two further helper indices so that three of the four endpoint indices
are fixed, and let `v` be the variable fourth index.

The two compatible inserted cells have distinct rows and distinct columns.  In the
chosen orientation, the variable index supplies exactly one coordinate of one
cell:

```text
(x_v,y_0)
```

or, after transposition,

```text
(x_0,y_v),
```

while the other inserted cell is fixed.

For every positive variable extension, choose one retained source anchor `p`
collinear with the two inserted cells.

### Proposition PP3anu -- PROVED

Fix the canonical orientation, the three nonvariable endpoint indices, and one
retained source anchor `p`.  Then `p` witnesses at most one variable endpoint
index `v`.

#### Proof

In the fixed-row form, the line through the fixed inserted cell and `p` meets the
row `y=y_0` in at most one point.  The line cannot equal that row because the two
compatible inserted cells have distinct rows.  Pool endpoint indices have
distinct old columns, so at most one index supplies the intersection column.
The fixed-column form is transposed. ∎

No divisor multiplicity is present after the three endpoint indices and the
anchor are fixed.

## 2. Distinct-anchor population

Let a typed anchored-pair pencil have `H` distinct variable extensions.

### Corollary PP3anv -- PROVED

The chosen witness anchors contain at least `H` distinct retained source points.

#### Proof

Assign one anchor to every positive extension.  Proposition PP3anu makes the map
from extensions to anchors injective. ∎

The conclusion counts physical source points, not witness multiplicity.

## 3. Layer and controller-class refinement

The saturated retained source is the union of two permutation layers.  Active
controllers are partitioned into `M` pools; a retained anchor outside all pools is
called free.

### Proposition PP3anw -- PROVED

From `H` distinct anchors in PP3anv one can extract a row/column-disjoint endpoint
bank of size at least

```text
ceil(ceil(H/2)/(M+1))
```

that is either entirely free or entirely contained in one controller pool.

#### Proof

Pigeonhole the two source permutation layers.  Anchors in one layer have distinct
old rows and columns.  Partition that same-layer family into the free class and
the `M` controller-pool classes; one class has at least the displayed average. ∎

Every selected anchor carries one designated anchored-pair certificate.

### Proposition PP3anx -- PROVED

Moving a selected anchor in the endpoint bank removes its chosen anchored-pair
certificate incidence while preserving saturation.  In the free case the fixed
controller infrastructure is unchanged; in the one-pool case the trade is pool-
compatible.  Thus the bank is a credited endpoint bank in the sense of PP3aad.

#### Proof

The selected anchors lie in one permutation layer and have pairwise distinct rows
and columns, so an endpoint derangement preserves saturation.  Every moved anchor
is absent from its designated collinearity certificate afterward.  The chosen
certificate records are distinct because their variable endpoint extensions are
distinct.  Controller preservation and pool compatibility are exactly the two
cases of the class refinement. ∎

As in the transition-bank theorem, removing one chosen witness incidence does not
assert that the inserted pair had no second witness; all remaining source and
insertion collateral is charged separately.

## 4. Slab-scale anchored-pair conversion

Use

```text
N=m^(19/20+o(1)),
M=m^(1/20+o(1)),
W=m^(19/40+o(1)).
```

### Theorem PP3any -- PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE

A terminal anchored-pair pencil of size

```text
H=N^(1-o(1))
```

contains a free or one-pool credited endpoint bank of size

```text
N^(1-o(1))/M=m^(9/10-o(1))=omega(W).
```

Consequently it has a target-size subbank entering the recapture-free,
source-valid marked-filler, positive-support avoidance, or robust final-state
conversion chains.

#### Proof

Apply PP3anw and use the displayed scales.  The resulting bank is credited by
PP3anx.  Restrict it to size `W` and apply PP3afn--PP3anm. ∎

Thus a near-linear anchored-pair support pencil is converted rather than retained
as a source-host obstruction.

## 5. Inserted-triple unique completion

Consider one fixed canonical orientation of an inserted collinear triple whose
total endpoint-index support has rank `h in {4,5,6}` and contains the marked
centre.  Fix `h-1` endpoint indices and vary the last index `v`.

### Proposition PP3anz -- PROVED

For each fixed orientation, at most one variable endpoint index `v` completes the
three inserted cells to a compatible collinear triple.

#### Proof

This is the completion argument PP3jk.  In rank four, fix three indices so that
two cells and the old column or row of the third are known; their nonaxis line
meets that coordinate fibre once.  Rank five fixes four indices, and rank six
fixes five, with the same final line--coordinate intersection.  Distinct pool
rows and columns identify at most one endpoint index at the intersection. ∎

Finite orientation pigeonholing changes the bound only by an absolute constant.

### Corollary PP3aoa -- PROVED

No rank-four, rank-five, or rank-six inserted-triple source class can realize the
terminal pencil alternative PP3anr with a growing number of variable extensions,
let alone `N^(1-o(1))` extensions.

#### Proof

After fixing the canonical class and typed orientation, PP3anz bounds the
extension count by one.  Before orientation pigeonholing the count is bounded by
an absolute constant. ∎

## 6. Revised terminal-source endpoint

### Corollary PP3aob -- PROVED

The near-linear terminal support pencil from PP3ans cannot remain a high-support
source obstruction.

1. A rank-four anchored-pair pencil yields a target-size credited endpoint bank.
2. A rank-four, rank-five, or rank-six inserted-triple pencil is impossible by
   unique completion.
3. Unary and transition source pencils are already converted by PP3amk--PP3amq
   and PP3zj--PP3aaj.

Therefore the remaining terminal pencils are insertion-support geometries or
external endpoint-host failures, not unconverted source-validity classes.

### Corollary PP3aoc -- PROVED

The live marked-centre frontier is narrowed to:

1. fixed/nested **insertion** pencils and support-free insertion weight at the
   removal-credit scale;
2. external endpoint-host or controller-pool compatibility failure;
3. controller-puncture reserve exhaustion;
4. one-step monotone-potential branches outside robust final allocation.

The no-three-in-line conjecture remains unproved.
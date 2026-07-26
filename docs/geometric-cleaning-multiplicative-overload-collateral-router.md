# Created-collateral structure from a multiplicative destroyed-factor overload

**Branch:** `research/geometric-cleaning`

GC2bw--GC2ca remove non-destroyed resources from the event Hall system and reduce the
remaining external obstruction to one exact destroyed factor whose Hall capacity is too
large relative to the event's raw gain density.  This note converts that multiplicative
ratio into geometric structure on the factors created by the same rectangle event.

The key point is elementary but useful: low gain density means that most destroyed weight is
replaced by newly created collateral.  Every newly created factor must meet one of the two
inserted rectangle cells, so a constant fraction localizes to one inserted-cell anchor and
then enters the existing rank/pair/star router.

## Exact event ledger

Fix one hard-legal rectangle event `j`.  Let

`Dsum_j=sum_(p in D_j)w_p>0`

be the total weight of exact current factors destroyed by `j`, let `Nsum_j>=0` be the total
weight of exact factors newly created by `j`, and let

`g_j=Dsum_j-Nsum_j>0`.

Put

`lambda_j=g_j/Dsum_j in (0,1]`.

For `p in D_j`, the raw gain-row coordinate is

`q_p=lambda_j*w_p`.

Assume the destruction-faithful Hall capacity is factor-conservative:

`0<=c_p<=w_p`.

Let the two inserted rectangle cells be `x_j,y_j`.  Every created factor has rank at most
`r`, with `r=3` in the no-three-in-line constraint ledger.

## GC2cb -- multiplicative overload forces large created collateral -- PROVED

Suppose one destroyed factor occurrence `p_*` satisfies

`R_*=c_(p_*)/q_(p_*)>1`.

Then

`lambda_j<=1/R_*`

and hence

`Nsum_j>= (1-1/R_*)*Dsum_j`.

More generally, if `R_*>=kappa>1`, then

`Nsum_j>= (1-1/kappa)*Dsum_j`.

### Proof

Since `c_(p_*)<=w_(p_*)` and `q_(p_*)=lambda_j*w_(p_*)`,

`R_*=c_(p_*)/(lambda_j*w_(p_*))<=1/lambda_j`.

Therefore `lambda_j<=1/R_*`.  Using
`Nsum_j=Dsum_j-g_j=(1-lambda_j)Dsum_j` gives the result. QED.

Thus the multiplicative obstruction is exactly a low-gain/high-collateral event.

## GC2cc -- every created factor meets an inserted cell -- PROVED

Every exact factor newly created by `j` contains at least one of `x_j,y_j`.

### Proof

The rectangle event changes the permutation layer only by deleting its two current cells and
inserting `x_j,y_j`.  A factor whose complete support avoids both inserted cells has the same
cell/label data after the event as before it.  Such a factor cannot change from absent to
present.  Therefore every newly created factor meets at least one inserted cell. QED.

If a created factor contains both inserted cells, assign it canonically to `x_j`; otherwise
assign it to the inserted cell it contains.

## GC2cd -- one inserted-cell/rank fibre retains a constant fraction -- PROVED

Partition the created-factor weight first by its canonical inserted-cell anchor in
`{x_j,y_j}` and then by rank in `{1,...,r}`.  One exact anchor/rank fibre has total weight at
least

`Nsum_j/(2*r)`.

For rank at most three, one fibre has weight at least `Nsum_j/6`.

### Proof

There are at most `2r` classes and their weights sum to `Nsum_j`.  Weighted pigeonhole gives
the bound. QED.

This rank split is physical: aliases of the same exact factor remain one weighted
occurrence.

## GC2ce -- lower-rank collapse or a created-collateral star -- PROVED

Let `q` be the selected inserted-cell anchor and let its selected rank fibre have weight
`W_q`.  Fix an integer `Delta>=1`.

1. If the rank is one, the fibre is an atomic created-factor overload at the exact cell `q`
   of total weight `W_q`.
2. If the rank is two, exactly one of the following holds:
   - some pair `{q,z}` has more than `Delta` created factor occurrences;
   - there is a family of rank-two factors through `q`, pairwise disjoint outside `q`, of
     total weight at least `W_q/Delta`.
3. If the rank is three, exactly one of the following holds:
   - some pair `{q,z}` belongs to more than `Delta` created factor occurrences;
   - there is an endpoint-disjoint family of created rank-three factors through `q`, pairwise
     disjoint outside `q`, of total weight at least

     `W_q/(2*Delta-1)`.

### Proof

The rank-one statement is immediate.  In rank two, group parallel occurrences by their
second endpoint `z`.  If every group has at most `Delta` occurrences, order the occurrences
inside each group and colour them by their local index in `{1,...,Delta}`.  Every colour
class contains at most one occurrence at each `z`, hence is disjoint outside `q`; one class
carries at least `W_q/Delta` weight.  Otherwise one pair has multiplicity greater than
`Delta`.

For rank three, form the weighted link multigraph at `q`; one edge occurrence represents the
other two cells of one created factor.  If every link vertex has occurrence degree at most
`Delta`, a greedy edge colouring uses at most `2Delta-1` colours.  One colour class is a
matching and carries at least a `1/(2Delta-1)` fraction of the total weight.  Otherwise one
pair has codegree greater than `Delta`. QED.

Parallel exact occurrences are retained in the multiplicity/codegree count and in the
weight ledger.

## GC2cf -- quantitative collateral continuation -- PROVED

Under the multiplicative overload ratio `R_*>1`, one of the following exact outputs holds:

1. an atomic created-factor fibre at one inserted cell of weight at least

   `(1-1/R_*)*Dsum_j/(2*r)`;
2. a created pair through one inserted cell with occurrence codegree greater than `Delta`;
3. an endpoint-disjoint rank-two or rank-three created-collateral star of weight at least

   `(1-1/R_*)*Dsum_j/[2*r*(2*Delta-1)]`.

For the rank-three ledger `r=3`, the uniform star guarantee is

`(1-1/R_*)*Dsum_j/[6*(2*Delta-1)]`.

### Proof

Apply GC2cb, then GC2cd and GC2ce.  The rank-two star has the stronger denominator `Delta`,
which is at most `2Delta-1`, so the displayed uniform bound holds. QED.

The star is prospective newly created collateral, not current payment.  It must be installed,
charged back, or routed through the existing GC4 conflict/overload machinery before it can
be used as descent.

## GC2cg -- complete multiplicative-overload collateral router -- PROVED

For every destruction-faithful capacity-deficient event star, the external branch now has
one exact continuation:

1. a destruction-faithful Hall deficit;
2. raw one-event overlap giving executable descent;
3. or one exact destroyed-factor multiplicative overload, which forces the created-collateral
   structure of GC2cf at one of the event's two inserted cells.

Thus the multiplicative ratio is no longer an unstructured terminal obstruction.  It returns
an atomic created factor, a high created pair codegree, or an endpoint-disjoint created-
collateral star with an explicit fraction of the destroyed weight.

### Proof

Use GC2ca for the first trichotomy and apply GC2cf in its third branch. QED.

## Corrected GC frontier

The live external-star obstruction is now prospective collateral at one exact inserted
cell.  The next obligation is to show that its atomic/pair/star output either conflicts with
bounded current structure, admits a GC4-compatible installation, or pays through an exact
created-factor chargeback.  Other open interfaces remain isolated-cell prospective stars,
pool depletion, global context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_multiplicative_overload_collateral.py` exhausts small exact event
ledgers and weighted created-factor links and samples larger systems.  It checks the
multiplicative collateral inequality, inserted-cell support wall, rank localization,
rank-two multiplicity extraction, rank-three codegree/star dichotomy and the final
quantitative constants.
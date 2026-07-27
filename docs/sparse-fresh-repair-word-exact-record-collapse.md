# Exact-record collapse of fresh repair-word mass

**Branch:** `research/sparse-algebraic-spread`

SAS5ei--SAS5em split every pair-local-minimal repaired union into matched opposite-side mass or fresh
residual repair mass.  The fresh branch localizes to one of the twelve repair-word types, but operations
in the selected bank need not use the same swap endpoints.  The repairing operation must therefore be
localized before the row/column arithmetic is applied.

This note performs that localization explicitly.  After an ordered repair-operation loss of at most
`N(N-1)`, collinearity gives `binom(N,3)` exact records in a fixed double-scope operation fibre and
`(N-2)binom(N,3)` in a fixed singleton fibre.  Thus a fresh word class still contains one
quantitatively heavy exact residual record.

## Exact repair-operation model

Fix a balanced colouring on `N>=3` columns.  Every fresh residual record is assigned
occurrence-faithfully to one **distinguished ordered repairing swap**

`omega=(x,y)`,

meaning that the twelve-word classification is evaluated with `x` in its first declared swap role and
`y` in its second.  There are at most

`K_op=N*(N-1)`

ordered repair-operation addresses.

This is the **repair-operation address contract**.  If a local pair operation repairs a record without a
canonical distinguished swap to which SAS5j applies, the exact operation address is returned as an
unrealized-operation branch rather than being included below.

An exact rank-three record has ordered row positions

`r_1<r_2<r_3`

and three distinct scope columns.  Required labels at columns outside `{x,y}` equal their current
colouring labels, while the repair word fixes the required post-swap labels at participating swap
columns.

Let `W_f>0` be fresh residual weight in one fixed repair-word type after exact alias aggregation.  The
weight is residual in the sense of SAS5ei: it is the excess `(r_Q-o_Q)_+` at each exact record.  The same
record may still have smaller matched opposite-side weight.

## SAS5en -- ordered repair-operation localization -- PROVED

One ordered repairing swap `omega=(x,y)` carries fresh residual weight at least

`W_omega>=W_f/[N*(N-1)]`.

### Proof

Partition the occurrence-faithful fresh residual ledger by its distinguished ordered repairing swap.
There are at most `N(N-1)` addresses.  Weighted pigeonhole gives the bound. QED.

The ordering absorbs the `X/Y` orientation and prevents a hidden factor of two later.

## SAS5eo -- double-scope exact address stock -- PROVED

Fix the ordered operation `omega=(x,y)` and one double-scope repair word `XY_(ij)`, with remaining
position `k`.  For every row triple there is at most one third column:

`c_k=x+[(r_k-r_i)/(r_j-r_i)]*(y-x)`.

Consequently the complete exact-record stock in this fixed operation/word fibre is at most

`K_double=binom(N,3)`.

### Proof

The word fixes `x,y` at ordered positions `i,j`.  Two fixed cells determine one rational line, so
evaluation at row `r_k` determines at most one rational third column.  A standard-grid record exists
only when that value is integral, in range and distinct from `x,y`.  The outside required label is then
forced by the current colouring.  Thus each row triple gives at most one exact record. QED.

No additional third-column factor is present after the operation fibre is fixed.

## SAS5ep -- singleton exact address stock -- PROVED

Fix `omega=(x,y)` and one singleton repair word `X_i` or `Y_i`.  Let `u` be its participating swap
column and let the other swap column be excluded from the record scope.  Let `j` be the smaller of the
two remaining ordered positions and let `k` be the other.

For each row triple and each choice

`z in [N]\{x,y}`

at position `j`, collinearity determines at most one column at position `k`:

`c_k=u+[(r_k-r_i)/(r_j-r_i)]*(z-u)`.

Hence the exact-record stock in the fixed operation/word fibre is at most

`K_single=(N-2)*binom(N,3)`.

For `N=3` the singleton stock is empty.

### Proof

The canonical address consists of the row triple and the column `z` at the fixed remaining position
`j`.  The two cells at positions `i,j` determine the rational line and therefore the final column at
position `k`.  Integrality, range and distinctness decide whether the record exists.  Required labels at
both outside columns are forced by the current colouring.  There are `N-2` choices for `z` and
`binom(N,3)` row triples. QED.

The canonical choice of position `j` prevents a further factor of two.

## SAS5eq -- fresh word to one exact residual record -- PROVED

Let one repair-word type carry fresh residual weight `W_f` under the repair-operation address contract.
Then one exact record has fresh residual weight at least:

- double-scope:

  `W_f/[N*(N-1)*binom(N,3)]`;

- singleton-scope:

  `W_f/[N*(N-1)*(N-2)*binom(N,3)]`.

Uniformly for `N>=4`, one exact residual record has weight at least

`W_f/K_fresh`,

where

`K_fresh=N*(N-1)*(N-2)*binom(N,3)`.

### Proof

Apply SAS5en and choose a fixed ordered operation fibre of weight at least `W_f/[N(N-1)]`.  Partition
that fibre over its exact records and apply SAS5eo or SAS5ep.  The uniform stock uses the singleton-safe
bound. QED.

The selected object is a physical exact record, not only a word, column or rational family.

## SAS5er -- integrated exact fresh-record router -- PROVED UNDER THE REPAIR-OPERATION ADDRESS CONTRACT

In the fresh branch of SAS5em, the selected repair-word type has weight at least

`B_pair/[24*(D_pair+1)]`.

Therefore one exact fresh residual record has weight at least:

- double-scope:

  `B_pair/[24*(D_pair+1)*N*(N-1)*binom(N,3)]`;

- singleton-scope:

  `B_pair/[24*(D_pair+1)*N*(N-1)*(N-2)*binom(N,3)]`.

Uniformly for `N>=4`, the denominator is

`24*(D_pair+1)*N*(N-1)*(N-2)*binom(N,3)`.

For double-scope pairs one may substitute `D_pair<=4Lambda`; for singleton pairs one may substitute
`D_pair<=20Lambda`.

Thus every line or dilation common-step bank has one continuation:

1. one exact adjacent pair or repair-operation address fails realization;
2. an executable compatible batch gives positive energy descent;
3. a column-incidence cap fails;
4. a matched opposite-side exact-record bank has weight at least
   `B_pair/[2*(D_pair+1)]`;
5. or one exact fresh residual record has the displayed bound.

The positive base-row branch retains its separate row-translation realization gate.

### Proof

SAS5em gives alternatives 1--4 or the fresh word lower bound.  In the fresh branch apply SAS5eq and
substitute `W_f>=B_pair/[24(D_pair+1)]`. QED.

## Corrected SAS6 frontier

After the necessary operation-address localization, the fresh repaired branch still collapses to one
exact physical rank-three record with a polynomially explicit weight.

The remaining work is therefore:

- realize every primitive adjacent-pair operation and its distinguished repairing swap;
- turn the matched exact-record bank into a physically compatible composition or cancellation;
- route the heavy fresh exact record through the active-record, donor or progression machinery;
- realize positive base-row translations;
- and handle reflected-board boundary and high-incidence profiles.

## Finite check

`scripts/verify_sparse_fresh_repair_exact_record.py` enumerates board orders, row triples and all twelve
word positions.  It checks unique rational reconstruction for fixed double-scope operation fibres,
canonical single-column addressing for singleton fibres, the ordered-operation and exact-record stock
bounds, and the weighted integrated pigeonhole constants.

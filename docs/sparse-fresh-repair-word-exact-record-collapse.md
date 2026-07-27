# Exact-record collapse of fresh repair-word mass

**Branch:** `research/sparse-algebraic-spread`

SAS5ei--SAS5em split every pair-local-minimal repaired union into matched opposite-side mass or fresh
residual repair mass.  The fresh branch already localizes to one of the twelve repair words, but it still
appears to carry a free column parameter.

This note removes that freedom.  Once the repair word is fixed, collinearity gives a finite exact-record
address stock: `binom(N,3)` for a double-scope word and `(N-2)binom(N,3)` for a singleton word.  Thus a
fresh word class contains one quantitatively heavy exact residual record.

## Exact repair-word model

Fix a balanced colouring on `N>=3` columns and a cross-label swap

`omega={x,y}`.

An exact rank-three record has ordered row positions

`r_1<r_2<r_3`

and three distinct scope columns.  Required labels at columns outside `{x,y}` equal their current
colouring labels, while the repair word fixes the required post-swap labels at the participating swap
columns.

Let `W_f>0` be fresh residual weight in one fixed repair word after exact alias aggregation.  The weight
is residual in the sense of SAS5ei: it is the excess `(r_Q-o_Q)_+` at each exact record.  The same record
may still have smaller matched opposite-side weight.

## SAS5en -- double-scope exact address stock -- PROVED

Fix one double-scope repair word `XY_(ij)`, with remaining position `k`.  For every row triple there is at
most one third column:

`c_k=x+[(r_k-r_i)/(r_j-r_i)]*(y-x)`

with the obvious exchange of `x,y` according to the ordered word positions.

Consequently the complete exact-record stock in this word is at most

`K_double=binom(N,3)`.

### Proof

The word fixes the columns `x,y` at ordered positions `i,j`.  Two fixed cells determine one rational
line, so evaluation at row `r_k` determines at most one rational third column.  A standard-grid record
exists only when that value is integral, in range and distinct from `x,y`.  The outside required label
is then forced by the current colouring.  Thus each row triple gives at most one exact record. QED.

No additional third-column factor is present.

## SAS5eo -- singleton exact address stock -- PROVED

Fix one singleton repair word `X_i` or `Y_i`.  Let `u` be its participating swap column and let `v` be
the other swap column, which is excluded from the record scope.  Let `j` be the smaller of the two
remaining ordered positions and let `k` be the other.

For each row triple and each choice

`z in [N]\{x,y}`

at position `j`, collinearity determines at most one column at position `k`:

`c_k=u+[(r_k-r_i)/(r_j-r_i)]*(z-u)`.

Hence the exact-record stock in the singleton word is at most

`K_single=(N-2)*binom(N,3)`.

For `N=3` the singleton stock is empty.

### Proof

The canonical address consists of the row triple and the column `z` at the fixed remaining position
`j`.  The two cells at positions `i,j` determine the rational line and therefore the final column at
position `k`.  Integrality, range and distinctness decide whether the record exists.  Required labels at
both outside columns are forced by the current colouring.  There are `N-2` choices for `z` and
`binom(N,3)` row triples. QED.

The canonical choice of position `j` prevents a factor of two.

## SAS5ep -- fresh word to one exact residual record -- PROVED

Let one repair word carry fresh residual weight `W_f`.

- If it is double-scope, one exact record has fresh residual weight at least

  `W_f/binom(N,3)`.

- If it is singleton-scope, one exact record has fresh residual weight at least

  `W_f/[(N-2)*binom(N,3)]`.

In either nonempty case, one exact record has fresh residual weight at least

`W_f/K_fresh`,

where

`K_fresh=(N-2)*binom(N,3)`

is the uniform safe stock for `N>=4`.

### Proof

Partition the fresh residual word weight over its exact records after alias aggregation.  Apply weighted
pigeonhole with the stocks from SAS5en and SAS5eo.  The uniform bound uses
`K_double<=K_fresh` for `N>=4`. QED.

The selected object is a physical exact record, not only a word, column or rational family.

## SAS5eq -- integrated fresh-record bound -- PROVED

In the fresh branch of SAS5em, the selected repair word has weight at least

`B_pair/[24*(D_pair+1)]`.

Therefore one exact fresh residual record has weight at least:

- double-scope:

  `B_pair/[24*(D_pair+1)*binom(N,3)]`;

- singleton-scope:

  `B_pair/[24*(D_pair+1)*(N-2)*binom(N,3)]`.

Uniformly for `N>=4`, one exact residual record has weight at least

`B_pair/[24*(D_pair+1)*(N-2)*binom(N,3)]`.

For double-scope pairs one may substitute `D_pair<=4Lambda`; for singleton pairs one may substitute
`D_pair<=20Lambda`.

### Proof

SAS5em supplies the fresh word lower bound.  Apply SAS5ep and substitute the relevant address stock.
QED.

## SAS5er -- exact fresh-record router -- PROVED

Every line or dilation common-step bank now has one continuation:

1. one exact adjacent pair fails realization;
2. an executable compatible batch gives positive energy descent;
3. a column-incidence cap fails;
4. a matched opposite-side exact-record bank has weight at least
   `B_pair/[2*(D_pair+1)]`;
5. or one exact fresh residual record has the SAS5eq lower bound.

The positive base-row branch retains its separate row-translation realization gate.

### Proof

Apply SAS5em.  Alternatives 1--4 are unchanged.  In its fresh word branch, apply SAS5eq. QED.

## Corrected SAS6 frontier

The fresh repaired branch no longer ends at a word/column class.  It collapses to one exact physical
rank-three record with a polynomially explicit weight.

The remaining work is therefore:

- realize every primitive adjacent-pair operation;
- turn the matched exact-record bank into a physically compatible composition or cancellation;
- route the heavy fresh exact record through the active-record, donor or progression machinery;
- realize positive base-row translations;
- and handle reflected-board boundary and high-incidence profiles.

## Finite check

`scripts/verify_sparse_fresh_repair_exact_record.py` enumerates board orders, row triples and all twelve
word positions.  It checks unique rational reconstruction for double-scope words, canonical
single-column addressing for singleton words, the exact stock bounds and the weighted integrated
pigeonhole constants.

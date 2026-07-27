# Low-order profile dictionary for product-star collateral

**Branch:** `research/geometric-cleaning`

GC2cx--GC2db execute a compatible paid current-star family by an independent product of allowed matching banks.  Every new rank-three certificate touches at most three moved star blocks, but the previous router retained only the number of touched blocks.

This note refines that residual to the complete block-occupancy dictionary.  There are exactly six matching-cell profiles, only three of them are genuinely cross-star, and each profile has one explicit product-spread denominator and one finite block-tuple stock.

## Product certificate notation

Use the compatible product bank from GC2cx.  For one prospective rank-three certificate `Q`, let

`r_i(Q)`

be the number of its required replacement-matching cells in star block `i`.  Put

`r(Q)=sum_i r_i(Q)<=3`.

Delete zero entries from the vector `(r_i(Q))` and sort the remaining positive entries in decreasing order.  Call the resulting partition

`lambda(Q)`.

The remaining `3-r(Q)` cells of `Q` lie in the fixed configuration `Z` from GC2cz.

For one block of size `t`, write

`(t)_r=t(t-1)...(t-r+1)`.

## GC2dc -- exact six-profile partition -- PROVED

Every compatible rank-three product certificate belongs to exactly one of the six profiles

`(1)`, `(2)`, `(3)`, `(1,1)`, `(2,1)`, `(1,1,1)`.

Their physical meanings are:

1. `(1)`: one matching cell from one block and two fixed `Z` cells;
2. `(2)`: two matching cells from one block and one fixed `Z` cell;
3. `(3)`: three matching cells from one block;
4. `(1,1)`: one matching cell from each of two blocks and one fixed `Z` cell;
5. `(2,1)`: two matching cells from one block and one from another;
6. `(1,1,1)`: one matching cell from each of three blocks.

The first three are precisely the one-block ranks already counted by the single-star AN4 inventory.  The last three are the complete genuinely cross-star dictionary.

### Proof

The positive entries of `(r_i(Q))` form a partition of an integer `r(Q)` in `{1,2,3}`.  The partitions of one, two and three are exactly

`(1)`;

`(2),(1,1)`;

`(3),(2,1),(1,1,1)`.

The number of fixed `Z` cells is `3-r(Q)`.  No other profile is possible. QED.

## GC2dd -- exact profilewise product-spread denominators -- PROVED

For compatible prescribed matching cells, the containment probabilities satisfy the following bounds.

For one block `i`:

`p_(1)(i)<=128/t_i`,

`p_(2)(i)<=128/(t_i)_2`,

`p_(3)(i)<=128/(t_i)_3`.

For two distinct blocks `i,j`:

`p_(1,1)(i,j)<=128^2/(t_i t_j)`,

`p_(2,1)(i,j)<=128^2/((t_i)_2 t_j)`,

where the ordered pair records which block contributes two cells.  The symmetric orientation uses `128^2/(t_i (t_j)_2)`.

For three distinct blocks `i,j,l`:

`p_(1,1,1)(i,j,l)<=128^3/(t_i t_j t_l)`.

Any forbidden or internally incompatible prescription has probability zero.

### Proof

Inside each touched block, AN1 bounds a prescribed compatible partial matching of rank `r` by `128/(t_i)_r`.  The product-bank choices are independent, so multiply the blockwise bounds.  GC2dc lists all possible blockwise rank vectors. QED.

## Profile-weight notation

Give each prospective exact certificate `Q` its weight `w_Q` and define its normalized expected contribution

`e_Q=w_Q*prod_(i:r_i(Q)>0) 128/(t_i)_(r_i(Q))`.

For a profile `lambda`, let

`E_lambda=sum_(Q:lambda(Q)=lambda)e_Q`.

Then

`E_prod=sum_lambda E_lambda`

with the sum over the six profiles of GC2dc.

## GC2de -- weighted localization to one profile and one block tuple -- PROVED

If `E_prod>=H>0`, then one of the six profiles carries normalized expected mass at least

`H/6`.

Fix a profile carrying mass `V`.  Then one exact physical block tuple carries at least:

- `V/k` for any one-block profile `(1)`, `(2)` or `(3)`;
- `V/binom(k,2)` for `(1,1)`;
- `V/[k(k-1)]` for the oriented profile `(2,1)`;
- `V/binom(k,3)^(-1)` for `(1,1,1)`.

The last expression means `V/binom(k,3)` when `k>=3`.

### Proof

The six profile masses sum to `E_prod`, so weighted pigeonhole gives `H/6`.  A one-block profile has at most `k` block choices.  Profile `(1,1)` has one unordered pair, profile `(2,1)` has one ordered pair specifying the double block, and profile `(1,1,1)` has one unordered triple.  A second weighted pigeonhole gives the displayed bounds. QED.

## GC2df -- one-block versus genuine cross-star reduction -- PROVED

Suppose product neutralization fails to produce descent and, after separating the fixed-switch term, the residual expected collateral is at least `H>0`.

Then one of the following holds:

1. **one-block return:** an exact star block carries an AN4 rank-one, rank-two or rank-three normalized collateral profile of mass at least `H/(6k)`;
2. **two-block bridge:** one exact block pair carries a `(1,1)` profile of mass at least `H/[6 binom(k,2)]`;
3. **oriented two-one chord:** one exact ordered block pair carries a `(2,1)` profile of mass at least `H/[6k(k-1)]`;
4. **three-block transversal:** one exact block triple carries a `(1,1,1)` profile of mass at least `H/[6 binom(k,3)]`.

If a denominator stock is zero, the corresponding branch is absent.

### Proof

Apply GC2de.  Profiles `(1)`, `(2)` and `(3)` are all one-block AN4 terms, so they combine into alternative 1 without creating a new cross-star object.  The remaining three profiles are exactly alternatives 2--4. QED.

Thus product failure no longer leaves an unspecified one-, two- or three-star interaction.  Its matching-cell occupancy is one of three named cross-star geometries.

## GC2dg -- refined product-collateral router -- PROVED UNDER THE PRODUCT-CERTIFICATE CONTRACT

A compatible paid current-star bank now has the following exact continuation:

1. strict product cleaning descent;
2. large fixed-switch collateral `F_prod`;
3. a one-block AN4 return;
4. one exact `(1,1)` bridge between two star blocks;
5. one exact oriented `(2,1)` chord between two star blocks;
6. one exact `(1,1,1)` three-block transversal;
7. a named failure of block disjointness, product legality, certificate completeness or occurrence-faithful payment.

Every noncontract geometric failure carries the explicit normalized mass from GC2df.

### Proof

GC2db separates descent, fixed-switch collateral and residual product collateral.  GC2dc--GC2df partition and localize that residual.  A failed product hypothesis is recorded before the probability calculation and therefore remains a distinct physical output. QED.

## Corrected GC frontier

The compatible current-star product branch is now reduced to three genuinely cross-star profiles:

- a two-block bridge with one fixed cell;
- an oriented two-one chord;
- a three-block transversal.

One-block profiles return to the existing AN4 inventory.  The live geometric task is to classify these three cross-star profiles by shared lines, inserted-cell anchors, repeated endpoints or bounded cause labels, then combine that classification with labelled paid-overload recursion, high created-pair multiplicity and the remaining identity-sensitive or unbounded recycling branches.

## Finite check

`scripts/verify_geometric_product_collateral_profiles.py` exhausts all block-count vectors of total rank at most three, checks that exactly the six stated partitions occur, computes exact local matching containment probabilities in small degree-two forbidden banks, verifies product factorization and tests the profile/block-tuple weighted localization bounds.
# Curvature import for heavy final records from matched-square barriers

**Branch:** `research/sparse-algebraic-spread`

SAS5fm--SAS5fq turn a high matched-square barrier into one heavy exact current final record.  The
record is changed by a unique selected operation square, so its complete two-swap address is already
known.  This note applies the conjunction four-state table at that address.  A final-positive record
cannot be an active negative record: it is either composed-only positive curvature or a neutral
one-swap repair which survives the other swap.  Thus the full heavy-record weight enters an existing
positive-barrier/negative-collateral or neutral-repair ledger without any further operation, word,
column or exact-record loss.

## Final-output square model

Fix one exact final-positive record `Q` of weight `H>0` supplied by SAS5fo.  Interaction independence
assigns it to the unique selected square `a`, with disjoint balanced swaps `sigma` and `tau`.  Let

`(I_0,I_sigma,I_tau,I_sigmatau)`

be its four exact indicators in the base, two single-swap and composed states.  Because `Q` is a
final-positive output,

`I_0=0`,

`I_sigmatau=1`.

Assume the existing conjunction-table and two-swap realization contracts.  Define

`chi_Q=I_0-I_sigma-I_tau+I_sigmatau`.

## SAS5fr -- final-positive table dichotomy -- PROVED

The table of `Q` is exactly one of:

1. composed-only positive:

   `(0,0,0,1)`, with `chi_Q=1`;

2. neutral `sigma` repair:

   `(0,1,0,1)`, with `chi_Q=0`;

3. neutral `tau` repair:

   `(0,0,1,1)`, with `chi_Q=0`.

No active negative table is possible.

### Proof

SAS5es classifies every conjunction-compatible repaired table with `I_0=0`.  Imposing
`I_sigmatau=1` removes the two single-swap-only negative tables, leaving exactly the three displayed
possibilities. QED.

## SAS5fs -- composed-only final output enters the exact barrier router -- PROVED

In the composed-only branch, `Q` contributes exact positive mixed-curvature weight `H` for the fixed
square `(sigma,tau)`.

If either single swap improves the energy, that swap is an immediate descent.  Otherwise
`Delta_sigma,Delta_tau>=0`.  For every `eta in (0,1)`, either

`C_minus>=eta*H`

for the negative mixed collateral at the same square address, or

`Delta_a>(1-eta)*H`.

Any improving composed square necessarily satisfies

`C_minus>H`.

### Proof

The table `(0,0,0,1)` has curvature `+1`.  If a single-swap increment is negative, use it directly.
Otherwise substitute the full `+H` contribution into

`Delta_a=Delta_sigma+Delta_tau+H+C_plus-C_minus`

and apply SAS5eu. QED.

The operation square and exact record are already fixed by SAS5fo, so no localization loss occurs.

## SAS5ft -- neutral final output is a persistent one-swap repair -- PROVED

In either neutral branch, exactly one of `sigma,tau` creates `Q` from the base colouring and the other
swap preserves it in the composed final state.  The full weight `H` therefore enters one exact
original- or donor-swap repair ledger with zero mixed-curvature charge.

If several such records are collected, their creating operations enter SAS5ex--SAS5fb and the unified
realized repair/opposite-ledger router SAS5fc--SAS5fg.

### Proof

For `(0,1,0,1)`, `sigma` creates and `tau` preserves; for `(0,0,1,1)`, the roles reverse.  These are
exactly the neutral persistent tables of SAS5ev. QED.

## SAS5fu -- high-barrier exact-record continuation -- PROVED UNDER THE DECLARED CONTRACTS

Let an original matched bank have weight `M`, square interaction degree `D_sq`, final-output stock
`K_out` and density threshold `lambda>0`.  In the high-barrier branch of SAS5fp, one exact final record
has weight

`H>lambda*M/[2(D_sq+1)K_out]`.

That full lower bound has one continuation:

1. one of its two single swaps gives direct energy descent;
2. it is composed-only positive and, for every `eta in (0,1)`, gives negative mixed collateral greater
   than or equal to

   `eta*lambda*M/[2(D_sq+1)K_out]`

   or a composed-square barrier greater than

   `(1-eta)*lambda*M/[2(D_sq+1)K_out]`;
3. it is neutral persistent and enters one exact realized one-swap repair ledger with the same weight;
4. or one output-stock, conjunction-table, square-address, legality or boundary field fails.

### Proof

Apply SAS5fr.  SAS5fs gives alternatives 1--2, SAS5ft gives alternative 3, and the lower bound from
SAS5fo is unchanged because no further pigeonhole step is used. QED.

## SAS5fv -- neutral and common-step final-output bounds -- PROVED

Let

`A_neu=(2N-3)(4Lambda_rep+1)`.

For the neutral matched branch, every heavy final exact record from SAS5fq has weight greater than

`lambda*W_neu/[4A_neu(D_sq+1)K_out]`.

For a common-step pair bank, the corresponding bound is

`lambda*B_pair/[4(D_pair+1)(D_sq+1)K_out]`.

Each bound enters SAS5fu unchanged.  Thus both prior matched-bank sources now end at direct one-swap
descent, quantified negative mixed collateral or positive barrier, a neutral realized repair ledger, or
a named physical contract failure.

### Proof

These are the exact high-record bounds from SAS5fq.  Apply SAS5fu with no additional address or record
loss. QED.

## Corrected SAS6 frontier

A heavy final current record from the matched-square barrier router no longer waits for a new
classifier.  Its unique square address and final-positive table send its full mass directly to a
single-swap descent, the existing positive-curvature barrier/negative-collateral ledger, or a neutral
persistent repair bank.

The remaining sparse work is choosing and paying a useful global barrier-density scale, resolving the
resulting positive barriers or negative collateral, batching the imported neutral repairs when their
incidence cap fails, realizing matched-square contracts for every word family, positive base-row
realization and reflected-boundary/high-incidence branches.

## Finite check

`scripts/verify_sparse_final_output_curvature_import.py` enumerates all conjunction-compatible
final-positive four-state tables, checks the two-case curvature classification, samples exact
barrier/negative-collateral identities and verifies propagation of the general, neutral and common-step
heavy-record bounds without further loss.

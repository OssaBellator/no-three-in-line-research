# Paying installed negative-record banks with their opposite destroyers

**Branch:** `research/sparse-algebraic-spread`

SAS5gg--SAS5gk give a lossless table-and-energy trichotomy for a low-cost installed negative bank.
That theorem can stop at an opposite base barrier, current-only payment or composed-only output without
executing the retained destroyers.  This note adds the physical continuation: every installed record
retains a legal opposite constituent swap, and the complete opposite-destroyer stage is executed.

Either the destruction stage pays the bank by quantified energy descent, or its complete new-output
ledger is itself a large realized one-swap word/column bank.  Combining the creator and destroyer stages
gives an actual net descent whenever the creator-density scale is smaller than the destruction margin.

## Installed bank and opposite-destroyer model

Fix a low-cost installed bank from SAS5gf.  For every selected square `a`, let:

- `R_a>0` be its installed exact negative-record weight;
- `gamma_a` be its creator swap;
- `delta_a` be the retained legal opposite destroyer after `gamma_a`;
- `F_a>=0` be the total weight of exact records absent immediately before `delta_a` and present after it;
- `Xi_a` be the energy change of `delta_a` from the installed state.

Put

`R=sum_a R_a`,  `F=sum_a F_a`.

Assume the **opposite-destroyer payment contract**:

1. the installed square family remains interaction independent after the creator stage;
2. all opposite destroyers are jointly legal when executed simultaneously from the installed state;
3. every selected installed record is destroyed by its own `delta_a`;
4. the complete exact rank-three ledger contains every record changed by the destruction stage;
5. no complete exact record scope meets two selected destroyer supports;
6. every new record retains its destroyer operation, one of the twelve one-swap word labels and its
   three physical columns;
7. aliases are aggregated before summation;
8. failure returns the least destruction-legality, support, scope, record, word, alias or boundary field.

Additional destroyed current records are allowed and only improve the payment estimate.

## SAS5gl -- exact opposite-destroyer payment inequality -- PROVED

For every selected square,

`Xi_a<=F_a-R_a`.

For the simultaneous opposite-destroyer stage,

`T(kappa^(Gamma Delta))-T(kappa^Gamma)<=F-R`.

### Proof

The destroyer removes every selected record of total weight `R_a`.  Every newly present exact record is
counted in `F_a`, while additional destroyed records only lower the energy change.  This gives the local
inequality.  Complete-scope independence makes every exact record respond to at most one selected
destroyer, so the simultaneous complete-ledger difference is the sum of the local differences. QED.

## SAS5gm -- destruction descent or realized output bank -- PROVED

Fix `epsilon in (0,1)`.  Exactly one of the following weighted alternatives holds:

1. `F<=(1-epsilon)R`, and the simultaneous destruction stage decreases energy by at least `epsilon R`;
2. `F>(1-epsilon)R`, and the final state contains a distinct realized one-swap output bank of total
   weight greater than `(1-epsilon)R`.

### Proof

In the first branch apply SAS5gl.  In the second branch, the complete output ledger consists of exact
records present after the jointly legal destruction stage; alias aggregation makes their union distinct
and its weight is `F`. QED.

## SAS5gn -- fresh word and column localization -- PROVED

In the output-bank branch of SAS5gm, one of the twelve retained one-swap word classes has realized weight
greater than

`(1-epsilon)R/12`,

and one physical column in that word class has record-incidence weight greater than

`(1-epsilon)R/(4N)`.

### Proof

Weighted pigeonhole over the twelve word labels gives the first bound.  Every exact rank-three record
contributes its weight to three distinct physical columns.  Pigeonhole over the `N` columns gives
`3[(1-epsilon)R/12]/N=(1-epsilon)R/(4N)`. QED.

The output is physically present after the destruction stage.  It enters the realized repair-bank
router once its declared opposite ledger is supplied.

## SAS5go -- net two-stage descent or recycling -- PROVED

Suppose the creator stage has energy cost at most `kappa_0 R`, with

`0<kappa_0<epsilon<1`.

Then either:

1. the complete creator-then-destroyer operation decreases energy from the original base state by at
   least

   `(epsilon-kappa_0)R`;

2. the final state contains realized output weight greater than `(1-epsilon)R`, with the word and column
   bounds of SAS5gn;

3. or one creator-stage or opposite-destroyer payment field fails.

### Proof

In the destruction-descent branch, add creator cost at most `kappa_0R` to destruction change at most
`-epsilon R`.  The net change is at most `-(epsilon-kappa_0)R`.  The other branch is SAS5gm--SAS5gn.
QED.

## SAS5gp -- integrated installed-negative-bank payment router -- PROVED UNDER THE DECLARED CONTRACTS

Let the original matched bank have weight `M` and square interaction degree `D_sq`.  In the low-cost
installation branch of SAS5gf,

`R>(1-theta)lambda M/[16(D_sq+1)]`.

For `0<kappa_0<epsilon<1`, one has:

1. net two-stage energy descent greater than

   `(epsilon-kappa_0)(1-theta)lambda M/[16(D_sq+1)]`;

2. or one final realized one-swap word has weight greater than

   `(1-epsilon)(1-theta)lambda M/[192(D_sq+1)]`,

   and one physical column in that word class has incidence greater than

   `(1-epsilon)(1-theta)lambda M/[64N(D_sq+1)]`;

3. or the aggregate creator barrier alternative of SAS5gf holds;
4. or one creator, opposite-destroyer, complete-ledger, word, incidence, alias or boundary field fails.

### Proof

Apply SAS5go and substitute the strict lower bound for `R`.  The word denominator gains the factor
twelve; the column denominator gains the factor `4N`.  Retain the high creator-barrier and failed
contract alternatives from SAS5gf. QED.

## Corrected SAS6 frontier

The algebraic installed-bank trichotomy now has a physical destroyer continuation.  A low-cost installed
negative bank either converts creator cost into strict net two-stage descent or recycles a constant
fraction into a physically realized one-swap word and column bank.

The remaining sparse work is supplying and paying the recycled output's opposite ledger, choosing global
`lambda,theta,kappa_0,epsilon` scales, proving creator/destroyer joint legality in every arithmetic word
family, resolving the aggregate creator-barrier branch, and the positive-base-row, high-incidence and
reflected-boundary profiles.

## Finite check

`scripts/verify_sparse_opposite_destroyer_payment.py` samples interaction-independent installed banks and
complete destruction-stage ledgers.  It checks the exact destruction inequality, simultaneous
additivity, the descent/output dichotomy, twelve-word and column localization, net two-stage descent and
the integrated matched-bank constants.

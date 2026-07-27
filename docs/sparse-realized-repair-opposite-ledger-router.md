# Opposite-ledger routing for realized repair banks

**Branch:** `research/sparse-algebraic-spread`

SAS5ei--SAS5em compare the repaired union from a common-step pair bank with its declared opposite destruction ledger.  SAS5ex--SAS5fb now produce a second kind of genuinely realized union: a simultaneous compatible bank of neutral persistent one-swap repairs.

This note gives one exact-record comparison theorem for both sources.  The repair side must be physically realized and distinct after simultaneous execution; the opposite side remains an exact weighted destruction ledger.  The result is an alias-safe matched cancellation or a fresh repair word and column with explicit mass.

## Realized exact repair-bank model

Let `J` be a simultaneously executable operation bank.  Assume the **realized repair-bank contract**:

1. every selected operation is legal in the declared common state;
2. the complete exact-record ledger contains every affected rank-three record;
3. selected repaired exact records are present after simultaneous execution;
4. selected repaired records are distinct after exact alias aggregation;
5. every repaired occurrence retains its repairing operation, one of the twelve repair-word labels and its three physical scope columns;
6. the opposite destruction ledger is alias-aggregated on the same exact-record universe;
7. failure returns the least operation, record, alias, label, incidence or boundary field.

For each exact record `Q`, let

`r_Q>=0`

be its selected realized repair weight and

`o_Q>=0`

its weight in the declared opposite destruction ledger.  Put

`R_J=sum_Q r_Q`.

Define

`m_Q=min(r_Q,o_Q)`,

`f_Q=(r_Q-o_Q)_+`,

`M_J=sum_Q m_Q`,

`F_J=sum_Q f_Q`.

## SAS5fc -- universal realized overlap/fresh identity -- PROVED

Every realized repair bank has the exact decomposition

`R_J=M_J+F_J`.

Consequently

`max(M_J,F_J)>=R_J/2`.

### Proof

For each exact record,

`r_Q=min(r_Q,o_Q)+(r_Q-o_Q)_+`.

Sum over the common alias-aggregated record universe.  One of the two nonnegative summands is at least half their total. QED.

The identity does not depend on how the compatible operation bank was extracted.

## SAS5fd -- physically realized matched cancellation ledger -- PROVED

The overlap weights `m_Q` pair realized repaired mass with opposite-side destruction mass record by record.  Subtracting `m_Q` from both sides leaves nonnegative residuals

`r_Q^res=r_Q-m_Q`,

`o_Q^res=o_Q-m_Q`

and preserves the signed ledger difference:

`sum_Q(r_Q-o_Q)=sum_Q(r_Q^res-o_Q^res)`.

Moreover, every repaired occurrence on the matched side is genuinely present after the simultaneous operation bank `J`; no prospective or unrealized repair mass enters `M_J`.

### Proof

The coordinatewise minimum is bounded by both ledger weights, so the residuals are nonnegative and equal subtraction preserves each coordinate difference.  Physical realization and distinctness are items 3 and 4 of the contract. QED.

This is exact signed-ledger cancellation.  It does not by itself assert that the operations defining the opposite destruction occurrences can be composed simultaneously with `J`.

## SAS5fe -- fresh realized repair localization -- PROVED

If `F_J>0`, one of the twelve repair-word classes carries fresh realized repair weight at least

`F_J/12`.

Inside that word class, one physical column carries fresh record-incidence weight at least

`F_J/(4N)`.

### Proof

Partition the positive fresh weights `f_Q` by the twelve retained repair-word labels.  A heaviest word has weight at least `F_J/12`.

Every exact rank-three record contributes its weight to three distinct physical columns.  The total weighted column incidence in the selected word class is therefore three times its word weight.  Weighted pigeonhole over the `N` board columns gives at least

`3(F_J/12)/N=F_J/(4N)`.

All records are present after `J` by the realized repair-bank contract. QED.

The selected column retains its exact endpoint, reconstructed-third-column or outside-column role.

## SAS5ff -- neutral repair/opposite-ledger dichotomy -- PROVED UNDER THE OPPOSITE-LEDGER CONTRACT

Let a swap-local-minimal neutral repair bank have original neutral weight `W_neu` and global incidence cap `Lambda`.  SAS5fb supplies a realized distinct repair union with

`R_J>=C_neu`,

where

`C_neu=W_neu/[(2N-3)(4Lambda+1)]`.

Then one of the following holds:

1. a matched realized repair/destruction exact-record bank has weight at least

   `C_neu/2`;
2. a fresh realized repair bank has weight at least `C_neu/2`, one repair word has weight at least

   `C_neu/24`,

   and one physical column in that word class has incidence at least

   `C_neu/(8N)`.

### Proof

Apply SAS5fc.  In the overlap branch use SAS5fd and `M_J>=R_J/2>=C_neu/2`.  In the fresh branch use SAS5fe with `F_J>=R_J/2>=C_neu/2`. QED.

Equivalently, the explicit fresh bounds are

`W_neu/[24(2N-3)(4Lambda+1)]`

for one word and

`W_neu/[8N(2N-3)(4Lambda+1)]`

for one column incidence.

## SAS5fg -- integrated realized-repair comparison router -- PROVED

For a neutral persistent repair bank of total weight `W_neu`, one of the following holds:

1. one creating swap, neutral table, exact record, opposite-ledger or realization field fails;
2. an endpoint-disjoint compatible improving batch gives energy descent at least

   `G_neu/[(2N-3)(4Lambda+1)]`;
3. the global incidence cap fails, yielding one physical column in more than `Lambda` exact record scopes;
4. at a swap-local minimum, a matched realized repair/opposite-destruction bank has weight at least

   `W_neu/[2(2N-3)(4Lambda+1)]`;
5. at a swap-local minimum, a fresh realized repair word has weight at least

   `W_neu/[24(2N-3)(4Lambda+1)]`,

   and one physical column in that word class has incidence at least

   `W_neu/[8N(2N-3)(4Lambda+1)]`.

The same universal lemmas SAS5fc--SAS5fe apply to the common-step pair repair bank of SAS5eh; substituting its retained repair lower bound recovers the SAS5el--SAS5em constants.

### Proof

Use the improving, high-incidence or local-minimum alternatives of SAS5fb.  In the local-minimum branch apply SAS5ff.  The final statement follows because SAS5fc--SAS5fe use only the realized repair-bank contract, which is also satisfied by the independent common-step bank after SAS5eg. QED.

## Corrected SAS6 frontier

Both common-step and neutral persistent repair unions now reach the same alias-safe opposite-ledger endpoint: exact matched cancellation or fresh realized word/column mass.  Neutral repairs no longer stop at an unclassified simultaneous union.

The remaining sparse work is physical composition or payment of the matched opposite-side bank beyond signed-ledger cancellation, resolution of positive barriers by negative mixed collateral, realization of positive base-row translations, and the reflected-boundary or high-incidence branches.

## Finite check

`scripts/verify_sparse_realized_repair_opposite_ledger.py` samples realized distinct repair ledgers and opposite destruction ledgers.  It checks exact overlap/fresh decomposition, signed residual preservation, the half-mass dichotomy, twelve-word and column localization, and the integrated neutral-batch constants.
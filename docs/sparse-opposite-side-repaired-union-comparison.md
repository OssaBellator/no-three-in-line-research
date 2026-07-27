# Opposite-side comparison for common-step repaired unions

**Branch:** `research/sparse-algebraic-spread`

SAS5ec--SAS5eh turn a weighted common-step parameter batch into a constraint-compatible subbank with
exact additive energy.  At a pair-local minimum, the selected operations return a distinct repaired
record union whose weight is at least the retained bottleneck mass.  The next issue is to compare that
union with the concentrated destruction family on the opposite energy side.

This note performs that comparison at the exact-record level.  Weighted aliases are aggregated first.
The repaired ledger then splits canonically into matched opposite-side mass and genuinely fresh repair
mass.  One of those two parts retains half the repaired weight; the fresh branch further localizes to
one of the twelve repair words and one physical column.

## Exact weighted ledgers

Let `I` be an independent pair-operation subbank supplied by SAS5ef--SAS5eh.  Aggregate exact-record
aliases as in SAS5ch.  Write

`r_Q>=0`

for the total weight with which exact record `Q` is repaired by the selected pair operations, and

`o_Q>=0`

for its weight in the declared opposite-side destruction ledger.

Put

`R_I=sum_Q r_Q`,

`O_I=sum_Q o_Q`.

At a pair-local minimum, SAS5eh gives

`R_I>=B_I`,

where `B_I` is the retained bottleneck mass and

`B_I>=B_pair/(D_pair+1)`.

Define the matched and fresh repaired weights recordwise by

`m_Q=min{r_Q,o_Q}`,

`f_Q=(r_Q-o_Q)_+`.

Let

`M=sum_Q m_Q`,

`F=sum_Q f_Q`.

## SAS5ei -- exact overlap-fresh identity -- PROVED

The repaired ledger has the exact disjoint decomposition

`R_I=M+F`.

Consequently

`max{M,F}>=R_I/2>=B_I/2`.

### Proof

For every exact record,

`r_Q=min{r_Q,o_Q}+(r_Q-o_Q)_+`.

Sum over `Q`.  One of two nonnegative summands in a decomposition of `R_I` is at least half the total.
Use `R_I>=B_I` for the final inequality. QED.

The identity is weighted and alias-safe; no record is duplicated by choosing a preferred operation.

## SAS5ej -- matched exact-record cancellation ledger -- PROVED

The overlap weights `m_Q` define an occurrence-faithful matching between repaired mass and
opposite-side destruction mass of total weight `M`.

Subtracting `m_Q` from both ledgers leaves nonnegative residuals

`r_Q^res=r_Q-m_Q`,

`o_Q^res=o_Q-m_Q`

and preserves their signed weight difference:

`sum_Q(r_Q-o_Q)=sum_Q(r_Q^res-o_Q^res)`.

If `M>=B_I/2`, the comparison therefore returns a paired exact-record bank of weight at least
`B_I/2` whose two sides may be cancelled in every subsequent difference ledger.

### Proof

The definition of `m_Q` never exceeds either record weight, so both residuals are nonnegative.  The
same quantity is subtracted from the repaired and opposite ledgers record by record, preserving their
difference.  Summing gives the stated identities. QED.

This is an accounting cancellation, not yet a claim that the operations producing the two occurrences
can be composed simultaneously.  Composition remains a separate physical compatibility question.

## SAS5ek -- fresh repair-word localization -- PROVED

Suppose `F>0`.  Relative to its repairing balanced operation, every fresh exact record belongs to one
of the twelve repair words from SAS5j.  Therefore one repair word carries fresh weight at least

`F/12`.

Every exact rank-three record has three distinct scope columns.  Inside the selected repair word, one
physical column has fresh record-incidence weight at least

`F/(4N)`.

In particular, if the fresh branch of SAS5ei holds, then one repair word carries at least `B_I/24`,
and one physical column in that word class carries incidence at least

`B_I/(8N)`.

### Proof

Partition the fresh exact records by the twelve repair words and choose a heaviest class.  Its weight
is at least `F/12`.

Sum weighted column incidences inside that class.  Every record contributes its weight to three
distinct columns, so the total column-incidence weight is three times the word-class weight.  One of
the `N` physical columns therefore carries at least

`3*(F/12)/N=F/(4N)`.

If `F>=B_I/2`, substitute that bound. QED.

The high-incidence column is weighted.  It may be a swap endpoint, reconstructed third column or an
outside column; the twelve-word and third-column dictionaries retain that exact role.

## SAS5el -- opposite-side comparison router -- PROVED

At a pair-local minimum, every independent common-step subbank has one of two exact continuations:

1. a matched repaired/destruction exact-record bank of weight at least `B_I/2`;
2. a genuinely fresh repaired bank of weight at least `B_I/2`, containing one repair word of weight
   at least `B_I/24` and one physical column of incidence at least `B_I/(8N)`.

The two branches are canonical after exact alias aggregation.

### Proof

Apply SAS5ei.  In the overlap branch use SAS5ej.  In the fresh branch use SAS5ek. QED.

Thus the destruction-side comparison cannot end in an unstructured repaired union: at least half is
exactly matched to the opposite ledger or at least half is fresh and concentrated in the finite word
and column dictionaries.

## SAS5em -- integrated common-step energy router -- PROVED UNDER THE OPPOSITE-LEDGER CONTRACT

Let a line or dilation pair bank have total bottleneck mass `B_pair` and interaction degree
`D_pair`.  Then at least one of the following holds:

1. one adjacent arithmetic pair fails the local pair-operation contract;
2. an executable compatible batch gives positive energy descent;
3. the column-incidence cap fails and yields one high-incidence physical column;
4. a matched opposite-side exact-record bank has weight at least

   `B_pair/[2*(D_pair+1)]`;

5. a fresh repair word has weight at least

   `B_pair/[24*(D_pair+1)]`,

   and one physical column in that word class has incidence at least

   `B_pair/[8*N*(D_pair+1)]`.

For double-scope pairs one may substitute `D_pair<=4Lambda`; for singleton pairs one may substitute
`D_pair<=20Lambda`.

The positive base-row chain retains its separate row-translation realization gate from SAS5eh.

### Proof

SAS5eh gives alternatives 1--3 or an independent pair-local-minimal subbank with

`B_I>=B_pair/(D_pair+1)`

and repaired union weight at least `B_I`.  Apply SAS5el and substitute the retained-mass bound. QED.

## Corrected SAS6 frontier

The common-step branch now reaches one of:

- an unrealized exact adjacent-pair operation;
- an improving additive batch;
- a high-incidence column;
- a large exact overlap with the opposite destruction ledger;
- or a fresh repaired word/column class with explicit mass.

The remaining arithmetic work is to realize every primitive pair operation, turn the matched
exact-record bank into a physically compatible composition or cancellation, run the existing
third-column and progression classifiers on the fresh word/column branch, realize positive base-row
translations and handle reflected-board boundary profiles.

## Finite check

`scripts/verify_sparse_opposite_side_repaired_union.py` exhausts small weighted record ledgers and
samples independent repaired unions.  It checks exact overlap/fresh decomposition, residual signed
weight preservation, the half-mass dichotomy, twelve-word localization, weighted column incidence and
the integrated `1/(D_pair+1)` constants.
# Superregular repair-transversal witness conservation

## Status

This note proves SRR2es--SRR2ew under the complete occurrence-faithful candidate/witness repair-source contract. It does not construct the tensor-reference repair graph and does not prove SRR2, SRR4 or the no-three-in-line conjecture.

## Setup

Fix the canonical burden repair transversal from SRR2en--SRR2er. Every selected incidence retains candidate, conditioned threshold, witness atom, physical source, repair class and epoch. A unit witness-source token is rooted only in initial stock or a named exogenous deposit. A valid transition consumes one predecessor and creates one successor in the same complete conditioned class. Issuing one selected repair incidence consumes one live token exactly once.

## Theorem block

**SRR2es (exact witness issuance).** Every selected burden-to-slot repair incidence backed by a live compatible candidate/witness occurrence is one actual unit debit.

**SRR2et (global conservation).** At every prefix,

`live witness-source tokens + issued repair incidences = initial tokens + named deposits`.

**SRR2eu (classwise conservation).** The identity holds separately for every complete candidate/witness/threshold/source class; changed conditioning or threshold is a reset.

**SRR2ev (transversal payment).** For deficit `delta`, class counts sum to `delta`, so one class carries at least `ceil(delta/|C|)` incidences. Exact balances pay the transversal or return the least overloaded witness-source class.

**SRR2ew (first failure).** The first violation is an exact source-less issuance, predecessor split, repeated debit, hidden deposit or conditioned-class mismatch. Omitted witness data, relabelling and unrecorded capacity reset.

## Proof

Induction through the event log preserves the global and classwise identities: deposits add one unit to both source and live accounts; valid transitions preserve live mass and complete class; valid issuance exchanges one live unit for one issued incidence. Every forbidden operation is detected at its first prefix. Summing classwise issued counts gives concentration.

## Remaining interface

The superregular work is to build the complete candidate/witness occurrence dictionary and verify a live compatible token for every selected burden incidence, or discharge the returned exact failure.
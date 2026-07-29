# Sparse typed repair-transversal neutral conservation

## Status

This note proves SAS5mi--SAS5mm under the complete typed occurrence-faithful boundary-neutral repair-source contract. It does not construct the neutral repair graph and does not prove SAS6 or the no-three-in-line conjecture.

## Setup

Fix the canonical pair/completion repair transversal from SAS5md--SAS5mh. Every selected incidence retains pair-or-completion type, sign, boundary profile, neutral move, legality class, physical source and epoch. A unit neutral-source token is rooted only in initial stock or a named exogenous deposit. A valid transition consumes one predecessor and creates one successor with the same complete boundary-neutral class. Issuing one selected incidence consumes one live token exactly once.

## Theorem block

**SAS5mi (exact typed issuance).** A selected pair/completion incidence backed by a live compatible neutral occurrence is one actual unit debit with sign, profile and legality fields preserved.

**SAS5mj (global conservation).** At every prefix,

`live neutral-source tokens + issued typed repair incidences = initial tokens + named deposits`.

**SAS5mk (classwise conservation).** The identity holds separately for every complete source/move/sign/profile/legality class; changing a retained field is a reset.

**SAS5ml (typed transversal payment).** The class counts of a deficit-`delta` transversal sum to `delta`, so one complete typed class carries at least `ceil(delta/|C|)` incidences. Exact balances pay the transversal or return the least overloaded boundary-neutral class.

**SAS5mm (first failure).** The first violation is an exact source-less issuance, predecessor split, repeated debit, hidden deposit or boundary-neutral class mismatch. Omitted legality, relabelling and unrecorded capacity reset.

## Proof

Induction on the event log preserves the global and classwise identities. Deposits add one unit to source and live accounts; valid transitions preserve mass and complete class; valid issuance exchanges one live token for one issued typed incidence. Any other event breaks an identity at its first prefix. Summing classwise issued counts proves concentration.

## Remaining interface

The sparse-algebraic work is to construct the complete neutral-source/move occurrence dictionary and verify one live compatible token for every selected pair/completion incidence, or discharge the returned exact failure.
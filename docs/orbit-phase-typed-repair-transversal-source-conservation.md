# Orbit-phase typed repair-transversal source conservation

## Status

This note proves OP4fi--OP4fm under the complete typed occurrence-faithful source-repair contract. It does not construct the unit-sensitive repair graph and does not prove OP5 or the no-three-in-line conjecture.

## Setup

Fix the canonical residual/edit repair transversal from OP4fd--OP4fh. Every selected incidence retains residual-or-edit type, unit class, valuation, holonomy, physical-source address and epoch. A unit repair-source token is rooted only in initial stock or a named exogenous deposit. A valid transition consumes one predecessor and creates one successor with the same complete unit-sensitive class. Issuing one selected incidence consumes one live token exactly once.

## Theorem block

**OP4fi (exact typed issuance).** A selected residual/edit incidence backed by a live compatible source occurrence is one actual unit debit with every unit-sensitive field preserved.

**OP4fj (global conservation).** At every prefix,

`live source tokens + issued typed repair incidences = initial tokens + named deposits`.

**OP4fk (classwise conservation).** The identity holds for each complete source/unit/valuation/holonomy class; changing a retained field is a reset.

**OP4fl (typed transversal payment).** The class counts of a deficit-`delta` transversal sum to `delta`, so one complete typed class carries at least `ceil(delta/|C|)` incidences. Current balances pay the transversal or return the least overloaded unit-sensitive source class.

**OP4fm (first failure).** The first violation is an exact source-less issuance, predecessor split, repeated debit, hidden deposit or unit-sensitive class mismatch. Unbounded unrecorded source creation, relabelling or omitted fields reset.

## Proof

Induction on the event log gives the global and classwise identities. Deposits add one source and one live token; valid transitions preserve total mass and class; valid issuance converts one live token into one issued typed incidence. Every other operation breaks an identity at its first prefix. Summing classwise issued counts proves concentration.

## Remaining interface

The orbit-phase work is to construct the complete unit-sensitive source dictionary and verify one live compatible token for every selected residual/edit incidence, or discharge the returned exact failure.
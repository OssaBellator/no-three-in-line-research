# Rational-inverse typed repair-transversal collateral conservation

## Status

This note proves RI5gc--RI5gg under the complete typed occurrence-faithful collateral repair-source contract. It does not construct the arithmetic repair graph and does not prove RI6 or the no-three-in-line conjecture.

## Setup

Fix the canonical owner/charge repair transversal from RI5fx--RI5gb. Every selected incidence retains owner-or-charge type, terminal arithmetic address, outside physical/collateral slot, source class and epoch. A unit collateral token is rooted only in initial stock or a named exogenous deposit. A valid transition consumes one predecessor and creates one successor with the same complete arithmetic class. Issuing one selected incidence consumes one live token exactly once.

## Theorem block

**RI5gc (exact typed issuance).** A selected owner/charge incidence backed by a live compatible collateral occurrence is one actual unit debit with its type and arithmetic fields preserved.

**RI5gd (global conservation).** At every prefix,

`live collateral tokens + issued typed repair incidences = initial tokens + named deposits`.

**RI5ge (classwise conservation).** The identity holds for every complete source/owner/charge/perturbation class; changing a retained field is a reset.

**RI5gf (typed transversal payment).** The class counts of a deficit-`delta` transversal sum to `delta`. One complete typed class carries at least `ceil(delta/|C|)` incidences, so exact class balances pay the transversal or return the least overloaded typed collateral class.

**RI5gg (first failure).** The first violation is an exact source-less issuance, predecessor split, repeated debit, hidden deposit or typed arithmetic-class mismatch. Omitted fields, relabelling and unrecorded replenishment reset.

## Proof

Induct on the event log. Named deposits add one unit to both the source and live sides. Valid transitions preserve token mass and complete arithmetic class. Valid issuance exchanges one live token for one issued typed incidence. These operations preserve the two identities, and each forbidden operation is detected at its first prefix. Summing classwise issued counts proves concentration.

## Remaining interface

The RI work is to build the complete physical/collateral occurrence dictionary and verify one live compatible source token for every selected owner/charge incidence, or discharge the returned exact failure.
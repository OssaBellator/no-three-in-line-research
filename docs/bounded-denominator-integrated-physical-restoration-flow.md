# Bounded-denominator integrated physical restoration flow

This note records BDA5en--BDA5er. It composes primitive-integer gain mass, source compatibility and restoration payment without preallocating physical potential to source classes.

## Contract

Fix finite physical potential classes `P`, primitive-integer source classes `S` and exact restoration classes `R`. Retain complete relations `P -> S` and `S -> R`. Physical and existing source balances, together with restoration demands, are nonnegative integers. All weights, gains and addresses remain fixed.

## Theorem block

### BDA5en — physical-potential split network

Physical potential and existing source potential feed one integral `P -> S -> R` network. Every paid restoration unit has one retained physical or existing-source predecessor.

### BDA5eo — simultaneous source issuance

Maximum flow chooses physical-to-source issuance and source-to-restoration payment simultaneously. A separately selected issuance can lose feasible restoration payment.

### BDA5ep — complete Hall/min-cut criterion

All restoration demand is paid exactly when every network cut has capacity at least total restoration demand.

### BDA5eq — canonical arithmetic cut

Failure returns one canonical minimum cut containing exact physical-potential, source and restoration classes. Its deficit equals unpaid primitive potential.

### BDA5er — reset boundary

Changed primitive weights, gain factors or compatibility, hidden potential creation, splitting, or missing predecessor lineage returns reset or amplification.

## Finite audit

Run `python scripts/verify_bda_integrated_physical_restoration_flow.py`.

The audit checks 6,000 systems: 21,142 physical-potential, 20,991 source and 21,025 restoration classes; 78,679 compatibility arcs; 74,078 physical-potential units; 63,239 restoration-demand units; 53,283 paid and 9,956 unpaid units; 2,242 deficient systems; 222 preissuance losses; and 84,144 exact Hall-subset checks.

## Scope

The result does not construct the arithmetic graph or prove its local gain factors. It does not prove BDA6 or the no-three-in-line conjecture.

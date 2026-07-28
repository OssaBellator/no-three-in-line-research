# Superregular integrated physical atom-burden flow

This note records SRR2cu--SRR2cy. It composes physical source issuance with atom-capacity payment at one exact threshold.

## Contract

Fix physical source classes `P`, witness atoms `A`, burden classes `B`, and complete relations `P -> A` and `A -> B`. Current physical mass, existing atom balances and exact burden demands are integral. Every burden unit retains its threshold and complete conflict witness.

## Theorem block

### SRR2cu — physical-to-atom split network

Physical source mass and existing atom capacity feed one integral `P -> A -> B` network.

### SRR2cv — simultaneous atom issuance

Maximum flow chooses physical atom-capacity issuance and burden payment simultaneously. Preassigning source mass to atoms can lose a feasible payment.

### SRR2cw — paid-burden execution interface

If all actual atom burden is paid, the earlier conditioned atom-budget theorem applies with the paid current balances and retains its executable-weight lower bound.

### SRR2cx — canonical source/atom/burden cut

Failure returns one canonical minimum cut with exact physical-source, witness-atom and burden classes; its deficit is unpaid conflict burden.

### SRR2cy — reset boundary

Missing conflict witnesses, changed thresholds, hidden atom deposits, splitting, source-less creation or incomplete compatibility returns reset or amplification.

## Finite audit

Run `python scripts/verify_srr_integrated_physical_atom_burden_flow.py`.

The audit checks 5,500 systems: 19,256 physical-source, 19,187 witness-atom and 19,355 burden classes; 74,385 compatibility arcs; 57,947 physical-source and 48,308 existing atom units; 58,285 burden units; 49,723 paid and 8,562 unpaid units; 1,976 deficient systems; and 165 preissuance losses.

## Scope

The theorem does not construct the geometric witness dictionary or prove concrete atom capacities and deposits. It does not prove SRR2, SRR4 or the no-three-in-line conjecture.

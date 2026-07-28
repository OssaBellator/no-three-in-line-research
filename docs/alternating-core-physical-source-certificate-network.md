# Alternating-core physical source/certificate network

This note records AC5dc--AC5dg. It composes the cumulative source/certificate bank with the physical source-lineage interface without preissuing source capacity.

## Contract

Fix finite physical source classes `P`, issued source classes `S`, certificate classes `C` and exact layer-defect classes `D`. Retain complete compatibility relations `P -> S`, `S -> C` and `C -> D`. Physical source mass, existing issued-source balances, certificate throughputs and defect demands are nonnegative integers. Every routed unit keeps its full physical and obstruction address.

## Theorem block

### AC5dc — four-layer split network

Physical source mass and existing issued-source balances feed one integral network through source classes, split certificate nodes and defect demands. Certificate node splitting enforces its exact throughput once.

### AC5dd — simultaneous issuance and payment

Maximum flow equals the largest defect mass that can be paid while choosing physical-source issuance and certificate routing simultaneously. No sequential issuance rule is assumed.

### AC5de — complete cut criterion

All defects are paid exactly when every source/certificate/defect network cut has capacity at least total defect demand.

### AC5df — canonical physical mixed obstruction

If payment fails, the canonical minimum cut retains exact physical-source, issued-source, certificate and defect classes. Its deficit is the unpaid defect mass and is the next physical target.

### AC5dg — reset boundary

Omitted compatibility, relabelled classes, hidden source creation, certificate splitting beyond retained throughput, or changed obstruction addresses returns reset or amplification rather than payment.

## Finite audit

Run `python scripts/verify_ac_physical_source_certificate_flow.py`.

The deterministic audit checks 5,000 systems: 17,595 physical-source, 17,356 issued-source, 17,495 certificate and 17,598 defect classes; 97,789 retained compatibility arcs; 44,510 defect-demand units; 29,792 paid and 14,718 unpaid units; 3,155 deficient systems; and 52 cases where greedy preissuance loses a feasible simultaneous solution.

## Scope

This theorem does not construct the geometric graph or prove its capacities and deposits. It does not prove AC4, AC5, AC6 or the no-three-in-line conjecture.

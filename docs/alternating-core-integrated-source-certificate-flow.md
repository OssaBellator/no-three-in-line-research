# Alternating-core integrated source/certificate/defect flow

This note records AC5cs--AC5cw. It composes the conserved certificate-source account with the layer-defect transport without first choosing certificate deposits.

## Contract

Fix one complete restricted-menu epoch. Let `S` be exact physical source classes, `C` exact certificate classes and `D` exact layer-defect classes. Source class `s` has current capacity `k_s`; certificate class `c` has issue/throughput capacity `q_c`; defect class `d` has integral demand `a_d`. The complete retained compatibility relations are `s -> c` and `c -> d`. All source, certificate, defect, obstruction and endpoint addresses are occurrence-faithful and fixed during the flow.

## Theorem block

### AC5cs — split-certificate network

Create a directed network

`source -> S -> C_in -> C_out -> D -> sink`,

with capacities `k_s` on source nodes, `q_c` on `C_in -> C_out`, `a_d` on `D -> sink`, and infinite capacity on declared compatibility arcs.

### AC5ct — exact integrated payment

Every integral flow unit is one physical source unit issued into one compatible certificate class and then spent on one compatible defect unit. Source capacity and certificate throughput are each debited once.

### AC5cu — cut criterion

All defect demand is paid if and only if the maximum integral flow has value `sum_d a_d`, equivalently every cut in the split-certificate network has capacity at least total demand.

### AC5cv — canonical mixed obstruction

If full payment fails, the residual minimum cut returns one exact mixed source/certificate/defect obstruction. Its deficit equals the unpaid defect mass. This cut is stronger than independently checking aggregate source stock and certificate-to-defect Hall inequalities, because both compatibility layers are enforced simultaneously.

### AC5cw — reset boundary

Omitted source/certificate or certificate/defect arcs, changing class labels, hidden source deposits, certificate splitting, nonadditive certificate capacity or payment-sensitive fields absent from the state return reset or amplification rather than payment.

## Proof

Integral max-flow applies because all capacities are integral. Node splitting enforces exact certificate throughput. Flow decomposition gives occurrence-faithful source/certificate/defect paths. Max-flow/min-cut gives the payment criterion and exact unpaid mass.

## Finite audit

Run `python scripts/verify_ac_integrated_source_certificate_flow.py`.

The deterministic audit samples finite split-certificate networks, verifies max-flow/min-cut equality, and counts systems where a greedy sequential certificate issue fails although the integrated network pays all demand.

## Scope

This is a conditional composition theorem. It does not construct the physical graph or prove AC5 or the no-three-in-line conjecture.
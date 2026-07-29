# Rational-inverse integrated physical-source collateral flow

This note records RI5dz--RI5ed. It combines physical source mass, collateral throughput and the joint owner/perturbation demand bank into one finite network, rather than issuing collateral before the final demand is known.

## Contract

Fix finite physical source classes `P`, collateral classes `C` and combined demand classes `D` containing both symmetric owner cost and compatibility-perturbation charge. Retain complete compatibility relations `P -> C` and `C -> D`, nonnegative integral physical source capacities, nonnegative integral collateral throughput capacities and exact integral demands. Every paid unit follows one retained path `p -> c -> d` and consumes one unit at both constrained layers.

## Theorem block

### RI5dz — split-collateral network

Split each collateral class into input and output vertices with its throughput capacity. Attach physical source capacities on the left and combined owner/charge demands on the right.

### RI5ea — simultaneous payment criterion

All combined demand is paid exactly when the maximum flow equals total demand. The integral max-flow theorem returns an occurrence-level path decomposition.

### RI5eb — no sequential issuance requirement

A preliminary choice of how much physical mass to issue to each collateral class may destroy a feasible final payment. The integrated network optimizes issuance and demand payment simultaneously.

### RI5ec — canonical mixed obstruction

If full payment fails, a canonical minimum cut retains exact physical source, collateral and owner/charge demand classes, with cut deficit equal to the unpaid mass.

### RI5ed — reset boundary

Changed owner, coherence, host, context, source occurrence, compatibility or capacity fields; source-less collateral creation; splitting; and payment outside a retained path return reset or amplification.

## Finite audit

Run:

`python scripts/verify_ri_integrated_physical_collateral_flow.py`

The deterministic audit checks 5,500 systems, 19,342 physical source classes, 19,170 collateral classes, 19,214 combined demand classes, 35,163 physical/collateral arcs, 32,011 collateral/demand arcs, 48,022 demand units, 23,196 paid units, 24,826 unpaid units and 247 systems where sequential preissuance fails although the integrated flow succeeds.

## Scope

This theorem does not prove the concrete arithmetic compatibility relations, capacities or exogenous source deposits. It does not prove RI6 or the no-three-in-line conjecture.
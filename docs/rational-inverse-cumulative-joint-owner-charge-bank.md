# Rational-inverse cumulative joint owner/charge bank

This note records RI5dp--RI5dt. It extends the one-epoch joint owner/charge transport to repeated epochs with shared named collateral deposits.

## Contract

Symmetric owner-cost classes and compatibility-perturbation charge classes form one finite demand set `D`. Collateral source classes `S` have current integral balances and one complete compatibility graph. Initial balances and every source-class deposit are named. Each successful epoch uses one integral joint flow and debits each source only once.

## Theorem block RI5dp--RI5dt

### RI5dp — current joint feasibility

At every epoch, all current owner and charge demands are paid exactly iff all capacitated Hall inequalities hold in the combined graph.

### RI5dq — exact shared debit

A successful integral flow updates each source balance by its actual used capacity. No source unit can pay both a symmetric owner cost and a perturbation charge.

### RI5dr — cumulative joint account

Across all successful epochs, cumulative source debit is bounded by initial shared balance plus named deposits.

### RI5ds — first unpaid mixed cut

The first failed epoch returns the canonical maximum-deficit subset of combined owner/charge classes and its exact collateral neighbourhood.

### RI5dt — reset boundary

Changed owner, charge or source dictionaries, changed compatibility, missing flow lineage or unrecorded deposits return reset.

## Proof

Apply integral max flow at each epoch to the current combined graph. Debit the actual source-side flow. Induction preserves every nonnegative balance and the cumulative identity. Max-flow/min-cut gives the failed mixed cut.

## Finite audit

Run `python scripts/verify_ri_cumulative_joint_owner_charge_bank.py`.

## Scope

The theorem does not construct the arithmetic combined graph, capacities or deposits. It does not prove RI6 or the no-three-in-line conjecture.

# Frontier pass 5: incremental alternating-core repair epochs

## AC5fp -- unchanged-pair persistence -- PROVED

If an incidence and token retain every compatibility-predicate input, physical identity, repair class, epoch signature and occurrence address, their compatibility truth value is unchanged at the next repair epoch.

## AC5fq -- boundary-only dictionary audit -- PROVED

For

`R' = R^circ disjoint_union Delta R`

and

`T' = T^circ disjoint_union Delta T`,

all potentially new compatibility values lie in

`B = (Delta R x T') disjoint_union (R^circ x Delta T)`.

Thus

`|B| = |Delta R||T'| + |R^circ||Delta T|`,

and an exact old dictionary plus an exact audit on `B` gives the exact new dictionary.

## AC5fr -- carried matching deficit -- PROVED

Restrict the old compatible assignment to unchanged incidences whose assigned tokens remain unchanged. If `a=|Delta R|` and `b` old retained incidences lose their assigned token, the carried matching leaves exactly `a+b` next-epoch incidences unmatched.

## AC5fs -- bounded reaugmentation or Hall core -- PROVED

If the new exact compatibility graph has a complete assignment, at most `a+b` augmenting paths are needed from the carried matching. Otherwise its matching deficit is at most `a+b`, and AC5ff--AC5fj return the canonical Hall core and missing-compatibility rectangle.

## AC5ft -- bounded-churn recurrent repair router -- PROVED UNDER THE EPOCH CONTRACT

Across a finite epoch sequence, exact dictionaries and assignments require at most the sum of boundary pair counts in new predicate evaluations and at most the sum of matching disturbances in augmenting paths. Every failure is a first boundary discrepancy, false unchanged declaration, stale or relabelled field, source-ledger failure, or canonical Hall core.

## Validation

`scripts/verify_ac_incremental_repair_epochs.py` checks finite exact dictionaries, bounded mutations, boundary reconstruction, carried matching deficits and complete-versus-deficient reassignments.

## Corrected frontier

The AC5 recurrence cost is now controlled by physical churn rather than total menu size. The remaining AC6 task is to bound concrete incidence/token churn, prove the geometric compatibility predicate on the audited boundary, and discharge the exact source or Hall witness when incremental reassignment fails.
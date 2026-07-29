# Frontier pass: free-token repair gains

- Proved AC5gp: every balanced selected track-key Hall component contains at least `m` free tokens, giving an `m^2` unmatched-root/free-token rectangle.
- Proved AC5gq: one retained track predicate labels at least `ceil(m|Z|/q_s)` such pairs.
- Proved AC5gr: endpoint-disjoint local repairs reduce synchronized matching deficit by the number of restored pairs; stars give one-step descent, common-witness batches give batch descent, and independent stocks give full descent.
- Proved AC5gs: `Delta_j <= Delta_{j-1}+U_j-g_j`, so cumulative successful repairs are funded by initial deficit plus declared physical churn.
- Added `scripts/verify_ac_free_token_repair_gains.py`.

Remaining: construct the actual seven-track repair operations, prove preservation and commutation, charge their costs, and combine the deficit ledger with pool replenishment and macro-state recurrence.
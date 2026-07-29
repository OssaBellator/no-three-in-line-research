# Frontier pass: free-token repair gains

- Proved RI5hm: the balanced rooted Hall component has at least `m` free same-key collateral tokens, and `U x Z` is a missing rectangle.
- Proved RI5hn: one retained predicate labels at least `ceil(m|Z|/q) >= ceil(m^2/q)` unmatched-root/free-token pairs.
- Proved RI5ho: restoring endpoint-disjoint pairs preserves a matching and reduces deficit by the number of repaired pairs.
- Proved RI5hp: stars give one-step descent, uniform witness overloads give batch descent, and independent stocks give full simultaneous descent; otherwise a rigid repair-contract failure is returned.
- Added `scripts/verify_ri_free_token_repair_gains.py`.

Remaining: construct the actual arithmetic repair operations, prove preservation and commutation, and charge their costs without creating collateral mass.
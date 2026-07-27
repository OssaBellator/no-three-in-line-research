# Alternating-core frontier ledger addendum

**Branch:** `research/alternating-core-chain`

This compact addendum records the AC5 Hall-cut reduction proved after the current canonical theorem-index compaction.

| ID | Statement | Status | Location |
|---|---|---|---|
| AC5ag | The optimal complete current/protected event-flow cost equals the sum of endpoint-cost sublevel matching deficiencies | PROVED | `docs/alternating-core-sublevel-hall-cuts.md` |
| AC5ah | If the low-event Hall-deficiency sum is less than `t|A|`, one stationary state is protected-safe and has at most `t-1` current events | PROVED | `docs/alternating-core-sublevel-hall-cuts.md` |
| AC5ai | The same Hall-deficiency criterion gives multistep protected safety without independence between steps | PROVED | `docs/alternating-core-sublevel-hall-cuts.md` |
| AC5aj | Failure of every safe flow returns one event-cost threshold and one explicit low-event Hall cut of deficiency at least `t|A|/C_t` | PROVED | `docs/alternating-core-sublevel-hall-cuts.md` |

## Updated AC5 frontier

Restricted-menu resampling now has three exact interfaces:

1. per-cylinder reverse-load bounds;
2. aggregate min-cost Hall flow;
3. endpoint-cost sublevel Hall deficiencies.

The remaining work is geometric: prove the required low-event neighbourhood expansion for each pivot, BDA, RI, target and petal menu, or route the returned threshold Hall cut to alternate switches, payment or tickets.

No statement here proves AC6 or the global conjecture.

# Frontier pass: AC3 physical signature recurrence

## Active branch

`agent/ac-ac3-signature-recurrence`

Parent: `agent/ac-ac2-structural-reextraction` at `edf88a96767039815c69e515f293f26d1ccf3974`.

Only AC is active. Historical side branches remain immutable source libraries.

## New theorem block

- **AC5lr:** finite occurrence-faithful signature normal form.
- **AC5ls:** monotone exposure ledger and exact first-use route.
- **AC5lt:** occurrence-faithful reuse tickets and paid/delegated reuse.
- **AC5lu:** canonical unticketed strongly connected cycle extraction.
- **AC5lv:** strict labelled-support descent and reopening contract.
- **AC5lw:** complete AC3 no-recycling compiler.

## Logical gain

Product carries, cross carries, coordinate carries, wrap centres, determinant-realized BDA profiles and physical RI profiles now share one tagged signature registry. First exposure is permanent progress. Reuse is accepted only with a physical reuse ticket, current payment, or an exact BDA/RI delegation.

The residual old-signature/no-ticket graph is audited directly. An acyclic graph receives a strict topological rank; a cyclic graph returns its least strongly connected component and a directed cycle. A cycle cannot be repaired merely by changing scalar coefficients on the same unchanged signature data.

Labelled AC2 recursion strictly shrinks its object universe. Reintroducing a discarded object requires a reopening ticket or another paid/delegated/reset route.

## Deterministic audit

Equivalent execution of `scripts/verify_ac_ac3_signature_recurrence.py` checks 2,500 systems:

- physical signature records: `12,549`;
- first exposures: `9,132`;
- ticketed reuses: `4,602`;
- paid or BDA/RI delegated reuses: `4,304`;
- canonical unticketed cycles: `500`;
- directed edges retained in returned cycles: `917`;
- strict support descents: `3,737`;
- unticketed reopening failures: `202`;
- malformed signature records: `500`;
- duplicate ticket-alias witnesses: `500`.

All assertions pass.

## Remaining AC frontier

1. Populate the actual signature registry reached from the AN/AC2 path.
2. Construct every physical reuse/reopening ticket.
3. Classify each unticketed cycle by payment, descent, impossibility or a new finite ticket.
4. Append accepted transitions to the ordinal edge table.
5. Continue fair reachable expansion and the initial-state manifest.

AC6 and the global no-three-in-line conjecture remain open.

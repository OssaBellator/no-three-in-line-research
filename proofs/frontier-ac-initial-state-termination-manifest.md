# Frontier pass: AC initial-state termination manifest

## Active branch

`agent/ac-initial-state-termination-manifest`

Parent: `agent/ac-reachable-cofinality` at `c7c8c72042496c8b6ee976a32c28ac54ae0c66a6`.

Only AC is active. Historical AC, RI, BDA, GC, OP, SRR, SAS and all-n branches remain immutable source libraries.

## New theorem block

- **AC5kh:** exact seven-section dependency order and coherent manifest digest.
- **AC5ki:** monotone manifest refinement preserving every earlier accepted record.
- **AC5kj:** complete initial-state termination certificate.
- **AC5kk:** finite minimal first-failure witness.
- **AC5kl:** proof-object stability under cap enlargement.
- **AC5km:** final current AC6 reduction to physical manifest population.

## Logical gain

The current AC chain is consolidated into one versioned physical proof object with sections for:

1. schema;
2. deterministic serialization;
3. frontier completion;
4. fair reachable expansion;
5. rank extension;
6. edge stratification;
7. exceptional source/claim flow.

A complete manifest composes AC5kd, AC5jj, AC5jp, AC5jz and AC5jh to prove that no infinite nonterminal trajectory starts at the chosen initial state. An incomplete manifest returns the first finite physical witness from the first failed section.

Supplying that missing record preserves every earlier accepted digest. Cap enlargement appends an ordered shell delta rather than rebuilding old proof objects.

## Deterministic audit

Equivalent execution of `scripts/verify_ac_initial_state_termination_manifest.py` checks 3,200 manifests:

- complete valid manifests: `400`;
- coherent proof digests: `400`;
- terminating ordinal trajectory steps: `6,340`;
- exceptional interruptions used: `538`;
- exact schema failures: `400`;
- exact serializer failures: `400`;
- exact frontier failures: `400`;
- exact fairness failures: `400`;
- exact rank failures: `400`;
- exact stratification failures: `400`;
- exact exception-ledger failures: `400`;
- monotone refinements preserving earlier sections: `2,800`.

All assertions pass.

## Remaining AC frontier

1. Choose and serialize the actual AC initial-state class.
2. Populate the seven physical manifest sections from the historical AC records.
3. Run the manifest compiler.
4. Discharge its first returned finite witness.
5. Repeat until every initial state required by AC6 has a complete manifest.

AC6 and the global no-three-in-line conjecture remain open.

# Frontier pass: BDA schema adequacy

- Branch: `agent/bda-schema-adequacy-compiler`
- Theorems: BDA5ip--BDA5is
- Logical blocks: `6`
- Audit coordinates: `4`
- Audit alphabet: `180`
- Binary logical states: `64`
- Binary result: capacity-feasible, encoder unproved

The pass proves exact schema extraction, a lossless-encoder and compatibility-factorization criterion, a capacity/omission/collision router, and fail-closed import of synthetic audit constants.

Verifier: 2,500 systems; 2,400 capacity obstructions; 100 feasible cases; 2,500 omission witnesses; 100 sample packings; 1,838,228 logical states counted.

Remaining frontier: construct the physical encoder and compatibility factorization before deriving BDA footprint, rank, reset, reserve or payment constants.

# Frontier pass: GC schema adequacy

- Branch: `agent/gc-schema-adequacy-compiler`
- Theorems: GC2nn--GC2nq
- Logical blocks: `7`
- Audit coordinates: `4`
- Audit alphabet: `180`
- Binary logical states: `128`
- Binary result: capacity-feasible, encoder unproved

The pass proves exact schema extraction, encoder/factorization adequacy, capacity and omission routing, and fail-closed import of synthetic audit constants.

Verifier: 2,500 systems; 2,500 generated capacity obstructions; 2,500 omission witnesses; 5,495,023 logical states counted.

Remaining frontier: implement the physical geometric encoder and compatibility factorization before deriving donor, height, footprint, rank, reset or payment constants.

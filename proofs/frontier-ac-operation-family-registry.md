# Frontier pass: AC operation-family registry

## Active branch

`agent/ac-operation-family-registry`

Parent: `agent/ac-physical-schema-registry` at `1c441889d0d64def3d2e707c8ff9ff119d0c0a05`.

Only AC is active. Historical AC, RI, BDA, GC, OP, SRR, SAS and all-n branches remain immutable source libraries.

## New theorem block

- **AC5kt:** complete historical operation-family partition.
- **AC5ku:** deterministic operation address and exact omitted-choice witness.
- **AC5kv:** typed occurrence identity, cross-kind nonaliasing and one-use accounting.
- **AC5kw:** complete precondition/effect and physical-footprint contract.
- **AC5kx:** cap-invariant untruncated successor exposure.
- **AC5ky:** accepted operation registry as complete bounded-serializer input.

## Logical gain

The live operation dictionary is no longer an untyped list of state edits. Every event belongs to one of ten physical families:

1. target installation;
2. occurrence-slot repair;
3. physical source/certificate flow;
4. transition-relative payment debit;
5. resource macro;
6. recreation/restoration;
7. periodic-tail step;
8. exogenous disturbance;
9. funded reset;
10. terminal commit.

Every address retains its exact precondition, footprint, lineage, effect vector and untruncated successor. A similar effect does not identify two operation kinds. A payment and a disturbance remain distinct even when they change the same numeric coordinate.

Under cap-only refinement, the operation address and untruncated successor remain identical. Only the boundary-versus-interior classification may change.

## Deterministic audit

Equivalent execution of `scripts/verify_ac_operation_family_registry.py` checks 2,500 registries:

- valid complete registries: `1,000`;
- complete operation records: `10,000`;
- deterministic repeated outcomes: `10,000`;
- internal outcomes in the minimal current box: `6,655`;
- upper-bound outcomes refining after enlargement: `3,345`;
- cap-invariance successor checks: `10,000`;
- cross-kind address-alias witnesses: `1,000`;
- first omitted kind-specific field witnesses: `1,500`.

All assertions pass.

## Remaining AC frontier

1. Instantiate the ten operation families with the actual historical physical records.
2. Enumerate every operation enabled at the chosen initial state.
3. Compute the reachable successor and boundary tables.
4. Populate the six historical recognizer row families on those objects.
5. Run fair reachable expansion, rank extension, edge stratification and the global exceptional flow.

AC6 and the global no-three-in-line conjecture remain open.

# Sparse algebraic schema-adequacy compiler

## Status

This note proves SAS5om--SAS5op from the field list in `docs/sparse-typed-repair-neutral-compatibility-dictionary.md` and the alphabet in `scripts/verify_sas_typed_repair_neutral_compatibility_dictionary.py`. It corrects the old tuple-audit scope and does not prove SAS6.

## Inventory

The logical address has seven blocks: `repair_type`, `sign`, `boundary_profile`, `neutral_move`, `legality_class`, `physical_source`, and `epoch`. The old audit uses radices `(2,4,3,5)`, giving 120 synthetic addresses.

## SAS5om -- exact schema extraction -- PROVED

All seven blocks and four radices are imported exactly. Missing sign, profile, move, legality, source, type, or epoch information returns the least schema discrepancy.

## SAS5on -- lossless encoder and compatibility factorization -- PROVED

Physical use requires an injective encoder into the 120-state alphabet and a proof that boundary-neutral compatibility factors through encoded pairs. Same-code/different-address, same-code/different-compatibility, and omitted-field pairs are exact witnesses.

## SAS5oo -- binary capacity obstruction -- PROVED

For domain sizes `d_i`, injectivity requires

\[
\boxed{\prod_i d_i\le120}.
\]

Seven independently binary blocks give 128 states, so the old alphabet cannot losslessly encode even the minimal independent schema.

## SAS5op -- fail-closed import -- PROVED

Until SAS5on is discharged with an adequate replacement encoding or proved field dependencies, the old verifier proves only its synthetic tuple model. No physical legality predicate, sparse footprint, orientation multiplicity, lineage rank, reset, reserve, or payment constant may be imported.

## Finite check

`scripts/verify_sas_schema_adequacy_compiler.py` checks 2,500 schemas. All 2,500 exceed the 120-state capacity and all 2,500 omitted-field projections give exact collisions.

## Corrected SAS6 frontier

Construct a lossless sign/profile/move/legality/source/epoch encoder or prove concrete dependencies reducing the state count, then verify physical compatibility.

# Orbit-phase schema-adequacy compiler

## Status

This note proves OP4hm--OP4hp from the field list in `docs/orbit-phase-typed-repair-source-compatibility-dictionary.md` and the alphabet in `scripts/verify_op_typed_repair_source_compatibility_dictionary.py`. It corrects the four-coordinate audit scope and does not prove OP5.

## Inventory

The logical address has seven blocks: `repair_type`, `physical_source`, `unit_class`, `valuation_vector`, `holonomy`, `action_kernel`, and `epoch`. The old audit uses radices `(2,4,3,5)`, giving exactly 120 synthetic addresses.

## OP4hm -- exact schema extraction -- PROVED

All seven named blocks and all four radices are versioned inputs. Missing unit, valuation, holonomy, kernel, source, type, or epoch data returns the least schema discrepancy.

## OP4hn -- lossless encoder and compatibility factorization -- PROVED

Physical use requires an injective encoder into the 120-state alphabet and a proof that unit-sensitive `Compat` factors through encoded pairs. Same-code/different-address and same-code/different-compatibility pairs are exact witnesses; omitting any block gives a canonical collision.

## OP4ho -- binary capacity obstruction -- PROVED

For field-domain sizes `d_i`, injectivity requires

\[
\boxed{\prod_i d_i\le120}.
\]

Seven independently binary blocks already give 128 states. Therefore the old alphabet cannot losslessly encode even that minimal independent schema.

## OP4hp -- fail-closed import -- PROVED

Until OP4hn is discharged with a different adequate encoding or a proved dependence among logical fields, the old verifier proves only its synthetic tuple-equality model. No physical predicate, quotient footprint, unit/valuation multiplicity, holonomy rank, reset, reserve, or payment constant may be imported.

## Finite check

`scripts/verify_op_schema_adequacy_compiler.py` checks 2,500 schemas. All 2,500 exceed the 120-state capacity and all 2,500 omitted-field projections give exact collisions.

## Corrected OP5 frontier

Construct a lossless unit-sensitive address encoder or prove concrete field dependencies reducing the logical state count, then prove compatibility factorization.

# Geometric-cleaning schema-adequacy compiler

## Status

This note proves GC2nn--GC2nq from the field list in `docs/geometric-cleaning-repair-source-compatibility-dictionary.md` and the alphabet in `scripts/verify_gc_repair_source_compatibility_dictionary.py`. It does not construct physical compatibility or prove GC5.

## Inventory

The logical address has seven blocks: `physical_source`, `donor`, `remedy`, `height`, `cause`, `local_geometry`, and `epoch`. The existing audit generates anonymous tuples with radices `(3,4,3,5)`, so its synthetic alphabet has size 180.

## GC2nn -- exact schema extraction -- PROVED

The compiler imports those seven blocks and four radices exactly. Any changed or omitted geometry, epoch, field name, or radix returns a schema-version witness.

## GC2no -- lossless encoder and compatibility factorization -- PROVED

Physical use of the tuple audit requires an injective encoder from complete logical addresses to the 180-state alphabet and a proof that geometric `Compat` factors through encoded incidence-token pairs. The least same-code/different-address or same-code/different-compatibility pair is returned. Omitting one block gives a canonical pair differing only in that block.

## GC2np -- capacity test -- PROVED

For logical domain sizes `d_i`, injectivity requires

\[
\boxed{\prod_i d_i\le180}.
\]

Independent binary variation gives 128 states, so counting alone does not obstruct an encoder. It does not construct one. Every larger product returns an exact capacity obstruction.

## GC2nq -- fail-closed import -- PROVED

Until GC2no is discharged, the old verifier proves only a synthetic four-tuple equality model. Its audit constants remain valid, but no physical predicate, footprint, donor multiplicity, height rank, reset, reserve, or payment constant may be imported.

## Finite check

`scripts/verify_gc_schema_adequacy_compiler.py` checks 2,500 schemas: all 2,500 generated products exceeded 180, and all 2,500 omitted-field projections produced exact collisions.

## Corrected GC5 frontier

Construct the source/donor/remedy/height/cause/geometry/epoch encoder and geometric compatibility evaluator before compiling physical constants.

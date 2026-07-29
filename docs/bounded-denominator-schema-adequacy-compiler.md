# Bounded-denominator schema-adequacy compiler

## Status

This note proves BDA5ip--BDA5is from the field list in `docs/bounded-denominator-repair-potential-compatibility-dictionary.md` and the alphabet in `scripts/verify_bda_repair_potential_compatibility_dictionary.py`. It corrects the scope of the four-coordinate audit. It does not construct physical compatibility or prove BDA6.

## Concrete inventory

The logical address has six blocks: `physical_source`, `numerator_weight`, `rational_gain`, `damping_factor`, `restoration_class`, and `epoch`. The existing audit instead generates anonymous tuples with radices `(3,4,3,5)`, hence

\[
N_{\rm audit}=3\cdot4\cdot3\cdot5=\boxed{180}.
\]

## BDA5ip -- exact schema extraction -- PROVED

The compiler imports the six named blocks and four radices exactly. Changed fields, radices, epochs, or address names return a schema-version witness; anonymous coordinates are not silently identified with physical fields.

## BDA5iq -- encoder and factorization criterion -- PROVED

Using the tuple audit physically requires an injective encoder `enc:L->A` from logical addresses to the audit alphabet and a proof that `Compat(r,s)` factors through `enc(r),enc(s)`. The least same-code/different-address or same-code/different-compatibility pair is an exact collision witness. Omitting one field returns two records differing only in that field.

## BDA5ir -- finite capacity test -- PROVED

For logical domain sizes `d_i`, injectivity requires

\[
\boxed{\prod_i d_i\le180}.
\]

Independent binary variation gives 64 states, so counting alone does not obstruct an encoder. It also does not construct one. Any larger declared product exceeding 180 returns an exact capacity obstruction.

## BDA5is -- fail-closed import -- PROVED

Until BDA5iq is discharged, the old verifier proves only its synthetic tuple-equality model. Audit arity, radices, alphabet size and generated pair counts remain valid; physical predicate, footprint, multiplicity, rank, reset, reserve and payment constants may not be imported.

The router returns an adequate encoder/factorization certificate, a field omission, a capacity obstruction, a compatibility collision, a stale schema, or the explicit synthetic-model-only result.

## Finite check

`scripts/verify_bda_schema_adequacy_compiler.py` checks 2,500 schemas: 2,400 capacity obstructions, 100 capacity-feasible cases still requiring an encoder, 2,500 omission witnesses, and 100 feasible sample packings.

## Corrected BDA6 frontier

Implement the actual source/numerator/gain/damping/restoration/epoch encoder and compatibility evaluator before compiling physical constants.

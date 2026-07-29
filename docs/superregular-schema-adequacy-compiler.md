# Superregular schema-adequacy compiler

## Status

This note proves SRR2gw--SRR2gz from the field list in `docs/superregular-repair-witness-compatibility-dictionary.md` and the alphabet in `scripts/verify_srr_repair_witness_compatibility_dictionary.py`. It does not construct conditioned compatibility or prove SRR4.

## Inventory

The logical address has six blocks: `candidate`, `witness_atom`, `conditioned_threshold`, `physical_source`, `tensor_cylinder`, and `epoch`. The old audit uses radices `(3,4,3,5)`, hence 180 synthetic addresses.

## SRR2gw -- exact schema extraction -- PROVED

The six blocks and four radices are imported exactly. Missing witness, threshold, conditioning, cylinder, source, or epoch information returns a schema witness.

## SRR2gx -- encoder and factorization criterion -- PROVED

Physical use requires an injective encoder into the audit alphabet and a proof that conditioned compatibility factors through encoded pairs. The least address collision, compatibility collision, or omitted-field pair is returned.

## SRR2gy -- capacity test -- PROVED

For field-domain sizes `d_i`, injectivity requires

\[
\boxed{\prod_i d_i\le180}.
\]

Six independent binary fields give 64 states, so the minimal count test passes but supplies no encoder.

## SRR2gz -- fail-closed import -- PROVED

Until SRR2gx is discharged, the old verifier validates only its synthetic tuple model. No physical predicate, candidate/witness footprint, threshold multiplicity, burden rank, reset, reserve, or payment constant may be imported.

## Finite check

`scripts/verify_srr_schema_adequacy_compiler.py` checks 2,500 schemas: 2,403 capacity obstructions, 97 capacity-feasible cases still requiring an encoder, 2,500 omission witnesses, and 97 feasible sample packings.

## Corrected SRR frontier

Construct the candidate/witness/threshold/source/cylinder/epoch encoder and conditioned compatibility factorization before compiling physical constants.

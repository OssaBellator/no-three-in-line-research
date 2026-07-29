# Rational-inverse schema-adequacy compiler

## Status

This note proves RI5ig--RI5ij from the concrete logical field list in `docs/rational-inverse-typed-repair-collateral-compatibility-dictionary.md` and the executable alphabet in `scripts/verify_ri_typed_repair_collateral_compatibility_dictionary.py`. It corrects the scope of the four-coordinate deterministic audit. It does not construct the physical compatibility predicate, repair maps, ranks, reset sources, or prove RI6 or the no-three-in-line conjecture.

## Concrete inventory

The retained logical address has exactly `7` named blocks:

- `repair_type`
- `field_element_data`
- `host_context`
- `secant_line_address`
- `coherence`
- `collateral_class`
- `epoch`

The existing deterministic audit does not instantiate those blocks. It generates anonymous four-tuples with coordinate radices

\[
(2,4,3,5)
\]

and therefore an exact synthetic address alphabet of size

\[
N_{\rm audit}=2\cdot4\cdot3\cdot5=\boxed{120}.
\]

## RI5ig -- exact declared-schema extraction -- PROVED

The compiler imports the seven logical block names above and the four audit radices directly from the committed dictionary note and verifier. A changed block, changed radix, missing epoch, or renamed address component is returned as a schema-version discrepancy. No anonymous tuple coordinate is silently identified with a physical block.

## RI5ih -- lossless encoder and compatibility-factorization criterion -- PROVED

Let `L` be the set of logical addresses and let `A` be the four-coordinate audit alphabet. To use the old tuple audit as evidence for the physical dictionary one must provide an encoder

\[
\operatorname{enc}:L\to A
\]

satisfying both:

1. every declared logical block is recoverable from `enc`, equivalently `enc` is injective on retained addresses;
2. physical compatibility is constant on encoded incidence-token pairs, so `Compat(r,s)` is determined by `enc(r),enc(s)`.

If either condition fails, the least pair of logical records with the same encoding but different retained address or different compatibility value is an exact schema-collision witness. A field-omission witness is the special case of two records differing only in the omitted block.

A lossless reference compiler may bundle several logical blocks into one composite coordinate; this proves the compiler theorem but does not identify the old small integer alphabets with those composite values.

## RI5ii -- finite alphabet capacity obstruction -- PROVED

If logical block `i` has domain size `d_i`, injectivity requires

\[
\boxed{\prod_i d_i\le120}.
\]

Under the minimal test that every declared block independently admits two values, the logical address set has 128 states. Because `128>120`, even the minimal binary-independence test already forbids a lossless encoding into the old audit alphabet.

More generally, whenever `prod_i d_i>120`, the compiler returns the cardinality excess and the least declared block prefix at which the mixed-radix logical count first exceeds the audit capacity. Passing the count test is only necessary; an explicit encoder/decoder and factorization proof are still required.

## RI5ij -- fail-closed constant import -- PROVED

Until RI5ih is discharged, the old verifier proves exactness only for its synthetic four-tuple equality model. Its tuple arity, alphabet size, and generated pair counts may be quoted as audit-model constants, but no physical predicate count, footprint bound, multiplicity bound, rank allowance, or payment constant may be imported from it.

The continuation router returns exactly one of:

1. an adequate encoder/decoder and compatibility factorization;
2. a field-omission collision;
3. an audit-alphabet capacity obstruction;
4. a same-code/different-compatibility collision;
5. a stale schema version or changed radix;
6. the explicit statement that only the synthetic tuple model has been verified.

## Finite check

`scripts/verify_ri_schema_adequacy_compiler.py` performs 2,500 generated finite-schema tests. It found 2,500 capacity obstructions, zero capacity-feasible cases, and 2,500 exact omitted-field collision witnesses.

## Corrected RI6 frontier

The immediate concrete task is no longer to choose another symbolic `q`. It is to implement the actual encoder and compatibility predicate for owner/charge, arithmetic, host/context, secant/line, coherence, collateral and epoch, or return a concrete collision/omission/capacity witness. Only after that may the physical footprint, fanout, rank, reset and payment constants be compiled.

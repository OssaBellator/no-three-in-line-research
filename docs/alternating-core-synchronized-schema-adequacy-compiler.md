# Alternating-core synchronized schema-adequacy compiler

## Status

This note proves AC5hj--AC5hm by compiling the seven concrete compatibility-dictionary notes and their committed audit alphabets. It corrects the scope of the anonymous four-coordinate models. It does not construct the seven physical compatibility predicates or prove AC6 or the no-three-in-line conjecture.

## Seven-track inventory

| Track | logical blocks | audit radices | audit alphabet | binary states | minimal result |
|---|---:|---|---:|---:|---|
| AC | 5 | `(3,4,3,5)` | 180 | 32 | encoder required |
| RI | 7 | `(2,4,3,5)` | 120 | 128 | obstruction |
| BDA | 6 | `(3,4,3,5)` | 180 | 64 | encoder required |
| GC | 7 | `(3,4,3,5)` | 180 | 128 | encoder required |
| OP | 7 | `(2,4,3,5)` | 120 | 128 | obstruction |
| SRR | 6 | `(3,4,3,5)` | 180 | 64 | encoder required |
| SAS | 7 | `(2,4,3,5)` | 120 | 128 | obstruction |

The synchronized inventory contains 45 declared logical blocks and 28 anonymous audit coordinates. Coordinate count alone is not an obstruction because one coordinate may encode a compound value; adequacy requires an explicit lossless encoder and compatibility factorization on every track.

## AC5hj -- exact synchronized schema inventory -- PROVED

The compiler imports the named blocks and exact audit radices for AC, RI, BDA, GC, OP, SRR, and SAS. Each track keeps its own encoder, decoder, epoch, compatibility predicate, and failure order. A changed field list, changed radix, missing epoch, or track migration is returned as the least schema-version discrepancy.

## AC5hk -- trackwise lossless compilation criterion -- PROVED

For track `s`, let `L_s` be its logical address set and `A_s` its four-coordinate audit alphabet. Physical import requires an encoder

\[
\operatorname{enc}_s:L_s\to A_s
\]

such that every retained field is recoverable, physical compatibility factors through encoded incidence-token pairs, track and epoch are preserved, and shared physical fields receive consistent values across tracks.

The least injectivity collision, same-code/different-compatibility pair, shared-field inconsistency, or omitted field is an exact synchronized schema witness.

## AC5hl -- finite capacity and omission router -- PROVED

For logical domain sizes `d_{s,i}`, injectivity requires

\[
\boxed{\prod_i d_{s,i}\le|A_s|}.
\]

Under minimal independent binary variation, RI, OP, and SAS require 128 states but have only 120 audit states. AC, BDA, GC, and SRR pass only this necessary count test and still require explicit encoders and factorization proofs.

For every declared field, omission gives a canonical pair differing only in that field and colliding under the omitted-field projection. The router returns the least track, field, and pair.

## AC5hm -- fail-closed synchronized constant import -- PROVED

Until every track discharges AC5hk, the old audits validate only seven synthetic tuple-equality models. The exact field lists, tuple radices, alphabet sizes, and old generated pair counts may be imported. Physical predicate counts, repair footprints, fanout, multiplicities, ranks, resets, payment capacities, reserves, and recurrence constants may not.

The synchronized continuation is a complete encoder/factorization certificate for all tracks or the least capacity, omission, collision, compatibility, shared-field, or schema-version witness.

## Finite check

`scripts/verify_ac_synchronized_schema_adequacy_compiler.py` checks 1,500 seven-track macro systems, comprising 10,500 finite schema instances. It verifies 10,500 omitted-field witnesses, 9,809 generated capacity obstructions, 691 capacity-feasible sample packings, and the three minimal binary obstruction tracks RI, OP, and SAS.

## Corrected AC6 frontier

The next numerical AC constants must be generated from concrete field encoders and physical compatibility evaluators, not from anonymous tuple audits. Once every track supplies that certificate, the compiler can safely derive predicate dictionaries, footprint dependencies, multiplicities, ranks, resets, and paid-touch capacities.

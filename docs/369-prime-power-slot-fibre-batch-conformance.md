# Noncircular slot-to-fibre batch conformance

CMR2118--CMR2125 separate source-independent operation slots from source-dependent
`fibre_id`s. CMR2086--CMR2093 validate complete populated operation records. This
chapter composes the two surfaces and makes slot coverage the only accepted completeness
criterion.

## Theorem CMR2126 -- PROVED

A slot-covered batch certificate contains:

1. one independently validated operation-slot registry;
2. one canonical populated fibre batch;
3. one exact assignment of every supplied fibre to one slot.

Each assignment stores

\[
(\text{slot ID},\text{fibre ID},\text{host ID},\text{source digest})
\]

and is protected by its own digest.

## Theorem CMR2127 -- PROVED

For every assignment, the checker recomputes the fibre record and requires exact equality
of:

- populated and expected host IDs;
- populated and assigned source digests;
- populated and assigned fibre IDs; and
- the linkage certificate's ordered seven-label tuple and the slot's ordered label tuple.

Thus a record cannot borrow a slot from another host, source or labelled state.

## Theorem CMR2128 -- PROVED

The underlying populated batch must leave its source-dependent `expected_fibre_ids` field
unset. A slot-covered certificate is rejected if that older field declares completeness.

This prevents two competing notions of completeness. Source-dependent fibre IDs remain
exact populated-record identities, but operation slots define the expected universe.

## Theorem CMR2129 -- PROVED

Every populated fibre must be assigned exactly once, and every assignment must name a
fibre present in the batch. Duplicate slot assignments, duplicate fibre assignments,
unassigned batch fibres and assignments to absent fibres are rejected.

## Theorem CMR2130 -- PROVED

The assignment list is converted mechanically into the CMR2121 population audit. The
missing, unexpected, duplicate and host-mismatch lists are therefore inherited from the
independently validated slot registry rather than trusted from the batch.

## Theorem CMR2131 -- PROVED

A slot-covered batch is complete exactly when

\[
\boxed{
\text{all expected slots are covered once, every batch fibre is assigned once, and all
host/source/label equalities hold}.
}
\]

Equivalently, the exact population audit has empty missing, unexpected, duplicate and
host-mismatch lists.

## Theorem CMR2132 -- PROVED

The certificate reconstructs the complete aggregate census of the covered batch,
including response records, primitive witnesses, strict scalar improvements, parent
policy matches and penalties, Pareto vectors and dominated responses. These totals are
bound to both the batch-record digest and the slot-assignment digest.

## Corollary CMR2133 -- PROVED

`scripts/check_prime_power_slot_fibre_batch_conformance.py` validates arbitrary
slot-covered batches. Its deterministic composition regression contains a 60-slot
complete batch and a 50-operation partial batch with exactly ten missing slots, and its
mutation suite rejects twelve independent corruptions.

The checker proves conformance to a supplied expected registry. It does not prove that
the genuine parent-rule enumerator producing that registry is exhaustive, nor does it
prove state-label semantics.

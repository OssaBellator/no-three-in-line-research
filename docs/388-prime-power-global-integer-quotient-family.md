# Exhaustive global denominator-cleared quotient family

The preceding chapters produce globally identified states, synchronized recurrent blocks
and exact return/interface rows. This chapter assembles them into one canonical integer
matrix/vector/rank package relative to an explicit expected family manifest.

## Theorem CMR2278 — PROVED AS AN INTERFACE

A family manifest fixes:

1. one family ID;
2. the complete expected integer-block ID list;
3. the complete expected interface-row ID list;
4. the complete expected global parent-state list; and
5. one evidence string.

Every list is canonical, duplicate-free and protected by the family digest.

## Theorem CMR2279 — PROVED

The actual block IDs from the state-identification certificate must equal the expected block
list exactly. The actual return/interface row IDs must equal the expected interface list
exactly.

Missing and unexpected blocks or interface rows are rejected.

## Theorem CMR2280 — PROVED

Every synchronized recurrent row is lifted by its component multiplier into the final global
weight scale. The exact strict identity remains

\[
\widehat W_p-\widehat b_p-\sum_t a_{p,t}\widehat W_t
=\widehat\mu_p>0.
\]

All selected slot, fibre and response identities are retained.

## Theorem CMR2281 — PROVED

Recurrent and interface rows are merged into one global row family. Every global parent must
occur exactly once, and the resulting parent set must equal the expected parent registry.

Auxiliary parents and surviving auxiliary target columns are forbidden.

## Theorem CMR2282 — PROVED

The quotient publishes one canonical package

\[
\boxed{(A,b,W,\mu,\rho)}
\]

whose rows are ordered by global parent and whose columns are all nonauxiliary global states.
Recurrent rows have positive margin. Interface rows have positive margin or zero margin with
strict rank descent.

## Theorem CMR2283 — PROVED

The `complete_global_integer_family` flag is set only when all of the following hold:

- complete local-to-global state coverage;
- exact cross-block scale consistency;
- accepted global interface rows;
- every integer recurrent block is complete;
- exact expected block coverage;
- exact expected interface-row coverage;
- exact expected parent coverage; and
- every row is strict or critical-descending.

## Theorem CMR2284 — HONEST GLOBAL COMPLETENESS BOUNDARY

A complete global integer family is complete only relative to the supplied family manifest,
state identifications, component scales, ranks and populated rows.

It is not a proof that the manifest is the genuine exhaustive recurrence, that every state
or transition has the intended semantics, or that the resulting quotient proves the
all-`n` conjecture.

## Corollary CMR2285 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_global_integer_quotient_family.py` validates the expected family,
lifts every recurrent block, appends every interface row, enforces exact parent coverage and
publishes the global denominator-cleared integer matrix/vector/rank package.

The checker was syntax-compiled in the publication environment. No genuine complete global
family is claimed.

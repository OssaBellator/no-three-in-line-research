# Denominator-cleared integer recurrent quotient block

The preceding interfaces separately certify candidate operation choice, literal resource
scopes, common recurrent weights and complete auxiliary elimination. This chapter composes
them into one exact integer matrix/vector block.

## Theorem CMR2246 — PROVED AS AN INTERFACE

One quotient certificate composes:

1. a common-weight candidate-policy certificate;
2. a resource-overlap-derived simultaneous-scope certificate; and
3. an acyclic auxiliary-elimination certificate.

All three must contain the same common recurrent block and exactly the same routed row
family.

## Theorem CMR2247 — PROVED

The response selected after full auxiliary elimination must equal the response whose
witness-bound routes were audited by the simultaneous nonreuse certificate. If elimination
changes the selected response, quotient assembly is rejected until new literal routes are
supplied.

## Theorem CMR2248 — PROVED

For every recurrent parent `p`, full elimination produces one signed integer fixed offset
`b_p`, one nonnegative integer target vector `a_{p,t}` over nonauxiliary states and one
positive parent weight `w_p` satisfying

\[
\boxed{w_p-b_p-\sum_t a_{p,t}w_t=\mu_p.}
\]

The identity is checked exactly against the transformed row load.

## Theorem CMR2249 — PROVED

The quotient publishes a canonical integer package

\[
(A,b,w,\mu),
\]

where rows are ordered by recurrent parent state and columns by nonauxiliary state. Matrix
entries are nonnegative integers; fixed offsets may be signed because retained destroyed
credit is already incorporated into the net offset.

## Theorem CMR2250 — PROVED

Every quotient row must be strict:

\[
\boxed{\mu_p>0.}
\]

The certificate publishes minimum and total margins, nonzero matrix entries and all row
and block digests.

## Theorem CMR2251 — PROVED

A block receives the `complete_integer_recurrent_block` flag only when all of the following
hold simultaneously:

- exact common-weight candidate policy;
- exact overlap-derived resource scopes;
- complete strict source SCC;
- strictness preserved by full auxiliary elimination;
- selected-response stability; and
- positive integer margin on every quotient row.

## Theorem CMR2252 — HONEST GLOBAL BOUNDARY

A complete integer recurrent block is not the final global CRT quotient. The proof must
still cover every recurrent and interface block, verify cross-block state identification,
assemble all off-diagonal and return terms, and prove that the complete block family is the
genuine exhaustive recurrence.

## Corollary CMR2253 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_integer_recurrent_quotient_block.py` composes policy, scopes,
common weights and acyclic elimination; verifies response stability; and publishes the
exact denominator-cleared integer matrix/vector block.

The checker was syntax-compiled in the publication environment. No genuine complete block
or global quotient is claimed.

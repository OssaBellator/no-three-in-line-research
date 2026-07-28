# Prime-power auxiliary-semantics frontier

This chapter records CMR2542--CMR2549. It makes

```text
T12_AUXILIARY_SEMANTICS
AUXILIARY_EXPANSIONS_SEMANTIC
```

an exact documentary proof surface over the already fixed T07 semantic and T11 recurrent-block banks.

The canonical executable endpoint is:

```text
scripts/check_prime_power_auxiliary_semantics_frontier_v2.py
```

The version-1 checker remains as the published base schema. The version-2 adapter preserves its
per-block record, expansion, arithmetic and artifact formats while correcting the shared dependency
root and aggregate obligation support.

## CMR2542: parallel auxiliary-population defect

The older one-step and acyclic elimination checkers accept a common-weight certificate and an
auxiliary expansion table as direct inputs. They correctly verify finite weighted substitution,
recursive coverage, acyclicity, zero auxiliary credit and responsewise load monotonicity.

By themselves, however, they do not prove that:

1. the common rows are the exact selected T11 rows;
2. the expansion sources and targets are the exact states occurring in those rows;
3. the expansion edges are supported by the exact T07 semantic claim bank; or
4. elimination preserves the response selected by the current recurrence policy.

Using either older checker directly for T12 would therefore permit a second auxiliary and
common-weight population parallel to the T07/T11 frontier.

## CMR2543: corrected T12 dependency root

The exact proof flow is:

```text
T07_FATE_TRANSITION_STATE + T11_RECURRENT_BLOCK_CLOSURE
    -> T12_AUXILIARY_SEMANTICS
```

The semantic obligation has the corresponding immediate dependencies:

```text
FATE_TRANSITION_STATE_SEMANTICS
CLOSED_STRICT_RECURRENT_BLOCKS
    -> AUXILIARY_EXPANSIONS_SEMANTIC
```

The fixed atomic execution checker and the fixed obligation-closure checker now publish this same
order. T12 cannot close or become research-actionable before the exact T11 recurrent-block population
exists.

## CMR2544: exact T11-derived block bank

Every T11 recurrent-block record receives exactly one open/proved T12 record. The canonical record
binds:

```text
block_id
t11_block_closure_record_sha256
t11_common_weight_record_sha256
status
verification_locator
verification_digest
note
```

A proved record uses:

```text
auxiliary-semantics-registry://<block ID>
```

and requires the corresponding T11 block and common-weight records to be proved. Missing, extra,
duplicated or reordered T12 block records are rejected against the exact T11 block census.

## CMR2545: exact recursive expansion and weighted substitution

For each proved block, the embedded acyclic elimination certificate must use the exact T11
`common_weight_certificate`; a parallel certificate is rejected even if it satisfies the same finite
inequalities.

The expansion table must cover exactly the recursive closure of every auxiliary state occurring with
positive coefficient in the selected recurrent response vectors. The checker reconstructs the
auxiliary dependency graph, rejects self-targets and cycles, publishes a canonical topological order,
and verifies locally and after complete substitution:

\[
f_a+\sum_t m_{a,t}w_t\le w_a.
\]

Every effective expansion has a nonnegative integer fixed load and nonnegative integer multiplicities
on nonauxiliary target states. No response-local routed credit may remain on an eliminated auxiliary
coordinate.

For every response the checker reconstructs the fully substituted child vector, net fixed offset,
row load and margin and verifies:

\[
L_{\mathrm{elim}}(Q)\le L(Q),
\qquad
\mu_{\mathrm{elim}}(Q)\ge\mu(Q).
\]

## CMR2546: edgewise T07 semantic support

Every auxiliary expansion has one exact semantic record. It binds:

```text
block_id
auxiliary_state_id
expansion_record_sha256
fixed_load
source_state_claim_ids
fixed_load_transition_claim_ids
target_edge_semantics
expansion_statement
evidence
no_auxiliary_credit_statement
no_auxiliary_credit_evidence
```

Every target edge has one record containing:

```text
target_state_id
multiplicity
target_record_sha256
target_state_claim_ids
transition_claim_ids
edge_statement
evidence
```

Source and target state support must come from the exact T07 state claims of the slots selected by the
block's T11 rows. Transition support must come from the same selected-slot T07 transition banks. Every
target edge requires nonempty state and transition support. A positive fixed load requires nonempty
transition support.

These records prove exact documentary claim coverage. They do not prove the statements or evidence
mathematically true.

## CMR2547: selected-response and strict-margin stability

The older acyclic checker recomputes a deterministic eliminated-row minimizer. T12 now compares that
result with the exact T11 row bridge.

For every row, complete elimination must satisfy:

```text
eliminated selected response = T11 selected response
eliminated selected row load <= T11 minimum row load
eliminated selected margin >= T11 strict margin
```

The checker publishes one selected-response stability record binding the T11 row bridge and the exact
eliminated-row record. This prevents weighted substitution from changing the recurrence operation while
still claiming only abstract strictness preservation.

## CMR2548: typed artifacts and noncircular synchronization

Every proved block requires one internal artifact of kind:

```text
recurrent-block-auxiliary-elimination-proof
```

Its exact support is:

1. the block's T11 common-weight artifact;
2. the block's T11 closure artifact; and
3. every selected-slot T07 semantic artifact used by the block.

The per-block verification digest seals the record core, complete elimination wrapper, artifact and
all three support banks. The record core excludes its verification digest, avoiding a hash fixed point.

The aggregate proof bank commits to the independent T07 state and transition banks, the combined T11
closure bank, every T12 record, every elimination, every per-block artifact and every proof bundle.

When `AUXILIARY_EXPANSIONS_SEMANTIC` closes, its unique artifact must have kind
`auxiliary-expansion-proof`, locator

```text
auxiliary-semantics-frontier://AUXILIARY_EXPANSIONS_SEMANTIC
```

and the reconstructed aggregate digest. Its immediate support is exactly the two T07 obligation
artifacts and the two T11 obligation artifacts.

The T12 target artifact has kind `auxiliary-semantics-proof`, locator

```text
auxiliary-semantics-frontier://T12_AUXILIARY_SEMANTICS
```

and the same proof-bank digest. Obligation closure, effective target completion and reconstructed T12
readiness must agree exactly.

## CMR2549: honesty boundary and executable endpoint

Passing the checker establishes exact T11 block identity, exact recursive auxiliary coverage, an
acyclic expansion graph, finite weighted domination, zero auxiliary credit, complete response
substitution, selected-response stability, load and margin monotonicity, exact T07 claim support, typed
artifacts and noncircular digest synchronization.

It does not prove that:

- any expansion statement, fixed load or multiplicity is mathematically correct;
- the cited T07 state or transition claims are true or logically sufficient;
- the T11 rows describe the genuine all-`n` recurrence;
- a nonauxiliary target has the intended external state meaning;
- cross-block state identifications or component scales are correct;
- interface rows are exhaustive or the global rank is well founded;
- every exceptional chamber closes; or
- the quotient implies `D(n)=2n`.

Both T12 checkers always report:

```text
all_n_proved_by_checker = 0
```

Run the canonical endpoint with:

```bash
python scripts/check_prime_power_auxiliary_semantics_frontier_v2.py certificate.json
```

The next exact fronts are T13 cross-block state equivalence, T14 component scales, and the T15--T18
interface, rank, state-predicate and final-row theorem banks.

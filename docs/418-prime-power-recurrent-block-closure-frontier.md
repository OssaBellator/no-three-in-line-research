# Prime-power recurrent-block closure frontier

This chapter records CMR2534--CMR2541. It makes

```text
T11_RECURRENT_BLOCK_CLOSURE
CLOSED_STRICT_RECURRENT_BLOCKS
```

an exact documentary proof surface over the already fixed T04, T06 and T10 banks.

The executable checker is:

```text
scripts/check_prime_power_recurrent_block_closure_frontier.py
```

It reuses `check_prime_power_common_recurrent_block_weights.py` for finite common-weight arithmetic,
but does not accept that older certificate as a parallel population. Every common row must first be
bridged back to the exact selected T03/T05/T06/T10 data.

## CMR2534: parallel common-weight population defect

The older common-weight checker accepts its own routed-row certificate list. It correctly checks one
primitive positive weight vector, exact row margins, recurrent support, strong connectivity and
recurrent exits relative to those rows.

By itself, however, it does not prove that its rows are the exact rows selected by the current T06
policy and proved through T10. Using it directly for T11 would permit a second, parallel recurrent
population.

T11 therefore derives its block census from T04 and its row census from T08 before reading any
common-weight certificate.

## CMR2535: exact skeleton-derived recurrent-block census

Every T04 unit of kind `recurrent-block` receives exactly one open/proved T11 record. The record binds:

```text
block_id
unit_id
unit_identity_sha256
parent_global_state_ids
local_parent_state_ids
active_row_ids
t04_population_payload_sha256
```

The global parent list is the exact T04 parent-binding list. The active row list is reconstructed by
looking up the unique T08 row for every parent. Missing, extra, duplicated or reordered block records
are rejected.

A proved block requires the corresponding T04 block population record and artifact to be proved.

## CMR2536: exact common-row identity bridge

A proved block contains one validated common-weight certificate. Its SCC state list must equal the
complete set of local parents reconstructed from the T08 rows.

For every active row, the checker locates the unique common row with the same local parent and requires:

1. the common row fibre equals the selected T03 fibre;
2. the common row's linked operation certificate equals the selected slot's exact T05 certificate;
3. the T03 `labelled_vectors` list equals the common row exposure table;
4. the T03 `row_loads` list equals the complete common row arithmetic table; and
5. the common minimum row load equals the proved T06 slot score.

The resulting bridge record seals the T03 payload, T05 geometry, T06 score, T10 semantic row and the
common routed-row and margin certificates. A common-weight proof can therefore no longer float over a
different finite row family.

## CMR2537: exact selected-credit-unit bridge

T11 gives the previously generic T03 `routed_credits` entries the exact unit schema:

```text
child_state_id
unit_index
selected_response_sha256
```

For one selected response and child, unit indices must be exactly

```text
0, 1, ..., routed_count - 1.
```

Every T10 route assignment must use the child named by its literal credit unit. Aggregating the unit
bank by child must reproduce exactly the selected response's `credit_routes` vector in the common
row-margin certificate.

This bridge distinguishes the simultaneously selected response from alternative response records and
prevents a strict common-weight row from using a different credit vector from T10.

## CMR2538: primitive common weights and strict recurrent support

The embedded finite common-weight checker requires:

- one positive integer weight for every shared row state;
- greatest common divisor one;
- exactly one routed row for every SCC parent;
- each row parent budget equal to its common parent weight;
- each child-weight table equal to the common restriction;
- the exact recurrent support graph from positive child coordinates;
- no recurrent edge leaving the declared SCC;
- strong connectivity; and
- positive margin on every row.

Thus every proved block satisfies the finite condition

\[
\boxed{
\text{primitive positive common weights}
\land
\text{recurrent closure}
\land
\text{strong connectivity}
\land
\min_p\mu_p>0.
}
\]

The T04 `local_states` list must equal the common shared-state registry, and its `recurrent_rows` list
must equal the exact T08 active-row IDs.

Nonrecurrent exits are published separately. They do not invalidate recurrent-core closure because
auxiliary and interface semantics remain the downstream T12 and T15 fronts.

## CMR2539: typed per-block artifacts and noncircular sealing

Every proved block requires two internal artifacts:

```text
recurrent-block-common-weight-proof
recurrent-block-closure-proof
```

The common-weight artifact binds the complete common-weight record and cites exactly:

- the T04 block-population artifact;
- every selected-slot T05 geometry artifact;
- every selected-slot T06 score artifact;
- every T06 global-parent application artifact in the block; and
- every T10 routed-credit artifact in the block.

The closure artifact cites the common-weight artifact and binds the block record's core digest.

The block verification digest seals the record core, common-weight record and both artifacts. The
record core excludes the verification digest itself, so the completion seal is not a hash fixed point.

## CMR2540: obligation and atomic-target synchronization

The aggregate common-weight bank commits to the exact T04, T06 and T10 proof banks, expected recurrent
blocks, all common-weight records and all common-weight artifacts.

The separate closure bank commits to the common-weight bank, all block status records, all closure
artifacts and every per-block proof bundle.

When `CLOSED_STRICT_RECURRENT_BLOCKS` closes, its two required artifacts must be:

```text
block-closure-proof
common-weight-proof
```

with locators:

```text
recurrent-block-closure-frontier://CLOSED_STRICT_RECURRENT_BLOCKS/block-closure-proof
recurrent-block-closure-frontier://CLOSED_STRICT_RECURRENT_BLOCKS/common-weight-proof
```

and digests equal to the independently reconstructed closure and common-weight banks. Both cite exactly
the `CANDIDATE_POLICY_CORRECT` and `CREDIT_ROUTING_SEMANTIC` obligation-artifact bundles.

The T11 target artifact has kind `block-closure-proof`, locator:

```text
recurrent-block-closure-frontier://T11_RECURRENT_BLOCK_CLOSURE
```

and proof digest equal to the combined noncircular T11 bank. Reconstructed readiness must agree with
both semantic closure and effective atomic-target completion.

## CMR2541: honesty boundary and executable endpoint

Passing the checker establishes exact block and row census, exact T03/T05/T06/T10 ancestry, exact
finite common-weight arithmetic, primitive positive weights, recurrent closure, strong connectivity,
strict margins, typed support and digest synchronization.

It does not prove that:

- the T02 recurrence is genuine or exhaustive;
- the T06 score theorem has its intended external meaning;
- the T08 family is the genuine simultaneous recurrence family;
- the T09 resource model is physically exhaustive;
- any T07 or T10 semantic statement is mathematically true;
- nonrecurrent auxiliary or interface exits are semantically valid;
- cross-block equivalences or scales are correct;
- every exceptional chamber closes; or
- the quotient implies `D(n)=2n`.

The checker always reports:

```text
all_n_proved_by_checker = 0
```

Run it with:

```bash
python scripts/check_prime_power_recurrent_block_closure_frontier.py certificate.json
```

The next exact fronts are T12 auxiliary semantics, T13 state equivalence, T14 component scales and the
T15--T18 interface/rank/state-predicate/row-theorem banks.

# Prime-power candidate-policy frontier

This chapter records CMR2502--CMR2509. It makes `T06_CANDIDATE_POLICY` and
`CANDIDATE_POLICY_CORRECT` an exact noncircular candidate-minimization proof surface.

The checker is:

```text
scripts/check_prime_power_candidate_policy_frontier.py
```

It composes the corrected T05 geometry/selector bank with the exact T07
fate/transition/state bank and the independently expected operation-slot registry.

## CMR2502: common-weight dependency-cycle isolation

The older `check_prime_power_common_weight_candidate_policy.py` checker imports recurrent-population
and common-recurrent-block-weight certificates. Those objects belong to the later recurrent-block
closure front.

The fixed atomic proof DAG instead requires:

```text
T05_GEOMETRY_SELECTORS + T07_FATE_TRANSITION_STATE
    -> T06_CANDIDATE_POLICY
    -> T11_RECURRENT_BLOCK_CLOSURE
```

Using later common weights as the definition of T06 would reverse this dependency and create a proof
cycle. The new T06 checker therefore uses exact externally proved labelled-row scores supported only
by T05 and T07.

The older common-weight checker remains useful later as a recurrent-block consistency audit; it is not
the T06 closure object.

## CMR2503: exact slot score bank

Every expected operation slot has one exact open/proved score record.

A proved score records:

```text
slot_id
parent_state_id
slot_population_payload_sha256
row_loads_sha256
slot_selector_summary_sha256
slot_semantic_certificate_sha256
minimum_labelled_row_load
score_statement
evidence
```

It requires one artifact of kind:

```text
candidate-score-proof
```

citing exactly the slot's T05 geometry artifact and T07 semantic artifact. The score proof bundle
binds all identities, the external proof pointer and both support lists.

The checker treats the integer score as a proved external statement. It does not infer the score from
opaque `row_loads` JSON.

## CMR2504: complete candidate sets from the independent registry

Candidate sets are reconstructed before policy data are read.

For every `parent_state_id`, the exact candidate set is the complete sorted set of expected operation
slots with that parent. Counts or self-declared candidate lists are not accepted.

Every parent has one open/proved policy record containing the exact candidate slot list. A proved
parent policy requires every candidate score and one artifact of kind:

```text
parent-candidate-policy-proof
```

whose support is the complete candidate-score artifact set.

## CMR2505: deterministic minimization

For a proved parent, the checker computes the winner by:

```text
(minimum_labelled_row_load, slot_id)
```

The parent record publishes:

- the minimum score;
- the exact minimizer count;
- the selected slot;
- each candidate's nonnegative score gap;
- minimizer and selected flags.

Thus ties are resolved by the lexicographically least slot ID, and a supplied winner cannot float
independently of the complete score bank.

## CMR2506: exact T02 application-to-winner binding

Every T02 global-parent application has one exact T06 application record. It binds:

```text
parent_global_state_id
local_parent_state_id
t02_application_record_id
applied_slot_id
policy_selected_slot_id
```

A proved application requires the T02 applied slot to equal the reconstructed parent-policy winner.

Its artifact kind is:

```text
candidate-policy-application-proof
```

and its exact support consists of the parent-policy artifact and the T02
global-parent-application artifact.

This closes the documentary gap between computing a candidate winner and actually using that winner
in every recurrence-skeleton parent.

## CMR2507: exact three-level artifact hierarchy

The internal T06 proof hierarchy is:

```text
T05 geometry + T07 semantics
    -> candidate score
    -> parent candidate policy
    -> T02 global-parent application
```

Every support list is sorted, duplicate-free and exact. Artifact IDs are globally unique across the
three T06 levels.

The aggregate bank binds all score, parent and application records, artifacts and per-level bundles,
together with exact T02 application, T05 selector and T07 semantic identities.

## CMR2508: obligation and atomic-target sealing

When `CANDIDATE_POLICY_CORRECT` closes, its unique required artifact must have kind:

```text
candidate-policy-proof
```

locator:

```text
candidate-policy-frontier://CANDIDATE_POLICY_CORRECT
```

and digest equal to the reconstructed T06 policy bank. Its support is exactly the two T05 obligation
artifacts and the two T07 obligation artifacts.

The T06 atomic target artifact has the same fixed kind, locator:

```text
candidate-policy-frontier://T06_CANDIDATE_POLICY
```

and the same noncircular policy-bank digest.

Reconstructed readiness must agree with closure of `CANDIDATE_POLICY_CORRECT` and effective
completion of `T06_CANDIDATE_POLICY`.

## CMR2509: honesty boundary and executable endpoint

Passing the checker proves exact candidate-set reconstruction, deterministic minimization,
application-to-winner identity, artifact support and digest binding. It does not prove that:

- the supplied score statement is mathematically true;
- `row_loads` have the intended recurrence meaning;
- T05 finite geometry covers every all-`n` case;
- T07 state and transition claims are true;
- the T02 recurrence is genuine and exhaustive;
- common recurrent-block weights exist;
- any exceptional chamber closes; or
- the quotient implies `D(n)=2n`.

The checker always reports:

```text
all_n_proved_by_checker = 0
```

Run it with:

```bash
python scripts/check_prime_power_candidate_policy_frontier.py certificate.json
```

The next exact front is T08/T09/T10: active-row-family exhaustiveness, destroyed-resource-model
exhaustiveness and routed-credit semantics.

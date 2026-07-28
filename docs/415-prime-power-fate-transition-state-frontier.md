# Prime-power fate, transition and state semantic frontier

This chapter records CMR2494--CMR2501. It corrects the T05 closure-record execution path and makes
`T07_FATE_TRANSITION_STATE` together with `FATE_TRANSITION_STATE_SEMANTICS` an exact proof-work
surface.

The executable checkers are:

```text
scripts/check_prime_power_geometry_selector_frontier_v2.py
scripts/check_prime_power_fate_transition_state_frontier.py
```

The result remains documentary. It seals exact semantic statements and their support; it does not
decide whether those statements are mathematically true.

## CMR2494: corrected T05 closure execution

The original T05 checker reconstructed the geometry and selector proof banks correctly, but its final
synchronization read the field `closed` from `proof_obligations`. The closure checker publishes that
field in `obligation_closure_records`.

The version-2 execution adapter supplies a merged closure view only to the T05 module. The underlying
closure checker and obligation-artifact validator remain unchanged. The certificate schema and all
T05 proof digests are unchanged.

The canonical executable T05 endpoint is now:

```bash
python scripts/check_prime_power_geometry_selector_frontier_v2.py certificate.json
```

## CMR2495: exact literal semantic-subject bank

For every independently expected T03 slot, T07 reconstructs three exact subject banks.

- one fate subject for every literal `owner_fate_witnesses` entry;
- one parent-state subject plus one state subject for every `labelled_vectors` entry; and
- one transition subject for every literal `transitions` entry.

Every subject contains its slot, kind, occurrence index and literal JSON value. The occurrence index
prevents repeated equal values from collapsing into one subject.

## CMR2496: exact claim coverage

Every subject has exactly one canonical semantic claim with fields:

```text
claim_id
claim_kind
subject_sha256
statement
support_claim_ids
evidence
semantic_claim_sha256
```

The claim ID is reconstructed from the kind, slot ID, occurrence index and subject digest. Missing,
extra, reordered or digest-mismatched claims are rejected.

A proved slot therefore cannot cite a summary statement while leaving individual literal witnesses,
states or transitions without a review record.

## CMR2497: acyclic semantic-claim support

Every semantic claim may cite other claims in the same exact slot certificate. Support IDs must be
sorted, duplicate-free, known and non-self-referential.

The checker reconstructs the complete support-edge bank and a canonical heap-ordered topological
claim order. A support cycle is rejected.

Acyclicity proves only noncircular documentary support. It does not establish that the cited semantic
claims logically imply one another.

## CMR2498: exact T03 and T04 artifact ancestry

A proved slot requires exactly one artifact of kind:

```text
slot-fate-transition-state-proof
```

Its support is reconstructed as:

1. the unique T03 slot-population artifact for that slot; and
2. every T04 recurrent-block or interface-row population artifact whose skeleton parent uses the
   slot.

The slot proof digest seals the exact T03 payload, complete semantic certificate, slot artifact and
both support lists. A slot cannot close while its T03 population or any using T04 assembly unit
remains unproved.

## CMR2499: separate state and transition proof banks

The checker builds two aggregate banks.

The state-semantics bank binds all fate and state claims together with the exact T03/T04 ancestry,
slot status records, semantic certificates, artifacts and per-slot bundles.

The transition bank binds the complete transition-claim bank with the same exact slot census and
proof artifacts.

When `FATE_TRANSITION_STATE_SEMANTICS` is proved, its required artifacts must be:

```text
state-semantics-proof
transition-proof
```

with locators:

```text
fate-transition-state-frontier://FATE_TRANSITION_STATE_SEMANTICS/state-semantics-proof
fate-transition-state-frontier://FATE_TRANSITION_STATE_SEMANTICS/transition-proof
```

and digests equal to the independently reconstructed banks. Both cite exactly the
`SLOT_AND_CANDIDATE_POPULATION` obligation artifact bank.

## CMR2500: noncircular T07 target binding and synchronization

The combined T07 bank contains the state-bank digest, transition-bank digest, exact slot-status bank
and exact slot-artifact bank.

It excludes the obligation registry, current-frontier certificate and target-artifact registry from
the sealed digest because those ancestors contain the T07 obligation or completion digests.

The T07 target artifact must have kind:

```text
transition-state-proof
```

locator:

```text
fate-transition-state-frontier://T07_FATE_TRANSITION_STATE
```

and proof digest equal to the combined noncircular bank.

Reconstructed T07 readiness must agree with both closure of
`FATE_TRANSITION_STATE_SEMANTICS` and effective completion of
`T07_FATE_TRANSITION_STATE`.

## CMR2501: honesty boundary and executable endpoint

Passing the checker establishes exact literal subject coverage, canonical semantic statements,
acyclic support, T03/T04 ancestry and digest synchronization. It does not prove that:

- an owner or fate assignment has its intended external meaning;
- a state label denotes the intended mathematical state;
- a transition preserves the intended invariant or reaches the stated child;
- the supplied recurrence and population are genuine and exhaustive;
- the candidate policy is correct;
- any recurrent block is closed or strict; or
- the quotient implies `D(n)=2n`.

The checker always reports:

```text
all_n_proved_by_checker = 0
```

Run it with:

```bash
python scripts/check_prime_power_fate_transition_state_frontier.py certificate.json
```

# T03 hard-core population bridge

## Scope

The T21 scalar theory through CMR2781 evaluates and constrains every finite side-four hard-core survivor background once that background is known. The unresolved interface is upstream: the canonical T03 schema reserves literal `survivor_background`, `response_family` and `selector_data` fields, but the actual parent rule and genuine slot populations are not present.

This chapter introduces an executable bridge from any future exact T03 slot/candidate-population certificate to the established T21 scalar selector.

Run the self-test with:

```text
python scripts/check_prime_power_hard_core_population_bridge.py --self-test
```

Run it against a genuine T03 certificate with:

```text
python scripts/check_prime_power_hard_core_population_bridge.py \
  t03-certificate.json \
  --write artifacts/hard-core-population-bridge.json
```

The bridge does not create the parent rule, invent operation slots, populate survivor points, or prove any T03 payload mathematically correct. It validates identity and scalar consistency only and permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2782--CMR2793

### CMR2782 — exact hard-core host projection

The bridge reconstructs the canonical side-four raw-host catalogue independently and selects exactly the eleven positive-minimum hosts.

Their response-family census is:

```text
9 hosts: Q1=(3,0,1,2), Q4=(3,2,1,0)
2 hosts: Q4=(3,2,1,0) only
20 scalar chambers in total
```

The bridge contract stores all eleven exact host IDs and rejects any response family outside those two canonical forms.

### CMR2783 — exact T03 certificate ancestry

Certificate mode first delegates to:

```text
check_prime_power_slot_candidate_population_frontier.validate_certificate
```

and reconstructs the exact T03 certificate before reading any population payload.

The independently expected operation slots are taken from the exact chain:

```text
T03 certificate
  -> T02 rule-exhaustiveness certificate
  -> source-truth certificate
  -> source-statement registry
  -> rule-source provenance
  -> clause manifest
  -> expected-slot registry
```

No hard-core slot is inferred from a payload-supplied host ID. A slot enters the bridge only when its independently expected host is one of the eleven canonical hard-core hosts.

### CMR2784 — exact hard-core slot census

For every hard-core expected slot, the bridge requires exactly one T03 status record in the canonical `open`, `populated` or `proved` state.

It reconstructs separate counts for:

```text
open_hard_core_slots
data_populated_hard_core_slots
t03_proved_hard_core_slots
scalar_projection_ready_slots
```

The bridge manifest retains one record per hard-core slot in expected-slot order. Non-hard-core slots are ignored by this projection but remain governed by the full T03 checker.

### CMR2785 — literal survivor-background validation

Every non-open hard-core slot must contain one literal `survivor_background`.

The bridge requires:

1. a JSON list;
2. each point to be an exact two-integer list;
3. Boolean values not to masquerade as integers;
4. pairwise-distinct points;
5. every point outside the side-four response grid
   \(\{0,1,2,3\}^2\).

The point set is sorted canonically before hashing and scalar evaluation.

An open hard-core slot must contain no payload and is recorded as:

```text
bridge_status = awaiting_population
```

### CMR2786 — exact response-family binding

For every populated or proved hard-core slot, the T03 payload field

```text
population_data.response_family
```

must equal the response family reconstructed from the independently expected raw host.

Thus a two-response host must carry exactly:

```text
[(3,0,1,2), (3,2,1,0)]
```

in canonical order, while a singleton host must carry exactly:

```text
[(3,2,1,0)]
```

A payload cannot silently remove an admissible response, add an inadmissible response, or change response order.

### CMR2787 — exact arbitrary-background scalar projection

For the validated survivor background \(B\), the bridge recomputes:

\[
E_+(B),\qquad E_-(B),\qquad W(B),
\]

and then

\[
\Delta(B)=E_+(B)-E_-(B)+W(B)-3.
\]

For a two-response host it selects:

```text
Q1 iff Delta <= 0
Q4 iff Delta > 0
```

For a singleton host it selects `Q4` for all signatures while still recording the exchange delta diagnostically.

The bridge does not trust a supplied scalar score or selected response.

### CMR2788 — canonical selector-data subrecord

Every non-open hard-core T03 payload must contain an exact `selector_data` object with fields:

```text
selector_kind
hard_core_host_id
survivor_background_sha256
survivor_background_points
positive_pivot_energy
negative_pivot_energy
point_weight_sum
delta_q1_minus_q4
selected_response
selector_condition
hard_core_selector_sha256
```

The fixed selector kind is:

```text
side-four-hard-core-exchange-v1
```

The selector-data digest binds the host, literal background, all energy terms, the selected response and the weak/strict/singleton chamber condition.

Any stale or hand-entered selector value inconsistent with the literal background is rejected.

### CMR2789 — open, populated and proved separation

The bridge distinguishes three independent facts:

1. whether a hard-core slot has literal population data;
2. whether its scalar selector projection is exact;
3. whether T03 marks the slot `proved`.

A `populated` slot with a valid literal background and exact selector data is scalar-projection ready but is not T03-proved.

A `proved` slot is counted separately, relying on the upstream T03 checker to verify the required T02 support artifact and proof-bundle binding.

Neither state proves any T21 semantic chamber argument.

### CMR2790 — exact population-gap manifest

The derived bridge manifest records:

- all eleven canonical hard-core host IDs;
- every expected hard-core slot;
- its T03 status;
- its fibre and payload digest when present;
- its exact selector projection when present;
- open/populated/proved counts;
- `Q1` and `Q4` selected-slot counts;
- scalar-readiness and T03-proof readiness separately;
- a top-level `manifest_sha256`.

This makes the first T21 population gap machine-readable:

```text
open slot -> supply literal T03 payload
non-open slot -> exact scalar selector projection must match
proved slot -> upstream T03 proof support must also validate
```

### CMR2791 — readiness is not semantic closure

The bridge publishes:

```text
all_hard_core_slots_scalar_ready
all_hard_core_slots_t03_proved
t21_semantic_chambers_proved = 0
```

Even if every hard-core slot is populated and T03-proved, the bridge does not infer any of:

- destroyed-threshold consequences;
- owner-fate semantics;
- labelled child vectors;
- routed-credit correctness;
- row-load correctness;
- transition correctness;
- return or interface terms;
- recurrent contraction;
- any of the twenty host-labelled chamber proofs.

Those remain ordinary mathematical obligations.

### CMR2792 — executable fixtures and mutation rejection

The self-test reconstructs all eleven hard-core hosts and runs two canonical banks.

The mixed bank contains:

```text
11 hard-core slots
3 open
4 populated
4 proved
8 scalar-projection ready
```

The complete bank contains eleven proved, scalar-ready slots while retaining:

```text
t21_semantic_chambers_proved = 0
all_n_proved_by_checker = 0
```

Ten corruptions are rejected:

1. duplicate survivor point;
2. response-grid survivor point;
3. response-family corruption;
4. delta corruption;
5. selected-response corruption;
6. payload-host corruption;
7. open status with a payload;
8. missing status record;
9. honesty-claim corruption;
10. manifest-seal corruption.

The canonical bridge-contract digest is:

```text
c7773e0f18779f6fa89db7d31e802c281e4e2618e60096a9a3d86471d08d528c
```

### CMR2793 — frontier consequence and honesty boundary

The branch now has an exact executable route from a genuine T03 certificate to the complete finite T21 scalar theory.

The first missing object is no longer ambiguous: the repository needs the actual parent rule and, for every resulting hard-core expected slot, a literal mathematically justified T03 payload containing the genuine survivor background and exact response family. Once supplied, the bridge recomputes the selector and exposes any inconsistency immediately.

This closes no mathematical target. In particular:

```text
actual_parent_rule_present = 0
actual_t03_population_supplied_by_bridge = 0
t21_semantic_chambers_proved = 0
all_n_proved_by_checker = 0
```

T01 source truth, T02 genuine recurrence exhaustiveness, complete T03/T04 population, all semantic T05--T21 arguments and every downstream T22--T43 implication remain open.

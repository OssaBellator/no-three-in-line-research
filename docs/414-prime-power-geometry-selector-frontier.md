# Prime-power geometry and selector frontier

This chapter records CMR2486--CMR2493. It makes
`T05_GEOMETRY_SELECTORS` and the semantic obligation
`GEOMETRY_SELECTOR_CORRECT` an exact documentary proof surface.

The checker is:

```text
scripts/check_prime_power_geometry_selector_frontier.py
```

It composes the exact T03 slot/candidate population bank, the exact T04
block/interface population bank, the existing finite linked-operation geometry checker, the typed
obligation-artifact registry and the sealed atomic-target artifact registry.

The result remains bounded by the supplied finite systems. It does not prove that the supplied
sources, recurrence, slots, blocks or interfaces are the genuine exhaustive all-`n` construction.

## CMR2486: exact slotwise geometry/selector work bank

Every independently expected T03 slot has exactly one T05 record.

- `open`: no linked-operation geometry certificate and no slot proof artifact;
- `proved`: one exact linked-operation geometry certificate and one sealed slot-specific artifact.

A proved record uses

```text
geometry-selector-slot-registry://<slot ID>
```

and its digest is the reconstructed slot proof-bundle digest. A slot cannot be proved unless its T03
payload and T03 population artifact both exist.

## CMR2487: exact T03 geometry projection

For each proved slot, the checker validates the existing
`check_prime_power_linked_operation_selector.py` certificate and reconstructs the exact finite
geometry projection:

```text
points                         = pre_response_points
removals                       = removed_point_indices
survivor_background            = source background_points
owner_fate_witnesses           = canonical flattened rank-1/2/3 fate records
response_family                = every literal perfect-matching response
selector_data                  = exact finite selector and threshold summary
```

All six fields must agree exactly with the corresponding T03 literal payload fields. The host ID must
also equal the T03 host. Thus the geometry certificate cannot describe a parallel fibre unrelated to
the one populated and sealed at T03.

The selector summary records the canonical host and source identities, linked finite certificate
hashes, selected response, minimum new-triple count, destroyed-current-triple count, minimum delta,
strictness flag, minimizer count and complete response-record hashes.

## CMR2488: responsewise delta and threshold identity

The nested finite checker verifies every response `Q` and the identity

```text
direct_delta(Q) = new_background_triples(Q) - destroyed_current_triples.
```

It also verifies that

```text
minimum_delta < 0
```

is equivalent to

```text
minimum_new_triples < destroyed_current_triples.
```

The T05 bank records separate geometry and selector summaries for each slot. These are exact finite
arithmetic statements for the supplied point sets and response families, not a proof that those
families exhaust the intended recurrence for arbitrary `n`.

## CMR2489: exact T03 and T04 proof support

A proved slot requires one artifact of kind

```text
slot-geometry-selector-proof
```

with two reconstructed support lists:

1. the unique T03 slot-population artifact for that slot; and
2. every proved T04 recurrent-block or interface-row population artifact whose skeleton parent uses
   that slot.

The checker rejects missing, unrelated, duplicate and self support. A geometry slot therefore cannot
close before its exact population ancestry and every assembly unit using it are proved.

## CMR2490: separate geometry and selector obligation banks

The checker builds two aggregate banks.

The geometry bank binds the exact T03 and T04 population digests, all slot status records, every
linked finite geometry certificate, every direct-delta summary, every slot proof artifact and every
per-slot bundle.

The selector bank binds the same slot census together with all full-selector summaries, minimizers,
threshold identities, slot proof artifacts and per-slot bundles.

When `GEOMETRY_SELECTOR_CORRECT` is proved, its two required typed artifacts must be:

```text
geometry-proof
selector-proof
```

with locators

```text
geometry-selector-frontier://GEOMETRY_SELECTOR_CORRECT/geometry-proof
geometry-selector-frontier://GEOMETRY_SELECTOR_CORRECT/selector-proof
```

and digests equal to the reconstructed geometry and selector bank digests respectively. Both must
cite exactly the `SLOT_AND_CANDIDATE_POPULATION` artifact bank.

## CMR2491: noncircular T05 target binding

The combined T05 proof bank contains the geometry-bank digest, selector-bank digest, exact slot
record bank and exact slot artifact bank.

It deliberately excludes the obligation-registry certificate, current-frontier certificate,
atomic-completion records and atomic-target registry from the sealed digest. Those ancestors contain
the geometry/selector obligation digests or the T05 completion digest, so including them would make
the T05 proof object hash itself indirectly.

The T05 target artifact must have kind

```text
geometry-selector-proof
```

locator

```text
geometry-selector-frontier://T05_GEOMETRY_SELECTORS
```

and proof digest equal to the noncircular combined T05 bank digest.

## CMR2492: exact readiness synchronization

T05 readiness requires all of the following:

1. T03 slot/candidate population is ready;
2. T04 block/interface population is ready;
3. every expected slot has a proved geometry/selector record;
4. every slot has exactly one linked finite geometry certificate;
5. every slot has exactly one proof artifact with exact T03/T04 support;
6. the `geometry-proof` and `selector-proof` obligation artifacts bind the reconstructed banks; and
7. the T05 atomic target artifact binds the reconstructed combined bank.

Reconstructed readiness must equal both closure of `GEOMETRY_SELECTOR_CORRECT` and effective
completion of `T05_GEOMETRY_SELECTORS`.

## CMR2493: honesty boundary and executable endpoint

Passing the checker establishes exact finite data identity, responsewise arithmetic, threshold
identity, artifact support and digest binding. It does not prove that:

- the source statements or parent rule are genuine and exhaustive;
- the T03 or T04 population data have their intended external meaning;
- the finite raw-host family covers every all-`n` geometric case;
- the declared owner/fate, state labels or transitions are semantically correct;
- the candidate policy is the intended global recurrence policy;
- any recurrent block is closed, strongly connected or strict;
- any exceptional chamber closes; or
- the global quotient implies `D(n)=2n`.

The checker always reports:

```text
all_n_proved_by_checker = 0
```

Run it with:

```bash
python scripts/check_prime_power_geometry_selector_frontier.py certificate.json
```

The next mathematical fronts are candidate-policy correctness, fate/transition/state semantics,
active-row and destroyed-resource exhaustiveness, routed-credit semantics, genuine recurrent-block
closure, cross-block semantics and interface/rank proof.

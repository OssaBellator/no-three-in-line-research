# Prime-power slot and candidate population frontier

This chapter records CMR2470--CMR2477. It makes the third atomic source-to-population target,
`T03_SLOT_CANDIDATE_POPULATION`, an exact documentary proof surface.

The checker is:

```text
scripts/check_prime_power_slot_candidate_population_frontier.py
```

It composes the exact T02 rule-exhaustiveness frontier with the independently generated operation-
slot registry, the typed semantic-obligation registry and the forty-three-target execution schedule.

The result does **not** prove that any supplied point set, witness, response, selector, route, load or
transition is mathematically correct. It prevents T03 from closing through slot counts, host equality,
an unattached source hash or an opaque population certificate.

## CMR2470: exact three-state slot population bank

Every expected operation slot has exactly one record in canonical slot order. The allowed states are:

- `open`: no payload and no proof artifact;
- `populated`: one exact literal payload, but no T02-backed proof artifact yet;
- `proved`: one exact payload and one sealed slot-specific proof artifact.

This distinction preserves the research-start semantics of T03. Genuine population data may be
entered before T02 closes, but proof completion cannot be claimed until the required T02 evidence is
available.

Open records have null locator and digest. A populated record binds

```text
slot-candidate-population-data://<slot ID>
```

and its reconstructed data-bundle digest. A proved record binds

```text
slot-candidate-population-registry://<slot ID>
```

and its reconstructed payload/artifact/support bundle digest.

## CMR2471: literal population payload

Every non-open slot carries one canonical population payload. Its `population_data` object has the
exact ordered fields:

```text
points
removals
survivor_background
owner_fate_witnesses
response_family
feasibility_signatures
selector_data
labelled_vectors
routed_credits
row_loads
transitions
```

Thus the population source digest is recomputed from the literal data rather than accepted as an
unattached string. The checker verifies documentary presence and identity only; it does not prove
any field semantically correct or complete.

## CMR2472: canonical fibre identity

For a slot with expected host `H`, let `s` be the SHA-256 of the exact population-data object. The
payload must use

```text
fibre_id = H:<first 16 hexadecimal characters of s>
```

and must store `source_sha256 = s`. The host must equal the independently expected host in the
operation-slot registry. Fibre IDs are globally unique.

This removes the old gap in which a fibre ID and source digest could be supplied independently of
any literal population object.

## CMR2473: exact T02 support

A proved slot artifact has fixed kind

```text
slot-candidate-population-proof
```

and cites the exact T02 rule-exhaustiveness artifacts for:

- the slot's parent case;
- the slot's generating clause; and
- every global-parent application that selects that slot.

Slots not selected by a global recurrence parent still cite their exact case and clause artifacts,
because they remain members of the complete candidate family. Omitted, unrelated, duplicate,
unknown or self support is rejected.

## CMR2474: payload-to-proof sealing

The slot proof artifact contains a separate external proof locator/digest, proof statement and
evidence field. It also contains the exact population-payload digest.

The proved slot record does not repeat that external pointer. Instead, its digest commits to a
reconstructed bundle containing:

- the independent slot digest;
- the literal population-payload digest;
- the slot-proof-artifact digest; and
- the exact T02 support-artifact IDs.

The intermediate `populated` state commits only to the independent slot and literal payload. This
keeps data entry useful without confusing it with a completed proof.

## CMR2475: exact aggregate population certificate

The aggregate T03 proof bundle binds:

- the independently expected operation-slot registry;
- the exact T02 record bank;
- the exact T02 artifact bank;
- every slot population record;
- every literal population payload;
- every slot-specific proof artifact; and
- every reconstructed per-slot bundle.

It intentionally does not include an ancestor certificate containing the population obligation's own
digest. This avoids a self-referential certificate equation.

## CMR2476: obligation and atomic-target synchronization

Population readiness requires:

1. T02 rule exhaustiveness is ready;
2. every expected slot is in state `proved`;
3. every proved slot has exactly one literal payload and one exact proof artifact; and
4. the unique `population-certificate` artifact for `SLOT_AND_CANDIDATE_POPULATION` binds the
   aggregate T03 proof bundle.

The population artifact must use

```text
slot-candidate-population-registry://SLOT_AND_CANDIDATE_POPULATION
```

The checker then requires exact equality among:

- reconstructed slot/candidate population readiness;
- closure of `SLOT_AND_CANDIDATE_POPULATION`; and
- effective completion of `T03_SLOT_CANDIDATE_POPULATION`.

No one layer can close independently.

## CMR2477: honesty boundary and executable endpoint

The checker always publishes

```text
all_n_proved_by_checker = 0
```

Passing it establishes exact slot coverage, literal payload identity, canonical fibre/source binding,
T02 support and digest sealing. It does not prove the supplied population genuine, verify geometry,
selectors, fate, responses, routes or transitions, populate T04 recurrent-block/interface rows,
close an exceptional chamber or imply `D(n)=2n`.

Run it with:

```bash
python scripts/check_prime_power_slot_candidate_population_frontier.py certificate.json
```

The next genuine work is to enter actual population data for every expected slot, review every
slot-specific proof, close T03, and then build the separate T04 recurrent-block and interface-row
population bank.

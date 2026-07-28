# Prime-power rule-exhaustiveness frontier

This chapter records CMR2462--CMR2469. It makes the second atomic source-rule target,
`T02_RULE_EXHAUSTIVENESS`, an exact documentary proof surface.

The checker is:

```text
scripts/check_prime_power_rule_exhaustiveness_frontier.py
```

It composes the sealed source-statement/T01 frontier with the declarative parent-rule clause
manifest, the source provenance graph, the source-independent operation-slot registry, the global
recurrence skeleton, the typed obligation registry and the forty-three-target execution schedule.

The result does **not** prove that the supplied rule is genuine or exhaustive. The repository still
states that the actual parent rule is absent. The checker instead makes every missing T02 proof
component explicit and prevents an opaque `RULE_EXHAUSTIVE` or `T02_RULE_EXHAUSTIVENESS` flag from
closing without the exact supporting bank.

## CMR2462: fixed rule-exhaustiveness record bank

The checker reconstructs one exact record for every object in five categories:

1. every parent case;
2. every rule clause;
3. every finite parameter axis;
4. every excluded parameter row; and
5. every global parent in the recurrence skeleton.

The record IDs are canonical:

```text
case::<case ID>
clause::<clause ID>
axis::<clause ID>::<axis name>
exclusion::<clause ID>::<excluded-row SHA-256>
application::<global parent state ID>
```

Every record is either `open` or `proved`. Open records have null verification fields. A proved
record binds the canonical locator

```text
rule-exhaustiveness-artifact-registry://<record ID>
```

and the digest of its reconstructed one-artifact bundle.

## CMR2463: exact source support

Every proved rule record cites the complete sealed source-verification artifact set determined by
the source-provenance certificate.

- A parent-case record cites exactly the sources linked to that case.
- A clause record cites exactly the sources linked to that clause.
- An axis record cites exactly the sources linked to that clause/axis pair.
- An exclusion record cites exactly the sources linked to that clause/excluded-row pair.
- A global-parent application cites the union of the exact case and clause source supports.

A rule record cannot be proved while one of its required source statements remains open.

## CMR2464: exact internal rule support

The rule-artifact support relation is reconstructed rather than supplied freely.

- Every clause artifact cites all axis and exclusion artifacts belonging to that clause.
- Every parent-case artifact cites all clause artifacts declared applicable to that case.
- Every global-parent application artifact cites its exact parent-case and selected-clause
  artifacts.
- Axis and exclusion artifacts have no internal rule dependencies.

The resulting dependency direction is structurally acyclic:

```text
axis/exclusion -> clause -> case -> global-parent application.
```

Artifact IDs are globally unique, support lists are exact and an artifact cannot support itself.

## CMR2465: exact global-parent operation binding

The previous skeleton named only `source_rule_id` and `source_case_id`. It did not identify the
clause or admitted parameter row responsible for a global parent.

Every `application::<global parent>` record now supplies:

```text
source_case_id
source_clause_id
operation_slot_id
```

The checker resolves the slot in the source-independent expected operation-slot registry and
requires exact agreement of:

- skeleton rule ID;
- skeleton and slot case ID;
- slot and application clause ID;
- case/clause incidence in both directions;
- local parent-state ID;
- expected raw host;
- ordered state labels; and
- operation kind.

Because the slot registry is generated only from admitted Cartesian-product rows, resolving the
slot also binds the global parent to one exact admitted parameter row rather than merely to a case
name.

## CMR2466: sealed rule-manifest artifact

The existing `rule-manifest` obligation artifact for `RULE_EXHAUSTIVE` must use

```text
rule-exhaustiveness-registry://RULE_EXHAUSTIVE/rule-manifest
```

and bind a reconstructed manifest bundle containing:

- rule ID;
- rule-source digest;
- clause-manifest digest;
- expected operation-slot registry digest;
- recurrence-skeleton digest;
- parent-case digest; and
- clause digest.

Thus the typed artifact cannot point to a different rule, slot family or recurrence skeleton.

## CMR2467: sealed rule-exhaustiveness proof artifact

The existing `rule-exhaustiveness-proof` obligation artifact must use

```text
rule-exhaustiveness-registry://RULE_EXHAUSTIVE/rule-exhaustiveness-proof
```

and bind a reconstructed proof bundle containing:

- the sealed rule-manifest bundle digest;
- the sealed source-statement registry digest;
- the complete rule-exhaustiveness record-bank digest; and
- the complete rule-exhaustiveness artifact-bank digest.

The two existing typed obligation artifacts remain the unique `RULE_EXHAUSTIVE` path. This checker
does not create a parallel closure locator.

## CMR2468: exact RULE_EXHAUSTIVE and T02 synchronization

Rule readiness requires all of the following:

1. every source statement is proved with its sealed verification artifact;
2. every case, clause, axis, exclusion and global-parent application record is proved;
3. every proved record has exactly one artifact of its fixed kind;
4. every artifact has exact source and internal rule support; and
5. the two typed `RULE_EXHAUSTIVE` obligation artifacts bind the reconstructed bundles.

The checker then requires exact equality among:

- the reconstructed rule-readiness flag;
- closure of the semantic obligation `RULE_EXHAUSTIVE`; and
- effective completion of `T02_RULE_EXHAUSTIVENESS`.

No one layer can close independently of the others.

## CMR2469: honesty boundary and executable endpoint

The checker always publishes

```text
all_n_proved_by_checker = 0
```

Passing it establishes exact documentary coverage, source support, slot identity and digest
binding. It does not verify the external proof artifacts, prove the parent-case partition complete,
prove the supplied clauses are the genuine recurrence, populate any operation slot, close an
exceptional chamber or imply `D(n)=2n`.

Run it with:

```bash
python scripts/check_prime_power_rule_exhaustiveness_frontier.py certificate.json
```

The next genuine work remains to provide the actual source material and proofs, instantiate the
complete T02 bank, and subject the resulting parent-rule exhaustiveness theorem to ordinary
mathematical review before beginning T03 population closure.

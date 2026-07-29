# Prime-power final-premise frontiers

This chapter records CMR2614--CMR2629. It makes the ten targets

```text
T22_BASE_CASES_PREMISE
T23_RECURRENCE_PREMISE
T24_INVARIANT_PREMISE
T25_SELECTION_PREMISE
T26_RESOURCE_PREMISE
T27_CONTRACTION_PREMISE
T28_CROSS_BLOCK_PREMISE
T29_EXCEPTIONAL_PREMISE
T30_TERMINATION_PREMISE
T31_OBJECTIVE_TRANSLATION_PREMISE
```

exact documentary proof surfaces over the canonical T01--T21 target banks.

The executable endpoint is:

```text
scripts/check_prime_power_final_premise_frontiers.py
```

It permanently reports:

```text
all_n_proved_by_checker = 0
```

## CMR2614: exact premise-to-target registry

The checker fixes one canonical target for each of the ten final implication premises. The order is the
same as the fixed final-contract order, from `BASE_CASES_COMPLETE` through
`OBJECTIVE_TRANSLATION_TO_D_EQ_2N`. Missing, reordered or substituted premise/target identities are
rejected.

## CMR2615: exact T01--T21 dependency roots

For each premise target, the proof dependencies are reconstructed from the atomic target definition rather
than supplied by the premise record. Every dependency must lie in T01--T21.

The exact roots are:

```text
T22 <- T01
T23 <- T02, T19
T24 <- T05, T07
T25 <- T03, T06
T26 <- T08, T09, T10
T27 <- T11, T12
T28 <- T13, T14, T15, T16, T17, T18
T29 <- T20, T21
T30 <- T11, T16, T18
T31 <- T12, T16, T18, T19, T20, T21
```

## CMR2616: dependency-target support records

Every premise publishes one support record for every dependency target. Each record retains:

```text
dependency target ID
effective completion flag
target result and completion digests
typed target artifact ID and digest when complete
target artifact-bundle digest
external proof locator and digest when complete
```

Open dependency targets retain null artifact and proof fields but still publish their exact empty bundle and
result digests.

## CMR2617: no premature premise proof

A premise may be declared `proved` only after every exact dependency target is effectively complete. A
premise declared proved while any T01--T21 dependency remains open is rejected, even if the older premise
contract would otherwise store a documentary proof pointer.

## CMR2618: canonical premise records

Every premise has one record containing:

```text
premise ID
target ID
open/proved status
proof mode
exact dependency target IDs
dependency-support digest
canonical verification locator/digest when proved
note
```

The record status and proof mode must agree exactly with the fixed final implication contract.

## CMR2619: reviewed semantic implication

Every proved premise has exactly one semantic certificate containing:

```text
exact dependency support records
mathematical premise statement
dependency-to-premise implication statement
arbitrary-n scope statement
review boundary
evidence
```

Open premises contain no semantic certificate. Nonempty prose fields are documentary requirements, not a
machine proof of their statements.

## CMR2620: stable premise-artifact core

The typed premise artifact is projected to a stable core containing its identity, fixed artifact kind,
statement, semantic-obligation support, optional finite termination certificate and evidence.

The outward `final-premise-frontier://` locator and digest are deliberately excluded from this core before
hashing.

## CMR2621: stable atomic-target artifact core

The T22--T31 atomic target artifact is projected to a stable core containing its identity, fixed target kind,
statement, evidence, exact dependency-target support, namespace-qualified external support and independent
certificate references.

Its outward proof locator and digest are also excluded before hashing.

## CMR2622: noncircular per-premise bundle

For each proved premise, the checker reconstructs one proof bundle from:

```text
premise-record core digest
semantic-certificate digest
exact lower-target support digest
exact dependency target artifact IDs
stable premise-artifact core digest
stable atomic-target artifact core digest
```

No ancestor certificate SHA or outward locator/digest is used to define this bundle. Therefore the bundle can
be referenced by its ancestors without solving a self-referential hash equation.

## CMR2623: typed premise-artifact binding

The existing typed premise artifact must point to the reconstructed bundle by:

```text
locator = final-premise-frontier://PREMISE-ID
digest  = final_premise_frontier_proof_bundle_sha256
```

Its obligation-artifact support remains governed by the typed premise-artifact registry.

## CMR2624: atomic target-artifact binding

The corresponding T22--T31 atomic target artifact must point to the same bundle by:

```text
proof_locator = final-premise-frontier://TARGET-ID
proof_digest  = final_premise_frontier_proof_bundle_sha256
```

It must cite the exact typed artifacts of every dependency target and the namespace-qualified typed premise
artifact.

## CMR2625: contract effectiveness synchronization

For every premise, frontier readiness must equal the effective premise result in the fixed final implication
contract. A contract premise cannot be effective while its exact T01--T21 frontier record is open, and an
exact frontier record cannot be proved while the contract result is ineffective.

## CMR2626: atomic target synchronization

For every T22--T31 target, frontier readiness must equal `effective_target_complete` in the atomic execution
DAG. Open premise frontiers contain neither a typed premise artifact nor an atomic target artifact.

## CMR2627: aggregate T22--T31 proof bank

The aggregate bank publishes digests for:

- the exact T20 and T21 chamber proof banks;
- every dependency-target support record;
- all ten premise frontier records;
- every proved semantic certificate; and
- every proved per-premise proof bundle.

The checker also publishes exact open premise and target ID lists and the shared contract, premise-registry,
target-registry and T21 certificate identities.

## CMR2628: honesty boundary

Passing a premise frontier proves exact documentary ancestry, artifact support, noncircular bundle binding
and synchronization with the existing contract and atomic target. It does not prove any lower target true,
does not prove the dependency statements imply the premise, and does not establish arbitrary-`n` coverage.
Every premise artifact still requires ordinary mathematical review.

## CMR2629: executable endpoint

`scripts/check_prime_power_final_premise_frontiers.py` validates the ten exact T22--T31 premise banks and
publishes the conditional `t22_t31_final_premise_frontiers_ready` flag.

The script passes `python -m py_compile`. A complete nested certificate fixture was not available, so no full
dependency-backed regression run is claimed. With the branch's genuine mathematical premises still open,
the T22--T31 readiness flag remains zero and the no-three-in-line conjecture remains open.

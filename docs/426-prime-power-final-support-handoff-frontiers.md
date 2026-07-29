# Prime-power final support, handoff and root frontiers

## Scope

This chapter records the exact documentary T32--T43 endpoint above the canonical T22--T31 final-premise frontiers.
The executable checker is:

```text
scripts/check_prime_power_final_support_handoff_frontiers.py
```

It composes the existing typed obligation registry, obligation-artifact support DAG, typed premise registry, six
handoff assertions, handoff-artifact registry, final handoff, seven-gate dossier audit, root semantic obligation and
atomic target registry. It does not prove any mathematical statement. Every result permanently reports:

```text
all_n_proved_by_checker = 0
```

## Fixed target order

The checker accepts exactly the following canonical sequence:

```text
T32_OBLIGATION_ARTIFACTS
T33_OBLIGATION_SUPPORT_DAG
T34_PREMISE_ARTIFACTS
T35_BASE_HANDOFF
T36_RECURRENCE_HANDOFF
T37_INVARIANT_HANDOFF
T38_TERMINATION_HANDOFF
T39_EXCEPTIONAL_HANDOFF
T40_TRANSLATION_HANDOFF
T41_FINAL_HANDOFF_REVIEW
T42_FINAL_DOSSIER_AUDIT
T43_ROOT_IMPLICATION
```

Every target receives one open/proved frontier record. A proved record is rejected unless the atomic execution result
is effective, every immediate atomic dependency is complete, the exact target artifact exists, and one reviewed
semantic certificate is supplied.

## CMR2630--CMR2647

### CMR2630 — Canonical T32--T43 registry

The twelve remaining atomic targets have a fixed order, fixed artifact kind, fixed immediate dependency list and one
canonical frontier URI:

```text
final-support-handoff-frontier://TARGET-ID
```

Open targets have null verification fields and no semantic certificate.

### CMR2631 — Exact immediate-target census

For every T32--T43 target, the checker reconstructs every immediate atomic dependency and publishes:

```text
dependency target result digest
dependency completion digest
effective completion flag
typed target artifact ID and record digest
target artifact-bundle digest
external proof locator and digest
```

No caller-supplied support list can omit, reorder or add a dependency.

### CMR2632 — T32 typed-obligation bank

T32 is reconstructed from the exact obligation-bearing targets below T22. Every source target is paired with its one
semantic obligation, closure record, required artifact-kind sequence, typed artifact records and obligation bundle.
The root obligation is deliberately excluded and remains T43 work.

T32 aggregates the already canonical T01--T21 frontier seals. It does not replace their obligation-artifact locators.

### CMR2633 — T33 support-DAG frontier

T33 binds the exact obligation-artifact support graph, including its edge count, roots, maximum depth, acyclicity,
dependency alignment and immediate-dependency artifact coverage. Only stable graph records are hashed; the enclosing
registry certificate SHA is not part of the T33 proof bundle.

### CMR2634 — T34 premise-artifact frontier

T34 reconstructs all ten T22--T31 premise frontiers. For each premise it binds the exact frontier record, optional
reviewed semantic certificate, optional noncircular T22--T31 proof bundle, typed premise artifact and premise-registry
bundle.

The canonical `final-premise-frontier://` premise seals remain authoritative and are aggregated rather than rewritten.

### CMR2635 — T35 base handoff

T35 binds `BASE_DOMAIN_ESTABLISHED` to the exact base-case premise frontier, its typed premise artifact, the handoff
assertion record/result and the typed handoff artifact bundle.

### CMR2636 — T36 recurrence handoff

T36 binds `NONBASE_RECURRENCE_COVERS_ALL_CASES` to the exact recurrence and selection premise frontiers, their typed
artifacts, and the corresponding reviewed handoff assertion.

### CMR2637 — T37 invariant handoff

T37 binds `STATE_AND_RESOURCE_INVARIANTS_PRESERVED` to the invariant and resource/credit premise frontiers and their
complete typed support.

### CMR2638 — T38 termination handoff

T38 binds `EVERY_RECURRENCE_BRANCH_TERMINATES` to the contraction, cross-block and termination premise frontiers and
their exact handoff artifact.

### CMR2639 — T39 exceptional handoff

T39 binds `EXCEPTIONAL_AND_HARD_CORE_CASES_CLOSED` to the exact exceptional-case premise frontier. This remains open
until all 252 T20/T21 chamber proofs and the T29 implication are genuinely proved and reviewed.

### CMR2640 — T40 translation handoff

T40 binds `QUOTIENT_CONCLUSION_TRANSLATES_TO_D_EQ_2N` to the exact objective-translation premise frontier and its typed
handoff artifact.

### CMR2641 — T41 final handoff review

T41 reconstructs all six handoff assertion results, typed assertion bundles and T35--T40 frontier bundles. Its status
must agree with the existing `final_induction_handoff_ready` gate. A proved T41 record also requires an ordinary review
statement; six effective metadata records alone are not accepted as mathematical review.

### CMR2642 — T42 dossier audit

T42 binds the exact seven-gate dossier record, exact blocker record and T41 frontier bundle. Its status must agree with
`final_dossier_integrity_ready`. The audit remains documentary and does not close the root theorem.

### CMR2643 — Stable T43 root cores

The T43 proof bundle uses stable cores of:

```text
the root semantic obligation, excluding registry locator and bundle digest;
the root closure result, excluding the obligation-record digest;
the three root obligation artifacts, excluding outward locator and digest;
the T43 atomic target artifact, excluding outward proof locator and digest.
```

These exclusions prevent the root digest from occurring inside an ancestor used to define itself.

### CMR2644 — Exact root artifact bank

A proved T43 frontier requires the exact ordered artifact kinds:

```text
all-n-implication-proof
base-case-proof
invariant-preservation-proof
```

No missing, duplicate or extra root artifact is accepted.

### CMR2645 — Dual T43 binding

The same reconstructed T43 digest must be carried by:

```text
atomic target artifact:
  proof_locator = final-support-handoff-frontier://T43_ROOT_IMPLICATION

root obligation artifacts:
  locator = final-support-handoff-frontier://T43_ROOT_IMPLICATION/ARTIFACT-ID
```

Every pointer carries the same `final_support_handoff_frontier_proof_bundle_sha256`.

### CMR2646 — Noncircular aggregate bank

The aggregate proof bank seals all dependency-support records, all external frontier-support records, all twelve
frontier records, all reviewed semantic certificates and all completed per-target proof bundles. Ancestor certificate
SHAs may appear in the final report for identity, but no per-target digest depends on an ancestor that contains that
same outward pointer.

### CMR2647 — Honesty boundary

Passing the checker proves only exact documentary ancestry, canonical support and noncircular hash binding. It does not
prove source truth, recurrence exhaustiveness, arbitrary-`n` coverage, semantic correctness, chamber closure, any final
premise, any handoff assertion, the final review, or the implication to `D(n)=2n`.

## Reviewed semantic certificate

Every proved T32--T43 target has exactly one semantic certificate containing:

```text
completion statement
support-to-completion implication statement
arbitrary-n scope statement
review boundary
evidence
```

Nonempty text is necessary documentary data, not proof. The review boundary must identify what was checked by ordinary
mathematical review rather than inferred by the checker.

## Noncircularity notes

The new layer preserves older canonical seals:

```text
T01--T21 obligation artifacts retain their exact frontier locators.
T22--T31 premise artifacts retain final-premise-frontier:// locators.
T35--T40 handoff artifacts retain handoff-artifact-registry:// locators.
```

The T32--T42 frontier digest is therefore bound only into its atomic target artifact. T43 is the sole target with a new
additional outward binding, because the root obligation artifacts previously had no exact frontier seal.

## Current mathematical work

All twelve T32--T43 frontier records are open in the current certificate stack. Closing them requires the genuine
T01--T31 mathematics first, then the six ordinary handoff arguments, the final review, the dossier audit and the root
implication. The classical no-three-in-line conjecture remains open.

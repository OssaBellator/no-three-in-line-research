# Prime-power global-family and exceptional-chamber frontiers

This chapter records CMR2598--CMR2613. It makes

```text
T19_GLOBAL_FAMILY
T20_EXCEPTIONAL_ZERO_ROWS
T21_HARD_CORE_ROWS
```

exact documentary proof surfaces over the fixed T02, T04, T05 and T18 banks.

The executable endpoints are:

```text
scripts/check_prime_power_global_family_exhaustiveness_frontier.py
scripts/check_prime_power_exceptional_chamber_frontier.py
```

Both permanently report:

```text
all_n_proved_by_checker = 0
```

## CMR2598: legacy global-family defect and corrected T19 root

The older `check_prime_power_global_family_skeleton.py` derives a manifest from a supplied recurrence
skeleton and then checks a separately assembled global integer family against that manifest. It therefore
does not establish that the exact T18 final rows are the family selected by the exact T02 applications.

The canonical T19 endpoint uses the corrected target flow

```text
T02_RULE_EXHAUSTIVENESS + T18_ROW_THEOREMS
    -> T19_GLOBAL_FAMILY
```

and removes the legacy `global-family-skeleton` special certificate support from T19. The correction is
scoped while the T19 checker runs and restores the shared modules afterwards. Concrete certificates built
under the former target definition or support rule must be regenerated.

## CMR2599: exact T02 application census

T19 derives one expected coverage unit for every exact T02 record of kind
`global-parent-application`, in canonical T02 order. Every unit binds:

```text
parent_global_state_id
source_case_id
source_clause_id
operation_slot_id
T02 application record digest
```

No parent, case, clause or selected operation is supplied independently by T19.

## CMR2600: exact T18 final-row census

T19 reads the complete T18 `final_row_subjects` bank and rejects every row whose parent is absent from the
T02 application census or whose selected slot differs from the T02 application.

The row family remains the exact T18 union:

```text
T12-eliminated recurrent final rows
+
T15 return/interface/off-diagonal final rows
```

No legacy global integer family is imported.

## CMR2601: exact T04 case/clause/slot ancestry

Every T18 row is rebound to the unique T04 parent binding for its recurrent block or interface-row unit.
The checker requires exact agreement of:

```text
source_case_id
source_clause_id
operation_slot_id
parent_global_state_id
```

with the T02 application and seals the T04 unit, parent-binding and population digests into a canonical row
ancestry record.

Thus matching only the quotient parent or slot is insufficient; a row assembled from a different source
clause is rejected.

## CMR2602: parent-to-row exhaustiveness semantics

Every T02 parent has one `open` or `proved` coverage record whose expected final-row IDs are reconstructed
from the T18 bank. A proved record requires at least one final row, a proved T02 application and proved T18
row theorems for every reconstructed alternative.

The semantic certificate separately states:

```text
application exhaustiveness
row-alternative exhaustiveness
source-clause interpretation
supporting evidence
```

The checker verifies complete finite coverage and ancestry. The ordinary claim that these alternatives
cover every genuine recurrence outcome remains external mathematics.

## CMR2603: typed per-parent support

Every proved parent requires one artifact of kind:

```text
global-family-parent-coverage-proof
```

Its exact support consists of:

1. the parent’s T02 application artifact;
2. every T04 population artifact used by the reconstructed rows; and
3. every corresponding T18 `global-row-theorem-proof` artifact.

The parent verification digest seals the coverage-record core, semantic certificate, artifact and support
bank.

## CMR2604: noncircular T19 synchronization

The aggregate T19 bank commits to the independent T02 rule proof bundle, T04 expected-unit and population
banks, the T18 row-theorem proof bank, every row ancestry record and every parent coverage proof bundle.
It excludes ancestors containing T19’s own completion digest.

When ready it synchronizes:

```text
EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE
T19_GLOBAL_FAMILY
```

through `global-family-exhaustiveness-proof` and `global-family-proof` artifacts with canonical locators
under `global-family-exhaustiveness-frontier://`.

## CMR2605: T19 honesty boundary

Passing T19 establishes exact parent and row censuses, clause ancestry, finite coverage, typed support and
registry synchronization relative to supplied certificates. It does not prove the T02 recurrence
exhaustive, the T18 row theorems true or the reconstructed alternatives complete for every mathematical
case.

## CMR2606: legacy chamber defect and corrected T20/T21 roots

The older exceptional-chamber registry binds row-based dispositions to the obsolete semantic-refinement
family and permits direct proof kinds with only an opaque locator and digest.

The canonical chamber endpoint instead uses:

```text
T05_GEOMETRY_SELECTORS
T18_ROW_THEOREMS
T19_GLOBAL_FAMILY
    -> T20_EXCEPTIONAL_ZERO_ROWS
    -> T21_HARD_CORE_ROWS
```

for both chamber targets. Research begins after T19. Legacy chamber-registry special certificate support
is removed within the scoped corrected execution context.

## CMR2607: exact 232+20 chamber census

The canonical CMR2110 worklist is reconstructed without modification and must contain exactly:

```text
232 zero-selector chambers
20 hard-core chambers
252 total chambers
```

Every record binds the exact host, selected index, selected-row digest, permutation, rank-three triples,
minimum rank and host/worklist digests. Dispositions must cover this bank in exact order.

## CMR2608: exact T05 host geometry support

Every closed chamber must cite the complete exact T05 geometry-artifact bank whose slot geometry has the
chamber’s host ID. A chamber with no exact host geometry cannot be marked closed.

This binds the chamber to the current finite geometry surface. It does not prove that the supplied T05 host
family is exhaustive for arbitrary `n`.

## CMR2609: four explicit closure modes

A closed chamber has exactly one proof kind:

```text
global-row-theorem
direct-chamber-proof
signature-infeasibility
host-union-proof
```

A `global-row-theorem` disposition must identify one exact T18 row from the same host and cite its T18
artifact plus the parent’s T19 coverage artifact.

A `host-union-proof` cites every exact T18 row theorem and every T19 parent coverage represented at that
host.

Direct and signature-infeasibility proofs cite the exact T05 host geometry but no unrelated row theorem.
Every mode still requires a closure statement, interpretation and evidence.

## CMR2610: typed chamber artifacts

Every closed zero-selector chamber requires:

```text
exceptional-zero-chamber-proof
```

Every closed hard-core chamber requires:

```text
hard-core-chamber-proof
```

The artifact seals the exact disposition digest and its T05, T18 and T19 support lists. Open chambers may
contain neither proof fields nor artifacts.

## CMR2611: separate zero and hard-core banks

T20 and T21 use separate noncircular proof banks. Each commits to:

- the exact T05, T18 and T19 proof-bank digests;
- its canonical chamber subset;
- every disposition;
- every typed chamber artifact; and
- every per-chamber verification bundle.

The fixed-response correction `17`, rollback distance `12` and uniform correction `44` remain distinct
external chamber theorems; this checker does not merge or infer them.

## CMR2612: obligation and atomic-target synchronization

Complete closure of the 232 zero-selector chambers synchronizes:

```text
EXCEPTIONAL_ZERO_ROWS_CLOSED
T20_EXCEPTIONAL_ZERO_ROWS
```

Complete closure of the 20 hard-core chambers synchronizes:

```text
HARD_CORE_ROWS_CLOSED
T21_HARD_CORE_ROWS
```

The obligation artifacts use the fixed kinds `exceptional-zero-row-proof` and `hard-core-row-proof`. The
atomic targets use `exceptional-zero-proof` and `hard-core-proof`, with exact frontier-bank digests.

## CMR2613: finite endpoint and honesty boundary

The exact executable documentary stack now reaches T21 and publishes the full 252-chamber worklist over
the exact T18/T19 family.

Passing T20/T21 would establish exact chamber census, host ancestry, selected proof mode, typed support and
registry synchronization relative to supplied evidence. It would not prove any chamber feasible,
infeasible or contracting, would not prove the global family genuinely exhaustive, and would not prove
`D(n)=2n`.

The next executable layer is T22--T31: the ten final premise contracts. Those premises must be rebuilt from
the exact T01--T21 banks rather than accepted as free summary statements.

The no-three-in-line conjecture remains open.

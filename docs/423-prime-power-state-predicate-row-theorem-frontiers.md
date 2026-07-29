# Prime-power state-predicate and final-row-theorem frontiers

This chapter records CMR2582--CMR2597. It makes

```text
T17_STATE_PREDICATES
T18_ROW_THEOREMS
```

exact documentary proof surfaces over the fixed T05, T07, T10--T16 banks.

The executable endpoints are:

```text
scripts/check_prime_power_state_predicate_frontier.py
scripts/check_prime_power_row_theorem_frontier.py
```

Both permanently report:

```text
all_n_proved_by_checker = 0
```

## CMR2582: legacy semantic-refinement defect

The older `check_prime_power_global_quotient_semantic_refinement.py` reads a separately assembled
integer-quotient family and accepts opaque predicate and row-theorem locators and digests. Consequently
its state universe, row universe and semantic ancestry can differ from the exact T13--T16 frontiers.

The fixed atomic graph also allowed T17 to close after T13 alone, although a rank-sensitive predicate
cannot be completed before its exact T16 rank theorem. The target-artifact registry separately forced
T17 and T18 to cite the obsolete refinement certificate.

The corrected proof flow is:

```text
T13_STATE_EQUIVALENCE + T16_GLOBAL_RANK -> T17_STATE_PREDICATES
T05 + T07 + T10 + T11 + T12 + T14 + T15 + T16 + T17 -> T18_ROW_THEOREMS
```

T17 research can begin after T13, but proof closure waits for T16. T17 and T18 target artifacts now use
only their exact immediate target-artifact ancestry. Concrete certificates generated under the former
target definitions or legacy certificate-support rule must be regenerated.

## CMR2583: exact T13-derived predicate census

Every exact T13 global-state record contributes one T17 predicate record in canonical T13 order. The
record binds:

```text
global_state_id
global_state_record_sha256
t13_class_artifact_id
predicate_id
status
verification_locator
verification_digest
note
```

Records are `open` or `proved`. Predicate IDs are globally unique. A proved record uses:

```text
global-state-predicate-registry://<global state ID>
```

Missing, duplicated, reordered or independently supplied states are rejected.

## CMR2584: representative-by-representative agreement

A proved predicate requires one semantic certificate whose representative bank is exactly the T13 class
member bank. Every representative record binds its block, unit, local state, local-state subject digest,
local-to-global link digest and exact T07 state-claim support, plus an agreement statement and evidence.

Thus a class predicate cannot be asserted only at the quotient label. It must state why every literal
local representative has the same intended predicate.

The checker verifies identity and complete coverage; it does not prove the representative agreement
statements mathematically true.

## CMR2585: exact rank-sensitive predicate binding

A state is rank-sensitive exactly when it occurs in the T16 critical-state rank bank. Such a predicate
must bind the exact proved T16 rank record, rank artifact and rank value. A non-rank-sensitive predicate
must have null T16 rank fields.

This prevents an arbitrary predicate from importing an unrelated rank and prevents a genuinely
rank-sensitive predicate from silently omitting its termination meaning.

## CMR2586: typed predicate proof sealing

Every proved state requires one internal artifact of kind:

```text
global-state-predicate-proof
```

Its exact support is the state's T13 class artifact and, when rank-sensitive, its T16 state-rank artifact.
The per-state verification digest seals the status-record core, semantic certificate, artifact and support
bank.

The aggregate noncircular T17 bank commits to the independent T13 and T16 proof-bank digests and every
predicate record, semantic certificate, artifact and bundle. It excludes ancestors containing T17's own
completion digest.

## CMR2587: T17 target synchronization

T17 readiness requires complete T13 and T16 readiness plus one proved predicate, semantic certificate
and artifact for every T13 global state.

The atomic target uses artifact kind `global-state-predicate-proof`, locator

```text
state-predicate-frontier://T17_STATE_PREDICATES
```

and the aggregate T17 proof-bank digest. T17 has no separate semantic obligation in the fixed obligation
DAG; its typed atomic target is the documentary closure surface.

## CMR2588: exact final-row census

T18 derives its row census before reading any row theorem. It is the canonical union of:

1. every selected recurrent row after complete T12 auxiliary elimination; and
2. every exact T15 return/interface/off-diagonal row.

Derived IDs are namespace-separated:

```text
final-row::recurrent::<T11 active row ID>
final-row::interface::<T15 interface row ID>
```

Missing, duplicated, reordered or independently supplied final rows are rejected.

## CMR2589: recurrent-row global rescaling

For each T12 eliminated recurrent row, T18 binds the exact T11 row bridge and selected slot, the T12 row
and block elimination digests, the selected response, and the T13 identities of the parent and all final
nonauxiliary targets.

The checker reconstructs the integer scale from the T11 local parent weight and the final T14/T15 global
parent weight. It scales the selected net fixed offset, row load and margin and verifies

\[
L=B+\sum_g a_g\widehat W_g,
\qquad
M=\widehat W_p-L>0.
\]

Equal global targets are aggregated before the weighted calculation. Every derived recurrent final row is
strict.

## CMR2590: exact interface-row classification

Every T15 semantic row contributes one T18 interface subject with its exact parent, operation slot, fixed
offset, target multiplicities, final weights, load and margin.

A T15 `strict` row remains `strict`. A T15 `critical-unranked` row becomes `critical-descending` only
through the exact T16 bank; T18 does not accept another rank table or support graph.

## CMR2591: exact predicate multiset reconstruction

Every proved row theorem binds the exact T17 predicate of its parent and the exact multiplicity-weighted
T17 predicate multiset of its targets. The theorem semantic certificate also records:

```text
fixed_offset
row_load
margin
classification
row_theorem_statement
fixed_offset_interpretation
external_recurrence_statement
evidence
```

This separates finite row arithmetic from the external theorem explaining what the row and fixed offset
mean in the recurrence.

## CMR2592: complete T16 critical-edge binding

For a `critical-descending` interface row, every positive target occurrence must have the corresponding
proved T16 critical-edge subject, record and artifact. The exact sorted edge-ID bank is sealed into the
row theorem.

Strict rows must cite no T16 critical edge. A critical row with a missing edge, an extra edge or only a
partial descent bank is rejected.

## CMR2593: typed row-theorem support

Every proved final row requires one internal artifact of kind:

```text
global-row-theorem-proof
```

All rows cite the aggregate T15 component-scale artifact, exact T14 component artifacts, exact parent and
target T17 predicate artifacts, and the exact T07 slot artifact.

A recurrent row additionally cites its T05 geometry artifact, T10 routed-credit artifact, T11 common
weight and closure artifacts, and T12 auxiliary artifact. An interface row cites its exact T15 row
artifact and, when critical, every exact T16 edge artifact.

The row verification digest seals the record core, semantic certificate, artifact and complete support
bank.

## CMR2594: noncircular T18 proof bank

The aggregate T18 bank commits to the independent T05, T07, T10, T11, T12, T14, T15, T16 and T17 proof
banks, the derived final-row census, every open/proved theorem record, every theorem semantic certificate,
every typed artifact and every verification bundle.

It excludes the current-frontier and target-registry certificates that contain T18's own completion digest.

## CMR2595: T18 target synchronization

T18 readiness requires all upstream exact banks ready and one proved theorem semantic and artifact for
every derived final row.

The atomic target uses artifact kind `global-row-theorem-proof`, locator

```text
row-theorem-frontier://T18_ROW_THEOREMS
```

and the aggregate T18 proof-bank digest. The corrected target-artifact registry requires only exact
immediate target-artifact ancestry and no longer cites the obsolete parallel semantic-refinement
certificate.

## CMR2596: finite endpoint

The exact executable documentary stack now reaches T18:

```text
T13 exact state quotient
T16 exact critical rank
T17 exact state predicates
T11/T12 recurrent rows + T15 interface rows
T18 exact final row theorems
```

The next executable target is T19 global-family exhaustiveness. It must derive the complete global row
family from the genuine T02 recurrence skeleton and the exact T11/T15/T18 row banks rather than accept
the older global-family package as an independent population.

## CMR2597: honesty boundary

Passing T17 and T18 establishes exact finite census, ancestry, representative coverage, rank-sensitive
binding, row arithmetic, predicate multisets, critical-edge coverage, typed support and target
synchronization relative to supplied certificates.

It does not prove that:

- any T17 predicate has its claimed mathematical meaning;
- local representatives genuinely satisfy the same predicate;
- any fixed offset has the asserted recurrence interpretation;
- the T18 row statements are mathematically true;
- the T02/T04/T11/T15 populations are genuinely exhaustive;
- the T16 rank measures genuine recurrence progress;
- the T18 row union is the complete global family;
- all 252 exceptional chambers close; or
- the quotient implies `D(n)=2n` for every `n`.

The no-three-in-line conjecture remains open.

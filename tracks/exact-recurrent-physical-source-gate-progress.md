# Exact recurrent physical-source gate progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

The classical no-three-in-line conjecture remains open. This addendum records
only the first-host physical-source inventory and ingestion gate.

## ERL1r — exact physical source coverage

Seven installed artifacts were joined for host
`s4-75b04c45c1c8eac2` and deletion trace `{02,20}`. The sixteen-field worklist
has the exact coverage census

```text
required physical fields       16
source-backed populated fields  0
unpopulated physical fields     16
physical occurrence records     0
```

Nearest evidence is normalized-only, schema-only, deletion-presence-only,
intrinsic-geometry-only, catalog-only, local-candidate-only, upper-bound-only,
or absent. No surrogate class counts as a physical field.

## ERL1s — reject-by-default physical batch gate

A complete batch must provide

```text
source-defined physical occurrence domain
exact expected occurrence count
source-backed completeness proof
one unique fully sourced record per occurrence
```

Every record must preserve the dual-edge convention and populate all sixteen
physical fields. Current result:

```text
records                               0
accepted physical records             0
expected occurrence count known       0
schema-completion candidates rejected 2
batch complete                         0
promotion allowed                      0
```

## ERL1t — chart-confinement source transfer

The response-disjoint complement of the five-response union in the standard
side-four chart is exactly

```text
{00,01,11,22,33}.
```

Thus chart confinement plus response disjointness forces every background into
the 32-state safe class. Every such background has minimizer face

```text
{2031,2310,3201}.
```

Under these predicates, neither a strict original-response reversal nor an
original-response tie is possible.

## ERL1u — chart-fixture non-promotion

The installed geometric-fibre chapters put coordinate-labelled response hosts on
the standard grid, but treat the background `B` as an independent input. The
host-census endpoint explicitly leaves actual background and provenance
attachment open.

Two verifiers sample synthetic backgrounds from

```text
grid - response
```

for conditional identity and capacity tests. These random fixtures do not prove
a physical invariant. The geometric ancestry checker and repository status keep
all-provenance background coverage at zero.

Therefore the chart transfer remains conditional; re-running those fixtures
cannot activate it.

## ERL1v — complete one-exterior original-face classification

For a two-point background with exactly one standard-chart point and one
exterior point, `3012` enters the minimizer face exactly in two infinite families
and two isolated cases.

```text
{11,(t,2-t)}, t in Z minus {0,1,2}
{22,(t,4-t)}, t in Z minus {1,2,3}
{00,(-3,-1)}
{33,(6,4)}.
```

There are no other integer cases. In every case `3012` is tied with at least one
reopening response; it is never strictly minimal.

The exact reduction audits

```text
20 response secant lines
36 safe-point/response pair lines
114 admissible integer exception candidates
18,525 bounded regression pairs.
```

Consequently:

```text
one exterior point can create an original-response tie    1
one exterior point can create a strict original reversal  0
strict two-point reversal requires two exterior points    1
```

This yields a three-level source hierarchy:

1. **chart confinement + response disjointness:** closes all complete-score
   selector obstructions;
2. **at most one exterior point:** closes strict reversals but retains the two
   infinite tie families and two isolated ties;
3. **unrestricted exterior background:** retains those ties and the four strict
   two-exterior reversals.

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_physical_source_coverage.py
data/exact_recurrent_first_host_physical_source_coverage.json

scripts/check_exact_recurrent_first_host_physical_fibre_batch_gate.py
data/exact_recurrent_first_host_physical_fibre_batch_gate.json

scripts/check_exact_recurrent_first_host_chart_confinement_transfer.py
data/exact_recurrent_first_host_chart_confinement_transfer.json

scripts/check_exact_recurrent_first_host_chart_fixture_nonpromotion.py
data/exact_recurrent_first_host_chart_fixture_nonpromotion.json

scripts/check_exact_recurrent_first_host_one_exterior_original_face.py
data/exact_recurrent_first_host_one_exterior_original_face.json

.github/workflows/exact-recurrent-first-host-physical-fibre-gate.yml
```

## Next admissible result

The next proof-relevant artifact must be one of:

1. a source-backed proof that no physical `{02,20}` occurrence exists;
2. a complete source-backed batch of all such occurrences;
3. a partial source-backed batch with a quantified remaining-record worklist;
4. a source-backed chart-confinement and response-disjointness theorem;
5. a source-backed exterior-count theorem, followed by exclusion or labelled
   retention of the exact one- or two-exterior worklist.

Only after the batch gate accepts complete physical coverage may the branch
compile exact child rows or test strict Lyapunov inequalities for this host.

Physical realization, physical exclusion, chart-confinement provenance,
recurrent rows, strict Lyapunov slack, global termination, all-side transfer,
and `all_n_proved_by_checker` remain zero.

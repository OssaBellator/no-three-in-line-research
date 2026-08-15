# First-host physical source coverage

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact source-inventory theorem. No physical occurrence is populated.

## Question

The dual-edge bridge identified sixteen fields that must be supplied before the
first residual host can be promoted into a physical recurrent row. This audit
asks whether any installed artifact already supplies those fields for
`s4-75b04c45c1c8eac2` with deletion trace `{02,20}`.

## Exact result

```text
required physical fields       16
source-backed populated fields  0
unpopulated physical fields     16
physical occurrence records     0
```

Every field remains physically unpopulated. Several have nearby evidence, but
that evidence is not occurrence-level physical data.

```text
normalized-only          5
schema-only              2
deletion-presence-only   2
intrinsic-geometry-only  1
catalog-only             1
local-candidate-only     1
upper-bound-only         1
no nearby evidence       3
```

## Field-by-field boundary

The selected provenance manifest supplies normalized owner scope, fate `B`, the
collision key `02,20`, interface `target-01`, and CRT scope `not-applied`. None
of these values identifies a physical owner or construction ancestry.

The selected-line geometry proves that response `3012` is supported on
`x-y-1=0`, but explicitly leaves physical line ownership incomplete.

The side-four kernel records local restorations of `02` and `20`; it does not
prove a legal installed transition or populate intermediate physical states.

The installed operation registry contains the global operation kind
`rank-three-zero-response-strict-dispatch`, but it does not select an operation
for this host occurrence.

The occupancy-moment artifact supplies the upper certificate `E2=69`, while its
honesty fields explicitly leave destroyed load and parent budget unpopulated.

No artifact supplies a physical embedding reference, physical source trace,
deleting causes, child row, positive weights, or a source-backed realization
status.

## Promotion rule

A normalized label, structural projection, local candidate, operation catalogue,
or upper certificate does not count as a physical field. Therefore the current
source set authorizes neither physical coverage nor promotion to a recurrent
row.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_physical_source_coverage.py \
  --check data/exact_recurrent_first_host_physical_source_coverage.json
```

The checker joins seven installed artifacts, verifies their exact first-host
facts and honesty flags, reconstructs the sixteen-field matrix, and rejects
eleven deliberate corruptions.

Physical realizability, physical exclusion, legal operations, recurrent child
rows, strict Lyapunov slack, global termination, and
`all_n_proved_by_checker` remain zero.

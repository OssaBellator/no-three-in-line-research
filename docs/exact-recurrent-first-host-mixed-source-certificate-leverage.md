# First-host mixed source-certificate leverage

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional classification of route-cover leverage from mixing source-backed state-impossibility certificates with source-backed action-family certificates. No state impossibility, uniform action-family theorem, physical edge, route, recurrent row, or Lyapunov certificate is imported.

## Certificate universe

The finite classifier uses eight conditional certificate types:

```text
state certificates
  state:00
  state:01
  state:10
  state:11

action-family certificates
  family:restore_02
  family:delete_02
  family:restore_20
  family:delete_20
```

A state certificate physically excludes every directed edge incident to that state. An action-family certificate closes both context edges of one directed action family.

These are different source claims. A missing physical-state record is not a proof that the state is impossible, and the two symbolic members of an action family do not prove one uniform occurrence-faithful family theorem.

## Complete subset census

All `2^8 = 256` certificate subsets are enumerated against the six selected-label scalar covers and fourteen menu-state scalar covers.

```text
certificate subsets                         256
subsets containing a label scalar cover     215
subsets containing a menu scalar cover      205
```

Feasible subsets by certificate count are:

```text
count       2   3   4   5   6   7  8
label      11  44  67  56  28   8  1
menu        6  40  66  56  28   8  1
```

No one-certificate shortcut exists.

## Inclusion-minimal label antichain

There are exactly thirteen inclusion-minimal label patterns:

```text
pure state pairs                 3
pure action-family pairs         4
mixed state/family pairs         4
mixed two-state/one-family       2
```

The four genuinely mixed two-certificate shortcuts are exactly

```text
state:00 + family:restore_02
state:00 + family:delete_02
state:01 + family:restore_02
state:01 + family:delete_02.
```

Each closes five directed edges and contains three of the six label covers.

The two inclusion-minimal triples are

```text
state:10 + state:11 + family:restore_20
state:10 + state:11 + family:delete_20.
```

Neither triple contains a feasible certificate pair.

## Inclusion-minimal menu antichain

There are exactly fourteen inclusion-minimal menu patterns:

```text
pure opposite-state pairs        2
pure cross-bit family pairs      4
mixed two-state/one-family       8
```

No one-state/one-family pair closes a menu scalar cover. Every one of the sixteen such pairs still requires at least one additional directed edge.

The two pure state shortcuts remain

```text
state:00 + state:11
state:01 + state:10.
```

The four pure family shortcuts remain one directed `02` family plus one directed `20` family.

The eight mixed triples are the inclusion-minimal cases in which two non-shortcut state exclusions leave one reversal pair, and one action family supplies the required direction.

## Restore-both warning

Excluding state `11` and adding any one action-family certificate closes neither a label nor a menu cover. In every such case at least one additional edge remains.

Thus a future source theorem proving the restore-both state impossible would be useful, but it would not combine with one family theorem to finish this first-host scalar closure.

## Source evidence burden

A state-impossibility certificate requires six evidence fields:

```text
physical_occurrence_domain_ref
state_definition_ref
state_impossibility_theorem_ref
domain_completeness_ref
incident_edge_exclusion_ref
realization_status
```

An action-family certificate inherits the seven evidence fields from the v2 family source-import gate:

```text
shared_theorem_ref
both_context_values_proved
shared_owner_schema_ref
shared_operation_schema_ref
shared_route_schema_ref
child_payment_compatibility_ref
realization_status
```

The inclusion-minimal evidence-slot distributions are:

```text
label patterns
  12 slots   3 patterns   two state certificates
  13 slots   4 patterns   one state plus one family
  14 slots   4 patterns   two family certificates
  19 slots   2 patterns   two states plus one family

menu patterns
  12 slots   2 patterns   two state certificates
  14 slots   4 patterns   two family certificates
  19 slots   8 patterns   two states plus one family
```

These counts compare missing source-evidence fields only. They do not replace occurrence coverage, owner persistence, legal operation traces, recurrent child rows, or final boundedness and realization checks.

## Current source state

```text
accepted state-impossibility certificates     0 of 4
accepted action-family certificates           0 of 4
complete label scalar covers                  0
complete menu scalar covers                   0
```

The state-exclusion manifest currently records no source-backed impossible state. The action-family source-import gate records zero accepted uniform family imports.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_mixed_source_certificate_leverage.py \
  --check data/exact_recurrent_first_host_mixed_source_certificate_leverage.json \
  --self-test
```

The checker reconstructs all 256 certificate subsets, the 13- and 14-pattern inclusion-minimal antichains, the four exact mixed label pairs, the absence of mixed menu pairs, source-evidence burdens, stable pattern IDs, and a registry digest. It rejects eighteen deliberate corruptions.

Physical occurrence coverage, physical transition legality, persistent owner identity, recurrent child rows, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.

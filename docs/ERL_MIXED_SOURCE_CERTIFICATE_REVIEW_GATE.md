# ERL mixed source-certificate review gate

This gate applies to any claim that first-host scalar closure follows from a mixture of state exclusions and action-family theorems.

## Required certificate semantics

A `state:xy` certificate is accepted only when all six evidence fields in `data/exact_recurrent_first_host_mixed_source_certificate_leverage.json` are populated and prove that state `xy` is impossible over the complete physical occurrence domain. Absence from the current transition manifest is not an impossibility theorem.

A `family:*` certificate is accepted only through the v2 action-family source-import gate. Both exact context edges must be proved for one occurrence-faithful owner lineage. Symbolic family structure, matching action names, or one member edge does not suffice.

## Accepted closure patterns

The proposed accepted certificates must contain one complete pattern from the exact inclusion-minimal registry:

```text
label registry: 13 patterns
menu registry:  14 patterns
```

Supersets are allowed only after every included certificate is independently source-accepted. Reviewers should reduce a proposed set to an inclusion-minimal contained pattern before counting its burden.

## Mixed-pair boundary

Exactly four state/family pairs close a selected-label cover:

```text
state:00 + family:restore_02
state:00 + family:delete_02
state:01 + family:restore_02
state:01 + family:delete_02
```

No state/family pair closes a menu cover.

Reject claims that:

- state `11` plus one family is sufficient;
- any state plus any cross-bit family is sufficient;
- five closed directed edges automatically contain a scalar cover;
- label closure implies menu closure.

## Three-certificate patterns

The two minimal label triples and eight minimal menu triples are admissible only as exact registered patterns. A three-certificate set that contains a feasible pair is not a new minimal shortcut and should be reported through that pair instead.

## Source burden

Use six missing evidence fields for each state-impossibility certificate and seven for each action-family certificate. Current accepted and populated counts are zero.

Do not count structural state labels, family IDs, edge lists, or context-bit names as physical evidence.

## Mandatory retained obligations

Even a complete certificate pattern does not by itself prove the recurrent theorem. The review must still retain:

```text
physical occurrence-domain completeness
persistent owner identity where required
legal operation traces for realized edges
recurrent child rows and payments
boundedness or terminal-route hypotheses
strict Lyapunov closure
global termination and all-side transfer
```

## Current decision

```text
accepted state certificates      0
accepted family certificates     0
complete label covers            0
complete menu covers             0
promotion allowed                0
all_n_proved_by_checker           0
```

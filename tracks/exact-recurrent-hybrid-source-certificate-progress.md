# Exact recurrent hybrid source-certificate progress

## ERL2w — full certificate antichain

**Status:** exact finite classification complete; physical source acceptance remains empty.

The first-host scalar-cover optimizer now combines:

```text
4 state-impossibility certificates
4 uniform directed action-family certificates
8 individual directed-edge route certificates
```

All `65,536` subsets are classified.

```text
                              label       menu
feasible subsets             62,564     61,679
inclusion-minimal patterns       51        100
minimum certificates              2          2
```

Minimal certificate-count distributions:

```text
label: 19 pairs, 32 triples
menu:   6 pairs, 80 triples, 14 quadruples
```

### Exact edge-route refinement

Four state-plus-edge pairs close a selected-label scalar cover:

```text
state:01 + edge:00->10
state:00 + edge:01->11
state:01 + edge:10->00
state:00 + edge:11->01
```

Four family-plus-edge pairs also close a label cover. No state-plus-edge, family-plus-edge, or state-plus-family pair closes a menu cover.

### Evidence sensitivity

```text
certificate contract                 fields
state impossibility                     6
uniform action family                    7
edge physical exclusion                  5
edge decorated outer reset               8
edge finite capacity                      9
edge terminal/improving output           10
edge bounded strict potential            11
```

Therefore:

```text
label floor with edge physical exclusion   11
label floor with any other edge route       12
menu floor for every route class            12
```

The `11`-slot floor is attained by exactly the four state-plus-edge pairs above. It is not a generic one-edge routing shortcut.

### Current source state

```text
accepted state certificates             0 of 4
accepted family certificates            0 of 4
accepted edge certificates              0 of 8
complete label covers                   0
complete menu covers                    0
```

Physical occurrence coverage, legal transitions, persistent owners, recurrent child rows, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.

## Artifacts

```text
scripts/check_exact_recurrent_first_host_hybrid_source_certificate_antichain.py
data/exact_recurrent_first_host_hybrid_source_certificate_antichain.json
docs/exact-recurrent-first-host-hybrid-source-certificate-antichain.md
docs/ERL_HYBRID_SOURCE_CERTIFICATE_REVIEW_GATE.md
```

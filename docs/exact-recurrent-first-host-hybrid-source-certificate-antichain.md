# First-host hybrid source-certificate antichain

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional classification of scalar-cover certificates assembled from source-backed state impossibility, source-backed uniform action families, and individually routed directed edges. No certificate is accepted by the current source.

## Certificate universe

The optimizer uses sixteen conditional certificate types:

```text
state impossibility
  state:00
  state:01
  state:10
  state:11

action-family theorem
  family:restore_02
  family:delete_02
  family:restore_20
  family:delete_20

individual directed-edge route
  edge:00->01
  edge:00->10
  edge:01->00
  edge:01->11
  edge:10->00
  edge:10->11
  edge:11->01
  edge:11->10
```

A state certificate closes every directed edge incident to the impossible state. A family certificate closes both context members of one directed action family. An edge certificate closes one exact directed edge only after one complete route contract is accepted.

These are distinct physical claims. A symbolic state, family, or edge name is not itself a certificate.

## Complete subset census

All `2^16 = 65,536` certificate subsets are enumerated against the six selected-label scalar covers and fourteen menu-state scalar covers.

```text
subsets containing a label scalar cover    62,564
subsets containing a menu scalar cover     61,679
```

No one-certificate shortcut exists.

## Inclusion-minimal antichains

The selected-label antichain has fifty-one patterns:

```text
certificate count 2                         19
certificate count 3                         32
```

Its certificate-class profile is:

```text
states families edges   patterns
  0       0       3        6
  0       1       1        4
  0       1       2        6
  0       2       0        4
  1       0       1        4
  1       0       2        8
  1       1       0        4
  1       1       1        8
  2       0       0        3
  2       0       1        2
  2       1       0        2
```

The menu-state antichain has one hundred patterns:

```text
certificate count 2                          6
certificate count 3                         80
certificate count 4                         14
```

Its profile is:

```text
states families edges   patterns
  0       0       4       14
  0       1       2       16
  0       2       0        4
  1       0       2       16
  1       1       1       32
  2       0       0        2
  2       0       1        8
  2       1       0        8
```

No one-state/one-edge pair, one-family/one-edge pair, or one-state/one-family pair closes a menu scalar cover.

## Exact two-certificate label shortcuts

There are four state-plus-edge label pairs:

```text
state:01 + edge:00->10
state:00 + edge:01->11
state:01 + edge:10->00
state:00 + edge:11->01
```

There are also four family-plus-edge label pairs:

```text
family:restore_02 + edge:00->01
family:delete_02  + edge:00->01
family:restore_02 + edge:01->00
family:delete_02  + edge:01->00
```

The state-plus-edge pairs close five directed selector-changing edges and contain three of the six label covers. They do not close a menu cover.

## Route-class evidence sensitivity

The installed edge-route contracts have the following per-certificate field counts:

```text
physical exclusion                 5
 decorated outer reset             8
 finite unrestorable capacity      9
 terminal or improving output     10
 bounded strict potential         11
```

The counts include the route's base physical fields and route-specific fields. They are contract-slot counts, not counts of distinct source documents. Reusing one source reference in several slots requires the corresponding theorem to satisfy every field.

A state-impossibility certificate has six evidence fields. A uniform action-family certificate has seven.

Under the cheapest edge route, physical exclusion, the four state-plus-edge pairs have nominal burden

```text
6 state fields + 5 edge fields = 11 fields.
```

This is the unique route-class improvement over the prior twelve-field two-state floor.

For every non-exclusion edge route, the cheapest label burden remains twelve fields and is attained by the three pure two-state patterns. The exact sensitivity is:

```text
edge route                         label floor   menu floor
physical exclusion                     11           12
decorated outer reset                  12           12
finite unrestorable capacity           12           12
terminal or improving output           12           12
bounded strict potential               12           12
```

Thus one individually routed edge does not generically improve source ingestion. Only an exact edge-level physical-exclusion theorem produces the eleven-slot label bound.

## Source boundary

The eleven-slot statement is conditional on both certificates being physically accepted:

1. a complete state-impossibility theorem for `state:00` or `state:01` on the source-defined occurrence domain;
2. a complete physical-exclusion route contract for the listed directed `02` edge;
3. exact compatibility with one selected-label scalar cover;
4. no promotion from label closure to menu closure;
5. no assumption that a missing state or edge record proves physical exclusion.

An edge physical-exclusion theorem need not imply that either endpoint state is globally impossible. Conversely, a state-impossibility theorem closes all incident edges and must not be replaced by one excluded transition.

## Current source state

```text
accepted state-impossibility certificates    0 of 4
accepted action-family certificates          0 of 4
accepted individual edge certificates        0 of 8
complete label scalar covers                 0
complete menu scalar covers                  0
```

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_hybrid_source_certificate_antichain.py \
  --check data/exact_recurrent_first_host_hybrid_source_certificate_antichain.json \
  --self-test
```

The checker reconstructs all 65,536 subsets, both inclusion-minimal antichains, the exact class profiles, route-class evidence sensitivity, four cheapest label pairs, stable registry digests, and eighteen mutation rejections.

Physical occurrence coverage, legal transitions, persistent owner identity, recurrent child rows, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.

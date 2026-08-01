# Packed-conflict deletion, protected contacts and recurrent-set batching are exact operations

This chapter records **CMR3384--CMR3401** and installs CMR577--CMR592 as literal construction and scheduler ancestry.

Executable checker:

```text
scripts/check_prime_power_protected_conflict_batching_ancestry.py
```

## CMR3384 — literal packed-conflict deletion pass

Every matchable side-three host is generated from its exact edge set. Every nonempty family of pairwise edge-disjoint active permutation triples is processed in a fixed order.

```text
247 matchable hosts
434 packed-conflict profiles
486 processed packed conflicts
```

## CMR3385 — matching-preserving nonessential deletion

When a packed triple contains a nonessential edge, the lexicographically first such edge is deleted and the complete perfect-matching family is regenerated.

```text
324 matching-preserving deletion steps
```

## CMR3386 — fully forced terminality

When no packed-triple edge is deletable, all three are essential. Essentiality persists through the remaining pass and the final essential core is regenerated as a matching.

```text
162 fully forced packed conflicts
maximum edge-disjoint packing size = 3
```

Every profile satisfies `3F <= t`.

## CMR3387 — private deleted-edge code

Deleted edges selected from distinct packed triples are distinct. Every killed triple is absent from the final deletion-pass host.

## CMR3388 — exact restoration payment

All 802 subsets of the private deleted-edge sets are restored. Every recreated killed conflict contains its own private restored edge.

```text
414 recreated conflict incidences
414 private restoration incidences
```

## CMR3389 — protected contact universe

All 208 nonempty protected partial matchings of `K_4,4` are generated with their canonical forbidden extension. The physical blocked-edge universe satisfies the exact `2k(n-1)` bound.

```text
2,256 physical blocked-edge incidences
```

## CMR3390 — contact support and finite histories

```text
89,040 protected-contact subsets
12,480 finite contact histories
832 recurrent contact histories
```

Every nonrecurrent history satisfies the CMR583 finite-stock bound.

## CMR3391 — protected wall extraction

Every nonempty distinct contact set is covered by the protected source and target vertices. One protected vertex meets at least the exact ceiling average.

```text
171,072 protected-wall edge incidences
```

## CMR3392 — heavy/dispersed protected-contact tokens

The selected wall is partitioned by the varying coordinate modulo two.

```text
30,574 heavy protected-contact tokens
58,466 dispersed protected-contact banks
```

Every dispersed bank attains the exact `ceil(d/(H-1))` lower bound.

## CMR3393 — recurrent unavailable-set extraction

All histories of one-, two-, three- and four-occurrence three-element inventories in a five-edge universe are exhausted for two-edge recurrent subsets.

```text
11,110 subset histories
11,070 recurrent-set histories
40 finite-subset histories
```

## CMR3394 — exact matching-cover decomposition

All unavailable witness sets of size at most four in every protected `K_4,4` state are classified by the matching number on unprotected vertices.

```text
164,944 matching-cover decomposition profiles
```

## CMR3395 — batch protected absorption

When the unprotected witness graph contains a two-edge matching, both edges are added simultaneously to the protected matching.

```text
9,680 batch-absorption profiles
19,360 absorbed-edge incidences
```

Every combined protected set remains a partial matching.

## CMR3396 — persistent small-cover wall

When the unprotected matching number is below two, a minimum König cover together with the protected vertices covers the complete witness set.

```text
155,264 persistent-wall profiles
288,048 persistent-wall edge incidences
```

Every profile satisfies the exact `ceil(r/(2k+s-1))` wall-degree bound.

## CMR3397 — aggregate reintroduction or joint persistence

All six-time availability histories of a fixed two-edge set with at least three joint-absence times are exhausted.

```text
694 joint-absence histories
486 aggregate-reintroduction endpoints
208 jointly persistent-set endpoints
```

## CMR3398 — finite batch growth

Twenty parameter pairs verify the exact bound `floor((n-k_0)/s)` for repeated batch growth.

## CMR3399 — corruption rejection

Eleven independently resealed report corruptions are rejected.

## CMR3400 — contract

```text
a48ee5aa77c167c1dba3d6eab6e3a65db7397e1739323fb794df66c32d76ec5f
```

## CMR3401 — exact consequence and honesty boundary

```text
packed_conflict_deletion_ancestry_proved = 1
protected_contact_token_ledger_exact = 1
recurrent_unavailable_set_batching_exact = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The remaining immediate operation range begins at CMR593 with selector slack, persistent-core amplification and owned-certificate accounting. No all-`n` theorem is claimed.

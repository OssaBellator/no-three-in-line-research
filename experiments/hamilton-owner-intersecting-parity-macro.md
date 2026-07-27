# Owner-intersecting parity-clean Hamilton macro audit

Run:

```bash
python scripts/check_hamilton_owner_intersecting_parity_macro.py \
  experiments/hamilton-owner-intersecting-parity-macro-audit.json
```

The diagnostic reconstructs every Hamilton pair cycle, every fixed-cycle two-owner
parity system, and every three-source successor rotation for `4<=m<=8`.  For each
parity-satisfiable cycle and each possible three-owner source set `S`, it counts
parity-satisfiable rotations whose source triple intersects `S`.

| `m` | Hamilton cycles | parity-satisfiable | minimum clean degree | source triples disjoint from `S` | degree margin | minimum clean rotations intersecting `S` |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 6 | 4 | 0 | 4 | 4 |
| 5 | 24 | 22 | 9 | 0 | 9 | 9 |
| 6 | 120 | 112 | 16 | 1 | 15 | 15 |
| 7 | 720 | 664 | 26 | 4 | 22 | 22 |
| 8 | 5,040 | 3,542 | 27 | 10 | 17 | 19 |

Thus every audited parity-satisfiable cycle has, for every owner triple `S`, a
parity-satisfiable successor rotation touching at least one owner in `S`.  Such a
rotation removes at least one orbit block of the original three-owner flaw, so
nearest parity recleaning gives an enlarged parity-clean macro deletion even when
the prescribed rotation on exactly `S` is parity inconsistent.

The satisfiable induced rotation graph remains connected through `m=8`, and every
inconsistent cycle is one rotation from the satisfiable set.

At `m=8`, parity inconsistency splits for the first time into two exact types:

```text
owner pair forbids both XOR values       480 cycles,
nonzero-XOR signed constraint cycle    1,018 cycles.
```

Every pair-local obstruction occurs exactly once in its cycle.  The signed-cycle
witnesses have shortest lengths

```text
triangle:   910,
4-cycle:    108.
```

No asymptotic nonemptiness, connectivity, owner-intersection, or seed theorem is
claimed by this finite audit.

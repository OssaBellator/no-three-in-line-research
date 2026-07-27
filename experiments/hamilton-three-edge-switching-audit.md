# Hamilton three-edge switching audit

Run:

```bash
python scripts/check_hamilton_three_edge_switchings.py \
  experiments/hamilton-three-edge-switching-audit.json
```

For each directed Hamilton cycle length `4<=ell<=8`, the checker enumerates all
`(ell-1)!` anchored cyclic orders and every unordered source triple.  It applies
the cyclic successor rotation from PP3bjg and verifies exact support, involution,
regular degree, symmetry, and graph connectivity.

The exact census is:

| cycle length `ell` | states `(ell-1)!` | degree `C(ell,3)` | directed moves |
|---:|---:|---:|---:|
| 4 | 6 | 4 | 24 |
| 5 | 24 | 10 | 240 |
| 6 | 120 | 20 | 2,400 |
| 7 | 720 | 35 | 25,200 |
| 8 | 5,040 | 56 | 282,240 |
| **total** | **5,910** |  | **310,104** |

Every move changes exactly the selected three successor assignments.  Applying
the same unordered source triple in the new cyclic order restores the original
cycle.  Each switching graph is one connected component.

For signed Hamilton covers, the three new nonloop edges have eight independent
orientation choices.  The signed degree is therefore

```text
8 C(ell,3).
```

The same graph applies to the long cycle of a one-fixed near-Hamilton cover.
This is a verified repair kernel, not a proof that repeated repairs terminate or
that their line-defect potential has negative drift.

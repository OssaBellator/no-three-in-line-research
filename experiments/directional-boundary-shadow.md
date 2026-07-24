# Directional boundary-shadow diagnostics

This experiment accompanies
[`docs/57-directional-boundary-shadow-cleaning.md`](../docs/57-directional-boundary-shadow-cleaning.md)
and
[`docs/58-fixed-core-pattern-compression.md`](../docs/58-fixed-core-pattern-compression.md).

Run

```bash
python scripts/analyze_directional_boundary_shadow.py \
  certificates/prime-patching-small.json

python scripts/analyze_fixed_core_pattern_compression.py \
  certificates/prime-patching-small.json
```

Each orientation uses one perfect-matching layer as the source pool and the
other as the fixed opposite layer.  The new interval is `{n+1,n+2}`.

## Directional cell-shadow counts

The five-entry vector is

```text
[u, movement-first, movement-second, refill-first, refill-second].
```

| Side | Pool layer | Directional counts | PP3cp lower bound | Exact feasible deletions | Blocker-free geometries | Opposite-layer clean geometries |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0 | `[0,2,1,0,1]` | `1` | `1/1` | 3 | 0 |
| 4 | 1 | `[0,0,1,0,1]` | `1` | `1/1` | 9 | 0 |
| 5 | 0 | `[0,1,2,0,0]` | `1` | `5/5` | 42 | 0 |
| 5 | 1 | `[0,2,1,2,3]` | `3/5` | `3/5` | 4 | 0 |
| 6 | 0 | `[1,0,0,0,1]` | `1/3` | `5/15` | 108 | 3 |
| 6 | 1 | `[1,1,2,2,1]` | `1/3` | `5/15` | 9 | 0 |
| 7 | 0 | `[1,2,1,0,2]` | `3/7` | `15/35` | 56 | 1 |
| 7 | 1 | `[1,2,3,3,1]` | `1/5` | `10/35` | 13 | 0 |
| 8 | 0 | `[3,2,2,1,1]` | `0` | `5/70` | 12 | 0 |
| 8 | 1 | `[2,1,2,1,3]` | `0` | `12/70` | 23 | 0 |
| 9 | 0 | `[5,0,1,2,2]` | `0` | `1/126` | 3 | 0 |
| 9 | 1 | `[3,2,3,3,2]` | `0` | `10/126` | 10 | 0 |
| 10 | 0 | `[1,3,2,4,4]` | `3/10` | `80/210` | 139 | 0 |
| 10 | 1 | `[3,1,3,2,4]` | `0` | `22/210` | 39 | 0 |

The PP3cp bound is exact in several small cases and remains a valid lower bound
when it drops to zero.  Raw secant multiplicity is not the decisive statistic:
several orientations retain many blocker-feasible deletions despite extensive
boundary shadow.

The last column checks the patch together with the opposite layer only.  The
three side-six and one side-seven states show that directional cleaning can
occasionally clear the entire fixed layer, but this is not typical.

## PP3cr distinct-pattern counts

| Side | Pool | `C` | `H` | `A` | Local full-bank density `delta` | PP3cr loss | Exact globally clean states |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0 | 4 | 0 | 3 | `5/36` | `3` | 0 |
| 4 | 1 | 2 | 2 | 7 | `5/36` | `23/6` | 0 |
| 5 | 0 | 3 | 1 | 13 | `11/180` | `4` | 0 |
| 5 | 1 | 8 | 0 | 12 | `7/90` | `28/5` | 0 |
| 6 | 0 | 3 | 3 | 14 | `1/20` | `101/30` | 0 |
| 6 | 1 | 9 | 4 | 17 | `43/540` | `89/15` | 0 |
| 7 | 0 | 7 | 2 | 25 | `29/1260` | `14/3` | 0 |
| 7 | 1 | 12 | 1 | 27 | `53/1260` | `43/7` | 0 |
| 8 | 0 | 13 | 1 | 29 | `23/630` | `305/56` | 0 |
| 8 | 1 | 12 | 2 | 25 | `83/2520` | `141/28` | 0 |
| 9 | 0 | 18 | 0 | 37 | `47/4536` | `109/18` | 0 |
| 9 | 1 | 18 | 6 | 42 | `59/4536` | `7` | 0 |
| 10 | 0 | 15 | 1 | 55 | `1/120` | `499/90` | 0 |
| 10 | 1 | 18 | 2 | 48 | `83/7560` | `89/15` | 0 |

The distinct-pattern compression is substantially smaller than counting every
anchor and secant incidence, but the stored full-layer pools still fail its
sufficient inequality.  The dominant finite obstruction has shifted from
fixed-pair cells to ordinary anchored pair patterns.  This supports the revised
strategy: use PP3cp for cell flexibility, then add geometry multiplicity or
protected trades specifically for the remaining pair patterns.
# Exact recurrent minimizer-face scalar progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

## ERL2v — complete-face state graph

The 32 safe backgrounds expose five exact minimizer-face states:

```text
A={3012}
B={3201}
C={2031,2310}
D3={2031,2310,3201}
D4={2031,2301,2310,3201}.
```

Their transition graph is `K_{2,3}` with six reversal pairs and twelve directed face-edge types.

## ERL2w — exact scalar covers

All 64 orientations are classified:

```text
acyclic face-scalar covers             46
cyclic obstructions                    18
menu-projectable covers                14
background-sensitive covers            32.
```

The fourteen projectable covers equal the existing fourteen menu covers. The thirty-two additional covers distinguish `D3` and `D4`:

```text
split changing restore-both family     12
split neutral restore-both family      12
split both families                     8.
```

## ERL2x — route boundary

Every face scalar leaves exactly four external transitions per background:

```text
3 selector-changing
1 selector-neutral
2 flipping r02
2 flipping r20.
```

Across all 32 backgrounds this is 128 external occurrence edges. Face refinement therefore adds edge-sensitive flexibility but does not lower the route count.

## ERL2y — source boundary

A face scalar avoids the unsourced lexicographic tie-break, but requires source-backed classification of every occurrence into `A,B,C,D3,D4`. Any background-sensitive cover additionally requires exact separation of the 24-case `D3` and 8-case `D4` domains.

Current source state:

```text
physical face classifications          0
physical face scalar values            0
physical face-edge routes              0
strict recurrent closure               0
all_n_proved_by_checker                 0.
```

## ERL2z — convex completion and source leverage

Every background-sensitive cover `O` has two exact menu-projectable completions:

```text
O_D3 copies the D3 directions onto D4
O_D4 copies the D4 directions onto D3.
```

Both completions are acyclic for all thirty-two sensitive covers. Their occurrence-route vectors satisfy

```text
4 R(O) = 3 R(O_D3) + R(O_D4).
```

Hence every `D3/D4`-blind linear route cost satisfies

```text
C(O) = 3/4 C(O_D3) + 1/4 C(O_D4),
min(C(O_D3),C(O_D4)) <= C(O).
```

Exact consequence:

```text
class-blind advantageous sensitive covers   0 of 32
sensitive covers with no-worse completion  32 of 32.
```

A sensitive cover can become uniquely optimal only under source-backed costs or routes that genuinely distinguish the six face-pair domains.

The minimum differential source interfaces are

```text
menu-projectable                   12 records
one-family split                   16 records
both-families split                18 records.
```

Every sensitive cover also requires an eight-field `D3/D4` classifier. Current populated classifier fields and accepted classifier records are zero.

## Artifacts

```text
scripts/check_exact_recurrent_first_host_minimizer_face_scalar_route_cover.py
data/exact_recurrent_first_host_minimizer_face_scalar_route_cover.json
docs/exact-recurrent-first-host-minimizer-face-scalar-route-cover.md
docs/ERL_MINIMIZER_FACE_SCALAR_REVIEW_GATE.md

scripts/check_exact_recurrent_first_host_minimizer_face_source_leverage.py
data/exact_recurrent_first_host_minimizer_face_source_leverage.json
docs/exact-recurrent-first-host-minimizer-face-source-leverage.md
docs/ERL_MINIMIZER_FACE_SOURCE_LEVERAGE_REVIEW_GATE.md
.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```

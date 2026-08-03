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

## Artifacts

```text
scripts/check_exact_recurrent_first_host_minimizer_face_scalar_route_cover.py
data/exact_recurrent_first_host_minimizer_face_scalar_route_cover.json
docs/exact-recurrent-first-host-minimizer-face-scalar-route-cover.md
docs/ERL_MINIMIZER_FACE_SCALAR_REVIEW_GATE.md
.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```

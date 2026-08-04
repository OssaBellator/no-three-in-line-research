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

## ERL2z — exact cost dominance

Every background-sensitive cover `S` has two canonical menu-projectable completions:

```text
C_D3 copies the D3 directions onto D4
C_D4 copies the D4 directions onto D3.
```

Both completions are acyclic for all thirty-two sensitive covers. Their paid and external occurrence vectors satisfy the componentwise identities

```text
4 S = 3 C_D3 + C_D4.
```

Therefore every `D3/D4`-blind linear route or payment cost satisfies

```text
cost(S) = 3/4 cost(C_D3) + 1/4 cost(C_D4),
min(cost(C_D3),cost(C_D4)) <= cost(S).
```

The same completion argument shows that class-blind route feasibility adds no new cover: if a sensitive cover is feasible, both ordinary completions are feasible.

Exact completion graph:

```text
ordered sensitive completion maps       32
unordered ordinary completion pairs     16
sensitive mixtures per pair               2
ordinary-cover degree distribution   10 of degree 2, 4 of degree 3.
```

Source-domain comparison:

```text
ordinary menu cover                    4 route domains
one-family sensitive split            5 route domains, 24 covers
two-family sensitive split            6 route domains,  8 covers.
```

A strict sensitive advantage requires eight source fields covering the physical occurrence domain, exact `D3/D4` partition, class completeness, split-pair cost and admissibility, a benefit theorem, and realization. Current populated fields and accepted advantage theorems are zero.

## Artifacts

```text
scripts/check_exact_recurrent_first_host_minimizer_face_scalar_route_cover.py
data/exact_recurrent_first_host_minimizer_face_scalar_route_cover.json
docs/exact-recurrent-first-host-minimizer-face-scalar-route-cover.md
docs/ERL_MINIMIZER_FACE_SCALAR_REVIEW_GATE.md

scripts/check_exact_recurrent_first_host_minimizer_face_cost_dominance.py
data/exact_recurrent_first_host_minimizer_face_cost_dominance.json
docs/exact-recurrent-first-host-minimizer-face-cost-dominance.md
docs/ERL_MINIMIZER_FACE_COST_DOMINANCE_REVIEW_GATE.md
.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```

# First-host minimizer-face scalar route covers

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional classification of strict potentials on complete minimizer faces. This avoids choosing a lexicographic response inside a tied face, but imports no physical occurrence, face classification, potential, route, or recurrent row.

## Exact face graph

Across the 32 safe backgrounds, the four restoration menus expose five distinct complete minimizer faces:

```text
A  = {3012}                         state 00, 32 backgrounds
B  = {3201}                         state 01, 32 backgrounds
C  = {2031,2310}                    state 10, 32 backgrounds
D3 = {2031,2310,3201}               state 11, 24 backgrounds
D4 = {2031,2301,2310,3201}          state 11,  8 backgrounds.
```

The six undirected face-transition types are

```text
A--B
A--C
B--D3
B--D4
C--D3
C--D4.
```

Thus the exact face graph is `K_{2,3}` with bipartition

```text
{B,C} | {A,D3,D4}.
```

It has five face vertices, six reversal pairs, and twelve directed face-edge types.

## Scalar-cover census

Every orientation of the six reversal pairs was enumerated.

```text
all pair orientations                   64
acyclic strict-scalar orientations       46
cyclic incompatible orientations         18.
```

The forty-six scalar covers split as

```text
menu-projectable                         14
background-sensitive                     32
  split changing restore-both family     12
  split neutral restore-both family      12
  split both restore-both families        8.
```

The fourteen menu-projectable covers orient `B--D3` and `B--D4` identically and orient `C--D3` and `C--D4` identically. Their projections are exactly the existing fourteen menu-state scalar covers; no additional ordinary menu cover appears.

The other thirty-two covers assign different directions to at least one restore-both face class. They therefore require a physical theorem distinguishing the 24-background face `D3` from the 8-background face `D4` on every occurrence where that orientation is used.

## Route burden

Every strict face scalar pays one direction and leaves the reverse direction external in each face pair.

For each of the 32 safe backgrounds:

```text
paid menu transitions                  4
external menu transitions              4
  selector-changing                    3
  selector-neutral                     1.
```

Over the complete safe domain:

```text
paid occurrence edges                128
external occurrence edges            128
  selector-changing                   96
  selector-neutral                    32
  flipping r02                        64
  flipping r20                        64.
```

Therefore the face refinement does not reduce the minimum route burden. It only permits the external direction on a transition incident to state `11` to depend on whether the physical face is `D3` or `D4`.

## Interpretation

A complete-face scalar has one genuine advantage: it does not require the unsourced lexicographic tie-break used by the selected-response audit.

It has a stronger source requirement instead:

```text
physical occurrence coverage
exact safe-background or equivalent face classification
proof that the physical minimizer face is A, B, C, D3, or D4
source-backed scalar value on that face
strict descent on every paid physical face transition
one accepted route for every external physical face transition.
```

Equal selected response, equal score vector, or membership in one operation-signature class does not determine the physical face.

Current source census:

```text
physical face classifications populated   0
physical face scalar values populated     0
physical face-edge routes populated       0.
```

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_minimizer_face_scalar_route_cover.py \
  --check data/exact_recurrent_first_host_minimizer_face_scalar_route_cover.json
```

The checker reconstructs the exact `K_{2,3}` graph, enumerates all 64 orientations, validates the 46/18 acyclic/cyclic split, proves that exactly fourteen covers project to the existing menu covers, records stable cover IDs and a registry digest, and rejects eighteen deliberate corruptions.

Physical occurrence coverage, legal operations, persistent owner identity, recurrent child rows, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.

# First-host minimizer-face source leverage

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional comparison between the fourteen menu-projectable face covers and the thirty-two background-sensitive face covers. No physical occurrence, face classifier, scalar value, transition, route, child row, or Lyapunov certificate is imported.

## Completion theorem

Let `O` be one of the thirty-two background-sensitive acyclic orientations of the exact face graph

```text
K_{2,3},  bipartition {B,C} | {A,D3,D4}.
```

Construct two menu-projectable orientations:

```text
O_D3: copy the directions incident to D3 onto D4;
O_D4: copy the directions incident to D4 onto D3.
```

For every background-sensitive `O`, both completions are acyclic and occur among the fourteen registered menu-projectable covers.

The restore-both face census is

```text
D3 backgrounds  24
D4 backgrounds   8.
```

Therefore the directed menu-edge occurrence vector satisfies the exact identity

```text
4 R(O) = 3 R(O_D3) + R(O_D4).
```

Equivalently, for every linear per-occurrence external-route cost `C` that depends on the directed menu-state edge but does not distinguish `D3` from `D4`,

```text
C(O) = 3/4 C(O_D3) + 1/4 C(O_D4).
```

Hence

```text
min(C(O_D3), C(O_D4)) <= C(O).
```

No background-sensitive cover can be strictly cheaper than every menu-projectable cover under a `D3/D4`-blind route cost.

Exact census:

```text
background-sensitive covers                    32
D3 completions acyclic and projectable          32
D4 completions acyclic and projectable          32
exact 3/4--1/4 decompositions                   32
class-blind strictly advantageous covers         0.
```

## When sensitivity can matter

If source-backed costs or route classes are allowed to distinguish all six exact face-pair domains, then every one of the thirty-two background-sensitive covers can be made uniquely optimal by a nonnegative cost assignment: give cost zero to its six external directions and positive cost to every reverse direction.

This construction is only a conditional optimization statement. It does not provide the required physical distinction between the two restore-both faces. A background-sensitive cover is admissible only after source evidence proves that the physical occurrence belongs to `D3` or `D4` and that the relevant route or descent data genuinely differ by that class.

## Differential source interface

The comparison counts only records that differ between the three scalar modes. Occurrence-domain, owner, legality, boundedness, and realization contracts remain mandatory for every mode and are not counted here.

A `D3` and `D4` transition may share one descent or route record only when the directions agree and a source theorem is uniform over both face classes.

```text
mode                         scalar  descent  routes  classifier  total
menu-projectable                4       4       4         0       12
one restore-both family split   5       5       5         1       16
both families split             5       6       6         1       18
```

Cover census by interface:

```text
12-unit menu-projectable covers   14
16-unit one-family splits         24
18-unit two-family splits          8.
```

Thus every background-sensitive cover has a strictly larger differential source interface. Under class-blind costs it also has no route-cost advantage.

## Exact `D3/D4` classifier contract

A background-sensitive cover requires one accepted classifier record with eight fields:

```text
physical_occurrence_domain_ref
restore_both_state_domain_ref
safe_background_or_equivalent_signature_ref
D3_characterization_ref
D4_characterization_ref
disjointness_ref
completeness_ref
realization_status
```

Current state:

```text
populated classifier fields       0 of 8
accepted classifier records       0
physical directed edges           0
source face scalar values          0
source face-edge routes            0.
```

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_minimizer_face_source_leverage.py \
  --check data/exact_recurrent_first_host_minimizer_face_source_leverage.json \
  --mutation-audit
```

The checker joins the canonical face-cover registry, closure-route source gate, and transition-domain source audit; reconstructs all forty-six face covers; proves all thirty-two completion identities; pins the completion registry by stable IDs and digest; and rejects eighteen deliberate corruptions.

Physical occurrence coverage, minimizer-face classification, transition legality, persistent owner identity, recurrent child rows, strict Lyapunov closure, global termination, and `all_n_proved_by_checker` remain zero.

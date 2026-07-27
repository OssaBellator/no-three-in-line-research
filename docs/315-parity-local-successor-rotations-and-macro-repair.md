# Parity-local successor rotations and a parity-clean macro repair

The two-owner parity CSP from `docs/312` gives an exact preprocessing step for a
fixed Hamilton pair cycle. A three-edge successor rotation changes that cycle,
so the parity system must be updated. This chapter proves that the update is
local at the constraint level and gives a polynomial macro repair that returns
to the parity-clean state space whenever the rotated cycle has a satisfiable
parity system.

The finite rotation graph through `m=7` is especially favorable: the
parity-satisfiable Hamilton cycles form one connected induced component, every
inconsistent cycle is one rotation away from it, and every satisfiable cycle has
many satisfiable rotation neighbors.

No asymptotic connectivity or termination theorem is claimed.

## 1. One rotation changes only incident parity constraints

Fix a Hamilton pair cycle `rho` and its two-owner constraint system from
PP3bkw. Apply one successor rotation on a source triple `S`, producing `rho'`.

### Proposition PP3blh -- PROVED / LOCAL UPDATE

For every owner pair `{i,k}` disjoint from `S`, its forbidden-XOR set is identical
for `rho` and `rho'`. Consequently at most

```text
C(m,2)-C(m-3,2)=3m-6
```

owner-pair constraints can change.

#### Proof

The geometric predicate for owner pair `{i,k}` depends only on the two signed
pair edges

```text
i -> rho(i),
k -> rho(k).
```

A successor rotation changes `rho` only at its three selected sources. If both
`i` and `k` lie outside `S`, both directed pair edges and all four orientation
cases are unchanged, so the forbidden-XOR set is unchanged. The number of
unordered owner pairs meeting a fixed three-set is `3m-6`. ∎

Thus the parity instance can be updated by recomputing only a linear number of
pair predicates, rather than rebuilding all `C(m,2)` predicates.

## 2. Nearest parity-clean orientation

### Proposition PP3bli -- PROVED

Let a satisfiable signed parity graph on `m` orientation variables have connected
components `C_1,...,C_c`. For any reference orientation vector `e`, a satisfying
orientation vector of minimum Hamming distance from `e` can be found in linear
time. Its distance is at most

```text
sum_j floor(|C_j|/2) <= floor(m/2).
```

#### Proof

Parity propagation determines one satisfying vector on each component after one
root bit is chosen. Complementing every bit in that component gives the only
other satisfying vector. If the two distances from the reference vector are
`d_j` and `|C_j|-d_j`, choose the smaller. Summing the componentwise minima gives
the displayed bound. Propagation and the distance comparison are linear in the
signed graph size. ∎

Isolated variables are components of size one and can be matched to the
reference vector exactly.

## 3. A parity-clean macro repair

### Theorem PP3blj -- PROVED / CONDITIONAL MACRO REPAIR

Let `(rho,e)` be a parity-clean signed Hamilton state, and let a present
three-owner flaw have source set `S`. Rotate the three successors, obtaining
`rho'`. Suppose the two-owner parity CSP of `rho'` is satisfiable. Choose a
nearest satisfying orientation vector `e'` as in PP3bli.

Then the macro transition

```text
(rho,e) -> (rho',e')
```

has all of the following properties:

1. it deletes the targeted three-owner flaw;
2. it preserves Hamiltonicity, matching, pair-2-cycle-freeness, and
   duplicate-orbit validity;
3. its output has no two-owner flaw;
4. its signed assignment support is at most
   ```text
   3 + floor(m/2).
   ```

#### Proof

The successor rotation changes all three old source-to-target assignments, so
all three old orbit blocks supporting the targeted flaw disappear, independently
of the new orientation choices. The rotated pair permutation is Hamilton by
PP3bjg and therefore has no pair 2-cycle. Matching and duplicate-orbit validity
follow as before.

The chosen vector `e'` satisfies the complete parity CSP of `rho'`, so PP3bkw
excludes every two-owner flaw. Only the three rotated sources change targets,
and PP3bli changes at most `floor(m/2)` orientation bits; the union of these
supports has the stated upper bound. ∎

The macro action may create other three-owner flaws. Its purpose is to keep the
process inside the parity-clean manifold, not to establish monotone descent.

## 4. Exact parity-satisfiable rotation graphs

### Proposition PP3blk -- VERIFIED FINITELY

For every `4<=m<=7`, construct the graph of Hamilton pair cycles under
three-source successor rotations and retain only cycles whose two-owner parity
CSP is satisfiable. The induced graph is connected in every case.

| `m` | all cycles | satisfiable | inconsistent | induced components | minimum satisfiable neighbors | maximum distance to satisfiable |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 6 | 0 | 1 | 4 | 0 |
| 5 | 24 | 22 | 2 | 1 | 9 | 1 |
| 6 | 120 | 112 | 8 | 1 | 16 | 1 |
| 7 | 720 | 664 | 56 | 1 | 26 | 1 |

Every inconsistent cycle in the audited range has a satisfiable successor-
rotation neighbor. The exact directed transition counts at `m=7` are

```text
satisfiable -> satisfiable     21,616,
satisfiable -> inconsistent     1,624,
inconsistent -> satisfiable     1,624,
inconsistent -> inconsistent      336.
```

Parity satisfiability is therefore not preserved by every rotation, but no
audited satisfiable cycle is trapped away from the satisfiable induced graph.

#### Verification

Run

```bash
python scripts/check_hamilton_parity_rotation_graph.py \
  experiments/hamilton-parity-rotation-graph-audit.json
```

The checker reconstructs each exact parity system from orbit geometry, applies
every source triple rotation, verifies PP3blh constraint by constraint, and
computes the induced connected components and distances. ∎

## 5. Finite update-width census

### Proposition PP3bll -- VERIFIED FINITELY

Across all successor rotations through `m=7`, no changed parity constraint is
disjoint from the three rotated sources. The maximum observed numbers of changed
constraints are

```text
m=4: 1,
m=5: 5,
m=6: 7,
m=7: 9,
```

all below the deterministic bound `3m-6`.

At `m=7`, the full changed-constraint distribution over `25,200` directed
rotations is

| changed constraints | rotations |
|---:|---:|
| 0 | 1,880 |
| 1 | 5,592 |
| 2 | 7,314 |
| 3 | 5,344 |
| 4 | 3,046 |
| 5 | 1,366 |
| 6 | 486 |
| 7 | 142 |
| 8 | 22 |
| 9 | 8 |

∎

## 6. Update and recleaning complexity

### Corollary PP3blm -- PROVED

Given the old parity constraint dictionary and the orbit geometry for the
`3m-6` owner pairs incident to `S`, the conditional macro repair can be decided
and constructed in polynomial time:

1. recompute only those incident forbidden-XOR predicates, by PP3blh;
2. test parity consistency by graph propagation;
3. if consistent, construct a nearest satisfying orientation by PP3bli.

With constant-time access to each geometric pair predicate, the constraint
update uses `O(m)` predicate evaluations and the consistency/recleaning stage is
linear in the updated signed graph.

#### Proof

PP3blh localizes every changed predicate to an owner pair meeting `S`. Standard
signed-graph parity propagation simultaneously tests consistency and constructs
one solution on each component. PP3bli chooses the nearer component
orientation. ∎

## 7. Revised parity-clean frontier

### Corollary PP3bln -- PROVED / FRONTIER SHARPENED

The two-owner subsystem can now be integrated with dynamic three-owner repair as
follows:

1. restrict to Hamilton cycles with satisfiable parity systems;
2. maintain a parity-clean orientation vector;
3. target a three-owner flaw using a successor rotation whose new cycle remains
   parity satisfiable;
4. update only the incident parity predicates and choose a nearest clean
   orientation.

This gives a polynomially computable parity-clean macro action. Through `m=7`,
the satisfiable induced graph is connected and every inconsistent cycle is one
rotation away from it. However, a present three-owner flaw fixes its source
triple, so the finite degree bounds do not imply that this particular rotation
is parity satisfiable.

The remaining asymptotic gaps are precise:

- prove that sufficiently large `m` admit a nonempty, suitably connected
  parity-satisfiable rotation subgraph;
- show that every relevant three-owner flaw has an admissible parity-satisfiable
  rotation, or enlarge the macro move;
- control the three-owner collateral flaws and action charges after the global
  orientation recleaning step.

The finite connectivity through `m=7` does not imply these uniform statements.
The asymptotic seed theorem remains open.

# Parity-satisfiable Hamilton cycles under successor rotations

`docs/312` turns all two-owner flaws of a fixed Hamilton cycle into a signed
parity graph.  Dynamic repair changes the Hamilton cycle, so the next question
is whether that parity system can be updated locally and whether parity-clean
cycles remain connected under successor rotations.

This chapter proves the local update rule and records the complete finite
rotation graph through `m=7`.  The satisfiable induced graph is connected in
that range, and every inconsistent cycle is one rotation from it.  No uniform
asymptotic connectivity theorem is claimed.

## 1. Only incident parity constraints can change

Let `rho'` be obtained from a Hamilton cycle `rho` by rotating the successors of
three sources `S={a,b,c}`.  The pair edge `i->rho(i)` is unchanged for every
`i` outside `S`.

### Proposition PP3blh -- PROVED / LOCAL PARITY UPDATE

If an owner pair `{i,k}` is disjoint from `S`, then its two-owner forbidden-XOR
set is identical before and after the successor rotation.  Consequently every
changed edge or label in the signed parity graph is incident to at least one
source in `S`.

#### Proof

The owner-pair predicate from PP3bkw depends only on the two signed orbit blocks
attached to

```text
i -> rho(i),
k -> rho(k).
```

When `i,k` are outside `S`, both directed pair assignments are exactly unchanged
by the successor rotation.  Their four orientation combinations therefore
select the same orbit-block unions and have the same collinearity predicates.
Hence the forbidden XOR set is unchanged. ∎

### Corollary PP3bli -- PROVED

One successor rotation changes at most

```text
3(m-3)+C(3,2)=3m-6
```

owner-pair parity predicates.  Given the new geometric predicates on those
pairs, parity consistency can be updated by modifying only edges incident to
the three rotated sources.

#### Proof

There are `3(m-3)` pairs with one endpoint in `S` and one outside, plus the
three pairs internal to `S`.  PP3blh excludes every other pair. ∎

This makes parity preprocessing compatible with local cycle repair at the
constraint-update level; it does not say that every rotation preserves
satisfiability.

## 2. Exact finite rotation graph

### Proposition PP3blj -- VERIFIED FINITELY

For every Hamilton cycle with `4<=m<=7`, every three-source successor rotation
was applied and the exact parity systems before and after were compared.  All
changed constraints touch a rotated source.

The maximum observed changed-constraint counts are

```text
m=4: 1,
m=5: 5,
m=6: 7,
m=7: 9,
```

below the deterministic bound `3m-6`.

#### Verification

Run

```bash
python scripts/check_hamilton_parity_rotation_graph.py \
  experiments/hamilton-parity-rotation-graph-audit.json
```

The checker reconstructs every parity CSP directly from the two-orbit geometry,
applies every successor rotation, and compares the complete labelled constraint
dictionaries. ∎

## 3. The satisfiable induced subgraph through `m=7`

### Theorem PP3blk -- VERIFIED FINITELY / FRONTIER REFINED

In the complete audited range `4<=m<=7`:

1. the subgraph induced by parity-satisfiable Hamilton cycles is connected;
2. every inconsistent Hamilton cycle has rotation distance one from a
   satisfiable cycle;
3. every satisfiable cycle has at least the following number of satisfiable
   rotation neighbours:

```text
m=4: 4,
m=5: 9,
m=6: 16,
m=7: 26.
```

The exact cycle counts are:

| `m` | all cycles | satisfiable | inconsistent | satisfiable components | maximum distance to satisfiable |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 6 | 0 | 1 | 0 |
| 5 | 24 | 22 | 2 | 1 | 1 |
| 6 | 120 | 112 | 8 | 1 | 1 |
| 7 | 720 | 664 | 56 | 1 | 1 |

At `m=7`, the `25,200` directed rotations split as

```text
satisfiable -> satisfiable     21,616,
satisfiable -> inconsistent     1,624,
inconsistent -> satisfiable     1,624,
inconsistent -> inconsistent      336.
```

#### Verification

The diagnostic builds the unsigned Hamilton rotation graph, labels every vertex
by parity satisfiability, computes induced connected components and reverse
distance from the satisfiable set, and records every transition type. ∎

Parity satisfiability is therefore not invariant under arbitrary successor
rotation, but the finite satisfiable region has substantial internal mobility.

## 4. Revised parity-preserving repair frontier

### Corollary PP3bll -- PROVED / FINITE EVIDENCE RECORDED

A repair architecture may maintain two-owner cleanliness by alternating:

1. local successor rotations whose parity changes are confined to three source
   stars by PP3blh; and
2. linear-time parity propagation after each local update.

Through `m=7`, one can also restrict cycle motion to the connected
parity-satisfiable induced graph without losing access to any audited
satisfiable Hamilton cycle.

The unresolved asymptotic tasks are:

1. prove that parity-satisfiable Hamilton cycles exist for all sufficiently
   large `m` or for the prime-derived subsequence of interest;
2. prove connectivity, expansion, or at least large components of their induced
   rotation graph;
3. combine parity-preserving rotations with the residual three-owner causal
   scale `O(log n/n)` from PP3bkt;
4. control the orientation solution chosen after each local parity update so
   that three-owner collateral defects do not accumulate.

The finite connectivity and distance-one results do not establish any of these
uniform statements.  The asymptotic seed theorem remains open.

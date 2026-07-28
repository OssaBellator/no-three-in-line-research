# Exact `m=10` pair-safe frustration repair and clean mobility

`docs/327` verifies one-step frustration descent through `m=9`.  Pair size ten
is the first audited size with parity-satisfiable constraint graphs of positive
cyclomatic rank, so it is the first test of whether consistent signed cycles
break the clean-cycle mobility pattern.

This chapter reconstructs all Hamilton cycles and successor rotations at
`m=10`.  No asymptotic clean-mobility or seed theorem is claimed.

## 1. Complete frustration census at `m=10`

### Theorem PP3bnq -- VERIFIED FINITELY / FIRST NONFOREST SIZE

Among all

```text
9! = 362,880
```

directed Hamilton cycles on ten pair vertices, exactly `342,720` are pair-safe
and exactly `297,886` have satisfiable parity systems.  The exact frustration
index distribution on the pair-safe cycles is

| `lambda` | cycles |
|---:|---:|
| 0 | 297,886 |
| 1 | 42,190 |
| 2 | 2,582 |
| 3 | 62 |

The clean cycles support exactly `115,586,396` clean orientation vectors.  Their
constraint-graph cyclomatic-rank distribution is

```text
rank 0: 296,298 cycles,
rank 1:   1,588 cycles.
```

No clean graph of larger rank occurs.

#### Verification

The checker reconstructs every geometric owner-pair predicate, discards the
20,160 cycles containing a locally impossible pair, minimizes the number of
violated parity constraints over all `2^10` orientation vectors, and computes
the component and cyclomatic-rank data on every clean graph.  All values are
compared with the stored exact ledger. ∎

Thus the first consistent signed cycles do not create a new frustration level:
the maximum remains three, as at `m=9`.

## 2. Every pair-safe inconsistent cycle is one rotation from clean

### Theorem PP3bnr -- VERIFIED FINITELY / DIRECT CLEAN REPAIR

Every pair-safe `m=10` Hamilton cycle with positive frustration index has a
pair-safe successor rotation whose target parity system is satisfiable.  The
exact source-to-best-target counts are

```text
lambda 1 -> 0 : 42,190 cycles,
lambda 2 -> 0 :  2,582 cycles,
lambda 3 -> 0 :     62 cycles.
```

Consequently the pair-safe distance distribution to the clean set is

```text
0:297,886,
1: 44,834,
```

and no pair-safe cycle is unreachable.

#### Proof

For every pair-safe source cycle, enumerate all `C(10,3)=120` successor
rotations and retain pair-safe targets.  Exact lookup of the precomputed target
frustration index shows that every positive source has a target of index zero.
The displayed counts partition all 44,834 positive-frustration sources. ∎

This strengthens one-step strict descent at `m=10` to one-step arrival at the
clean manifold.

## 3. Clean connectivity and owner-intersecting mobility

### Theorem PP3bns -- VERIFIED FINITELY / CLEAN GRAPH CONNECTED

The induced successor-rotation graph on the 297,886 clean `m=10` Hamilton
cycles is connected.  Its degree range is

```text
minimum clean degree:  69,
maximum clean degree: 120.
```

Moreover, for every clean cycle and every three-owner set `S`, at least

```text
40
```

clean successor rotations use a source triple intersecting `S`.

#### Verification

For every clean cycle, the checker constructs the 120-bit mask of rotations
whose target cycle is clean.  A graph traversal visits all 297,886 clean cycles.
Intersecting each clean mask with the precomputed source-triple masks meeting
all 120 possible owner triples gives the exact minimum 40. ∎

Therefore the owner-intersecting macro targetability of PP3blr and PP3bmg
extends through `m=10`, despite the appearance of rank-one clean parity graphs.

## 4. Every optimal violated edge can be hit by a direct clean rotation

### Theorem PP3bnt -- VERIFIED FINITELY / MARKED CORE TARGETABILITY

For every pair-safe `m=10` cycle `rho`, every orientation attaining
`lambda(rho)>0`, and every parity edge violated by that orientation, there is a
successor rotation satisfying all three properties:

1. its target cycle is parity satisfiable;
2. its source triple meets an endpoint of the selected violated edge;
3. it therefore replaces at least one directed assignment supporting that edge.

The complete audit contains

```text
13,185,264
```

optimal violated-edge instances.  None is untargetable.  The minimum number of
direct clean rotations meeting one selected violated edge is six, and every
positive-frustration cycle has at least 11 direct clean rotations before an edge
is specified.

#### Verification

For every pair-safe positive-frustration cycle, the checker enumerates all
minimum orientations, records every violated parity edge, constructs the mask
of rotations whose target cycle is clean, and intersects that mask with the
source triples meeting either endpoint of the selected edge.  The exact minimum
and total-check counts are compared with the stored ledger. ∎

This extends the marked-core targeting theorem PP3bnj from `m<=9` to the first
nonforest size.

## 5. Finite preprocessing and macro interface through `m=10`

### Corollary PP3bnu -- VERIFIED FINITELY / FRONTIER EXTENDED

At `m=10`, any pair-safe Hamilton cycle can be brought to the parity-clean
manifold by at most one successor rotation and global parity reoptimization.
Every edge in every minimum frustration core can be selected in advance and hit
by such a direct clean rotation.  Once clean, the cycle lies in the unique clean
rotation component and every three-owner set has at least 40 clean intersecting
rotations.

#### Proof

If the source is clean there is nothing to do.  Otherwise PP3bnr supplies a
direct clean rotation, while PP3bnt permits any selected optimal violated edge
to be hit.  PP3bns supplies connected clean mobility and the owner-intersection
bound. ∎

The reoptimization is cycle-level and may change many orientation bits.  The
result does not yet control atomic three-owner collateral, weighted predecessor
charge, or the distance to a line-valid signed state.

## 6. Revised asymptotic frontier

The favorable finite pattern now survives the first nonforest parity fibres:

```text
m<=10 pair-safe inconsistent cycle -> clean cycle in one rotation,
m<=10 every optimal violated edge is targetable by a descending rotation,
m<=10 clean induced rotation graph connected,
m=10 every owner triple has at least 40 clean intersecting rotations.
```

The next targets are:

1. prove an asymptotic one-rotation or bounded-rotation clean-repair theorem for
   the logarithmic frustration core from `docs/326`;
2. prove polynomially many clean rotations meet every marked violated edge;
3. couple cycle-level clean repair to exact fibre regeneration while controlling
   merged charge;
4. extend the optimized cycle audit to `m=11` by avoiding exhaustive orientation
   enumeration where possible;
5. determine whether higher clean cyclomatic ranks eventually obstruct
   connectivity or owner-intersecting degree.

The exact `m=10` result is finite evidence, not an asymptotic construction.

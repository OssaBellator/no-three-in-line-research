# Exact compressed `m=10` flaw-source census and min-cut envelope

`docs/342` proves that a three-owner atomic flaw is supported on at most
`(m-4)!` Hamilton cycles and uses that compression to complete weighted-Hall
transport through `m=9`.  This chapter carries the source-side compression to
`m=10` and measures the exact family of Hall instances before running the full
min-cut stage.

No complete `m=10` weighted-Hall census or asymptotic expansion theorem is
claimed.

## 1. Exact supported-flaw census

As in `docs/342`, an atomic signed-assignment flaw prescribes three source
owners, three distinct successor targets, and three owner signs.  Global sign
complementation permits one representative of each complementary sign pair.
For every representative, contract the three prescribed Hamilton arcs and
retain the parity-satisfiable source cycles compatible with the prescribed
signs.

### Theorem PP3brs -- VERIFIED FINITELY / COMPLETE `m=10` COMPRESSED SOURCE CENSUS

At `m=10` there are

```text
362,880 Hamilton cycles,
297,886 parity-satisfiable cycles,
115,586,396 parity-clean signed states.
```

The exact compressed flaw ledger is

```text
nonempty three-arc assignment keys:                 60,480,
complement-reduced geometric flaw candidates:       24,762,
signed atomic flaws with at least one clean source: 47,512.
```

Thus 1,006 complement representatives, or 2,012 signed geometric flaws, have no
parity-clean source and disappear before any Hall graph is built.

For the 47,512 supported signed flaws, the number of compatible source cycles
lies in

```text
106 to 720.
```

The exact source-count quantiles are

```text
25 percent: 545,
median:     612,
75 percent: 658,
90 percent: 687,
99 percent: 718.
```

Exactly 412 signed flaws attain all `6!=720` possible source cycles.  Summed over
all flaws, there are

```text
27,939,188 flaw--source-cycle incidences,
1,485,249,312 units of exact signed source weight.
```

The largest source weight of one flaw is 65,256 and is attained by a flaw with
all 720 source cycles.

#### Verification

The checker reconstructs the complete pair geometry, all Hamilton cycles, and
every affine clean fibre.  It stores source cycles by their three prescribed
arcs, enumerates complement-reduced three-owner geometric flaws, imposes the
three prescribed root values in every source fibre, and accumulates exact fibre
weights.  Every displayed count and quantile is hard-coded as a regression
value. ∎

The lower endpoint 106 is notable: the `m=10` transport frontier has no
supported flaw whose source universe is a constant-size exceptional set.  Any
proper Hall bottleneck must occur inside an already substantial source family.

## 2. Per-flaw min-cut envelope

Let `S` be the three source owners of a flaw.  A clean transport rotation is
allowed only when its owner triple `T` meets `S`.  Hence the number of possible
rotation labels from one source cycle is at most

```text
binom(m,3)-binom(m-3,3).
```

### Proposition PP3brt -- PROVED / VERIFIED FINITELY / BOUNDED `m=10` HALL INSTANCES

Every supported `m=10` flaw transport instance has at most

```text
720 source-cycle vertices,
85 owner-intersecting rotation labels per source,
61,200 raw source--rotation incidences
```

before duplicate target cycles are merged.

#### Proof

The three prescribed arcs contract to `m-3=7` directed path blocks, so
`docs/342` gives at most `(10-4)!=720` containing Hamilton cycles.  Of the
`binom(10,3)=120` owner triples, exactly `binom(7,3)=35` avoid all three flaw
owners.  Therefore 85 triples meet the flaw, and multiplying by the source bound
gives 61,200 raw incidences.  Target deduplication can only reduce this number.
∎

Together with PP3brs, the complete `m=10` audit is reduced to exactly 47,512
weighted maximum-closure problems, each with at most 720 source vertices and the
stated raw edge envelope.  This is a finite and explicit computational target;
it is not yet the completed Hall census.

Compile and run the exact source audit with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_compressed_flaw_source_census.cpp \
  -o /tmp/check_m10_compressed_flaw_source_census

OMP_NUM_THREADS=12 \
  /tmp/check_m10_compressed_flaw_source_census
```

The remaining implementation problem is to reuse target-position storage and
min-cut workspaces across these dense but uniformly bounded instances.  The
remaining mathematical problem is still all-scale weighted expansion: the
`m=9` maximizer shows that controlling only tiny or complete source sets is not
enough.

The next theorem identifier after this chapter is `PP3bru`.

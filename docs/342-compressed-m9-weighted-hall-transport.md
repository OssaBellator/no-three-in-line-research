# Compressed exact weighted-Hall transport through `m=9`

`docs/337` replaces exponential Hall-subset enumeration by exact maximum-closure
min-cuts and completes the `m=8` audit.  The apparent obstacle at `m=9` is the
`6,727,728` parity-clean signed states.  This chapter removes that obstacle by
generating the source cycles of one flaw directly from its three prescribed
Hamilton arcs.

No asymptotic expansion or no-three-in-line theorem is claimed.

## 1. Three prescribed arcs have factorially compressed support

An atomic signed-assignment flaw prescribes three distinct source owners, three
distinct target owners, and three signs.  Ignore the signs temporarily and view
the assignments as directed arcs.

### Proposition PP3bpn -- PROVED / THREE-ARC CONTRACTION COUNT

Let `m>=4`.  Three prescribed directed arcs with distinct tails and distinct
heads are contained in a directed Hamilton cycle only if they form a directed
path forest, with no proper directed cycle.  When they do, the number of directed
Hamilton cycles containing all three arcs is exactly

```text
(m-4)!.
```

#### Proof

Distinct tails and heads give indegree and outdegree at most one in the
prescribed subgraph.  A proper directed cycle cannot be extended to one
Hamilton cycle, so every extendible component is a directed path or isolated
vertex.

Contract each prescribed arc.  Three contractions leave `m-3` directed path
blocks.  A Hamilton cycle containing the arcs is uniquely a cyclic ordering of
these blocks, with the internal direction of every path fixed.  The number of
cyclic orders of `m-3` labelled blocks is

```text
(m-4)!.
```

Expanding the contracted paths is inverse to contraction. ∎

Hence one `m=9` flaw has at most `5!=120` source cycles, despite the millions of
clean signed states.

## 2. Global sign complementation halves the signed audit

### Proposition PP3bpo -- PROVED / COMPLEMENT-PAIR REDUCTION

Complementing every owner sign preserves:

1. whether a prescribed three-owner assignment contains a collinear triple;
2. compatibility with every parity-clean source cycle;
3. every source fibre weight;
4. the complete source-cycle/target-cycle transport graph;
5. the optimal weighted Hall charge.

#### Proof

For one owner assignment, changing its sign reflects its four orbit cells in the
horizontal midline:

```text
(x,y) -> (x,Jy).
```

Complementing all signs applies this reflection to the complete point set, so it
preserves collinearity.  Every parity constraint depends only on XORs of owner
signs, hence global complementation preserves compatibility and component-root
multiplicities.  Cycle rotations and target fibre sizes do not depend on the
sign mask.  Therefore the weighted transport instance is identical. ∎

The executable audit processes one representative of each complement pair and
counts both members.

## 3. Compressed exact algorithm

For each owner triple and prescribed target triple, the checker stores the list
of containing Hamilton cycles.  By PP3bpn this list has at most `(m-4)!` entries.
For each complement-reduced sign mask it then:

1. rejects assignments with no three-owner collinearity;
2. retains only parity-satisfiable source cycles whose clean fibre is compatible
   with the three prescribed signs;
3. assigns the exact source weight `2^(c-r)`;
4. enumerates every owner-intersecting clean successor rotation;
5. solves the exact Hall ratio by rational Dinkelbach iteration and weighted
   maximum-closure min-cut as in `docs/337`.

### Theorem PP3bpp -- VERIFIED FINITELY / COMPLETE REGRESSION

The compressed algorithm exactly reproduces every published invariant for
`4<=m<=8`, including clean-state counts, flaw counts, proper bottleneck counts,
worst charges, global ratios, maximum merging penalties, and Dinkelbach cut
counts.

The maximum source-cycle counts are

```text
m=4: 1,
m=5: 1,
m=6: 2,
m=7: 6,
m=8: 24,
```

matching `(m-4)!` whenever the maximum is attained.

## 4. Complete `m=9` weighted transport audit

### Theorem PP3bpq -- VERIFIED FINITELY / EXACT `m=9` HALL CENSUS

At `m=9` the compressed audit gives

```text
parity-clean signed states:       6,727,728,
atomic signed-assignment flaws:      25,540,
maximum source cycles per flaw:         120,
flaws with a proper bottleneck:       25,520.
```

Thus only 20 flaws have their optimum at the complete source set.

The exact worst optimal charge is

```text
gamma_max = 223/29271,
9^3 gamma_max = 162567/29271 = 5.553858... .
```

One maximizing flaw has

```text
source owners:       (1,4,7),
target assignments:  (7,5,6),
orientations:        (0,1,0).
```

It has 96 compatible source cycles.  Its maximizing Hall set contains 77 of
them, with

```text
W=3,568,
V=468,336,
W/V=223/29,271.
```

The worst complete-source-set ratio over all flaws is

```text
501/66,848,
```

strictly smaller than the worst optimal charge.  The maximum local/global
merging penalty is

```text
226,808/108,915 = 2.08240... .
```

The exact Dinkelbach algorithm uses at most eight conceptual min-cuts, counting
the analytically known zero-ratio initial closure.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_weighted_hall_transport_m9_compressed.cpp \
  -o /tmp/check_weighted_hall_transport_m9_compressed
OMP_NUM_THREADS=5 /tmp/check_weighted_hall_transport_m9_compressed
```

The checker hard-codes and verifies every exact ledger through `m=9`.  Its JSON
output is stored in
`experiments/weighted-hall-transport-m9-compressed-audit.json`. ∎

## 5. Revised weighted-expansion frontier

The finite cut geometry changes again at `m=9`.

1. At `m=8` the worst absolute obstruction is a two-source cut.
2. At `m=9` the worst cut is intermediate and large: 77 of 96 sources.
3. Proper bottlenecks occur for `25,520/25,540` flaws.
4. The scaled worst charge rises only slightly, from `5.50538` to `5.55386`.
5. The maximum merging penalty remains just above two and decreases from its
   `m=8` value.

Therefore neither a purely global-mass theorem nor a theorem controlling only
constant-size cuts is sufficient.  The asymptotic target must control a spectrum
of weighted cuts, including intermediate source sets, or prove that a short
clean heat trajectory disperses them.

The compressed source generator makes larger exact audits conceptually possible;
the next computational bottleneck is the `(m-4)!` source list and the number of
geometric signed-assignment flaws, not the clean signed-state universe.

The next theorem identifier after this chapter is `PP3bpr`.

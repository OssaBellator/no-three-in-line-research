# Alternating-core bounded-epoch atlas census

## Status

This note keeps AC as the sole active research focus and proves AC5in--AC5ir. It continues the kernel coverage atlas of AC5ii--AC5im by making atlas construction itself finite and auditable on one declared bounded physical epoch.

The pass does not construct the missing geometric AC epoch, prove that the historical template registry is complete, prove AC6, or prove the no-three-in-line conjecture. It proves that once a bounded physical object census and a finite candidate-template list are supplied, the least uncovered object, an irredundant closed atlas, and an exact minimum closed atlas are canonical finite outputs.

## Bounded epoch census

Fix one physical AC epoch with one complete schema version. Let

\[
\mathcal U=\Omega\sqcup V\sqcup E
\]

be the disjoint ordered union of all admissible tagged compatibility pairs, physical macro states and certified transitions in that epoch.

Let `K_1,...,K_m` be a finite ordered candidate-template registry. Every template retains:

- its exact subset `C_i subseteq U` of covered physical objects;
- complete records for every object in `C_i`;
- a finite prerequisite set `P_i subseteq {1,...,m}`;
- a nonnegative integral construction weight `w_i`;
- references to globally addressed typed capacities;
- every bridge, restart and source-lineage field required by AC5ii--AC5il.

Prerequisites mean that a template may be used only together with all templates in its transitive prerequisite closure. They are not hidden edges and do not create physical coverage by themselves.

For an atlas index set `A`, put

\[
C(A)=\bigcup_{i\in A}C_i,
\qquad
U(A)=|\mathcal U\setminus C(A)|.
\]

An atlas is **closed** when `P_i subseteq A` for every `i in A`, **consistent** when all overlapping physical and capacity records agree, and **complete** when `U(A)=0`.

## AC5in -- canonical epoch incidence matrix and first malformed record -- PROVED

The complete epoch serialization canonically determines the finite incidence matrix

\[
M_{x,i}=1_{x\in C_i},
\qquad x\in\mathcal U,\ 1\le i\le m,
\]

together with the prerequisite matrix, construction weights and capacity-address table.

Before atlas selection, the compiler returns the least of:

1. an out-of-range or stale prerequisite;
2. two candidate records assigning different values to the same physical object;
3. two candidate records assigning different types, amounts, weights or lineages to the same capacity address;
4. an unknown object not belonging to the declared epoch universe.

On the accepted branch every candidate subset has a well-defined coverage set, prerequisite closure, weight and globally deduplicated capacity record.

### Proof

All records are finite, ordered and field-complete. Matrix membership is finite set membership. Canonical serialization makes equality of records equality of every retained field, and the fixed product order selects the least malformed or conflicting record. QED.

## AC5io -- deterministic closed greedy atlas and irredundant witnesses -- PROVED

Start with `A=empty`. At each stage, for every unselected template `i`, form the transitive prerequisite bundle

\[
Q_i=\operatorname{cl}(\{i\})\setminus A.
\]

Among consistent bundles with positive uncovered gain, select the one maximizing, in order,

1. `|C(Q_i)\setminus C(A)|`;
2. minus its added total weight;
3. minus its number of added templates;
4. the fixed reverse template order.

Insert that bundle and continue. Every successful insertion decreases `U(A)` by exactly its displayed gain. If no positive-gain consistent bundle exists while `U(A)>0`, the least uncovered object is returned.

When `U(A)=0`, scan the selected templates in reverse insertion order and delete any template whose removal leaves the atlas complete, closed and consistent. The resulting atlas `G` is irredundant in the closed-atlas sense. For every `i in G`, removing `i` produces exactly one of:

- a least **private physical object** in `C_i` no longer covered;
- a least **dependency-critical witness**, namely a retained selected template whose prerequisite closure uses `i`.

Thus every retained greedy template has a finite reason for remaining in the atlas.

### Proof

Each insertion uses a finite deterministic maximum and strictly lowers the nonnegative integer `U(A)`, so the process terminates. Reverse deletion preserves completeness and closure at every accepted deletion. At termination, removing a selected template must fail completeness or closure; the fixed object and template orders select the stated witness. QED.

## AC5ip -- exact minimum closed atlas -- PROVED

For a complete consistent candidate registry, order every closed complete atlas `A` by

\[
\operatorname{obj}(A)
=
\left(
\sum_{i\in A}w_i,
|A|,
(i_1,\ldots,i_{|A|})
\right),
\]

where `i_1<...<i_|A|`.

Finite subset enumeration, bitmask dynamic programming or any equivalent exact branch-and-bound procedure returns the unique lexicographically least minimizer

\[
A_{\min}=\arg\min \operatorname{obj}(A).
\]

If no closed complete atlas exists, the compiler returns the least uncovered object after the union of all consistent prerequisite-closed candidates, or the earlier malformed/conflict witness of AC5in.

The exact optimizer never selects a template without its prerequisites and never counts two aliases of one physical capacity as separate stock.

### Proof

There are only `2^m` template subsets. Closure, coverage and consistency are finite predicates, so the set of feasible atlases is finite and decidable. The displayed objective is a total order, hence has a unique minimum whenever the feasible set is nonempty. QED.

## AC5iq -- candidate-neighbourhood bottleneck packing -- PROVED

For every physical object `x in U`, define its candidate neighbourhood

\[
N(x)=\{i:x\in C_i\}.
\]

If `N(x)=empty`, then `x` is an exact uncovered-object obstruction.

If `W subseteq U` has pairwise disjoint candidate neighbourhoods, then every complete atlas contains at least `|W|` templates. Consequently

\[
|A_{\min}|\ge \max\{|W|:N(x)\cap N(y)=\varnothing\text{ for }x\ne y\}.
\]

A deterministic greedy packing obtained by scanning objects in increasing `( |N(x)|,x )` order gives a canonical computable lower bound. An object with `|N(x)|=1` makes its unique template coverage-essential unless a prerequisite or record conflict has already invalidated that candidate.

### Proof

One selected template can cover objects from at most one member of a family whose template neighbourhoods are pairwise disjoint. Therefore distinct members require distinct selected templates. The zero-neighbourhood and singleton conclusions are immediate. QED.

## AC5ir -- optimized bounded-epoch atlas certificate -- PROVED UNDER A COMPLETE CENSUS

Assume AC5in accepts and AC5ip returns `A_min`. Form the selected union graph and run AC5ik on it. Let `Psi_*` be its exact mixed-radix maximum. Deduplicate only the globally addressed capacities referenced by `A_min`, obtaining

\[
C_{\rm pay}^{\min},
C_{\rm ticket}^{\min},
C_{\rm reset}^{\min},
U^{\min},
W_{\rm dist}^{\min}.
\]

The scheduler restricted to the selected complete atlas satisfies

\[
\boxed{
E_{\min}
\le
(C_{\rm reset}^{\min}+1)\Psi_*
+U^{\min}W_{\rm dist}^{\min}
+C_{\rm pay}^{\min}
+C_{\rm ticket}^{\min}.
}
\]

Extra candidate templates and unreferenced capacities are not used by this scheduler and are not counted. Shared physical addresses cited by several selected templates contribute once.

The complete bounded-epoch census output is exactly one of:

- an exact minimum closed atlas, its greedy irredundant comparison, private/dependency witnesses, bottleneck lower bound, union rank and finite episode bound;
- the least uncovered pair, state or edge;
- the least malformed prerequisite, overlap conflict, capacity-alias conflict, bridge/restart violation or unreachable selected-union state.

### Proof

AC5ip supplies a complete closed consistent selected atlas. AC5ik supplies selected-union reachability and strict minimax rank. AC5il deduplicates the selected capacity addresses. AC5im then applies verbatim to the scheduler restricted to that selected atlas. QED.

## Deterministic audit

`scripts/verify_ac_bounded_epoch_atlas_census.py` checks 2,500 bounded epoch systems. It verifies:

- canonical malformed-prerequisite, object-conflict, capacity-conflict and uncovered-object routes;
- exact prerequisite closure and marginal coverage descent;
- reverse-deletion irredundancy with private or dependency-critical witnesses;
- exact minimum weighted closed-atlas enumeration;
- the candidate-neighbourhood packing lower bound;
- globally deduplicated selected capacity totals;
- the selected-atlas episode formula.

The deterministic run contains 500 valid complete censuses and 500 instances of each of four exact failure classes.

## Main AC frontier

Only AC remains active. The next physical work is now sharply finite:

1. serialize the first actual bounded AC epoch into `Omega sqcup V sqcup E`;
2. generate candidate templates from the historical direct-exclusion, layered, pool-shadow, repair, source-flow and recurrence records;
3. run AC5in to eliminate malformed overlaps and aliases;
4. run AC5io/AC5ip to obtain an irredundant and exact minimum physical atlas;
5. use AC5iq to identify zero-neighbourhood and low-neighbourhood frontier objects;
6. certify the selected union graph, bridges and capacities;
7. run AC5ir;
8. enlarge the physical epoch or discharge the least returned object.

AC6 and the global no-three-in-line conjecture remain open.

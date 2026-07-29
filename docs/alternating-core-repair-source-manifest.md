# Alternating-core repair-source physical manifest compiler

## Status

This note keeps AC as the sole active research focus and proves AC5mj--AC5mo. It imports the strongest later alternating-core repair machinery into the current physical manifest: layer-witness concentration, deficit-sized occurrence-slot transversals, classwise repair-source conservation, source-incidence compatibility Hall cores and missing-predicate rectangles.

The result does not construct the actual geometric incidence layers or compatibility predicates. It proves that every repair failure is reduced to one finite physical target: a bad layer, a deficit-sized outside-slot transversal, a source-less issuance, an overloaded conserved class, or a canonical missing compatibility rectangle.

## Layered repair records

For every retained incidence layer `i`, record:

- forward-degree lower bound `d_i`;
- exact conditioning loss `b_i`;
- endpoint-overlap excess `o_i`;
- reverse-load bound `D_i`;
- every physical incidence assigned to the layer.

Put

\[
a_i=d_i-b_i-o_i,
\qquad
A=\sum_i a_i,
\qquad
D=\sum_iD_i.
\]

Every deletion, overlap and reverse incidence belongs to exactly one retained layer field.

## AC5mj -- global layer success or canonical bad-layer witness -- PROVED

When `D>0`, the global relative deficiency is

\[
\eta=(1-A/D)_+.
\]

If every positive-load layer satisfies

\[
a_i\ge(1-\varepsilon)D_i,
\]

then `A>=(1-epsilon)D`. Conversely, when `A<D`, the compiler returns the least positive-load layer satisfying

\[
\boxed{
\frac{(D_i-a_i)_+}{D_i}
\ge
\frac{D-A}{D}.
}
\]

A missing layer field, unrecorded overlap or negative zero-load contribution is a schema/reset witness, not a paid obstruction.

### Proof

The identity `sum_i(D_i-a_i)=D-A` expresses the global deficit as a reverse-load-weighted average of local relative deficits after negative contributions are discarded in the favourable direction. Some positive-load layer attains at least the average. QED.

## AC5mk -- deficit-sized occurrence-slot repair transversal -- PROVED

Fix a finite occurrence-faithful use/slot graph `G=(U,S,E)` and its canonical maximum-deficit Hall core `C`. Put

\[
\delta=|C|-|N_G(C)|>0.
\]

For any complete repair extension with injective assignment `P:U->S^+`, define

\[
R_P(C)=\{(u,P(u)):u\in C,\ P(u)\notin N_G(C)\}.
\]

Then

\[
\boxed{|R_P(C)|\ge\delta.}
\]

Every incidence in this set is genuinely new relative to the old graph. Sorting by complete physical pair address and taking the first `delta` gives a canonical transversal with distinct core uses and distinct outside slots.

If selected incidences carry one of `L` physical creation/restoration classes, one class contains at least

\[
\boxed{\lceil\delta/L\rceil}
\]

transversal incidences. A proposed repair exposing fewer than `delta` distinct compatible outside slots is impossible.

### Proof

At most `|N(C)|` core uses can be assigned to distinct old-neighbourhood slots, while `P` assigns all `|C|` uses. The remaining at least `delta` uses occupy distinct outside slots and use edges absent from the old graph. Pigeonhole gives class concentration. QED.

## AC5ml -- exact repair-source issuance and classwise conservation -- PROVED

A repair-source occurrence is a unit token with complete predecessor address and one retained repair class. Initial tokens and named deposits are the only roots. A legal source transition consumes one live predecessor and creates one same-class successor. Issuing one transversal incidence consumes one compatible live token exactly once.

At every prefix,

\[
\boxed{
\text{live repair tokens}
+
\text{issued transversal incidences}
=
\text{initial tokens}
+
\text{named deposits}.
}
\]

The same identity holds separately in each complete repair class. Therefore cumulative selected incidences cannot exceed initial plus deposited source mass, globally or classwise.

The first source-less issuance, predecessor split, repeated debit, hidden deposit, class migration or address mismatch is returned with its exact event-log prefix.

### Proof

Induct on the event log. Deposits increase both available mass and the right side; same-class transitions preserve live mass; issuances transfer one unit from live to issued. These are the only accepted events. QED.

## AC5mm -- source compatibility assignment or canonical Hall core -- PROVED

Let `R` be the selected unit repair incidences and `T` the live unit repair-source tokens after conservation. Join `r` to `t` exactly when every retained class, physical source, issued-source, certificate, layer and defect compatibility predicate passes.

A complete source realization exists exactly when Hall's inequalities hold. Otherwise choose the canonical deficient subset by:

1. maximum deficit;
2. minimum cardinality;
3. lexicographic complete incidence address.

For the returned core `X`, let

\[
\delta_X=|X|-|N(X)|>0.
\]

Every proper subset has smaller deficit and a maximum matching saturates the entire old token neighbourhood.

### Proof

This is finite bipartite matching and Hall's theorem. The displayed tie-breaking makes the core canonical. Maximum-deficit minimality gives the proper-subset statement and standard alternating-path structure saturates the old neighbourhood. QED.

## AC5mn -- missing compatibility rectangle and predicate concentration -- PROVED

Assume classwise numerical source sufficiency: the class containing core `X` has at least `|X|` live tokens. Then at least `delta_X` same-class tokens lie outside `N(X)`.

Let `T_out` be all such outside tokens. Every pair in

\[
\boxed{X\times T_{\rm out}}
\]

is a missing compatibility edge. Assign each pair to the least failed retained predicate. If `q` predicates are retained, one predicate class contains at least a `1/q` share of the rectangle, and one core incidence fails against at least the corresponding `1/q` share of outside tokens.

The exact minimum number of newly validated source-incidence pairs required for a complete assignment is the Hall deficit `delta_X`.

### Proof

Outside tokens are not neighbours of any core incidence, hence the product is a missing-edge rectangle. Pigeonhole over the ordered predicate dictionary gives concentration. Adding fewer than `delta_X` edges cannot remove deficit `delta_X`; a maximum-matching augmentation can use exactly one new edge per deficit unit when completion is possible. QED.

## AC5mo -- complete repair/source manifest compiler -- PROVED

For every localized repair failure, run:

1. AC5mj on the retained layer table;
2. AC5mk on the occurrence-slot Hall core;
3. AC5ml on the repair-source event log;
4. AC5mm on incidence-to-source compatibility;
5. AC5mn on any remaining Hall deficiency.

The output is exactly one of:

- a globally adequate layered incidence system;
- a canonical bad layer;
- a deficit-sized physical repair transversal;
- a conserved classwise source issuance;
- a complete occurrence-faithful source assignment;
- a canonical source Hall core and missing predicate rectangle;
- an impossible repair extension;
- the first source-less issuance, duplicate debit, hidden deposit, class migration, omitted compatibility field or schema reset.

Accepted assignments populate the `flow`, `repair`, `exception` and `frontier` sections of the initial-state manifest. Returned rectangles and bad layers are exact geometric construction targets.

### Proof

Each stage is finite and produces either the required input to the next stage or one exact failure. The contracts preserve physical addresses and class labels throughout, so the outputs compose without hidden relabelling or source creation. QED.

## Deterministic audit

`scripts/verify_ac_repair_source_manifest.py` checks 2,500 generated layered repair/source systems. It verifies bad-layer concentration, deficit-sized transversals, source conservation, occurrence-faithful assignments, Hall cores, missing rectangles, predicate concentration and source-less issuance failures.

## Main AC frontier

Only AC remains active. The next physical tasks are:

1. populate the actual incidence layers and local values `d_i,b_i,o_i,D_i`;
2. construct the outside repair slots for each returned Hall core;
3. enumerate the physical repair-source occurrence dictionary and event log;
4. validate the source-incidence compatibility predicates;
5. discharge the first bad layer, missing rectangle or source-conservation failure;
6. append accepted repair operations to the reachable rank and exception tables.

AC6 and the global no-three-in-line conjecture remain open.

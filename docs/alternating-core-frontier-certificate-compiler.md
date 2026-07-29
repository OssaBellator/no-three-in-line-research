# Alternating-core frontier certificate compiler

## Status

This note keeps AC as the sole active research focus and proves AC5jd--AC5ji. It continues AC5iy by compiling the two active nonterminal queues:

1. interior objects with zero historical-template neighbourhood;
2. boundary records that still need a permanent physical certificate or a construction route.

The compiler works at the level of complete physical source rows, producer graphs and boundary certificates. It never assigns an object to a template because its untagged combinatorial shape resembles a previously covered object.

The result remains contract-qualified. It does not construct the missing geometric rows, prove that every shortage is permanent or repairable, prove all claimed positive-drift escapes, prove the physical source graph, prove AC6, or prove the no-three-in-line conjecture.

## Historical recognizer rows

Fix one bounded epoch and its canonical object serialization. The six AC-native recognizer kinds require the following row families.

| Kind | Required physical rows |
|---|---|
| `direct` | support, secant, dangerous-line, residual and declared-new-blocker rows |
| `layered` | incidence layers, conditioning deletions, endpoint identities and reverse-load rows |
| `pool` | initial blockers, paid depletion, new blockers, new-cell lists and charged pair-shadow rows |
| `repair` | defect uses, faithful slots, compatibility, repair extensions and live source-compatible tokens |
| `flow` | physical sources, issued sources, certificates, defects and all retained capacity/compatibility arcs |
| `recurrence` | low-buffer lineages, recreation edges, guards, residue phases and complete tail transition rows |

Every row has a complete physical address, schema version, source provenance, declared weight and soundness certificate. A row unavailable in the physical epoch is distinguished from a row merely not yet attached to the object. A conflicting row is distinguished from both.

## AC5jd -- exact recognizer-row deficit matrix -- PROVED

For each zero-neighbourhood interior object `x` and recognizer kind `k`, let

- `R_k(x)` be the finite required row set;
- `P(x)` be the rows already present on `x`;
- `A(x)` be the rows available with sound physical certificates;
- `F(x)` be the rows whose retained values conflict with the required record.

Define the missing-row set

\[
M_k(x)=R_k(x)\setminus P(x).
\]

Kind `k` is **completion-feasible** for `x` exactly when

\[
R_k(x)\cap F(x)=\varnothing
\qquad\text{and}\qquad
M_k(x)\subseteq A(x).
\]

The complete ordered row serialization determines a finite object--kind--row incidence matrix and returns the least of:

1. a stale row version;
2. an omitted row address;
3. two available rows assigning different physical values;
4. a required row with a conflicting retained value;
5. a required missing row unavailable in the epoch.

On the accepted branch, every object-kind pair has an exact finite missing set and feasibility value.

### Proof

All six row dictionaries are finite and every record is field-complete. Feasibility is the displayed finite set test, and the fixed object, kind and row orders select the first discrepancy. QED.

## AC5je -- least single-object completion or rigid schema witness -- PROVED

Give every physical row `r` a nonnegative integral construction weight `w(r)`. For a feasible recognizer kind define

\[
\operatorname{cost}_k(x)
=
\left(
\sum_{r\in M_k(x)}w(r),
|M_k(x)|,
k
\right).
\]

The lexicographically least feasible kind and its exact missing-row set form the canonical completion bundle for `x`.

Adding that bundle covers `x` only after every missing row is supplied with its declared certificate and all overlap checks pass. No value is inferred for another object.

If no kind is feasible, `x` is a **rigid schema object**. The compiler returns the least recognizer kind together with its least failed required row, classified as unavailable or conflicting. Thus a zero-neighbourhood object cannot remain an anonymous atlas deficit.

### Proof

There are six finite candidates. The cost order selects a unique least feasible bundle. If none is feasible, every kind has a finite failed-row witness, and the fixed orders select the first. QED.

## AC5jf -- exact minimum shared completion atlas -- PROVED

Let `Z` be a finite batch of zero-neighbourhood objects that are not rigid. A candidate completion template retains:

- one recognizer kind and complete template parameters;
- one finite supplied-row set;
- the exact objects whose missing rows it supplies without conflict;
- all prerequisite templates;
- one construction weight;
- every referenced physical capacity address.

A selected completion atlas must be prerequisite-closed, overlap-consistent and cover every object in `Z`.

Among all such atlases, finite subset enumeration or equivalent branch-and-bound returns the unique minimizer of

\[
\left(
\text{total construction weight},
\text{template count},
\text{lexicographic template list}
\right).
\]

Reverse deletion from any complete selected atlas produces an irredundant closed atlas. Every retained template has either:

1. a private zero-neighbourhood object that becomes uncovered on removal; or
2. a dependency-critical selected template whose prerequisite closure uses it.

Physical capacity aliases are deduplicated by global address exactly as in AC5il.

### Proof

The candidate registry is finite. Closure, consistency and coverage are finite predicates, and the displayed objective is a total order. Reverse deletion can fail only coverage or closure, giving the stated witnesses. QED.

## AC5jg -- producer-graph shortage criterion -- PROVED

Fix one typed shortage record for resource or balance coordinate `d`. Construct the finite directed producer graph whose vertices are complete resource/source/certificate classes and whose edges are legal occurrence-faithful unit transfers or issuances. Mark the currently live source vertices and retain all capacities and compatibility guards.

Exactly one of the following occurs:

1. `d` is reachable from a live source by a legal residual producer path; the canonical shortest lexicographically least path is the next repair/flow construction route;
2. `d` is unreachable; the residual set reachable from all live sources gives a canonical producer cut separating every available source from the shortage coordinate.

In the second branch the shortage is permanent inside the current fixed source dictionary unless a named deposit, compatibility addition, capacity increase or schema reset crosses that cut.

### Proof

This is finite directed reachability. Breadth-first search from the ordered live-source set gives the canonical shortest path when one exists. Otherwise the reachable set has no legal outgoing path to `d`, so its boundary is the asserted producer cut. QED.

## AC5jh -- permanent boundary certificate normal form -- PROVED

Every non-overflow boundary record is accepted as permanent only with one of the following complete certificates.

1. **Terminal:** the exact terminal predicate and completed physical state.
2. **Shortage:** the producer cut of AC5jg, or a named reachable producer path that moves the record back to the construction queue.
3. **Amplification:** the source/certificate conservation equation and exact excess above initial-plus-named deposits; a named deposit instead refines the record into the enlarged physical balance.
4. **Monotone escape:** one complete finite phase cycle, its threshold `T(C)`, drift
   \[
   D\equiv0\pmod M,
   \]
   and `D>0`; zero drift is an exact return and negative drift has finite headroom rather than escape.
5. **Reset:** the first changed schema or physical-interpretation field together with one globally addressed funded reset; without a funded reset it is a schema-tower boundary, not paid progress.

A record missing one required field, carrying inconsistent source identity, using a nonpositive escape drift, or claiming an unfunded reset is returned to the exact missing-certificate queue.

### Proof

The five cases are the permanent non-overflow routes of AC5iy. AC5jg supplies the shortage certificate, source conservation supplies amplification, the periodic-tail theorem supplies the drift trichotomy, and the restart theorem supplies the funded-reset condition. QED.

## AC5ji -- finite frontier completion pass and exact descent -- PROVED

For one bounded box define the frontier measure

\[
\Phi_{m fr}
=(Z,R,B),
\]

ordered lexicographically, where

- `Z` is the number of zero-neighbourhood interior objects;
- `R` is the number of non-overflow boundary records lacking a permanent certificate or construction route;
- `B` is the number of unresolved overflow records.

One **frontier completion pass** performs, in order:

1. AC5jd--AC5jf on every zero-neighbourhood object;
2. AC5jg--AC5jh on every non-overflow boundary record;
3. AC5iz--AC5ja on the remaining finite overflow queue.

Every successful row completion decreases `Z`; every accepted permanent boundary certificate or producer route decreases `R`; and the least cap enlargement resolves every current overflow and decreases `B` to zero before the new shell is serialized.

The output is exactly one of:

- a completed interior template atlas, permanent boundary certificate table and drained current overflow queue;
- a rigid schema object;
- an unavailable or conflicting physical row;
- a producer cut or missing producer edge;
- an amplification, escape or reset certificate failure;
- the exact new shell and refined-boundary queue for the next pass.

No completed old object is reintroduced by cap enlargement because AC5iw preserves the interior and AC5ja restricts new work to the shell and refined boundary records.

### Proof

Each stage is finite and either supplies the stated certificate or exact failure. The relevant nonnegative component of `Phi_fr` strictly decreases on every successful old-frontier action. AC5iw gives no regression. QED.

## Deterministic audit

`scripts/verify_ac_frontier_certificate_compiler.py` checks 2,500 generated frontier systems. It verifies:

- exact required, present, available and conflicting recognizer-row sets;
- least feasible single-object completion and rigid-object witnesses;
- exact minimum prerequisite-closed shared completion atlases;
- private-object and dependency-critical irredundancy witnesses;
- canonical producer paths and permanent producer cuts;
- amplification/deposit, drift and funded-reset boundary routing;
- exact decrease of the old-frontier measure.

## Main AC frontier

Only AC remains active. The remaining physical tasks are now executable queues:

1. supply or refute the returned row for each rigid or incomplete object;
2. build the named producer path or prove the returned producer cut permanent;
3. provide conservation, drift and reset certificates for boundary records;
4. expand only the unresolved overflow coordinates;
5. repeat on the exact new shell;
6. use AC5jc once the resulting physical tower is cofinal and uniformly bounded.

AC6 and the global no-three-in-line conjecture remain open.

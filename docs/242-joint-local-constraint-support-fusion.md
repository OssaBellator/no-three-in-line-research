# Joint local constraints fuse into one rank-three helper hypergraph

PP3aru leaves source-clean, transition, anchor, distinguished-endpoint, Hall,
alternating, and matching conditions as external second-host alternatives.  For the
strictly alternating one-layer construction, most of these conditions are not
independent graph-theoretic stages.

The cycle itself is already a permutation and hence a perfect matching.  Every
local reason that one of its arcs, arc pairs, or arc triples is inadmissible can be
recorded in the same ordinary-helper support hypergraph as the source and insertion
events.  Strict alternation keeps support rank at most three.  One independent
helper set therefore satisfies all local conditions simultaneously.

This replaces the sequence

```text
prepare source-safe host -> prove Hall -> find alternating cycle -> control cost
```

by one direct support-free cycle selection.

## 1. Local constraint families

Let `D` be a marked set and `H` an ordinary-helper reservoir in one permutation
layer.  Consider strictly alternating cycles on `D` and equally many helpers.

A **local admissibility constraint** is a forbidden pattern determined by at most
three selected endpoint cells, together with fixed retained-source, controller,
label, anchor, or distinguished-endpoint data.  Examples include:

1. a selected arc forbidden by source safety, pool use, controller preservation, or
   a distinguished endpoint;
2. an anchored transition or same-slot anchor condition on one or two selected
   arcs;
3. a source-invalid pair or triple;
4. a positive unary or binary controller-shadow insertion event;
5. an edge, path, or partner condition used to define a source-safe endpoint host.

For each positive forbidden pattern, record the ordinary helper indices appearing
in its selected cells.

### Proposition PP3ase -- PROVED

Every nonzero local admissibility pattern has nonempty ordinary-helper support of
size at most three.

#### Proof

A forbidden pattern contains at least one selected endpoint cell.  Every selected
cell of a strictly alternating cycle contains exactly one ordinary helper by
PP3arp.  By definition the pattern uses at most three selected cells, so its helper
support has size between one and three. ∎

## 2. The fused support hypergraph

Let

```text
K_joint
```

be the simple hypergraph obtained by taking the union of the helper supports from
all local constraint families, including every canonical source-invalid and
insertion signature.

### Proposition PP3asf -- PROVED

The hypergraph `K_joint` has rank at most three.  If `H_0 subseteq H` is independent
in `K_joint`, then every strictly alternating cycle on `D union H_0`:

1. preserves the tied permutation layer and saturation;
2. fixes every active controller outside the punctured marked set;
3. satisfies every encoded source, transition, anchor, distinguished-endpoint,
   pool, and local endpoint-host condition;
4. is source-valid;
5. has insertion cost zero.

#### Proof

The rank statement is PP3ase.  Selection of any forbidden local pattern would put
its complete nonempty helper support inside `H_0`, contradicting independence.
The permutation and controller statements are PP3ari--PP3arl. ∎

The conclusion is deterministic after `H_0` is chosen.

## 3. Hall and alternating structure are bypassed

### Theorem PP3asg -- PROVED

For the fused strictly alternating construction, no separate Hall or alternating-
SCC theorem is required.

1. The selected cycle is itself a permutation of the chosen tied indices, hence a
   perfect matching.
2. Every selected off-diagonal edge is locally admissible by PP3asf.
3. The cycle is one nontrivial alternating component on its selected indices.
4. Every unselected tied endpoint remains on its reference edge.

Thus Hall, matching, and alternating feasibility follow directly from the explicit
cycle, provided every edge-local and bounded-pattern obstruction has been included
in `K_joint`.

#### Proof

A directed cycle permutation is a perfect matching on its selected rows and
columns.  PP3asf excludes every encoded forbidden edge or bounded pattern.  The
remaining indices are fixed, so the union is a perfect matching of the full layer.
∎

This theorem does not assert that arbitrary global constraints are local.  It says
that the Hall/alternating machinery is unnecessary once all actual admissibility
conditions have the finite local normal form used throughout the prime-patching
construction.

## 4. Critical square-root joint dichotomy

Assume

```text
|D|=W,
|H|=Theta(W^2).
```

### Theorem PP3ash -- PROVED / CONDITIONAL FINITE LOCAL NORMAL FORM

Exactly one of the following occurs.

1. `K_joint` has an independent `W`-set, giving a cycle satisfying all local source,
   transition, anchor, distinguished-endpoint, pool, controller, matching, Hall,
   alternating, and insertion requirements simultaneously.
2. One local constraint family has, after constant type refinement:
   - `Omega(W^2)` rank-two supports, or
   - `Omega(W^3)` rank-three supports, or
   - `Omega(W^2)` individually forbidden helpers.
3. A constraint outside the finite rank-three local normal form is genuinely global.

#### Proof

Apply PP3arr to `K_joint`.  In every dense branch, each edge has one of finitely
many constraint types and endpoint roles.  Pigeonhole one type with constant
relative mass.  The independent branch is PP3asf--PP3asg. ∎

### Corollary PP3asi -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

In alternative 2 of PP3ash, the concentrated family yields a target-size star,
matching, fixed-core petal bank, endpoint bank, transition sunflower, anchor bank,
or one of the canonical `A_2/B_3/B_4` geometries.

#### Proof

Apply PP3art after the finite type refinement. ∎

## 5. Direct second-host theorem

### Theorem PP3asj -- PROVED / CONDITIONAL COMMON-LAYER AND FINITE LOCAL NORMAL FORM

For a co-layered target marked set with controller density bounded away from one,
the complete second-host problem has the exact alternatives:

1. a directly constructed strictly alternating cycle with zero source violations
   and zero insertion cost;
2. a target-size converted local certificate;
3. a genuinely global condition not representable by a forbidden pattern on at
   most three selected cells;
4. failure of co-layering or loss of the square-root-size controller-disjoint
   reservoir.

Source-clean, transition, anchor, distinguished-endpoint, matching, Hall, and
alternating conditions are not separate alternatives when they have the local
normal forms already used in the endpoint architecture.

#### Proof

Fuse all local families by PP3asf and apply PP3ash--PP3asi. ∎

## 6. Application to cycle cancellation

### Corollary PP3ask -- PROVED

In PP3asa, the zero-cost second cycle may be selected against the union of every
local host constraint and every source/insertion support family.  Hence the target-
cycle composite cancellation theorem fails internally only if:

1. a target-size converted local structure is produced;
2. the marked cells are not co-layered;
3. no eligible layer contains `Theta(W^2)` controller-disjoint helpers;
4. a genuinely global nonlocal condition remains.

A separate Hall or alternating-host failure is no longer an endpoint of the direct
cycle construction.

The no-three-in-line conjecture remains unproved.

# Canonical private-owner assignment and selected subbanks

**Branch:** `research/alternating-core-chain`

AC3mq leaves arbitrary selected protected subbanks and independent owner assignments
as live outer data.  Some of those choices are genuinely discretionary, but the
private capacity-one case has a canonical matching model.  Once the exact demand
set, eligible owner-capacity units and spent mask are fixed, choose the
lexicographically least maximum matching.  The selected subbank and its private
assignment are then derived outputs rather than additional set-valued fields.

This note applies only to exact private capacity units.  A shared owner used by
several alternatives is counted once by AC3w and must not be cloned into several
capacity units unless the underlying theorem supplies those distinct units.
Likewise, a matching edge records eligibility, not payment; AC3ke--AC3kf still
require current, physical, coherent and payable status for the selected
transition.

## Demand--owner graph

Fix finite totally ordered sets:

\[
D=\{d_1,\ldots,d_s\},
\qquad
T=\{t_1,\ldots,t_m\},
\]

where `D` is the exact demand set of one proposed transition and `T` is a set of
exact private capacity-one owner units.  Let

\[
E\subseteq D\times T
\]

be the exact eligibility graph.  Let `F subseteq T` be the persistent spent or
unavailable mask, and write `T_F=T\setminus F`.

A partial owner assignment is a matching in `E[D,T_F]`.  Encode it by the owner
index assigned to each ordered demand, using the sentinel `m+1` for an unmatched
demand.  Order assignments lexicographically after first maximizing their
cardinality.

## AC3nc -- canonical maximum private-owner assignment -- PROVED

There is one unique canonical assignment

\[
\boxed{M^*(D,T,E,F)}
\]

obtained as the lexicographically least maximum matching in `E[D,T_F]`.  Its
selected private subbank is the set of owner units met by `M^*`.

Consequently:

1. fixed demands, exact owner units, eligibility graph, spent mask and fixed
   orders force one exact selected subbank and assignment;
2. if any private assignment saturates every demand, `M^*` also saturates every
   demand;
3. if no complete private assignment exists, `M^*` has maximum possible size;
4. storing another arbitrary selected subset or private assignment duplicates
   derived data when the canonical policy is declared.

### Proof

The finite matching set is nonempty because the empty matching is allowed.
Maximum cardinality is therefore defined, and the finite set of maximum matchings
has one lexicographically least member.  A maximum matching saturates `D` exactly
when some matching does.  Its incident owner set is determined by the matching.
QED.

The theorem is mathematical and does not require a particular matching algorithm.

## AC3nd -- one-atom rank sensitivity and assignment-rotation guardrail -- PROVED

Let `nu(E,F)=|M^*(D,T,E,F)|` be the maximum assignable demand count.

1. Adding or removing one eligibility edge changes `nu` by at most one.
2. Making one owner-capacity unit available or unavailable changes `nu` by at
   most one.
3. The exact canonical matching may nevertheless change on many demand--owner
   pairs after one input-atom change.

Thus the valid Lipschitz statement is

\[
\boxed{|\nu-\nu'|\le1}
\]

for one eligibility-edge or one owner-availability update.  No analogous
constant bound is claimed for `|M^* triangle M^{*prime}|`.

For fixed universes of sizes `s,m`, every strict input change has a canonical
least decoration of one of the forms

\[
(d,t,+),\ (d,t,-),\ (t,+),\ (t,-),\ (d,+),\ (d,-),
\]

for eligibility, availability or demand-set changes.  A safe atomic reset
alphabet has size

\[
\boxed{R_{\rm assign}\le2(sm+m+s).}
\]

A weighted family of assignment resets of total weight `W` therefore has one
exact input-atom/direction class of weight at least

\[
\boxed{W/R_{\rm assign}.}
\]

### Proof

Adding one matching edge can enlarge a maximum matching by at most the one new
edge; deleting one edge can destroy at most one edge of an old maximum matching,
leaving a matching of size at least `nu-1`.  Adding or removing one owner vertex
has the same argument.  Lexicographic tie-breaking may select a different
alternating path or cycle and hence rotate many assignments while preserving the
same rank.  Fixed orders select the least changed input atom and its direction.
The alphabet count and weighted conclusion are immediate. QED.

Equality of one reset decoration does not identify the complete eligibility graph
or assignment state and is not progress by itself.

## AC3ne -- canonical Hall-core failure output -- PROVED

If `M^*` does not saturate every demand, Hall's theorem gives a nonempty set

\[
X\subseteq D
\]

with

\[
|N_{E[D,T_F]}(X)|<|X|.
\]

Choose first an inclusion-minimal deficient set, then the lexicographically least
one among those of minimum cardinality.  This gives one canonical private-owner
Hall core

\[
\boxed{X^*(D,T,E,F).}
\]

Every complete-assignment failure therefore returns exact demand identities,
its available owner neighbourhood and deficiency

\[
\boxed{\delta(X^*)=|X^*|-|N(X^*)|\ge1.}
\]

The core enters the existing owner-resource, common-owner and many-owner routers.
It is not payment merely because it is deficient.

### Proof

The contrapositive direction of Hall's theorem gives a deficient demand set when
a saturating matching does not exist.  The finite collection of deficient sets
contains an inclusion-minimal member and the fixed orders select one canonically.
The displayed deficiency is a positive integer. QED.

## AC3nf -- persistent capacity consumption has a linear potential -- PROVED

Fix the demand set and eligibility graph inside one owner epoch.  Suppose the
spent masks form a monotone history

\[
F_0\subseteq F_1\subseteq\cdots
\]

and every accepted private-owner transition consumes at least one owner unit of
its selected canonical matching:

\[
(F_{i+1}\setminus F_i)\cap V_T(M_i^*)\ne\varnothing.
\]

Then the number of accepted private-owner transitions is at most

\[
\boxed{|T\setminus F_0|\le m.}
\]

The potential is simply

\[
\boxed{\Xi_{\rm cap}=|F|.}
\]

It strictly increases on every accepted transition even when the recomputed
canonical matching rotates across many unspent owners.

### Proof

Every accepted transition adds at least one previously unspent owner unit to the
persistent mask.  There are only `|T\F_0|` such units.  Matching rotation does not
restore a spent unit and therefore cannot decrease the potential. QED.

If a proposed transition selects an owner but does not consume it, that owner is
`FIXED_CURRENT`, not a capacity-progress step.  If the spent mask can shrink, the
history has left the persistent-capacity epoch and the mask change is an outer
reset.

## AC3ng -- selected-subbank and owner-assignment profile reduction -- PROVED UNDER THE PRIVATE CAPACITY CONTRACT

Assume an installed transition family declares:

- its exact ordered demand set;
- its exact private capacity-unit universe;
- the complete demand--owner eligibility graph;
- one persistent spent mask;
- the canonical assignment policy AC3nc;
- the AC3ke status and faithful destruction or consumption contract for every
  selected edge.

Then:

1. the selected private subbank and assignment are derived from `(D,T,E,F)` and
   need not be independent AC3ka profile coordinates;
2. a complete canonical matching supplies an assignment, but payment is credited
   only on edges whose owner rows are `PAID`;
3. failure returns the canonical Hall core AC3ne;
4. one eligibility, demand or availability change receives the AC3nd atomic reset
   decoration;
5. within a persistent capacity epoch, accepted consuming transitions terminate
   after AC3nf's linear token budget;
6. an assignment change with no changed input is impossible.

### Proof

AC3nc gives deterministic reconstruction and preserves complete-match existence.
AC3ne handles failure.  AC3nd localizes every changed input without asserting a
false matching-distance bound.  AC3nf supplies the monotone capacity potential.
The payment restriction is AC3ke--AC3kf. QED.

## AC3nh -- corrected selected-owner frontier -- PROVED

The following owner-selection fields are removed under AC3ng:

- a separately stored private selected subbank;
- a separately stored private demand--owner assignment;
- matching rotations caused only by the already recorded eligibility or spent
  input change.

The following remain live:

1. the generator of the demand set or eligibility graph;
2. arbitrary noncanonical selected subbanks;
3. shared owners and common-token accounting under AC3w;
4. capacities not decomposed into exact capacity-one units;
5. owner-status or destruction-contract changes;
6. nonpersistent spent masks;
7. recurrent exact input-atom resets outside a consuming epoch.

Thus a surviving owner recurrence must expose the actual changed eligibility,
demand, capacity, owner-status or generator atom.  Repetition of one assignment
reset label still needs current payment, bounded descent, impossibility or a
capacity-one ticket through AC3kd and AC3lc.

### Proof

The removed fields are deterministic outputs of AC3nc.  The remaining fields are
not determined by the canonical private matching inputs or violate the persistent
capacity hypothesis, so no reconstruction or monotone-consumption conclusion
applies. QED.

## Consequence

The private selected-subbank and owner-assignment part of the AC4 set-state
frontier is no longer arbitrary under a canonical capacity-one policy.  Feasible
private assignments are preserved exactly, failed assignments expose one Hall
core, and every paid consuming epoch has at most the number of initially
available owner units many accepted transitions.

The remaining owner frontier consists of eligibility/demand generators, shared
owners, non-unit capacities, status/destruction resets and recurrent exact macro
edges.

## Finite check

`scripts/verify_ac_canonical_owner_assignment.py` exhausts every bipartite graph
with up to three demands and three owner units, every spent mask, all one-edge and
one-token updates, every canonical Hall core and every nonempty capacity
consumption step.  It also preserves explicit examples where one input atom
rotates several assignment pairs while changing the matching rank by at most one.
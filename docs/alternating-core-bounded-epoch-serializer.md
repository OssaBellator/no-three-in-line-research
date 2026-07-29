# Alternating-core bounded physical epoch serializer

## Status

This note keeps AC as the sole active research focus and proves AC5is--AC5iw. It supplies the missing finite object census required by AC5in--AC5ir: one declared bounded physical epoch is serialized into an exact compatibility-pair universe, an exact macro-state universe, an exact deterministic transition universe and a typed boundary frontier.

The result is contract-qualified. It does not choose the physical caps, prove that every global AC trajectory stays in one box, construct the missing geometric compatibility predicates, prove AC6, or prove the no-three-in-line conjecture. It proves that a complete bounded epoch has a canonical finite serialization, that no attempted transition disappears at the boundary, and that cap enlargement preserves all previously certified interior records.

## Bounded epoch record

Fix one complete schema version `v`. A bounded AC epoch record contains:

- a fixed ordered target batch `B=(b_1,...,b_t)` and retained partner pool `P` of size `p_*`;
- a finite ordered repair-job catalogue `J` whose jobs retain complete owner, footprint, cost, witness and epoch fields;
- a finite ordered physical recreation-atom set `A`;
- a finite boundary/controller dictionary `Q` and all owner, zone, phase and restart fields;
- bounded resource coordinates `m_i in {0,...,K_i}`;
- bounded globally addressed payment/source/certificate/ticket/reset balances `c_a in {0,...,C_a}`;
- a bounded tail or absolute-balance coordinate `b in {0,...,H}` together with its finite control and residue fields;
- a finite incidence catalogue `I`, a finite token catalogue `T`, and every predicate field needed to decide compatibility;
- a finite ordered operation dictionary `O`.

A complete operation address includes every physical choice needed to make its update deterministic. Its record contains:

1. the complete precondition;
2. the exact resource and capacity increments;
3. the target, partner, queue, atom and source/certificate edits;
4. the complete footprint and occurrence lineage;
5. any schema or infrastructure change;
6. for each upper resource boundary, either a certified monotone-escape route or the declaration that the exit is an unresolved overflow.

An operation with an omitted physical choice is not deterministic and is rejected before transition enumeration.

## AC5is -- canonical finite state serialization and ambient count -- PROVED

A bounded epoch state retains:

1. a compatible partial injection of the first `j` targets into `P`, for some `0<=j<=t`;
2. an ordered queue of distinct jobs from the catalogue `J`;
3. the active subset of recreation atoms;
4. the complete finite boundary/controller record;
5. the exact tail balance `b` inside the declared box;
6. every bounded resource coordinate;
7. every bounded globally addressed capacity balance.

Let

\[
N_{\rm inj}=\sum_{j=0}^{t}(p_*)_j,
\qquad
N_{\rm queue}=\sum_{k=0}^{|J|}(|J|)_k,
\]

where `(n)_k=n(n-1)...(n-k+1)`. If `F` is the number of complete finite boundary/controller records, the ambient state count is

\[
\boxed{
N_{\rm box}
=
N_{\rm inj}
N_{\rm queue}
2^{|A|}
F(H+1)
\prod_i(K_i+1)
\prod_a(C_a+1).
}
\]

The physically legal state set `V_box` is the subset passing the exact compatibility, queue, lineage, balance and shared-state predicates, so

\[
|V_{\rm box}|\le N_{\rm box}.
\]

The canonical serialization is injective. Omitting the schema version, queue order, physical occurrence, balance address, owner, phase, restart or another retained field returns the least pair of states that collide after that omission.

### Proof

There are `(p_*)_j` unrestricted ordered partial injections of length `j`, and `(|J|)_k` ordered queues of `k` distinct jobs. Active atoms form a subset of `A`. Every other coordinate ranges over its displayed finite set. Multiplication gives the ambient count. Canonical serialization retains every named field and is therefore injective. QED.

## AC5it -- exact bounded compatibility-pair universe -- PROVED UNDER THE PREDICATE CERTIFICATES

For every incidence `i in I` and token `tau in T`, retain the full tagged pair record

\[
(v,i,\tau,\text{owner},\text{track},\text{epoch},\text{support},\text{predicate fields}).
\]

After rejecting the least stale version, omitted field, shared-state disagreement or overlap conflict, evaluate every retained physical predicate. This produces a total bounded evaluator

\[
\operatorname{Compat}_{\rm box}:I\times T\longrightarrow\{0,1\}
\]

and the exact ordered pair universe

\[
\Omega_{\rm box}=I\times T,
\qquad
|\Omega_{\rm box}|=|I||T|.
\]

A restricted physical menu may use a certified subset, but it may not infer a value outside its declared pair records. Two pair records that differ only in an omitted schema, owner, occurrence, source, phase or predicate field are an exact omission witness.

### Proof

The catalogues are finite. Complete field records make every predicate evaluation a finite deterministic computation. The fixed product order selects the first failed record. QED.

## AC5iu -- total deterministic edge compiler and typed boundary completion -- PROVED

For every legal state `x in V_box` and every operation address `o in O`, evaluate the operation using the following ordered router:

1. a changed schema or undeclared infrastructure change returns `reset`;
2. a negative resource result returns the least exact `resource shortage`;
3. a negative payment/source/certificate/ticket balance returns the least exact `capacity shortage`;
4. a balance exceeding its declared physical capacity returns `amplification` with the exact excess;
5. a resource exceeding `K_i` returns the declared `monotone escape` when its certificate is present, and otherwise the exact `bounded overflow`;
6. all remaining updates produce one internal successor `x' in V_box`.

Thus every pair `(x,o)` has exactly one outcome. No attempted operation is silently dropped at the edge of the box.

Let `E_box` be the internal certified edges and `partial_box` the typed noninternal outcome records. Then

\[
|E_{\rm box}|\le |V_{\rm box}||O|,
\qquad
|E_{\rm box}|+|\partial_{\rm box}|=|V_{\rm box}||O|.
\]

Every internal edge retains its source, operation, successor, footprint, resource increments, capacity debits, owner and lineage. Every boundary object retains its source, operation, least failed coordinate and exact shortage, excess or changed field.

### Proof

The complete operation address makes the update deterministic. The ordered router is exhaustive and mutually exclusive because it stops at the first applicable condition. Each state-operation pair therefore contributes one internal edge or one boundary record. QED.

## AC5iv -- canonical historical-template extraction and zero-neighbourhood frontier -- PROVED

Attach complete provenance tags to every object in

\[
\mathcal U_{\rm box}
=
\Omega_{\rm box}\sqcup V_{\rm box}\sqcup E_{\rm box}.
\]

The six historical AC recognizers are:

1. `direct`: complete support, secant, dangerous-line, residual and new-blocker records;
2. `layered`: exact incidence layers, conditioning deletions, endpoint identities and reverse loads;
3. `pool`: initial blockers, paid depletion, new blockers, new-cell sets and charged pair-shadow incidences;
4. `repair`: occurrence-faithful defect uses, slots, repair extensions and source-compatible repair tokens;
5. `flow`: physical source, issued-source, certificate and defect network records;
6. `recurrence`: low-buffer lineages, recreation atoms, finite guards, residue phases and tail tables.

For each complete template instance, its coverage set is exactly the objects whose full provenance satisfies that recognizer. Prerequisites and capacity references are inherited from the retained source records. These sets are valid candidates for AC5in--AC5ip.

For an object `x`, let `N(x)` be the set of complete template instances recognizing it. If `N(x)=empty`, the serializer returns `x` with its full physical record as the next zero-neighbourhood construction target. An object is never assigned to a template merely because its untagged shape resembles another object.

### Proof

Each recognizer is a finite predicate on complete serialized provenance. Candidate coverage and prerequisite records are therefore finite and exact. The empty-neighbourhood test is finite set membership. QED.

## AC5iw -- nested-box refinement and no-regression theorem -- PROVED

Let two epoch boxes have the same schema, dictionaries and physical interpretation, with coordinatewise larger caps

\[
K_i\le K_i',
\qquad
C_a\le C_a',
\qquad
H\le H'.
\]

Then:

1. every old state has the identical serialization in the larger box;
2. every old compatibility pair has the identical evaluator value;
3. every old internal transition remains the identical internal transition;
4. an old shortage or reset record remains identical;
5. an old amplification, overflow or monotone-escape record either remains a boundary record of the same physical operation or refines to its exact internal successor;
6. no previously certified internal object is invalidated solely by cap enlargement.

The new state shell has exact ambient size

\[
N_{\rm shell}=N_{\rm box}'-N_{\rm box}.
\]

The next census consists of the new shell objects plus the old boundary records that refine or remain unresolved. Global capacity addresses retain their identities; raising a physical capacity requires one named deposit or cap certificate and does not duplicate the old address.

Consequently one may enlarge a bounded AC epoch monotonically: all old interior template certificates remain reusable, while only the exact shell and boundary-refinement queue require new construction.

### Proof

Every old coordinate value lies in the larger box and every dictionary field is unchanged, giving identical state and pair records. An update that stayed inside the old caps also stays inside the larger caps with the same arithmetic successor. Lower-bound failures and schema changes do not depend on upper caps. Upper-bound outcomes may cease to be boundary events only when their exact successor enters the enlarged box. The product count gives the shell formula. QED.

## Bounded-epoch output

A complete serializer returns

\[
(\Omega_{\rm box},V_{\rm box},E_{\rm box},\partial_{\rm box},\mathcal K_{\rm cand}),
\]

where `K_cand` is the finite historical-template candidate registry. The interior universe

\[
\Omega_{\rm box}\sqcup V_{\rm box}\sqcup E_{\rm box}
\]

may be passed directly to AC5in--AC5ir. Boundary records are not silently declared physical edges; they are terminal routes, exact obstructions or the ordered expansion frontier.

## Deterministic audit

`scripts/verify_ac_bounded_epoch_serializer.py` checks 2,500 generated bounded epochs. It verifies:

- the partial-injection and ordered-queue count formulas;
- the exact product state bound;
- total compatibility-pair serialization and omitted-field collision witnesses;
- the six-way operation router;
- one outcome for every sampled state-operation pair;
- preservation of every old internal edge under cap enlargement;
- refinement or persistence of every upper-bound boundary event;
- exact shell-state counts;
- complete historical-template candidate neighbourhoods or exact zero-neighbourhood objects.

## Main AC frontier

Only AC remains active. The next physical tasks are:

1. choose the first actual bounded AC schema and cap vector;
2. serialize its concrete menu, queue, resource, source/certificate and recurrence records;
3. compile its exact `Omega_box,V_box,E_box,partial_box`;
4. instantiate the six historical template recognizers;
5. run AC5in--AC5ir on the resulting physical census;
6. discharge zero-neighbourhood interior objects;
7. classify every boundary record as terminal, paid, monotone escape, rigid obstruction or cap-expansion target;
8. enlarge the box using AC5iw without discarding old interior proofs.

AC6 and the global no-three-in-line conjecture remain open.

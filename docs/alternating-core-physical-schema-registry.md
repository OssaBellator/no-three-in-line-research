# Alternating-core physical schema registry

## Status

This note keeps AC as the sole active research focus and proves AC5kn--AC5ks. It begins physical population of the seven-section initial-state manifest of AC5kh--AC5km. The historical alternating-core chain already determines which state fields are physical inputs and which are deterministic reconstructions. This note compiles that distinction into one canonical prime-minus-one schema record.

The result does not supply the missing geometric exclusion predicates, complete target corrections, physical source arcs, or reachable operation graph. It does not prove AC6 or the no-three-in-line conjecture. It completes the manifest's schema normal form and returns an exact field witness whenever a proposed initial record is incomplete, inconsistent, or stores a derived value as independent data.

## Prime-minus-one physical schema

Fix an odd prime `p`, put

\[
n=p-1,
\]

and work on the `n x n` board with two permutation layers. Fix the least primitive root `gamma` of `F_p^*`, all physical-address orders, and one schema version.

The immutable schema dictionary contains:

1. the board and two-layer cell universes;
2. the red and blue permutation-variable dictionaries;
3. hard, protected, factor, owner, source, certificate, ticket, reset and operation kinds;
4. the six historical template-recognizer kinds `direct`, `layered`, `pool`, `repair`, `flow`, `recurrence`;
5. the six transition-relative owner routes `PAID`, `FIXED_CURRENT`, `PROSPECTIVE`, `OCCURRENCE_FAILURE`, `COHERENCE_MISMATCH`, `OWNER_RESET`;
6. all total orders used for canonical least witnesses;
7. the prime-field and determinant conventions used by the BDA and RI reconstructions.

A physical initial record contains two current permutations, an AN4 neutralization bank of size `t>=7`, the current star and exact rank-one through rank-three certificate ledgers, and the live generators listed below.

## Derived and live fields

The following fields are **derived** when their historical contracts are declared.

| Derived field | Complete retained inputs |
|---|---|
| canonical active host | base-support generator output, exact one-cell exclusion registry, exact context assignment |
| maximal protected registry | exact physical state, protected-atom dictionary, protection context |
| private and common repair envelopes | exact finite local-state families and common states |
| determinant-realized BDA denominator, directions and residue profile | physical board directions and determinant occurrences |
| prime-field RI subgroup, coset, root, image, companion and scale labels | physical occurrence `(a,b,x,u,z)`, subgroup order `h`, fixed primitive-root convention |
| canonical private selected subbank and owner assignment | ordered demand set, capacity-one owner units, exact eligibility graph, persistent spent mask |

The following remain **live generator data** unless a later theorem reconstructs them:

1. the base-support generator and arithmetic/physical context;
2. the exact exclusion registry and context literals;
3. the local-state or transition-family generator;
4. discretionary partner filters or nonmaximal protected subbanks;
5. global or unbounded-scope contracts;
6. the source-coset family generator and the assignment of physical occurrences to RI components;
7. exact target-menu complete states and their executable/forbidden/reset/open partition;
8. shared owners, non-unit capacities and owner destruction contracts;
9. transition-relative owner-status rows;
10. resource, source, certificate, disturbance, recreation and reset dictionaries;
11. the complete deterministic operation dictionary.

A derived field may be cached for audit convenience, but the cache is accepted only when it equals its reconstruction and is excluded from the canonical schema digest.

## AC5kn -- canonical prime-minus-one initial schema -- PROVED UNDER THE HISTORICAL INPUT CONTRACTS

A proposed physical initial schema is accepted only when:

1. `p` is an odd prime and `n=p-1`;
2. the primitive-root convention agrees with the declared least primitive root;
3. both current layers are permutations of the same `n` symbols;
4. the neutralization bank has size at least seven;
5. all physical dictionaries and fixed witness orders are finite and versioned;
6. every live field has one complete physical address and interpretation;
7. every BDA or RI arithmetic name is accompanied by its required physical realization rather than appearing only as an abstract symbol.

These checks define a canonical initial-schema serialization. Their failure returns the least of: a prime-minus-one mismatch, primitive-root mismatch, malformed permutation layer, undersized bank, stale or infinite dictionary, omitted live field, or unrealized arithmetic label.

### Proof

Each condition is a finite predicate on the complete record. The prime-minus-one and permutation conditions identify the intended board and two-layer state. The AN4 chain requires `t>=7`. Fixed finite dictionaries and physical realization are exactly the prerequisites of the bounded serializer, determinant BDA reconstruction and prime-field RI reconstruction. The fixed product order selects the first failure. QED.

## AC5ko -- exact derived-field reconstruction and reduced digest -- PROVED

For every accepted live record, reconstruct:

\[
A_{\rm can}=G\setminus\{z:\text{an active one-cell exclusion targets }z\},
\]

\[
P_j^{\min}=\bigcup_{S\in\mathcal X_j}S,
\]

the maximal protected registry when the maximal policy is declared, every determinant-reduced BDA profile, every RI quotient address, and the lexicographically least maximum private-owner matching.

Let

\[
D_{\rm red}=H(\text{immutable schema},\text{live generators})
\]

be the canonical digest. Then:

1. every derived field is a deterministic function of the data inside `D_red`;
2. two accepted reduced records with equal digests reconstruct identical derived fields;
3. changing only a cached derived value does not change `D_red` and returns the least cache mismatch;
4. changing a genuine live field changes the reduced serialization and therefore its digest;
5. storing a second independent copy of a derived set, quotient label or private matching is forbidden schema duplication.

### Proof

Active-host reconstruction is cellwise Boolean evaluation. Minimal envelopes are exact unions. Determinant reduction and the prime-field quotient formulas are deterministic arithmetic. The private owner assignment is the unique lexicographically least maximum matching. Hence all derived values are functions of the reduced record. Canonical serialization and collision-resistant digest notation are used only as equality interfaces: equality of serialized inputs implies equality of every reconstruction. A mismatching cache is directly witnessed by the least differing derived field. QED.

## AC5kp -- live-field guardrail and exact change localization -- PROVED

No polynomial-state or recurrence conclusion is inferred merely because a live field is a subset of a finite physical atom universe. In particular, arbitrary filters, nonmaximal protected subbanks, transition-family generators and global contracts remain exact live fields.

For two accepted reduced records, every change has a least live cause in this ordered list:

1. board, prime, schema or dictionary;
2. one permutation entry;
3. neutralization-bank or current-star data;
4. base-support generator, exclusion atom or context literal;
5. local-state generator, target-completion or legality record;
6. physical BDA or RI occurrence;
7. demand, eligibility, owner, capacity or spent-mask input;
8. source, certificate, ticket, disturbance, reset or operation record;
9. discretionary filter, shared owner or global contract.

A derived output that changes while none of its listed inputs changes is an exact reconstruction failure. Repetition of one live-change label is not automatically progress; it must enter the rank, exceptional-ledger or boundary router.

### Proof

The live fields form a finite ordered serialization. Distinct serializations have a first differing component. AC3lv's set-profile guardrail forbids replacing an arbitrary live subset by its atom count, while AC3ml, AC3mf, AC3my and AC3nc identify the derived-output/input dependencies. QED.

## AC5kq -- transition-relative owner and menu schema rows -- PROVED

Every target alternative and owner claim in the initial schema is recorded transition-relatively.

For one target value, a complete menu state retains its centre assignment, residual correction, both permutation layers, opposite-layer repairs, minimal envelope, paid-token union, reverse tickets and owner-status rows. A target lacking any of these records is `open`, not executable.

For one owner token `pi` and proposed transition `T`, the schema retains

\[
(\pi,T,\kappa,\texttt{current},\texttt{physical},\texttt{coherent},\texttt{payable}).
\]

Payment is accepted only on a `PAID` row backed by faithful destruction or capacity consumption. A current untouched token is `FIXED_CURRENT`; absent-target geometry is `PROSPECTIVE`; physical and coherence failures retain their exact witnesses. Changing the transition, physical scale, assignment or destruction contract changes the live owner row and therefore the reduced digest.

### Proof

Alternative states are menu choices, not simultaneous factors, so legality and payment are checked per complete state. Owner payability depends on the proposed transition, not the owner name alone. These are precisely the historical AC3ki and AC3ke contracts. QED.

## AC5kr -- cap-only refinement preserves the schema digest -- PROVED

Consider a nested box refinement that changes only numerical upper caps on already declared resource, balance and tail coordinates. If the prime, physical dictionaries, live generators, operation meanings and physical address interpretations are fixed, then `D_red` is identical at every level.

Consequently:

1. all reconstructed active hosts, envelopes, arithmetic labels and canonical owner policies retain their meanings;
2. old live records retain identical addresses;
3. the schema section of the AC5kh manifest is reused verbatim;
4. shell work begins at the serializer section;
5. introduction of a new filter, owner kind, source class, operation, lineage, arithmetic interpretation or physical atom is a schema/dictionary boundary, not cap enlargement.

### Proof

Numerical cap values belong to the bounded serializer profile, not to the immutable physical schema or live generator dictionaries. The reconstruction formulas contain no current upper cap as an address-generating field. Therefore cap-only refinement leaves the reduced serialization unchanged. Any newly introduced dictionary object changes a live or immutable field and is detected before serialization. QED.

## AC5ks -- completed schema section of the initial-state manifest -- PROVED

For a proposed AC initial state, run AC5kn--AC5kq in dependency order. The compiler returns exactly one of:

1. an accepted reduced schema record, its canonical digest and all reconstructed audit caches;
2. the first malformed immutable field;
3. the first omitted or contradictory live generator;
4. the first unrealized BDA or RI arithmetic label;
5. the first derived-cache mismatch or duplicated derived field;
6. the first incomplete target-menu state or unsafe owner-status row.

On the accepted branch the `schema` section of AC5kh is complete. Later frontier repairs that leave this digest unchanged begin recompilation at `serializer`; a repair changing the digest is an explicit schema revision.

### Proof

AC5kn validates the immutable and initial physical record. AC5ko reconstructs every declared derived field. AC5kp and AC5kq validate the remaining live and transition-relative data. Their finite failure orders combine into the displayed first-witness router. AC5ki then gives monotone manifest refinement. QED.

## Deterministic audit

`scripts/verify_ac_physical_schema_registry.py` checks 2,500 generated prime-minus-one schemas. It verifies:

- both permutation layers and the `t>=7` bank condition;
- active-host and minimal-envelope reconstruction;
- determinant-reduced BDA profiles and their physical denominator bound;
- prime-field RI root, image, companion and scale quotient reconstruction;
- canonical private-owner matching and selected-subbank reconstruction;
- reduced-digest invariance under derived-cache mutation;
- reduced-digest sensitivity to genuine live-field changes;
- exact prime-minus-one, bank, permutation, BDA, RI and schema-digest failure routes.

## Main AC frontier

Only AC remains active. The schema section is now populated at the level justified by the historical chain. The next physical tasks are:

1. instantiate the reduced record with the actual initial red/blue permutations, neutralization bank and current star;
2. enumerate the concrete target-menu complete states and live operation dictionary;
3. serialize the reachable successors from those operations;
4. populate the direct, layered, pool, repair, flow and recurrence rows;
5. run the remaining six manifest sections;
6. discharge the first returned physical witness.

AC6 and the global no-three-in-line conjecture remain open.

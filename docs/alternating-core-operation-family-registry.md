# Alternating-core physical operation-family registry

## Status

This note keeps AC as the sole active research focus and proves AC5kt--AC5ky. It populates the operation-dictionary input required by the bounded serializer and the `serializer` section of the initial-state manifest. The registry is extracted from the historical target-menu, repair, source/certificate, resource-cycle, recreation, periodic-tail and outer-reset interfaces.

The result does not enumerate the actual geometric instances of these operations or prove their preconditions. It proves that every accepted operation belongs to one complete physical family, has one deterministic occurrence address and one exact untruncated successor, and cannot change meaning under numerical cap refinement.

## Common operation header

Every physical operation record retains:

1. schema version and epoch;
2. one operation-kind tag;
3. one globally unique operation address and one occurrence address;
4. its complete source-state precondition;
5. its complete touched footprint;
6. owner, source and recreation lineage fields;
7. exact resource and globally addressed balance increments;
8. queue, target, partner, atom, controller and schema edits;
9. its complete finite successor vector before cap truncation;
10. every payment, ticket, disturbance or funded-reset debit.

A field that influences legality or the successor but is absent from the address is an omitted physical choice and makes the operation nondeterministic.

## Ten physical operation families

| Kind | Required kind-specific fields |
|---|---|
| `install` | target, retained partner, complete target-state address |
| `repair` | exact defect, occurrence-faithful slot, live repair token |
| `flow` | physical source, issued source, certificate, exact defect class |
| `payment` | transition-relative owner token, exceptional claim address, amount |
| `resource` | macro address, complete increment vector, lower/guard row |
| `recreation` | physical atom, decorated restoration edge, recreation ticket |
| `tail` | control, residue, increment, lower requirement and table version |
| `disturbance` | event atom, disturbance weight and physical provenance |
| `reset` | least changed schema/profile field, target interpretation, funded reset address |
| `terminal` | exact terminal predicate and final physical state digest |

The family tag is not inferred from a similar effect vector. For example, a resource increment caused by an exogenous event remains `disturbance`, and a current owner debit remains `payment` even if it also changes a resource coordinate.

## AC5kt -- complete historical operation-family partition -- PROVED

Under the historical AC contracts, every accepted state-changing event belongs to exactly one of the ten families above after applying this ordered classifier:

1. terminal completion;
2. schema or interpretation reset;
3. declared external disturbance;
4. physical source/certificate flow;
5. transition-relative payment debit;
6. recreation/restoration;
7. periodic-tail controller step;
8. resource-only macro step;
9. occurrence-slot repair;
10. complete target installation.

An event satisfying two classes is rejected unless the record declares one primary physical occurrence and represents the other effect inside its complete effect vector. An event satisfying none is an unclassified operation witness.

### Proof

The historical target, repair, flow, payment, recurrence and reset interfaces cover the listed physical events. The fixed ordered classifier makes the tags disjoint. Complete effect records preserve simultaneous secondary changes without duplicating the primary operation occurrence. QED.

## AC5ku -- deterministic operation address and omission witness -- PROVED

Fix one source state and one complete accepted operation address. Its precondition and effect record determine exactly one of:

1. an exact internal successor;
2. the least resource shortage;
3. the least capacity/source/certificate/ticket shortage;
4. the least physical-capacity amplification;
5. the least unresolved upper overflow;
6. a certified monotone escape;
7. a reset or terminal route.

If two physical completions of the same purported address give different successors or routes, the compiler returns the least omitted field on which they differ. The witness may be a target, partner, slot, source, certificate, owner, lineage, increment, guard, controller value, reset address or terminal state.

### Proof

The common header and kind-specific fields contain every physical choice and every arithmetic update before cap comparison. Applying the ordered boundary router is deterministic. Distinct completions with different outputs have a first differing retained physical choice; its omission is the stated witness. QED.

## AC5kv -- occurrence identity, nonaliasing and one-use accounting -- PROVED

Operation addresses are typed. Two records with different family tags, source states, owners, source lineages, restoration edges or event atoms are distinct even when their effect vectors coincide.

A globally exceptional occurrence is keyed by its complete operation occurrence together with its physical source and claim address. Repeated template references to that key are aliases and contribute no additional stock. Reusing one exhausted occurrence, relabelling it into another family or assigning conflicting effect records returns the least address conflict.

### Proof

Canonical tagged serialization makes equality fieldwise. The global exceptional source quotient counts physical occurrences rather than references, so aliases collapse to one key. Conflicting records violate equality of the serialized operation object. QED.

## AC5kw -- exact precondition/effect and footprint contract -- PROVED

For every operation, the compiler verifies:

1. the source state satisfies every declared precondition;
2. all lower requirements and availability guards are checked before the update;
3. the displayed resource and balance deltas equal the kind-specific arithmetic data;
4. every queue, atom, target, partner and controller edit is listed in the effect record;
5. the footprint contains every changed physical cell, owner, source, certificate, atom and controller address;
6. the successor satisfies the fixed-schema legality predicates or is routed to the least failed predicate.

Two operations may commute or be batched only through a separate footprint/legality theorem. Disjoint effect vectors without a complete physical footprint are insufficient.

### Proof

Each item is finite equality, membership or predicate evaluation on the source and operation records. The effect vector supplies the candidate successor, and the legality dictionary either accepts it or identifies the first failed row. QED.

## AC5kx -- cap-invariant successor exposure -- PROVED

Let one accepted operation at an interior source state have complete untruncated successor vector

\[
s(v,o)=(s_1,\ldots,s_d).
\]

For a current cap vector `L`, the unique least cap vector making this operation internal is

\[
L_i^+(v,o)=\max(L_i,s_i(v,o)).
\]

Under every fixed-schema cap refinement dominating `L^+(v,o)`, the same source state and operation address produce the identical physical successor and footprint. A previous upper-bound record either persists or refines to this exact successor; its operation identity does not change.

### Proof

The successor is computed before cap comparison. Membership in the enlarged box is coordinatewise domination. AC5iw preserves the source and physical interpretation, while the operation address contains no current upper cap as a semantic field. QED.

## AC5ky -- operation-registry compiler and serializer input -- PROVED

Given a proposed finite operation dictionary, the compiler:

1. checks every common and kind-specific field;
2. rejects duplicate typed addresses or conflicting occurrence records;
3. verifies precondition/effect consistency and complete footprints;
4. computes the untruncated successor for every legal source-state/operation pair;
5. records every internal or typed boundary route;
6. returns the first missing physical choice when determinism fails.

On the accepted branch, the operation-family registry and its exact successor vectors are a complete input to AC5iu, AC5kb and the `serializer` section of AC5kh. The output is otherwise the least unclassified kind, omitted field, address collision, effect mismatch, footprint omission or stale schema record.

### Proof

AC5kt supplies the exhaustive kind partition, AC5ku supplies determinism, AC5kv supplies address uniqueness, AC5kw verifies effects and footprints, and AC5kx supplies cap-stable successor exposure. Their fixed failure orders combine into the stated compiler. QED.

## Deterministic audit

`scripts/verify_ac_operation_family_registry.py` checks 2,500 generated operation registries. It verifies all ten kinds, deterministic repeated execution, exact effect arithmetic, typed address nonaliasing, fixed-schema cap refinement and one first omitted-field witness for every kind.

## Main AC frontier

Only AC remains active. The next physical work is:

1. instantiate the ten families with the actual historical target, repair, source, resource, recreation, tail and reset records;
2. enumerate the complete operations enabled at the chosen initial state;
3. compute their exact successors and boundary routes;
4. begin the fair reachable expansion and populate the six historical template row families;
5. discharge the first missing operation or physical-row witness.

AC6 and the global no-three-in-line conjecture remain open.

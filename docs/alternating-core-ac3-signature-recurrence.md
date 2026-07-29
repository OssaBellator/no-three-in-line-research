# Alternating-core AC3 physical signature recurrence compiler

## Status

This note keeps AC as the sole active research focus and proves AC5lr--AC5lw. It continues the physical AC2 compiler by giving every carry, centre, bounded-denominator and rational-inverse continuation one exact physical signature, separating first exposure from reuse, assigning occurrence-faithful reuse and reopening tickets, and returning a canonical unticketed directed cycle whenever no valid progress route exists.

The result does not construct the missing physical ticket sources for every repeated signature. It proves the finite registry, exact reuse accounting, strict support descent and cycle obstruction compiler once the physical signature and source records are supplied.

## Physical signature registry

The fixed-schema registry contains six tagged signature kinds.

1. **Product carry:** channel word and bounded integer pair `(j_b,j_c)`.
2. **Cross carry:** anchor/channel word and exact carry level.
3. **Coordinate carry:** axis, endpoint role and exact coordinate-carry level.
4. **Wrap centre:** reduced rational numerator/denominator and physical anchor.
5. **BDA profile:** determinant-realized denominator, directions, scalar residue, physical occurrence and owner route.
6. **RI profile:** subgroup order, physical occurrence, source-component word, reconstructed quotient addresses and owner route.

Every signature also retains schema version, epoch, producing operation, current/prospective status and complete provenance. Equality means equality of every tagged physical field; a similar arithmetic value in another kind is not the same signature.

## AC5lr -- finite occurrence-faithful signature normal form -- PROVED

Under the fixed physical dictionaries and the determinant/prime-field reconstruction contracts, every accepted AC2 carry, centre, BDA or RI continuation has one canonical signature address in the registry above.

The compiler returns the least of:

1. an out-of-range integer or unreduced rational field;
2. a BDA denominator without determinant realization;
3. an RI quotient label without its physical occurrence and subgroup order;
4. an omitted channel, anchor, owner route, source component or epoch;
5. two records assigning different meanings to one signature address;
6. one record tagged simultaneously by two signature kinds.

On the accepted branch the signature universe is finite for one fixed board and schema.

### Proof

Product, cross, coordinate and centre signatures use finitely bounded integer and physical dictionaries. BDA profiles use the determinant bound and RI profiles use the prime-field occurrence reconstruction. Tagged canonical serialization makes the union disjoint and selects the first malformed field. QED.

## AC5ls -- monotone exposure ledger and exact first-use route -- PROVED

Let `Sigma` be the accepted signature universe and let `E` be the set exposed so far. For a transition producing signature `sigma`:

- if `sigma notin E`, insert it and classify the transition as `first exposure`;
- if `sigma in E`, classify it as `reuse` and do not increase the exposure count.

The potential

\[
\Xi_{\rm exp}=|E|
\]

strictly increases on every first exposure and never decreases. Re-encountering an existing address is not progress, even when its producer, target object or local matching differs.

### Proof

The ledger update is set union. A new member increases cardinality by one and an existing member does not. Signature equality includes all fields declared by AC5lr. QED.

## AC5lt -- occurrence-faithful reuse tickets and paid/delegated reuse -- PROVED

Every repeated signature transition must take exactly one of these routes:

1. consume one previously unused physical reuse ticket addressed by the signature, operation occurrence, owner/source lineage and epoch;
2. destroy or consume one current `PAID` owner occurrence;
3. enter one determinant-realized BDA or physical RI delegation with its complete owner and source records;
4. return an unticketed reuse edge.

Let `R_sigma` be the number of physical tickets declared for signature `sigma`. The ticket potential

\[
\Xi_{\rm ticket}=|E|+\sum_{\sigma}c_\sigma,
\qquad 0\le c_\sigma\le R_\sigma,
\]

strictly increases on first exposure or ticketed reuse. A ticket cannot be reused, split into aliases or replenished without a named deposit/reset.

### Proof

First exposure increases `|E|`. Ticketed reuse increments one bounded counter. Paid/delegated routes leave through their own exact compiler. Occurrence-faithful ticket addresses and the global source ledger forbid reuse or alias duplication. QED.

## AC5lu -- canonical unticketed-cycle extraction -- PROVED

Collapse states with the same complete exposure and ticket data. Form the finite directed graph `Q_old` of transitions that:

1. carry only previously exposed signatures;
2. consume no reuse ticket;
3. supply no current payment or accepted BDA/RI delegation;
4. remain nonterminal inside the same fixed schema.

Exactly one of the following occurs:

1. `Q_old` is acyclic, in which case reverse topological path length gives a strict finite rank;
2. the compiler returns the least nontrivial strongly connected component or self-loop and its least directed cycle.

No choice of scalar weights on the same unchanged exposure fields can make every edge of the returned cycle strictly progressive.

### Proof

A finite directed graph admits a strict integer topological rank exactly when it is acyclic. Strongly connected component decomposition finds a cycle precisely when acyclicity fails. Strict inequalities around a cycle would give a value strictly less than itself. QED.

## AC5lv -- strict labelled-support descent and reopening contract -- PROVED

For an AC2 labelled recursive overload, let `U` be the current structural object universe and replace it by

\[
U'=S_\lambda(o)\subseteq U\setminus\{o\}.
\]

Then

\[
\Xi_{\rm supp}=|O|-|U|
\]

strictly increases. A pure recursive epoch has at most `|U_0|-1` descents.

If a previously discarded object is reintroduced, the transition must consume one occurrence-faithful reopening ticket or take a paid/delegated/reset route. Reintroduction without such a record is returned with the object, label, previous deletion occurrence and attempted reopening edge.

### Proof

The recursive class excludes its centre, so its universe strictly shrinks. Reintroducing a deleted object reverses that monotone potential and therefore requires an independent finite resource or outer route. QED.

## AC5lw -- complete AC3 no-recycling compiler -- PROVED

For every successful AC2 continuation, run AC5lr--AC5lv. The output is exactly one of:

- a first physical signature exposure;
- a ticketed signature reuse;
- a current paid reuse;
- an accepted BDA or RI delegation;
- a strict labelled-support descent;
- a ticketed reopening;
- a terminal or funded-reset route;
- a canonical unticketed signature cycle;
- the first malformed signature, duplicate ticket, missing owner/source record or unticketed reopening.

Every accepted transition becomes either a progress or exceptional edge for the global ordinal manifest. Every returned cycle retains all physical signature, operation, owner and source addresses required for the next cycle-payment or impossibility theorem.

### Proof

AC5lr serializes signatures, AC5ls separates exposure from reuse, AC5lt handles finite reuse resources and paid/delegated exits, AC5lu handles residual cycles and AC5lv handles recursive support. Their routes are exhaustive for the AC2 output dictionary. QED.

## Deterministic audit

`scripts/verify_ac_ac3_signature_recurrence.py` checks 2,500 generated physical signature systems. It verifies all six signature kinds, first exposures, ticketed and paid/delegated reuse, canonical SCC cycles, strict support descent, ticketed reopening and exact malformed/ticket failures.

## Main AC frontier

Only AC remains active. The next physical tasks are:

1. enumerate the actual carry, centre, BDA and RI signatures reached from the AN/AC2 path;
2. construct every declared reuse and reopening ticket from the global source network;
3. classify each returned unticketed cycle by payment, arithmetic descent, physical impossibility or a new ticket;
4. stratify the accepted transitions in the ordinal manifest;
5. continue fair reachable expansion.

AC6 and the global no-three-in-line conjecture remain open.

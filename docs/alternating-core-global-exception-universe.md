# Alternating-core global exceptional occurrence universe

## Status

This note keeps AC as the sole active research focus and proves AC5jv--AC5ka. It discharges the abstract finiteness interface AC5jr under one fixed-schema physical registry: every payment, low-buffer ticket, recreation ticket, disturbance and funded reset is assigned through one integral physical-source network, so an underlying source capable of funding several exception types is counted only once.

The result remains contract-qualified. It does not construct the actual source-to-exception compatibility graph, prove the fixed-schema hypothesis globally, prove the repair-rank extension or edge stratification, prove cofinality, prove AC6, or prove the no-three-in-line conjecture.

## Exceptional registry contract

Fix one AC schema version with finite physical dictionaries. Retain five tagged exceptional claim families:

1. obstruction and repair payments;
2. low-buffer threshold tickets `(i,h,u)` with `0<=h<beta_i`;
3. recreation tickets `(a,e,lambda)` from the fixed atom and decorated restoration-edge dictionaries;
4. declared disturbance occurrences;
5. funded reset occurrences.

Every claim has a complete physical address, one finite multiplicity and one type. Let `A_exc` be their disjoint tagged union after exact address deduplication.

Let `S_phys` be the finite set of physical source occurrences. Source `s` has stock `b(s)`. A direct ticket or reset with its own independent stock is represented by a dedicated physical source node; a shared source that can fund several claim types appears only once. Retain the exact compatibility relation

\[
K\subseteq S_{\rm phys}\times A_{\rm exc}.
\]

Every exceptional event consumes one source unit and one compatible claim occurrence.

## AC5jv -- finite fixed-schema exceptional claim registry -- PROVED

The low-buffer claim stock has the exact ambient bound

\[
T_{\rm low}
=\sum_i\sum_{h=0}^{\beta_i-1}U_{i,h}.
\]

For a finite recreation-atom set `A`, decorated restoration-edge set `E_rec` and complete lineage decorations already included in the edge records,

\[
T_{\rm rec}\le |A||E_{\rm rec}|.
\]

The payment, disturbance and reset claim sets are finite because their obstruction, event and reset dictionaries are finite in the fixed schema. Therefore `A_exc` is finite.

If one address appears under two tags, carries two stocks, omits its lineage, changes schema version or is introduced without belonging to one of the five declared dictionaries, the least address discrepancy is returned before stock compilation.

### Proof

The threshold levels are restricted to the fixed finite ranges `0<=h<beta_i`; every ticket is addressed by a finite coordinate, level and lineage occurrence. Recreation addresses are finite products. The remaining claim families are finite dictionaries by contract. Exact tagged serialization decides alias equality and discrepancies. QED.

## AC5jw -- integrated physical-source exceptional flow -- PROVED

Construct the integral network

\[
\text{source}
\longrightarrow S_{\rm phys}
\longrightarrow A_{\rm exc}
\longrightarrow \text{sink}
\]

with capacities:

- `b(s)` from the super-source to physical source `s`;
- infinite or declared compatibility capacity on `s -> a` exactly when `(s,a) in K`;
- claim multiplicity `c(a)` on `a -> sink`.

Let `F_exc` be its maximum integral flow. Then `F_exc` is the exact maximum number of exceptional event occurrences that can be assigned simultaneously to distinct physical source units and distinct claim occurrences.

Every physical exceptional trajectory has at most

\[
\boxed{F_{\rm exc}}
\]

source-backed exceptional events.

A failed attempt to realize a declared exceptional multiset returns the canonical minimum source/claim cut and its exact unmatched exceptional demand.

### Proof

An occurrence-faithful exceptional history gives an integral flow by sending one unit through the consumed physical source and claim address. Conversely every integral flow decomposes into source--claim unit paths and therefore gives a legal one-use assignment. Max-flow/min-cut gives the exact optimum and canonical deficient cut. QED.

## AC5jx -- cross-type source conservation and no double use -- PROVED

At every time,

\[
\text{live physical source mass}
+
\text{exceptional mass already consumed}
=
\text{initial physical source mass}
+
\text{named deposits}.
\]

The equality is global across all five exceptional types. A physical source unit used for a payment cannot later be reused for a recreation ticket, reset or disturbance merely because those claims belong to different template families.

Consequently the sum of separately optimized typewise stocks is generally invalid. The integrated value `F_exc` is the correct source-backed quotient. Source splitting, claim splitting, alias relabelling, source-less exceptional creation and unrecorded deposits return the first exact physical source and operation.

### Proof

Legal source transitions preserve mass. Every exceptional event transfers one source unit to the consumed ledger. The type tag records the destination but does not create new source mass. QED.

## AC5jy -- cap-invariance of the exceptional universe -- PROVED

Consider any nested tower obtained only by increasing the numerical state caps of AC5iw while preserving the schema, physical dictionaries and address interpretation.

Then `S_phys`, `A_exc`, their stocks and the compatibility relation `K` are identical at every level. In particular:

- low-buffer addresses use the fixed thresholds `beta_i`, not the enlarged resource caps;
- recreation addresses use the fixed atom and decorated-edge dictionaries;
- obstruction classes, source classes, reset addresses and event atoms do not multiply with the number of states;
- refined boundary operations reuse their original operation and occurrence addresses.

Hence `F_exc` is level-independent.

If cap enlargement introduces a new source, claim, lineage, obstruction class, reset address or event atom, the transition is a schema/dictionary enlargement and returns reset or a new-schema tower boundary. It is not an ordinary cap refinement.

### Proof

AC5iw changes only coordinate ranges. Every exceptional address is defined by a fixed dictionary entry and complete physical lineage, none of which contains the current upper cap as an address-generating field. Thus the network serialization is unchanged. QED.

## AC5jz -- complete global exceptional bound -- PROVED UNDER THE FIXED REGISTRY

Let direct claim occurrences whose dedicated sources are already included in `S_phys` be part of the AC5jw network. Then the complete globally deduplicated exceptional stock is

\[
\boxed{C_{\rm exc}=F_{\rm exc}.}
\]

If a modelling convention keeps some independent, provably disjoint claim stocks outside that network, let their unique-address sum be `C_ind`; then

\[
C_{\rm exc}=F_{\rm exc}+C_{\rm ind}.
\]

Every physical trajectory contains at most `C_exc` exceptional edges. Repeated template references, repeated box references and several compatible exception types do not increase this bound.

The compiler outputs exactly one of:

1. the finite global registry, integrated max flow and canonical source assignment;
2. a malformed or conflicting address;
3. a canonical unpaid source/claim cut;
4. a duplicate debit or unrecorded deposit;
5. a new exceptional address introduced by a supposed cap-only refinement.

### Proof

AC5jw bounds all source-backed events, AC5jx forbids cross-type reuse, and AC5jy makes the network level-independent. Any outside stock is added only after proving physical disjointness. QED.

## AC5ka -- fixed-schema ordinal termination reduction -- PROVED

Assume:

1. the physical box tower is cofinal and fixed-schema;
2. repair ranks extend overlap-preservingly;
3. every internal edge passes AC5jp;
4. the exceptional registry passes AC5jv--AC5jz;
5. all noninternal boundary records pass AC5jh.

Then AC5js applies with the explicit finite exceptional bound `C_exc`. No uniform maximum of deficit, restart potential or repair rank is required.

Thus, under a fixed physical schema, the remaining qualitative route to AC6 consists only of:

- constructing the global repair rank;
- stratifying every internal physical edge;
- proving cofinality;
- discharging the exact source/claim or boundary witnesses returned by the compilers.

### Proof

AC5jz supplies the finite exceptional hypothesis of AC5jr. The other assumptions are exactly the remaining hypotheses of AC5js. QED.

## Deterministic audit

`scripts/verify_ac_global_exception_universe.py` checks 2,500 generated registries. It verifies:

- finite low-buffer, recreation, reset and disturbance registries;
- exact integral source-to-claim maximum flow;
- removal of cross-type source overcount;
- cap-invariance through repeated numerical enlargements;
- canonical failures for new addresses, relabelled records, duplicate debits and unrecorded deposits.

## Main AC frontier

Only AC remains active. The next physical tasks are:

1. enumerate the actual fixed-schema physical source and exceptional claim dictionaries;
2. construct their compatibility arcs and run AC5jw;
3. discharge the first source/claim cut or address discrepancy;
4. extract and stratify all physical internal edges;
5. extend the repair rank and prove cofinality;
6. apply AC5ka--AC5js.

AC6 and the global no-three-in-line conjecture remain open.

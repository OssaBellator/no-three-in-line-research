# Alternating-core AC2 physical structural re-extraction

## Status

This note keeps AC as the sole active research focus and proves AC5ll--AC5lq. It continues the AC1 physical certificate compiler by turning certified anchor, quotient, carry and bounded-denominator objects into occurrence-faithful structural candidates, completing their full incompatibility graph, re-extracting a compatible paid family or localizing a quantitatively paid overload, and checking that selected payment demands admit one physical capacity assignment.

The result does not prove the missing geometric degree bounds for every actual AC1 output. It proves the complete finite compiler once the physical object, conflict and source rows are supplied. Missing conflict rows, hidden cross-object collateral and duplicated paid occurrences are exact failures rather than optimistic omissions.

## Structural object records

A candidate structural object `o` retains:

1. its AC1 continuation kind and complete occurrence family;
2. one physical installation or delegation operation;
3. every touched row, column, cell, owner and source address;
4. its exact paid occurrence set and destroyed weight `w(o)`;
5. its exact individual collateral bound;
6. every protected contract it may affect;
7. every cross-object certificate or legality row;
8. finite arithmetic labels on each possible incompatibility;
9. every eligible physical payment/source unit and capacity.

Two objects conflict when any simultaneous installation would overlap a physical footprint, reuse one paid occurrence, violate a hard or protected contract, create an undeclared cross-object certificate, or fail another retained joint-legality row.

## AC5ll -- canonical complete incompatibility graph -- PROVED

For a finite structural family `O`, evaluate every unordered pair and insert an edge exactly when at least one complete conflict row fires. Retain on that edge the ordered list of all physical causes.

The compiler returns the least of:

1. a footprint or paid-occurrence overlap missing from the proposed graph;
2. a protected-contract or cross-certificate edge missing from the proposed graph;
3. a spurious edge with no physical cause;
4. an omitted edge label or stale object version;
5. two edge records assigning different causes to the same object pair.

On the accepted branch the graph is the full AC2a incompatibility graph. An independent set has pairwise disjoint paid occurrences and every nonadditive cross-object effect has been excluded or separately certified.

### Proof

All object and pair records are finite. Every conflict predicate is evaluated on the complete physical records, and the fixed pair/cause order selects the first discrepancy. Independence then means that none of the declared simultaneous-installation obstructions occurs. QED.

## AC5lm -- deterministic compatible-family extraction -- PROVED

Let the accepted conflict graph have maximum degree `Delta`. A deterministic greedy colouring in the fixed object order uses at most `Delta+1` colours. Select the colour class of maximum total paid weight, breaking ties lexicographically. Then

\[
\boxed{
\sum_{o\in I}w(o)
\ge
\frac{1}{\Delta+1}
\sum_{o\in O}w(o).
}
\]

If every object has collateral at most `eta w(o)` and all nonadditive effects appear in the graph, the simultaneous batch has collateral at most

\[
\eta\sum_{o\in I}w(o).
\]

For small bounded censuses the compiler may instead enumerate all independent sets and return the exact maximum-weight lexicographically least family; this can only improve the displayed guarantee.

### Proof

A maximum-degree-`Delta` graph has a greedy `(Delta+1)`-colouring. Colour classes are independent and their weights sum to the total. Paid occurrence disjointness and the complete conflict graph make the selected collateral and destroyed ledgers additive. QED.

## AC5ln -- paid closed-neighbourhood overload router -- PROVED

Discard zero-weight objects and define

\[
L(o)=\sum_{v\in N[o]}w(v).
\]

For every `K>=1`, the compiler returns exactly one of:

1. the least object satisfying
   \[
   \boxed{L(o)>K w(o)};
   \]
2. a compatible family `I` with
   \[
   \boxed{
   \sum_{o\in I}w(o)
   \ge
   \frac1K\sum_{o\in O}w(o).
   }
   \]

The executable compiler verifies the second branch by exact maximum-weight independent-set search on the bounded census, while the general existence statement follows from the weighted exponential-race argument of AC2c.

### Proof

If no overload exists, selecting an object whose exponential clock is earliest in its closed neighbourhood gives expected selected weight `sum_o w(o)^2/L(o)>=sum_o w(o)/K`. Exact finite search returns a family at least as heavy. QED.

## AC5lo -- labelled overload concentration and strict support descent -- PROVED

Assume `L(o)>K w(o)` with `K>1`. Partition the open-neighbourhood paid weight by the complete arithmetic edge labels. If `T` labels occur, select the least maximum-weight label `lambda`. Then

\[
\boxed{
\sum_{v\in S_\lambda(o)}w(v)
>
\frac{K-1}{T}w(o).
}
\]

For every `Q>=1`, run AC5ln on the graph induced by `S_lambda(o)`. It returns either:

1. a compatible same-label family of weight greater than
   \[
   \boxed{\frac{K-1}{TQ}w(o)};
   \]
2. a restricted overloaded centre inside the strict subset
   \[
   S_\lambda(o)\subseteq O\setminus\{o\}.
   \]

In the second branch the support-deficit potential

\[
\Xi_{\rm supp}=|O|-|U|
\]

strictly increases. Pure labelled recursion therefore has depth at most `|O|-1` unless a discarded object is explicitly reintroduced, in which case the reopening requires its own ticket or paid source.

### Proof

Paid open-neighbourhood weight exceeds `(K-1)w(o)`. Pigeonhole over `T` labels gives the first display. Applying AC5ln to the induced class gives the two alternatives. The recursive universe excludes its centre, so its cardinality strictly falls. QED.

## AC5lp -- occurrence-faithful source assignment or canonical Hall cut -- PROVED

Let `D` be the exact paid demands of a selected compatible structural family. Let `S` be the globally addressed physical source/capacity units with integral stocks `c(s)`, and retain the exact eligibility relation

\[
E\subseteq D\times S.
\]

Split every source stock into occurrence copies and compute a canonical maximum matching. Exactly one of the following occurs:

1. every demand is assigned to one compatible live physical source occurrence;
2. a canonical inclusion-minimal Hall-deficient demand set `X` is returned with
   \[
   \boxed{
   \sum_{s\in N(X)}c(s)<|X|.
   }
   \]

A source occurrence cannot pay two selected objects, even when those objects came from different AC1 continuation kinds. Repeated source aliases collapse before matching.

### Proof

After splitting integral capacities into unit copies, this is finite bipartite matching. Hall's theorem gives the deficiency criterion; fixed orders choose the canonical core and matching. QED.

## AC5lq -- complete AC2 physical continuation compiler -- PROVED

For every certified AC1 structural family, run:

1. AC5ll to complete the incompatibility graph;
2. AC5lm/AC5ln to return a compatible batch or paid overload;
3. AC5lo recursively on a labelled overload;
4. AC5lp on the selected paid demands;
5. the AC3v/AC3w footprint and payment audit on the resulting simultaneous operation.

The output is exactly one of:

- an installable occurrence-faithful structural batch with exact paid weight and collateral bound;
- a compatible same-label batch;
- a strict labelled support descent;
- a physical source assignment;
- a canonical source Hall cut;
- the first missing or spurious conflict row;
- the first duplicated paid occurrence or source alias;
- the first missing joint-legality or collateral certificate.

Every successful batch becomes a typed AC operation family for the reachable serializer. Every failure retains the AC1 occurrence family and the exact pair, edge label, demand or source address that blocks continuation.

### Proof

Each stage is finite and fail-closed. AC5ll validates additivity, AC5lm--AC5lo provide the paid structural alternatives, and AC5lp validates occurrence-faithful payment capacity. Their ordered failure routers compose. QED.

## Deterministic audit

`scripts/verify_ac_ac2_structural_reextraction.py` checks 2,500 bounded physical object systems. It verifies complete conflict construction, exact compatible batches, paid overloads, same-label re-extraction, strict recursive support descent, occurrence-capacity assignments, canonical Hall deficiencies, missing conflict rows and duplicate paid aliases.

## Main AC frontier

Only AC remains active. The next physical tasks are:

1. instantiate the complete conflict rows for actual AC1 quotient, carry, BDA and star objects;
2. discharge every returned paid overload label geometrically;
3. construct or refute each physical source assignment;
4. convert successful batches into reachable operation and rank records;
5. route repeated signatures through the AC3 ticket/cycle interfaces;
6. continue the initial-state termination manifest.

AC6 and the global no-three-in-line conjecture remain open.

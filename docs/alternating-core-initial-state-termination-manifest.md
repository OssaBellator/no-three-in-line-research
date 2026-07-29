# Alternating-core initial-state termination manifest

## Status

This note keeps AC as the sole active research focus and proves AC5kh--AC5km. It consolidates the current AC chain into one versioned physical proof object for a chosen initial state. The manifest either certifies that every reachable nonterminal trajectory terminates, or returns the first finite physical record missing from the dependency chain.

The result remains contract-qualified. It does not populate the manifest with the actual geometric AC data, prove AC6, or prove the no-three-in-line conjecture.

## Manifest record

Fix one chosen physical initial state `v_0`. An **AC initial-state termination manifest** contains seven versioned sections:

1. `schema`: complete physical dictionaries, address meanings and initial state;
2. `serializer`: total deterministic operation records and complete successor vectors;
3. `frontier`: interior template completions and permanent boundary certificates;
4. `fairness`: the reachable overflow queue and its fair selection certificate;
5. `rank`: overlap-preserving repair-rank extensions on every exposed shell;
6. `stratification`: supply, credited-restart, repair and exceptional edge records;
7. `exception`: the fixed global physical source/exception network and its finite flow bound.

Every section retains the hashes of all prerequisite sections and the complete physical addresses of its outputs. A changed prerequisite hash invalidates the dependent section rather than silently reusing it.

## AC5kh -- exact dependency order and coherent manifest digest -- PROVED

The manifest dependency order is

\[
\text{schema}
\prec
\text{serializer}
\prec
\text{frontier}
\prec
\text{fairness}
\prec
\text{rank}
\prec
\text{stratification}
\prec
\text{exception}.
\]

The complete canonical serialization of the seven sections determines one digest. The compiler returns the least of:

1. a stale or conflicting schema record;
2. a nondeterministic operation or missing successor coordinate;
3. an incomplete interior or boundary frontier certificate;
4. an omitted or starved reachable overflow record;
5. a rank cycle or overlap violation;
6. a mislabeled or unclassified internal edge;
7. an exceptional source/claim conflict, unpaid cut or nonfinite address universe.

If no failure occurs, every downstream record refers to exactly the accepted upstream digest.

### Proof

The dependency graph is a finite total order. Every section is finite and canonically serialized, so equality of digests is equality of the retained prerequisite records. The fixed section and address orders select the first discrepancy. QED.

## AC5ki -- monotone manifest refinement -- PROVED

Suppose the compiler stops at section `j`. Add the exact missing record or discharge the exact conflict while leaving every earlier section unchanged.

Then all sections preceding `j` remain accepted with identical digests. Recompilation begins at `j`; no earlier physical object, edge, rank, capacity address or frontier certificate is rebuilt.

If the proposed repair changes an earlier record, it is a schema or prerequisite change and the compiler returns the least changed earlier section.

### Proof

Every section depends only on earlier digests and its own complete records. Supplying a missing record at `j` does not alter any earlier serialization. A changed earlier field changes its digest and is detected before `j`. QED.

## AC5kj -- complete initial-state termination certificate -- PROVED

Assume all seven manifest sections accept. Then:

1. AC5kd gives reachable-prefix cofinality from `v_0`;
2. AC5jj supplies one overlap-preserving global repair rank;
3. AC5jp stratifies every reachable internal edge;
4. AC5jz supplies one finite globally deduplicated exceptional stock;
5. AC5jh removes every noninternal permanent boundary route from the nonterminal graph.

Therefore AC5kf and AC5js apply: no infinite nonterminal physical trajectory starts at `v_0`.

The complete proof object consists of:

- the coherent manifest digest;
- the reachable direct-limit graph interface;
- the global rank table or rank-extension certificates;
- the edge-stratification table;
- the integrated exceptional source/claim flow and finite stock;
- the permanent boundary-certificate table.

### Proof

Each numbered item is exactly the corresponding hypothesis of AC5kf. Composition gives initial-state termination. QED.

## AC5kk -- finite minimal failure witness -- PROVED

If the complete certificate is unavailable, the compiler returns one finite witness from the first failed section. Deleting any address or field required to identify that witness makes the failure record incomplete.

For set- or graph-valued failures, the witness is canonical:

- least missing physical row;
- least zero-neighbourhood object;
- least starved queue record;
- least directed progress cycle or violated old edge;
- least nondecreasing progress edge;
- canonical minimum source/claim cut;
- least malformed exceptional address.

Thus every remaining AC task is a finite construction or contradiction target, not an unnamed global recurrence gap.

### Proof

Each prerequisite compiler already supplies a finite canonical first witness. The manifest returns the first failed section and reuses that section's witness order. QED.

## AC5kl -- proof-object stability under cap enlargement -- PROVED

For a fixed schema, enlarging numerical caps and fairly exposing a new shell preserves the accepted prefixes of the manifest:

- `schema` remains identical;
- old serializer records remain identical;
- old frontier certificates remain valid;
- the fairness certificate appends new queue history;
- the rank section appends a shell extension;
- stratification appends new edge records;
- the exception section remains identical by AC5jy.

The new manifest digest can therefore be represented by the old digest plus the ordered shell delta. If a cap enlargement changes an old record, AC5iw returns the exact no-regression failure.

### Proof

This is the composition of AC5iw, AC5ji, AC5jj, AC5jy and AC5ke. QED.

## AC5km -- final current AC6 reduction -- PROVED

For the chosen AC initial state, the qualitative termination problem is reduced to populating the seven finite manifest sections.

A complete manifest proves initial-state termination. An incomplete manifest returns the first exact finite physical witness. No additional abstract compactness, uniform state maximum or unclassified recurrence theorem is required.

To promote this initial-state result to the full intended AC statement, the remaining physical work is:

1. specify the actual class of allowed initial states;
2. provide one coherent manifest or a uniform manifest-construction rule for each;
3. verify that those initial states represent every case required by AC6.

### Proof

AC5kj handles each manifested initial state. AC5kk handles every failure. The final promotion is exactly the stated physical coverage obligation. QED.

## Deterministic audit

`scripts/verify_ac_initial_state_termination_manifest.py` checks 3,200 generated manifests. It verifies:

- coherent seven-section dependency digests;
- exact first-failure routing at every section;
- monotone refinement without earlier-record regression;
- ordinal termination on complete manifests with finite exceptional interruptions.

## Main AC frontier

Only AC remains active. The remaining work is now physical data population:

1. choose and serialize the actual AC initial-state class;
2. populate the seven manifest sections from the historical AC records;
3. run the compiler;
4. discharge its first returned finite witness;
5. repeat until every required initial state has a complete manifest.

AC6 and the global no-three-in-line conjecture remain open.

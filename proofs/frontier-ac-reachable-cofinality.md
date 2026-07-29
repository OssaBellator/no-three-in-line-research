# Frontier pass: AC reachable cofinality

## Active branch

`agent/ac-reachable-cofinality`

Parent: `agent/ac-global-exception-universe` at `1d90681c7d77fe99358f9c5c5d74f4425574b887`.

Only AC is active. Historical AC, RI, BDA, GC, OP, SRR, SAS and all-n branches remain immutable source libraries.

## New theorem block

- **AC5kb:** complete finite successor exposure vector and least cap vector internalizing one operation.
- **AC5kc:** fair reachable-overflow queue and exact starvation witness.
- **AC5kd:** reachable-prefix cofinality from one chosen physical initial state.
- **AC5ke:** reachable direct-limit graph and preservation of all old certificates.
- **AC5kf:** initial-state ordinal termination certificate.
- **AC5kg:** exact reachable-cofinality failure router.

## Logical gain

Absolute enumeration of every formal finite AC state is unnecessary. The deterministic operation record gives the complete finite successor vector before cap truncation. A fair queue that eventually expands every reachable overflow therefore exposes every finite trajectory prefix from the chosen initial state.

For an expandable operation `(v,o)`, the least internalizing cap is

\[
L_i^+(v,o)=\max(L_i,s_i(v,o)).
\]

No-regression preserves the old graph, rank, templates and exception addresses. Induction along a finite path proves that one later box contains the entire path.

Combined with the overlap-preserving rank, global exception universe and ordinal edge stratification, reachable cofinality is enough to rule out an infinite nonterminal trajectory from the initial state.

## Deterministic audit

Equivalent execution of `scripts/verify_ac_reachable_cofinality.py` checks 2,500 generated reachable systems:

- valid fair systems: `500`;
- reachable states exposed: `7,366`;
- explicit cap expansions: `3,121`;
- states entering automatically after enlargement: `3,745`;
- exact aggregate shell size: `1,710,268`;
- omitted successor-coordinate witnesses: `500`;
- starved queue witnesses: `500`;
- aggregate starvation age: `2,904`;
- schema-changing expansion witnesses: `500`;
- false terminal/boundary classifications: `500`.

All assertions pass.

## Remaining AC frontier

1. Serialize the actual reachable physical graph from the chosen AC initial state.
2. Run the fair overflow queue and complete every exposed shell.
3. Extend the repair rank and stratify every reachable internal edge.
4. Compile the actual global exceptional source/claim network.
5. Certify every permanent boundary route.
6. Apply AC5kf, or retain the first AC5kg witness as the exact AC6 obstruction.

AC6 and the global no-three-in-line conjecture remain open.

# Frontier pass: AC overlap-preserving tower rank extension

## Active branch

`agent/ac-tower-rank-extension`

Parent: `agent/ac-frontier-certificate-compiler` at `c9a6fadd0e3d072142ae854dd7c527bbcb1d8c40`.

Only AC is active. Historical AC, RI, BDA, GC, OP, SRR, SAS and all-n branches remain immutable source libraries.

## New theorem block

- **AC5jj:** unique least overlap-preserving shell rank extension on an acyclic progress graph.
- **AC5jk:** strict-progress cycle, old-rank violation and shell-rank-cap obstructions.
- **AC5jl:** bounded integer stabilization with canonical shell/address witnesses for every strict increase.
- **AC5jm:** finite global physical-capacity quotient and level-independent deduplicated stock bounds.
- **AC5jn:** uniform scheduler and episode certificate after rank extension.
- **AC5jo:** exact tower-divergence router.

## Logical gain

The previous direct-limit theorem assumed schedulers agreed on overlaps. Recomputing a minimax rank after a box enlargement does not guarantee this. The new compiler fixes every old certified rank and solves

\[
\rho(u)\ge\rho(v)+1
\]

on the complete enlarged progress graph.

On a DAG, reverse topological evaluation gives the unique least shell extension. Failure is one of:

1. a directed strict-progress cycle;
2. an old state whose fixed rank is too small for a new successor;
3. a shell state whose least possible rank exceeds the declared global cap.

With a finite global physical-address universe, all selected payment, ticket and reset totals are bounded by one fixed stock table rather than by the number of templates or boxes. Bounded integer envelope components can strictly increase only finitely many times and therefore stabilize.

These facts turn the conditional AC5jc scheduler-agreement hypothesis into an executable shell-by-shell certificate.

## Deterministic audit

Equivalent execution of `scripts/verify_ac_tower_rank_extension.py` checks 2,500 shell extensions:

- valid overlap-preserving extensions: `625`;
- shell states assigned ranks: `1,908`;
- aggregate maximum extended rank: `4,168`;
- strict-progress cycle witnesses: `625`;
- old-rank overlap violations: `625`;
- shell rank-cap failures: `625`;
- strict bounded-component increases: `22,790`;
- aggregate declared component caps: `105,505`;
- global physical capacity stock: `44,332`;
- selected deduplicated stock: `28,435`;
- alias amount removed: `12,766`.

All assertions pass.

## Remaining AC frontier

1. Extract the actual scheduled strict-progress edges from the physical operation compiler.
2. Extend ranks over each physical shell or discharge the returned cycle/edge witness.
3. Prove finite global caps for deficit, restart potential and rank.
4. Declare the finite global physical capacity-address universe.
5. Prove cofinality and disturbance bounds.
6. Apply AC5jn--AC5jc or retain the first AC5jo divergence witness.

AC6 and the global no-three-in-line conjecture remain open.

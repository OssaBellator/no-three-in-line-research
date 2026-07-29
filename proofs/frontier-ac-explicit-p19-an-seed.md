# Frontier pass: explicit physical p=19 AN seed

## Active branch

`agent/ac-explicit-p19-an-seed`

Parent: `agent/ac-repair-source-manifest` at `472d0ac0c6ed9241c3bd724799c2167465204264`.

Only AC is active. Historical side branches remain immutable source libraries.

## New theorem block

- **AC5mp:** explicit legal rectangle switch in `H_1`.
- **AC5mq:** explicit endpoint-disjoint seven-pair secant star in `H_7`.
- **AC5mr:** exact 1,300-state alternating matching bank.
- **AC5ms:** exact physical collateral and potential census.
- **AC5mt:** explicit improving installation of potential decrease 25.
- **AC5mu:** completed terminating manifest prefix for this initial state.

## Concrete data

Use `p=19`, `n=18`, with layers `H_7` and `H_1`. Switch

\[
(6,16),(16,6)
\longrightarrow
(6,6),(16,16).
\]

The candidate `z=(6,6)` lies on seven endpoint-disjoint real secants of `H_7`. The selected endpoints have columns

\[
(1,3,4,8,9,10,14)
\]

and rows

\[
(7,15,16,8,5,14,10).
\]

The exact forbidden matching set has nine positions and the legal bank contains 1,300 permutations.

The occurrence-faithful certificate census is

\[
T_1=149,
\qquad
T_2=138,
\qquad
T_3=33.
\]

The current state has 66 real collinear triples. The canonical minimum-potential legal matching

\[
(3,6,1,5,2,4,0)
\]

uses replacement cells

\[
\{(1,8),(3,10),(4,15),(8,14),(9,16),(10,5),(14,7)\}
\]

and has potential 41. The exact decrease is 25. A total of 1,025 of the 1,300 bank states improve.

## Deterministic audit

`python scripts/verify_ac_explicit_p19_an_seed.py` reconstructs all data from the modular-hyperbola definitions and verifies:

- anchor-layer points: `18`;
- switch-layer points: `18`;
- secant pairs: `7`;
- forbidden positions: `9`;
- legal matching states: `1,300`;
- rank-one certificates: `149`;
- rank-two certificates: `138`;
- rank-three certificates: `33`;
- current potential: `66`;
- post-switch fixed potential: `29`;
- best successor potential: `41`;
- exact potential decrease: `25`;
- improving matching states: `1,025`;
- average anchor collateral: `30.953846153846...`.

All assertions pass.

## Remaining AC frontier

1. Manifest the improved 41-certificate successor and identify its next canonical state class.
2. Search for explicit nonimproving AN seeds that enter AC1.
3. Construct a coverage rule for the full intended initial-state class.
4. Continue the physical repair, rank and exception ledgers for later states.

AC6 and the global no-three-in-line conjecture remain open.

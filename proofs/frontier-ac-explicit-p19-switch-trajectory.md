# Frontier pass: explicit p=19 switch trajectory

## Active branch

`agent/ac-explicit-p19-switch-trajectory`

Parent: `agent/ac-explicit-p19-an-seed` at `bb557f6b529f7b8e8ec169678a74278045224ee7`.

Only AC is active. Historical side branches remain immutable source libraries.

## New theorem block

- **AC5mv:** eleven-step strict legal-switch descent from 41 to 10.
- **AC5mw:** exhaustive two-row-switch local minimum at potential 10.
- **AC5mx:** 247-edge loop-erased barrier path from 10 to 5.
- **AC5my:** exact five-certificate endpoint state.
- **AC5mz:** physical barrier-rank interpretation.
- **AC5na:** corrected explicit p=19 frontier.

## Exact results

The strict path has potential sequence

\[
41,30,25,22,20,17,15,14,13,12,11,10.
\]

At the final state, 270 two-row switches are legal after opposite-layer collision checks, and none lowers the potential below 10.

The committed loop-erased path from this local minimum contains 247 legal switches, visits no state twice, has maximum potential 40 and ends at potential 5.

The final state has exactly five real collinear triples, all listed in the data and theorem note.

## Deterministic audit

`python scripts/verify_ac_explicit_p19_switch_trajectory.py` verifies:

- strict descent moves: `11`;
- exact strict potential sequence: `[41,30,25,22,20,17,15,14,13,12,11,10]`;
- legal neighbours at the local minimum: `270`;
- improving neighbours: `0`;
- loop-erased barrier moves: `247`;
- barrier maximum: `40`;
- final potential: `5`;
- final triple occurrences: `5`.

All assertions pass.

## Logical gain

Raw triple count is not a complete legal-switch descent rank: a state locally minimal at 10 reaches a five-triple state through a finite nonmonotone path. The finite exposed move graph therefore requires the minimax barrier/depth rank already developed for AC, not strict one-step potential descent.

## Remaining AC frontier

1. Eliminate or structurally classify the five remaining triples.
2. Search for a smaller certified barrier path.
3. Populate AC1/repair/source rows on the five-triple state.
4. Generalize the explicit hyperbola-switch construction.
5. Continue the initial-state manifest.

AC6 and the global no-three-in-line conjecture remain open.

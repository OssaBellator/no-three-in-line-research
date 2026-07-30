# Frontier pass: explicit p=31 switch trajectory

## Active branch

`agent/ac-p31-explicit-switch-frontier`

Parent: `agent/ac-prime-seed-census` at `f2e402c881e8eefdfbec6fd1c316473639f89707`.

Only AC is active. Historical branches remain immutable theorem libraries.

## Theorem block

- **AC5nt:** explicit 154-switch trajectory from the strongest p=31 AN successor at potential 75 to potential 6.
- **AC5nu:** exact checkpoint minimax barriers for potentials 13,12,11,10,9,8,7.
- **AC5nv:** exact six-triple physical frontier and complete lower-sublevel components through barrier 9.
- **AC5nw:** fail-closed separation between exact component exhaustion and unsuccessful heuristic search.

## Physical trajectory

The initial state is the canonical minimum-potential bank state from the `H_1,H_12` alternating-star seed with switch rows `16,24` and candidate `(16,16)`.

A replayable sequence of 154 legal two-row switches reaches potential 6. The checkpoint potentials are

`75 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8 -> 7 -> 6`.

Every move preserves two disjoint permutation layers. Every stored potential is recomputed from all `C(60,3)` real triple determinants.

## Exact checkpoint barriers

The proved barriers to a lower-potential state are:

- from 13: barrier 16;
- from 12: barrier 13;
- from 11: barrier 11;
- from 10: barrier 12;
- from 9: barrier 12;
- from 8: barrier 12;
- from 7: barrier 11.

The six-triple endpoint has exact sublevel-component sizes

- barrier 6: 1;
- barrier 7: 9;
- barrier 8: 33;
- barrier 9: 860.

None contains a lower state, so the next minimax barrier is at least 10.

## Validation

Compile:

`g++ -O3 -std=c++17 scripts/verify_ac_p31_switch_frontier.cpp -o verify_p31`

Replay:

`./verify_p31`

Recompute checkpoint components separately:

`./verify_p31 13`
`./verify_p31 12`
`./verify_p31 10`
`./verify_p31 9`
`./verify_p31 8`
`./verify_p31 7`
`./verify_p31 6`

Each invocation passed locally. The final barrier-9 component contains 860 states. The mode split is operational only: it avoids one long combined process while running exactly the same deterministic component searches.

## Exact versus heuristic status

Bounded goal-directed and stochastic searches tested barriers through 24 without finding a lower state. Those searches were not exhaustive and therefore prove nothing beyond the exact barrier-9 exhaustion.

The accepted mathematical frontier is:

1. one complete physical path from 75 to 6;
2. exact low-potential barrier certificates along the path;
3. a proved lower bound of 10 for escape from the final six-triple state;
4. no upper bound yet for that escape.

## Next frontier

1. Enumerate the six remaining triples and their shared-point/line structure.
2. Build a targeted repair incidence graph from legal switches to destroyed and created certificate occurrences.
3. Exhaust the barrier-10 component efficiently or find and replay a lower-state path.
4. Classify any Hall core or missing compatibility rectangle returned by the targeted repair graph.
5. Continue the explicit state to zero and compare its repair templates with the completed p=19 trajectory.

AC6 and the global no-three-in-line conjecture remain open.

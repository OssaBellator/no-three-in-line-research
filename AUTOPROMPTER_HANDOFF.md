# AUTOPROMPTER HANDOFF

Checkpoint updated: 2026-08-02 22:20 Australia/Melbourne.

## Repository and current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Active branch: `agent/ac-p31-recovered-tail`
- Parent branch: `agent/ac-p31-explicit-switch-frontier`
- Active research track: alternating core (AC) only.
- Historical prime-patching and composite-modulus branches remain frozen source libraries.
- No pull request or merge has been requested or created.

## Goal

Complete the explicit `p=31`, `n=30` trajectory from the strongest alternating-star successor to a zero-triple configuration, retaining exact physical switch addresses and exact minimax barriers.

The broader goal remains a uniform AC theorem. AC6 and the general no-three-in-line conjecture remain open.

## Durable trajectory status

### Existing path through four triples

The branch contains:

- the 154-switch installed path from potential 75 to 6;
- a 69-switch route from 6 to 5 with exact barrier 10;
- a 527-switch route from 5 to 4 with exact barrier 10.

### Four to three: AC5od--AC5of

- complete four-triple immediate repair atlas: 810 legal moves, no improvement;
- complete lower components at barriers 4--8: `1,1,5,29,465`;
- 35-switch route from 4 to 3 with maximum 9;
- exact minimax barrier: 9;
- explicit three-triple endpoint committed.

Artifacts:

- `data/ac-p31-four-triple-core.json`
- `scripts/verify_ac_p31_four_triple_core.py`
- `scripts/verify_ac_p31_four_triple_frontier.cpp`
- `data/ac-p31-four-to-three.json`
- `scripts/verify_ac_p31_four_to_three.py`
- `docs/alternating-core-p31-four-triple-frontier.md`
- `proofs/frontier-ac-p31-four-triple-frontier.md`

### Three-triple physical frontier: AC5og--AC5oh

Artifacts:

- `data/ac-p31-three-triple-core.json`
- `scripts/verify_ac_p31_three_triple_core.py`
- `data/ac-p31-three-triple-frontier.json`
- `scripts/verify_ac_p31_three_triple_frontier.cpp`
- `docs/alternating-core-p31-three-triple-frontier.md`
- `proofs/frontier-ac-p31-three-triple-frontier.md`

Exact result:

- the three current triples are vertex-disjoint;
- 810 legal immediate switches;
- no one-switch improvement;
- least immediate potential 5, attained by four moves;
- complete component sizes at barriers 3--8: `1,1,9,42,205,3635`;
- no component contains a state below potential 3;
- therefore the next minimax barrier is at least 9.

## Current durable branch head before this handoff update

`d6942989b4f0f692cb35d8631683bce69866ec18`

## Current endpoint

Red permutation:

`(14,15,9,18,8,25,29,3,4,13,19,2,23,28,1,12,7,24,6,17,11,26,30,5,22,27,20,16,21,10)`

Blue permutation:

`(18,10,24,6,14,15,23,20,25,1,9,4,7,29,30,27,28,19,2,5,3,13,21,11,8,26,12,22,17,16)`

Exact potential: `3`.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains layer and exact row pair.
3. Barrier lower bounds require complete sublevel-component exhaustion.
4. Candidate paths are replayed exactly before acceptance.
5. Potential is the exact real collinear-triple count.
6. Every state remains two disjoint permutation layers.
7. Search statistics are diagnostic, not proof.
8. Completed logical units are committed before the next risky unit.
9. Do not create a pull request or merge unless explicitly requested.

## Current uncommitted computation

Upper-path searches from the explicit three-triple state are active:

- two best-first searches at barrier 9;
- three best-first searches at barrier 10;
- two tabu traversals at barrier 9;
- two tabu traversals at barrier 10.

Latest original best-first ledgers before this update:

- barrier 9: more than 60,000 states expanded and 84,000 states seen;
- barrier 10: more than 60,000 states expanded and 359,000 states seen;
- no two-triple endpoint yet.

No upper-path result is accepted until an exact move sequence is written and replayed.

## Blockers

- No durable `3 -> 2`, `2 -> 1` or `1 -> 0` segment exists yet.
- The exact barrier-nine component has not been exhausted; only barriers through 8 are complete.
- Uniform AC arithmetic and repair predicates remain open.
- No theorem guarantees terminal paths uniformly across prime-minus-one seeds.

## Exact next steps

1. Continue the active barrier-nine and barrier-ten candidate searches.
2. Preserve the first exact path reaching potential at most two.
3. Replay the path independently and determine its maximum potential.
4. If the path stays within barrier 9, combine it with AC5oh to prove exact barrier 9.
5. If it requires barrier 10, exhaust the complete barrier-nine component before claiming equality.
6. Commit the `3 -> 2` data, verifier, theorem note and proof ledger as a separate unit.
7. Repeat the process through potential 1 and 0.
8. Once zero is reached, add a standalone verifier from the installed 75-triple state to the terminal state.

## Validation commands

```text
python scripts/verify_ac_p31_three_triple_core.py

g++ -O3 -std=c++20 scripts/verify_ac_p31_three_triple_frontier.cpp -o verify_three
./verify_three
```

## Uncommitted files

No completed source or data file is waiting to be committed. Only active search processes and temporary local logs are uncommitted.

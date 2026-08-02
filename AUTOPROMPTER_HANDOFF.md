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

### Explicit path through three triples

The repository-backed switch lengths are:

- potential 75 to 6: `154`;
- 6 to 5: `69`, exact barrier 10;
- 5 to 4: `527`, exact barrier 10;
- 4 to 3: `35`, exact barrier 9.

Total durable switches from the installed potential-75 state to the explicit potential-three state:

`785`.

Including the alternating-star installation, the durable manifest prefix has `786` operations.

### End-to-end integrity theorem: AC5oi

Artifacts:

- `scripts/verify_ac_p31_durable_trajectory.py`
- `docs/alternating-core-p31-durable-trajectory-through-three.md`
- `proofs/frontier-ac-p31-durable-trajectory-through-three.md`

The verifier checks exact endpoint equality across all four data files, replays every switch, verifies disjoint permutation layers and recomputes every potential.

### Three-triple physical frontier: AC5og--AC5oh

Artifacts:

- `data/ac-p31-three-triple-core.json`
- `scripts/verify_ac_p31_three_triple_core.py`
- `data/ac-p31-three-triple-frontier.json`
- `scripts/verify_ac_p31_three_triple_frontier.cpp`
- `docs/alternating-core-p31-three-triple-frontier.md`
- `proofs/frontier-ac-p31-three-triple-frontier.md`

Exact result:

- three vertex-disjoint current triples;
- 810 legal immediate switches;
- no one-switch improvement;
- complete lower component sizes at barriers 3--8: `1,1,9,42,205,3635`;
- no state below potential three through barrier eight;
- next minimax barrier is at least nine.

## Current durable branch head before this handoff update

`c4233b2aff06c0e657b20344703a6ab778cf5ff0`

## Current endpoint

Red permutation:

`(14,15,9,18,8,25,29,3,4,13,19,2,23,28,1,12,7,24,6,17,11,26,30,5,22,27,20,16,21,10)`

Blue permutation:

`(18,10,24,6,14,15,23,20,25,1,9,4,7,29,30,27,28,19,2,5,3,13,21,11,8,26,12,22,17,16)`

Exact potential: `3`.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains layer and exact row pair.
3. Barrier lower bounds require complete physical sublevel-component exhaustion.
4. Candidate paths are replayed exactly before acceptance.
5. Potential is the exact real collinear-triple count.
6. Every state remains two disjoint permutation layers.
7. Search statistics are diagnostic, not proof.
8. Completed logical units are committed before the next risky unit.
9. Do not create a pull request or merge unless explicitly requested.

## Current uncommitted computation

### Exact barrier-nine traversal

A dedicated FIFO breadth-first traversal of the complete physical `Phi<=9` component is active from the explicit three-triple state.

Latest durable-session ledger before this update:

- at least `50,000` states processed;
- at least `53,664` states discovered;
- active queue roughly `3,664` states;
- no potential-two endpoint found yet.

The traversal stores a physical predecessor for every discovered state. It will either return an exact `3 -> 2` path within barrier nine or exhaust the component and prove the barrier is at least ten.

### Direct zero-target MILP

A pure-feasibility mixed-integer model is also active:

- 900 binary cell variables;
- exactly two cells in each row and column;
- 34,270 real-line constraints, each capped at two selected cells.

This search is independent of the local path graph. A feasible solution would give an explicit zero-triple target for goal-directed connection.

The local runtime restarted once during exploratory searches; no committed artifact was lost. All stale temporary candidate queues were discarded and are not theorem claims.

## Blockers

- No durable `3 -> 2`, `2 -> 1` or `1 -> 0` segment exists yet.
- The exact barrier-nine component is still open.
- The zero-target MILP has not yet produced a feasible incumbent.
- Uniform AC arithmetic and repair predicates remain open.

## Exact next steps

1. Continue the exact barrier-nine FIFO traversal to path or exhaustion.
2. Preserve and replay any returned physical `3 -> 2` path immediately.
3. If barrier nine exhausts, begin a durable barrier-ten traversal or use an already verified upper candidate.
4. Continue the direct zero-target solve; if feasible, store and independently verify the target before using it.
5. Commit the next completed path or exhaustion certificate as a separate logical unit.
6. Repeat through potential one and zero.
7. Extend the end-to-end trajectory verifier after each committed segment.

## Validation commands

```text
python scripts/verify_ac_p31_durable_trajectory.py
python scripts/verify_ac_p31_three_triple_core.py

g++ -O3 -std=c++20 scripts/verify_ac_p31_three_triple_frontier.cpp -o verify_three
./verify_three
```

## Uncommitted files

No completed source or data file is waiting to be committed. Only active exact search state and temporary solver logs are uncommitted.

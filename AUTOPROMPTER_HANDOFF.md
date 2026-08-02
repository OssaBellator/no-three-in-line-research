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

Complete the explicit prime-minus-one trajectory for `p=31`, `n=30` from the strongest alternating-star successor to a zero-triple configuration, retaining exact physical switch addresses and exact minimax-barrier certificates at every checkpoint.

The broader goal remains a uniform AC theorem. AC6 and the general no-three-in-line conjecture remain open.

## Durable completed work

### Existing ancestry

The branch contains the AC finite manifest architecture, the explicit `p=19`, `n=18` terminal certificate, the prime-minus-one seed census, and the committed explicit `p=31` path from potential 75 to potential 6.

### Recovered six-to-five segment: AC5nx--AC5ny

Artifacts:

- `data/ac-p31-recovered-tail.json`
- `scripts/verify_ac_p31_recovered_tail.cpp`
- `docs/alternating-core-p31-recovered-six-to-five.md`
- `proofs/frontier-ac-p31-recovered-six-to-five.md`

Exact result:

- 69 legal switches from potential 6 to potential 5;
- maximum potential 10;
- complete `Phi<=9` component: 860 states;
- no lower state in that component;
- exact minimax barrier from six to lower potential: 10.

### Five-triple lower frontier: AC5nz

Artifacts:

- `data/ac-p31-five-triple-frontier.json`
- `scripts/verify_ac_p31_five_triple_frontier.cpp`
- `docs/alternating-core-p31-five-triple-lower-frontier.md`
- `proofs/frontier-ac-p31-five-triple-lower-frontier.md`

Complete component sizes from the recovered five-triple endpoint are:

- barrier 5: 1 state;
- barrier 6: 2 states;
- barrier 7: 14 states;
- barrier 8: 100 states;
- barrier 9: 6797 states.

None contains a state below potential five. Therefore the next minimax barrier is at least 10.

## Current durable branch head before this handoff update

`619a2f892e7366391f60b036a9c5ac491068897c`

This commit records the proof ledger for AC5nz after the data, verifier and theorem-note commits.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains layer and exact row pair.
3. Barrier lower bounds require complete sublevel-component exhaustion.
4. Search may locate upper paths, but each path is replayed exactly.
5. Potential is the exact real collinear-triple count.
6. Every state remains two disjoint permutation layers.
7. Search statistics alone are not proof.
8. Completed logical units are committed before the next risky computation.
9. Do not create a pull request or merge unless explicitly requested.

## Current uncommitted computation

Three independent searches are active from the committed five-triple endpoint inside `Phi<=10`:

1. a best-first exact-potential search;
2. a sampled tabu/random walk;
3. a full-neighbour tabu search.

Latest observed best-first ledger:

- more than 76,000 states expanded;
- more than 274,000 states discovered;
- no four-triple endpoint yet;
- process still active.

The random searches are diagnostic candidate locators only. No result is accepted until replayed exactly.

## Blockers

- No repository-backed `5 -> 4` upper path exists yet, although AC5nz proves its barrier is at least 10.
- No durable `4 -> 3`, `3 -> 2`, `2 -> 1` or `1 -> 0` segment exists.
- The uniform AC1 arithmetic conversion, repair predicates and source-compatibility predicates remain open.
- No theorem guarantees terminal paths uniformly across prime-minus-one seeds.

## Exact next steps

1. Continue the current `Phi<=10` searches from the five-triple endpoint.
2. On the first lower endpoint, preserve the exact move and potential words immediately.
3. Replay the candidate independently and verify the endpoint permutation tables.
4. Commit the `5 -> 4` data, then its verifier, theorem note and proof ledger.
5. Combine the upper path with AC5nz to prove exact barrier 10.
6. Update this handoff after that logical unit.
7. Repeat through four, three, two, one and zero triples.
8. Once zero is reached, add a standalone verifier from the 75-triple installed state to the terminal state.

## Validation commands

Recovered six-to-five segment:

```text
g++ -O3 -std=c++20 scripts/verify_ac_p31_recovered_tail.cpp -o verify_tail
./verify_tail
```

Five-triple lower frontier:

```text
g++ -O3 -std=c++20 scripts/verify_ac_p31_five_triple_frontier.cpp -o verify_five
./verify_five 9
```

Expected barrier-nine result: `6797` states and no lower state.

## Uncommitted files

No completed source or data file is waiting to be committed. The only uncommitted work is the active candidate search and temporary local logs.

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

## Durable completed work

### Existing ancestry

The branch contains the AC finite manifest architecture, the explicit `p=19`, `n=18` terminal certificate, the prime-minus-one seed census, and the committed explicit `p=31` path from potential 75 to potential 6.

### Recovered six-to-five segment: AC5nx--AC5ny

Artifacts:

- `data/ac-p31-recovered-tail.json`
- `scripts/verify_ac_p31_recovered_tail.cpp`
- `docs/alternating-core-p31-recovered-six-to-five.md`
- `proofs/frontier-ac-p31-recovered-six-to-five.md`

Exact result: 69 legal switches from 6 to 5, maximum 10, and complete barrier-nine component size 860 with no lower state. Thus the exact minimax barrier is 10.

### Five-triple lower frontier: AC5nz

Artifacts:

- `data/ac-p31-five-triple-frontier.json`
- `scripts/verify_ac_p31_five_triple_frontier.cpp`
- `docs/alternating-core-p31-five-triple-lower-frontier.md`
- `proofs/frontier-ac-p31-five-triple-lower-frontier.md`

Complete component sizes at barriers 5 through 9 are:

`1, 2, 14, 100, 6797`.

None contains a state below potential five, so the next barrier is at least 10.

### Five-triple physical core atlas: AC5oa

Artifacts:

- `data/ac-p31-five-triple-core.json`
- `scripts/verify_ac_p31_five_triple_core.py`
- `docs/alternating-core-p31-five-triple-core-atlas.md`
- `proofs/frontier-ac-p31-five-triple-core-atlas.md`

Exact result:

- five current triples on five primitive lines;
- one shared current vertex, red `(27,24)`, appearing twice;
- 812 legal immediate switches;
- zero one-switch improvements;
- unique least-potential move `r:3,27` gives potential 6;
- it destroys 3 current triples and creates 4.

Correct destroyed-triple histogram:

- 0 destroyed: 475 moves;
- 1 destroyed: 281 moves;
- 2 destroyed: 53 moves;
- 3 destroyed: 3 moves.

A preliminary mismatched-tuple histogram was corrected before theorem promotion; the verifier enforces the corrected values.

## Current durable branch head before this handoff update

`2df18b5f2277ef452b6b07774a8ddfa8139064bf`

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains layer and exact row pair.
3. Barrier lower bounds require complete sublevel-component exhaustion.
4. Candidate paths are replayed exactly before acceptance.
5. Potential is the exact real collinear-triple count.
6. Every state remains two disjoint permutation layers.
7. Search statistics alone are not proof.
8. Completed logical units are committed before the next risky unit.
9. Do not create a pull request or merge unless explicitly requested.

## Current uncommitted computation

Three best-first searches with different deterministic tie seeds are active from the committed five-triple endpoint inside `Phi<=10`.

Latest main-search ledger:

- more than 144,000 states expanded;
- more than 512,000 states discovered;
- no four-triple endpoint yet;
- process still active.

Two independent seeded searches have each expanded more than 55,000 states. They are candidate locators only and do not affect the proved lower bound.

## Blockers

- No repository-backed `5 -> 4` upper path exists yet, although AC5nz proves its barrier is at least 10.
- No durable `4 -> 3`, `3 -> 2`, `2 -> 1` or `1 -> 0` segment exists.
- The uniform AC1 arithmetic conversion, repair predicates and source-compatibility predicates remain open.
- No theorem guarantees terminal paths uniformly across prime-minus-one seeds.

## Exact next steps

1. Continue the three active `Phi<=10` searches.
2. On the first four-triple endpoint, preserve the exact move and potential words immediately.
3. Replay the path independently and verify the endpoint permutations.
4. Commit `5 -> 4` data, verifier, theorem note and proof ledger.
5. Combine that upper path with AC5nz to prove exact barrier 10.
6. Update this handoff after the logical unit.
7. Repeat through four, three, two, one and zero triples.
8. Once zero is reached, add a standalone verifier from the installed 75-triple state to the terminal state.

## Validation commands

```text
g++ -O3 -std=c++20 scripts/verify_ac_p31_recovered_tail.cpp -o verify_tail
./verify_tail

g++ -O3 -std=c++20 scripts/verify_ac_p31_five_triple_frontier.cpp -o verify_five
./verify_five 9

python scripts/verify_ac_p31_five_triple_core.py
```

## Uncommitted files

No completed source or data file is waiting to be committed. Only temporary search logs and active processes are uncommitted.

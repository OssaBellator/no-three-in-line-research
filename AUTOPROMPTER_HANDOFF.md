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

Complete the explicit `p=31`, `n=30` trajectory from the strongest alternating-star successor to a zero-triple configuration, retaining exact switch addresses and exact minimax barriers.

## Durable trajectory status

### Existing path to six

The branch ancestry contains the committed 154-switch path from potential 75 to potential 6.

### Six to five: AC5nx--AC5ny

- 69 legal switches;
- maximum 10;
- complete barrier-nine component: 860 states;
- exact minimax barrier: 10;
- endpoint potential: 5.

### Five-triple lower frontier and core: AC5nz--AC5oa

- complete components at barriers 5--9: `1,2,14,100,6797`;
- no state below five;
- 812 legal immediate switches and no one-step improvement;
- unique least neighbour `r:3,27` has potential 6.

### Five to four: AC5ob--AC5oc

- 527 legal switches;
- maximum 10;
- exact minimax barrier: 10;
- endpoint potential: 4.

Artifacts:

- `data/ac-p31-five-to-four.json`
- `scripts/verify_ac_p31_five_to_four.py`
- `docs/alternating-core-p31-five-to-four.md`
- `proofs/frontier-ac-p31-five-to-four.md`

### Four-triple frontier and route to three: AC5od--AC5of

- four current triples;
- 810 legal immediate switches and no one-step improvement;
- complete lower components at barriers 4--8: `1,1,5,29,465`;
- 35-switch upper path with maximum 9;
- exact minimax barrier: 9;
- endpoint potential: 3.

Artifacts:

- `data/ac-p31-four-triple-core.json`
- `scripts/verify_ac_p31_four_triple_core.py`
- `scripts/verify_ac_p31_four_triple_frontier.cpp`
- `data/ac-p31-four-to-three.json`
- `scripts/verify_ac_p31_four_to_three.py`
- `docs/alternating-core-p31-four-triple-frontier.md`
- `proofs/frontier-ac-p31-four-triple-frontier.md`

## Current durable branch head before this handoff update

`40b27d8e9dc7b286e75c1aef66ed8a6445b3006d`

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

## Current uncommitted work

No completed file is waiting to be committed. The next computation has not yet started at this checkpoint.

## Exact next steps

1. Build the physical three-triple core atlas.
2. Enumerate complete lower sublevels from the three-triple state.
3. Search for and replay a path to potential two.
4. Commit data, verifier, theorem note and proof ledger for that logical unit.
5. Continue through one and zero triples.
6. Once zero is reached, add a standalone verifier from the installed 75-triple state to the terminal state.
7. Update this handoff after every completed segment or material blocker.

## Validation commands

```text
python scripts/verify_ac_p31_five_to_four.py
python scripts/verify_ac_p31_four_triple_core.py

g++ -O3 -std=c++20 scripts/verify_ac_p31_four_triple_frontier.cpp -o verify_four
./verify_four

python scripts/verify_ac_p31_four_to_three.py
```

## Blockers

- No durable three-to-two, two-to-one or one-to-zero segment exists yet.
- Uniform AC arithmetic and repair predicates remain open.
- No theorem guarantees terminal paths uniformly across prime-minus-one seeds.

# AUTOPROMPTER HANDOFF

Checkpoint updated: 2026-08-02 20:52 Australia/Melbourne.

## Repository and current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Active branch: `agent/ac-p31-tail-recovery`
- Parent branch: `agent/ac-p31-explicit-switch-frontier`
- Active research track: alternating core (AC) only.
- Historical side branches remain frozen source libraries.
- No pull request or merge has been requested or created.

## Goal

Complete the explicit `p=31`, `n=30` two-permutation trajectory from the strongest alternating-star successor to a zero-triple configuration, retaining exact physical switches and exact minimax barrier certificates at every low-potential checkpoint.

The broader goal remains a uniform AC theorem for the intended prime-minus-one initial-state class. AC6 and the general no-three-in-line conjecture remain open.

## Completed and committed work

### Existing ancestry

The branch ancestry contains the AC manifest architecture, the complete explicit `p=19`, `n=18` zero-triple certificate, the prime-minus-one seed census and the committed explicit `p=31` trajectory from potential 75 to potential 6 in 154 switches.

### Six triples to five

Artifacts:

- `data/ac-p31-tail-six-to-five.json`
- `scripts/verify_ac_p31_tail_six_to_five.py`
- `docs/alternating-core-p31-six-to-five-tail.md`
- `proofs/frontier-ac-p31-six-to-five-tail.md`

Results:

- lower components at barriers `6,7,8,9`: `1,9,33,860`;
- exact barrier: `10`;
- path length: `26` switches;
- endpoint potential: `5`;
- recovery processed/discovered counts: `65,865 / 75,945`.

### Five triples to four

Artifacts:

- `data/ac-p31-tail-five-to-four.json`
- `scripts/verify_ac_p31_tail_five_to_four.cpp`
- `docs/alternating-core-p31-five-to-four-tail.md`
- `proofs/frontier-ac-p31-five-to-four-tail.md`

Results:

- lower components at barriers `5,6,7,8,9`: `1,2,18,68,501`;
- exact barrier: `10`;
- path length: `32` switches;
- endpoint potential: `4`;
- recovery processed/discovered counts: `182,766 / 223,692`.

The durable explicit trajectory now reaches potential four in `154+26+32=212` switches after the alternating-star installation.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains its layer and exact row pair.
3. Every barrier lower bound requires complete sublevel-component exhaustion.
4. Every upper path is replayed with exact determinant potential and permutation/disjointness checks.
5. Long searches use durable accepted-state and predecessor checkpoints.
6. Each recovered segment is committed before the next long search.
7. Do not create a pull request or merge unless explicitly requested.

## Blockers

- The exact four-to-three move array remains absent from repository history and must be regenerated.
- The three-triple sublevel quotient is large and needs durable checkpoint serialization.
- No uniform theorem currently guarantees a terminal path for all prime-minus-one seeds.
- The physical AC1 arithmetic conversion, repair-layer predicates and source-compatibility predicates remain open in the uniform argument.

## Uncommitted work

- Regeneration of the exact four-to-three barrier-ten path.
- Durable exact search from three triples toward two.
- Any future `3 -> 2 -> 1 -> 0` certificate.

No completed logical unit is intentionally left only in chat at this checkpoint.

## Exact next steps

1. Start from the four-triple endpoint in `data/ac-p31-tail-five-to-four.json`.
2. Recompute complete lower components through barrier nine.
3. Regenerate the barrier-ten path to potential three with a durable predecessor checkpoint.
4. Commit data, exact verifier, theorem note and proof ledger.
5. Add a combined replay verifier from potential 75 through three.
6. Update this handoff.
7. Begin the exact three-triple search toward two with checkpoint files durable before a long run.
8. Continue through one and zero triples.

## Current remote checkpoint

The latest completed proof ledger before this handoff update is commit `36d8078b4adb483a8261c3ac1d29739fe6fc93c9` on `agent/ac-p31-tail-recovery`.

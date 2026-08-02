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

Complete the explicit `p=31`, `n=30` two-permutation trajectory from the strongest alternating-star successor to a zero-triple configuration. Every low-potential step must retain exact physical switch addresses, exact determinant potentials, and complete lower-sublevel exhaustion certificates.

The broader goal remains a uniform AC theorem for the intended prime-minus-one initial-state class. AC6 and the general no-three-in-line conjecture remain open.

## Completed and committed work

### Existing ancestry

The branch ancestry contains:

- the AC schema, operation, bounded-epoch, atlas, rank, ordinal, exception and initial-state manifest compilers;
- the complete explicit `p=19`, `n=18` zero-triple certificate and its recorded-state compression;
- the finite prime-minus-one seed census through `p=37`;
- the committed explicit `p=31` trajectory from potential `75` to potential `6` in 154 switches.

### Newly recovered six-to-five unit

The exact six-to-five tail is now repository-backed.

Artifacts:

- `data/ac-p31-tail-six-to-five.json`
- `scripts/verify_ac_p31_tail_six_to_five.py`
- `docs/alternating-core-p31-six-to-five-tail.md`
- `proofs/frontier-ac-p31-six-to-five-tail.md`

Results:

- complete components at barriers `6,7,8,9` have sizes `1,9,33,860` and contain no lower state;
- a 26-switch legal path reaches potential `5` inside barrier `10`;
- exact minimax barrier from the committed six-triple state is `10`;
- deterministic recovery ledger: `65,865` accepted states processed and `75,945` states discovered before the first lower endpoint;
- the explicit trajectory is now durable through potential `5`, using 180 switches after the alternating-star installation.

The replay verifier was run locally against exact determinant counts and passed.

## Current decisions and proof standards

1. AC remains the only active track.
2. Every switch keeps its layer and exact ordered row pair.
3. A barrier lower bound requires complete sublevel-component exhaustion.
4. A candidate path is accepted only after exact physical replay and determinant counting.
5. Heuristic or goal-directed searches may locate candidates but never establish lower bounds.
6. Each recovered tail segment is committed as a separate logical unit before the next long search.
7. Do not create a pull request or merge unless explicitly requested.

## Blockers

- The exact five-to-four and four-to-three move arrays remain absent from repository history and must be regenerated.
- The three-triple barrier-nine quotient is expected to be large and needs durable checkpoint serialization before another long run.
- No uniform theorem currently guarantees a terminal path for all prime-minus-one seeds.
- The physical AC1 arithmetic conversion, repair-layer predicates and source-compatibility predicates remain open in the uniform argument.

## Uncommitted work

- Regeneration of the exact five-to-four barrier-ten path.
- Regeneration of the exact four-to-three barrier-ten path.
- Durable exact search from three triples toward two.
- Any future `3 -> 2 -> 1 -> 0` certificates.

No completed source or data unit is intentionally left only in chat at this checkpoint.

## Exact next steps

1. Start from the five-triple endpoint in `data/ac-p31-tail-six-to-five.json`.
2. Recompute complete lower components through barrier nine.
3. Regenerate the exact barrier-ten path to potential four.
4. Commit its data, replay verifier, theorem note and proof ledger as a separate unit.
5. Update this handoff.
6. Repeat from four triples to recover the exact path to three.
7. Add a combined verifier for the durable trajectory from potential 75 through potential 3.
8. Resume the three-triple exact quotient search with checkpoint serialization committed before long computation.

## Current remote checkpoint

The latest completed proof ledger before this handoff update is commit `7442a680e3d373ba86bbf260f6d92b959731fa3d` on `agent/ac-p31-tail-recovery`.

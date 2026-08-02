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

Complete the explicit `p=31`, `n=30` two-permutation trajectory from the strongest alternating-star successor to a zero-triple configuration, retaining exact physical switch addresses and complete minimax barrier certificates.

The broader goal remains a uniform AC theorem for the intended prime-minus-one initial-state class. AC6 and the general no-three-in-line conjecture remain open.

## Completed and committed work

### Durable trajectory through three triples

The original committed 154-switch path reaches potential six. Three recovered exact tail segments now extend it:

- `6 -> 5`: 26 switches, exact barrier 10, lower components `1,9,33,860`;
- `5 -> 4`: 32 switches, exact barrier 10, lower components `1,2,18,68,501`;
- `4 -> 3`: 41 switches, exact barrier 10, lower components `1,2,10,29,286,2033`.

The repository-backed trajectory reaches potential three in 253 switches after the alternating-star installation.

Key new artifacts:

- `data/ac-p31-tail-six-to-five.json`
- `data/ac-p31-tail-five-to-four.json`
- `data/ac-p31-tail-four-to-three.json`
- their exact replay/component verifiers, theorem notes and proof ledgers;
- `scripts/verify_ac_p31_trajectory_through_three.py` for the combined trajectory.

### Three-triple lower components

Artifacts:

- `data/ac-p31-three-triple-lower-components.json`
- `scripts/verify_ac_p31_three_triple_lower_components.cpp`
- `docs/alternating-core-p31-three-triple-lower-components.md`
- `proofs/frontier-ac-p31-three-triple-lower-components.md`

Exact component sizes:

- barrier 3: `1`;
- barrier 4: `2`;
- barrier 5: `5`;
- barrier 6: `16`;
- barrier 7: `80`;
- barrier 8: `1159`.

None contains a two-triple state, so the certified next barrier lower bound is nine.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains its layer and exact row pair.
3. Every barrier lower bound requires complete sublevel-component exhaustion.
4. Every upper path is replayed with exact determinant potential and permutation/disjointness checks.
5. Long searches use durable accepted-state and predecessor checkpoints.
6. Symmetry quotienting is permitted only when returned paths are lifted and replayed in physical coordinates.
7. Each completed segment or exhausted component is committed before the next larger search.
8. Heuristic searches may locate candidates but never prove lower bounds.
9. Do not create a pull request or merge unless explicitly requested.

## Blockers

- Barrier nine from the committed three-triple state is not yet exhausted.
- No repository-backed three-to-two path exists.
- The expected barrier-nine quotient is large and requires durable serialization.
- No uniform theorem currently guarantees a terminal path for all prime-minus-one seeds.
- The physical AC1 arithmetic conversion, repair-layer predicates and source-compatibility predicates remain open in the uniform argument.

## Uncommitted work

- A durable symmetry-quotient search implementation for barrier nine.
- The barrier-nine accepted-state queue and predecessor forest.
- Any `3 -> 2 -> 1 -> 0` path.

No completed theorem or path unit is intentionally left only in chat at this checkpoint.

## Exact next steps

1. Commit a resumable barrier search tool that serializes canonical states, queue position, parent edge and physical lift data.
2. Start the barrier-nine search from the endpoint in `data/ac-p31-tail-four-to-three.json`.
3. Checkpoint frequently and preserve the complete predecessor forest.
4. If a canonical state of potential at most two appears, lift its path and replay every physical switch before committing it.
5. If the quotient exhausts, commit the exact quotient size, prove the quotient covers the physical component, and raise the barrier lower bound to ten.
6. Continue at the next barrier and then through one and zero triples.
7. Update this handoff after the search tool commit and after every completed component/path.

## Current remote checkpoint

The latest completed proof ledger before this handoff update is commit `f571ff1a3fc3d2ef30c96959a50336e0ef49253a` on `agent/ac-p31-tail-recovery`.

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

The repository-backed path reaches potential three in 253 switches after the alternating-star installation:

- `75 -> 6`: 154 switches;
- `6 -> 5`: 26 switches, exact barrier 10;
- `5 -> 4`: 32 switches, exact barrier 10;
- `4 -> 3`: 41 switches, exact barrier 10.

All four path blocks have exact replay data and verifiers. `scripts/verify_ac_p31_trajectory_through_three.py` audits the complete chain.

### Three-triple lower components

Exact complete component sizes at barriers `3,4,5,6,7,8` are

`1,2,5,16,80,1159`.

None contains a two-triple state, so the certified barrier lower bound is nine.

Artifacts:

- `data/ac-p31-three-triple-lower-components.json`
- `scripts/verify_ac_p31_three_triple_lower_components.cpp`
- theorem note and proof ledger.

### Durable quotient search implementation

Committed:

- `scripts/search_ac_p31_three_triple_quotient.cpp`

The tool:

- canonicalizes under all eight square symmetries and layer interchange;
- stores one actual physical representative for every canonical orbit;
- preserves the physical parent switch, so returned paths need no abstract relabelling;
- serializes canonical keys, physical representatives, queue position, parent indices, moves and potentials;
- writes checkpoints atomically;
- emits a replayable result file immediately when a lower state is found.

The implementation was tested at barrier eight and reproduced all `1159` physical states with no accidental orbit collapse.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains its layer and exact row pair.
3. Every barrier lower bound requires complete sublevel-component exhaustion.
4. Every upper path is replayed with exact determinant potential and permutation/disjointness checks.
5. Long searches use durable accepted-state and predecessor checkpoints.
6. Symmetry quotienting is valid only because one reachable physical representative is stored and expanded for every orbit.
7. Each completed segment or exhausted component is committed before the next larger search.
8. Heuristic searches may locate candidates but never prove lower bounds.
9. Do not create a pull request or merge unless explicitly requested.

## Current blocker

Barrier nine from the committed three-triple state is not yet exhausted, and no repository-backed three-to-two path exists.

## Uncommitted work

- The local barrier-nine quotient checkpoint and predecessor forest while the computation is incomplete.
- Any `3 -> 2 -> 1 -> 0` path.

No completed theorem or path unit is intentionally left only in chat at this checkpoint.

## Exact next steps

1. Compile `scripts/search_ac_p31_three_triple_quotient.cpp`.
2. Run barrier nine in bounded checkpoint chunks.
3. If a two-triple state is found, replay its stored physical path and commit the segment.
4. If the quotient exhausts, commit the exact quotient size and a theorem that orbit exhaustion excludes every physical barrier-nine path.
5. Proceed to barrier ten only after the barrier-nine result is durable.
6. Continue through one and zero triples.
7. Update this handoff after every completed component or path.

## Current remote checkpoint

The durable search implementation is commit `4edd6083ad0ee46e6664a3015a9d8bcb04a7c29b` on `agent/ac-p31-tail-recovery`.

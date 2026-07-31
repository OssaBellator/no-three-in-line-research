# AUTOPROMPTER HANDOFF

Checkpoint updated: 2026-07-31 12:31 Australia/Melbourne.

## Repository and current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Active branch: `agent/ac-p31-three-triple-frontier`
- Branch parent: `agent/ac-p31-explicit-switch-frontier` at shared research base `c00e4673c28b0cfd8c5e1508f3f671bfa1b5336e`.
- Active research track: alternating core (AC) only.
- Historical side branches remain frozen source libraries.
- No pull request, merge, issue, or main-branch modification has been requested or created for this branch.

## Goal

Complete the explicit prime-minus-one trajectory for `p=31`, `n=30` from the strongest alternating-star successor to a zero-triple configuration, retaining exact physical switch addresses and exact minimax barrier certificates at every low-potential checkpoint.

The broader goal remains a uniform AC theorem for the intended prime-minus-one initial-state class. AC6 and the general no-three-in-line conjecture remain open.

## Completed and committed work

### AC architecture

The branch ancestry contains the AC-only schema, operation, bounded-epoch serializer, atlas, rank-extension, ordinal-descent, exception-ledger, reachable-cofinality, and initial-state manifest compilers. These are conditional finite interfaces and exact failure routers; they do not replace physical geometric data.

### Explicit `p=19`, `n=18` terminal certificate

A complete explicit two-permutation no-three-in-line configuration of size `36=2n` is committed and independently replayable.

Key artifacts include:

- `data/ac-explicit-p19-an-seed.json`
- `data/ac-p19-switch-trajectory.json`
- `data/ac-p19-zero-certificate.json`
- `data/ac-p19-path-compression.json`
- `scripts/verify_ac_explicit_p19_an_seed.py`
- `scripts/verify_ac_explicit_p19_zero_certificate.py`
- `scripts/verify_ac_p19_path_compression.py`
- corresponding theorem notes and proof ledgers.

The raw post-installation route has 389 switches. The exact shortest route inside the recorded-state graph has 357 switches, so the compressed manifest uses 358 operations including the initial alternating-star installation.

### Prime-minus-one seed census

The committed census covers tested primes `11,13,17,19,23,29,31,37` for the exact two-hyperbola / one rectangle-switch / at-least-seven-secant-pair seed family.

At `p=31`:

- 216 retained seven-or-more-pair seed orientations were enumerated;
- 140 orientations have an improving alternating-star bank state;
- 76 are nonimproving;
- the strongest recorded seed lowers the exact triple potential from 108 to 75;
- the canonical nonimproving seed has 1,088 legal bank states and enters the physical AC1 rank-one branch, concentrated at anchor cell `(12,12)`.

Committed artifacts include:

- `data/ac-prime-seed-census.json`
- `scripts/verify_ac_prime_seed_census.py`
- `docs/alternating-core-prime-seed-census.md`
- `docs/alternating-core-p31-complete-seed-census.md`
- associated proof ledger.

### Explicit committed `p=31` trajectory through three triples

The strongest `p=31` alternating-star successor at potential 75 now has a committed 254-switch legal two-row-switch trajectory to potential 3.

The original 154-switch prefix reaches six triples. The committed barrier-ten extension adds:

- `6 -> 5`: 26 switches, exact minimax barrier 10;
- `5 -> 4`: 32 switches, exact minimax barrier 10;
- `4 -> 3`: 42 switches, exact minimax barrier 10.

Exact lower-component evidence:

- at six triples, barrier components 6,7,8,9 have sizes `1,9,33,860`;
- at five triples, barrier components 6,7,8,9 have sizes `2,18,68,501`;
- at four triples, barrier components 5,6,7,8,9 have sizes `2,10,29,286,2033`.

Committed artifacts on the active branch:

- `data/ac-p31-barrier-ten-extension.json`
- `scripts/verify_ac_p31_barrier_ten_extension.cpp`
- `docs/alternating-core-p31-barrier-ten-extension.md`
- `proofs/frontier-ac-p31-three-triple-frontier.md`

The cumulative physical trajectory has 254 switches from potential 75 to potential 3. Every state is an ordered pair of disjoint permutation layers and every transition is one legal two-row switch.

## Current unresolved computation

The active mathematical checkpoint is the committed three-triple endpoint of AC5oa.

An exact symmetry-quotiented barrier-nine breadth-first search was in progress to determine whether a two-triple state exists inside the sublevel.

Latest reliable session ledger before this continuity checkpoint:

- at least `1,896,669` quotient states discovered;
- at least `1,852,251` quotient states processed;
- no two-triple state found at that point;
- the queue had not closed;
- therefore no claim that barrier 10 is necessary has been proved.

A separate barrier-ten goal search may be used to locate a candidate path, but no repository-backed `3 -> 2` path currently exists.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch certificate retains the layer (`r` or `b`) and exact row pair.
3. Every barrier lower bound requires complete sublevel-component exhaustion.
4. Goal-directed or stochastic search may locate candidates, but every candidate must be replayed exactly and kept separate from lower-bound claims.
5. State potential is the exact number of real collinear triple occurrences.
6. Every state remains two disjoint permutation layers, with one point from each layer in every row and column.
7. Symmetry quotienting may reduce search, but every returned path must be lifted and replayed in physical coordinates.
8. Do not infer missing move arrays from summary statistics.
9. Do not create a pull request or merge unless explicitly requested.
10. Commit completed theorem/data/verifier/proof-ledger units before beginning a new frontier branch.

## Blockers

- The three-triple barrier-nine quotient is large and needs durable checkpoint serialization before another session interruption.
- No committed physical path exists from three triples to two, one, or zero.
- No uniform theorem currently guarantees a terminal path for all prime-minus-one seeds.
- The physical AC1 arithmetic conversion, repair-layer predicates, and source-compatibility predicates remain open in the uniform argument.

## Uncommitted work

- The in-progress three-triple barrier-nine quotient queue and predecessor forest were not available as repository files in this checkpoint tool session.
- Session-only processed/discovered counters are recorded above for continuity, but they are not theorem claims and must be regenerated or recovered before commitment.
- Any future `3 -> 2 -> 1 -> 0` paths, exact lower-component exhaustions, or symmetry-quotient checkpoints remain uncommitted.

No additional local source file or checkpoint artifact is accessible in this tool session. All completed, reviewable repository artifacts currently available are committed on the active branch.

## Exact next steps

1. Checkout or read `agent/ac-p31-three-triple-frontier`.
2. Compile and run `scripts/verify_ac_p31_barrier_ten_extension.cpp` to reconstruct and replay the committed 75-to-3 trajectory.
3. Reconstruct the committed three-triple endpoint from `data/ac-p31-barrier-ten-extension.json`.
4. Implement or recover durable serialization for the symmetry-quotiented barrier-nine queue, visited set, predecessor forest, processed index, and exact search schema/version.
5. Resume the exact barrier-nine search. If it exhausts, commit the component size as a lower-bound certificate and begin barrier 10. If it finds a two-triple state, lift the predecessor path to physical switches and replay it exactly before committing.
6. Keep a barrier-ten goal search separate as a candidate locator; never use it as a lower-bound proof.
7. Store any completed `3 -> 2` segment in a new versioned data file with exact move array, potential word, endpoint permutations, search counts, and lower-component evidence.
8. Add or extend a standalone verifier that replays the full 75-to-2 path and independently checks every claimed lower component.
9. Commit the data, verifier, theorem note, and proof ledger as one reviewable unit on a child branch.
10. Repeat checkpoint by checkpoint through `2 -> 1 -> 0`.
11. After a terminal `p=31` certificate is complete, compare its low-potential cores with the `p=19` certificate and extract reusable physical repair templates.
12. Return to the uniform AC1/AC2 arithmetic and source predicates only after the explicit `p=31` terminal frontier is settled.

## Checkpoint scope

This handoff update is repository continuity work only. No new theorem, search, construction, or project work was started while creating this checkpoint.

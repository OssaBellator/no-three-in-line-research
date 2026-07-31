# AUTOPROMPTER HANDOFF

Checkpoint updated: 2026-07-31 12:52 Australia/Melbourne.

## Repository and current branch

- Repository: `OssaBellator/no-three-in-line-research`
- Active branch: `agent/ac-p31-explicit-switch-frontier`
- Active research track: alternating core (AC) only.
- Historical side branches remain frozen source libraries.
- No pull request or merge has been requested or created for this branch.

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

### Explicit committed `p=31` frontier through six triples

The strongest `p=31` alternating-star successor at potential 75 has a committed 154-switch legal two-row-switch trajectory to potential 6.

Committed artifacts:

- `data/ac-p31-explicit-switch-frontier.json`
- `scripts/verify_ac_p31_switch_frontier.cpp`
- `docs/alternating-core-explicit-p31-switch-frontier.md`
- `proofs/frontier-ac-p31-explicit-switch-frontier.md`

Committed exact barriers:

- `13 -> 12`: 16;
- `12 -> 11`: 13;
- `11 -> 10`: 11;
- `10 -> 9`: 12;
- `9 -> 8`: 12;
- `8 -> 7`: 12;
- `7 -> 6`: 11.

At the committed six-triple state, complete components at barriers 6, 7, 8, and 9 have sizes `1, 9, 33, 860` and contain no lower state.

## Completed session results not yet materialized as repository certificates

The following results were obtained and replay-checked during the interrupted research session. Their exact move arrays and predecessor forests are not present in the repository and must be regenerated before they become repository-backed theorem claims.

### Six triples to five

- Complete lower component through barrier 9 exhausted.
- A 26-switch path reaches potential 5 inside barrier 10.
- Exact minimax barrier: 10.
- Search ledger: 65,864 accepted states processed; 75,944 sublevel states discovered before finding the lower endpoint.

### Five triples to four

- Complete lower components through barrier 9 exhausted.
- Component sizes at barriers 6, 7, 8, 9: `2, 18, 68, 501`.
- A 32-switch path reaches potential 4 inside barrier 10.
- Exact minimax barrier: 10.
- Search ledger: 182,765 accepted states processed; 223,691 sublevel states discovered before finding the lower endpoint.

### Four triples to three

- Complete lower components through barrier 9 exhausted.
- Component sizes at barriers 5, 6, 7, 8, 9: `2, 10, 29, 286, 2033`.
- A 42-switch path reaches potential 3 inside barrier 10.
- Exact minimax barrier: 10.
- The path was replay-verified during the session, but its physical move array was not committed and must be regenerated from an exact predecessor search.

These three segments would extend the explicit `p=31` trajectory from potential 75 to potential 3, using 254 switches after the alternating-star installation, but the repository-backed endpoint remains potential 6 until recovery and commit.

## Current unresolved computation

The active mathematical checkpoint is the explicit three-triple state reached by the uncommitted `4 -> 3` segment.

An exact symmetry-quotiented barrier-nine breadth-first search was in progress to determine whether a two-triple state exists inside the sublevel.

Latest reliable session ledger:

- at least 1,896,669 quotient states discovered;
- at least 1,852,251 quotient states processed;
- no two-triple state found at that point;
- the queue had not closed;
- therefore no claim that barrier 10 is necessary has been proved.

No repository-backed `3 -> 2` path exists. Any barrier-ten candidate search remains exploratory until its physical path is lifted and replayed.

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

## Blockers

- The exact physical move arrays for the completed session segments `6 -> 5`, `5 -> 4`, and `4 -> 3` were not preserved in repository files.
- No local workspace artifacts are available in this checkpoint tool session, so there are no additional reviewable source or data files available to commit beyond this continuity update.
- The three-triple barrier-nine quotient is large and needs durable checkpoint serialization.
- No uniform theorem currently guarantees a terminal path for all prime-minus-one seeds.
- The physical AC1 arithmetic conversion, repair-layer predicates, and source-compatibility predicates remain open in the uniform argument.

## Uncommitted work

- Regeneration of the exact 26-switch `6 -> 5` path.
- Regeneration of the exact 32-switch `5 -> 4` path.
- Regeneration of the exact 42-switch `4 -> 3` path.
- Durable serialization of the three-triple barrier-nine quotient queue and predecessor forest.
- Any future `3 -> 2 -> 1 -> 0` paths or lower-component exhaustions.

No uncommitted source file is currently accessible in this tool session; the items above are research results requiring reconstruction, not hidden files waiting to be staged.

## Exact next steps

1. Checkout or read `agent/ac-p31-explicit-switch-frontier`.
2. Compile and run `scripts/verify_ac_p31_switch_frontier.cpp` to reconstruct the committed six-triple state from `data/ac-p31-explicit-switch-frontier.json`.
3. Re-run the exact barrier-10 search from six triples and persist the 26-switch `6 -> 5` path, potentials, lower-component ledger, and processed/discovered counts.
4. Repeat from five triples to recover the 32-switch `5 -> 4` path and lower-component data.
5. Repeat from four triples to recover the 42-switch `4 -> 3` path and exact barrier-nine component sizes.
6. Store recovered segments in a new versioned data file; do not overwrite the original six-triple frontier until replay verification passes.
7. Add a standalone verifier that reconstructs the 75-triple installed state, replays all segments through potential 3, checks disjoint permutations and exact potentials, and independently exhausts all claimed lower components.
8. Commit the recovered `75 -> 3` certificate, theorem note, verifier, and proof ledger on a child branch.
9. Resume the exact three-triple barrier-nine quotient search with durable checkpoint files. If it exhausts, begin barrier 10; if it finds a two-triple state, lift and replay the path before committing.
10. Continue checkpoint by checkpoint through `3 -> 2 -> 1 -> 0`.

## Checkpoint scope

This handoff update is repository continuity work only. No new project theorem, search, or construction was started while creating this checkpoint.

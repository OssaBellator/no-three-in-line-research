# AUTOPROMPTER HANDOFF

## Repository

- Repository: `OssaBellator/no-three-in-line-research`
- Active branch: `agent/ac-p31-explicit-switch-frontier`
- Active research track: alternating core (AC) only
- Historical side branches are frozen source libraries.
- No pull request or merge has been requested or created for this branch.

## Goal

Continue the AC physical-data program, with the immediate concrete target of completing the explicit prime-minus-one trajectory for `p=31`, `n=30` from the strongest alternating-star successor to a zero-triple configuration, while preserving exact minimax barrier certificates and occurrence-faithful switch records.

The broader goal remains a uniform AC theorem for the intended prime-minus-one initial-state class. AC6 and the general no-three-in-line conjecture remain open.

## Completed and committed work

### AC architecture and manifest stack

The branch ancestry contains the AC-only schema, operation, bounded-epoch, atlas, rank, ordinal, exception-ledger, reachable-cofinality, and initial-state manifest compilers. These are conditional finite interfaces and exact failure routers; they do not substitute for physical geometry population.

### Explicit `p=19`, `n=18` certificate

A fully explicit two-permutation no-three-in-line configuration of size `36=2n` was constructed and committed.

Key committed artifacts include:

- `data/ac-explicit-p19-an-seed.json`
- `data/ac-p19-switch-trajectory.json`
- `data/ac-p19-zero-certificate.json`
- `data/ac-p19-path-compression.json`
- `scripts/verify_ac_explicit_p19_an_seed.py`
- `scripts/verify_ac_explicit_p19_zero_certificate.py`
- `scripts/verify_ac_p19_path_compression.py`
- corresponding theorem notes and proof ledgers.

The raw post-installation path has 389 switches; the exact shortest route inside the recorded-state graph has 357 switches, so the complete manifest uses 358 physical operations including the initial alternating-star installation.

### Prime-minus-one seed census

The committed census covers tested primes `11,13,17,19,23,29,31,37` for the exact two-hyperbola / one rectangle-switch / at-least-seven-secant-pair seed family.

At `p=31`:

- 216 retained seven-or-more-pair seed orientations were enumerated;
- 140 orientations have an improving alternating-star bank state;
- 76 are nonimproving;
- the strongest recorded seed lowers the exact triple potential from `108` to `75`;
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

The committed checkpoint barriers are:

- `13 -> 12`: exact barrier 16;
- `12 -> 11`: exact barrier 13;
- `11 -> 10`: exact barrier 11;
- `10 -> 9`: exact barrier 12;
- `9 -> 8`: exact barrier 12;
- `8 -> 7`: exact barrier 12;
- `7 -> 6`: exact barrier 11.

At the committed six-triple state, the complete components at barriers 6, 7, 8, and 9 have sizes `1, 9, 33, 860` and contain no lower state.

## Completed locally but not yet materialized in repository files

These results were obtained and replay-checked during the current session, but their exact move arrays and predecessor forests were not committed before the workspace context was interrupted. They must not be cited as repository-backed theorems until reconstructed and committed.

1. **Six triples to five**
   - exact lower component through barrier 9 exhausted;
   - a 26-switch path reaches potential 5 inside barrier 10;
   - therefore the exact minimax barrier is 10;
   - search ledger: 65,864 accepted states processed and 75,944 sublevel states discovered before the lower endpoint was found.

2. **Five triples to four**
   - lower component through barrier 9 exhausted, with component sizes `2, 18, 68, 501` at barriers 6, 7, 8, 9;
   - a 32-switch path reaches potential 4 inside barrier 10;
   - therefore the exact minimax barrier is 10;
   - search ledger: 182,765 accepted states processed and 223,691 sublevel states discovered before the lower endpoint was found.

3. **Four triples to three**
   - complete lower components through barrier 9 exhausted, with component sizes `2, 10, 29, 286, 2033` at barriers 5, 6, 7, 8, 9;
   - a 42-switch path reaches potential 3 inside barrier 10;
   - therefore the exact minimax barrier is 10;
   - the move array must be reconstructed from the exact predecessor search or regenerated.

These three segments would extend the physical trajectory from 75 to 3, but they are not yet part of the committed certificate.

## Current open computation

The active unresolved checkpoint is the explicit three-triple state reached by the uncommitted `4 -> 3` segment.

An exact symmetry-quotiented barrier-nine breadth-first search was running to determine whether a two-triple state exists inside the sublevel. The most recent reliable session ledger was:

- approximately 1.9 million accepted quotient states discovered;
- approximately 1.85 million processed;
- no two-triple state found at that point;
- the queue had not closed, so no barrier-10 lower bound was proved.

A separate barrier-ten goal search was contemplated, but no repository-backed path or impossibility result exists yet.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch certificate must retain the layer (`r` or `b`) and the exact row pair.
3. Every claimed barrier lower bound must come from complete sublevel-component exhaustion, not heuristic failure.
4. Goal-directed or stochastic search may locate candidate paths, but every candidate must be replayed exactly and kept separate from lower-bound claims.
5. State potentials are exact counts of real collinear triple occurrences.
6. Two-permutation states must remain disjoint and preserve one point from each layer in every row and column.
7. Symmetry quotienting may reduce search, but every returned path must be lifted and replayed in physical coordinates.
8. Do not infer uncommitted path data from summary statistics; reconstruct it from an exact search.
9. Do not create a pull request or merge unless explicitly requested.

## Blockers

- The exact move arrays for the locally completed `6 -> 5`, `5 -> 4`, and `4 -> 3` segments were lost with the interrupted local workspace and must be regenerated.
- The three-triple barrier-nine quotient enumeration is large and must be checkpointed durably.
- No uniform theorem currently guarantees a terminal path for all prime-minus-one seeds.
- The physical AC1 arithmetic conversion, repair-layer predicates, and source-compatibility predicates remain open in the uniform argument.

## Exact next steps

1. Checkout or otherwise read `agent/ac-p31-explicit-switch-frontier`.
2. Run `scripts/verify_ac_p31_switch_frontier.cpp` in replay mode to reconstruct the committed six-triple state from `data/ac-p31-explicit-switch-frontier.json`.
3. Re-run the exact barrier-10 search from six triples and persist:
   - the 26-switch `6 -> 5` move list;
   - all potentials;
   - the exact barrier-nine component size;
   - processed/discovered ledger.
4. Repeat from the resulting five-triple state to recover the 32-switch `5 -> 4` path and exact lower components.
5. Repeat from the resulting four-triple state to recover the 42-switch `4 -> 3` path and exact lower components.
6. Append these segments to a new versioned data file rather than overwriting the original committed frontier until replay verification passes.
7. Add a standalone verifier that:
   - reconstructs the 75-triple installed state;
   - replays all committed and recovered segments;
   - checks every state is two disjoint permutations;
   - recomputes every potential;
   - independently exhausts the stated lower-barrier components.
8. Commit the recovered `75 -> 3` certificate, theorem note, verifier, and proof ledger on a child branch.
9. Resume the exact three-triple barrier-nine quotient search with durable checkpoint files. If it exhausts, barrier 10 is the next search; if it finds a lower state, replay and commit the path.
10. Continue checkpoint by checkpoint through `3 -> 2 -> 1 -> 0`.

## Repository continuity status

At handoff creation, the latest committed, repository-backed physical `p=31` endpoint remains potential 6. The later potential-5, potential-4, and potential-3 endpoints are completed session results requiring reconstruction before they become repository claims.

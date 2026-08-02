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

All path blocks have exact data and replay/component verifiers. `scripts/verify_ac_p31_trajectory_through_three.py` audits the complete chain.

### Three-triple lower components

Complete component sizes at barriers `3,4,5,6,7,8` are

`1,2,5,16,80,1159`.

None contains a two-triple state, so the certified minimax lower bound is nine.

### Durable search implementation

Committed tool:

- `scripts/search_ac_p31_three_triple_quotient.cpp`

It canonicalizes under the eight square symmetries and layer interchange while retaining one reachable physical representative, physical parent switch and exact potential for every orbit.

## Current exact computations

Two independent exact quotient searches are active from the committed three-triple state.

### Barrier nine: lower-bound computation

Latest durable local checkpoint:

- processed quotient states: `6,350,000`;
- discovered quotient states: `6,447,907`;
- active queue: `97,907`;
- two-triple state found: no;
- checkpoint file: `/tmp/p31_3_b9_quot.cp`;
- checkpoint size: approximately `788 MiB`;
- SHA-256: `ccfae25306ffd73abee982ce98af8302cc3c0a0cf13284df20b13699cf161157`.

The queue is incomplete. No barrier-nine exhaustion claim is proved.

### Barrier ten: upper-path computation

Latest durable local checkpoint:

- processed quotient states: `3,700,000`;
- discovered quotient states: `4,125,401`;
- active queue: `425,401`;
- two-triple state found: no;
- checkpoint file: `/tmp/p31_3_b10_quot.cp`;
- checkpoint size: approximately `504 MiB`;
- SHA-256: `2974213b2a2de879068c65e758ab92a1940b5f665f5ca3448ea959c7774b6697`.

This search is also incomplete and gives no upper path yet.

The large binary checkpoints are local execution artifacts, not repository theorem artifacts. If the workspace is lost they must be regenerated from the committed search tool and the counts above are progress records only.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains its layer and exact row pair.
3. Every barrier lower bound requires complete sublevel-component exhaustion.
4. Every upper path is replayed with exact determinant potential and permutation/disjointness checks.
5. Long searches use atomic accepted-state and predecessor checkpoints.
6. Symmetry quotienting is permitted only because one reachable physical representative is retained for every orbit.
7. Heuristic searches may locate candidates but never prove lower bounds.
8. Search progress counts are not theorem claims.
9. Do not create a pull request or merge unless explicitly requested.

## Current blockers

- Barrier nine is much larger than the initial finite components and has not exhausted after 6.35 million processed quotient states.
- Barrier ten has not produced a two-triple path after 3.7 million processed quotient states.
- The compact fixed-record implementation used locally materially reduces memory, but the committed search source still uses the earlier string-backed record representation and should be updated before future clean reruns.
- No uniform theorem currently guarantees a terminal path for all prime-minus-one seeds.
- The physical AC1 arithmetic conversion, repair-layer predicates and source-compatibility predicates remain open in the uniform argument.

## Uncommitted work

- Compact fixed-record/open-addressing implementation of the quotient search.
- Incomplete barrier-nine and barrier-ten local checkpoint files.
- Any `3 -> 2 -> 1 -> 0` path.

No completed theorem or physical path is intentionally left only in chat.

## Exact next steps

1. Update the committed quotient search tool to the compact fixed-record implementation without changing the checkpoint format.
2. Resume barrier nine until a two-triple state is found or the quotient exhausts.
3. Continue barrier ten independently as an upper-path search.
4. On a lower-state hit, emit the stored physical path, replay it exactly and commit it as a separate segment.
5. On barrier-nine exhaustion, commit the exact quotient size and proof that orbit exhaustion excludes every physical barrier-nine path.
6. Continue through one and zero triples.
7. Update this handoff after every completed component or path.

## Current remote checkpoint

This handoff update follows the committed search tool at `4edd6083ad0ee46e6664a3015a9d8bcb04a7c29b` and the prior handoff at `f0525aa033007198a2204836defb28a380a80f71` on `agent/ac-p31-tail-recovery`.

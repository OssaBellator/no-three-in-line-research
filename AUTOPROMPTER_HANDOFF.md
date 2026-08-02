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

### Existing ancestry

The branch ancestry contains the AC manifest architecture, the complete explicit `p=19`, `n=18` zero-triple certificate, the prime-minus-one seed census, and the committed explicit `p=31` trajectory from potential 75 to potential 6 in 154 switches.

### Recovered p=31 tail

#### Six to five

- data: `data/ac-p31-tail-six-to-five.json`
- verifier: `scripts/verify_ac_p31_tail_six_to_five.py`
- exact barrier: `10`
- switches: `26`
- lower components through barrier nine: `1,9,33,860`
- recovery processed/discovered counts: `65,865 / 75,945`

#### Five to four

- data: `data/ac-p31-tail-five-to-four.json`
- verifier: `scripts/verify_ac_p31_tail_five_to_four.cpp`
- exact barrier: `10`
- switches: `32`
- lower components through barrier nine: `1,2,18,68,501`
- recovery processed/discovered counts: `182,766 / 223,692`

#### Four to three

- data: `data/ac-p31-tail-four-to-three.json`
- verifier: `scripts/verify_ac_p31_tail_four_to_three.cpp`
- exact barrier: `10`
- switches: `41`
- lower components through barrier nine: `1,2,10,29,286,2033`
- recovery processed/discovered counts: `1,367,504 / 1,524,432`

The durable explicit trajectory now reaches potential three in

`154 + 26 + 32 + 41 = 253`

legal two-row switches after the alternating-star installation.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains its layer and exact row pair.
3. Every barrier lower bound requires complete sublevel-component exhaustion.
4. Every upper path is replayed with exact determinant potential and permutation/disjointness checks.
5. Long searches use durable accepted-state and predecessor checkpoints.
6. Each recovered segment is committed before the next long search.
7. Heuristic searches may locate candidates but never prove lower bounds.
8. Do not create a pull request or merge unless explicitly requested.

## Blockers

- No repository-backed three-to-two path or lower-component certificate exists yet.
- The three-triple sublevel quotient is expected to be large and requires durable checkpoint serialization.
- No uniform theorem currently guarantees a terminal path for all prime-minus-one seeds.
- The physical AC1 arithmetic conversion, repair-layer predicates and source-compatibility predicates remain open in the uniform argument.

## Uncommitted work

- A combined replay verifier from potential 75 through potential 3.
- Durable exact search from the committed three-triple endpoint toward two.
- Any future `3 -> 2 -> 1 -> 0` certificate.

No completed logical unit is intentionally left only in chat at this checkpoint.

## Exact next steps

1. Add and commit a combined verifier chaining the original 75-to-6 path with all three recovered tail data files.
2. Start from the three-triple endpoint in `data/ac-p31-tail-four-to-three.json`.
3. Enumerate complete lower components beginning at barrier three using a durable checkpoint format.
4. If a lower state is found, replay and commit the exact path before increasing the barrier.
5. If a component exhausts, commit its exact size as a lower-bound certificate before starting the next barrier.
6. Continue checkpoint by checkpoint through two, one and zero triples.
7. Update this handoff after every completed tail segment or exact component exhaustion.

## Current remote checkpoint

The latest completed proof ledger before this handoff update is commit `5c8a5a85747688c0b67d92935b253ce8d8d58353` on `agent/ac-p31-tail-recovery`.

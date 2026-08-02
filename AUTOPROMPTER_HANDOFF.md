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

Complete the explicit prime-minus-one trajectory for `p=31`, `n=30` from the strongest alternating-star successor to a zero-triple configuration. Every segment must retain exact physical switch addresses and exact minimax-barrier certificates.

The broader goal remains a uniform AC theorem for the intended prime-minus-one initial-state class. AC6 and the general no-three-in-line conjecture remain open.

## Durable completed work

### Existing ancestry

The branch ancestry contains the AC finite schema/serializer/atlas/rank/ordinal/exception/reachable-manifest architecture, the explicit `p=19`, `n=18` zero-triple certificate, its recorded-state path compression, the finite prime-minus-one seed census, and the explicit `p=31` path from potential 75 to potential 6.

The committed `p=31` six-triple frontier is in:

- `data/ac-p31-explicit-switch-frontier.json`
- `scripts/verify_ac_p31_switch_frontier.cpp`
- `docs/alternating-core-explicit-p31-switch-frontier.md`
- `proofs/frontier-ac-p31-explicit-switch-frontier.md`

It contains 154 legal two-row switches from 75 to 6 and exact checkpoint barriers through `7 -> 6`.

### Newly recovered six-to-five segment

A new repository-backed route from the committed six-triple state to potential five is complete.

Artifacts:

- `data/ac-p31-recovered-tail.json`
- `scripts/verify_ac_p31_recovered_tail.cpp`
- `docs/alternating-core-p31-recovered-six-to-five.md`
- `proofs/frontier-ac-p31-recovered-six-to-five.md`

Exact result:

- route length: `69` legal switches;
- route maximum: `10`;
- complete component inside `Phi<=9`: `860` states;
- no state in that component has potential below six;
- endpoint potential: `5`.

Therefore the exact minimax barrier from the committed six-triple state to a lower state is `10`.

New theorem labels: AC5nx--AC5ny.

## Current durable branch head

The last completed logical-unit commit before this handoff update is:

`01e4a4f29045e14afb1281354d34a77fd95f9362`

It records the frontier ledger after the data, verifier and theorem-note commits.

## Decisions and proof standards

1. AC remains the only active track.
2. Every switch retains the layer (`r` or `b`) and exact row pair.
3. A barrier lower bound requires complete sublevel-component exhaustion.
4. Heuristic or best-first search may locate an upper path, but every path is replayed exactly.
5. State potential is the exact number of real collinear triple occurrences.
6. Every state remains two disjoint permutation layers.
7. Search counts are diagnostic only unless the corresponding component is exhausted.
8. Completed segments are committed separately before beginning another risky segment.
9. Do not create a pull request or merge unless explicitly requested.

## Current uncommitted computation

A best-first exact-potential search is running locally from the new five-triple endpoint, constrained to `Phi<=10`, looking for a state of potential at most four.

Latest observed local ledger before this handoff update:

- more than `11,000` states expanded;
- more than `39,000` states discovered;
- no lower endpoint reported yet;
- the process remains active.

This search is not yet a repository theorem or certificate. No move array from it has been committed.

The previously reported chat-only `5 -> 4` and `4 -> 3` paths are intentionally not treated as durable facts because their exact arrays were not preserved. They must be regenerated from the new committed five-triple endpoint.

## Blockers

- The five-triple barrier-ten search is larger than the recovered six-triple search.
- No durable `5 -> 4`, `4 -> 3`, `3 -> 2`, `2 -> 1` or `1 -> 0` segment exists yet on this branch.
- The uniform AC1 arithmetic conversion, repair-layer predicates and source-compatibility predicates remain open.
- No theorem yet guarantees terminal paths uniformly across prime-minus-one seeds.

## Exact next steps

1. Let the current five-triple `Phi<=10` search finish or reach a useful checkpoint.
2. When a lower endpoint is found, store the exact switch and potential words.
3. Independently enumerate the complete `Phi<=9` component from the five-triple endpoint and confirm the expected no-lower-state result; do not rely on old chat counts.
4. Commit the `5 -> 4` data first, then its verifier, theorem note and proof ledger.
5. Update this handoff immediately after that logical unit.
6. Repeat the same process from four to three, then three to two, two to one and one to zero.
7. Once zero is reached, add one standalone verifier that reconstructs the installed 75-triple state and replays the complete terminal path.
8. Only after the explicit `p=31` terminal certificate is durable should work return to uniform repair-template extraction.

## Validation commands

For the newly recovered segment:

```text
g++ -O3 -std=c++20 scripts/verify_ac_p31_recovered_tail.cpp -o verify_tail
./verify_tail
```

Expected output includes:

- `moves: 69`
- `barrier: 10`
- `lower_component_9: 860`
- `final_potential: 5`

## Uncommitted files

No completed source or data file is waiting to be committed. The only uncommitted work is the active search process and any temporary local search output it may later produce.

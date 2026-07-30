# Frontier pass: exact p=31 three-triple support closure

## Active branch

`agent/ac-p31-support-closure`

Parent: `agent/ac-p31-barrier-ten-extension` at `f74af25c635c961265cf3fb8354736d93874b715`.

Only AC remains active. No pull request or merge was created.

## Theorem block

- **AC5oe:** complete support census with at most two extra layer-row addresses.
- **AC5of:** no collision-free endpoint in that census has potential below three.
- **AC5og:** every lower-potential endpoint requires at least three additional layer-row addresses.

## Exact ledger

Core support:

- red rows: `14,16,20,23`;
- blue rows: `9,14,18,20,29`.

Enumerated families:

- one red and one blue extra: `650` jobs, `56,160,000` assignments, `42,195,600` valid states;
- two red extras: `325` jobs, `28,080,000` assignments, `20,353,104` valid states;
- two blue extras: `300` jobs, `36,288,000` assignments, `28,146,816` valid states.

Totals:

- support choices: `1,275`;
- assignments: `120,528,000`;
- collision-free states: `90,695,520`;
- minimum potential: `3`.

## Deterministic audit

- `scripts/verify_ac_p31_support_mixed.cpp` exhausts the `(1,1)` family.
- `scripts/verify_ac_p31_support_same_layer.cpp rr` exhausts the `(2,0)` family.
- `scripts/verify_ac_p31_support_same_layer.cpp bb` exhausts the `(0,2)` family.

All three local executions returned the committed exact counts and minimum potential three.

## Scope

The result is an endpoint support theorem. It does not restrict a path that temporarily moves additional rows, and it does not prove that three extra addresses suffice.

## Remaining AC frontier

1. Search support expansions of size at least three.
2. Finish the exact barrier-nine component from the three-triple state.
3. Find and order a two-triple endpoint.
4. Continue through one and zero triples.
5. Extend the support argument uniformly.

AC6 and the general no-three-in-line conjecture remain open.

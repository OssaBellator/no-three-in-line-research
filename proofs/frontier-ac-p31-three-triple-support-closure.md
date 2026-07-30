# Frontier pass: exact p=31 three-triple support closure

## Active branch

`agent/ac-p31-support-closure`

Parent: `agent/ac-p31-barrier-ten-extension` at `f74af25c635c961265cf3fb8354736d93874b715`.

Only AC remains active. No pull request or merge was created.

## Theorem block

- **AC5oe:** complete support census with at most two extra tagged rows.
- **AC5of:** no collision-free endpoint in that census has potential below three.
- **AC5og:** first support-expansion lower bound.
- **AC5oh:** complete exact closure of every three-extra support.
- **AC5oi:** no three-extra endpoint has potential below three.
- **AC5oj:** every lower endpoint requires at least four additional tagged rows.

## Exact ledger

Core support:

- red rows: `14,16,20,23`;
- blue rows: `9,14,18,20,29`.

Two-extra exhaustive assignments:

- `(1,1)`: `650` supports, `56,160,000` assignments, `42,195,600` collision-free states;
- `(2,0)`: `325` supports, `28,080,000` assignments, `20,353,104` collision-free states;
- `(0,2)`: `300` supports, `36,288,000` assignments, `28,146,816` collision-free states;
- minimum potential: `3`.

Three-extra exact branch-and-bound:

- `(0,3)`: `2,300` supports and `109,579` partial states;
- `(1,2)`: `7,800` supports and `295,821` partial states;
- `(2,1)`: `8,125` supports and `276,343` partial states;
- `(3,0)`: `2,600` supports and `92,218` partial states;
- total supports: `20,825`;
- total partial states: `773,961`;
- complete states satisfying potential at most two: `0`.

Thus every potential-two, potential-one or zero-triple endpoint has at least thirteen tagged rows in its support.

## Deterministic audit

- `scripts/verify_ac_p31_support_mixed.cpp` exhausts the `(1,1)` family.
- `scripts/verify_ac_p31_support_same_layer.cpp rr` exhausts the `(2,0)` family.
- `scripts/verify_ac_p31_support_same_layer.cpp bb` exhausts the `(0,2)` family.
- `scripts/verify_ac_p31_support_three.cpp` exhausts all four three-extra distributions.

All local executions returned the committed exact ledgers. The three-extra verifier uses direct insertion increments `binom(k,2)` for the number of existing points on each line through the proposed cell; independent determinant replay was used to reject two earlier experimental count representations before this committed version.

## Scope

The result is an endpoint support theorem. It does not restrict a path that temporarily moves additional rows, and it does not prove that four extra addresses suffice.

## Remaining AC frontier

1. Search support expansions of size at least four.
2. Finish the exact barrier-nine component from the three-triple state.
3. Find and order a two-triple endpoint.
4. Continue through one and zero triples.
5. Extend the support argument uniformly.

AC6 and the general no-three-in-line conjecture remain open.

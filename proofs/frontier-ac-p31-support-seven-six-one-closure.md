# Frontier pass: exact p=31 support-seven `(6,1)` closure

## Active branch

`agent/ac-p31-support-seven-six-one-closure`

Parent: `agent/ac-p31-support-seven-one-six-closure`.

Only AC is active.

## Theorem block

- **AC5oz:** complete `(6,1)` seven-extra support census.
- **AC5pa:** no lower endpoint in that family; four of eight seven-extra distributions are closed.

## Exact ledger

- support choices: `5755750`;
- admissible partial states: `961623575`;
- complete collision-free endpoints with potential at most two: `0`;
- exact contiguous intervals: `59`.

## Verification

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_seven_range.cpp -o verify_support_seven_range
./verify_support_seven_range 6 lo hi expected_nodes
```

Run once for each ledger interval in `data/ac-p31-support-seven-six-one-closure.json`.

## Consequence

Exactly four distributions remain open: `(2,5)`, `(3,4)`, `(4,3)`, and `(5,2)`.

## Remaining frontier

1. Close or solve those four central seven-extra distributions.
2. Finish the independent barrier-nine switch component.
3. Convert any wider-support endpoint into a legal switch path.
4. Explain the support closures structurally.

AC6 and the general conjecture remain open.

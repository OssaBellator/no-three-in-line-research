# Frontier pass: exact p=31 support-seven `(1,6)` closure

## Active branch

`agent/ac-p31-support-seven-one-six-closure`

Parent: `agent/ac-p31-support-seven-extreme-closure`.

Only AC is active.

## Theorem block

- **AC5ox:** complete `(1,6)` seven-extra support census.
- **AC5oy:** no potential-at-most-two endpoint in that mixed family.

## Exact ledger

- support choices: `4604600`;
- admissible partial states: `1163897840`;
- complete collision-free endpoints with potential at most two: `0`;
- exact contiguous ledger intervals: `87`.

## Verification

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_seven_one_six.cpp -o verify_support_seven_one_six
./verify_support_seven_one_six lo hi expected_nodes
```

Run once for each interval in `data/ac-p31-support-seven-one-six-closure.json`. Every interval asserts its exact size and node count.

## Consequence

The closed seven-extra distributions are now `(0,7)`, `(1,6)`, and `(7,0)`. Any seven-extra lower endpoint must lie in one of `(2,5)`, `(3,4)`, `(4,3)`, `(5,2)`, or `(6,1)`.

## Remaining frontier

1. Close or solve the remaining mixed seven-extra families.
2. Finish the independent barrier-nine switch component.
3. Convert any wider-support endpoint into a legal switch path.
4. Explain the support closure structurally.

AC6 and the general conjecture remain open.

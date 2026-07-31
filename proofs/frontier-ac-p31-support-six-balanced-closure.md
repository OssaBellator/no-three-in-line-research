# Frontier pass: balanced p=31 support-six closure

## Active branch

`agent/ac-p31-support-six-balanced-closure`

Parent: `agent/ac-p31-support-five-closure`.

Only AC is active.

## Theorem block

- **AC5oq:** complete `(3,3)` six-extra support census.
- **AC5or:** no potential-at-most-two endpoint in the balanced six-extra family.

## Exact ledger

- support choices: `5980000`;
- admissible partial states: `577440893`;
- complete collision-free endpoints with potential at most two: `0`.

The support universe is partitioned into twelve exact lexicographic shards, each retaining its own support interval and partial-state count in `data/ac-p31-support-six-balanced-closure.json`.

## Verification

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_six_balanced.cpp -o verify_support_six_balanced
for shard in 0 1 2 3 4 5 6 7 8 9 10 11; do
  ./verify_support_six_balanced "$shard"
done
```

Every shard asserts its exact support count, partial-state count and zero complete endpoints.

## Consequence

Even the maximally balanced first six-extra family cannot lower the explicit three-triple endpoint. The remaining six-extra work is confined to the six unbalanced red/blue distributions.

## Remaining frontier

1. Close or solve the unbalanced six-extra families.
2. Finish the independent barrier-nine switch component.
3. Convert any wider-support endpoint into a legal switch path.
4. Seek a structural explanation for the closure.

AC6 and the general conjecture remain open.

# Frontier pass: extreme p=31 support-seven closure

## Active branch

`agent/ac-p31-support-seven-extreme-closure`

Parent: `agent/ac-p31-support-six-closure`.

Only AC is active.

## Theorem block

- **AC5ov:** complete all-blue and all-red seven-extra support censuses.
- **AC5ow:** neither extreme distribution contains a potential-at-most-two endpoint.

## Exact ledger

- `(0,7)`: `480700` supports, `171025856` partial states, zero complete lower endpoints;
- `(7,0)`: `657800` supports, `144149641` partial states, zero complete lower endpoints.

Combined:

- support choices: `1138500`;
- partial states: `315175497`;
- complete potential-at-most-two endpoints: `0`.

## Verification

```text
g++ -O3 -std=c++20 -fopenmp scripts/verify_ac_p31_support_seven_extreme.cpp -o verify_support_seven_extreme
for shard in 0 1 2 3 4 5 6; do
  ./verify_support_seven_extreme "$shard"
done
```

## Consequence

Seven additional addresses confined to one layer cannot repair the explicit three-triple endpoint. Any seven-extra solution must use both layers.

## Remaining frontier

1. Search the six mixed seven-extra distributions.
2. Finish the independent barrier-nine switch component.
3. Convert any wider-support endpoint into a legal switch path.
4. Explain the single-layer closure structurally.

AC6 and the general conjecture remain open.

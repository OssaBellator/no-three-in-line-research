# Component-clean row-lift experiments

These computations use
[`scripts/analyze_component_clean_row_lift.py`](../scripts/analyze_component_clean_row_lift.py)
and test the exact PP3z and spread PP3aa endpoints from
[`docs/35-component-clean-row-lift-banks.md`](../docs/35-component-clean-row-lift-banks.md).

For each case the entire old configuration is deleted, so there are no
retained-core blocked cells or anchored pairs. Every reported defect is a
cross-component triple.

## Fully deleted widths three through five

| Width `t` | All movement states | Clean movement states | All refill states | Clean refill states | Clean component pairs | Cross support triples `MMF+MFF` | Exact PP3z expectation | PP3aa bound | Minimum cross triples | Clean pairs |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 12 | 4 | 12 | 4 | 16 | `8+8` | `11` | `16` | 8 | 0 |
| 4 | 216 | 40 | 216 | 40 | 1,600 | `64+64` | `358/25` | `704/25` | 5 | 0 |
| 5 | 5,280 | 64 | 5,280 | 64 | 4,096 | `152+152` | `671/32` | `1463/16` | 8 | 0 |

Commands:

```bash
python scripts/analyze_component_clean_row_lift.py \
  certificates/prime-patching-small.json --n 3 --rows 1,2,3

python scripts/analyze_component_clean_row_lift.py \
  certificates/prime-patching-small.json --n 4 --rows 1,2,3,4

python scripts/analyze_component_clean_row_lift.py \
  certificates/prime-patching-small.json --n 5 --rows 1,2,3,4,5
```

## Spread after conditioning

| `t` | Maximum component cell probability | Maximum component pair probability |
|---:|---:|---:|
| 3 | `1` | `1` |
| 4 | `11/20` | `2/5` |
| 5 | `11/16` | `7/16` |

Conditioning each component to be internally no-three removes all within-block
triples but substantially concentrates the remaining distribution. In these
small cases PP3aa is much weaker than the exact PP3z expectation, and even the
exact expectation remains far above one.

## Interpretation

Component cleaning succeeds at its intended first task: the logarithmic
candidate-only accumulation inside each full rectangle disappears. Proposition
PP3ab bounds every fixed component pair by `O(t^2)` cross triples.

It does not yet solve the second task. The clean component families above are
small and non-spread, so their cross-incidence expectation is large. A viable
component-clean construction needs a much larger algebraic family of internally
no-three states with cell probability `O(1/t)` and pair probability
`O(1/t^2)`, rather than conditioning the complete permutation bank after the
fact.
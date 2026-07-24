# Variable-reservoir bank experiments

The generic verifier
[`scripts/analyze_variable_reservoir_bank.py`](../scripts/analyze_variable_reservoir_bank.py)
checks the state-dependent-deletion endpoint PP2l and its uniform PP2m and
deletion-blind PP2n corollaries.

## Side-four parabolic bank

The regression bank
[`parabolic-variable-bank-n4.json`](parabolic-variable-bank-n4.json)
contains all four width-two parabolic matching reservoirs in the stored `n=4`
certificate.  Every state inserts the same internally clean eight-point patch,
but deletes a different perfect matching from the old configuration.

Run:

```bash
python scripts/analyze_variable_reservoir_bank.py \
  certificates/prime-patching-small.json \
  experiments/parabolic-variable-bank-n4.json \
  --n 4 --t 2
```

The exact output has:

| Quantity | Value |
|---|---:|
| States | 4 |
| Inserted support cells | 8 |
| Geometric `C1` certificates | 14 |
| Geometric `C2` certificates | 5 |
| Exact PP2l expectation | `17/4` |
| Uniform PP2m bound | `19/2` |
| Deletion-blind PP2n bound | `19` |
| Minimum state certificate count | 3 |
| Clean states | 0 |

The certificate histogram is

```text
3 defects: 2 states
4 defects: 1 state
7 defects: 1 state
```

## Interpretation

This example demonstrates why the variable-reservoir theorem is not merely a
rephrasing of the fixed-reservoir endpoint.  The inserted patch is identical in
all four states, so insertion marginals alone see no spread at all.  Changing
the deletion matching nevertheless clears many old-pair and old-anchor
certificates: the exact deletion-aware expectation `17/4` is less than one
quarter of the deletion-blind value `19`.

The gain is not yet enough to produce a clean state.  A successful prepared
bank needs substantially more deletion diversity, lower joint certificate
probabilities, or inserted-state variation in addition to the matching choice.

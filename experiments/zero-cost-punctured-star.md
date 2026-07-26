# Zero-cost punctured-star diagnostic

Run

```text
python scripts/check_zero_cost_punctured_star.py \
  experiments/zero-cost-punctured-star-example.json
```

The stored captive centre `p` has twelve designated star entries, none controlled
by `p`, so all twelve survive the puncture.

The complete positive source/insertion support table contains four ordinary-helper
supports, all using only `h4,h5,h6,h7`.  The selected helper block

```text
{h0,h1,h2,h3}
```

is independent.  The marked cycle

```text
p,h0,h1,h2,h3
```

moves the punctured centre and selects no positive support.  Its source-invalid
count and insertion cost are therefore zero.

The expected output is

```text
punctured centre p
required ordinary helpers 4
chosen independent helpers ['h0', 'h1', 'h2', 'h3']
positive helper supports 4
selected positive supports 0
designated star credit 12
insertion cost 0
punctured-universe potential change -12
outcome zero_cost_punctured_star_nested_progress
```

This is the finite form of PP3arb--PP3are: complete-support selection retains the
full punctured-star removal credit and eliminates self-recapture and every foreign
insertion term simultaneously.

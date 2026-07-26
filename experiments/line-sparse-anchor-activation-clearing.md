# Line-sparse anchor-activation clearing diagnostic

Run

```text
python scripts/check_line_sparse_anchor_activation_clearing.py \
  experiments/line-sparse-anchor-activation-clearing-example.json
```

The stored model has twelve marked gaps, a 144-edge helper matching, and twelve target
activation lines.  Six lines have equations

```text
y=x+d,
20<=d<=25,
```

and six have offsets from `-25` through `-20`.

For each cyclic gap, a target line can exclude at most one helper through the
marked-column replacement and at most one helper through the next-marked-row
replacement.  The exact bad-helper counts are

```text
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12].
```

Thus every gap retains at least

```text
144-12=132
```

target-clean helpers.  Greedy distinct selection chooses twelve helpers successfully.

The expected output is

```text
marked size 12
helper reservoir 144
target line count 12
bad helpers by gap [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12]
maximum bad helpers 12
minimum target-clean domain 132
chosen helper indices [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14]
distinct helpers 12
outcome line_sparse_anchor_activation_clearing
```

This verifies PP3avv--PP3avx.  A target-order activation bank removes only linear
many values from each role domain, while the clearing reservoir has quadratic size.

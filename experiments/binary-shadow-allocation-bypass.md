# Binary-shadow allocation-domain diagnostic

Run

```text
python scripts/check_binary_shadow_allocation_bypass.py \
  experiments/binary-shadow-allocation-bypass-example.json
```

The stored inserted state consists of eight row/column-disjoint integer cells
with no three collinear.  It therefore determines exactly

```text
binom(8,2)=28
```

nonaxis secant lines.  The checker intersects every secant with seven movement
rows and seven refill columns and maps every integer intersection back to the
identity controller layer.

The exact diagnostic is:

```text
inserted state size              8
secant lines                    28
movement candidate entries      36
refill candidate entries        31
maximum movement-label load      9
maximum refill-label load        8
maximum movement-controller load 3
maximum refill-controller load   3
line-union degree bound          28
maximum one-domain loss           5
general domain-loss bound        56
base domain size                500
post-binary lower bound         495
allocation threshold            400
outcome                         direct_binary_shadow_bypass
```

The margin condition is

```text
s(s-1)=56 <= xi R=100.
```

Although the 28 secants create 67 candidate entries in the finite label window,
no movement or refill label and no controller edge sees more than nine of them.
The exact maximum loss from one macro-label-pair domain is five.

The checker treats the candidate-entry support as simple.  Repeating one
candidate incidence with arbitrarily large rank-three or rank-four `Xi` weight
does not change the domain deletion count, which is the distinction used by
PP3aha--PP3ahg.

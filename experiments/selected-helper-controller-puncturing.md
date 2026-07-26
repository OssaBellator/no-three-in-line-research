# Selected-helper controller-puncturing diagnostic

Run

```text
python scripts/check_selected_helper_controller_puncturing.py \
  experiments/selected-helper-controller-puncturing-example.json
```

The stored layer has controller density one.  The target marked set and the selected
helper set both have size `W=1,000`, and every selected index is initially a
controller.  Puncturing all selected marked/helper controllers therefore costs
exactly `2W=2,000` values.

At

```text
R=1,000,000,
gamma=0.4,
xi=0.2,
```

the original domain lower bound is `600,000`.  After all selected punctures it is
`598,000`, still far above the half-margin threshold `500,000`.  The puncture ratio
is only `0.002`.

The chosen helper set is support-free after controller-membership singleton rules are
removed; puncturing the selected controllers can only delete later support.

The expected output is

```text
R 1000000
W 1000
selected marked size 1000
ambient controller density 1.0
selected marked controllers 1000
selected helper controllers 1000
total selected punctures 2000
puncture to R ratio 0.002
original domain lower bound 600000.0000000001
post-puncture lower bound 598000.0000000001
half-margin threshold 500000.0
selected positive supports 0
outcome selected_helper_puncturing_bypasses_full_controller_density
```

This verifies PP3asu--PP3asx in the extremal finite model: even full controller
density is bypassed by choosing first and puncturing only the selected `2W=o(R)`
indices.

# Initial blocker-density conversion diagnostic

Run

```text
python scripts/check_initial_blocker_conversion.py \
  experiments/initial-blocker-conversion-example.json
```

The stored instance uses `m=10^20` and bad-entry density `delta=0.10`.  The
slab-scale arithmetic gives

```text
M 10
R 9999999999999979520
W 3162277660
T 31622776600
bad entries 632455531999998680686785462272
star-entry lower bound 99999999936754242000
resource-bank lower bound 1581138829
```

The three routing cases return

```text
case free: fresh_helper_free_star
case captive: one_puncture_free_star
case bank: recapture_free_resource_bank
outcome structured_initial_blocker_conversion
```

The diagnostic checks the exact resource-hypergraph lower bound

```text
U/(4MR)
```

and verifies that it retains the `T=m^(21/40+o(1))` exponent.  It then checks
that every extracted geometric branch enters an existing conversion interface:
free marked star, one-controller punctured star, or recapture-free resource bank.

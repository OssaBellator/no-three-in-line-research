# Captive controller partner-bank diagnostic

Run

```text
python scripts/check_captive_controller_partner_bank.py \
  experiments/captive-controller-partner-bank-example.json
```

Both stored stars have degree 12 and distinct designated bad entries.

The first case has eight free partners.  Five lie in one permutation layer, so it
returns

```text
controller partners          4
free partners                8
best free layer              0
free partner bank size       5
credit lower bound           5
outcome controller_preserving_free_partner_bank
```

The second case has eight controller partners and only four free partners, split
equally between the two layers.  It returns

```text
controller partners          8
free partners                4
best free layer              0
free partner bank size       2
outcome controller_controller_star_core
```

The checker verifies distinct partner points and distinct designated entries.  It
then tests the exact `C/4` free one-layer bank threshold and the `C/2`
controller-partner threshold.

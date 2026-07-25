# Transition sunflower endpoint-bank diagnostic

This finite example exercises PP3aaa--PP3aad. Its petals already share only the
fixed centre, so the JSON lists only the noncentral typed resources. The checker
verifies that no listed resource is repeated, selects a majority source layer,
and then extracts the largest free class or single-controller-pool class.

Run:

```bash
python scripts/check_transition_sunflower_bank.py \
  experiments/transition-sunflower-bank-example.json
```

The example has five anchors in layer `A`. With two controller pools, the exact
pigeonhole lower bound is `ceil(5/3)=2`; pool `0` actually supplies a bank of
three anchors and therefore three selected transition-certificate removal units.

This diagnostic checks finite resource bookkeeping. It does not check the
geometric existence of the petals or the insertion collateral of the subsequent
endpoint trade.

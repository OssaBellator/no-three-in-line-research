# Completed-state binary support diagnostic

Run:

```bash
python scripts/check_completed_state_binary_support.py \
  experiments/completed-state-binary-support-example.json
```

The stored six-cell completed state has `15` distinct nonaxis pair lines, exactly the
unordered-pair bound.  Its candidate traces satisfy the one-line-per-label/controller
degree estimate.  The largest paired macro-domain loss is `4`, below both the abstract
bound `30` and the supplied margin allowance `50`.

The stored outcome is:

```text
binary_pair_shadow_absorbed
```

The diagnostic checks finite simple-support bookkeeping only.  The asymptotic
`b^2=o(R)` conclusion is the theorem in
`docs/276-completed-state-binary-support-absorption.md`.

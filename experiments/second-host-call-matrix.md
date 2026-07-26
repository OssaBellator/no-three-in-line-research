# Second-host call-matrix diagnostic

This experiment checks the finite bookkeeping assertions in
`docs/269-complete-second-host-call-matrix-audit.md`.

The JSON instance records:

- one current potential name, `Theta_E_plus`;
- a finite block partition with marked sizes, helper supplies, role-domain losses,
  controller punctures, support ranks, and second-host outcomes;
- the five exhaustive outcome classes;
- the five named terminal interface classes; and
- one all-independent insertion-cancellation payment example.

Run:

```bash
python scripts/check_second_host_call_matrix.py \
  experiments/second-host-call-matrix-example.json
```

The checker verifies:

```text
r_j<=W,
helpers_j>=r_j^2,
role loss and punctures=O(r_j),
support rank<=3,
sum_j r_j^2<=(sum_j r_j)^2,
later removals>=first insertion multiplicity,
later insertion multiplicity=0,
composite change<=-first removal credit.
```

This is a finite regression diagnostic.  It does not establish the asymptotic
conditional Hall, alternating, non-superregular, distinguished-endpoint, or
role-host conversion interfaces.

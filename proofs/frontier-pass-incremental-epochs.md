# Frontier pass: incremental OP repair-source epochs

- OP4fx: unchanged residual/edit, unit, valuation and holonomy pairs preserve compatibility.
- OP4fy: exact next-epoch reconstruction needs only the changed boundary.
- OP4fz: the carried source assignment loses at most new incidences plus disturbed assignments.
- OP4ga: bounded reaugmentation restores the assignment or returns a unit-sensitive Hall core of no larger deficit.
- OP4gb: cumulative quotient-repair cost is the sum of boundary evaluations and churn disturbances; matching maintenance creates no source or payment mass.

Verifier: `scripts/verify_op_incremental_source_epochs.py`.

Remaining: bound quotient-profile churn, evaluate the unit-sensitive predicate on boundary pairs, and discharge returned Hall cores and source-ledger failures.
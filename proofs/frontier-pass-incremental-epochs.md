# Frontier pass: incremental SRR witness epochs

- SRR2fh: unchanged candidate/witness records preserve conditioned compatibility.
- SRR2fi: exact next-epoch reconstruction needs only the changed boundary.
- SRR2fj: the carried witness assignment loses at most new candidates plus disturbed assignments.
- SRR2fk: bounded reaugmentation restores the assignment or returns a conditioned Hall core of no larger deficit.
- SRR2fl: cumulative resampling cost is the sum of boundary evaluations and churn disturbances; matching maintenance creates no witness mass.

Verifier: `scripts/verify_srr_incremental_witness_epochs.py`.

Remaining: bound actual switching-menu churn, evaluate conditioned compatibility on boundary pairs, and discharge returned Hall cores and witness-ledger failures.
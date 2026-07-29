# Frontier pass: incremental SAS neutral epochs

- SAS5mx: unchanged pair/completion neutral records preserve compatibility.
- SAS5my: exact next-epoch reconstruction needs only the changed boundary.
- SAS5mz: the carried neutral assignment loses at most new incidences plus disturbed assignments.
- SAS5na: bounded reaugmentation restores the assignment or returns a boundary-neutral Hall core of no larger deficit.
- SAS5nb: cumulative sparse-repair cost is the sum of boundary evaluations and churn disturbances; matching maintenance creates no neutral debit mass.

Verifier: `scripts/verify_sas_incremental_neutral_epochs.py`.

Remaining: bound sparse move churn, evaluate the boundary-neutral predicate on boundary pairs, and discharge returned Hall cores and lineage failures.
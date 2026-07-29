# Frontier pass: incremental GC donor epochs

- GC2ly: unchanged donor/remedy/height pairs preserve compatibility.
- GC2lz: exact next-epoch reconstruction needs only the changed boundary.
- GC2ma: the carried donor assignment loses at most new incidences plus disturbed assignments.
- GC2mb: bounded reaugmentation restores the assignment or returns a canonical geometric Hall core of no larger deficit.
- GC2mc: cumulative cleaning cost is the sum of boundary evaluations and churn disturbances; matching maintenance creates no donor mass or height credit.

Verifier: `scripts/verify_gc_incremental_donor_epochs.py`.

Remaining: bound cleaning-menu churn, evaluate geometric compatibility on boundary pairs, and discharge returned donor Hall cores and source-ledger failures.
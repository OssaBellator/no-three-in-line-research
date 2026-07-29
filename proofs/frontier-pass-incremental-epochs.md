# Frontier pass: incremental RI collateral epochs

- RI5gr: unchanged typed collateral pairs preserve compatibility.
- RI5gs: exact next-epoch reconstruction needs only the changed pair boundary.
- RI5gt: the carried assignment leaves at most new incidences plus disturbed old assignments unmatched.
- RI5gu: at most that many augmenting paths restore a complete assignment, or a canonical typed Hall core has no larger deficit.
- RI5gv: cumulative repair cost is the sum of boundary evaluations and churn disturbances; matching maintenance creates no collateral mass.

Verifier: `scripts/verify_ri_incremental_collateral_epochs.py`.

Remaining: prove bounded physical RI churn, evaluate the arithmetic predicate on boundary pairs, and discharge returned collateral Hall cores and source-ledger failures.
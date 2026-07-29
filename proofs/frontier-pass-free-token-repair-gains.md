# Frontier pass: free-token repair gains

- Proved SRR2gc: balanced conditioned Hall cuts contain at least `m` free same-key witness tokens.
- Proved SRR2gd: one retained predicate labels at least `ceil(m|Z|/q)` unmatched-candidate/free-witness pairs.
- Proved SRR2ge: endpoint-disjoint local repairs reduce matching deficit by the number of restored pairs.
- Proved SRR2gf: repairable stars, common-witness batches, and independent stocks give descent; otherwise one rigid conditioned repair failure is returned.
- Added `scripts/verify_srr_free_token_repair_gains.py`.

Remaining: construct concrete cycle/threshold/burden repairs and prove preservation, commutation, and burden payment.
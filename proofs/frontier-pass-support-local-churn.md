# SRR frontier pass: support-local witness churn

- SRR2fq: every changed resampling record has a least touched primitive dependency, or returns a nonlocal conditioning witness.
- SRR2fr: support size `H` and primitive incidence caps bound changed candidate and witness records by `H alpha_R`, `H alpha_+`, and `H alpha_-`.
- SRR2fs: audit cost is at most `H(alpha_R L_T+alpha_+ L_R)` and witness-assignment disturbance at most `H(alpha_R+alpha_-)`.
- SRR2ft: a residual deficit `delta` has only support-caused roots; one touched cycle primitive anchors at least `ceil(delta/H)` roots.

Validation: 2,500 systems, 54,479 key-local pairs versus 233,650 full-product pairs, 16,281 disturbed roots and 10,947 residual deficits.

Remaining: construct physical bounded-cycle dependencies and prove support, incidence, conditioned-fibre and burden-payment bounds.
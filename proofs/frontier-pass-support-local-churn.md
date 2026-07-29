# BDA frontier pass: support-local restoration churn

- BDA5hj: every changed restoration record has a least touched primitive dependency, or returns a nonlocal-change witness.
- BDA5hk: support size `H` and primitive incidence caps bound changed incidences and potential tokens by `H alpha_R`, `H alpha_+`, and `H alpha_-`.
- BDA5hl: audit cost is at most `H(alpha_R L_T+alpha_+ L_R)` and potential-assignment disturbance at most `H(alpha_R+alpha_-)`.
- BDA5hm: a residual deficit `delta` has only support-caused roots; one touched primitive anchors at least `ceil(delta/H)` roots.

Validation: 2,500 systems, 55,956 key-local pairs versus 231,556 full-product pairs, 16,229 disturbed roots and 10,923 residual deficits.

Remaining: construct physical restoration dependencies and prove support, incidence, key-fibre and partner/payment bounds.
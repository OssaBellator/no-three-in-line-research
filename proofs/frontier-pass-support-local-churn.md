# RI frontier pass: support-local collateral churn

- RI5ha: every changed incidence or collateral record has a least touched primitive dependency, or returns a nonlocal-change witness.
- RI5hb: support size `H` and primitive incidence caps give `|Delta R|<=H alpha_R`, `|Delta T|<=H alpha_+`, and `|T\T^circ|<=H alpha_-`.
- RI5hc: key-local audit cost is at most `H(alpha_R L_T+alpha_+ L_R)` and matching disturbance at most `H(alpha_R+alpha_-)`.
- RI5hd: a residual deficit `delta` leaves only support-caused unmatched roots; one touched primitive anchors at least `ceil(delta/H)` roots.

Validation: `verify_ri_support_local_collateral_churn.py` checks 2,500 systems, 59,139 key-local pairs versus 234,122 full-product pairs, 16,284 disturbed roots and 10,728 residual deficits.

Remaining: construct actual RI dependency sets and prove physical support, primitive-incidence, key-fibre and payment bounds.
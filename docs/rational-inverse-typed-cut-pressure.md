# Rational-inverse typed cut-pressure decomposition

This note refines the typed owner/charge overlap certificate on the same complete physical-source/collateral network. It turns exact shared-collateral overlap into named pressure on the canonical minimum cut.

## Contract

Let `C` be the canonical irreducible typed owner/charge core with deficit `delta>0`, split canonically as `C=A disjoint_union B`. Proper subsets are fully payable by integral flows `f_A,f_B`.

For the canonical maximum flow of `C`, let `R` be the residual-reachable set. For every original forward cut arc `e: R -> V\R`, set `p_e=f_A(e)+f_B(e)-c_e`; for every reverse crossing `e: V\R -> R`, set `p_e=-(f_A(e)+f_B(e))`. Retain owner/charge type, physical-source, collateral and arithmetic compatibility addresses.

## RI5ey--RI5fc

1. The signed cut pressures satisfy `sum_e p_e=delta`.
2. Reverse pressures are nonpositive, so positive forward pressure totals at least `delta`; some retained physical-source or collateral cut arc is over capacity under separate owner/charge payment.
3. With `m` forward cut arcs, the least maximum-pressure arc has pressure at least `ceil(delta/m)`.
4. Any arithmetic estimate making all forward pressures nonpositive, or bounding total positive pressure below `delta`, excludes the core. Otherwise the exact pressure must be charged to a named owner-source account.
5. Mixed cores preserve owner/charge type; singleton cores remain direct typed shortages. Suppressed type or retained fields, merged collateral, omitted compatibility, changed state or independent reuse is a reset.

## Consequence

A remaining RI obstruction is one direct typed shortage or one quantified physical/collateral cut-arc overload with complete owner/charge address data.

## Scope

This is conditional on the complete fixed typed network and canonical integral flows. It does not prove RI6 or the no-three-in-line conjecture.
# Orbit-phase typed cut-pressure decomposition

This note refines the irreducible residual/edit overlap certificate on the same complete shared-source network. It converts exact overlap into named pressure on the canonical minimum cut while preserving unit-sensitive type data.

## Contract

Let `C` be the canonical irreducible typed residual/edit core with deficit `delta>0`, split canonically as `C=A disjoint_union B`. Proper subsets are fully payable by integral flows `f_A,f_B`.

For the canonical maximum flow of `C`, let `R` be the residual-reachable set. On every original forward cut arc `e: R -> V\R`, set `p_e=f_A(e)+f_B(e)-c_e`; on every reverse crossing `e: V\R -> R`, set `p_e=-(f_A(e)+f_B(e))`. Retain residual/edit type, unit class, source and compatibility addresses.

## OP4ee--OP4ei

1. The signed cut pressures satisfy `sum_e p_e=delta`.
2. Reverse pressures are nonpositive, so positive forward pressure totals at least `delta`; some retained source cut arc is over capacity under separate residual/edit payment.
3. If `m` forward arcs cross the cut, the least maximum-pressure arc has pressure at least `ceil(delta/m)`.
4. Any valuation, unit or physical-source estimate making all forward pressures nonpositive, or total positive pressure below `delta`, excludes the core; otherwise the exact pressure must be charged to a named source class.
5. Mixed cores preserve residual/edit and unit fields; singleton cores remain direct typed shortages. Suppressed fields, merged sources, changed quotient state or independent capacity reuse is a reset.

## Consequence

The remaining OP obstruction is one direct typed shortage or one quantified source cut-arc overload with complete residual/edit and unit-sensitive address data.

## Scope

This is conditional on the complete fixed typed network and canonical integral flows. It does not prove OP5 or the no-three-in-line conjecture.
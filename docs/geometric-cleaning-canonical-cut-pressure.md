# Geometric-cleaning canonical cut-pressure decomposition

This note refines the irreducible cause-core overlap certificate on the same complete physical/remedy/height network. It turns exact competition into named pressure on the canonical cleaning minimum cut.

## Contract

Let `C` be the canonical irreducible cause core with deficit `delta>0`, split canonically as `C=A disjoint_union B`. Proper subsets are fully payable by integral flows `f_A,f_B`.

For the canonical maximum flow of `C`, let `R` be the residual-reachable set. On every original forward cut arc `e: R -> V\R`, set `p_e=f_A(e)+f_B(e)-c_e`; on every reverse crossing `e: V\R -> R`, set `p_e=-(f_A(e)+f_B(e))`. Retain every physical-source, remedy, height, compatibility and cause address.

## GC2kf--GC2kj

1. The signed cut pressures satisfy `sum_e p_e=delta`.
2. Reverse pressures are nonpositive, so positive forward pressure totals at least `delta` and some retained physical/remedy/height cut arc is over capacity under the two separate payments.
3. If `m` forward arcs cross the cut, the least maximum-pressure arc has pressure at least `ceil(delta/m)`.
4. A geometric or clean-height estimate proving all forward pressures nonpositive, or total positive pressure below `delta`, excludes the core; otherwise the exact pressure must be charged to a named physical or height source.
5. Singleton cause cores remain direct shortages. Omitted remedy or height arcs, merged sources, changed cleaning state, unrecorded nonlinear cost or independent capacity reuse is a reset.

## Consequence

The remaining GC obstruction is one direct cause shortage or one quantified physical/remedy/height cut-arc overload with a complete geometric address.

## Scope

This is conditional on the complete fixed network and canonical integral flows. It does not prove GC5 or the no-three-in-line conjecture.
# Superregular canonical cut-pressure decomposition

This note refines the irreducible burden-core overlap certificate on the same complete physical-source/atom network at one fixed conditioned threshold. It turns exact overlap into named pressure on the canonical minimum cut.

## Contract

Let `C` be the canonical irreducible burden core with deficit `delta>0`, split canonically as `C=A disjoint_union B`. Proper subsets are fully payable by integral flows `f_A,f_B`.

For the canonical maximum flow of `C`, let `R` be the residual-reachable set. On every original forward cut arc `e: R -> V\R`, set `p_e=f_A(e)+f_B(e)-c_e`; on every reverse crossing `e: V\R -> R`, set `p_e=-(f_A(e)+f_B(e))`. Retain every physical-source, witness-atom, burden and conditioned-threshold address.

## SRR2do--SRR2ds

1. The signed cut pressures satisfy `sum_e p_e=delta`.
2. Reverse pressures are nonpositive, so positive forward pressure totals at least `delta` and some retained physical-source or atom cut arc is over capacity under the two separate burden payments.
3. If `m` forward arcs cross the cut, the least maximum-pressure arc has pressure at least `ceil(delta/m)`.
4. A forward/reverse-load, conditioning or atom-capacity estimate proving all forward pressures nonpositive, or total positive pressure below `delta`, excludes the core; otherwise the exact pressure must be charged to a named physical source or atom budget.
5. Singleton burden cores remain direct shortages. Omitted conflicts or witnesses, merged capacities, changed threshold or independent capacity reuse is a reset.

## Consequence

The remaining SRR obstruction is one direct burden shortage or one quantified physical-source/atom cut-arc overload at the retained threshold.

## Scope

This is conditional on the complete fixed network and canonical integral flows. It does not prove SRR2, SRR4 or the no-three-in-line conjecture.
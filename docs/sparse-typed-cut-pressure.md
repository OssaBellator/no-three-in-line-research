# Sparse typed cut-pressure decomposition

This note refines the irreducible pair/completion overlap certificate on the same complete boundary-neutral physical-source/move network. It converts exact neutral-capacity overlap into named pressure on the canonical minimum cut.

## Contract

Let `C` be the canonical irreducible typed pair/completion core with deficit `delta>0`, split canonically as `C=A disjoint_union B`. Proper subsets are fully payable by integral flows `f_A,f_B`.

For the canonical maximum flow of `C`, let `R` be the residual-reachable set. On every original forward cut arc `e: R -> V\R`, set `p_e=f_A(e)+f_B(e)-c_e`; on every reverse crossing `e: V\R -> R`, set `p_e=-(f_A(e)+f_B(e))`. Retain pair/completion type, boundary coordinate, neutral-source, move and legality addresses.

## SAS5le--SAS5li

1. The signed cut pressures satisfy `sum_e p_e=delta`.
2. Reverse pressures are nonpositive, so positive forward pressure totals at least `delta`; some retained neutral-source or move cut arc is over capacity under separate pair/completion payment.
3. If `m` forward arcs cross the cut, the least maximum-pressure arc has pressure at least `ceil(delta/m)`.
4. Any shareability, legal-pair or neutral-source estimate making all forward pressures nonpositive, or total positive pressure below `delta`, excludes the core; otherwise the exact pressure must be charged to a named neutral source or move account.
5. Mixed cores preserve pair/completion and boundary data; singleton cores remain direct typed shortages. Omitted moves or tasks, changed boundary state, merged sources or independent capacity reuse is a reset.

## Consequence

The remaining SAS obstruction is one direct typed shortage or one quantified neutral-source/move cut-arc overload with complete boundary-neutral address data.

## Scope

This is conditional on the complete fixed typed network and canonical integral flows. It does not prove SAS6 or the no-three-in-line conjecture.